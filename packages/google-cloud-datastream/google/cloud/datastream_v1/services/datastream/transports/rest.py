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
from google.cloud.location import locations_pb2  # type: ignore
from google.iam.v1 import (
    iam_policy_pb2,  # type: ignore
    policy_pb2,  # type: ignore
)
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.datastream_v1._compat import transcode_request
from google.cloud.datastream_v1.types import datastream, datastream_resources

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseDatastreamRestTransport

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


class DatastreamRestInterceptor:
    """Interceptor for Datastream.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the DatastreamRestTransport.

    .. code-block:: python
        class MyCustomDatastreamInterceptor(DatastreamRestInterceptor):
            def pre_create_connection_profile(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_connection_profile(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_private_connection(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_private_connection(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_route(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_route(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_stream(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_stream(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_connection_profile(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_connection_profile(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_private_connection(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_private_connection(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_route(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_route(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_stream(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_stream(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_discover_connection_profile(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_discover_connection_profile(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_fetch_static_ips(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_fetch_static_ips(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_connection_profile(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_connection_profile(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_private_connection(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_private_connection(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_route(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_route(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_stream(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_stream(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_stream_object(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_stream_object(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_connection_profiles(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_connection_profiles(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_private_connections(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_private_connections(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_routes(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_routes(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_stream_objects(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_stream_objects(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_streams(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_streams(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_lookup_stream_object(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_lookup_stream_object(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_run_stream(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_run_stream(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_start_backfill_job(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_start_backfill_job(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_stop_backfill_job(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_stop_backfill_job(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_connection_profile(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_connection_profile(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_stream(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_stream(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = DatastreamRestTransport(interceptor=MyCustomDatastreamInterceptor())
        client = DatastreamClient(transport=transport)


    """

    def pre_create_connection_profile(
        self,
        request: datastream.CreateConnectionProfileRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datastream.CreateConnectionProfileRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_connection_profile

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Datastream server.
        """
        return request, metadata

    def post_create_connection_profile(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_connection_profile

        DEPRECATED. Please use the `post_create_connection_profile_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Datastream server but before
        it is returned to user code. This `post_create_connection_profile` interceptor runs
        before the `post_create_connection_profile_with_metadata` interceptor.
        """
        return response

    def post_create_connection_profile_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_connection_profile

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Datastream server but before it is returned to user code.

        We recommend only using this `post_create_connection_profile_with_metadata`
        interceptor in new development instead of the `post_create_connection_profile` interceptor.
        When both interceptors are used, this `post_create_connection_profile_with_metadata` interceptor runs after the
        `post_create_connection_profile` interceptor. The (possibly modified) response returned by
        `post_create_connection_profile` will be passed to
        `post_create_connection_profile_with_metadata`.
        """
        return response, metadata

    def pre_create_private_connection(
        self,
        request: datastream.CreatePrivateConnectionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datastream.CreatePrivateConnectionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_private_connection

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Datastream server.
        """
        return request, metadata

    def post_create_private_connection(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_private_connection

        DEPRECATED. Please use the `post_create_private_connection_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Datastream server but before
        it is returned to user code. This `post_create_private_connection` interceptor runs
        before the `post_create_private_connection_with_metadata` interceptor.
        """
        return response

    def post_create_private_connection_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_private_connection

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Datastream server but before it is returned to user code.

        We recommend only using this `post_create_private_connection_with_metadata`
        interceptor in new development instead of the `post_create_private_connection` interceptor.
        When both interceptors are used, this `post_create_private_connection_with_metadata` interceptor runs after the
        `post_create_private_connection` interceptor. The (possibly modified) response returned by
        `post_create_private_connection` will be passed to
        `post_create_private_connection_with_metadata`.
        """
        return response, metadata

    def pre_create_route(
        self,
        request: datastream.CreateRouteRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[datastream.CreateRouteRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_route

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Datastream server.
        """
        return request, metadata

    def post_create_route(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_route

        DEPRECATED. Please use the `post_create_route_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Datastream server but before
        it is returned to user code. This `post_create_route` interceptor runs
        before the `post_create_route_with_metadata` interceptor.
        """
        return response

    def post_create_route_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_route

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Datastream server but before it is returned to user code.

        We recommend only using this `post_create_route_with_metadata`
        interceptor in new development instead of the `post_create_route` interceptor.
        When both interceptors are used, this `post_create_route_with_metadata` interceptor runs after the
        `post_create_route` interceptor. The (possibly modified) response returned by
        `post_create_route` will be passed to
        `post_create_route_with_metadata`.
        """
        return response, metadata

    def pre_create_stream(
        self,
        request: datastream.CreateStreamRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[datastream.CreateStreamRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_stream

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Datastream server.
        """
        return request, metadata

    def post_create_stream(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_stream

        DEPRECATED. Please use the `post_create_stream_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Datastream server but before
        it is returned to user code. This `post_create_stream` interceptor runs
        before the `post_create_stream_with_metadata` interceptor.
        """
        return response

    def post_create_stream_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_stream

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Datastream server but before it is returned to user code.

        We recommend only using this `post_create_stream_with_metadata`
        interceptor in new development instead of the `post_create_stream` interceptor.
        When both interceptors are used, this `post_create_stream_with_metadata` interceptor runs after the
        `post_create_stream` interceptor. The (possibly modified) response returned by
        `post_create_stream` will be passed to
        `post_create_stream_with_metadata`.
        """
        return response, metadata

    def pre_delete_connection_profile(
        self,
        request: datastream.DeleteConnectionProfileRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datastream.DeleteConnectionProfileRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_connection_profile

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Datastream server.
        """
        return request, metadata

    def post_delete_connection_profile(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_connection_profile

        DEPRECATED. Please use the `post_delete_connection_profile_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Datastream server but before
        it is returned to user code. This `post_delete_connection_profile` interceptor runs
        before the `post_delete_connection_profile_with_metadata` interceptor.
        """
        return response

    def post_delete_connection_profile_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_connection_profile

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Datastream server but before it is returned to user code.

        We recommend only using this `post_delete_connection_profile_with_metadata`
        interceptor in new development instead of the `post_delete_connection_profile` interceptor.
        When both interceptors are used, this `post_delete_connection_profile_with_metadata` interceptor runs after the
        `post_delete_connection_profile` interceptor. The (possibly modified) response returned by
        `post_delete_connection_profile` will be passed to
        `post_delete_connection_profile_with_metadata`.
        """
        return response, metadata

    def pre_delete_private_connection(
        self,
        request: datastream.DeletePrivateConnectionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datastream.DeletePrivateConnectionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_private_connection

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Datastream server.
        """
        return request, metadata

    def post_delete_private_connection(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_private_connection

        DEPRECATED. Please use the `post_delete_private_connection_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Datastream server but before
        it is returned to user code. This `post_delete_private_connection` interceptor runs
        before the `post_delete_private_connection_with_metadata` interceptor.
        """
        return response

    def post_delete_private_connection_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_private_connection

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Datastream server but before it is returned to user code.

        We recommend only using this `post_delete_private_connection_with_metadata`
        interceptor in new development instead of the `post_delete_private_connection` interceptor.
        When both interceptors are used, this `post_delete_private_connection_with_metadata` interceptor runs after the
        `post_delete_private_connection` interceptor. The (possibly modified) response returned by
        `post_delete_private_connection` will be passed to
        `post_delete_private_connection_with_metadata`.
        """
        return response, metadata

    def pre_delete_route(
        self,
        request: datastream.DeleteRouteRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[datastream.DeleteRouteRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_route

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Datastream server.
        """
        return request, metadata

    def post_delete_route(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_route

        DEPRECATED. Please use the `post_delete_route_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Datastream server but before
        it is returned to user code. This `post_delete_route` interceptor runs
        before the `post_delete_route_with_metadata` interceptor.
        """
        return response

    def post_delete_route_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_route

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Datastream server but before it is returned to user code.

        We recommend only using this `post_delete_route_with_metadata`
        interceptor in new development instead of the `post_delete_route` interceptor.
        When both interceptors are used, this `post_delete_route_with_metadata` interceptor runs after the
        `post_delete_route` interceptor. The (possibly modified) response returned by
        `post_delete_route` will be passed to
        `post_delete_route_with_metadata`.
        """
        return response, metadata

    def pre_delete_stream(
        self,
        request: datastream.DeleteStreamRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[datastream.DeleteStreamRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_stream

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Datastream server.
        """
        return request, metadata

    def post_delete_stream(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_stream

        DEPRECATED. Please use the `post_delete_stream_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Datastream server but before
        it is returned to user code. This `post_delete_stream` interceptor runs
        before the `post_delete_stream_with_metadata` interceptor.
        """
        return response

    def post_delete_stream_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_stream

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Datastream server but before it is returned to user code.

        We recommend only using this `post_delete_stream_with_metadata`
        interceptor in new development instead of the `post_delete_stream` interceptor.
        When both interceptors are used, this `post_delete_stream_with_metadata` interceptor runs after the
        `post_delete_stream` interceptor. The (possibly modified) response returned by
        `post_delete_stream` will be passed to
        `post_delete_stream_with_metadata`.
        """
        return response, metadata

    def pre_discover_connection_profile(
        self,
        request: datastream.DiscoverConnectionProfileRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datastream.DiscoverConnectionProfileRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for discover_connection_profile

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Datastream server.
        """
        return request, metadata

    def post_discover_connection_profile(
        self, response: datastream.DiscoverConnectionProfileResponse
    ) -> datastream.DiscoverConnectionProfileResponse:
        """Post-rpc interceptor for discover_connection_profile

        DEPRECATED. Please use the `post_discover_connection_profile_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Datastream server but before
        it is returned to user code. This `post_discover_connection_profile` interceptor runs
        before the `post_discover_connection_profile_with_metadata` interceptor.
        """
        return response

    def post_discover_connection_profile_with_metadata(
        self,
        response: datastream.DiscoverConnectionProfileResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datastream.DiscoverConnectionProfileResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for discover_connection_profile

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Datastream server but before it is returned to user code.

        We recommend only using this `post_discover_connection_profile_with_metadata`
        interceptor in new development instead of the `post_discover_connection_profile` interceptor.
        When both interceptors are used, this `post_discover_connection_profile_with_metadata` interceptor runs after the
        `post_discover_connection_profile` interceptor. The (possibly modified) response returned by
        `post_discover_connection_profile` will be passed to
        `post_discover_connection_profile_with_metadata`.
        """
        return response, metadata

    def pre_fetch_static_ips(
        self,
        request: datastream.FetchStaticIpsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datastream.FetchStaticIpsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for fetch_static_ips

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Datastream server.
        """
        return request, metadata

    def post_fetch_static_ips(
        self, response: datastream.FetchStaticIpsResponse
    ) -> datastream.FetchStaticIpsResponse:
        """Post-rpc interceptor for fetch_static_ips

        DEPRECATED. Please use the `post_fetch_static_ips_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Datastream server but before
        it is returned to user code. This `post_fetch_static_ips` interceptor runs
        before the `post_fetch_static_ips_with_metadata` interceptor.
        """
        return response

    def post_fetch_static_ips_with_metadata(
        self,
        response: datastream.FetchStaticIpsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datastream.FetchStaticIpsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for fetch_static_ips

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Datastream server but before it is returned to user code.

        We recommend only using this `post_fetch_static_ips_with_metadata`
        interceptor in new development instead of the `post_fetch_static_ips` interceptor.
        When both interceptors are used, this `post_fetch_static_ips_with_metadata` interceptor runs after the
        `post_fetch_static_ips` interceptor. The (possibly modified) response returned by
        `post_fetch_static_ips` will be passed to
        `post_fetch_static_ips_with_metadata`.
        """
        return response, metadata

    def pre_get_connection_profile(
        self,
        request: datastream.GetConnectionProfileRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datastream.GetConnectionProfileRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_connection_profile

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Datastream server.
        """
        return request, metadata

    def post_get_connection_profile(
        self, response: datastream_resources.ConnectionProfile
    ) -> datastream_resources.ConnectionProfile:
        """Post-rpc interceptor for get_connection_profile

        DEPRECATED. Please use the `post_get_connection_profile_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Datastream server but before
        it is returned to user code. This `post_get_connection_profile` interceptor runs
        before the `post_get_connection_profile_with_metadata` interceptor.
        """
        return response

    def post_get_connection_profile_with_metadata(
        self,
        response: datastream_resources.ConnectionProfile,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datastream_resources.ConnectionProfile, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_connection_profile

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Datastream server but before it is returned to user code.

        We recommend only using this `post_get_connection_profile_with_metadata`
        interceptor in new development instead of the `post_get_connection_profile` interceptor.
        When both interceptors are used, this `post_get_connection_profile_with_metadata` interceptor runs after the
        `post_get_connection_profile` interceptor. The (possibly modified) response returned by
        `post_get_connection_profile` will be passed to
        `post_get_connection_profile_with_metadata`.
        """
        return response, metadata

    def pre_get_private_connection(
        self,
        request: datastream.GetPrivateConnectionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datastream.GetPrivateConnectionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_private_connection

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Datastream server.
        """
        return request, metadata

    def post_get_private_connection(
        self, response: datastream_resources.PrivateConnection
    ) -> datastream_resources.PrivateConnection:
        """Post-rpc interceptor for get_private_connection

        DEPRECATED. Please use the `post_get_private_connection_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Datastream server but before
        it is returned to user code. This `post_get_private_connection` interceptor runs
        before the `post_get_private_connection_with_metadata` interceptor.
        """
        return response

    def post_get_private_connection_with_metadata(
        self,
        response: datastream_resources.PrivateConnection,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datastream_resources.PrivateConnection, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_private_connection

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Datastream server but before it is returned to user code.

        We recommend only using this `post_get_private_connection_with_metadata`
        interceptor in new development instead of the `post_get_private_connection` interceptor.
        When both interceptors are used, this `post_get_private_connection_with_metadata` interceptor runs after the
        `post_get_private_connection` interceptor. The (possibly modified) response returned by
        `post_get_private_connection` will be passed to
        `post_get_private_connection_with_metadata`.
        """
        return response, metadata

    def pre_get_route(
        self,
        request: datastream.GetRouteRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[datastream.GetRouteRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_route

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Datastream server.
        """
        return request, metadata

    def post_get_route(
        self, response: datastream_resources.Route
    ) -> datastream_resources.Route:
        """Post-rpc interceptor for get_route

        DEPRECATED. Please use the `post_get_route_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Datastream server but before
        it is returned to user code. This `post_get_route` interceptor runs
        before the `post_get_route_with_metadata` interceptor.
        """
        return response

    def post_get_route_with_metadata(
        self,
        response: datastream_resources.Route,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[datastream_resources.Route, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_route

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Datastream server but before it is returned to user code.

        We recommend only using this `post_get_route_with_metadata`
        interceptor in new development instead of the `post_get_route` interceptor.
        When both interceptors are used, this `post_get_route_with_metadata` interceptor runs after the
        `post_get_route` interceptor. The (possibly modified) response returned by
        `post_get_route` will be passed to
        `post_get_route_with_metadata`.
        """
        return response, metadata

    def pre_get_stream(
        self,
        request: datastream.GetStreamRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[datastream.GetStreamRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_stream

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Datastream server.
        """
        return request, metadata

    def post_get_stream(
        self, response: datastream_resources.Stream
    ) -> datastream_resources.Stream:
        """Post-rpc interceptor for get_stream

        DEPRECATED. Please use the `post_get_stream_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Datastream server but before
        it is returned to user code. This `post_get_stream` interceptor runs
        before the `post_get_stream_with_metadata` interceptor.
        """
        return response

    def post_get_stream_with_metadata(
        self,
        response: datastream_resources.Stream,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[datastream_resources.Stream, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_stream

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Datastream server but before it is returned to user code.

        We recommend only using this `post_get_stream_with_metadata`
        interceptor in new development instead of the `post_get_stream` interceptor.
        When both interceptors are used, this `post_get_stream_with_metadata` interceptor runs after the
        `post_get_stream` interceptor. The (possibly modified) response returned by
        `post_get_stream` will be passed to
        `post_get_stream_with_metadata`.
        """
        return response, metadata

    def pre_get_stream_object(
        self,
        request: datastream.GetStreamObjectRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datastream.GetStreamObjectRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_stream_object

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Datastream server.
        """
        return request, metadata

    def post_get_stream_object(
        self, response: datastream_resources.StreamObject
    ) -> datastream_resources.StreamObject:
        """Post-rpc interceptor for get_stream_object

        DEPRECATED. Please use the `post_get_stream_object_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Datastream server but before
        it is returned to user code. This `post_get_stream_object` interceptor runs
        before the `post_get_stream_object_with_metadata` interceptor.
        """
        return response

    def post_get_stream_object_with_metadata(
        self,
        response: datastream_resources.StreamObject,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datastream_resources.StreamObject, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_stream_object

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Datastream server but before it is returned to user code.

        We recommend only using this `post_get_stream_object_with_metadata`
        interceptor in new development instead of the `post_get_stream_object` interceptor.
        When both interceptors are used, this `post_get_stream_object_with_metadata` interceptor runs after the
        `post_get_stream_object` interceptor. The (possibly modified) response returned by
        `post_get_stream_object` will be passed to
        `post_get_stream_object_with_metadata`.
        """
        return response, metadata

    def pre_list_connection_profiles(
        self,
        request: datastream.ListConnectionProfilesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datastream.ListConnectionProfilesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_connection_profiles

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Datastream server.
        """
        return request, metadata

    def post_list_connection_profiles(
        self, response: datastream.ListConnectionProfilesResponse
    ) -> datastream.ListConnectionProfilesResponse:
        """Post-rpc interceptor for list_connection_profiles

        DEPRECATED. Please use the `post_list_connection_profiles_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Datastream server but before
        it is returned to user code. This `post_list_connection_profiles` interceptor runs
        before the `post_list_connection_profiles_with_metadata` interceptor.
        """
        return response

    def post_list_connection_profiles_with_metadata(
        self,
        response: datastream.ListConnectionProfilesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datastream.ListConnectionProfilesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_connection_profiles

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Datastream server but before it is returned to user code.

        We recommend only using this `post_list_connection_profiles_with_metadata`
        interceptor in new development instead of the `post_list_connection_profiles` interceptor.
        When both interceptors are used, this `post_list_connection_profiles_with_metadata` interceptor runs after the
        `post_list_connection_profiles` interceptor. The (possibly modified) response returned by
        `post_list_connection_profiles` will be passed to
        `post_list_connection_profiles_with_metadata`.
        """
        return response, metadata

    def pre_list_private_connections(
        self,
        request: datastream.ListPrivateConnectionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datastream.ListPrivateConnectionsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_private_connections

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Datastream server.
        """
        return request, metadata

    def post_list_private_connections(
        self, response: datastream.ListPrivateConnectionsResponse
    ) -> datastream.ListPrivateConnectionsResponse:
        """Post-rpc interceptor for list_private_connections

        DEPRECATED. Please use the `post_list_private_connections_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Datastream server but before
        it is returned to user code. This `post_list_private_connections` interceptor runs
        before the `post_list_private_connections_with_metadata` interceptor.
        """
        return response

    def post_list_private_connections_with_metadata(
        self,
        response: datastream.ListPrivateConnectionsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datastream.ListPrivateConnectionsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_private_connections

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Datastream server but before it is returned to user code.

        We recommend only using this `post_list_private_connections_with_metadata`
        interceptor in new development instead of the `post_list_private_connections` interceptor.
        When both interceptors are used, this `post_list_private_connections_with_metadata` interceptor runs after the
        `post_list_private_connections` interceptor. The (possibly modified) response returned by
        `post_list_private_connections` will be passed to
        `post_list_private_connections_with_metadata`.
        """
        return response, metadata

    def pre_list_routes(
        self,
        request: datastream.ListRoutesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[datastream.ListRoutesRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_routes

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Datastream server.
        """
        return request, metadata

    def post_list_routes(
        self, response: datastream.ListRoutesResponse
    ) -> datastream.ListRoutesResponse:
        """Post-rpc interceptor for list_routes

        DEPRECATED. Please use the `post_list_routes_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Datastream server but before
        it is returned to user code. This `post_list_routes` interceptor runs
        before the `post_list_routes_with_metadata` interceptor.
        """
        return response

    def post_list_routes_with_metadata(
        self,
        response: datastream.ListRoutesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[datastream.ListRoutesResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_routes

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Datastream server but before it is returned to user code.

        We recommend only using this `post_list_routes_with_metadata`
        interceptor in new development instead of the `post_list_routes` interceptor.
        When both interceptors are used, this `post_list_routes_with_metadata` interceptor runs after the
        `post_list_routes` interceptor. The (possibly modified) response returned by
        `post_list_routes` will be passed to
        `post_list_routes_with_metadata`.
        """
        return response, metadata

    def pre_list_stream_objects(
        self,
        request: datastream.ListStreamObjectsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datastream.ListStreamObjectsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_stream_objects

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Datastream server.
        """
        return request, metadata

    def post_list_stream_objects(
        self, response: datastream.ListStreamObjectsResponse
    ) -> datastream.ListStreamObjectsResponse:
        """Post-rpc interceptor for list_stream_objects

        DEPRECATED. Please use the `post_list_stream_objects_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Datastream server but before
        it is returned to user code. This `post_list_stream_objects` interceptor runs
        before the `post_list_stream_objects_with_metadata` interceptor.
        """
        return response

    def post_list_stream_objects_with_metadata(
        self,
        response: datastream.ListStreamObjectsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datastream.ListStreamObjectsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_stream_objects

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Datastream server but before it is returned to user code.

        We recommend only using this `post_list_stream_objects_with_metadata`
        interceptor in new development instead of the `post_list_stream_objects` interceptor.
        When both interceptors are used, this `post_list_stream_objects_with_metadata` interceptor runs after the
        `post_list_stream_objects` interceptor. The (possibly modified) response returned by
        `post_list_stream_objects` will be passed to
        `post_list_stream_objects_with_metadata`.
        """
        return response, metadata

    def pre_list_streams(
        self,
        request: datastream.ListStreamsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[datastream.ListStreamsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_streams

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Datastream server.
        """
        return request, metadata

    def post_list_streams(
        self, response: datastream.ListStreamsResponse
    ) -> datastream.ListStreamsResponse:
        """Post-rpc interceptor for list_streams

        DEPRECATED. Please use the `post_list_streams_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Datastream server but before
        it is returned to user code. This `post_list_streams` interceptor runs
        before the `post_list_streams_with_metadata` interceptor.
        """
        return response

    def post_list_streams_with_metadata(
        self,
        response: datastream.ListStreamsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[datastream.ListStreamsResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_streams

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Datastream server but before it is returned to user code.

        We recommend only using this `post_list_streams_with_metadata`
        interceptor in new development instead of the `post_list_streams` interceptor.
        When both interceptors are used, this `post_list_streams_with_metadata` interceptor runs after the
        `post_list_streams` interceptor. The (possibly modified) response returned by
        `post_list_streams` will be passed to
        `post_list_streams_with_metadata`.
        """
        return response, metadata

    def pre_lookup_stream_object(
        self,
        request: datastream.LookupStreamObjectRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datastream.LookupStreamObjectRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for lookup_stream_object

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Datastream server.
        """
        return request, metadata

    def post_lookup_stream_object(
        self, response: datastream_resources.StreamObject
    ) -> datastream_resources.StreamObject:
        """Post-rpc interceptor for lookup_stream_object

        DEPRECATED. Please use the `post_lookup_stream_object_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Datastream server but before
        it is returned to user code. This `post_lookup_stream_object` interceptor runs
        before the `post_lookup_stream_object_with_metadata` interceptor.
        """
        return response

    def post_lookup_stream_object_with_metadata(
        self,
        response: datastream_resources.StreamObject,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datastream_resources.StreamObject, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for lookup_stream_object

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Datastream server but before it is returned to user code.

        We recommend only using this `post_lookup_stream_object_with_metadata`
        interceptor in new development instead of the `post_lookup_stream_object` interceptor.
        When both interceptors are used, this `post_lookup_stream_object_with_metadata` interceptor runs after the
        `post_lookup_stream_object` interceptor. The (possibly modified) response returned by
        `post_lookup_stream_object` will be passed to
        `post_lookup_stream_object_with_metadata`.
        """
        return response, metadata

    def pre_run_stream(
        self,
        request: datastream.RunStreamRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[datastream.RunStreamRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for run_stream

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Datastream server.
        """
        return request, metadata

    def post_run_stream(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for run_stream

        DEPRECATED. Please use the `post_run_stream_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Datastream server but before
        it is returned to user code. This `post_run_stream` interceptor runs
        before the `post_run_stream_with_metadata` interceptor.
        """
        return response

    def post_run_stream_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for run_stream

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Datastream server but before it is returned to user code.

        We recommend only using this `post_run_stream_with_metadata`
        interceptor in new development instead of the `post_run_stream` interceptor.
        When both interceptors are used, this `post_run_stream_with_metadata` interceptor runs after the
        `post_run_stream` interceptor. The (possibly modified) response returned by
        `post_run_stream` will be passed to
        `post_run_stream_with_metadata`.
        """
        return response, metadata

    def pre_start_backfill_job(
        self,
        request: datastream.StartBackfillJobRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datastream.StartBackfillJobRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for start_backfill_job

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Datastream server.
        """
        return request, metadata

    def post_start_backfill_job(
        self, response: datastream.StartBackfillJobResponse
    ) -> datastream.StartBackfillJobResponse:
        """Post-rpc interceptor for start_backfill_job

        DEPRECATED. Please use the `post_start_backfill_job_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Datastream server but before
        it is returned to user code. This `post_start_backfill_job` interceptor runs
        before the `post_start_backfill_job_with_metadata` interceptor.
        """
        return response

    def post_start_backfill_job_with_metadata(
        self,
        response: datastream.StartBackfillJobResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datastream.StartBackfillJobResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for start_backfill_job

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Datastream server but before it is returned to user code.

        We recommend only using this `post_start_backfill_job_with_metadata`
        interceptor in new development instead of the `post_start_backfill_job` interceptor.
        When both interceptors are used, this `post_start_backfill_job_with_metadata` interceptor runs after the
        `post_start_backfill_job` interceptor. The (possibly modified) response returned by
        `post_start_backfill_job` will be passed to
        `post_start_backfill_job_with_metadata`.
        """
        return response, metadata

    def pre_stop_backfill_job(
        self,
        request: datastream.StopBackfillJobRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datastream.StopBackfillJobRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for stop_backfill_job

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Datastream server.
        """
        return request, metadata

    def post_stop_backfill_job(
        self, response: datastream.StopBackfillJobResponse
    ) -> datastream.StopBackfillJobResponse:
        """Post-rpc interceptor for stop_backfill_job

        DEPRECATED. Please use the `post_stop_backfill_job_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Datastream server but before
        it is returned to user code. This `post_stop_backfill_job` interceptor runs
        before the `post_stop_backfill_job_with_metadata` interceptor.
        """
        return response

    def post_stop_backfill_job_with_metadata(
        self,
        response: datastream.StopBackfillJobResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datastream.StopBackfillJobResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for stop_backfill_job

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Datastream server but before it is returned to user code.

        We recommend only using this `post_stop_backfill_job_with_metadata`
        interceptor in new development instead of the `post_stop_backfill_job` interceptor.
        When both interceptors are used, this `post_stop_backfill_job_with_metadata` interceptor runs after the
        `post_stop_backfill_job` interceptor. The (possibly modified) response returned by
        `post_stop_backfill_job` will be passed to
        `post_stop_backfill_job_with_metadata`.
        """
        return response, metadata

    def pre_update_connection_profile(
        self,
        request: datastream.UpdateConnectionProfileRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datastream.UpdateConnectionProfileRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_connection_profile

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Datastream server.
        """
        return request, metadata

    def post_update_connection_profile(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_connection_profile

        DEPRECATED. Please use the `post_update_connection_profile_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Datastream server but before
        it is returned to user code. This `post_update_connection_profile` interceptor runs
        before the `post_update_connection_profile_with_metadata` interceptor.
        """
        return response

    def post_update_connection_profile_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_connection_profile

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Datastream server but before it is returned to user code.

        We recommend only using this `post_update_connection_profile_with_metadata`
        interceptor in new development instead of the `post_update_connection_profile` interceptor.
        When both interceptors are used, this `post_update_connection_profile_with_metadata` interceptor runs after the
        `post_update_connection_profile` interceptor. The (possibly modified) response returned by
        `post_update_connection_profile` will be passed to
        `post_update_connection_profile_with_metadata`.
        """
        return response, metadata

    def pre_update_stream(
        self,
        request: datastream.UpdateStreamRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[datastream.UpdateStreamRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_stream

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Datastream server.
        """
        return request, metadata

    def post_update_stream(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_stream

        DEPRECATED. Please use the `post_update_stream_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Datastream server but before
        it is returned to user code. This `post_update_stream` interceptor runs
        before the `post_update_stream_with_metadata` interceptor.
        """
        return response

    def post_update_stream_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_stream

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Datastream server but before it is returned to user code.

        We recommend only using this `post_update_stream_with_metadata`
        interceptor in new development instead of the `post_update_stream` interceptor.
        When both interceptors are used, this `post_update_stream_with_metadata` interceptor runs after the
        `post_update_stream` interceptor. The (possibly modified) response returned by
        `post_update_stream` will be passed to
        `post_update_stream_with_metadata`.
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
        before they are sent to the Datastream server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the Datastream server but before
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
        before they are sent to the Datastream server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the Datastream server but before
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
        before they are sent to the Datastream server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the Datastream server but before
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
        before they are sent to the Datastream server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the Datastream server but before
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
        before they are sent to the Datastream server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the Datastream server but before
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
        before they are sent to the Datastream server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the Datastream server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class DatastreamRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: DatastreamRestInterceptor


class DatastreamRestTransport(_BaseDatastreamRestTransport):
    """REST backend synchronous transport for Datastream.

    Datastream service

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "datastream.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[DatastreamRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'datastream.googleapis.com').
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
            interceptor (Optional[DatastreamRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or DatastreamRestInterceptor()
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
                ],
                "google.longrunning.Operations.DeleteOperation": [
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.GetOperation": [
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.ListOperations": [
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*}/operations",
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

    class _CreateConnectionProfile(
        _BaseDatastreamRestTransport._BaseCreateConnectionProfile, DatastreamRestStub
    ):
        def __hash__(self):
            return hash("DatastreamRestTransport.CreateConnectionProfile")

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
            request: datastream.CreateConnectionProfileRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create connection profile method over HTTP.

            Args:
                request (~.datastream.CreateConnectionProfileRequest):
                    The request object. Request message for creating a
                connection profile.
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

            http_options = _BaseDatastreamRestTransport._BaseCreateConnectionProfile._get_http_options()
            request, metadata = self._interceptor.pre_create_connection_profile(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDatastreamRestTransport._BaseCreateConnectionProfile,
                    "_BaseCreateConnectionProfile__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.datastream_v1.DatastreamClient.CreateConnectionProfile",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
                        "rpcName": "CreateConnectionProfile",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DatastreamRestTransport._CreateConnectionProfile._get_response(
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

            resp = self._interceptor.post_create_connection_profile(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_connection_profile_with_metadata(
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
                    "Received response for google.cloud.datastream_v1.DatastreamClient.create_connection_profile",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
                        "rpcName": "CreateConnectionProfile",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreatePrivateConnection(
        _BaseDatastreamRestTransport._BaseCreatePrivateConnection, DatastreamRestStub
    ):
        def __hash__(self):
            return hash("DatastreamRestTransport.CreatePrivateConnection")

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
            request: datastream.CreatePrivateConnectionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create private connection method over HTTP.

            Args:
                request (~.datastream.CreatePrivateConnectionRequest):
                    The request object. Request for creating a private
                connection.
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

            http_options = _BaseDatastreamRestTransport._BaseCreatePrivateConnection._get_http_options()
            request, metadata = self._interceptor.pre_create_private_connection(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDatastreamRestTransport._BaseCreatePrivateConnection,
                    "_BaseCreatePrivateConnection__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.datastream_v1.DatastreamClient.CreatePrivateConnection",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
                        "rpcName": "CreatePrivateConnection",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DatastreamRestTransport._CreatePrivateConnection._get_response(
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

            resp = self._interceptor.post_create_private_connection(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_private_connection_with_metadata(
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
                    "Received response for google.cloud.datastream_v1.DatastreamClient.create_private_connection",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
                        "rpcName": "CreatePrivateConnection",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateRoute(
        _BaseDatastreamRestTransport._BaseCreateRoute, DatastreamRestStub
    ):
        def __hash__(self):
            return hash("DatastreamRestTransport.CreateRoute")

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
            request: datastream.CreateRouteRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create route method over HTTP.

            Args:
                request (~.datastream.CreateRouteRequest):
                    The request object. Route creation request.
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
                _BaseDatastreamRestTransport._BaseCreateRoute._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_route(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDatastreamRestTransport._BaseCreateRoute,
                    "_BaseCreateRoute__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.datastream_v1.DatastreamClient.CreateRoute",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
                        "rpcName": "CreateRoute",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DatastreamRestTransport._CreateRoute._get_response(
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

            resp = self._interceptor.post_create_route(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_route_with_metadata(
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
                    "Received response for google.cloud.datastream_v1.DatastreamClient.create_route",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
                        "rpcName": "CreateRoute",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateStream(
        _BaseDatastreamRestTransport._BaseCreateStream, DatastreamRestStub
    ):
        def __hash__(self):
            return hash("DatastreamRestTransport.CreateStream")

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
            request: datastream.CreateStreamRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create stream method over HTTP.

            Args:
                request (~.datastream.CreateStreamRequest):
                    The request object. Request message for creating a
                stream.
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
                _BaseDatastreamRestTransport._BaseCreateStream._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_stream(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDatastreamRestTransport._BaseCreateStream,
                    "_BaseCreateStream__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.datastream_v1.DatastreamClient.CreateStream",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
                        "rpcName": "CreateStream",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DatastreamRestTransport._CreateStream._get_response(
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

            resp = self._interceptor.post_create_stream(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_stream_with_metadata(
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
                    "Received response for google.cloud.datastream_v1.DatastreamClient.create_stream",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
                        "rpcName": "CreateStream",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteConnectionProfile(
        _BaseDatastreamRestTransport._BaseDeleteConnectionProfile, DatastreamRestStub
    ):
        def __hash__(self):
            return hash("DatastreamRestTransport.DeleteConnectionProfile")

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
            request: datastream.DeleteConnectionProfileRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete connection profile method over HTTP.

            Args:
                request (~.datastream.DeleteConnectionProfileRequest):
                    The request object. Request message for deleting a
                connection profile.
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

            http_options = _BaseDatastreamRestTransport._BaseDeleteConnectionProfile._get_http_options()
            request, metadata = self._interceptor.pre_delete_connection_profile(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDatastreamRestTransport._BaseDeleteConnectionProfile,
                    "_BaseDeleteConnectionProfile__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.datastream_v1.DatastreamClient.DeleteConnectionProfile",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
                        "rpcName": "DeleteConnectionProfile",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DatastreamRestTransport._DeleteConnectionProfile._get_response(
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

            resp = self._interceptor.post_delete_connection_profile(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_connection_profile_with_metadata(
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
                    "Received response for google.cloud.datastream_v1.DatastreamClient.delete_connection_profile",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
                        "rpcName": "DeleteConnectionProfile",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeletePrivateConnection(
        _BaseDatastreamRestTransport._BaseDeletePrivateConnection, DatastreamRestStub
    ):
        def __hash__(self):
            return hash("DatastreamRestTransport.DeletePrivateConnection")

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
            request: datastream.DeletePrivateConnectionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete private connection method over HTTP.

            Args:
                request (~.datastream.DeletePrivateConnectionRequest):
                    The request object. Request to delete a private
                connection.
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

            http_options = _BaseDatastreamRestTransport._BaseDeletePrivateConnection._get_http_options()
            request, metadata = self._interceptor.pre_delete_private_connection(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDatastreamRestTransport._BaseDeletePrivateConnection,
                    "_BaseDeletePrivateConnection__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.datastream_v1.DatastreamClient.DeletePrivateConnection",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
                        "rpcName": "DeletePrivateConnection",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DatastreamRestTransport._DeletePrivateConnection._get_response(
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

            resp = self._interceptor.post_delete_private_connection(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_private_connection_with_metadata(
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
                    "Received response for google.cloud.datastream_v1.DatastreamClient.delete_private_connection",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
                        "rpcName": "DeletePrivateConnection",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteRoute(
        _BaseDatastreamRestTransport._BaseDeleteRoute, DatastreamRestStub
    ):
        def __hash__(self):
            return hash("DatastreamRestTransport.DeleteRoute")

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
            request: datastream.DeleteRouteRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete route method over HTTP.

            Args:
                request (~.datastream.DeleteRouteRequest):
                    The request object. Route deletion request.
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
                _BaseDatastreamRestTransport._BaseDeleteRoute._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_route(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDatastreamRestTransport._BaseDeleteRoute,
                    "_BaseDeleteRoute__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.datastream_v1.DatastreamClient.DeleteRoute",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
                        "rpcName": "DeleteRoute",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DatastreamRestTransport._DeleteRoute._get_response(
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

            resp = self._interceptor.post_delete_route(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_route_with_metadata(
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
                    "Received response for google.cloud.datastream_v1.DatastreamClient.delete_route",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
                        "rpcName": "DeleteRoute",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteStream(
        _BaseDatastreamRestTransport._BaseDeleteStream, DatastreamRestStub
    ):
        def __hash__(self):
            return hash("DatastreamRestTransport.DeleteStream")

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
            request: datastream.DeleteStreamRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete stream method over HTTP.

            Args:
                request (~.datastream.DeleteStreamRequest):
                    The request object. Request message for deleting a
                stream.
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
                _BaseDatastreamRestTransport._BaseDeleteStream._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_stream(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDatastreamRestTransport._BaseDeleteStream,
                    "_BaseDeleteStream__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.datastream_v1.DatastreamClient.DeleteStream",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
                        "rpcName": "DeleteStream",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DatastreamRestTransport._DeleteStream._get_response(
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

            resp = self._interceptor.post_delete_stream(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_stream_with_metadata(
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
                    "Received response for google.cloud.datastream_v1.DatastreamClient.delete_stream",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
                        "rpcName": "DeleteStream",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DiscoverConnectionProfile(
        _BaseDatastreamRestTransport._BaseDiscoverConnectionProfile, DatastreamRestStub
    ):
        def __hash__(self):
            return hash("DatastreamRestTransport.DiscoverConnectionProfile")

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
            request: datastream.DiscoverConnectionProfileRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> datastream.DiscoverConnectionProfileResponse:
            r"""Call the discover connection
            profile method over HTTP.

                Args:
                    request (~.datastream.DiscoverConnectionProfileRequest):
                        The request object. Request message for 'discover'
                    ConnectionProfile request.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.datastream.DiscoverConnectionProfileResponse:
                        Response from a discover request.
            """

            http_options = _BaseDatastreamRestTransport._BaseDiscoverConnectionProfile._get_http_options()
            request, metadata = self._interceptor.pre_discover_connection_profile(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDatastreamRestTransport._BaseDiscoverConnectionProfile,
                    "_BaseDiscoverConnectionProfile__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.datastream_v1.DatastreamClient.DiscoverConnectionProfile",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
                        "rpcName": "DiscoverConnectionProfile",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DatastreamRestTransport._DiscoverConnectionProfile._get_response(
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
            resp = datastream.DiscoverConnectionProfileResponse()
            pb_resp = datastream.DiscoverConnectionProfileResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_discover_connection_profile(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_discover_connection_profile_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        datastream.DiscoverConnectionProfileResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.datastream_v1.DatastreamClient.discover_connection_profile",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
                        "rpcName": "DiscoverConnectionProfile",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _FetchStaticIps(
        _BaseDatastreamRestTransport._BaseFetchStaticIps, DatastreamRestStub
    ):
        def __hash__(self):
            return hash("DatastreamRestTransport.FetchStaticIps")

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
            request: datastream.FetchStaticIpsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> datastream.FetchStaticIpsResponse:
            r"""Call the fetch static ips method over HTTP.

            Args:
                request (~.datastream.FetchStaticIpsRequest):
                    The request object. Request message for 'FetchStaticIps'
                request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.datastream.FetchStaticIpsResponse:
                    Response message for a
                'FetchStaticIps' response.

            """

            http_options = (
                _BaseDatastreamRestTransport._BaseFetchStaticIps._get_http_options()
            )
            request, metadata = self._interceptor.pre_fetch_static_ips(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDatastreamRestTransport._BaseFetchStaticIps,
                    "_BaseFetchStaticIps__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.datastream_v1.DatastreamClient.FetchStaticIps",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
                        "rpcName": "FetchStaticIps",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DatastreamRestTransport._FetchStaticIps._get_response(
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
            resp = datastream.FetchStaticIpsResponse()
            pb_resp = datastream.FetchStaticIpsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_fetch_static_ips(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_fetch_static_ips_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = datastream.FetchStaticIpsResponse.to_json(
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
                    "Received response for google.cloud.datastream_v1.DatastreamClient.fetch_static_ips",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
                        "rpcName": "FetchStaticIps",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetConnectionProfile(
        _BaseDatastreamRestTransport._BaseGetConnectionProfile, DatastreamRestStub
    ):
        def __hash__(self):
            return hash("DatastreamRestTransport.GetConnectionProfile")

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
            request: datastream.GetConnectionProfileRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> datastream_resources.ConnectionProfile:
            r"""Call the get connection profile method over HTTP.

            Args:
                request (~.datastream.GetConnectionProfileRequest):
                    The request object. Request message for getting a
                connection profile.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.datastream_resources.ConnectionProfile:
                    A set of reusable connection
                configurations to be used as a source or
                destination for a stream.

            """

            http_options = _BaseDatastreamRestTransport._BaseGetConnectionProfile._get_http_options()
            request, metadata = self._interceptor.pre_get_connection_profile(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDatastreamRestTransport._BaseGetConnectionProfile,
                    "_BaseGetConnectionProfile__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.datastream_v1.DatastreamClient.GetConnectionProfile",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
                        "rpcName": "GetConnectionProfile",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DatastreamRestTransport._GetConnectionProfile._get_response(
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
            resp = datastream_resources.ConnectionProfile()
            pb_resp = datastream_resources.ConnectionProfile.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_connection_profile(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_connection_profile_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = datastream_resources.ConnectionProfile.to_json(
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
                    "Received response for google.cloud.datastream_v1.DatastreamClient.get_connection_profile",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
                        "rpcName": "GetConnectionProfile",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetPrivateConnection(
        _BaseDatastreamRestTransport._BaseGetPrivateConnection, DatastreamRestStub
    ):
        def __hash__(self):
            return hash("DatastreamRestTransport.GetPrivateConnection")

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
            request: datastream.GetPrivateConnectionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> datastream_resources.PrivateConnection:
            r"""Call the get private connection method over HTTP.

            Args:
                request (~.datastream.GetPrivateConnectionRequest):
                    The request object. Request to get a private connection
                configuration.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.datastream_resources.PrivateConnection:
                    The PrivateConnection resource is
                used to establish private connectivity
                between Datastream and a customer's
                network.

            """

            http_options = _BaseDatastreamRestTransport._BaseGetPrivateConnection._get_http_options()
            request, metadata = self._interceptor.pre_get_private_connection(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDatastreamRestTransport._BaseGetPrivateConnection,
                    "_BaseGetPrivateConnection__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.datastream_v1.DatastreamClient.GetPrivateConnection",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
                        "rpcName": "GetPrivateConnection",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DatastreamRestTransport._GetPrivateConnection._get_response(
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
            resp = datastream_resources.PrivateConnection()
            pb_resp = datastream_resources.PrivateConnection.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_private_connection(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_private_connection_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = datastream_resources.PrivateConnection.to_json(
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
                    "Received response for google.cloud.datastream_v1.DatastreamClient.get_private_connection",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
                        "rpcName": "GetPrivateConnection",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetRoute(_BaseDatastreamRestTransport._BaseGetRoute, DatastreamRestStub):
        def __hash__(self):
            return hash("DatastreamRestTransport.GetRoute")

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
            request: datastream.GetRouteRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> datastream_resources.Route:
            r"""Call the get route method over HTTP.

            Args:
                request (~.datastream.GetRouteRequest):
                    The request object. Route get request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.datastream_resources.Route:
                    The route resource is the child of
                the private connection resource, used
                for defining a route for a private
                connection.

            """

            http_options = (
                _BaseDatastreamRestTransport._BaseGetRoute._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_route(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDatastreamRestTransport._BaseGetRoute,
                    "_BaseGetRoute__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.datastream_v1.DatastreamClient.GetRoute",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
                        "rpcName": "GetRoute",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DatastreamRestTransport._GetRoute._get_response(
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
            resp = datastream_resources.Route()
            pb_resp = datastream_resources.Route.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_route(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_route_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = datastream_resources.Route.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.datastream_v1.DatastreamClient.get_route",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
                        "rpcName": "GetRoute",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetStream(_BaseDatastreamRestTransport._BaseGetStream, DatastreamRestStub):
        def __hash__(self):
            return hash("DatastreamRestTransport.GetStream")

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
            request: datastream.GetStreamRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> datastream_resources.Stream:
            r"""Call the get stream method over HTTP.

            Args:
                request (~.datastream.GetStreamRequest):
                    The request object. Request message for getting a stream.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.datastream_resources.Stream:
                    A resource representing streaming
                data from a source to a destination.

            """

            http_options = (
                _BaseDatastreamRestTransport._BaseGetStream._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_stream(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDatastreamRestTransport._BaseGetStream,
                    "_BaseGetStream__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.datastream_v1.DatastreamClient.GetStream",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
                        "rpcName": "GetStream",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DatastreamRestTransport._GetStream._get_response(
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
            resp = datastream_resources.Stream()
            pb_resp = datastream_resources.Stream.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_stream(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_stream_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = datastream_resources.Stream.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.datastream_v1.DatastreamClient.get_stream",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
                        "rpcName": "GetStream",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetStreamObject(
        _BaseDatastreamRestTransport._BaseGetStreamObject, DatastreamRestStub
    ):
        def __hash__(self):
            return hash("DatastreamRestTransport.GetStreamObject")

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
            request: datastream.GetStreamObjectRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> datastream_resources.StreamObject:
            r"""Call the get stream object method over HTTP.

            Args:
                request (~.datastream.GetStreamObjectRequest):
                    The request object. Request for fetching a specific
                stream object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.datastream_resources.StreamObject:
                    A specific stream object (e.g a
                specific DB table).

            """

            http_options = (
                _BaseDatastreamRestTransport._BaseGetStreamObject._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_stream_object(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDatastreamRestTransport._BaseGetStreamObject,
                    "_BaseGetStreamObject__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.datastream_v1.DatastreamClient.GetStreamObject",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
                        "rpcName": "GetStreamObject",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DatastreamRestTransport._GetStreamObject._get_response(
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
            resp = datastream_resources.StreamObject()
            pb_resp = datastream_resources.StreamObject.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_stream_object(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_stream_object_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = datastream_resources.StreamObject.to_json(
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
                    "Received response for google.cloud.datastream_v1.DatastreamClient.get_stream_object",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
                        "rpcName": "GetStreamObject",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListConnectionProfiles(
        _BaseDatastreamRestTransport._BaseListConnectionProfiles, DatastreamRestStub
    ):
        def __hash__(self):
            return hash("DatastreamRestTransport.ListConnectionProfiles")

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
            request: datastream.ListConnectionProfilesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> datastream.ListConnectionProfilesResponse:
            r"""Call the list connection profiles method over HTTP.

            Args:
                request (~.datastream.ListConnectionProfilesRequest):
                    The request object. Request message for listing
                connection profiles.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.datastream.ListConnectionProfilesResponse:
                    Response message for listing
                connection profiles.

            """

            http_options = _BaseDatastreamRestTransport._BaseListConnectionProfiles._get_http_options()
            request, metadata = self._interceptor.pre_list_connection_profiles(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDatastreamRestTransport._BaseListConnectionProfiles,
                    "_BaseListConnectionProfiles__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.datastream_v1.DatastreamClient.ListConnectionProfiles",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
                        "rpcName": "ListConnectionProfiles",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DatastreamRestTransport._ListConnectionProfiles._get_response(
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
            resp = datastream.ListConnectionProfilesResponse()
            pb_resp = datastream.ListConnectionProfilesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_connection_profiles(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_connection_profiles_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        datastream.ListConnectionProfilesResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.datastream_v1.DatastreamClient.list_connection_profiles",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
                        "rpcName": "ListConnectionProfiles",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListPrivateConnections(
        _BaseDatastreamRestTransport._BaseListPrivateConnections, DatastreamRestStub
    ):
        def __hash__(self):
            return hash("DatastreamRestTransport.ListPrivateConnections")

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
            request: datastream.ListPrivateConnectionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> datastream.ListPrivateConnectionsResponse:
            r"""Call the list private connections method over HTTP.

            Args:
                request (~.datastream.ListPrivateConnectionsRequest):
                    The request object. Request for listing private
                connections.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.datastream.ListPrivateConnectionsResponse:
                    Response containing a list of private
                connection configurations.

            """

            http_options = _BaseDatastreamRestTransport._BaseListPrivateConnections._get_http_options()
            request, metadata = self._interceptor.pre_list_private_connections(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDatastreamRestTransport._BaseListPrivateConnections,
                    "_BaseListPrivateConnections__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.datastream_v1.DatastreamClient.ListPrivateConnections",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
                        "rpcName": "ListPrivateConnections",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DatastreamRestTransport._ListPrivateConnections._get_response(
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
            resp = datastream.ListPrivateConnectionsResponse()
            pb_resp = datastream.ListPrivateConnectionsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_private_connections(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_private_connections_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        datastream.ListPrivateConnectionsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.datastream_v1.DatastreamClient.list_private_connections",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
                        "rpcName": "ListPrivateConnections",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListRoutes(_BaseDatastreamRestTransport._BaseListRoutes, DatastreamRestStub):
        def __hash__(self):
            return hash("DatastreamRestTransport.ListRoutes")

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
            request: datastream.ListRoutesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> datastream.ListRoutesResponse:
            r"""Call the list routes method over HTTP.

            Args:
                request (~.datastream.ListRoutesRequest):
                    The request object. Route list request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.datastream.ListRoutesResponse:
                    Route list response.
            """

            http_options = (
                _BaseDatastreamRestTransport._BaseListRoutes._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_routes(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDatastreamRestTransport._BaseListRoutes,
                    "_BaseListRoutes__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.datastream_v1.DatastreamClient.ListRoutes",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
                        "rpcName": "ListRoutes",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DatastreamRestTransport._ListRoutes._get_response(
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
            resp = datastream.ListRoutesResponse()
            pb_resp = datastream.ListRoutesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_routes(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_routes_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = datastream.ListRoutesResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.datastream_v1.DatastreamClient.list_routes",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
                        "rpcName": "ListRoutes",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListStreamObjects(
        _BaseDatastreamRestTransport._BaseListStreamObjects, DatastreamRestStub
    ):
        def __hash__(self):
            return hash("DatastreamRestTransport.ListStreamObjects")

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
            request: datastream.ListStreamObjectsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> datastream.ListStreamObjectsResponse:
            r"""Call the list stream objects method over HTTP.

            Args:
                request (~.datastream.ListStreamObjectsRequest):
                    The request object. Request for listing all objects for a
                specific stream.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.datastream.ListStreamObjectsResponse:
                    Response containing the objects for a
                stream.

            """

            http_options = (
                _BaseDatastreamRestTransport._BaseListStreamObjects._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_stream_objects(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDatastreamRestTransport._BaseListStreamObjects,
                    "_BaseListStreamObjects__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.datastream_v1.DatastreamClient.ListStreamObjects",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
                        "rpcName": "ListStreamObjects",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DatastreamRestTransport._ListStreamObjects._get_response(
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
            resp = datastream.ListStreamObjectsResponse()
            pb_resp = datastream.ListStreamObjectsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_stream_objects(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_stream_objects_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = datastream.ListStreamObjectsResponse.to_json(
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
                    "Received response for google.cloud.datastream_v1.DatastreamClient.list_stream_objects",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
                        "rpcName": "ListStreamObjects",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListStreams(
        _BaseDatastreamRestTransport._BaseListStreams, DatastreamRestStub
    ):
        def __hash__(self):
            return hash("DatastreamRestTransport.ListStreams")

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
            request: datastream.ListStreamsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> datastream.ListStreamsResponse:
            r"""Call the list streams method over HTTP.

            Args:
                request (~.datastream.ListStreamsRequest):
                    The request object. Request message for listing streams.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.datastream.ListStreamsResponse:
                    Response message for listing streams.
            """

            http_options = (
                _BaseDatastreamRestTransport._BaseListStreams._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_streams(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDatastreamRestTransport._BaseListStreams,
                    "_BaseListStreams__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.datastream_v1.DatastreamClient.ListStreams",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
                        "rpcName": "ListStreams",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DatastreamRestTransport._ListStreams._get_response(
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
            resp = datastream.ListStreamsResponse()
            pb_resp = datastream.ListStreamsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_streams(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_streams_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = datastream.ListStreamsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.datastream_v1.DatastreamClient.list_streams",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
                        "rpcName": "ListStreams",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _LookupStreamObject(
        _BaseDatastreamRestTransport._BaseLookupStreamObject, DatastreamRestStub
    ):
        def __hash__(self):
            return hash("DatastreamRestTransport.LookupStreamObject")

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
            request: datastream.LookupStreamObjectRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> datastream_resources.StreamObject:
            r"""Call the lookup stream object method over HTTP.

            Args:
                request (~.datastream.LookupStreamObjectRequest):
                    The request object. Request for looking up a specific
                stream object by its source object
                identifier.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.datastream_resources.StreamObject:
                    A specific stream object (e.g a
                specific DB table).

            """

            http_options = (
                _BaseDatastreamRestTransport._BaseLookupStreamObject._get_http_options()
            )
            request, metadata = self._interceptor.pre_lookup_stream_object(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDatastreamRestTransport._BaseLookupStreamObject,
                    "_BaseLookupStreamObject__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.datastream_v1.DatastreamClient.LookupStreamObject",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
                        "rpcName": "LookupStreamObject",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DatastreamRestTransport._LookupStreamObject._get_response(
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
            resp = datastream_resources.StreamObject()
            pb_resp = datastream_resources.StreamObject.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_lookup_stream_object(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_lookup_stream_object_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = datastream_resources.StreamObject.to_json(
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
                    "Received response for google.cloud.datastream_v1.DatastreamClient.lookup_stream_object",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
                        "rpcName": "LookupStreamObject",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RunStream(_BaseDatastreamRestTransport._BaseRunStream, DatastreamRestStub):
        def __hash__(self):
            return hash("DatastreamRestTransport.RunStream")

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
            request: datastream.RunStreamRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the run stream method over HTTP.

            Args:
                request (~.datastream.RunStreamRequest):
                    The request object. Request message for running a stream.
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
                _BaseDatastreamRestTransport._BaseRunStream._get_http_options()
            )
            request, metadata = self._interceptor.pre_run_stream(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDatastreamRestTransport._BaseRunStream,
                    "_BaseRunStream__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.datastream_v1.DatastreamClient.RunStream",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
                        "rpcName": "RunStream",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DatastreamRestTransport._RunStream._get_response(
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

            resp = self._interceptor.post_run_stream(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_run_stream_with_metadata(
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
                    "Received response for google.cloud.datastream_v1.DatastreamClient.run_stream",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
                        "rpcName": "RunStream",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _StartBackfillJob(
        _BaseDatastreamRestTransport._BaseStartBackfillJob, DatastreamRestStub
    ):
        def __hash__(self):
            return hash("DatastreamRestTransport.StartBackfillJob")

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
            request: datastream.StartBackfillJobRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> datastream.StartBackfillJobResponse:
            r"""Call the start backfill job method over HTTP.

            Args:
                request (~.datastream.StartBackfillJobRequest):
                    The request object. Request for manually initiating a
                backfill job for a specific stream
                object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.datastream.StartBackfillJobResponse:
                    Response for manually initiating a
                backfill job for a specific stream
                object.

            """

            http_options = (
                _BaseDatastreamRestTransport._BaseStartBackfillJob._get_http_options()
            )
            request, metadata = self._interceptor.pre_start_backfill_job(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDatastreamRestTransport._BaseStartBackfillJob,
                    "_BaseStartBackfillJob__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.datastream_v1.DatastreamClient.StartBackfillJob",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
                        "rpcName": "StartBackfillJob",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DatastreamRestTransport._StartBackfillJob._get_response(
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
            resp = datastream.StartBackfillJobResponse()
            pb_resp = datastream.StartBackfillJobResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_start_backfill_job(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_start_backfill_job_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = datastream.StartBackfillJobResponse.to_json(
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
                    "Received response for google.cloud.datastream_v1.DatastreamClient.start_backfill_job",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
                        "rpcName": "StartBackfillJob",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _StopBackfillJob(
        _BaseDatastreamRestTransport._BaseStopBackfillJob, DatastreamRestStub
    ):
        def __hash__(self):
            return hash("DatastreamRestTransport.StopBackfillJob")

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
            request: datastream.StopBackfillJobRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> datastream.StopBackfillJobResponse:
            r"""Call the stop backfill job method over HTTP.

            Args:
                request (~.datastream.StopBackfillJobRequest):
                    The request object. Request for manually stopping a
                running backfill job for a specific
                stream object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.datastream.StopBackfillJobResponse:
                    Response for manually stop a backfill
                job for a specific stream object.

            """

            http_options = (
                _BaseDatastreamRestTransport._BaseStopBackfillJob._get_http_options()
            )
            request, metadata = self._interceptor.pre_stop_backfill_job(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDatastreamRestTransport._BaseStopBackfillJob,
                    "_BaseStopBackfillJob__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.datastream_v1.DatastreamClient.StopBackfillJob",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
                        "rpcName": "StopBackfillJob",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DatastreamRestTransport._StopBackfillJob._get_response(
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
            resp = datastream.StopBackfillJobResponse()
            pb_resp = datastream.StopBackfillJobResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_stop_backfill_job(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_stop_backfill_job_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = datastream.StopBackfillJobResponse.to_json(
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
                    "Received response for google.cloud.datastream_v1.DatastreamClient.stop_backfill_job",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
                        "rpcName": "StopBackfillJob",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateConnectionProfile(
        _BaseDatastreamRestTransport._BaseUpdateConnectionProfile, DatastreamRestStub
    ):
        def __hash__(self):
            return hash("DatastreamRestTransport.UpdateConnectionProfile")

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
            request: datastream.UpdateConnectionProfileRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update connection profile method over HTTP.

            Args:
                request (~.datastream.UpdateConnectionProfileRequest):
                    The request object. Connection profile update message.
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

            http_options = _BaseDatastreamRestTransport._BaseUpdateConnectionProfile._get_http_options()
            request, metadata = self._interceptor.pre_update_connection_profile(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDatastreamRestTransport._BaseUpdateConnectionProfile,
                    "_BaseUpdateConnectionProfile__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.datastream_v1.DatastreamClient.UpdateConnectionProfile",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
                        "rpcName": "UpdateConnectionProfile",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DatastreamRestTransport._UpdateConnectionProfile._get_response(
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

            resp = self._interceptor.post_update_connection_profile(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_connection_profile_with_metadata(
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
                    "Received response for google.cloud.datastream_v1.DatastreamClient.update_connection_profile",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
                        "rpcName": "UpdateConnectionProfile",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateStream(
        _BaseDatastreamRestTransport._BaseUpdateStream, DatastreamRestStub
    ):
        def __hash__(self):
            return hash("DatastreamRestTransport.UpdateStream")

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
            request: datastream.UpdateStreamRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update stream method over HTTP.

            Args:
                request (~.datastream.UpdateStreamRequest):
                    The request object. Request message for updating a
                stream.
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
                _BaseDatastreamRestTransport._BaseUpdateStream._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_stream(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDatastreamRestTransport._BaseUpdateStream,
                    "_BaseUpdateStream__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.datastream_v1.DatastreamClient.UpdateStream",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
                        "rpcName": "UpdateStream",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DatastreamRestTransport._UpdateStream._get_response(
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

            resp = self._interceptor.post_update_stream(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_stream_with_metadata(
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
                    "Received response for google.cloud.datastream_v1.DatastreamClient.update_stream",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
                        "rpcName": "UpdateStream",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_connection_profile(
        self,
    ) -> Callable[
        [datastream.CreateConnectionProfileRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateConnectionProfile(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_private_connection(
        self,
    ) -> Callable[
        [datastream.CreatePrivateConnectionRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreatePrivateConnection(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_route(
        self,
    ) -> Callable[[datastream.CreateRouteRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateRoute(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_stream(
        self,
    ) -> Callable[[datastream.CreateStreamRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateStream(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_connection_profile(
        self,
    ) -> Callable[
        [datastream.DeleteConnectionProfileRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteConnectionProfile(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_private_connection(
        self,
    ) -> Callable[
        [datastream.DeletePrivateConnectionRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeletePrivateConnection(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_route(
        self,
    ) -> Callable[[datastream.DeleteRouteRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteRoute(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_stream(
        self,
    ) -> Callable[[datastream.DeleteStreamRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteStream(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def discover_connection_profile(
        self,
    ) -> Callable[
        [datastream.DiscoverConnectionProfileRequest],
        datastream.DiscoverConnectionProfileResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DiscoverConnectionProfile(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def fetch_static_ips(
        self,
    ) -> Callable[
        [datastream.FetchStaticIpsRequest], datastream.FetchStaticIpsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._FetchStaticIps(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_connection_profile(
        self,
    ) -> Callable[
        [datastream.GetConnectionProfileRequest], datastream_resources.ConnectionProfile
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetConnectionProfile(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_private_connection(
        self,
    ) -> Callable[
        [datastream.GetPrivateConnectionRequest], datastream_resources.PrivateConnection
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetPrivateConnection(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_route(
        self,
    ) -> Callable[[datastream.GetRouteRequest], datastream_resources.Route]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetRoute(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_stream(
        self,
    ) -> Callable[[datastream.GetStreamRequest], datastream_resources.Stream]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetStream(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_stream_object(
        self,
    ) -> Callable[
        [datastream.GetStreamObjectRequest], datastream_resources.StreamObject
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetStreamObject(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_connection_profiles(
        self,
    ) -> Callable[
        [datastream.ListConnectionProfilesRequest],
        datastream.ListConnectionProfilesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListConnectionProfiles(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_private_connections(
        self,
    ) -> Callable[
        [datastream.ListPrivateConnectionsRequest],
        datastream.ListPrivateConnectionsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListPrivateConnections(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_routes(
        self,
    ) -> Callable[[datastream.ListRoutesRequest], datastream.ListRoutesResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListRoutes(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_stream_objects(
        self,
    ) -> Callable[
        [datastream.ListStreamObjectsRequest], datastream.ListStreamObjectsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListStreamObjects(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_streams(
        self,
    ) -> Callable[[datastream.ListStreamsRequest], datastream.ListStreamsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListStreams(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def lookup_stream_object(
        self,
    ) -> Callable[
        [datastream.LookupStreamObjectRequest], datastream_resources.StreamObject
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._LookupStreamObject(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def run_stream(
        self,
    ) -> Callable[[datastream.RunStreamRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RunStream(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def start_backfill_job(
        self,
    ) -> Callable[
        [datastream.StartBackfillJobRequest], datastream.StartBackfillJobResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._StartBackfillJob(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def stop_backfill_job(
        self,
    ) -> Callable[
        [datastream.StopBackfillJobRequest], datastream.StopBackfillJobResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._StopBackfillJob(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_connection_profile(
        self,
    ) -> Callable[
        [datastream.UpdateConnectionProfileRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateConnectionProfile(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_stream(
        self,
    ) -> Callable[[datastream.UpdateStreamRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateStream(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(
        _BaseDatastreamRestTransport._BaseGetLocation, DatastreamRestStub
    ):
        def __hash__(self):
            return hash("DatastreamRestTransport.GetLocation")

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
                _BaseDatastreamRestTransport._BaseGetLocation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDatastreamRestTransport._BaseGetLocation,
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
                    f"Sending request for google.cloud.datastream_v1.DatastreamClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DatastreamRestTransport._GetLocation._get_response(
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
                    "Received response for google.cloud.datastream_v1.DatastreamAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
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
        _BaseDatastreamRestTransport._BaseListLocations, DatastreamRestStub
    ):
        def __hash__(self):
            return hash("DatastreamRestTransport.ListLocations")

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
                _BaseDatastreamRestTransport._BaseListLocations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDatastreamRestTransport._BaseListLocations,
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
                    f"Sending request for google.cloud.datastream_v1.DatastreamClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DatastreamRestTransport._ListLocations._get_response(
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
                    "Received response for google.cloud.datastream_v1.DatastreamAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
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
        _BaseDatastreamRestTransport._BaseCancelOperation, DatastreamRestStub
    ):
        def __hash__(self):
            return hash("DatastreamRestTransport.CancelOperation")

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
                _BaseDatastreamRestTransport._BaseCancelOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDatastreamRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.datastream_v1.DatastreamClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DatastreamRestTransport._CancelOperation._get_response(
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
        _BaseDatastreamRestTransport._BaseDeleteOperation, DatastreamRestStub
    ):
        def __hash__(self):
            return hash("DatastreamRestTransport.DeleteOperation")

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
                _BaseDatastreamRestTransport._BaseDeleteOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDatastreamRestTransport._BaseDeleteOperation,
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
                    f"Sending request for google.cloud.datastream_v1.DatastreamClient.DeleteOperation",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DatastreamRestTransport._DeleteOperation._get_response(
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
        _BaseDatastreamRestTransport._BaseGetOperation, DatastreamRestStub
    ):
        def __hash__(self):
            return hash("DatastreamRestTransport.GetOperation")

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
                _BaseDatastreamRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDatastreamRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.datastream_v1.DatastreamClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DatastreamRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.datastream_v1.DatastreamAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
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
        _BaseDatastreamRestTransport._BaseListOperations, DatastreamRestStub
    ):
        def __hash__(self):
            return hash("DatastreamRestTransport.ListOperations")

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
                _BaseDatastreamRestTransport._BaseListOperations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDatastreamRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.datastream_v1.DatastreamClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DatastreamRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.datastream_v1.DatastreamAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.datastream.v1.Datastream",
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


__all__ = ("DatastreamRestTransport",)
