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
import logging
import json  # type: ignore

from google.auth.transport.requests import AuthorizedSession  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.api_core import client_options as client_options_lib
from google.api_core import exceptions as core_exceptions
from google.api_core import retry as retries
from google.api_core import rest_helpers
from google.api_core import rest_streaming
from google.api_core import gapic_v1
from google.showcase_v1beta1._compat import transcode_request, trace_http_request
import google.protobuf

from google.protobuf import json_format
from google.api_core import operations_v1
from google.iam.v1 import iam_policy_pb2  # type: ignore
from google.iam.v1 import policy_pb2  # type: ignore
from google.cloud.location import locations_pb2 # type: ignore

from requests import __version__ as requests_version
import dataclasses
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union
import warnings


from google.showcase_v1beta1.types import messaging
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore


from .rest_base import _BaseMessagingRestTransport
from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO

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


class MessagingRestInterceptor:
    """Interceptor for Messaging.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the MessagingRestTransport.

    .. code-block:: python
        class MyCustomMessagingInterceptor(MessagingRestInterceptor):
            def pre_create_blurb(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_blurb(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_room(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_room(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_blurb(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_room(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_get_blurb(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_blurb(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_room(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_room(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_blurbs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_blurbs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_rooms(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_rooms(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_search_blurbs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_search_blurbs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_stream_blurbs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_stream_blurbs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_blurb(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_blurb(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_room(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_room(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = MessagingRestTransport(interceptor=MyCustomMessagingInterceptor())
        client = MessagingClient(transport=transport)


    """
    def pre_create_blurb(self, request: messaging.CreateBlurbRequest, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[messaging.CreateBlurbRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_blurb

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Messaging server.
        """
        return request, metadata

    def post_create_blurb(self, response: messaging.Blurb) -> messaging.Blurb:
        """Post-rpc interceptor for create_blurb

        DEPRECATED. Please use the `post_create_blurb_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Messaging server but before
        it is returned to user code. This `post_create_blurb` interceptor runs
        before the `post_create_blurb_with_metadata` interceptor.
        """
        return response

    def post_create_blurb_with_metadata(self, response: messaging.Blurb, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[messaging.Blurb, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_blurb

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Messaging server but before it is returned to user code.

        We recommend only using this `post_create_blurb_with_metadata`
        interceptor in new development instead of the `post_create_blurb` interceptor.
        When both interceptors are used, this `post_create_blurb_with_metadata` interceptor runs after the
        `post_create_blurb` interceptor. The (possibly modified) response returned by
        `post_create_blurb` will be passed to
        `post_create_blurb_with_metadata`.
        """
        return response, metadata

    def pre_create_room(self, request: messaging.CreateRoomRequest, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[messaging.CreateRoomRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_room

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Messaging server.
        """
        return request, metadata

    def post_create_room(self, response: messaging.Room) -> messaging.Room:
        """Post-rpc interceptor for create_room

        DEPRECATED. Please use the `post_create_room_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Messaging server but before
        it is returned to user code. This `post_create_room` interceptor runs
        before the `post_create_room_with_metadata` interceptor.
        """
        return response

    def post_create_room_with_metadata(self, response: messaging.Room, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[messaging.Room, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_room

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Messaging server but before it is returned to user code.

        We recommend only using this `post_create_room_with_metadata`
        interceptor in new development instead of the `post_create_room` interceptor.
        When both interceptors are used, this `post_create_room_with_metadata` interceptor runs after the
        `post_create_room` interceptor. The (possibly modified) response returned by
        `post_create_room` will be passed to
        `post_create_room_with_metadata`.
        """
        return response, metadata

    def pre_delete_blurb(self, request: messaging.DeleteBlurbRequest, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[messaging.DeleteBlurbRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_blurb

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Messaging server.
        """
        return request, metadata

    def pre_delete_room(self, request: messaging.DeleteRoomRequest, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[messaging.DeleteRoomRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_room

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Messaging server.
        """
        return request, metadata

    def pre_get_blurb(self, request: messaging.GetBlurbRequest, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[messaging.GetBlurbRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_blurb

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Messaging server.
        """
        return request, metadata

    def post_get_blurb(self, response: messaging.Blurb) -> messaging.Blurb:
        """Post-rpc interceptor for get_blurb

        DEPRECATED. Please use the `post_get_blurb_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Messaging server but before
        it is returned to user code. This `post_get_blurb` interceptor runs
        before the `post_get_blurb_with_metadata` interceptor.
        """
        return response

    def post_get_blurb_with_metadata(self, response: messaging.Blurb, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[messaging.Blurb, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_blurb

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Messaging server but before it is returned to user code.

        We recommend only using this `post_get_blurb_with_metadata`
        interceptor in new development instead of the `post_get_blurb` interceptor.
        When both interceptors are used, this `post_get_blurb_with_metadata` interceptor runs after the
        `post_get_blurb` interceptor. The (possibly modified) response returned by
        `post_get_blurb` will be passed to
        `post_get_blurb_with_metadata`.
        """
        return response, metadata

    def pre_get_room(self, request: messaging.GetRoomRequest, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[messaging.GetRoomRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_room

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Messaging server.
        """
        return request, metadata

    def post_get_room(self, response: messaging.Room) -> messaging.Room:
        """Post-rpc interceptor for get_room

        DEPRECATED. Please use the `post_get_room_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Messaging server but before
        it is returned to user code. This `post_get_room` interceptor runs
        before the `post_get_room_with_metadata` interceptor.
        """
        return response

    def post_get_room_with_metadata(self, response: messaging.Room, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[messaging.Room, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_room

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Messaging server but before it is returned to user code.

        We recommend only using this `post_get_room_with_metadata`
        interceptor in new development instead of the `post_get_room` interceptor.
        When both interceptors are used, this `post_get_room_with_metadata` interceptor runs after the
        `post_get_room` interceptor. The (possibly modified) response returned by
        `post_get_room` will be passed to
        `post_get_room_with_metadata`.
        """
        return response, metadata

    def pre_list_blurbs(self, request: messaging.ListBlurbsRequest, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[messaging.ListBlurbsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_blurbs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Messaging server.
        """
        return request, metadata

    def post_list_blurbs(self, response: messaging.ListBlurbsResponse) -> messaging.ListBlurbsResponse:
        """Post-rpc interceptor for list_blurbs

        DEPRECATED. Please use the `post_list_blurbs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Messaging server but before
        it is returned to user code. This `post_list_blurbs` interceptor runs
        before the `post_list_blurbs_with_metadata` interceptor.
        """
        return response

    def post_list_blurbs_with_metadata(self, response: messaging.ListBlurbsResponse, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[messaging.ListBlurbsResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_blurbs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Messaging server but before it is returned to user code.

        We recommend only using this `post_list_blurbs_with_metadata`
        interceptor in new development instead of the `post_list_blurbs` interceptor.
        When both interceptors are used, this `post_list_blurbs_with_metadata` interceptor runs after the
        `post_list_blurbs` interceptor. The (possibly modified) response returned by
        `post_list_blurbs` will be passed to
        `post_list_blurbs_with_metadata`.
        """
        return response, metadata

    def pre_list_rooms(self, request: messaging.ListRoomsRequest, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[messaging.ListRoomsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_rooms

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Messaging server.
        """
        return request, metadata

    def post_list_rooms(self, response: messaging.ListRoomsResponse) -> messaging.ListRoomsResponse:
        """Post-rpc interceptor for list_rooms

        DEPRECATED. Please use the `post_list_rooms_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Messaging server but before
        it is returned to user code. This `post_list_rooms` interceptor runs
        before the `post_list_rooms_with_metadata` interceptor.
        """
        return response

    def post_list_rooms_with_metadata(self, response: messaging.ListRoomsResponse, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[messaging.ListRoomsResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_rooms

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Messaging server but before it is returned to user code.

        We recommend only using this `post_list_rooms_with_metadata`
        interceptor in new development instead of the `post_list_rooms` interceptor.
        When both interceptors are used, this `post_list_rooms_with_metadata` interceptor runs after the
        `post_list_rooms` interceptor. The (possibly modified) response returned by
        `post_list_rooms` will be passed to
        `post_list_rooms_with_metadata`.
        """
        return response, metadata

    def pre_search_blurbs(self, request: messaging.SearchBlurbsRequest, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[messaging.SearchBlurbsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for search_blurbs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Messaging server.
        """
        return request, metadata

    def post_search_blurbs(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for search_blurbs

        DEPRECATED. Please use the `post_search_blurbs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Messaging server but before
        it is returned to user code. This `post_search_blurbs` interceptor runs
        before the `post_search_blurbs_with_metadata` interceptor.
        """
        return response

    def post_search_blurbs_with_metadata(self, response: operations_pb2.Operation, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for search_blurbs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Messaging server but before it is returned to user code.

        We recommend only using this `post_search_blurbs_with_metadata`
        interceptor in new development instead of the `post_search_blurbs` interceptor.
        When both interceptors are used, this `post_search_blurbs_with_metadata` interceptor runs after the
        `post_search_blurbs` interceptor. The (possibly modified) response returned by
        `post_search_blurbs` will be passed to
        `post_search_blurbs_with_metadata`.
        """
        return response, metadata

    def pre_stream_blurbs(self, request: messaging.StreamBlurbsRequest, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[messaging.StreamBlurbsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for stream_blurbs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Messaging server.
        """
        return request, metadata

    def post_stream_blurbs(self, response: rest_streaming.ResponseIterator) -> rest_streaming.ResponseIterator:
        """Post-rpc interceptor for stream_blurbs

        DEPRECATED. Please use the `post_stream_blurbs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Messaging server but before
        it is returned to user code. This `post_stream_blurbs` interceptor runs
        before the `post_stream_blurbs_with_metadata` interceptor.
        """
        return response

    def post_stream_blurbs_with_metadata(self, response: rest_streaming.ResponseIterator, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[rest_streaming.ResponseIterator, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for stream_blurbs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Messaging server but before it is returned to user code.

        We recommend only using this `post_stream_blurbs_with_metadata`
        interceptor in new development instead of the `post_stream_blurbs` interceptor.
        When both interceptors are used, this `post_stream_blurbs_with_metadata` interceptor runs after the
        `post_stream_blurbs` interceptor. The (possibly modified) response returned by
        `post_stream_blurbs` will be passed to
        `post_stream_blurbs_with_metadata`.
        """
        return response, metadata

    def pre_update_blurb(self, request: messaging.UpdateBlurbRequest, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[messaging.UpdateBlurbRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_blurb

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Messaging server.
        """
        return request, metadata

    def post_update_blurb(self, response: messaging.Blurb) -> messaging.Blurb:
        """Post-rpc interceptor for update_blurb

        DEPRECATED. Please use the `post_update_blurb_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Messaging server but before
        it is returned to user code. This `post_update_blurb` interceptor runs
        before the `post_update_blurb_with_metadata` interceptor.
        """
        return response

    def post_update_blurb_with_metadata(self, response: messaging.Blurb, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[messaging.Blurb, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_blurb

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Messaging server but before it is returned to user code.

        We recommend only using this `post_update_blurb_with_metadata`
        interceptor in new development instead of the `post_update_blurb` interceptor.
        When both interceptors are used, this `post_update_blurb_with_metadata` interceptor runs after the
        `post_update_blurb` interceptor. The (possibly modified) response returned by
        `post_update_blurb` will be passed to
        `post_update_blurb_with_metadata`.
        """
        return response, metadata

    def pre_update_room(self, request: messaging.UpdateRoomRequest, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[messaging.UpdateRoomRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_room

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Messaging server.
        """
        return request, metadata

    def post_update_room(self, response: messaging.Room) -> messaging.Room:
        """Post-rpc interceptor for update_room

        DEPRECATED. Please use the `post_update_room_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Messaging server but before
        it is returned to user code. This `post_update_room` interceptor runs
        before the `post_update_room_with_metadata` interceptor.
        """
        return response

    def post_update_room_with_metadata(self, response: messaging.Room, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[messaging.Room, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_room

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Messaging server but before it is returned to user code.

        We recommend only using this `post_update_room_with_metadata`
        interceptor in new development instead of the `post_update_room` interceptor.
        When both interceptors are used, this `post_update_room_with_metadata` interceptor runs after the
        `post_update_room` interceptor. The (possibly modified) response returned by
        `post_update_room` will be passed to
        `post_update_room_with_metadata`.
        """
        return response, metadata

    def pre_list_locations(
        self, request: locations_pb2.ListLocationsRequest, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[locations_pb2.ListLocationsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_locations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Messaging server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the Messaging server but before
        it is returned to user code.
        """
        return response

    def pre_get_location(
        self, request: locations_pb2.GetLocationRequest, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[locations_pb2.GetLocationRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_location

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Messaging server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the Messaging server but before
        it is returned to user code.
        """
        return response

    def pre_set_iam_policy(
        self, request: iam_policy_pb2.SetIamPolicyRequest, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[iam_policy_pb2.SetIamPolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Messaging server.
        """
        return request, metadata

    def post_set_iam_policy(
        self, response: policy_pb2.Policy
    ) -> policy_pb2.Policy:
        """Post-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the Messaging server but before
        it is returned to user code.
        """
        return response

    def pre_get_iam_policy(
        self, request: iam_policy_pb2.GetIamPolicyRequest, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[iam_policy_pb2.GetIamPolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Messaging server.
        """
        return request, metadata

    def post_get_iam_policy(
        self, response: policy_pb2.Policy
    ) -> policy_pb2.Policy:
        """Post-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the Messaging server but before
        it is returned to user code.
        """
        return response

    def pre_test_iam_permissions(
        self, request: iam_policy_pb2.TestIamPermissionsRequest, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[iam_policy_pb2.TestIamPermissionsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for test_iam_permissions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Messaging server.
        """
        return request, metadata

    def post_test_iam_permissions(
        self, response: iam_policy_pb2.TestIamPermissionsResponse
    ) -> iam_policy_pb2.TestIamPermissionsResponse:
        """Post-rpc interceptor for test_iam_permissions

        Override in a subclass to manipulate the response
        after it is returned by the Messaging server but before
        it is returned to user code.
        """
        return response

    def pre_list_operations(
        self, request: operations_pb2.ListOperationsRequest, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[operations_pb2.ListOperationsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_operations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Messaging server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the Messaging server but before
        it is returned to user code.
        """
        return response

    def pre_get_operation(
        self, request: operations_pb2.GetOperationRequest, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[operations_pb2.GetOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Messaging server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the Messaging server but before
        it is returned to user code.
        """
        return response

    def pre_delete_operation(
        self, request: operations_pb2.DeleteOperationRequest, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[operations_pb2.DeleteOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Messaging server.
        """
        return request, metadata

    def post_delete_operation(
        self, response: None
    ) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the Messaging server but before
        it is returned to user code.
        """
        return response

    def pre_cancel_operation(
        self, request: operations_pb2.CancelOperationRequest, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[operations_pb2.CancelOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Messaging server.
        """
        return request, metadata

    def post_cancel_operation(
        self, response: None
    ) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the Messaging server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class MessagingRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: MessagingRestInterceptor
    _client_options: Optional[Union[client_options_lib.ClientOptions, dict]] = None


class MessagingRestTransport(_BaseMessagingRestTransport):
    """REST backend synchronous transport for Messaging.

    A simple messaging service that implements chat rooms and
    profile posts.
    This messaging service showcases the features that API clients
    generated by gapic-generators implement.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(self, *,
            host: str = 'localhost:7469',
            credentials: Optional[ga_credentials.Credentials] = None,
            credentials_file: Optional[str] = None,
            scopes: Optional[Sequence[str]] = None,
            client_cert_source_for_mtls: Optional[Callable[[
                ], Tuple[bytes, bytes]]] = None,
            quota_project_id: Optional[str] = None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            always_use_jwt_access: Optional[bool] = False,
            url_scheme: str = 'https',
            interceptor: Optional[MessagingRestInterceptor] = None,
            api_audience: Optional[str] = None,
            client_options: Optional[Union[client_options_lib.ClientOptions, dict]] = None,
            **kwargs,
            ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'localhost:7469').
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
            interceptor (Optional[MessagingRestInterceptor]): Interceptor used
                to manipulate requests, request metadata, and responses.
            api_audience (Optional[str]): The intended audience for the API calls
                to the service that will be set when using certain 3rd party
                authentication flows. Audience is typically a resource identifier.
                If not set, the host value will be used as a default.
            client_options (Optional[Union[google.api_core.client_options.ClientOptions, dict]]):
                Custom options for the client, containing options such as
                custom OpenTelemetry tracer providers.
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
            client_options=client_options,
            **kwargs,
        )
        self._session = AuthorizedSession(
            self._credentials, default_host=self.DEFAULT_HOST)
        self._operations_client: Optional[operations_v1.AbstractOperationsClient] = None
        if client_cert_source_for_mtls:
            self._session.configure_mtls_channel(client_cert_source_for_mtls)
        self._interceptor = interceptor or MessagingRestInterceptor()
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
                'google.longrunning.Operations.ListOperations': [
                    {
                        'method': 'get',
                        'uri': '/v1beta1/operations',
                    },
                ],
                'google.longrunning.Operations.GetOperation': [
                    {
                        'method': 'get',
                        'uri': '/v1beta1/{name=operations/**}',
                    },
                ],
                'google.longrunning.Operations.DeleteOperation': [
                    {
                        'method': 'delete',
                        'uri': '/v1beta1/{name=operations/**}',
                    },
                ],
                'google.longrunning.Operations.CancelOperation': [
                    {
                        'method': 'post',
                        'uri': '/v1beta1/{name=operations/**}:cancel',
                    },
                ],
            }

            rest_transport = operations_v1.OperationsRestTransport(
                    host=self._host,
                    # use the credentials which are saved
                    credentials=self._credentials,
                    scopes=self._scopes,
                    http_options=http_options,
                    path_prefix="v1beta1")

            self._operations_client = operations_v1.AbstractOperationsClient(transport=rest_transport)

        # Return the client from cache.
        return self._operations_client

    class _Connect(_BaseMessagingRestTransport._BaseConnect, MessagingRestStub):
        def __hash__(self):
            return hash("MessagingRestTransport.Connect")

        def __call__(self,
                request: messaging.ConnectRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
                ) -> rest_streaming.ResponseIterator:
            raise NotImplementedError(
                "Method Connect is not available over REST transport"
            )
    class _CreateBlurb(_BaseMessagingRestTransport._BaseCreateBlurb, MessagingRestStub):
        def __hash__(self):
            return hash("MessagingRestTransport.CreateBlurb")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request['uri']
            method = transcoded_request['method']
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                    )
                trace_ctx.record_response(response)
                return response

        def __call__(self,
                request: messaging.CreateBlurbRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
                ) -> messaging.Blurb:
            r"""Call the create blurb method over HTTP.

            Args:
                request (~.messaging.CreateBlurbRequest):
                    The request object. The request message for the
                google.showcase.v1beta1.Messaging\CreateBlurb
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.messaging.Blurb:
                    This protocol buffer message
                represents a blurb sent to a chat room
                or posted on a user profile.

            """

            http_options = _BaseMessagingRestTransport._BaseCreateBlurb._get_http_options()
            request, metadata = self._interceptor.pre_create_blurb(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMessagingRestTransport._BaseCreateBlurb,
                    "_BaseCreateBlurb__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
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
                    f"Sending request for google.showcase_v1beta1.MessagingClient.CreateBlurb",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Messaging",
                        "rpcName": "CreateBlurb",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MessagingRestTransport._CreateBlurb._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = messaging.Blurb()
            pb_resp = messaging.Blurb.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_create_blurb(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_blurb_with_metadata(resp, response_metadata)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                try:
                    response_payload = messaging.Blurb.to_json(response)
                except:
                    response_payload = None
                http_response = {
                "payload": response_payload,
                "headers":  dict(response.headers),
                "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.showcase_v1beta1.MessagingClient.create_blurb",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Messaging",
                        "rpcName": "CreateBlurb",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateRoom(_BaseMessagingRestTransport._BaseCreateRoom, MessagingRestStub):
        def __hash__(self):
            return hash("MessagingRestTransport.CreateRoom")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request['uri']
            method = transcoded_request['method']
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                    )
                trace_ctx.record_response(response)
                return response

        def __call__(self,
                request: messaging.CreateRoomRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
                ) -> messaging.Room:
            r"""Call the create room method over HTTP.

            Args:
                request (~.messaging.CreateRoomRequest):
                    The request object. The request message for the
                google.showcase.v1beta1.Messaging\CreateRoom
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.messaging.Room:
                    A chat room.
            """

            http_options = _BaseMessagingRestTransport._BaseCreateRoom._get_http_options()
            request, metadata = self._interceptor.pre_create_room(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMessagingRestTransport._BaseCreateRoom,
                    "_BaseCreateRoom__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
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
                    f"Sending request for google.showcase_v1beta1.MessagingClient.CreateRoom",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Messaging",
                        "rpcName": "CreateRoom",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MessagingRestTransport._CreateRoom._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = messaging.Room()
            pb_resp = messaging.Room.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_create_room(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_room_with_metadata(resp, response_metadata)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                try:
                    response_payload = messaging.Room.to_json(response)
                except:
                    response_payload = None
                http_response = {
                "payload": response_payload,
                "headers":  dict(response.headers),
                "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.showcase_v1beta1.MessagingClient.create_room",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Messaging",
                        "rpcName": "CreateRoom",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteBlurb(_BaseMessagingRestTransport._BaseDeleteBlurb, MessagingRestStub):
        def __hash__(self):
            return hash("MessagingRestTransport.DeleteBlurb")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request['uri']
            method = transcoded_request['method']
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    )
                trace_ctx.record_response(response)
                return response

        def __call__(self,
                request: messaging.DeleteBlurbRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
                ):
            r"""Call the delete blurb method over HTTP.

            Args:
                request (~.messaging.DeleteBlurbRequest):
                    The request object. The request message for the
                google.showcase.v1beta1.Messaging\DeleteBlurb
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseMessagingRestTransport._BaseDeleteBlurb._get_http_options()
            request, metadata = self._interceptor.pre_delete_blurb(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMessagingRestTransport._BaseDeleteBlurb,
                    "_BaseDeleteBlurb__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
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
                    f"Sending request for google.showcase_v1beta1.MessagingClient.DeleteBlurb",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Messaging",
                        "rpcName": "DeleteBlurb",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MessagingRestTransport._DeleteBlurb._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

    class _DeleteRoom(_BaseMessagingRestTransport._BaseDeleteRoom, MessagingRestStub):
        def __hash__(self):
            return hash("MessagingRestTransport.DeleteRoom")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request['uri']
            method = transcoded_request['method']
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    )
                trace_ctx.record_response(response)
                return response

        def __call__(self,
                request: messaging.DeleteRoomRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
                ):
            r"""Call the delete room method over HTTP.

            Args:
                request (~.messaging.DeleteRoomRequest):
                    The request object. The request message for the
                google.showcase.v1beta1.Messaging\DeleteRoom
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseMessagingRestTransport._BaseDeleteRoom._get_http_options()
            request, metadata = self._interceptor.pre_delete_room(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMessagingRestTransport._BaseDeleteRoom,
                    "_BaseDeleteRoom__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
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
                    f"Sending request for google.showcase_v1beta1.MessagingClient.DeleteRoom",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Messaging",
                        "rpcName": "DeleteRoom",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MessagingRestTransport._DeleteRoom._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

    class _GetBlurb(_BaseMessagingRestTransport._BaseGetBlurb, MessagingRestStub):
        def __hash__(self):
            return hash("MessagingRestTransport.GetBlurb")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request['uri']
            method = transcoded_request['method']
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    )
                trace_ctx.record_response(response)
                return response

        def __call__(self,
                request: messaging.GetBlurbRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
                ) -> messaging.Blurb:
            r"""Call the get blurb method over HTTP.

            Args:
                request (~.messaging.GetBlurbRequest):
                    The request object. The request message for the
                google.showcase.v1beta1.Messaging\GetBlurb
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.messaging.Blurb:
                    This protocol buffer message
                represents a blurb sent to a chat room
                or posted on a user profile.

            """

            http_options = _BaseMessagingRestTransport._BaseGetBlurb._get_http_options()
            request, metadata = self._interceptor.pre_get_blurb(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMessagingRestTransport._BaseGetBlurb,
                    "_BaseGetBlurb__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
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
                    f"Sending request for google.showcase_v1beta1.MessagingClient.GetBlurb",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Messaging",
                        "rpcName": "GetBlurb",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MessagingRestTransport._GetBlurb._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = messaging.Blurb()
            pb_resp = messaging.Blurb.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_get_blurb(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_blurb_with_metadata(resp, response_metadata)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                try:
                    response_payload = messaging.Blurb.to_json(response)
                except:
                    response_payload = None
                http_response = {
                "payload": response_payload,
                "headers":  dict(response.headers),
                "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.showcase_v1beta1.MessagingClient.get_blurb",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Messaging",
                        "rpcName": "GetBlurb",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetRoom(_BaseMessagingRestTransport._BaseGetRoom, MessagingRestStub):
        def __hash__(self):
            return hash("MessagingRestTransport.GetRoom")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request['uri']
            method = transcoded_request['method']
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    )
                trace_ctx.record_response(response)
                return response

        def __call__(self,
                request: messaging.GetRoomRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
                ) -> messaging.Room:
            r"""Call the get room method over HTTP.

            Args:
                request (~.messaging.GetRoomRequest):
                    The request object. The request message for the
                google.showcase.v1beta1.Messaging\GetRoom
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.messaging.Room:
                    A chat room.
            """

            http_options = _BaseMessagingRestTransport._BaseGetRoom._get_http_options()
            request, metadata = self._interceptor.pre_get_room(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMessagingRestTransport._BaseGetRoom,
                    "_BaseGetRoom__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
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
                    f"Sending request for google.showcase_v1beta1.MessagingClient.GetRoom",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Messaging",
                        "rpcName": "GetRoom",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MessagingRestTransport._GetRoom._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = messaging.Room()
            pb_resp = messaging.Room.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_get_room(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_room_with_metadata(resp, response_metadata)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                try:
                    response_payload = messaging.Room.to_json(response)
                except:
                    response_payload = None
                http_response = {
                "payload": response_payload,
                "headers":  dict(response.headers),
                "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.showcase_v1beta1.MessagingClient.get_room",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Messaging",
                        "rpcName": "GetRoom",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListBlurbs(_BaseMessagingRestTransport._BaseListBlurbs, MessagingRestStub):
        def __hash__(self):
            return hash("MessagingRestTransport.ListBlurbs")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request['uri']
            method = transcoded_request['method']
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    )
                trace_ctx.record_response(response)
                return response

        def __call__(self,
                request: messaging.ListBlurbsRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
                ) -> messaging.ListBlurbsResponse:
            r"""Call the list blurbs method over HTTP.

            Args:
                request (~.messaging.ListBlurbsRequest):
                    The request object. The request message for the
                google.showcase.v1beta1.Messaging\ListBlurbs
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.messaging.ListBlurbsResponse:
                    The response message for the
                google.showcase.v1beta1.Messaging\ListBlurbs
                method.

            """

            http_options = _BaseMessagingRestTransport._BaseListBlurbs._get_http_options()
            request, metadata = self._interceptor.pre_list_blurbs(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMessagingRestTransport._BaseListBlurbs,
                    "_BaseListBlurbs__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
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
                    f"Sending request for google.showcase_v1beta1.MessagingClient.ListBlurbs",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Messaging",
                        "rpcName": "ListBlurbs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MessagingRestTransport._ListBlurbs._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = messaging.ListBlurbsResponse()
            pb_resp = messaging.ListBlurbsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_list_blurbs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_blurbs_with_metadata(resp, response_metadata)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                try:
                    response_payload = messaging.ListBlurbsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                "payload": response_payload,
                "headers":  dict(response.headers),
                "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.showcase_v1beta1.MessagingClient.list_blurbs",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Messaging",
                        "rpcName": "ListBlurbs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListRooms(_BaseMessagingRestTransport._BaseListRooms, MessagingRestStub):
        def __hash__(self):
            return hash("MessagingRestTransport.ListRooms")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request['uri']
            method = transcoded_request['method']
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    )
                trace_ctx.record_response(response)
                return response

        def __call__(self,
                request: messaging.ListRoomsRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
                ) -> messaging.ListRoomsResponse:
            r"""Call the list rooms method over HTTP.

            Args:
                request (~.messaging.ListRoomsRequest):
                    The request object. The request message for the
                google.showcase.v1beta1.Messaging\ListRooms
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.messaging.ListRoomsResponse:
                    The response message for the
                google.showcase.v1beta1.Messaging\ListRooms
                method.

            """

            http_options = _BaseMessagingRestTransport._BaseListRooms._get_http_options()
            request, metadata = self._interceptor.pre_list_rooms(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMessagingRestTransport._BaseListRooms,
                    "_BaseListRooms__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
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
                    f"Sending request for google.showcase_v1beta1.MessagingClient.ListRooms",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Messaging",
                        "rpcName": "ListRooms",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MessagingRestTransport._ListRooms._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = messaging.ListRoomsResponse()
            pb_resp = messaging.ListRoomsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_list_rooms(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_rooms_with_metadata(resp, response_metadata)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                try:
                    response_payload = messaging.ListRoomsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                "payload": response_payload,
                "headers":  dict(response.headers),
                "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.showcase_v1beta1.MessagingClient.list_rooms",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Messaging",
                        "rpcName": "ListRooms",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SearchBlurbs(_BaseMessagingRestTransport._BaseSearchBlurbs, MessagingRestStub):
        def __hash__(self):
            return hash("MessagingRestTransport.SearchBlurbs")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request['uri']
            method = transcoded_request['method']
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                    )
                trace_ctx.record_response(response)
                return response

        def __call__(self,
                request: messaging.SearchBlurbsRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
                ) -> operations_pb2.Operation:
            r"""Call the search blurbs method over HTTP.

            Args:
                request (~.messaging.SearchBlurbsRequest):
                    The request object. The request message for the
                google.showcase.v1beta1.Messaging\SearchBlurbs
                method.
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

            http_options = _BaseMessagingRestTransport._BaseSearchBlurbs._get_http_options()
            request, metadata = self._interceptor.pre_search_blurbs(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMessagingRestTransport._BaseSearchBlurbs,
                    "_BaseSearchBlurbs__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
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
                    f"Sending request for google.showcase_v1beta1.MessagingClient.SearchBlurbs",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Messaging",
                        "rpcName": "SearchBlurbs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MessagingRestTransport._SearchBlurbs._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_search_blurbs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_search_blurbs_with_metadata(resp, response_metadata)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                "payload": response_payload,
                "headers":  dict(response.headers),
                "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.showcase_v1beta1.MessagingClient.search_blurbs",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Messaging",
                        "rpcName": "SearchBlurbs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SendBlurbs(_BaseMessagingRestTransport._BaseSendBlurbs, MessagingRestStub):
        def __hash__(self):
            return hash("MessagingRestTransport.SendBlurbs")

        def __call__(self,
                request: messaging.CreateBlurbRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
                ) -> messaging.SendBlurbsResponse:
            raise NotImplementedError(
                "Method SendBlurbs is not available over REST transport"
            )
    class _StreamBlurbs(_BaseMessagingRestTransport._BaseStreamBlurbs, MessagingRestStub):
        def __hash__(self):
            return hash("MessagingRestTransport.StreamBlurbs")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request['uri']
            method = transcoded_request['method']
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                    stream=True,
                    )
                trace_ctx.record_response(response)
                return response

        def __call__(self,
                request: messaging.StreamBlurbsRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
                ) -> rest_streaming.ResponseIterator:
            r"""Call the stream blurbs method over HTTP.

            Args:
                request (~.messaging.StreamBlurbsRequest):
                    The request object. The request message for the
                google.showcase.v1beta1.Messaging\StreamBlurbs
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.messaging.StreamBlurbsResponse:
                    The response message for the
                google.showcase.v1beta1.Messaging\StreamBlurbs
                method.

            """

            http_options = _BaseMessagingRestTransport._BaseStreamBlurbs._get_http_options()
            request, metadata = self._interceptor.pre_stream_blurbs(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMessagingRestTransport._BaseStreamBlurbs,
                    "_BaseStreamBlurbs__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
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
                    f"Sending request for google.showcase_v1beta1.MessagingClient.StreamBlurbs",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Messaging",
                        "rpcName": "StreamBlurbs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MessagingRestTransport._StreamBlurbs._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = rest_streaming.ResponseIterator(response, messaging.StreamBlurbsResponse)
            resp = self._interceptor.post_stream_blurbs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_stream_blurbs_with_metadata(resp, response_metadata)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                http_response = {
                "headers":  dict(response.headers),
                "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.showcase_v1beta1.MessagingClient.stream_blurbs",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Messaging",
                        "rpcName": "StreamBlurbs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateBlurb(_BaseMessagingRestTransport._BaseUpdateBlurb, MessagingRestStub):
        def __hash__(self):
            return hash("MessagingRestTransport.UpdateBlurb")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request['uri']
            method = transcoded_request['method']
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                    )
                trace_ctx.record_response(response)
                return response

        def __call__(self,
                request: messaging.UpdateBlurbRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
                ) -> messaging.Blurb:
            r"""Call the update blurb method over HTTP.

            Args:
                request (~.messaging.UpdateBlurbRequest):
                    The request object. The request message for the
                google.showcase.v1beta1.Messaging\UpdateBlurb
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.messaging.Blurb:
                    This protocol buffer message
                represents a blurb sent to a chat room
                or posted on a user profile.

            """

            http_options = _BaseMessagingRestTransport._BaseUpdateBlurb._get_http_options()
            request, metadata = self._interceptor.pre_update_blurb(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMessagingRestTransport._BaseUpdateBlurb,
                    "_BaseUpdateBlurb__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
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
                    f"Sending request for google.showcase_v1beta1.MessagingClient.UpdateBlurb",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Messaging",
                        "rpcName": "UpdateBlurb",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MessagingRestTransport._UpdateBlurb._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = messaging.Blurb()
            pb_resp = messaging.Blurb.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_update_blurb(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_blurb_with_metadata(resp, response_metadata)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                try:
                    response_payload = messaging.Blurb.to_json(response)
                except:
                    response_payload = None
                http_response = {
                "payload": response_payload,
                "headers":  dict(response.headers),
                "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.showcase_v1beta1.MessagingClient.update_blurb",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Messaging",
                        "rpcName": "UpdateBlurb",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateRoom(_BaseMessagingRestTransport._BaseUpdateRoom, MessagingRestStub):
        def __hash__(self):
            return hash("MessagingRestTransport.UpdateRoom")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request['uri']
            method = transcoded_request['method']
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                    )
                trace_ctx.record_response(response)
                return response

        def __call__(self,
                request: messaging.UpdateRoomRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
                ) -> messaging.Room:
            r"""Call the update room method over HTTP.

            Args:
                request (~.messaging.UpdateRoomRequest):
                    The request object. The request message for the
                google.showcase.v1beta1.Messaging\UpdateRoom
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.messaging.Room:
                    A chat room.
            """

            http_options = _BaseMessagingRestTransport._BaseUpdateRoom._get_http_options()
            request, metadata = self._interceptor.pre_update_room(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMessagingRestTransport._BaseUpdateRoom,
                    "_BaseUpdateRoom__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
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
                    f"Sending request for google.showcase_v1beta1.MessagingClient.UpdateRoom",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Messaging",
                        "rpcName": "UpdateRoom",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MessagingRestTransport._UpdateRoom._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = messaging.Room()
            pb_resp = messaging.Room.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_update_room(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_room_with_metadata(resp, response_metadata)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                try:
                    response_payload = messaging.Room.to_json(response)
                except:
                    response_payload = None
                http_response = {
                "payload": response_payload,
                "headers":  dict(response.headers),
                "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.showcase_v1beta1.MessagingClient.update_room",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Messaging",
                        "rpcName": "UpdateRoom",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def connect(self) -> Callable[
            [messaging.ConnectRequest],
            messaging.StreamBlurbsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Connect(self._session, self._host, self._interceptor, getattr(self, "_client_options", None)) # type: ignore

    @property
    def create_blurb(self) -> Callable[
            [messaging.CreateBlurbRequest],
            messaging.Blurb]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateBlurb(self._session, self._host, self._interceptor, getattr(self, "_client_options", None)) # type: ignore

    @property
    def create_room(self) -> Callable[
            [messaging.CreateRoomRequest],
            messaging.Room]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateRoom(self._session, self._host, self._interceptor, getattr(self, "_client_options", None)) # type: ignore

    @property
    def delete_blurb(self) -> Callable[
            [messaging.DeleteBlurbRequest],
            empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteBlurb(self._session, self._host, self._interceptor, getattr(self, "_client_options", None)) # type: ignore

    @property
    def delete_room(self) -> Callable[
            [messaging.DeleteRoomRequest],
            empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteRoom(self._session, self._host, self._interceptor, getattr(self, "_client_options", None)) # type: ignore

    @property
    def get_blurb(self) -> Callable[
            [messaging.GetBlurbRequest],
            messaging.Blurb]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetBlurb(self._session, self._host, self._interceptor, getattr(self, "_client_options", None)) # type: ignore

    @property
    def get_room(self) -> Callable[
            [messaging.GetRoomRequest],
            messaging.Room]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetRoom(self._session, self._host, self._interceptor, getattr(self, "_client_options", None)) # type: ignore

    @property
    def list_blurbs(self) -> Callable[
            [messaging.ListBlurbsRequest],
            messaging.ListBlurbsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListBlurbs(self._session, self._host, self._interceptor, getattr(self, "_client_options", None)) # type: ignore

    @property
    def list_rooms(self) -> Callable[
            [messaging.ListRoomsRequest],
            messaging.ListRoomsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListRooms(self._session, self._host, self._interceptor, getattr(self, "_client_options", None)) # type: ignore

    @property
    def search_blurbs(self) -> Callable[
            [messaging.SearchBlurbsRequest],
            operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SearchBlurbs(self._session, self._host, self._interceptor, getattr(self, "_client_options", None)) # type: ignore

    @property
    def send_blurbs(self) -> Callable[
            [messaging.CreateBlurbRequest],
            messaging.SendBlurbsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SendBlurbs(self._session, self._host, self._interceptor, getattr(self, "_client_options", None)) # type: ignore

    @property
    def stream_blurbs(self) -> Callable[
            [messaging.StreamBlurbsRequest],
            messaging.StreamBlurbsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._StreamBlurbs(self._session, self._host, self._interceptor, getattr(self, "_client_options", None)) # type: ignore

    @property
    def update_blurb(self) -> Callable[
            [messaging.UpdateBlurbRequest],
            messaging.Blurb]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateBlurb(self._session, self._host, self._interceptor, getattr(self, "_client_options", None)) # type: ignore

    @property
    def update_room(self) -> Callable[
            [messaging.UpdateRoomRequest],
            messaging.Room]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateRoom(self._session, self._host, self._interceptor, getattr(self, "_client_options", None)) # type: ignore

    @property
    def list_locations(self):
        return self._ListLocations(self._session, self._host, self._interceptor, getattr(self, "_client_options", None)) # type: ignore

    class _ListLocations(_BaseMessagingRestTransport._BaseListLocations, MessagingRestStub):
        def __hash__(self):
            return hash("MessagingRestTransport.ListLocations")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request['uri']
            method = transcoded_request['method']
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    )
                trace_ctx.record_response(response)
                return response

        def __call__(self,
            request: locations_pb2.ListLocationsRequest, *,
            retry: OptionalRetry=gapic_v1.method.DEFAULT,
            timeout: Optional[float]=None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
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

            http_options = _BaseMessagingRestTransport._BaseListLocations._get_http_options()
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMessagingRestTransport._BaseListLocations,
                    "_BaseListLocations__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
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
                    f"Sending request for google.showcase_v1beta1.MessagingClient.ListLocations",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Messaging",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MessagingRestTransport._ListLocations._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            content = response.content.decode("utf-8")
            resp = locations_pb2.ListLocationsResponse()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_list_locations(resp)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers":  dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.showcase_v1beta1.MessagingAsyncClient.ListLocations",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Messaging",
                        "rpcName": "ListLocations",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor, getattr(self, "_client_options", None)) # type: ignore

    class _GetLocation(_BaseMessagingRestTransport._BaseGetLocation, MessagingRestStub):
        def __hash__(self):
            return hash("MessagingRestTransport.GetLocation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request['uri']
            method = transcoded_request['method']
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    )
                trace_ctx.record_response(response)
                return response

        def __call__(self,
            request: locations_pb2.GetLocationRequest, *,
            retry: OptionalRetry=gapic_v1.method.DEFAULT,
            timeout: Optional[float]=None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
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

            http_options = _BaseMessagingRestTransport._BaseGetLocation._get_http_options()
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMessagingRestTransport._BaseGetLocation,
                    "_BaseGetLocation__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
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
                    f"Sending request for google.showcase_v1beta1.MessagingClient.GetLocation",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Messaging",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MessagingRestTransport._GetLocation._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            content = response.content.decode("utf-8")
            resp = locations_pb2.Location()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_get_location(resp)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers":  dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.showcase_v1beta1.MessagingAsyncClient.GetLocation",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Messaging",
                        "rpcName": "GetLocation",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def set_iam_policy(self):
        return self._SetIamPolicy(self._session, self._host, self._interceptor, getattr(self, "_client_options", None)) # type: ignore

    class _SetIamPolicy(_BaseMessagingRestTransport._BaseSetIamPolicy, MessagingRestStub):
        def __hash__(self):
            return hash("MessagingRestTransport.SetIamPolicy")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request['uri']
            method = transcoded_request['method']
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                    )
                trace_ctx.record_response(response)
                return response

        def __call__(self,
            request: iam_policy_pb2.SetIamPolicyRequest, *,
            retry: OptionalRetry=gapic_v1.method.DEFAULT,
            timeout: Optional[float]=None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
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

            http_options = _BaseMessagingRestTransport._BaseSetIamPolicy._get_http_options()
            request, metadata = self._interceptor.pre_set_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMessagingRestTransport._BaseSetIamPolicy,
                    "_BaseSetIamPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
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
                    f"Sending request for google.showcase_v1beta1.MessagingClient.SetIamPolicy",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Messaging",
                        "rpcName": "SetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MessagingRestTransport._SetIamPolicy._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            content = response.content.decode("utf-8")
            resp = policy_pb2.Policy()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_set_iam_policy(resp)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers":  dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.showcase_v1beta1.MessagingAsyncClient.SetIamPolicy",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Messaging",
                        "rpcName": "SetIamPolicy",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def get_iam_policy(self):
        return self._GetIamPolicy(self._session, self._host, self._interceptor, getattr(self, "_client_options", None)) # type: ignore

    class _GetIamPolicy(_BaseMessagingRestTransport._BaseGetIamPolicy, MessagingRestStub):
        def __hash__(self):
            return hash("MessagingRestTransport.GetIamPolicy")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request['uri']
            method = transcoded_request['method']
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    )
                trace_ctx.record_response(response)
                return response

        def __call__(self,
            request: iam_policy_pb2.GetIamPolicyRequest, *,
            retry: OptionalRetry=gapic_v1.method.DEFAULT,
            timeout: Optional[float]=None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
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

            http_options = _BaseMessagingRestTransport._BaseGetIamPolicy._get_http_options()
            request, metadata = self._interceptor.pre_get_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMessagingRestTransport._BaseGetIamPolicy,
                    "_BaseGetIamPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
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
                    f"Sending request for google.showcase_v1beta1.MessagingClient.GetIamPolicy",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Messaging",
                        "rpcName": "GetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MessagingRestTransport._GetIamPolicy._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            content = response.content.decode("utf-8")
            resp = policy_pb2.Policy()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_get_iam_policy(resp)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers":  dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.showcase_v1beta1.MessagingAsyncClient.GetIamPolicy",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Messaging",
                        "rpcName": "GetIamPolicy",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def test_iam_permissions(self):
        return self._TestIamPermissions(self._session, self._host, self._interceptor, getattr(self, "_client_options", None)) # type: ignore

    class _TestIamPermissions(_BaseMessagingRestTransport._BaseTestIamPermissions, MessagingRestStub):
        def __hash__(self):
            return hash("MessagingRestTransport.TestIamPermissions")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request['uri']
            method = transcoded_request['method']
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                    )
                trace_ctx.record_response(response)
                return response

        def __call__(self,
            request: iam_policy_pb2.TestIamPermissionsRequest, *,
            retry: OptionalRetry=gapic_v1.method.DEFAULT,
            timeout: Optional[float]=None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
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

            http_options = _BaseMessagingRestTransport._BaseTestIamPermissions._get_http_options()
            request, metadata = self._interceptor.pre_test_iam_permissions(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMessagingRestTransport._BaseTestIamPermissions,
                    "_BaseTestIamPermissions__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
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
                    f"Sending request for google.showcase_v1beta1.MessagingClient.TestIamPermissions",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Messaging",
                        "rpcName": "TestIamPermissions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MessagingRestTransport._TestIamPermissions._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            content = response.content.decode("utf-8")
            resp = iam_policy_pb2.TestIamPermissionsResponse()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_test_iam_permissions(resp)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers":  dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.showcase_v1beta1.MessagingAsyncClient.TestIamPermissions",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Messaging",
                        "rpcName": "TestIamPermissions",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def list_operations(self):
        return self._ListOperations(self._session, self._host, self._interceptor, getattr(self, "_client_options", None)) # type: ignore

    class _ListOperations(_BaseMessagingRestTransport._BaseListOperations, MessagingRestStub):
        def __hash__(self):
            return hash("MessagingRestTransport.ListOperations")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request['uri']
            method = transcoded_request['method']
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    )
                trace_ctx.record_response(response)
                return response

        def __call__(self,
            request: operations_pb2.ListOperationsRequest, *,
            retry: OptionalRetry=gapic_v1.method.DEFAULT,
            timeout: Optional[float]=None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
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

            http_options = _BaseMessagingRestTransport._BaseListOperations._get_http_options()
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMessagingRestTransport._BaseListOperations,
                    "_BaseListOperations__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
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
                    f"Sending request for google.showcase_v1beta1.MessagingClient.ListOperations",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Messaging",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MessagingRestTransport._ListOperations._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            content = response.content.decode("utf-8")
            resp = operations_pb2.ListOperationsResponse()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_list_operations(resp)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers":  dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.showcase_v1beta1.MessagingAsyncClient.ListOperations",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Messaging",
                        "rpcName": "ListOperations",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor, getattr(self, "_client_options", None)) # type: ignore

    class _GetOperation(_BaseMessagingRestTransport._BaseGetOperation, MessagingRestStub):
        def __hash__(self):
            return hash("MessagingRestTransport.GetOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request['uri']
            method = transcoded_request['method']
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    )
                trace_ctx.record_response(response)
                return response

        def __call__(self,
            request: operations_pb2.GetOperationRequest, *,
            retry: OptionalRetry=gapic_v1.method.DEFAULT,
            timeout: Optional[float]=None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
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

            http_options = _BaseMessagingRestTransport._BaseGetOperation._get_http_options()
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMessagingRestTransport._BaseGetOperation,
                    "_BaseGetOperation__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
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
                    f"Sending request for google.showcase_v1beta1.MessagingClient.GetOperation",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Messaging",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MessagingRestTransport._GetOperation._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            content = response.content.decode("utf-8")
            resp = operations_pb2.Operation()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_get_operation(resp)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers":  dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.showcase_v1beta1.MessagingAsyncClient.GetOperation",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Messaging",
                        "rpcName": "GetOperation",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def delete_operation(self):
        return self._DeleteOperation(self._session, self._host, self._interceptor, getattr(self, "_client_options", None)) # type: ignore

    class _DeleteOperation(_BaseMessagingRestTransport._BaseDeleteOperation, MessagingRestStub):
        def __hash__(self):
            return hash("MessagingRestTransport.DeleteOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request['uri']
            method = transcoded_request['method']
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    )
                trace_ctx.record_response(response)
                return response

        def __call__(self,
            request: operations_pb2.DeleteOperationRequest, *,
            retry: OptionalRetry=gapic_v1.method.DEFAULT,
            timeout: Optional[float]=None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
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

            http_options = _BaseMessagingRestTransport._BaseDeleteOperation._get_http_options()
            request, metadata = self._interceptor.pre_delete_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMessagingRestTransport._BaseDeleteOperation,
                    "_BaseDeleteOperation__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
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
                    f"Sending request for google.showcase_v1beta1.MessagingClient.DeleteOperation",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Messaging",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MessagingRestTransport._DeleteOperation._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            return self._interceptor.post_delete_operation(None)

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor, getattr(self, "_client_options", None)) # type: ignore

    class _CancelOperation(_BaseMessagingRestTransport._BaseCancelOperation, MessagingRestStub):
        def __hash__(self):
            return hash("MessagingRestTransport.CancelOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request['uri']
            method = transcoded_request['method']
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    )
                trace_ctx.record_response(response)
                return response

        def __call__(self,
            request: operations_pb2.CancelOperationRequest, *,
            retry: OptionalRetry=gapic_v1.method.DEFAULT,
            timeout: Optional[float]=None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
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

            http_options = _BaseMessagingRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMessagingRestTransport._BaseCancelOperation,
                    "_BaseCancelOperation__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
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
                    f"Sending request for google.showcase_v1beta1.MessagingClient.CancelOperation",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Messaging",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MessagingRestTransport._CancelOperation._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            return self._interceptor.post_cancel_operation(None)

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__=(
    'MessagingRestTransport',
)
