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

from google.cloud.eventarc_v1._compat import transcode_request
from google.cloud.eventarc_v1.types import (
    channel,
    channel_connection,
    discovery,
    enrollment,
    eventarc,
    google_api_source,
    google_channel_config,
    message_bus,
    pipeline,
    trigger,
)
from google.cloud.eventarc_v1.types import (
    google_channel_config as gce_google_channel_config,
)

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseEventarcRestTransport

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


class EventarcRestInterceptor:
    """Interceptor for Eventarc.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the EventarcRestTransport.

    .. code-block:: python
        class MyCustomEventarcInterceptor(EventarcRestInterceptor):
            def pre_create_channel(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_channel(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_channel_connection(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_channel_connection(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_enrollment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_enrollment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_google_api_source(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_google_api_source(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_message_bus(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_message_bus(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_pipeline(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_pipeline(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_trigger(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_trigger(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_channel(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_channel(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_channel_connection(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_channel_connection(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_enrollment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_enrollment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_google_api_source(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_google_api_source(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_message_bus(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_message_bus(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_pipeline(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_pipeline(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_trigger(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_trigger(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_channel(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_channel(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_channel_connection(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_channel_connection(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_enrollment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_enrollment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_google_api_source(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_google_api_source(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_google_channel_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_google_channel_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_message_bus(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_message_bus(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_pipeline(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_pipeline(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_provider(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_provider(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_trigger(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_trigger(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_channel_connections(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_channel_connections(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_channels(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_channels(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_enrollments(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_enrollments(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_google_api_sources(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_google_api_sources(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_message_bus_enrollments(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_message_bus_enrollments(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_message_buses(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_message_buses(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_pipelines(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_pipelines(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_providers(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_providers(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_triggers(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_triggers(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_channel(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_channel(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_enrollment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_enrollment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_google_api_source(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_google_api_source(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_google_channel_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_google_channel_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_message_bus(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_message_bus(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_pipeline(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_pipeline(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_trigger(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_trigger(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = EventarcRestTransport(interceptor=MyCustomEventarcInterceptor())
        client = EventarcClient(transport=transport)


    """

    def pre_create_channel(
        self,
        request: eventarc.CreateChannelRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[eventarc.CreateChannelRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_channel

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Eventarc server.
        """
        return request, metadata

    def post_create_channel(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_channel

        DEPRECATED. Please use the `post_create_channel_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Eventarc server but before
        it is returned to user code. This `post_create_channel` interceptor runs
        before the `post_create_channel_with_metadata` interceptor.
        """
        return response

    def post_create_channel_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_channel

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Eventarc server but before it is returned to user code.

        We recommend only using this `post_create_channel_with_metadata`
        interceptor in new development instead of the `post_create_channel` interceptor.
        When both interceptors are used, this `post_create_channel_with_metadata` interceptor runs after the
        `post_create_channel` interceptor. The (possibly modified) response returned by
        `post_create_channel` will be passed to
        `post_create_channel_with_metadata`.
        """
        return response, metadata

    def pre_create_channel_connection(
        self,
        request: eventarc.CreateChannelConnectionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        eventarc.CreateChannelConnectionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_channel_connection

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Eventarc server.
        """
        return request, metadata

    def post_create_channel_connection(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_channel_connection

        DEPRECATED. Please use the `post_create_channel_connection_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Eventarc server but before
        it is returned to user code. This `post_create_channel_connection` interceptor runs
        before the `post_create_channel_connection_with_metadata` interceptor.
        """
        return response

    def post_create_channel_connection_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_channel_connection

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Eventarc server but before it is returned to user code.

        We recommend only using this `post_create_channel_connection_with_metadata`
        interceptor in new development instead of the `post_create_channel_connection` interceptor.
        When both interceptors are used, this `post_create_channel_connection_with_metadata` interceptor runs after the
        `post_create_channel_connection` interceptor. The (possibly modified) response returned by
        `post_create_channel_connection` will be passed to
        `post_create_channel_connection_with_metadata`.
        """
        return response, metadata

    def pre_create_enrollment(
        self,
        request: eventarc.CreateEnrollmentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        eventarc.CreateEnrollmentRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_enrollment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Eventarc server.
        """
        return request, metadata

    def post_create_enrollment(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_enrollment

        DEPRECATED. Please use the `post_create_enrollment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Eventarc server but before
        it is returned to user code. This `post_create_enrollment` interceptor runs
        before the `post_create_enrollment_with_metadata` interceptor.
        """
        return response

    def post_create_enrollment_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_enrollment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Eventarc server but before it is returned to user code.

        We recommend only using this `post_create_enrollment_with_metadata`
        interceptor in new development instead of the `post_create_enrollment` interceptor.
        When both interceptors are used, this `post_create_enrollment_with_metadata` interceptor runs after the
        `post_create_enrollment` interceptor. The (possibly modified) response returned by
        `post_create_enrollment` will be passed to
        `post_create_enrollment_with_metadata`.
        """
        return response, metadata

    def pre_create_google_api_source(
        self,
        request: eventarc.CreateGoogleApiSourceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        eventarc.CreateGoogleApiSourceRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_google_api_source

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Eventarc server.
        """
        return request, metadata

    def post_create_google_api_source(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_google_api_source

        DEPRECATED. Please use the `post_create_google_api_source_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Eventarc server but before
        it is returned to user code. This `post_create_google_api_source` interceptor runs
        before the `post_create_google_api_source_with_metadata` interceptor.
        """
        return response

    def post_create_google_api_source_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_google_api_source

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Eventarc server but before it is returned to user code.

        We recommend only using this `post_create_google_api_source_with_metadata`
        interceptor in new development instead of the `post_create_google_api_source` interceptor.
        When both interceptors are used, this `post_create_google_api_source_with_metadata` interceptor runs after the
        `post_create_google_api_source` interceptor. The (possibly modified) response returned by
        `post_create_google_api_source` will be passed to
        `post_create_google_api_source_with_metadata`.
        """
        return response, metadata

    def pre_create_message_bus(
        self,
        request: eventarc.CreateMessageBusRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        eventarc.CreateMessageBusRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_message_bus

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Eventarc server.
        """
        return request, metadata

    def post_create_message_bus(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_message_bus

        DEPRECATED. Please use the `post_create_message_bus_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Eventarc server but before
        it is returned to user code. This `post_create_message_bus` interceptor runs
        before the `post_create_message_bus_with_metadata` interceptor.
        """
        return response

    def post_create_message_bus_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_message_bus

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Eventarc server but before it is returned to user code.

        We recommend only using this `post_create_message_bus_with_metadata`
        interceptor in new development instead of the `post_create_message_bus` interceptor.
        When both interceptors are used, this `post_create_message_bus_with_metadata` interceptor runs after the
        `post_create_message_bus` interceptor. The (possibly modified) response returned by
        `post_create_message_bus` will be passed to
        `post_create_message_bus_with_metadata`.
        """
        return response, metadata

    def pre_create_pipeline(
        self,
        request: eventarc.CreatePipelineRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[eventarc.CreatePipelineRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_pipeline

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Eventarc server.
        """
        return request, metadata

    def post_create_pipeline(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_pipeline

        DEPRECATED. Please use the `post_create_pipeline_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Eventarc server but before
        it is returned to user code. This `post_create_pipeline` interceptor runs
        before the `post_create_pipeline_with_metadata` interceptor.
        """
        return response

    def post_create_pipeline_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_pipeline

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Eventarc server but before it is returned to user code.

        We recommend only using this `post_create_pipeline_with_metadata`
        interceptor in new development instead of the `post_create_pipeline` interceptor.
        When both interceptors are used, this `post_create_pipeline_with_metadata` interceptor runs after the
        `post_create_pipeline` interceptor. The (possibly modified) response returned by
        `post_create_pipeline` will be passed to
        `post_create_pipeline_with_metadata`.
        """
        return response, metadata

    def pre_create_trigger(
        self,
        request: eventarc.CreateTriggerRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[eventarc.CreateTriggerRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_trigger

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Eventarc server.
        """
        return request, metadata

    def post_create_trigger(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_trigger

        DEPRECATED. Please use the `post_create_trigger_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Eventarc server but before
        it is returned to user code. This `post_create_trigger` interceptor runs
        before the `post_create_trigger_with_metadata` interceptor.
        """
        return response

    def post_create_trigger_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_trigger

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Eventarc server but before it is returned to user code.

        We recommend only using this `post_create_trigger_with_metadata`
        interceptor in new development instead of the `post_create_trigger` interceptor.
        When both interceptors are used, this `post_create_trigger_with_metadata` interceptor runs after the
        `post_create_trigger` interceptor. The (possibly modified) response returned by
        `post_create_trigger` will be passed to
        `post_create_trigger_with_metadata`.
        """
        return response, metadata

    def pre_delete_channel(
        self,
        request: eventarc.DeleteChannelRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[eventarc.DeleteChannelRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_channel

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Eventarc server.
        """
        return request, metadata

    def post_delete_channel(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_channel

        DEPRECATED. Please use the `post_delete_channel_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Eventarc server but before
        it is returned to user code. This `post_delete_channel` interceptor runs
        before the `post_delete_channel_with_metadata` interceptor.
        """
        return response

    def post_delete_channel_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_channel

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Eventarc server but before it is returned to user code.

        We recommend only using this `post_delete_channel_with_metadata`
        interceptor in new development instead of the `post_delete_channel` interceptor.
        When both interceptors are used, this `post_delete_channel_with_metadata` interceptor runs after the
        `post_delete_channel` interceptor. The (possibly modified) response returned by
        `post_delete_channel` will be passed to
        `post_delete_channel_with_metadata`.
        """
        return response, metadata

    def pre_delete_channel_connection(
        self,
        request: eventarc.DeleteChannelConnectionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        eventarc.DeleteChannelConnectionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_channel_connection

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Eventarc server.
        """
        return request, metadata

    def post_delete_channel_connection(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_channel_connection

        DEPRECATED. Please use the `post_delete_channel_connection_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Eventarc server but before
        it is returned to user code. This `post_delete_channel_connection` interceptor runs
        before the `post_delete_channel_connection_with_metadata` interceptor.
        """
        return response

    def post_delete_channel_connection_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_channel_connection

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Eventarc server but before it is returned to user code.

        We recommend only using this `post_delete_channel_connection_with_metadata`
        interceptor in new development instead of the `post_delete_channel_connection` interceptor.
        When both interceptors are used, this `post_delete_channel_connection_with_metadata` interceptor runs after the
        `post_delete_channel_connection` interceptor. The (possibly modified) response returned by
        `post_delete_channel_connection` will be passed to
        `post_delete_channel_connection_with_metadata`.
        """
        return response, metadata

    def pre_delete_enrollment(
        self,
        request: eventarc.DeleteEnrollmentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        eventarc.DeleteEnrollmentRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_enrollment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Eventarc server.
        """
        return request, metadata

    def post_delete_enrollment(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_enrollment

        DEPRECATED. Please use the `post_delete_enrollment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Eventarc server but before
        it is returned to user code. This `post_delete_enrollment` interceptor runs
        before the `post_delete_enrollment_with_metadata` interceptor.
        """
        return response

    def post_delete_enrollment_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_enrollment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Eventarc server but before it is returned to user code.

        We recommend only using this `post_delete_enrollment_with_metadata`
        interceptor in new development instead of the `post_delete_enrollment` interceptor.
        When both interceptors are used, this `post_delete_enrollment_with_metadata` interceptor runs after the
        `post_delete_enrollment` interceptor. The (possibly modified) response returned by
        `post_delete_enrollment` will be passed to
        `post_delete_enrollment_with_metadata`.
        """
        return response, metadata

    def pre_delete_google_api_source(
        self,
        request: eventarc.DeleteGoogleApiSourceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        eventarc.DeleteGoogleApiSourceRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_google_api_source

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Eventarc server.
        """
        return request, metadata

    def post_delete_google_api_source(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_google_api_source

        DEPRECATED. Please use the `post_delete_google_api_source_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Eventarc server but before
        it is returned to user code. This `post_delete_google_api_source` interceptor runs
        before the `post_delete_google_api_source_with_metadata` interceptor.
        """
        return response

    def post_delete_google_api_source_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_google_api_source

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Eventarc server but before it is returned to user code.

        We recommend only using this `post_delete_google_api_source_with_metadata`
        interceptor in new development instead of the `post_delete_google_api_source` interceptor.
        When both interceptors are used, this `post_delete_google_api_source_with_metadata` interceptor runs after the
        `post_delete_google_api_source` interceptor. The (possibly modified) response returned by
        `post_delete_google_api_source` will be passed to
        `post_delete_google_api_source_with_metadata`.
        """
        return response, metadata

    def pre_delete_message_bus(
        self,
        request: eventarc.DeleteMessageBusRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        eventarc.DeleteMessageBusRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_message_bus

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Eventarc server.
        """
        return request, metadata

    def post_delete_message_bus(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_message_bus

        DEPRECATED. Please use the `post_delete_message_bus_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Eventarc server but before
        it is returned to user code. This `post_delete_message_bus` interceptor runs
        before the `post_delete_message_bus_with_metadata` interceptor.
        """
        return response

    def post_delete_message_bus_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_message_bus

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Eventarc server but before it is returned to user code.

        We recommend only using this `post_delete_message_bus_with_metadata`
        interceptor in new development instead of the `post_delete_message_bus` interceptor.
        When both interceptors are used, this `post_delete_message_bus_with_metadata` interceptor runs after the
        `post_delete_message_bus` interceptor. The (possibly modified) response returned by
        `post_delete_message_bus` will be passed to
        `post_delete_message_bus_with_metadata`.
        """
        return response, metadata

    def pre_delete_pipeline(
        self,
        request: eventarc.DeletePipelineRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[eventarc.DeletePipelineRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_pipeline

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Eventarc server.
        """
        return request, metadata

    def post_delete_pipeline(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_pipeline

        DEPRECATED. Please use the `post_delete_pipeline_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Eventarc server but before
        it is returned to user code. This `post_delete_pipeline` interceptor runs
        before the `post_delete_pipeline_with_metadata` interceptor.
        """
        return response

    def post_delete_pipeline_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_pipeline

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Eventarc server but before it is returned to user code.

        We recommend only using this `post_delete_pipeline_with_metadata`
        interceptor in new development instead of the `post_delete_pipeline` interceptor.
        When both interceptors are used, this `post_delete_pipeline_with_metadata` interceptor runs after the
        `post_delete_pipeline` interceptor. The (possibly modified) response returned by
        `post_delete_pipeline` will be passed to
        `post_delete_pipeline_with_metadata`.
        """
        return response, metadata

    def pre_delete_trigger(
        self,
        request: eventarc.DeleteTriggerRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[eventarc.DeleteTriggerRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_trigger

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Eventarc server.
        """
        return request, metadata

    def post_delete_trigger(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_trigger

        DEPRECATED. Please use the `post_delete_trigger_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Eventarc server but before
        it is returned to user code. This `post_delete_trigger` interceptor runs
        before the `post_delete_trigger_with_metadata` interceptor.
        """
        return response

    def post_delete_trigger_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_trigger

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Eventarc server but before it is returned to user code.

        We recommend only using this `post_delete_trigger_with_metadata`
        interceptor in new development instead of the `post_delete_trigger` interceptor.
        When both interceptors are used, this `post_delete_trigger_with_metadata` interceptor runs after the
        `post_delete_trigger` interceptor. The (possibly modified) response returned by
        `post_delete_trigger` will be passed to
        `post_delete_trigger_with_metadata`.
        """
        return response, metadata

    def pre_get_channel(
        self,
        request: eventarc.GetChannelRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[eventarc.GetChannelRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_channel

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Eventarc server.
        """
        return request, metadata

    def post_get_channel(self, response: channel.Channel) -> channel.Channel:
        """Post-rpc interceptor for get_channel

        DEPRECATED. Please use the `post_get_channel_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Eventarc server but before
        it is returned to user code. This `post_get_channel` interceptor runs
        before the `post_get_channel_with_metadata` interceptor.
        """
        return response

    def post_get_channel_with_metadata(
        self,
        response: channel.Channel,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[channel.Channel, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_channel

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Eventarc server but before it is returned to user code.

        We recommend only using this `post_get_channel_with_metadata`
        interceptor in new development instead of the `post_get_channel` interceptor.
        When both interceptors are used, this `post_get_channel_with_metadata` interceptor runs after the
        `post_get_channel` interceptor. The (possibly modified) response returned by
        `post_get_channel` will be passed to
        `post_get_channel_with_metadata`.
        """
        return response, metadata

    def pre_get_channel_connection(
        self,
        request: eventarc.GetChannelConnectionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        eventarc.GetChannelConnectionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_channel_connection

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Eventarc server.
        """
        return request, metadata

    def post_get_channel_connection(
        self, response: channel_connection.ChannelConnection
    ) -> channel_connection.ChannelConnection:
        """Post-rpc interceptor for get_channel_connection

        DEPRECATED. Please use the `post_get_channel_connection_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Eventarc server but before
        it is returned to user code. This `post_get_channel_connection` interceptor runs
        before the `post_get_channel_connection_with_metadata` interceptor.
        """
        return response

    def post_get_channel_connection_with_metadata(
        self,
        response: channel_connection.ChannelConnection,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        channel_connection.ChannelConnection, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_channel_connection

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Eventarc server but before it is returned to user code.

        We recommend only using this `post_get_channel_connection_with_metadata`
        interceptor in new development instead of the `post_get_channel_connection` interceptor.
        When both interceptors are used, this `post_get_channel_connection_with_metadata` interceptor runs after the
        `post_get_channel_connection` interceptor. The (possibly modified) response returned by
        `post_get_channel_connection` will be passed to
        `post_get_channel_connection_with_metadata`.
        """
        return response, metadata

    def pre_get_enrollment(
        self,
        request: eventarc.GetEnrollmentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[eventarc.GetEnrollmentRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_enrollment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Eventarc server.
        """
        return request, metadata

    def post_get_enrollment(
        self, response: enrollment.Enrollment
    ) -> enrollment.Enrollment:
        """Post-rpc interceptor for get_enrollment

        DEPRECATED. Please use the `post_get_enrollment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Eventarc server but before
        it is returned to user code. This `post_get_enrollment` interceptor runs
        before the `post_get_enrollment_with_metadata` interceptor.
        """
        return response

    def post_get_enrollment_with_metadata(
        self,
        response: enrollment.Enrollment,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[enrollment.Enrollment, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_enrollment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Eventarc server but before it is returned to user code.

        We recommend only using this `post_get_enrollment_with_metadata`
        interceptor in new development instead of the `post_get_enrollment` interceptor.
        When both interceptors are used, this `post_get_enrollment_with_metadata` interceptor runs after the
        `post_get_enrollment` interceptor. The (possibly modified) response returned by
        `post_get_enrollment` will be passed to
        `post_get_enrollment_with_metadata`.
        """
        return response, metadata

    def pre_get_google_api_source(
        self,
        request: eventarc.GetGoogleApiSourceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        eventarc.GetGoogleApiSourceRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_google_api_source

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Eventarc server.
        """
        return request, metadata

    def post_get_google_api_source(
        self, response: google_api_source.GoogleApiSource
    ) -> google_api_source.GoogleApiSource:
        """Post-rpc interceptor for get_google_api_source

        DEPRECATED. Please use the `post_get_google_api_source_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Eventarc server but before
        it is returned to user code. This `post_get_google_api_source` interceptor runs
        before the `post_get_google_api_source_with_metadata` interceptor.
        """
        return response

    def post_get_google_api_source_with_metadata(
        self,
        response: google_api_source.GoogleApiSource,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        google_api_source.GoogleApiSource, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_google_api_source

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Eventarc server but before it is returned to user code.

        We recommend only using this `post_get_google_api_source_with_metadata`
        interceptor in new development instead of the `post_get_google_api_source` interceptor.
        When both interceptors are used, this `post_get_google_api_source_with_metadata` interceptor runs after the
        `post_get_google_api_source` interceptor. The (possibly modified) response returned by
        `post_get_google_api_source` will be passed to
        `post_get_google_api_source_with_metadata`.
        """
        return response, metadata

    def pre_get_google_channel_config(
        self,
        request: eventarc.GetGoogleChannelConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        eventarc.GetGoogleChannelConfigRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_google_channel_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Eventarc server.
        """
        return request, metadata

    def post_get_google_channel_config(
        self, response: google_channel_config.GoogleChannelConfig
    ) -> google_channel_config.GoogleChannelConfig:
        """Post-rpc interceptor for get_google_channel_config

        DEPRECATED. Please use the `post_get_google_channel_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Eventarc server but before
        it is returned to user code. This `post_get_google_channel_config` interceptor runs
        before the `post_get_google_channel_config_with_metadata` interceptor.
        """
        return response

    def post_get_google_channel_config_with_metadata(
        self,
        response: google_channel_config.GoogleChannelConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        google_channel_config.GoogleChannelConfig,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_google_channel_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Eventarc server but before it is returned to user code.

        We recommend only using this `post_get_google_channel_config_with_metadata`
        interceptor in new development instead of the `post_get_google_channel_config` interceptor.
        When both interceptors are used, this `post_get_google_channel_config_with_metadata` interceptor runs after the
        `post_get_google_channel_config` interceptor. The (possibly modified) response returned by
        `post_get_google_channel_config` will be passed to
        `post_get_google_channel_config_with_metadata`.
        """
        return response, metadata

    def pre_get_message_bus(
        self,
        request: eventarc.GetMessageBusRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[eventarc.GetMessageBusRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_message_bus

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Eventarc server.
        """
        return request, metadata

    def post_get_message_bus(
        self, response: message_bus.MessageBus
    ) -> message_bus.MessageBus:
        """Post-rpc interceptor for get_message_bus

        DEPRECATED. Please use the `post_get_message_bus_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Eventarc server but before
        it is returned to user code. This `post_get_message_bus` interceptor runs
        before the `post_get_message_bus_with_metadata` interceptor.
        """
        return response

    def post_get_message_bus_with_metadata(
        self,
        response: message_bus.MessageBus,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[message_bus.MessageBus, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_message_bus

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Eventarc server but before it is returned to user code.

        We recommend only using this `post_get_message_bus_with_metadata`
        interceptor in new development instead of the `post_get_message_bus` interceptor.
        When both interceptors are used, this `post_get_message_bus_with_metadata` interceptor runs after the
        `post_get_message_bus` interceptor. The (possibly modified) response returned by
        `post_get_message_bus` will be passed to
        `post_get_message_bus_with_metadata`.
        """
        return response, metadata

    def pre_get_pipeline(
        self,
        request: eventarc.GetPipelineRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[eventarc.GetPipelineRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_pipeline

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Eventarc server.
        """
        return request, metadata

    def post_get_pipeline(self, response: pipeline.Pipeline) -> pipeline.Pipeline:
        """Post-rpc interceptor for get_pipeline

        DEPRECATED. Please use the `post_get_pipeline_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Eventarc server but before
        it is returned to user code. This `post_get_pipeline` interceptor runs
        before the `post_get_pipeline_with_metadata` interceptor.
        """
        return response

    def post_get_pipeline_with_metadata(
        self,
        response: pipeline.Pipeline,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[pipeline.Pipeline, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_pipeline

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Eventarc server but before it is returned to user code.

        We recommend only using this `post_get_pipeline_with_metadata`
        interceptor in new development instead of the `post_get_pipeline` interceptor.
        When both interceptors are used, this `post_get_pipeline_with_metadata` interceptor runs after the
        `post_get_pipeline` interceptor. The (possibly modified) response returned by
        `post_get_pipeline` will be passed to
        `post_get_pipeline_with_metadata`.
        """
        return response, metadata

    def pre_get_provider(
        self,
        request: eventarc.GetProviderRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[eventarc.GetProviderRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_provider

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Eventarc server.
        """
        return request, metadata

    def post_get_provider(self, response: discovery.Provider) -> discovery.Provider:
        """Post-rpc interceptor for get_provider

        DEPRECATED. Please use the `post_get_provider_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Eventarc server but before
        it is returned to user code. This `post_get_provider` interceptor runs
        before the `post_get_provider_with_metadata` interceptor.
        """
        return response

    def post_get_provider_with_metadata(
        self,
        response: discovery.Provider,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[discovery.Provider, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_provider

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Eventarc server but before it is returned to user code.

        We recommend only using this `post_get_provider_with_metadata`
        interceptor in new development instead of the `post_get_provider` interceptor.
        When both interceptors are used, this `post_get_provider_with_metadata` interceptor runs after the
        `post_get_provider` interceptor. The (possibly modified) response returned by
        `post_get_provider` will be passed to
        `post_get_provider_with_metadata`.
        """
        return response, metadata

    def pre_get_trigger(
        self,
        request: eventarc.GetTriggerRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[eventarc.GetTriggerRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_trigger

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Eventarc server.
        """
        return request, metadata

    def post_get_trigger(self, response: trigger.Trigger) -> trigger.Trigger:
        """Post-rpc interceptor for get_trigger

        DEPRECATED. Please use the `post_get_trigger_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Eventarc server but before
        it is returned to user code. This `post_get_trigger` interceptor runs
        before the `post_get_trigger_with_metadata` interceptor.
        """
        return response

    def post_get_trigger_with_metadata(
        self,
        response: trigger.Trigger,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[trigger.Trigger, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_trigger

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Eventarc server but before it is returned to user code.

        We recommend only using this `post_get_trigger_with_metadata`
        interceptor in new development instead of the `post_get_trigger` interceptor.
        When both interceptors are used, this `post_get_trigger_with_metadata` interceptor runs after the
        `post_get_trigger` interceptor. The (possibly modified) response returned by
        `post_get_trigger` will be passed to
        `post_get_trigger_with_metadata`.
        """
        return response, metadata

    def pre_list_channel_connections(
        self,
        request: eventarc.ListChannelConnectionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        eventarc.ListChannelConnectionsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_channel_connections

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Eventarc server.
        """
        return request, metadata

    def post_list_channel_connections(
        self, response: eventarc.ListChannelConnectionsResponse
    ) -> eventarc.ListChannelConnectionsResponse:
        """Post-rpc interceptor for list_channel_connections

        DEPRECATED. Please use the `post_list_channel_connections_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Eventarc server but before
        it is returned to user code. This `post_list_channel_connections` interceptor runs
        before the `post_list_channel_connections_with_metadata` interceptor.
        """
        return response

    def post_list_channel_connections_with_metadata(
        self,
        response: eventarc.ListChannelConnectionsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        eventarc.ListChannelConnectionsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_channel_connections

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Eventarc server but before it is returned to user code.

        We recommend only using this `post_list_channel_connections_with_metadata`
        interceptor in new development instead of the `post_list_channel_connections` interceptor.
        When both interceptors are used, this `post_list_channel_connections_with_metadata` interceptor runs after the
        `post_list_channel_connections` interceptor. The (possibly modified) response returned by
        `post_list_channel_connections` will be passed to
        `post_list_channel_connections_with_metadata`.
        """
        return response, metadata

    def pre_list_channels(
        self,
        request: eventarc.ListChannelsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[eventarc.ListChannelsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_channels

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Eventarc server.
        """
        return request, metadata

    def post_list_channels(
        self, response: eventarc.ListChannelsResponse
    ) -> eventarc.ListChannelsResponse:
        """Post-rpc interceptor for list_channels

        DEPRECATED. Please use the `post_list_channels_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Eventarc server but before
        it is returned to user code. This `post_list_channels` interceptor runs
        before the `post_list_channels_with_metadata` interceptor.
        """
        return response

    def post_list_channels_with_metadata(
        self,
        response: eventarc.ListChannelsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[eventarc.ListChannelsResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_channels

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Eventarc server but before it is returned to user code.

        We recommend only using this `post_list_channels_with_metadata`
        interceptor in new development instead of the `post_list_channels` interceptor.
        When both interceptors are used, this `post_list_channels_with_metadata` interceptor runs after the
        `post_list_channels` interceptor. The (possibly modified) response returned by
        `post_list_channels` will be passed to
        `post_list_channels_with_metadata`.
        """
        return response, metadata

    def pre_list_enrollments(
        self,
        request: eventarc.ListEnrollmentsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        eventarc.ListEnrollmentsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_enrollments

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Eventarc server.
        """
        return request, metadata

    def post_list_enrollments(
        self, response: eventarc.ListEnrollmentsResponse
    ) -> eventarc.ListEnrollmentsResponse:
        """Post-rpc interceptor for list_enrollments

        DEPRECATED. Please use the `post_list_enrollments_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Eventarc server but before
        it is returned to user code. This `post_list_enrollments` interceptor runs
        before the `post_list_enrollments_with_metadata` interceptor.
        """
        return response

    def post_list_enrollments_with_metadata(
        self,
        response: eventarc.ListEnrollmentsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        eventarc.ListEnrollmentsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_enrollments

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Eventarc server but before it is returned to user code.

        We recommend only using this `post_list_enrollments_with_metadata`
        interceptor in new development instead of the `post_list_enrollments` interceptor.
        When both interceptors are used, this `post_list_enrollments_with_metadata` interceptor runs after the
        `post_list_enrollments` interceptor. The (possibly modified) response returned by
        `post_list_enrollments` will be passed to
        `post_list_enrollments_with_metadata`.
        """
        return response, metadata

    def pre_list_google_api_sources(
        self,
        request: eventarc.ListGoogleApiSourcesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        eventarc.ListGoogleApiSourcesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_google_api_sources

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Eventarc server.
        """
        return request, metadata

    def post_list_google_api_sources(
        self, response: eventarc.ListGoogleApiSourcesResponse
    ) -> eventarc.ListGoogleApiSourcesResponse:
        """Post-rpc interceptor for list_google_api_sources

        DEPRECATED. Please use the `post_list_google_api_sources_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Eventarc server but before
        it is returned to user code. This `post_list_google_api_sources` interceptor runs
        before the `post_list_google_api_sources_with_metadata` interceptor.
        """
        return response

    def post_list_google_api_sources_with_metadata(
        self,
        response: eventarc.ListGoogleApiSourcesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        eventarc.ListGoogleApiSourcesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_google_api_sources

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Eventarc server but before it is returned to user code.

        We recommend only using this `post_list_google_api_sources_with_metadata`
        interceptor in new development instead of the `post_list_google_api_sources` interceptor.
        When both interceptors are used, this `post_list_google_api_sources_with_metadata` interceptor runs after the
        `post_list_google_api_sources` interceptor. The (possibly modified) response returned by
        `post_list_google_api_sources` will be passed to
        `post_list_google_api_sources_with_metadata`.
        """
        return response, metadata

    def pre_list_message_bus_enrollments(
        self,
        request: eventarc.ListMessageBusEnrollmentsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        eventarc.ListMessageBusEnrollmentsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_message_bus_enrollments

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Eventarc server.
        """
        return request, metadata

    def post_list_message_bus_enrollments(
        self, response: eventarc.ListMessageBusEnrollmentsResponse
    ) -> eventarc.ListMessageBusEnrollmentsResponse:
        """Post-rpc interceptor for list_message_bus_enrollments

        DEPRECATED. Please use the `post_list_message_bus_enrollments_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Eventarc server but before
        it is returned to user code. This `post_list_message_bus_enrollments` interceptor runs
        before the `post_list_message_bus_enrollments_with_metadata` interceptor.
        """
        return response

    def post_list_message_bus_enrollments_with_metadata(
        self,
        response: eventarc.ListMessageBusEnrollmentsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        eventarc.ListMessageBusEnrollmentsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_message_bus_enrollments

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Eventarc server but before it is returned to user code.

        We recommend only using this `post_list_message_bus_enrollments_with_metadata`
        interceptor in new development instead of the `post_list_message_bus_enrollments` interceptor.
        When both interceptors are used, this `post_list_message_bus_enrollments_with_metadata` interceptor runs after the
        `post_list_message_bus_enrollments` interceptor. The (possibly modified) response returned by
        `post_list_message_bus_enrollments` will be passed to
        `post_list_message_bus_enrollments_with_metadata`.
        """
        return response, metadata

    def pre_list_message_buses(
        self,
        request: eventarc.ListMessageBusesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        eventarc.ListMessageBusesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_message_buses

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Eventarc server.
        """
        return request, metadata

    def post_list_message_buses(
        self, response: eventarc.ListMessageBusesResponse
    ) -> eventarc.ListMessageBusesResponse:
        """Post-rpc interceptor for list_message_buses

        DEPRECATED. Please use the `post_list_message_buses_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Eventarc server but before
        it is returned to user code. This `post_list_message_buses` interceptor runs
        before the `post_list_message_buses_with_metadata` interceptor.
        """
        return response

    def post_list_message_buses_with_metadata(
        self,
        response: eventarc.ListMessageBusesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        eventarc.ListMessageBusesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_message_buses

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Eventarc server but before it is returned to user code.

        We recommend only using this `post_list_message_buses_with_metadata`
        interceptor in new development instead of the `post_list_message_buses` interceptor.
        When both interceptors are used, this `post_list_message_buses_with_metadata` interceptor runs after the
        `post_list_message_buses` interceptor. The (possibly modified) response returned by
        `post_list_message_buses` will be passed to
        `post_list_message_buses_with_metadata`.
        """
        return response, metadata

    def pre_list_pipelines(
        self,
        request: eventarc.ListPipelinesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[eventarc.ListPipelinesRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_pipelines

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Eventarc server.
        """
        return request, metadata

    def post_list_pipelines(
        self, response: eventarc.ListPipelinesResponse
    ) -> eventarc.ListPipelinesResponse:
        """Post-rpc interceptor for list_pipelines

        DEPRECATED. Please use the `post_list_pipelines_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Eventarc server but before
        it is returned to user code. This `post_list_pipelines` interceptor runs
        before the `post_list_pipelines_with_metadata` interceptor.
        """
        return response

    def post_list_pipelines_with_metadata(
        self,
        response: eventarc.ListPipelinesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[eventarc.ListPipelinesResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_pipelines

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Eventarc server but before it is returned to user code.

        We recommend only using this `post_list_pipelines_with_metadata`
        interceptor in new development instead of the `post_list_pipelines` interceptor.
        When both interceptors are used, this `post_list_pipelines_with_metadata` interceptor runs after the
        `post_list_pipelines` interceptor. The (possibly modified) response returned by
        `post_list_pipelines` will be passed to
        `post_list_pipelines_with_metadata`.
        """
        return response, metadata

    def pre_list_providers(
        self,
        request: eventarc.ListProvidersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[eventarc.ListProvidersRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_providers

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Eventarc server.
        """
        return request, metadata

    def post_list_providers(
        self, response: eventarc.ListProvidersResponse
    ) -> eventarc.ListProvidersResponse:
        """Post-rpc interceptor for list_providers

        DEPRECATED. Please use the `post_list_providers_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Eventarc server but before
        it is returned to user code. This `post_list_providers` interceptor runs
        before the `post_list_providers_with_metadata` interceptor.
        """
        return response

    def post_list_providers_with_metadata(
        self,
        response: eventarc.ListProvidersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[eventarc.ListProvidersResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_providers

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Eventarc server but before it is returned to user code.

        We recommend only using this `post_list_providers_with_metadata`
        interceptor in new development instead of the `post_list_providers` interceptor.
        When both interceptors are used, this `post_list_providers_with_metadata` interceptor runs after the
        `post_list_providers` interceptor. The (possibly modified) response returned by
        `post_list_providers` will be passed to
        `post_list_providers_with_metadata`.
        """
        return response, metadata

    def pre_list_triggers(
        self,
        request: eventarc.ListTriggersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[eventarc.ListTriggersRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_triggers

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Eventarc server.
        """
        return request, metadata

    def post_list_triggers(
        self, response: eventarc.ListTriggersResponse
    ) -> eventarc.ListTriggersResponse:
        """Post-rpc interceptor for list_triggers

        DEPRECATED. Please use the `post_list_triggers_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Eventarc server but before
        it is returned to user code. This `post_list_triggers` interceptor runs
        before the `post_list_triggers_with_metadata` interceptor.
        """
        return response

    def post_list_triggers_with_metadata(
        self,
        response: eventarc.ListTriggersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[eventarc.ListTriggersResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_triggers

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Eventarc server but before it is returned to user code.

        We recommend only using this `post_list_triggers_with_metadata`
        interceptor in new development instead of the `post_list_triggers` interceptor.
        When both interceptors are used, this `post_list_triggers_with_metadata` interceptor runs after the
        `post_list_triggers` interceptor. The (possibly modified) response returned by
        `post_list_triggers` will be passed to
        `post_list_triggers_with_metadata`.
        """
        return response, metadata

    def pre_update_channel(
        self,
        request: eventarc.UpdateChannelRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[eventarc.UpdateChannelRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_channel

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Eventarc server.
        """
        return request, metadata

    def post_update_channel(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_channel

        DEPRECATED. Please use the `post_update_channel_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Eventarc server but before
        it is returned to user code. This `post_update_channel` interceptor runs
        before the `post_update_channel_with_metadata` interceptor.
        """
        return response

    def post_update_channel_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_channel

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Eventarc server but before it is returned to user code.

        We recommend only using this `post_update_channel_with_metadata`
        interceptor in new development instead of the `post_update_channel` interceptor.
        When both interceptors are used, this `post_update_channel_with_metadata` interceptor runs after the
        `post_update_channel` interceptor. The (possibly modified) response returned by
        `post_update_channel` will be passed to
        `post_update_channel_with_metadata`.
        """
        return response, metadata

    def pre_update_enrollment(
        self,
        request: eventarc.UpdateEnrollmentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        eventarc.UpdateEnrollmentRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_enrollment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Eventarc server.
        """
        return request, metadata

    def post_update_enrollment(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_enrollment

        DEPRECATED. Please use the `post_update_enrollment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Eventarc server but before
        it is returned to user code. This `post_update_enrollment` interceptor runs
        before the `post_update_enrollment_with_metadata` interceptor.
        """
        return response

    def post_update_enrollment_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_enrollment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Eventarc server but before it is returned to user code.

        We recommend only using this `post_update_enrollment_with_metadata`
        interceptor in new development instead of the `post_update_enrollment` interceptor.
        When both interceptors are used, this `post_update_enrollment_with_metadata` interceptor runs after the
        `post_update_enrollment` interceptor. The (possibly modified) response returned by
        `post_update_enrollment` will be passed to
        `post_update_enrollment_with_metadata`.
        """
        return response, metadata

    def pre_update_google_api_source(
        self,
        request: eventarc.UpdateGoogleApiSourceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        eventarc.UpdateGoogleApiSourceRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_google_api_source

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Eventarc server.
        """
        return request, metadata

    def post_update_google_api_source(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_google_api_source

        DEPRECATED. Please use the `post_update_google_api_source_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Eventarc server but before
        it is returned to user code. This `post_update_google_api_source` interceptor runs
        before the `post_update_google_api_source_with_metadata` interceptor.
        """
        return response

    def post_update_google_api_source_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_google_api_source

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Eventarc server but before it is returned to user code.

        We recommend only using this `post_update_google_api_source_with_metadata`
        interceptor in new development instead of the `post_update_google_api_source` interceptor.
        When both interceptors are used, this `post_update_google_api_source_with_metadata` interceptor runs after the
        `post_update_google_api_source` interceptor. The (possibly modified) response returned by
        `post_update_google_api_source` will be passed to
        `post_update_google_api_source_with_metadata`.
        """
        return response, metadata

    def pre_update_google_channel_config(
        self,
        request: eventarc.UpdateGoogleChannelConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        eventarc.UpdateGoogleChannelConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_google_channel_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Eventarc server.
        """
        return request, metadata

    def post_update_google_channel_config(
        self, response: gce_google_channel_config.GoogleChannelConfig
    ) -> gce_google_channel_config.GoogleChannelConfig:
        """Post-rpc interceptor for update_google_channel_config

        DEPRECATED. Please use the `post_update_google_channel_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Eventarc server but before
        it is returned to user code. This `post_update_google_channel_config` interceptor runs
        before the `post_update_google_channel_config_with_metadata` interceptor.
        """
        return response

    def post_update_google_channel_config_with_metadata(
        self,
        response: gce_google_channel_config.GoogleChannelConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gce_google_channel_config.GoogleChannelConfig,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for update_google_channel_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Eventarc server but before it is returned to user code.

        We recommend only using this `post_update_google_channel_config_with_metadata`
        interceptor in new development instead of the `post_update_google_channel_config` interceptor.
        When both interceptors are used, this `post_update_google_channel_config_with_metadata` interceptor runs after the
        `post_update_google_channel_config` interceptor. The (possibly modified) response returned by
        `post_update_google_channel_config` will be passed to
        `post_update_google_channel_config_with_metadata`.
        """
        return response, metadata

    def pre_update_message_bus(
        self,
        request: eventarc.UpdateMessageBusRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        eventarc.UpdateMessageBusRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_message_bus

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Eventarc server.
        """
        return request, metadata

    def post_update_message_bus(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_message_bus

        DEPRECATED. Please use the `post_update_message_bus_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Eventarc server but before
        it is returned to user code. This `post_update_message_bus` interceptor runs
        before the `post_update_message_bus_with_metadata` interceptor.
        """
        return response

    def post_update_message_bus_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_message_bus

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Eventarc server but before it is returned to user code.

        We recommend only using this `post_update_message_bus_with_metadata`
        interceptor in new development instead of the `post_update_message_bus` interceptor.
        When both interceptors are used, this `post_update_message_bus_with_metadata` interceptor runs after the
        `post_update_message_bus` interceptor. The (possibly modified) response returned by
        `post_update_message_bus` will be passed to
        `post_update_message_bus_with_metadata`.
        """
        return response, metadata

    def pre_update_pipeline(
        self,
        request: eventarc.UpdatePipelineRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[eventarc.UpdatePipelineRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_pipeline

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Eventarc server.
        """
        return request, metadata

    def post_update_pipeline(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_pipeline

        DEPRECATED. Please use the `post_update_pipeline_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Eventarc server but before
        it is returned to user code. This `post_update_pipeline` interceptor runs
        before the `post_update_pipeline_with_metadata` interceptor.
        """
        return response

    def post_update_pipeline_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_pipeline

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Eventarc server but before it is returned to user code.

        We recommend only using this `post_update_pipeline_with_metadata`
        interceptor in new development instead of the `post_update_pipeline` interceptor.
        When both interceptors are used, this `post_update_pipeline_with_metadata` interceptor runs after the
        `post_update_pipeline` interceptor. The (possibly modified) response returned by
        `post_update_pipeline` will be passed to
        `post_update_pipeline_with_metadata`.
        """
        return response, metadata

    def pre_update_trigger(
        self,
        request: eventarc.UpdateTriggerRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[eventarc.UpdateTriggerRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_trigger

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Eventarc server.
        """
        return request, metadata

    def post_update_trigger(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_trigger

        DEPRECATED. Please use the `post_update_trigger_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Eventarc server but before
        it is returned to user code. This `post_update_trigger` interceptor runs
        before the `post_update_trigger_with_metadata` interceptor.
        """
        return response

    def post_update_trigger_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_trigger

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Eventarc server but before it is returned to user code.

        We recommend only using this `post_update_trigger_with_metadata`
        interceptor in new development instead of the `post_update_trigger` interceptor.
        When both interceptors are used, this `post_update_trigger_with_metadata` interceptor runs after the
        `post_update_trigger` interceptor. The (possibly modified) response returned by
        `post_update_trigger` will be passed to
        `post_update_trigger_with_metadata`.
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
        before they are sent to the Eventarc server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the Eventarc server but before
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
        before they are sent to the Eventarc server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the Eventarc server but before
        it is returned to user code.
        """
        return response

    def pre_get_iam_policy(
        self,
        request: iam_policy_pb2.GetIamPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        iam_policy_pb2.GetIamPolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Eventarc server.
        """
        return request, metadata

    def post_get_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the Eventarc server but before
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
        before they are sent to the Eventarc server.
        """
        return request, metadata

    def post_set_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the Eventarc server but before
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
        before they are sent to the Eventarc server.
        """
        return request, metadata

    def post_test_iam_permissions(
        self, response: iam_policy_pb2.TestIamPermissionsResponse
    ) -> iam_policy_pb2.TestIamPermissionsResponse:
        """Post-rpc interceptor for test_iam_permissions

        Override in a subclass to manipulate the response
        after it is returned by the Eventarc server but before
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
        before they are sent to the Eventarc server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the Eventarc server but before
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
        before they are sent to the Eventarc server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the Eventarc server but before
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
        before they are sent to the Eventarc server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the Eventarc server but before
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
        before they are sent to the Eventarc server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the Eventarc server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class EventarcRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: EventarcRestInterceptor


class EventarcRestTransport(_BaseEventarcRestTransport):
    """REST backend synchronous transport for Eventarc.

    Eventarc allows users to subscribe to various events that are
    provided by Google Cloud services and forward them to supported
    destinations.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "eventarc.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[EventarcRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'eventarc.googleapis.com').
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
            interceptor (Optional[EventarcRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or EventarcRestInterceptor()
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

    class _CreateChannel(
        _BaseEventarcRestTransport._BaseCreateChannel, EventarcRestStub
    ):
        def __hash__(self):
            return hash("EventarcRestTransport.CreateChannel")

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
            request: eventarc.CreateChannelRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create channel method over HTTP.

            Args:
                request (~.eventarc.CreateChannelRequest):
                    The request object. The request message for the
                CreateChannel method.
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
                _BaseEventarcRestTransport._BaseCreateChannel._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_channel(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEventarcRestTransport._BaseCreateChannel,
                    "_BaseCreateChannel__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.eventarc_v1.EventarcClient.CreateChannel",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "CreateChannel",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EventarcRestTransport._CreateChannel._get_response(
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

            resp = self._interceptor.post_create_channel(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_channel_with_metadata(
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
                    "Received response for google.cloud.eventarc_v1.EventarcClient.create_channel_",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "CreateChannel",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateChannelConnection(
        _BaseEventarcRestTransport._BaseCreateChannelConnection, EventarcRestStub
    ):
        def __hash__(self):
            return hash("EventarcRestTransport.CreateChannelConnection")

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
            request: eventarc.CreateChannelConnectionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create channel connection method over HTTP.

            Args:
                request (~.eventarc.CreateChannelConnectionRequest):
                    The request object. The request message for the
                CreateChannelConnection method.
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

            http_options = _BaseEventarcRestTransport._BaseCreateChannelConnection._get_http_options()
            request, metadata = self._interceptor.pre_create_channel_connection(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEventarcRestTransport._BaseCreateChannelConnection,
                    "_BaseCreateChannelConnection__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.eventarc_v1.EventarcClient.CreateChannelConnection",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "CreateChannelConnection",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EventarcRestTransport._CreateChannelConnection._get_response(
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

            resp = self._interceptor.post_create_channel_connection(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_channel_connection_with_metadata(
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
                    "Received response for google.cloud.eventarc_v1.EventarcClient.create_channel_connection",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "CreateChannelConnection",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateEnrollment(
        _BaseEventarcRestTransport._BaseCreateEnrollment, EventarcRestStub
    ):
        def __hash__(self):
            return hash("EventarcRestTransport.CreateEnrollment")

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
            request: eventarc.CreateEnrollmentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create enrollment method over HTTP.

            Args:
                request (~.eventarc.CreateEnrollmentRequest):
                    The request object. The request message for the
                CreateEnrollment method.
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
                _BaseEventarcRestTransport._BaseCreateEnrollment._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_enrollment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEventarcRestTransport._BaseCreateEnrollment,
                    "_BaseCreateEnrollment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.eventarc_v1.EventarcClient.CreateEnrollment",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "CreateEnrollment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EventarcRestTransport._CreateEnrollment._get_response(
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

            resp = self._interceptor.post_create_enrollment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_enrollment_with_metadata(
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
                    "Received response for google.cloud.eventarc_v1.EventarcClient.create_enrollment",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "CreateEnrollment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateGoogleApiSource(
        _BaseEventarcRestTransport._BaseCreateGoogleApiSource, EventarcRestStub
    ):
        def __hash__(self):
            return hash("EventarcRestTransport.CreateGoogleApiSource")

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
            request: eventarc.CreateGoogleApiSourceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create google api source method over HTTP.

            Args:
                request (~.eventarc.CreateGoogleApiSourceRequest):
                    The request object. The request message for the
                CreateGoogleApiSource method.
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

            http_options = _BaseEventarcRestTransport._BaseCreateGoogleApiSource._get_http_options()
            request, metadata = self._interceptor.pre_create_google_api_source(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEventarcRestTransport._BaseCreateGoogleApiSource,
                    "_BaseCreateGoogleApiSource__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.eventarc_v1.EventarcClient.CreateGoogleApiSource",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "CreateGoogleApiSource",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EventarcRestTransport._CreateGoogleApiSource._get_response(
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

            resp = self._interceptor.post_create_google_api_source(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_google_api_source_with_metadata(
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
                    "Received response for google.cloud.eventarc_v1.EventarcClient.create_google_api_source",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "CreateGoogleApiSource",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateMessageBus(
        _BaseEventarcRestTransport._BaseCreateMessageBus, EventarcRestStub
    ):
        def __hash__(self):
            return hash("EventarcRestTransport.CreateMessageBus")

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
            request: eventarc.CreateMessageBusRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create message bus method over HTTP.

            Args:
                request (~.eventarc.CreateMessageBusRequest):
                    The request object. The request message for the
                CreateMessageBus method.
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
                _BaseEventarcRestTransport._BaseCreateMessageBus._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_message_bus(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEventarcRestTransport._BaseCreateMessageBus,
                    "_BaseCreateMessageBus__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.eventarc_v1.EventarcClient.CreateMessageBus",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "CreateMessageBus",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EventarcRestTransport._CreateMessageBus._get_response(
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

            resp = self._interceptor.post_create_message_bus(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_message_bus_with_metadata(
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
                    "Received response for google.cloud.eventarc_v1.EventarcClient.create_message_bus",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "CreateMessageBus",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreatePipeline(
        _BaseEventarcRestTransport._BaseCreatePipeline, EventarcRestStub
    ):
        def __hash__(self):
            return hash("EventarcRestTransport.CreatePipeline")

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
            request: eventarc.CreatePipelineRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create pipeline method over HTTP.

            Args:
                request (~.eventarc.CreatePipelineRequest):
                    The request object. The request message for the
                CreatePipeline method.
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
                _BaseEventarcRestTransport._BaseCreatePipeline._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_pipeline(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEventarcRestTransport._BaseCreatePipeline,
                    "_BaseCreatePipeline__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.eventarc_v1.EventarcClient.CreatePipeline",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "CreatePipeline",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EventarcRestTransport._CreatePipeline._get_response(
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

            resp = self._interceptor.post_create_pipeline(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_pipeline_with_metadata(
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
                    "Received response for google.cloud.eventarc_v1.EventarcClient.create_pipeline",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "CreatePipeline",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateTrigger(
        _BaseEventarcRestTransport._BaseCreateTrigger, EventarcRestStub
    ):
        def __hash__(self):
            return hash("EventarcRestTransport.CreateTrigger")

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
            request: eventarc.CreateTriggerRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create trigger method over HTTP.

            Args:
                request (~.eventarc.CreateTriggerRequest):
                    The request object. The request message for the
                CreateTrigger method.
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
                _BaseEventarcRestTransport._BaseCreateTrigger._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_trigger(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEventarcRestTransport._BaseCreateTrigger,
                    "_BaseCreateTrigger__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.eventarc_v1.EventarcClient.CreateTrigger",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "CreateTrigger",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EventarcRestTransport._CreateTrigger._get_response(
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

            resp = self._interceptor.post_create_trigger(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_trigger_with_metadata(
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
                    "Received response for google.cloud.eventarc_v1.EventarcClient.create_trigger",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "CreateTrigger",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteChannel(
        _BaseEventarcRestTransport._BaseDeleteChannel, EventarcRestStub
    ):
        def __hash__(self):
            return hash("EventarcRestTransport.DeleteChannel")

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
            request: eventarc.DeleteChannelRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete channel method over HTTP.

            Args:
                request (~.eventarc.DeleteChannelRequest):
                    The request object. The request message for the
                DeleteChannel method.
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
                _BaseEventarcRestTransport._BaseDeleteChannel._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_channel(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEventarcRestTransport._BaseDeleteChannel,
                    "_BaseDeleteChannel__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.eventarc_v1.EventarcClient.DeleteChannel",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "DeleteChannel",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EventarcRestTransport._DeleteChannel._get_response(
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

            resp = self._interceptor.post_delete_channel(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_channel_with_metadata(
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
                    "Received response for google.cloud.eventarc_v1.EventarcClient.delete_channel",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "DeleteChannel",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteChannelConnection(
        _BaseEventarcRestTransport._BaseDeleteChannelConnection, EventarcRestStub
    ):
        def __hash__(self):
            return hash("EventarcRestTransport.DeleteChannelConnection")

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
            request: eventarc.DeleteChannelConnectionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete channel connection method over HTTP.

            Args:
                request (~.eventarc.DeleteChannelConnectionRequest):
                    The request object. The request message for the
                DeleteChannelConnection method.
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

            http_options = _BaseEventarcRestTransport._BaseDeleteChannelConnection._get_http_options()
            request, metadata = self._interceptor.pre_delete_channel_connection(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEventarcRestTransport._BaseDeleteChannelConnection,
                    "_BaseDeleteChannelConnection__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.eventarc_v1.EventarcClient.DeleteChannelConnection",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "DeleteChannelConnection",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EventarcRestTransport._DeleteChannelConnection._get_response(
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

            resp = self._interceptor.post_delete_channel_connection(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_channel_connection_with_metadata(
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
                    "Received response for google.cloud.eventarc_v1.EventarcClient.delete_channel_connection",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "DeleteChannelConnection",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteEnrollment(
        _BaseEventarcRestTransport._BaseDeleteEnrollment, EventarcRestStub
    ):
        def __hash__(self):
            return hash("EventarcRestTransport.DeleteEnrollment")

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
            request: eventarc.DeleteEnrollmentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete enrollment method over HTTP.

            Args:
                request (~.eventarc.DeleteEnrollmentRequest):
                    The request object. The request message for the
                DeleteEnrollment method.
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
                _BaseEventarcRestTransport._BaseDeleteEnrollment._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_enrollment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEventarcRestTransport._BaseDeleteEnrollment,
                    "_BaseDeleteEnrollment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.eventarc_v1.EventarcClient.DeleteEnrollment",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "DeleteEnrollment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EventarcRestTransport._DeleteEnrollment._get_response(
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

            resp = self._interceptor.post_delete_enrollment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_enrollment_with_metadata(
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
                    "Received response for google.cloud.eventarc_v1.EventarcClient.delete_enrollment",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "DeleteEnrollment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteGoogleApiSource(
        _BaseEventarcRestTransport._BaseDeleteGoogleApiSource, EventarcRestStub
    ):
        def __hash__(self):
            return hash("EventarcRestTransport.DeleteGoogleApiSource")

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
            request: eventarc.DeleteGoogleApiSourceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete google api source method over HTTP.

            Args:
                request (~.eventarc.DeleteGoogleApiSourceRequest):
                    The request object. The request message for the
                DeleteGoogleApiSource method.
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

            http_options = _BaseEventarcRestTransport._BaseDeleteGoogleApiSource._get_http_options()
            request, metadata = self._interceptor.pre_delete_google_api_source(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEventarcRestTransport._BaseDeleteGoogleApiSource,
                    "_BaseDeleteGoogleApiSource__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.eventarc_v1.EventarcClient.DeleteGoogleApiSource",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "DeleteGoogleApiSource",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EventarcRestTransport._DeleteGoogleApiSource._get_response(
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

            resp = self._interceptor.post_delete_google_api_source(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_google_api_source_with_metadata(
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
                    "Received response for google.cloud.eventarc_v1.EventarcClient.delete_google_api_source",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "DeleteGoogleApiSource",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteMessageBus(
        _BaseEventarcRestTransport._BaseDeleteMessageBus, EventarcRestStub
    ):
        def __hash__(self):
            return hash("EventarcRestTransport.DeleteMessageBus")

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
            request: eventarc.DeleteMessageBusRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete message bus method over HTTP.

            Args:
                request (~.eventarc.DeleteMessageBusRequest):
                    The request object. The request message for the
                DeleteMessageBus method.
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
                _BaseEventarcRestTransport._BaseDeleteMessageBus._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_message_bus(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEventarcRestTransport._BaseDeleteMessageBus,
                    "_BaseDeleteMessageBus__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.eventarc_v1.EventarcClient.DeleteMessageBus",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "DeleteMessageBus",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EventarcRestTransport._DeleteMessageBus._get_response(
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

            resp = self._interceptor.post_delete_message_bus(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_message_bus_with_metadata(
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
                    "Received response for google.cloud.eventarc_v1.EventarcClient.delete_message_bus",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "DeleteMessageBus",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeletePipeline(
        _BaseEventarcRestTransport._BaseDeletePipeline, EventarcRestStub
    ):
        def __hash__(self):
            return hash("EventarcRestTransport.DeletePipeline")

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
            request: eventarc.DeletePipelineRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete pipeline method over HTTP.

            Args:
                request (~.eventarc.DeletePipelineRequest):
                    The request object. The request message for the
                DeletePipeline method.
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
                _BaseEventarcRestTransport._BaseDeletePipeline._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_pipeline(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEventarcRestTransport._BaseDeletePipeline,
                    "_BaseDeletePipeline__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.eventarc_v1.EventarcClient.DeletePipeline",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "DeletePipeline",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EventarcRestTransport._DeletePipeline._get_response(
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

            resp = self._interceptor.post_delete_pipeline(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_pipeline_with_metadata(
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
                    "Received response for google.cloud.eventarc_v1.EventarcClient.delete_pipeline",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "DeletePipeline",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteTrigger(
        _BaseEventarcRestTransport._BaseDeleteTrigger, EventarcRestStub
    ):
        def __hash__(self):
            return hash("EventarcRestTransport.DeleteTrigger")

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
            request: eventarc.DeleteTriggerRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete trigger method over HTTP.

            Args:
                request (~.eventarc.DeleteTriggerRequest):
                    The request object. The request message for the
                DeleteTrigger method.
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
                _BaseEventarcRestTransport._BaseDeleteTrigger._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_trigger(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEventarcRestTransport._BaseDeleteTrigger,
                    "_BaseDeleteTrigger__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.eventarc_v1.EventarcClient.DeleteTrigger",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "DeleteTrigger",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EventarcRestTransport._DeleteTrigger._get_response(
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

            resp = self._interceptor.post_delete_trigger(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_trigger_with_metadata(
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
                    "Received response for google.cloud.eventarc_v1.EventarcClient.delete_trigger",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "DeleteTrigger",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetChannel(_BaseEventarcRestTransport._BaseGetChannel, EventarcRestStub):
        def __hash__(self):
            return hash("EventarcRestTransport.GetChannel")

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
            request: eventarc.GetChannelRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> channel.Channel:
            r"""Call the get channel method over HTTP.

            Args:
                request (~.eventarc.GetChannelRequest):
                    The request object. The request message for the
                GetChannel method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.channel.Channel:
                    A representation of the Channel
                resource. A Channel is a resource on
                which event providers publish their
                events. The published events are
                delivered through the transport
                associated with the channel. Note that a
                channel is associated with exactly one
                event provider.

            """

            http_options = (
                _BaseEventarcRestTransport._BaseGetChannel._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_channel(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEventarcRestTransport._BaseGetChannel,
                    "_BaseGetChannel__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.eventarc_v1.EventarcClient.GetChannel",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "GetChannel",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EventarcRestTransport._GetChannel._get_response(
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
            resp = channel.Channel()
            pb_resp = channel.Channel.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_channel(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_channel_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = channel.Channel.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.eventarc_v1.EventarcClient.get_channel",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "GetChannel",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetChannelConnection(
        _BaseEventarcRestTransport._BaseGetChannelConnection, EventarcRestStub
    ):
        def __hash__(self):
            return hash("EventarcRestTransport.GetChannelConnection")

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
            request: eventarc.GetChannelConnectionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> channel_connection.ChannelConnection:
            r"""Call the get channel connection method over HTTP.

            Args:
                request (~.eventarc.GetChannelConnectionRequest):
                    The request object. The request message for the
                GetChannelConnection method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.channel_connection.ChannelConnection:
                    A representation of the
                ChannelConnection resource. A
                ChannelConnection is a resource which
                event providers create during the
                activation process to establish a
                connection between the provider and the
                subscriber channel.

            """

            http_options = (
                _BaseEventarcRestTransport._BaseGetChannelConnection._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_channel_connection(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEventarcRestTransport._BaseGetChannelConnection,
                    "_BaseGetChannelConnection__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.eventarc_v1.EventarcClient.GetChannelConnection",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "GetChannelConnection",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EventarcRestTransport._GetChannelConnection._get_response(
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
            resp = channel_connection.ChannelConnection()
            pb_resp = channel_connection.ChannelConnection.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_channel_connection(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_channel_connection_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = channel_connection.ChannelConnection.to_json(
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
                    "Received response for google.cloud.eventarc_v1.EventarcClient.get_channel_connection",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "GetChannelConnection",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetEnrollment(
        _BaseEventarcRestTransport._BaseGetEnrollment, EventarcRestStub
    ):
        def __hash__(self):
            return hash("EventarcRestTransport.GetEnrollment")

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
            request: eventarc.GetEnrollmentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> enrollment.Enrollment:
            r"""Call the get enrollment method over HTTP.

            Args:
                request (~.eventarc.GetEnrollmentRequest):
                    The request object. The request message for the
                GetEnrollment method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.enrollment.Enrollment:
                    An enrollment represents a
                subscription for messages on a
                particular message bus. It defines a
                matching criteria for messages on the
                bus and the subscriber endpoint where
                matched messages should be delivered.

            """

            http_options = (
                _BaseEventarcRestTransport._BaseGetEnrollment._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_enrollment(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEventarcRestTransport._BaseGetEnrollment,
                    "_BaseGetEnrollment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.eventarc_v1.EventarcClient.GetEnrollment",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "GetEnrollment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EventarcRestTransport._GetEnrollment._get_response(
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
            resp = enrollment.Enrollment()
            pb_resp = enrollment.Enrollment.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_enrollment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_enrollment_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = enrollment.Enrollment.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.eventarc_v1.EventarcClient.get_enrollment",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "GetEnrollment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetGoogleApiSource(
        _BaseEventarcRestTransport._BaseGetGoogleApiSource, EventarcRestStub
    ):
        def __hash__(self):
            return hash("EventarcRestTransport.GetGoogleApiSource")

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
            request: eventarc.GetGoogleApiSourceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> google_api_source.GoogleApiSource:
            r"""Call the get google api source method over HTTP.

            Args:
                request (~.eventarc.GetGoogleApiSourceRequest):
                    The request object. The request message for the
                GetGoogleApiSource method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.google_api_source.GoogleApiSource:
                    A GoogleApiSource represents a
                subscription of 1P events from a
                MessageBus.

            """

            http_options = (
                _BaseEventarcRestTransport._BaseGetGoogleApiSource._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_google_api_source(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEventarcRestTransport._BaseGetGoogleApiSource,
                    "_BaseGetGoogleApiSource__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.eventarc_v1.EventarcClient.GetGoogleApiSource",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "GetGoogleApiSource",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EventarcRestTransport._GetGoogleApiSource._get_response(
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
            resp = google_api_source.GoogleApiSource()
            pb_resp = google_api_source.GoogleApiSource.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_google_api_source(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_google_api_source_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = google_api_source.GoogleApiSource.to_json(
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
                    "Received response for google.cloud.eventarc_v1.EventarcClient.get_google_api_source",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "GetGoogleApiSource",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetGoogleChannelConfig(
        _BaseEventarcRestTransport._BaseGetGoogleChannelConfig, EventarcRestStub
    ):
        def __hash__(self):
            return hash("EventarcRestTransport.GetGoogleChannelConfig")

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
            request: eventarc.GetGoogleChannelConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> google_channel_config.GoogleChannelConfig:
            r"""Call the get google channel config method over HTTP.

            Args:
                request (~.eventarc.GetGoogleChannelConfigRequest):
                    The request object. The request message for the
                GetGoogleChannelConfig method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.google_channel_config.GoogleChannelConfig:
                    A GoogleChannelConfig is a resource
                that stores the custom settings
                respected by Eventarc first-party
                triggers in the matching region. Once
                configured, first-party event data will
                be protected using the specified custom
                managed encryption key instead of
                Google-managed encryption keys.

            """

            http_options = _BaseEventarcRestTransport._BaseGetGoogleChannelConfig._get_http_options()
            request, metadata = self._interceptor.pre_get_google_channel_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEventarcRestTransport._BaseGetGoogleChannelConfig,
                    "_BaseGetGoogleChannelConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.eventarc_v1.EventarcClient.GetGoogleChannelConfig",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "GetGoogleChannelConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EventarcRestTransport._GetGoogleChannelConfig._get_response(
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
            resp = google_channel_config.GoogleChannelConfig()
            pb_resp = google_channel_config.GoogleChannelConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_google_channel_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_google_channel_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        google_channel_config.GoogleChannelConfig.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.eventarc_v1.EventarcClient.get_google_channel_config",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "GetGoogleChannelConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetMessageBus(
        _BaseEventarcRestTransport._BaseGetMessageBus, EventarcRestStub
    ):
        def __hash__(self):
            return hash("EventarcRestTransport.GetMessageBus")

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
            request: eventarc.GetMessageBusRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> message_bus.MessageBus:
            r"""Call the get message bus method over HTTP.

            Args:
                request (~.eventarc.GetMessageBusRequest):
                    The request object. The request message for the
                GetMessageBus method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.message_bus.MessageBus:
                    MessageBus for the messages flowing
                through the system. The admin has
                visibility and control over the messages
                being published and consumed and can
                restrict publishers and subscribers to
                only a subset of data available in the
                system by defining authorization
                policies.

            """

            http_options = (
                _BaseEventarcRestTransport._BaseGetMessageBus._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_message_bus(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEventarcRestTransport._BaseGetMessageBus,
                    "_BaseGetMessageBus__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.eventarc_v1.EventarcClient.GetMessageBus",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "GetMessageBus",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EventarcRestTransport._GetMessageBus._get_response(
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
            resp = message_bus.MessageBus()
            pb_resp = message_bus.MessageBus.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_message_bus(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_message_bus_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = message_bus.MessageBus.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.eventarc_v1.EventarcClient.get_message_bus",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "GetMessageBus",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetPipeline(_BaseEventarcRestTransport._BaseGetPipeline, EventarcRestStub):
        def __hash__(self):
            return hash("EventarcRestTransport.GetPipeline")

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
            request: eventarc.GetPipelineRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> pipeline.Pipeline:
            r"""Call the get pipeline method over HTTP.

            Args:
                request (~.eventarc.GetPipelineRequest):
                    The request object. The request message for the
                GetPipeline method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.pipeline.Pipeline:
                    A representation of the Pipeline
                resource.

            """

            http_options = (
                _BaseEventarcRestTransport._BaseGetPipeline._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_pipeline(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEventarcRestTransport._BaseGetPipeline,
                    "_BaseGetPipeline__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.eventarc_v1.EventarcClient.GetPipeline",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "GetPipeline",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EventarcRestTransport._GetPipeline._get_response(
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
            resp = pipeline.Pipeline()
            pb_resp = pipeline.Pipeline.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_pipeline(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_pipeline_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = pipeline.Pipeline.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.eventarc_v1.EventarcClient.get_pipeline",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "GetPipeline",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetProvider(_BaseEventarcRestTransport._BaseGetProvider, EventarcRestStub):
        def __hash__(self):
            return hash("EventarcRestTransport.GetProvider")

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
            request: eventarc.GetProviderRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> discovery.Provider:
            r"""Call the get provider method over HTTP.

            Args:
                request (~.eventarc.GetProviderRequest):
                    The request object. The request message for the
                GetProvider method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.discovery.Provider:
                    A representation of the Provider
                resource.

            """

            http_options = (
                _BaseEventarcRestTransport._BaseGetProvider._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_provider(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEventarcRestTransport._BaseGetProvider,
                    "_BaseGetProvider__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.eventarc_v1.EventarcClient.GetProvider",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "GetProvider",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EventarcRestTransport._GetProvider._get_response(
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
            resp = discovery.Provider()
            pb_resp = discovery.Provider.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_provider(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_provider_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = discovery.Provider.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.eventarc_v1.EventarcClient.get_provider",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "GetProvider",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetTrigger(_BaseEventarcRestTransport._BaseGetTrigger, EventarcRestStub):
        def __hash__(self):
            return hash("EventarcRestTransport.GetTrigger")

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
            request: eventarc.GetTriggerRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> trigger.Trigger:
            r"""Call the get trigger method over HTTP.

            Args:
                request (~.eventarc.GetTriggerRequest):
                    The request object. The request message for the
                GetTrigger method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.trigger.Trigger:
                    A representation of the trigger
                resource.

            """

            http_options = (
                _BaseEventarcRestTransport._BaseGetTrigger._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_trigger(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEventarcRestTransport._BaseGetTrigger,
                    "_BaseGetTrigger__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.eventarc_v1.EventarcClient.GetTrigger",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "GetTrigger",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EventarcRestTransport._GetTrigger._get_response(
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
            resp = trigger.Trigger()
            pb_resp = trigger.Trigger.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_trigger(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_trigger_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = trigger.Trigger.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.eventarc_v1.EventarcClient.get_trigger",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "GetTrigger",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListChannelConnections(
        _BaseEventarcRestTransport._BaseListChannelConnections, EventarcRestStub
    ):
        def __hash__(self):
            return hash("EventarcRestTransport.ListChannelConnections")

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
            request: eventarc.ListChannelConnectionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> eventarc.ListChannelConnectionsResponse:
            r"""Call the list channel connections method over HTTP.

            Args:
                request (~.eventarc.ListChannelConnectionsRequest):
                    The request object. The request message for the
                ListChannelConnections method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.eventarc.ListChannelConnectionsResponse:
                    The response message for the ``ListChannelConnections``
                method.

            """

            http_options = _BaseEventarcRestTransport._BaseListChannelConnections._get_http_options()
            request, metadata = self._interceptor.pre_list_channel_connections(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEventarcRestTransport._BaseListChannelConnections,
                    "_BaseListChannelConnections__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.eventarc_v1.EventarcClient.ListChannelConnections",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "ListChannelConnections",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EventarcRestTransport._ListChannelConnections._get_response(
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
            resp = eventarc.ListChannelConnectionsResponse()
            pb_resp = eventarc.ListChannelConnectionsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_channel_connections(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_channel_connections_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = eventarc.ListChannelConnectionsResponse.to_json(
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
                    "Received response for google.cloud.eventarc_v1.EventarcClient.list_channel_connections",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "ListChannelConnections",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListChannels(_BaseEventarcRestTransport._BaseListChannels, EventarcRestStub):
        def __hash__(self):
            return hash("EventarcRestTransport.ListChannels")

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
            request: eventarc.ListChannelsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> eventarc.ListChannelsResponse:
            r"""Call the list channels method over HTTP.

            Args:
                request (~.eventarc.ListChannelsRequest):
                    The request object. The request message for the
                ListChannels method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.eventarc.ListChannelsResponse:
                    The response message for the ``ListChannels`` method.
            """

            http_options = (
                _BaseEventarcRestTransport._BaseListChannels._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_channels(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEventarcRestTransport._BaseListChannels,
                    "_BaseListChannels__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.eventarc_v1.EventarcClient.ListChannels",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "ListChannels",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EventarcRestTransport._ListChannels._get_response(
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
            resp = eventarc.ListChannelsResponse()
            pb_resp = eventarc.ListChannelsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_channels(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_channels_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = eventarc.ListChannelsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.eventarc_v1.EventarcClient.list_channels",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "ListChannels",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListEnrollments(
        _BaseEventarcRestTransport._BaseListEnrollments, EventarcRestStub
    ):
        def __hash__(self):
            return hash("EventarcRestTransport.ListEnrollments")

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
            request: eventarc.ListEnrollmentsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> eventarc.ListEnrollmentsResponse:
            r"""Call the list enrollments method over HTTP.

            Args:
                request (~.eventarc.ListEnrollmentsRequest):
                    The request object. The request message for the
                ListEnrollments method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.eventarc.ListEnrollmentsResponse:
                    The response message for the ``ListEnrollments`` method.
            """

            http_options = (
                _BaseEventarcRestTransport._BaseListEnrollments._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_enrollments(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEventarcRestTransport._BaseListEnrollments,
                    "_BaseListEnrollments__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.eventarc_v1.EventarcClient.ListEnrollments",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "ListEnrollments",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EventarcRestTransport._ListEnrollments._get_response(
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
            resp = eventarc.ListEnrollmentsResponse()
            pb_resp = eventarc.ListEnrollmentsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_enrollments(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_enrollments_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = eventarc.ListEnrollmentsResponse.to_json(
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
                    "Received response for google.cloud.eventarc_v1.EventarcClient.list_enrollments",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "ListEnrollments",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListGoogleApiSources(
        _BaseEventarcRestTransport._BaseListGoogleApiSources, EventarcRestStub
    ):
        def __hash__(self):
            return hash("EventarcRestTransport.ListGoogleApiSources")

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
            request: eventarc.ListGoogleApiSourcesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> eventarc.ListGoogleApiSourcesResponse:
            r"""Call the list google api sources method over HTTP.

            Args:
                request (~.eventarc.ListGoogleApiSourcesRequest):
                    The request object. The request message for the
                ListGoogleApiSources method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.eventarc.ListGoogleApiSourcesResponse:
                    The response message for the ``ListGoogleApiSources``
                method.

            """

            http_options = (
                _BaseEventarcRestTransport._BaseListGoogleApiSources._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_google_api_sources(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEventarcRestTransport._BaseListGoogleApiSources,
                    "_BaseListGoogleApiSources__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.eventarc_v1.EventarcClient.ListGoogleApiSources",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "ListGoogleApiSources",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EventarcRestTransport._ListGoogleApiSources._get_response(
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
            resp = eventarc.ListGoogleApiSourcesResponse()
            pb_resp = eventarc.ListGoogleApiSourcesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_google_api_sources(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_google_api_sources_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = eventarc.ListGoogleApiSourcesResponse.to_json(
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
                    "Received response for google.cloud.eventarc_v1.EventarcClient.list_google_api_sources",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "ListGoogleApiSources",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListMessageBusEnrollments(
        _BaseEventarcRestTransport._BaseListMessageBusEnrollments, EventarcRestStub
    ):
        def __hash__(self):
            return hash("EventarcRestTransport.ListMessageBusEnrollments")

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
            request: eventarc.ListMessageBusEnrollmentsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> eventarc.ListMessageBusEnrollmentsResponse:
            r"""Call the list message bus
            enrollments method over HTTP.

                Args:
                    request (~.eventarc.ListMessageBusEnrollmentsRequest):
                        The request object. The request message for the
                    ``ListMessageBusEnrollments`` method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.eventarc.ListMessageBusEnrollmentsResponse:
                        The response message for the
                    ``ListMessageBusEnrollments`` method.\`

            """

            http_options = _BaseEventarcRestTransport._BaseListMessageBusEnrollments._get_http_options()
            request, metadata = self._interceptor.pre_list_message_bus_enrollments(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEventarcRestTransport._BaseListMessageBusEnrollments,
                    "_BaseListMessageBusEnrollments__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.eventarc_v1.EventarcClient.ListMessageBusEnrollments",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "ListMessageBusEnrollments",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EventarcRestTransport._ListMessageBusEnrollments._get_response(
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
            resp = eventarc.ListMessageBusEnrollmentsResponse()
            pb_resp = eventarc.ListMessageBusEnrollmentsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_message_bus_enrollments(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_message_bus_enrollments_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        eventarc.ListMessageBusEnrollmentsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.eventarc_v1.EventarcClient.list_message_bus_enrollments",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "ListMessageBusEnrollments",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListMessageBuses(
        _BaseEventarcRestTransport._BaseListMessageBuses, EventarcRestStub
    ):
        def __hash__(self):
            return hash("EventarcRestTransport.ListMessageBuses")

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
            request: eventarc.ListMessageBusesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> eventarc.ListMessageBusesResponse:
            r"""Call the list message buses method over HTTP.

            Args:
                request (~.eventarc.ListMessageBusesRequest):
                    The request object. The request message for the
                ListMessageBuses method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.eventarc.ListMessageBusesResponse:
                    The response message for the ``ListMessageBuses``
                method.

            """

            http_options = (
                _BaseEventarcRestTransport._BaseListMessageBuses._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_message_buses(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEventarcRestTransport._BaseListMessageBuses,
                    "_BaseListMessageBuses__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.eventarc_v1.EventarcClient.ListMessageBuses",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "ListMessageBuses",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EventarcRestTransport._ListMessageBuses._get_response(
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
            resp = eventarc.ListMessageBusesResponse()
            pb_resp = eventarc.ListMessageBusesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_message_buses(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_message_buses_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = eventarc.ListMessageBusesResponse.to_json(
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
                    "Received response for google.cloud.eventarc_v1.EventarcClient.list_message_buses",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "ListMessageBuses",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListPipelines(
        _BaseEventarcRestTransport._BaseListPipelines, EventarcRestStub
    ):
        def __hash__(self):
            return hash("EventarcRestTransport.ListPipelines")

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
            request: eventarc.ListPipelinesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> eventarc.ListPipelinesResponse:
            r"""Call the list pipelines method over HTTP.

            Args:
                request (~.eventarc.ListPipelinesRequest):
                    The request object. The request message for the
                ListPipelines method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.eventarc.ListPipelinesResponse:
                    The response message for the
                ListPipelines method.

            """

            http_options = (
                _BaseEventarcRestTransport._BaseListPipelines._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_pipelines(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEventarcRestTransport._BaseListPipelines,
                    "_BaseListPipelines__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.eventarc_v1.EventarcClient.ListPipelines",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "ListPipelines",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EventarcRestTransport._ListPipelines._get_response(
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
            resp = eventarc.ListPipelinesResponse()
            pb_resp = eventarc.ListPipelinesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_pipelines(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_pipelines_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = eventarc.ListPipelinesResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.eventarc_v1.EventarcClient.list_pipelines",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "ListPipelines",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListProviders(
        _BaseEventarcRestTransport._BaseListProviders, EventarcRestStub
    ):
        def __hash__(self):
            return hash("EventarcRestTransport.ListProviders")

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
            request: eventarc.ListProvidersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> eventarc.ListProvidersResponse:
            r"""Call the list providers method over HTTP.

            Args:
                request (~.eventarc.ListProvidersRequest):
                    The request object. The request message for the
                ListProviders method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.eventarc.ListProvidersResponse:
                    The response message for the ``ListProviders`` method.
            """

            http_options = (
                _BaseEventarcRestTransport._BaseListProviders._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_providers(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEventarcRestTransport._BaseListProviders,
                    "_BaseListProviders__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.eventarc_v1.EventarcClient.ListProviders",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "ListProviders",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EventarcRestTransport._ListProviders._get_response(
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
            resp = eventarc.ListProvidersResponse()
            pb_resp = eventarc.ListProvidersResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_providers(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_providers_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = eventarc.ListProvidersResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.eventarc_v1.EventarcClient.list_providers",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "ListProviders",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListTriggers(_BaseEventarcRestTransport._BaseListTriggers, EventarcRestStub):
        def __hash__(self):
            return hash("EventarcRestTransport.ListTriggers")

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
            request: eventarc.ListTriggersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> eventarc.ListTriggersResponse:
            r"""Call the list triggers method over HTTP.

            Args:
                request (~.eventarc.ListTriggersRequest):
                    The request object. The request message for the
                ListTriggers method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.eventarc.ListTriggersResponse:
                    The response message for the ``ListTriggers`` method.
            """

            http_options = (
                _BaseEventarcRestTransport._BaseListTriggers._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_triggers(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEventarcRestTransport._BaseListTriggers,
                    "_BaseListTriggers__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.eventarc_v1.EventarcClient.ListTriggers",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "ListTriggers",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EventarcRestTransport._ListTriggers._get_response(
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
            resp = eventarc.ListTriggersResponse()
            pb_resp = eventarc.ListTriggersResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_triggers(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_triggers_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = eventarc.ListTriggersResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.eventarc_v1.EventarcClient.list_triggers",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "ListTriggers",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateChannel(
        _BaseEventarcRestTransport._BaseUpdateChannel, EventarcRestStub
    ):
        def __hash__(self):
            return hash("EventarcRestTransport.UpdateChannel")

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
            request: eventarc.UpdateChannelRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update channel method over HTTP.

            Args:
                request (~.eventarc.UpdateChannelRequest):
                    The request object. The request message for the
                UpdateChannel method.
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
                _BaseEventarcRestTransport._BaseUpdateChannel._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_channel(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEventarcRestTransport._BaseUpdateChannel,
                    "_BaseUpdateChannel__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.eventarc_v1.EventarcClient.UpdateChannel",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "UpdateChannel",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EventarcRestTransport._UpdateChannel._get_response(
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

            resp = self._interceptor.post_update_channel(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_channel_with_metadata(
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
                    "Received response for google.cloud.eventarc_v1.EventarcClient.update_channel",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "UpdateChannel",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateEnrollment(
        _BaseEventarcRestTransport._BaseUpdateEnrollment, EventarcRestStub
    ):
        def __hash__(self):
            return hash("EventarcRestTransport.UpdateEnrollment")

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
            request: eventarc.UpdateEnrollmentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update enrollment method over HTTP.

            Args:
                request (~.eventarc.UpdateEnrollmentRequest):
                    The request object. The request message for the
                UpdateEnrollment method.
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
                _BaseEventarcRestTransport._BaseUpdateEnrollment._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_enrollment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEventarcRestTransport._BaseUpdateEnrollment,
                    "_BaseUpdateEnrollment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.eventarc_v1.EventarcClient.UpdateEnrollment",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "UpdateEnrollment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EventarcRestTransport._UpdateEnrollment._get_response(
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

            resp = self._interceptor.post_update_enrollment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_enrollment_with_metadata(
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
                    "Received response for google.cloud.eventarc_v1.EventarcClient.update_enrollment",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "UpdateEnrollment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateGoogleApiSource(
        _BaseEventarcRestTransport._BaseUpdateGoogleApiSource, EventarcRestStub
    ):
        def __hash__(self):
            return hash("EventarcRestTransport.UpdateGoogleApiSource")

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
            request: eventarc.UpdateGoogleApiSourceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update google api source method over HTTP.

            Args:
                request (~.eventarc.UpdateGoogleApiSourceRequest):
                    The request object. The request message for the
                UpdateGoogleApiSource method.
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

            http_options = _BaseEventarcRestTransport._BaseUpdateGoogleApiSource._get_http_options()
            request, metadata = self._interceptor.pre_update_google_api_source(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEventarcRestTransport._BaseUpdateGoogleApiSource,
                    "_BaseUpdateGoogleApiSource__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.eventarc_v1.EventarcClient.UpdateGoogleApiSource",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "UpdateGoogleApiSource",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EventarcRestTransport._UpdateGoogleApiSource._get_response(
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

            resp = self._interceptor.post_update_google_api_source(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_google_api_source_with_metadata(
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
                    "Received response for google.cloud.eventarc_v1.EventarcClient.update_google_api_source",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "UpdateGoogleApiSource",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateGoogleChannelConfig(
        _BaseEventarcRestTransport._BaseUpdateGoogleChannelConfig, EventarcRestStub
    ):
        def __hash__(self):
            return hash("EventarcRestTransport.UpdateGoogleChannelConfig")

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
            request: eventarc.UpdateGoogleChannelConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gce_google_channel_config.GoogleChannelConfig:
            r"""Call the update google channel
            config method over HTTP.

                Args:
                    request (~.eventarc.UpdateGoogleChannelConfigRequest):
                        The request object. The request message for the
                    UpdateGoogleChannelConfig method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.gce_google_channel_config.GoogleChannelConfig:
                        A GoogleChannelConfig is a resource
                    that stores the custom settings
                    respected by Eventarc first-party
                    triggers in the matching region. Once
                    configured, first-party event data will
                    be protected using the specified custom
                    managed encryption key instead of
                    Google-managed encryption keys.

            """

            http_options = _BaseEventarcRestTransport._BaseUpdateGoogleChannelConfig._get_http_options()
            request, metadata = self._interceptor.pre_update_google_channel_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEventarcRestTransport._BaseUpdateGoogleChannelConfig,
                    "_BaseUpdateGoogleChannelConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.eventarc_v1.EventarcClient.UpdateGoogleChannelConfig",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "UpdateGoogleChannelConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EventarcRestTransport._UpdateGoogleChannelConfig._get_response(
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
            resp = gce_google_channel_config.GoogleChannelConfig()
            pb_resp = gce_google_channel_config.GoogleChannelConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_google_channel_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_google_channel_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        gce_google_channel_config.GoogleChannelConfig.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.eventarc_v1.EventarcClient.update_google_channel_config",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "UpdateGoogleChannelConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateMessageBus(
        _BaseEventarcRestTransport._BaseUpdateMessageBus, EventarcRestStub
    ):
        def __hash__(self):
            return hash("EventarcRestTransport.UpdateMessageBus")

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
            request: eventarc.UpdateMessageBusRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update message bus method over HTTP.

            Args:
                request (~.eventarc.UpdateMessageBusRequest):
                    The request object. The request message for the
                UpdateMessageBus method.
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
                _BaseEventarcRestTransport._BaseUpdateMessageBus._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_message_bus(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEventarcRestTransport._BaseUpdateMessageBus,
                    "_BaseUpdateMessageBus__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.eventarc_v1.EventarcClient.UpdateMessageBus",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "UpdateMessageBus",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EventarcRestTransport._UpdateMessageBus._get_response(
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

            resp = self._interceptor.post_update_message_bus(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_message_bus_with_metadata(
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
                    "Received response for google.cloud.eventarc_v1.EventarcClient.update_message_bus",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "UpdateMessageBus",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdatePipeline(
        _BaseEventarcRestTransport._BaseUpdatePipeline, EventarcRestStub
    ):
        def __hash__(self):
            return hash("EventarcRestTransport.UpdatePipeline")

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
            request: eventarc.UpdatePipelineRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update pipeline method over HTTP.

            Args:
                request (~.eventarc.UpdatePipelineRequest):
                    The request object. The request message for the
                UpdatePipeline method.
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
                _BaseEventarcRestTransport._BaseUpdatePipeline._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_pipeline(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEventarcRestTransport._BaseUpdatePipeline,
                    "_BaseUpdatePipeline__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.eventarc_v1.EventarcClient.UpdatePipeline",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "UpdatePipeline",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EventarcRestTransport._UpdatePipeline._get_response(
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

            resp = self._interceptor.post_update_pipeline(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_pipeline_with_metadata(
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
                    "Received response for google.cloud.eventarc_v1.EventarcClient.update_pipeline",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "UpdatePipeline",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateTrigger(
        _BaseEventarcRestTransport._BaseUpdateTrigger, EventarcRestStub
    ):
        def __hash__(self):
            return hash("EventarcRestTransport.UpdateTrigger")

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
            request: eventarc.UpdateTriggerRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update trigger method over HTTP.

            Args:
                request (~.eventarc.UpdateTriggerRequest):
                    The request object. The request message for the
                UpdateTrigger method.
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
                _BaseEventarcRestTransport._BaseUpdateTrigger._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_trigger(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEventarcRestTransport._BaseUpdateTrigger,
                    "_BaseUpdateTrigger__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.eventarc_v1.EventarcClient.UpdateTrigger",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "UpdateTrigger",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EventarcRestTransport._UpdateTrigger._get_response(
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

            resp = self._interceptor.post_update_trigger(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_trigger_with_metadata(
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
                    "Received response for google.cloud.eventarc_v1.EventarcClient.update_trigger",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "UpdateTrigger",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_channel_(
        self,
    ) -> Callable[[eventarc.CreateChannelRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateChannel(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_channel_connection(
        self,
    ) -> Callable[[eventarc.CreateChannelConnectionRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateChannelConnection(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_enrollment(
        self,
    ) -> Callable[[eventarc.CreateEnrollmentRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateEnrollment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_google_api_source(
        self,
    ) -> Callable[[eventarc.CreateGoogleApiSourceRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateGoogleApiSource(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_message_bus(
        self,
    ) -> Callable[[eventarc.CreateMessageBusRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateMessageBus(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_pipeline(
        self,
    ) -> Callable[[eventarc.CreatePipelineRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreatePipeline(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_trigger(
        self,
    ) -> Callable[[eventarc.CreateTriggerRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateTrigger(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_channel(
        self,
    ) -> Callable[[eventarc.DeleteChannelRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteChannel(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_channel_connection(
        self,
    ) -> Callable[[eventarc.DeleteChannelConnectionRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteChannelConnection(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_enrollment(
        self,
    ) -> Callable[[eventarc.DeleteEnrollmentRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteEnrollment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_google_api_source(
        self,
    ) -> Callable[[eventarc.DeleteGoogleApiSourceRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteGoogleApiSource(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_message_bus(
        self,
    ) -> Callable[[eventarc.DeleteMessageBusRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteMessageBus(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_pipeline(
        self,
    ) -> Callable[[eventarc.DeletePipelineRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeletePipeline(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_trigger(
        self,
    ) -> Callable[[eventarc.DeleteTriggerRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteTrigger(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_channel(self) -> Callable[[eventarc.GetChannelRequest], channel.Channel]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetChannel(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_channel_connection(
        self,
    ) -> Callable[
        [eventarc.GetChannelConnectionRequest], channel_connection.ChannelConnection
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetChannelConnection(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_enrollment(
        self,
    ) -> Callable[[eventarc.GetEnrollmentRequest], enrollment.Enrollment]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetEnrollment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_google_api_source(
        self,
    ) -> Callable[
        [eventarc.GetGoogleApiSourceRequest], google_api_source.GoogleApiSource
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetGoogleApiSource(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_google_channel_config(
        self,
    ) -> Callable[
        [eventarc.GetGoogleChannelConfigRequest],
        google_channel_config.GoogleChannelConfig,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetGoogleChannelConfig(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_message_bus(
        self,
    ) -> Callable[[eventarc.GetMessageBusRequest], message_bus.MessageBus]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetMessageBus(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_pipeline(
        self,
    ) -> Callable[[eventarc.GetPipelineRequest], pipeline.Pipeline]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetPipeline(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_provider(
        self,
    ) -> Callable[[eventarc.GetProviderRequest], discovery.Provider]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetProvider(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_trigger(self) -> Callable[[eventarc.GetTriggerRequest], trigger.Trigger]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetTrigger(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_channel_connections(
        self,
    ) -> Callable[
        [eventarc.ListChannelConnectionsRequest],
        eventarc.ListChannelConnectionsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListChannelConnections(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_channels(
        self,
    ) -> Callable[[eventarc.ListChannelsRequest], eventarc.ListChannelsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListChannels(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_enrollments(
        self,
    ) -> Callable[[eventarc.ListEnrollmentsRequest], eventarc.ListEnrollmentsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListEnrollments(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_google_api_sources(
        self,
    ) -> Callable[
        [eventarc.ListGoogleApiSourcesRequest], eventarc.ListGoogleApiSourcesResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListGoogleApiSources(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_message_bus_enrollments(
        self,
    ) -> Callable[
        [eventarc.ListMessageBusEnrollmentsRequest],
        eventarc.ListMessageBusEnrollmentsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListMessageBusEnrollments(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_message_buses(
        self,
    ) -> Callable[
        [eventarc.ListMessageBusesRequest], eventarc.ListMessageBusesResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListMessageBuses(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_pipelines(
        self,
    ) -> Callable[[eventarc.ListPipelinesRequest], eventarc.ListPipelinesResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListPipelines(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_providers(
        self,
    ) -> Callable[[eventarc.ListProvidersRequest], eventarc.ListProvidersResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListProviders(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_triggers(
        self,
    ) -> Callable[[eventarc.ListTriggersRequest], eventarc.ListTriggersResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListTriggers(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_channel(
        self,
    ) -> Callable[[eventarc.UpdateChannelRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateChannel(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_enrollment(
        self,
    ) -> Callable[[eventarc.UpdateEnrollmentRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateEnrollment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_google_api_source(
        self,
    ) -> Callable[[eventarc.UpdateGoogleApiSourceRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateGoogleApiSource(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_google_channel_config(
        self,
    ) -> Callable[
        [eventarc.UpdateGoogleChannelConfigRequest],
        gce_google_channel_config.GoogleChannelConfig,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateGoogleChannelConfig(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_message_bus(
        self,
    ) -> Callable[[eventarc.UpdateMessageBusRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateMessageBus(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_pipeline(
        self,
    ) -> Callable[[eventarc.UpdatePipelineRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdatePipeline(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_trigger(
        self,
    ) -> Callable[[eventarc.UpdateTriggerRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateTrigger(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(_BaseEventarcRestTransport._BaseGetLocation, EventarcRestStub):
        def __hash__(self):
            return hash("EventarcRestTransport.GetLocation")

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
                _BaseEventarcRestTransport._BaseGetLocation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEventarcRestTransport._BaseGetLocation,
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
                    f"Sending request for google.cloud.eventarc_v1.EventarcClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EventarcRestTransport._GetLocation._get_response(
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
                    "Received response for google.cloud.eventarc_v1.EventarcAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
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
        _BaseEventarcRestTransport._BaseListLocations, EventarcRestStub
    ):
        def __hash__(self):
            return hash("EventarcRestTransport.ListLocations")

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
                _BaseEventarcRestTransport._BaseListLocations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEventarcRestTransport._BaseListLocations,
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
                    f"Sending request for google.cloud.eventarc_v1.EventarcClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EventarcRestTransport._ListLocations._get_response(
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
                    "Received response for google.cloud.eventarc_v1.EventarcAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "ListLocations",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def get_iam_policy(self):
        return self._GetIamPolicy(self._session, self._host, self._interceptor)  # type: ignore

    class _GetIamPolicy(_BaseEventarcRestTransport._BaseGetIamPolicy, EventarcRestStub):
        def __hash__(self):
            return hash("EventarcRestTransport.GetIamPolicy")

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
                _BaseEventarcRestTransport._BaseGetIamPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEventarcRestTransport._BaseGetIamPolicy,
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
                    f"Sending request for google.cloud.eventarc_v1.EventarcClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "GetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EventarcRestTransport._GetIamPolicy._get_response(
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
                    "Received response for google.cloud.eventarc_v1.EventarcAsyncClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "GetIamPolicy",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def set_iam_policy(self):
        return self._SetIamPolicy(self._session, self._host, self._interceptor)  # type: ignore

    class _SetIamPolicy(_BaseEventarcRestTransport._BaseSetIamPolicy, EventarcRestStub):
        def __hash__(self):
            return hash("EventarcRestTransport.SetIamPolicy")

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
                _BaseEventarcRestTransport._BaseSetIamPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_set_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEventarcRestTransport._BaseSetIamPolicy,
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
                    f"Sending request for google.cloud.eventarc_v1.EventarcClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "SetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EventarcRestTransport._SetIamPolicy._get_response(
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
                    "Received response for google.cloud.eventarc_v1.EventarcAsyncClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
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
        _BaseEventarcRestTransport._BaseTestIamPermissions, EventarcRestStub
    ):
        def __hash__(self):
            return hash("EventarcRestTransport.TestIamPermissions")

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
                _BaseEventarcRestTransport._BaseTestIamPermissions._get_http_options()
            )
            request, metadata = self._interceptor.pre_test_iam_permissions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEventarcRestTransport._BaseTestIamPermissions,
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
                    f"Sending request for google.cloud.eventarc_v1.EventarcClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "TestIamPermissions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EventarcRestTransport._TestIamPermissions._get_response(
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
                    "Received response for google.cloud.eventarc_v1.EventarcAsyncClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "TestIamPermissions",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseEventarcRestTransport._BaseCancelOperation, EventarcRestStub
    ):
        def __hash__(self):
            return hash("EventarcRestTransport.CancelOperation")

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
                _BaseEventarcRestTransport._BaseCancelOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEventarcRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.eventarc_v1.EventarcClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EventarcRestTransport._CancelOperation._get_response(
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
        _BaseEventarcRestTransport._BaseDeleteOperation, EventarcRestStub
    ):
        def __hash__(self):
            return hash("EventarcRestTransport.DeleteOperation")

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
                _BaseEventarcRestTransport._BaseDeleteOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEventarcRestTransport._BaseDeleteOperation,
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
                    f"Sending request for google.cloud.eventarc_v1.EventarcClient.DeleteOperation",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EventarcRestTransport._DeleteOperation._get_response(
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

    class _GetOperation(_BaseEventarcRestTransport._BaseGetOperation, EventarcRestStub):
        def __hash__(self):
            return hash("EventarcRestTransport.GetOperation")

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
                _BaseEventarcRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEventarcRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.eventarc_v1.EventarcClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EventarcRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.eventarc_v1.EventarcAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
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
        _BaseEventarcRestTransport._BaseListOperations, EventarcRestStub
    ):
        def __hash__(self):
            return hash("EventarcRestTransport.ListOperations")

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
                _BaseEventarcRestTransport._BaseListOperations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEventarcRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.eventarc_v1.EventarcClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EventarcRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.eventarc_v1.EventarcAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.eventarc.v1.Eventarc",
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


__all__ = ("EventarcRestTransport",)
