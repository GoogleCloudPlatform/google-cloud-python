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

from google.cloud.datacatalog_lineage_v1._compat import transcode_request
from google.cloud.datacatalog_lineage_v1.types import lineage

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseLineageRestTransport

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


class LineageRestInterceptor:
    """Interceptor for Lineage.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the LineageRestTransport.

    .. code-block:: python
        class MyCustomLineageInterceptor(LineageRestInterceptor):
            def pre_batch_search_link_processes(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_search_link_processes(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_lineage_event(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_lineage_event(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_process(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_process(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_run(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_run(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_lineage_event(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_process(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_process(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_run(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_run(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_lineage_event(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_lineage_event(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_process(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_process(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_run(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_run(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_lineage_events(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_lineage_events(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_processes(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_processes(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_runs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_runs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_process_open_lineage_run_event(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_process_open_lineage_run_event(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_search_lineage_streaming(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_search_lineage_streaming(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_search_links(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_search_links(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_process(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_process(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_run(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_run(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = LineageRestTransport(interceptor=MyCustomLineageInterceptor())
        client = LineageClient(transport=transport)


    """

    def pre_batch_search_link_processes(
        self,
        request: lineage.BatchSearchLinkProcessesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        lineage.BatchSearchLinkProcessesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for batch_search_link_processes

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Lineage server.
        """
        return request, metadata

    def post_batch_search_link_processes(
        self, response: lineage.BatchSearchLinkProcessesResponse
    ) -> lineage.BatchSearchLinkProcessesResponse:
        """Post-rpc interceptor for batch_search_link_processes

        DEPRECATED. Please use the `post_batch_search_link_processes_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Lineage server but before
        it is returned to user code. This `post_batch_search_link_processes` interceptor runs
        before the `post_batch_search_link_processes_with_metadata` interceptor.
        """
        return response

    def post_batch_search_link_processes_with_metadata(
        self,
        response: lineage.BatchSearchLinkProcessesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        lineage.BatchSearchLinkProcessesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_search_link_processes

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Lineage server but before it is returned to user code.

        We recommend only using this `post_batch_search_link_processes_with_metadata`
        interceptor in new development instead of the `post_batch_search_link_processes` interceptor.
        When both interceptors are used, this `post_batch_search_link_processes_with_metadata` interceptor runs after the
        `post_batch_search_link_processes` interceptor. The (possibly modified) response returned by
        `post_batch_search_link_processes` will be passed to
        `post_batch_search_link_processes_with_metadata`.
        """
        return response, metadata

    def pre_create_lineage_event(
        self,
        request: lineage.CreateLineageEventRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        lineage.CreateLineageEventRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_lineage_event

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Lineage server.
        """
        return request, metadata

    def post_create_lineage_event(
        self, response: lineage.LineageEvent
    ) -> lineage.LineageEvent:
        """Post-rpc interceptor for create_lineage_event

        DEPRECATED. Please use the `post_create_lineage_event_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Lineage server but before
        it is returned to user code. This `post_create_lineage_event` interceptor runs
        before the `post_create_lineage_event_with_metadata` interceptor.
        """
        return response

    def post_create_lineage_event_with_metadata(
        self,
        response: lineage.LineageEvent,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[lineage.LineageEvent, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_lineage_event

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Lineage server but before it is returned to user code.

        We recommend only using this `post_create_lineage_event_with_metadata`
        interceptor in new development instead of the `post_create_lineage_event` interceptor.
        When both interceptors are used, this `post_create_lineage_event_with_metadata` interceptor runs after the
        `post_create_lineage_event` interceptor. The (possibly modified) response returned by
        `post_create_lineage_event` will be passed to
        `post_create_lineage_event_with_metadata`.
        """
        return response, metadata

    def pre_create_process(
        self,
        request: lineage.CreateProcessRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[lineage.CreateProcessRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_process

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Lineage server.
        """
        return request, metadata

    def post_create_process(self, response: lineage.Process) -> lineage.Process:
        """Post-rpc interceptor for create_process

        DEPRECATED. Please use the `post_create_process_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Lineage server but before
        it is returned to user code. This `post_create_process` interceptor runs
        before the `post_create_process_with_metadata` interceptor.
        """
        return response

    def post_create_process_with_metadata(
        self,
        response: lineage.Process,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[lineage.Process, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_process

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Lineage server but before it is returned to user code.

        We recommend only using this `post_create_process_with_metadata`
        interceptor in new development instead of the `post_create_process` interceptor.
        When both interceptors are used, this `post_create_process_with_metadata` interceptor runs after the
        `post_create_process` interceptor. The (possibly modified) response returned by
        `post_create_process` will be passed to
        `post_create_process_with_metadata`.
        """
        return response, metadata

    def pre_create_run(
        self,
        request: lineage.CreateRunRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[lineage.CreateRunRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_run

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Lineage server.
        """
        return request, metadata

    def post_create_run(self, response: lineage.Run) -> lineage.Run:
        """Post-rpc interceptor for create_run

        DEPRECATED. Please use the `post_create_run_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Lineage server but before
        it is returned to user code. This `post_create_run` interceptor runs
        before the `post_create_run_with_metadata` interceptor.
        """
        return response

    def post_create_run_with_metadata(
        self, response: lineage.Run, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[lineage.Run, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_run

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Lineage server but before it is returned to user code.

        We recommend only using this `post_create_run_with_metadata`
        interceptor in new development instead of the `post_create_run` interceptor.
        When both interceptors are used, this `post_create_run_with_metadata` interceptor runs after the
        `post_create_run` interceptor. The (possibly modified) response returned by
        `post_create_run` will be passed to
        `post_create_run_with_metadata`.
        """
        return response, metadata

    def pre_delete_lineage_event(
        self,
        request: lineage.DeleteLineageEventRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        lineage.DeleteLineageEventRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_lineage_event

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Lineage server.
        """
        return request, metadata

    def pre_delete_process(
        self,
        request: lineage.DeleteProcessRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[lineage.DeleteProcessRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_process

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Lineage server.
        """
        return request, metadata

    def post_delete_process(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_process

        DEPRECATED. Please use the `post_delete_process_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Lineage server but before
        it is returned to user code. This `post_delete_process` interceptor runs
        before the `post_delete_process_with_metadata` interceptor.
        """
        return response

    def post_delete_process_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_process

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Lineage server but before it is returned to user code.

        We recommend only using this `post_delete_process_with_metadata`
        interceptor in new development instead of the `post_delete_process` interceptor.
        When both interceptors are used, this `post_delete_process_with_metadata` interceptor runs after the
        `post_delete_process` interceptor. The (possibly modified) response returned by
        `post_delete_process` will be passed to
        `post_delete_process_with_metadata`.
        """
        return response, metadata

    def pre_delete_run(
        self,
        request: lineage.DeleteRunRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[lineage.DeleteRunRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_run

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Lineage server.
        """
        return request, metadata

    def post_delete_run(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_run

        DEPRECATED. Please use the `post_delete_run_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Lineage server but before
        it is returned to user code. This `post_delete_run` interceptor runs
        before the `post_delete_run_with_metadata` interceptor.
        """
        return response

    def post_delete_run_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_run

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Lineage server but before it is returned to user code.

        We recommend only using this `post_delete_run_with_metadata`
        interceptor in new development instead of the `post_delete_run` interceptor.
        When both interceptors are used, this `post_delete_run_with_metadata` interceptor runs after the
        `post_delete_run` interceptor. The (possibly modified) response returned by
        `post_delete_run` will be passed to
        `post_delete_run_with_metadata`.
        """
        return response, metadata

    def pre_get_lineage_event(
        self,
        request: lineage.GetLineageEventRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[lineage.GetLineageEventRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_lineage_event

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Lineage server.
        """
        return request, metadata

    def post_get_lineage_event(
        self, response: lineage.LineageEvent
    ) -> lineage.LineageEvent:
        """Post-rpc interceptor for get_lineage_event

        DEPRECATED. Please use the `post_get_lineage_event_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Lineage server but before
        it is returned to user code. This `post_get_lineage_event` interceptor runs
        before the `post_get_lineage_event_with_metadata` interceptor.
        """
        return response

    def post_get_lineage_event_with_metadata(
        self,
        response: lineage.LineageEvent,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[lineage.LineageEvent, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_lineage_event

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Lineage server but before it is returned to user code.

        We recommend only using this `post_get_lineage_event_with_metadata`
        interceptor in new development instead of the `post_get_lineage_event` interceptor.
        When both interceptors are used, this `post_get_lineage_event_with_metadata` interceptor runs after the
        `post_get_lineage_event` interceptor. The (possibly modified) response returned by
        `post_get_lineage_event` will be passed to
        `post_get_lineage_event_with_metadata`.
        """
        return response, metadata

    def pre_get_process(
        self,
        request: lineage.GetProcessRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[lineage.GetProcessRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_process

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Lineage server.
        """
        return request, metadata

    def post_get_process(self, response: lineage.Process) -> lineage.Process:
        """Post-rpc interceptor for get_process

        DEPRECATED. Please use the `post_get_process_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Lineage server but before
        it is returned to user code. This `post_get_process` interceptor runs
        before the `post_get_process_with_metadata` interceptor.
        """
        return response

    def post_get_process_with_metadata(
        self,
        response: lineage.Process,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[lineage.Process, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_process

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Lineage server but before it is returned to user code.

        We recommend only using this `post_get_process_with_metadata`
        interceptor in new development instead of the `post_get_process` interceptor.
        When both interceptors are used, this `post_get_process_with_metadata` interceptor runs after the
        `post_get_process` interceptor. The (possibly modified) response returned by
        `post_get_process` will be passed to
        `post_get_process_with_metadata`.
        """
        return response, metadata

    def pre_get_run(
        self,
        request: lineage.GetRunRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[lineage.GetRunRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_run

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Lineage server.
        """
        return request, metadata

    def post_get_run(self, response: lineage.Run) -> lineage.Run:
        """Post-rpc interceptor for get_run

        DEPRECATED. Please use the `post_get_run_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Lineage server but before
        it is returned to user code. This `post_get_run` interceptor runs
        before the `post_get_run_with_metadata` interceptor.
        """
        return response

    def post_get_run_with_metadata(
        self, response: lineage.Run, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[lineage.Run, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_run

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Lineage server but before it is returned to user code.

        We recommend only using this `post_get_run_with_metadata`
        interceptor in new development instead of the `post_get_run` interceptor.
        When both interceptors are used, this `post_get_run_with_metadata` interceptor runs after the
        `post_get_run` interceptor. The (possibly modified) response returned by
        `post_get_run` will be passed to
        `post_get_run_with_metadata`.
        """
        return response, metadata

    def pre_list_lineage_events(
        self,
        request: lineage.ListLineageEventsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        lineage.ListLineageEventsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_lineage_events

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Lineage server.
        """
        return request, metadata

    def post_list_lineage_events(
        self, response: lineage.ListLineageEventsResponse
    ) -> lineage.ListLineageEventsResponse:
        """Post-rpc interceptor for list_lineage_events

        DEPRECATED. Please use the `post_list_lineage_events_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Lineage server but before
        it is returned to user code. This `post_list_lineage_events` interceptor runs
        before the `post_list_lineage_events_with_metadata` interceptor.
        """
        return response

    def post_list_lineage_events_with_metadata(
        self,
        response: lineage.ListLineageEventsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        lineage.ListLineageEventsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_lineage_events

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Lineage server but before it is returned to user code.

        We recommend only using this `post_list_lineage_events_with_metadata`
        interceptor in new development instead of the `post_list_lineage_events` interceptor.
        When both interceptors are used, this `post_list_lineage_events_with_metadata` interceptor runs after the
        `post_list_lineage_events` interceptor. The (possibly modified) response returned by
        `post_list_lineage_events` will be passed to
        `post_list_lineage_events_with_metadata`.
        """
        return response, metadata

    def pre_list_processes(
        self,
        request: lineage.ListProcessesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[lineage.ListProcessesRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_processes

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Lineage server.
        """
        return request, metadata

    def post_list_processes(
        self, response: lineage.ListProcessesResponse
    ) -> lineage.ListProcessesResponse:
        """Post-rpc interceptor for list_processes

        DEPRECATED. Please use the `post_list_processes_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Lineage server but before
        it is returned to user code. This `post_list_processes` interceptor runs
        before the `post_list_processes_with_metadata` interceptor.
        """
        return response

    def post_list_processes_with_metadata(
        self,
        response: lineage.ListProcessesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[lineage.ListProcessesResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_processes

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Lineage server but before it is returned to user code.

        We recommend only using this `post_list_processes_with_metadata`
        interceptor in new development instead of the `post_list_processes` interceptor.
        When both interceptors are used, this `post_list_processes_with_metadata` interceptor runs after the
        `post_list_processes` interceptor. The (possibly modified) response returned by
        `post_list_processes` will be passed to
        `post_list_processes_with_metadata`.
        """
        return response, metadata

    def pre_list_runs(
        self,
        request: lineage.ListRunsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[lineage.ListRunsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_runs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Lineage server.
        """
        return request, metadata

    def post_list_runs(
        self, response: lineage.ListRunsResponse
    ) -> lineage.ListRunsResponse:
        """Post-rpc interceptor for list_runs

        DEPRECATED. Please use the `post_list_runs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Lineage server but before
        it is returned to user code. This `post_list_runs` interceptor runs
        before the `post_list_runs_with_metadata` interceptor.
        """
        return response

    def post_list_runs_with_metadata(
        self,
        response: lineage.ListRunsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[lineage.ListRunsResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_runs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Lineage server but before it is returned to user code.

        We recommend only using this `post_list_runs_with_metadata`
        interceptor in new development instead of the `post_list_runs` interceptor.
        When both interceptors are used, this `post_list_runs_with_metadata` interceptor runs after the
        `post_list_runs` interceptor. The (possibly modified) response returned by
        `post_list_runs` will be passed to
        `post_list_runs_with_metadata`.
        """
        return response, metadata

    def pre_process_open_lineage_run_event(
        self,
        request: lineage.ProcessOpenLineageRunEventRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        lineage.ProcessOpenLineageRunEventRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for process_open_lineage_run_event

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Lineage server.
        """
        return request, metadata

    def post_process_open_lineage_run_event(
        self, response: lineage.ProcessOpenLineageRunEventResponse
    ) -> lineage.ProcessOpenLineageRunEventResponse:
        """Post-rpc interceptor for process_open_lineage_run_event

        DEPRECATED. Please use the `post_process_open_lineage_run_event_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Lineage server but before
        it is returned to user code. This `post_process_open_lineage_run_event` interceptor runs
        before the `post_process_open_lineage_run_event_with_metadata` interceptor.
        """
        return response

    def post_process_open_lineage_run_event_with_metadata(
        self,
        response: lineage.ProcessOpenLineageRunEventResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        lineage.ProcessOpenLineageRunEventResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for process_open_lineage_run_event

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Lineage server but before it is returned to user code.

        We recommend only using this `post_process_open_lineage_run_event_with_metadata`
        interceptor in new development instead of the `post_process_open_lineage_run_event` interceptor.
        When both interceptors are used, this `post_process_open_lineage_run_event_with_metadata` interceptor runs after the
        `post_process_open_lineage_run_event` interceptor. The (possibly modified) response returned by
        `post_process_open_lineage_run_event` will be passed to
        `post_process_open_lineage_run_event_with_metadata`.
        """
        return response, metadata

    def pre_search_lineage_streaming(
        self,
        request: lineage.SearchLineageStreamingRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        lineage.SearchLineageStreamingRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for search_lineage_streaming

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Lineage server.
        """
        return request, metadata

    def post_search_lineage_streaming(
        self, response: rest_streaming.ResponseIterator
    ) -> rest_streaming.ResponseIterator:
        """Post-rpc interceptor for search_lineage_streaming

        DEPRECATED. Please use the `post_search_lineage_streaming_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Lineage server but before
        it is returned to user code. This `post_search_lineage_streaming` interceptor runs
        before the `post_search_lineage_streaming_with_metadata` interceptor.
        """
        return response

    def post_search_lineage_streaming_with_metadata(
        self,
        response: rest_streaming.ResponseIterator,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        rest_streaming.ResponseIterator, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for search_lineage_streaming

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Lineage server but before it is returned to user code.

        We recommend only using this `post_search_lineage_streaming_with_metadata`
        interceptor in new development instead of the `post_search_lineage_streaming` interceptor.
        When both interceptors are used, this `post_search_lineage_streaming_with_metadata` interceptor runs after the
        `post_search_lineage_streaming` interceptor. The (possibly modified) response returned by
        `post_search_lineage_streaming` will be passed to
        `post_search_lineage_streaming_with_metadata`.
        """
        return response, metadata

    def pre_search_links(
        self,
        request: lineage.SearchLinksRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[lineage.SearchLinksRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for search_links

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Lineage server.
        """
        return request, metadata

    def post_search_links(
        self, response: lineage.SearchLinksResponse
    ) -> lineage.SearchLinksResponse:
        """Post-rpc interceptor for search_links

        DEPRECATED. Please use the `post_search_links_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Lineage server but before
        it is returned to user code. This `post_search_links` interceptor runs
        before the `post_search_links_with_metadata` interceptor.
        """
        return response

    def post_search_links_with_metadata(
        self,
        response: lineage.SearchLinksResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[lineage.SearchLinksResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for search_links

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Lineage server but before it is returned to user code.

        We recommend only using this `post_search_links_with_metadata`
        interceptor in new development instead of the `post_search_links` interceptor.
        When both interceptors are used, this `post_search_links_with_metadata` interceptor runs after the
        `post_search_links` interceptor. The (possibly modified) response returned by
        `post_search_links` will be passed to
        `post_search_links_with_metadata`.
        """
        return response, metadata

    def pre_update_process(
        self,
        request: lineage.UpdateProcessRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[lineage.UpdateProcessRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_process

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Lineage server.
        """
        return request, metadata

    def post_update_process(self, response: lineage.Process) -> lineage.Process:
        """Post-rpc interceptor for update_process

        DEPRECATED. Please use the `post_update_process_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Lineage server but before
        it is returned to user code. This `post_update_process` interceptor runs
        before the `post_update_process_with_metadata` interceptor.
        """
        return response

    def post_update_process_with_metadata(
        self,
        response: lineage.Process,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[lineage.Process, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_process

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Lineage server but before it is returned to user code.

        We recommend only using this `post_update_process_with_metadata`
        interceptor in new development instead of the `post_update_process` interceptor.
        When both interceptors are used, this `post_update_process_with_metadata` interceptor runs after the
        `post_update_process` interceptor. The (possibly modified) response returned by
        `post_update_process` will be passed to
        `post_update_process_with_metadata`.
        """
        return response, metadata

    def pre_update_run(
        self,
        request: lineage.UpdateRunRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[lineage.UpdateRunRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_run

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Lineage server.
        """
        return request, metadata

    def post_update_run(self, response: lineage.Run) -> lineage.Run:
        """Post-rpc interceptor for update_run

        DEPRECATED. Please use the `post_update_run_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Lineage server but before
        it is returned to user code. This `post_update_run` interceptor runs
        before the `post_update_run_with_metadata` interceptor.
        """
        return response

    def post_update_run_with_metadata(
        self, response: lineage.Run, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[lineage.Run, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_run

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Lineage server but before it is returned to user code.

        We recommend only using this `post_update_run_with_metadata`
        interceptor in new development instead of the `post_update_run` interceptor.
        When both interceptors are used, this `post_update_run_with_metadata` interceptor runs after the
        `post_update_run` interceptor. The (possibly modified) response returned by
        `post_update_run` will be passed to
        `post_update_run_with_metadata`.
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
        before they are sent to the Lineage server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the Lineage server but before
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
        before they are sent to the Lineage server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the Lineage server but before
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
        before they are sent to the Lineage server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the Lineage server but before
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
        before they are sent to the Lineage server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the Lineage server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class LineageRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: LineageRestInterceptor


class LineageRestTransport(_BaseLineageRestTransport):
    """REST backend synchronous transport for Lineage.

    Lineage is used to track data flows between assets over time. You
    can create
    [LineageEvents][google.cloud.datacatalog.lineage.v1.LineageEvent] to
    record lineage between multiple sources and a single target, for
    example, when table data is based on data from multiple tables.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "datalineage.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[LineageRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'datalineage.googleapis.com').
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
            interceptor (Optional[LineageRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or LineageRestInterceptor()
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

    class _BatchSearchLinkProcesses(
        _BaseLineageRestTransport._BaseBatchSearchLinkProcesses, LineageRestStub
    ):
        def __hash__(self):
            return hash("LineageRestTransport.BatchSearchLinkProcesses")

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
            request: lineage.BatchSearchLinkProcessesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> lineage.BatchSearchLinkProcessesResponse:
            r"""Call the batch search link
            processes method over HTTP.

                Args:
                    request (~.lineage.BatchSearchLinkProcessesRequest):
                        The request object. Request message for
                    [BatchSearchLinkProcesses][google.cloud.datacatalog.lineage.v1.Lineage.BatchSearchLinkProcesses].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.lineage.BatchSearchLinkProcessesResponse:
                        Response message for
                    [BatchSearchLinkProcesses][google.cloud.datacatalog.lineage.v1.Lineage.BatchSearchLinkProcesses].

            """

            http_options = _BaseLineageRestTransport._BaseBatchSearchLinkProcesses._get_http_options()
            request, metadata = self._interceptor.pre_batch_search_link_processes(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLineageRestTransport._BaseBatchSearchLinkProcesses,
                    "_BaseBatchSearchLinkProcesses__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.datacatalog.lineage_v1.LineageClient.BatchSearchLinkProcesses",
                    extra={
                        "serviceName": "google.cloud.datacatalog.lineage.v1.Lineage",
                        "rpcName": "BatchSearchLinkProcesses",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LineageRestTransport._BatchSearchLinkProcesses._get_response(
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
            resp = lineage.BatchSearchLinkProcessesResponse()
            pb_resp = lineage.BatchSearchLinkProcessesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_search_link_processes(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_search_link_processes_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = lineage.BatchSearchLinkProcessesResponse.to_json(
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
                    "Received response for google.cloud.datacatalog.lineage_v1.LineageClient.batch_search_link_processes",
                    extra={
                        "serviceName": "google.cloud.datacatalog.lineage.v1.Lineage",
                        "rpcName": "BatchSearchLinkProcesses",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateLineageEvent(
        _BaseLineageRestTransport._BaseCreateLineageEvent, LineageRestStub
    ):
        def __hash__(self):
            return hash("LineageRestTransport.CreateLineageEvent")

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
            request: lineage.CreateLineageEventRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> lineage.LineageEvent:
            r"""Call the create lineage event method over HTTP.

            Args:
                request (~.lineage.CreateLineageEventRequest):
                    The request object. Request message for
                [CreateLineageEvent][google.cloud.datacatalog.lineage.v1.Lineage.CreateLineageEvent].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.lineage.LineageEvent:
                    A lineage event represents an
                operation on assets. Within the
                operation, the data flows from the
                source to the target defined in the
                links field.

            """

            http_options = (
                _BaseLineageRestTransport._BaseCreateLineageEvent._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_lineage_event(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLineageRestTransport._BaseCreateLineageEvent,
                    "_BaseCreateLineageEvent__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.datacatalog.lineage_v1.LineageClient.CreateLineageEvent",
                    extra={
                        "serviceName": "google.cloud.datacatalog.lineage.v1.Lineage",
                        "rpcName": "CreateLineageEvent",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LineageRestTransport._CreateLineageEvent._get_response(
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
            resp = lineage.LineageEvent()
            pb_resp = lineage.LineageEvent.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_lineage_event(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_lineage_event_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = lineage.LineageEvent.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.datacatalog.lineage_v1.LineageClient.create_lineage_event",
                    extra={
                        "serviceName": "google.cloud.datacatalog.lineage.v1.Lineage",
                        "rpcName": "CreateLineageEvent",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateProcess(_BaseLineageRestTransport._BaseCreateProcess, LineageRestStub):
        def __hash__(self):
            return hash("LineageRestTransport.CreateProcess")

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
            request: lineage.CreateProcessRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> lineage.Process:
            r"""Call the create process method over HTTP.

            Args:
                request (~.lineage.CreateProcessRequest):
                    The request object. Request message for
                [CreateProcess][google.cloud.datacatalog.lineage.v1.Lineage.CreateProcess].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.lineage.Process:
                    A process is the definition of a data
                transformation operation.

            """

            http_options = (
                _BaseLineageRestTransport._BaseCreateProcess._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_process(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLineageRestTransport._BaseCreateProcess,
                    "_BaseCreateProcess__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.datacatalog.lineage_v1.LineageClient.CreateProcess",
                    extra={
                        "serviceName": "google.cloud.datacatalog.lineage.v1.Lineage",
                        "rpcName": "CreateProcess",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LineageRestTransport._CreateProcess._get_response(
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
            resp = lineage.Process()
            pb_resp = lineage.Process.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_process(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_process_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = lineage.Process.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.datacatalog.lineage_v1.LineageClient.create_process",
                    extra={
                        "serviceName": "google.cloud.datacatalog.lineage.v1.Lineage",
                        "rpcName": "CreateProcess",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateRun(_BaseLineageRestTransport._BaseCreateRun, LineageRestStub):
        def __hash__(self):
            return hash("LineageRestTransport.CreateRun")

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
            request: lineage.CreateRunRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> lineage.Run:
            r"""Call the create run method over HTTP.

            Args:
                request (~.lineage.CreateRunRequest):
                    The request object. Request message for
                [CreateRun][google.cloud.datacatalog.lineage.v1.Lineage.CreateRun].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.lineage.Run:
                    A lineage run represents an execution
                of a process that creates lineage
                events.

            """

            http_options = _BaseLineageRestTransport._BaseCreateRun._get_http_options()
            request, metadata = self._interceptor.pre_create_run(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLineageRestTransport._BaseCreateRun,
                    "_BaseCreateRun__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.datacatalog.lineage_v1.LineageClient.CreateRun",
                    extra={
                        "serviceName": "google.cloud.datacatalog.lineage.v1.Lineage",
                        "rpcName": "CreateRun",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LineageRestTransport._CreateRun._get_response(
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
            resp = lineage.Run()
            pb_resp = lineage.Run.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_run(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_run_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = lineage.Run.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.datacatalog.lineage_v1.LineageClient.create_run",
                    extra={
                        "serviceName": "google.cloud.datacatalog.lineage.v1.Lineage",
                        "rpcName": "CreateRun",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteLineageEvent(
        _BaseLineageRestTransport._BaseDeleteLineageEvent, LineageRestStub
    ):
        def __hash__(self):
            return hash("LineageRestTransport.DeleteLineageEvent")

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
            request: lineage.DeleteLineageEventRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete lineage event method over HTTP.

            Args:
                request (~.lineage.DeleteLineageEventRequest):
                    The request object. Request message for
                [DeleteLineageEvent][google.cloud.datacatalog.lineage.v1.Lineage.DeleteLineageEvent].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseLineageRestTransport._BaseDeleteLineageEvent._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_lineage_event(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLineageRestTransport._BaseDeleteLineageEvent,
                    "_BaseDeleteLineageEvent__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.datacatalog.lineage_v1.LineageClient.DeleteLineageEvent",
                    extra={
                        "serviceName": "google.cloud.datacatalog.lineage.v1.Lineage",
                        "rpcName": "DeleteLineageEvent",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LineageRestTransport._DeleteLineageEvent._get_response(
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

    class _DeleteProcess(_BaseLineageRestTransport._BaseDeleteProcess, LineageRestStub):
        def __hash__(self):
            return hash("LineageRestTransport.DeleteProcess")

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
            request: lineage.DeleteProcessRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete process method over HTTP.

            Args:
                request (~.lineage.DeleteProcessRequest):
                    The request object. Request message for
                [DeleteProcess][google.cloud.datacatalog.lineage.v1.Lineage.DeleteProcess].
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
                _BaseLineageRestTransport._BaseDeleteProcess._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_process(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLineageRestTransport._BaseDeleteProcess,
                    "_BaseDeleteProcess__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.datacatalog.lineage_v1.LineageClient.DeleteProcess",
                    extra={
                        "serviceName": "google.cloud.datacatalog.lineage.v1.Lineage",
                        "rpcName": "DeleteProcess",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LineageRestTransport._DeleteProcess._get_response(
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

            resp = self._interceptor.post_delete_process(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_process_with_metadata(
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
                    "Received response for google.cloud.datacatalog.lineage_v1.LineageClient.delete_process",
                    extra={
                        "serviceName": "google.cloud.datacatalog.lineage.v1.Lineage",
                        "rpcName": "DeleteProcess",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteRun(_BaseLineageRestTransport._BaseDeleteRun, LineageRestStub):
        def __hash__(self):
            return hash("LineageRestTransport.DeleteRun")

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
            request: lineage.DeleteRunRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete run method over HTTP.

            Args:
                request (~.lineage.DeleteRunRequest):
                    The request object. Request message for
                [DeleteRun][google.cloud.datacatalog.lineage.v1.Lineage.DeleteRun].
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

            http_options = _BaseLineageRestTransport._BaseDeleteRun._get_http_options()
            request, metadata = self._interceptor.pre_delete_run(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLineageRestTransport._BaseDeleteRun,
                    "_BaseDeleteRun__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.datacatalog.lineage_v1.LineageClient.DeleteRun",
                    extra={
                        "serviceName": "google.cloud.datacatalog.lineage.v1.Lineage",
                        "rpcName": "DeleteRun",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LineageRestTransport._DeleteRun._get_response(
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

            resp = self._interceptor.post_delete_run(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_run_with_metadata(
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
                    "Received response for google.cloud.datacatalog.lineage_v1.LineageClient.delete_run",
                    extra={
                        "serviceName": "google.cloud.datacatalog.lineage.v1.Lineage",
                        "rpcName": "DeleteRun",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetLineageEvent(
        _BaseLineageRestTransport._BaseGetLineageEvent, LineageRestStub
    ):
        def __hash__(self):
            return hash("LineageRestTransport.GetLineageEvent")

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
            request: lineage.GetLineageEventRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> lineage.LineageEvent:
            r"""Call the get lineage event method over HTTP.

            Args:
                request (~.lineage.GetLineageEventRequest):
                    The request object. Request message for
                [GetLineageEvent][google.cloud.datacatalog.lineage.v1.Lineage.GetLineageEvent].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.lineage.LineageEvent:
                    A lineage event represents an
                operation on assets. Within the
                operation, the data flows from the
                source to the target defined in the
                links field.

            """

            http_options = (
                _BaseLineageRestTransport._BaseGetLineageEvent._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_lineage_event(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLineageRestTransport._BaseGetLineageEvent,
                    "_BaseGetLineageEvent__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.datacatalog.lineage_v1.LineageClient.GetLineageEvent",
                    extra={
                        "serviceName": "google.cloud.datacatalog.lineage.v1.Lineage",
                        "rpcName": "GetLineageEvent",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LineageRestTransport._GetLineageEvent._get_response(
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
            resp = lineage.LineageEvent()
            pb_resp = lineage.LineageEvent.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_lineage_event(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_lineage_event_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = lineage.LineageEvent.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.datacatalog.lineage_v1.LineageClient.get_lineage_event",
                    extra={
                        "serviceName": "google.cloud.datacatalog.lineage.v1.Lineage",
                        "rpcName": "GetLineageEvent",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetProcess(_BaseLineageRestTransport._BaseGetProcess, LineageRestStub):
        def __hash__(self):
            return hash("LineageRestTransport.GetProcess")

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
            request: lineage.GetProcessRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> lineage.Process:
            r"""Call the get process method over HTTP.

            Args:
                request (~.lineage.GetProcessRequest):
                    The request object. Request message for
                [GetProcess][google.cloud.datacatalog.lineage.v1.Lineage.GetProcess].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.lineage.Process:
                    A process is the definition of a data
                transformation operation.

            """

            http_options = _BaseLineageRestTransport._BaseGetProcess._get_http_options()
            request, metadata = self._interceptor.pre_get_process(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLineageRestTransport._BaseGetProcess,
                    "_BaseGetProcess__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.datacatalog.lineage_v1.LineageClient.GetProcess",
                    extra={
                        "serviceName": "google.cloud.datacatalog.lineage.v1.Lineage",
                        "rpcName": "GetProcess",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LineageRestTransport._GetProcess._get_response(
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
            resp = lineage.Process()
            pb_resp = lineage.Process.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_process(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_process_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = lineage.Process.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.datacatalog.lineage_v1.LineageClient.get_process",
                    extra={
                        "serviceName": "google.cloud.datacatalog.lineage.v1.Lineage",
                        "rpcName": "GetProcess",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetRun(_BaseLineageRestTransport._BaseGetRun, LineageRestStub):
        def __hash__(self):
            return hash("LineageRestTransport.GetRun")

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
            request: lineage.GetRunRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> lineage.Run:
            r"""Call the get run method over HTTP.

            Args:
                request (~.lineage.GetRunRequest):
                    The request object. Request message for
                [GetRun][google.cloud.datacatalog.lineage.v1.Lineage.GetRun].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.lineage.Run:
                    A lineage run represents an execution
                of a process that creates lineage
                events.

            """

            http_options = _BaseLineageRestTransport._BaseGetRun._get_http_options()
            request, metadata = self._interceptor.pre_get_run(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLineageRestTransport._BaseGetRun,
                    "_BaseGetRun__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.datacatalog.lineage_v1.LineageClient.GetRun",
                    extra={
                        "serviceName": "google.cloud.datacatalog.lineage.v1.Lineage",
                        "rpcName": "GetRun",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LineageRestTransport._GetRun._get_response(
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
            resp = lineage.Run()
            pb_resp = lineage.Run.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_run(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_run_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = lineage.Run.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.datacatalog.lineage_v1.LineageClient.get_run",
                    extra={
                        "serviceName": "google.cloud.datacatalog.lineage.v1.Lineage",
                        "rpcName": "GetRun",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListLineageEvents(
        _BaseLineageRestTransport._BaseListLineageEvents, LineageRestStub
    ):
        def __hash__(self):
            return hash("LineageRestTransport.ListLineageEvents")

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
            request: lineage.ListLineageEventsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> lineage.ListLineageEventsResponse:
            r"""Call the list lineage events method over HTTP.

            Args:
                request (~.lineage.ListLineageEventsRequest):
                    The request object. Request message for
                [ListLineageEvents][google.cloud.datacatalog.lineage.v1.Lineage.ListLineageEvents].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.lineage.ListLineageEventsResponse:
                    Response message for
                [ListLineageEvents][google.cloud.datacatalog.lineage.v1.Lineage.ListLineageEvents].

            """

            http_options = (
                _BaseLineageRestTransport._BaseListLineageEvents._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_lineage_events(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLineageRestTransport._BaseListLineageEvents,
                    "_BaseListLineageEvents__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.datacatalog.lineage_v1.LineageClient.ListLineageEvents",
                    extra={
                        "serviceName": "google.cloud.datacatalog.lineage.v1.Lineage",
                        "rpcName": "ListLineageEvents",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LineageRestTransport._ListLineageEvents._get_response(
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
            resp = lineage.ListLineageEventsResponse()
            pb_resp = lineage.ListLineageEventsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_lineage_events(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_lineage_events_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = lineage.ListLineageEventsResponse.to_json(
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
                    "Received response for google.cloud.datacatalog.lineage_v1.LineageClient.list_lineage_events",
                    extra={
                        "serviceName": "google.cloud.datacatalog.lineage.v1.Lineage",
                        "rpcName": "ListLineageEvents",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListProcesses(_BaseLineageRestTransport._BaseListProcesses, LineageRestStub):
        def __hash__(self):
            return hash("LineageRestTransport.ListProcesses")

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
            request: lineage.ListProcessesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> lineage.ListProcessesResponse:
            r"""Call the list processes method over HTTP.

            Args:
                request (~.lineage.ListProcessesRequest):
                    The request object. Request message for
                [ListProcesses][google.cloud.datacatalog.lineage.v1.Lineage.ListProcesses].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.lineage.ListProcessesResponse:
                    Response message for
                [ListProcesses][google.cloud.datacatalog.lineage.v1.Lineage.ListProcesses].

            """

            http_options = (
                _BaseLineageRestTransport._BaseListProcesses._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_processes(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLineageRestTransport._BaseListProcesses,
                    "_BaseListProcesses__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.datacatalog.lineage_v1.LineageClient.ListProcesses",
                    extra={
                        "serviceName": "google.cloud.datacatalog.lineage.v1.Lineage",
                        "rpcName": "ListProcesses",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LineageRestTransport._ListProcesses._get_response(
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
            resp = lineage.ListProcessesResponse()
            pb_resp = lineage.ListProcessesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_processes(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_processes_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = lineage.ListProcessesResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.datacatalog.lineage_v1.LineageClient.list_processes",
                    extra={
                        "serviceName": "google.cloud.datacatalog.lineage.v1.Lineage",
                        "rpcName": "ListProcesses",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListRuns(_BaseLineageRestTransport._BaseListRuns, LineageRestStub):
        def __hash__(self):
            return hash("LineageRestTransport.ListRuns")

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
            request: lineage.ListRunsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> lineage.ListRunsResponse:
            r"""Call the list runs method over HTTP.

            Args:
                request (~.lineage.ListRunsRequest):
                    The request object. Request message for
                [ListRuns][google.cloud.datacatalog.lineage.v1.Lineage.ListRuns].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.lineage.ListRunsResponse:
                    Response message for
                [ListRuns][google.cloud.datacatalog.lineage.v1.Lineage.ListRuns].

            """

            http_options = _BaseLineageRestTransport._BaseListRuns._get_http_options()
            request, metadata = self._interceptor.pre_list_runs(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLineageRestTransport._BaseListRuns,
                    "_BaseListRuns__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.datacatalog.lineage_v1.LineageClient.ListRuns",
                    extra={
                        "serviceName": "google.cloud.datacatalog.lineage.v1.Lineage",
                        "rpcName": "ListRuns",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LineageRestTransport._ListRuns._get_response(
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
            resp = lineage.ListRunsResponse()
            pb_resp = lineage.ListRunsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_runs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_runs_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = lineage.ListRunsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.datacatalog.lineage_v1.LineageClient.list_runs",
                    extra={
                        "serviceName": "google.cloud.datacatalog.lineage.v1.Lineage",
                        "rpcName": "ListRuns",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ProcessOpenLineageRunEvent(
        _BaseLineageRestTransport._BaseProcessOpenLineageRunEvent, LineageRestStub
    ):
        def __hash__(self):
            return hash("LineageRestTransport.ProcessOpenLineageRunEvent")

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
            request: lineage.ProcessOpenLineageRunEventRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> lineage.ProcessOpenLineageRunEventResponse:
            r"""Call the process open lineage run
            event method over HTTP.

                Args:
                    request (~.lineage.ProcessOpenLineageRunEventRequest):
                        The request object. Request message for
                    [ProcessOpenLineageRunEvent][google.cloud.datacatalog.lineage.v1.Lineage.ProcessOpenLineageRunEvent].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.lineage.ProcessOpenLineageRunEventResponse:
                        Response message for
                    [ProcessOpenLineageRunEvent][google.cloud.datacatalog.lineage.v1.Lineage.ProcessOpenLineageRunEvent].

            """

            http_options = _BaseLineageRestTransport._BaseProcessOpenLineageRunEvent._get_http_options()
            request, metadata = self._interceptor.pre_process_open_lineage_run_event(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLineageRestTransport._BaseProcessOpenLineageRunEvent,
                    "_BaseProcessOpenLineageRunEvent__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.datacatalog.lineage_v1.LineageClient.ProcessOpenLineageRunEvent",
                    extra={
                        "serviceName": "google.cloud.datacatalog.lineage.v1.Lineage",
                        "rpcName": "ProcessOpenLineageRunEvent",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LineageRestTransport._ProcessOpenLineageRunEvent._get_response(
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
            resp = lineage.ProcessOpenLineageRunEventResponse()
            pb_resp = lineage.ProcessOpenLineageRunEventResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_process_open_lineage_run_event(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_process_open_lineage_run_event_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        lineage.ProcessOpenLineageRunEventResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.datacatalog.lineage_v1.LineageClient.process_open_lineage_run_event",
                    extra={
                        "serviceName": "google.cloud.datacatalog.lineage.v1.Lineage",
                        "rpcName": "ProcessOpenLineageRunEvent",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SearchLineageStreaming(
        _BaseLineageRestTransport._BaseSearchLineageStreaming, LineageRestStub
    ):
        def __hash__(self):
            return hash("LineageRestTransport.SearchLineageStreaming")

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
                stream=True,
            )
            return response

        def __call__(
            self,
            request: lineage.SearchLineageStreamingRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> rest_streaming.ResponseIterator:
            r"""Call the search lineage streaming method over HTTP.

            Args:
                request (~.lineage.SearchLineageStreamingRequest):
                    The request object. Request message for
                [SearchLineageStreaming][google.cloud.datacatalog.lineage.v1.Lineage.SearchLineageStreaming].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.lineage.SearchLineageStreamingResponse:
                    Response message for
                [SearchLineageStreaming][google.cloud.datacatalog.lineage.v1.Lineage.SearchLineageStreaming].

            """

            http_options = _BaseLineageRestTransport._BaseSearchLineageStreaming._get_http_options()
            request, metadata = self._interceptor.pre_search_lineage_streaming(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLineageRestTransport._BaseSearchLineageStreaming,
                    "_BaseSearchLineageStreaming__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.datacatalog.lineage_v1.LineageClient.SearchLineageStreaming",
                    extra={
                        "serviceName": "google.cloud.datacatalog.lineage.v1.Lineage",
                        "rpcName": "SearchLineageStreaming",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LineageRestTransport._SearchLineageStreaming._get_response(
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
            resp = rest_streaming.ResponseIterator(
                response, lineage.SearchLineageStreamingResponse
            )

            resp = self._interceptor.post_search_lineage_streaming(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_search_lineage_streaming_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                http_response = {
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.datacatalog.lineage_v1.LineageClient.search_lineage_streaming",
                    extra={
                        "serviceName": "google.cloud.datacatalog.lineage.v1.Lineage",
                        "rpcName": "SearchLineageStreaming",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SearchLinks(_BaseLineageRestTransport._BaseSearchLinks, LineageRestStub):
        def __hash__(self):
            return hash("LineageRestTransport.SearchLinks")

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
            request: lineage.SearchLinksRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> lineage.SearchLinksResponse:
            r"""Call the search links method over HTTP.

            Args:
                request (~.lineage.SearchLinksRequest):
                    The request object. Request message for
                [SearchLinks][google.cloud.datacatalog.lineage.v1.Lineage.SearchLinks].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.lineage.SearchLinksResponse:
                    Response message for
                [SearchLinks][google.cloud.datacatalog.lineage.v1.Lineage.SearchLinks].

            """

            http_options = (
                _BaseLineageRestTransport._BaseSearchLinks._get_http_options()
            )
            request, metadata = self._interceptor.pre_search_links(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLineageRestTransport._BaseSearchLinks,
                    "_BaseSearchLinks__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.datacatalog.lineage_v1.LineageClient.SearchLinks",
                    extra={
                        "serviceName": "google.cloud.datacatalog.lineage.v1.Lineage",
                        "rpcName": "SearchLinks",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LineageRestTransport._SearchLinks._get_response(
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
            resp = lineage.SearchLinksResponse()
            pb_resp = lineage.SearchLinksResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_search_links(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_search_links_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = lineage.SearchLinksResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.datacatalog.lineage_v1.LineageClient.search_links",
                    extra={
                        "serviceName": "google.cloud.datacatalog.lineage.v1.Lineage",
                        "rpcName": "SearchLinks",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateProcess(_BaseLineageRestTransport._BaseUpdateProcess, LineageRestStub):
        def __hash__(self):
            return hash("LineageRestTransport.UpdateProcess")

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
            request: lineage.UpdateProcessRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> lineage.Process:
            r"""Call the update process method over HTTP.

            Args:
                request (~.lineage.UpdateProcessRequest):
                    The request object. Request message for
                [UpdateProcess][google.cloud.datacatalog.lineage.v1.Lineage.UpdateProcess].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.lineage.Process:
                    A process is the definition of a data
                transformation operation.

            """

            http_options = (
                _BaseLineageRestTransport._BaseUpdateProcess._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_process(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLineageRestTransport._BaseUpdateProcess,
                    "_BaseUpdateProcess__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.datacatalog.lineage_v1.LineageClient.UpdateProcess",
                    extra={
                        "serviceName": "google.cloud.datacatalog.lineage.v1.Lineage",
                        "rpcName": "UpdateProcess",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LineageRestTransport._UpdateProcess._get_response(
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
            resp = lineage.Process()
            pb_resp = lineage.Process.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_process(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_process_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = lineage.Process.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.datacatalog.lineage_v1.LineageClient.update_process",
                    extra={
                        "serviceName": "google.cloud.datacatalog.lineage.v1.Lineage",
                        "rpcName": "UpdateProcess",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateRun(_BaseLineageRestTransport._BaseUpdateRun, LineageRestStub):
        def __hash__(self):
            return hash("LineageRestTransport.UpdateRun")

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
            request: lineage.UpdateRunRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> lineage.Run:
            r"""Call the update run method over HTTP.

            Args:
                request (~.lineage.UpdateRunRequest):
                    The request object. Request message for
                [UpdateRun][google.cloud.datacatalog.lineage.v1.Lineage.UpdateRun].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.lineage.Run:
                    A lineage run represents an execution
                of a process that creates lineage
                events.

            """

            http_options = _BaseLineageRestTransport._BaseUpdateRun._get_http_options()
            request, metadata = self._interceptor.pre_update_run(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLineageRestTransport._BaseUpdateRun,
                    "_BaseUpdateRun__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.datacatalog.lineage_v1.LineageClient.UpdateRun",
                    extra={
                        "serviceName": "google.cloud.datacatalog.lineage.v1.Lineage",
                        "rpcName": "UpdateRun",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LineageRestTransport._UpdateRun._get_response(
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
            resp = lineage.Run()
            pb_resp = lineage.Run.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_run(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_run_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = lineage.Run.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.datacatalog.lineage_v1.LineageClient.update_run",
                    extra={
                        "serviceName": "google.cloud.datacatalog.lineage.v1.Lineage",
                        "rpcName": "UpdateRun",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def batch_search_link_processes(
        self,
    ) -> Callable[
        [lineage.BatchSearchLinkProcessesRequest],
        lineage.BatchSearchLinkProcessesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchSearchLinkProcesses(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_lineage_event(
        self,
    ) -> Callable[[lineage.CreateLineageEventRequest], lineage.LineageEvent]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateLineageEvent(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_process(
        self,
    ) -> Callable[[lineage.CreateProcessRequest], lineage.Process]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateProcess(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_run(self) -> Callable[[lineage.CreateRunRequest], lineage.Run]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateRun(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_lineage_event(
        self,
    ) -> Callable[[lineage.DeleteLineageEventRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteLineageEvent(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_process(
        self,
    ) -> Callable[[lineage.DeleteProcessRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteProcess(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_run(
        self,
    ) -> Callable[[lineage.DeleteRunRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteRun(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_lineage_event(
        self,
    ) -> Callable[[lineage.GetLineageEventRequest], lineage.LineageEvent]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetLineageEvent(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_process(self) -> Callable[[lineage.GetProcessRequest], lineage.Process]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetProcess(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_run(self) -> Callable[[lineage.GetRunRequest], lineage.Run]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetRun(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_lineage_events(
        self,
    ) -> Callable[
        [lineage.ListLineageEventsRequest], lineage.ListLineageEventsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListLineageEvents(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_processes(
        self,
    ) -> Callable[[lineage.ListProcessesRequest], lineage.ListProcessesResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListProcesses(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_runs(
        self,
    ) -> Callable[[lineage.ListRunsRequest], lineage.ListRunsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListRuns(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def process_open_lineage_run_event(
        self,
    ) -> Callable[
        [lineage.ProcessOpenLineageRunEventRequest],
        lineage.ProcessOpenLineageRunEventResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ProcessOpenLineageRunEvent(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def search_lineage_streaming(
        self,
    ) -> Callable[
        [lineage.SearchLineageStreamingRequest], lineage.SearchLineageStreamingResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SearchLineageStreaming(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def search_links(
        self,
    ) -> Callable[[lineage.SearchLinksRequest], lineage.SearchLinksResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SearchLinks(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_process(
        self,
    ) -> Callable[[lineage.UpdateProcessRequest], lineage.Process]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateProcess(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_run(self) -> Callable[[lineage.UpdateRunRequest], lineage.Run]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateRun(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseLineageRestTransport._BaseCancelOperation, LineageRestStub
    ):
        def __hash__(self):
            return hash("LineageRestTransport.CancelOperation")

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
                _BaseLineageRestTransport._BaseCancelOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLineageRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.datacatalog.lineage_v1.LineageClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.datacatalog.lineage.v1.Lineage",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LineageRestTransport._CancelOperation._get_response(
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
        _BaseLineageRestTransport._BaseDeleteOperation, LineageRestStub
    ):
        def __hash__(self):
            return hash("LineageRestTransport.DeleteOperation")

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
                _BaseLineageRestTransport._BaseDeleteOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLineageRestTransport._BaseDeleteOperation,
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
                    f"Sending request for google.cloud.datacatalog.lineage_v1.LineageClient.DeleteOperation",
                    extra={
                        "serviceName": "google.cloud.datacatalog.lineage.v1.Lineage",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LineageRestTransport._DeleteOperation._get_response(
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

    class _GetOperation(_BaseLineageRestTransport._BaseGetOperation, LineageRestStub):
        def __hash__(self):
            return hash("LineageRestTransport.GetOperation")

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
                _BaseLineageRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLineageRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.datacatalog.lineage_v1.LineageClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.datacatalog.lineage.v1.Lineage",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LineageRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.datacatalog.lineage_v1.LineageAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.datacatalog.lineage.v1.Lineage",
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
        _BaseLineageRestTransport._BaseListOperations, LineageRestStub
    ):
        def __hash__(self):
            return hash("LineageRestTransport.ListOperations")

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
                _BaseLineageRestTransport._BaseListOperations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLineageRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.datacatalog.lineage_v1.LineageClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.datacatalog.lineage.v1.Lineage",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LineageRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.datacatalog.lineage_v1.LineageAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.datacatalog.lineage.v1.Lineage",
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


__all__ = ("LineageRestTransport",)
