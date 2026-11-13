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

from grafeas.grafeas_v1._compat import transcode_request
from grafeas.grafeas_v1.types import grafeas

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseGrafeasRestTransport

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


class GrafeasRestInterceptor:
    """Interceptor for Grafeas.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the GrafeasRestTransport.

    .. code-block:: python
        class MyCustomGrafeasInterceptor(GrafeasRestInterceptor):
            def pre_batch_create_notes(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_create_notes(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_create_occurrences(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_create_occurrences(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_note(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_note(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_occurrence(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_occurrence(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_note(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_occurrence(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_get_note(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_note(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_occurrence(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_occurrence(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_occurrence_note(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_occurrence_note(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_note_occurrences(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_note_occurrences(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_notes(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_notes(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_occurrences(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_occurrences(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_note(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_note(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_occurrence(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_occurrence(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = GrafeasRestTransport(interceptor=MyCustomGrafeasInterceptor())
        client = GrafeasClient(transport=transport)


    """

    def pre_batch_create_notes(
        self,
        request: grafeas.BatchCreateNotesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        grafeas.BatchCreateNotesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for batch_create_notes

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Grafeas server.
        """
        return request, metadata

    def post_batch_create_notes(
        self, response: grafeas.BatchCreateNotesResponse
    ) -> grafeas.BatchCreateNotesResponse:
        """Post-rpc interceptor for batch_create_notes

        DEPRECATED. Please use the `post_batch_create_notes_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Grafeas server but before
        it is returned to user code. This `post_batch_create_notes` interceptor runs
        before the `post_batch_create_notes_with_metadata` interceptor.
        """
        return response

    def post_batch_create_notes_with_metadata(
        self,
        response: grafeas.BatchCreateNotesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        grafeas.BatchCreateNotesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for batch_create_notes

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Grafeas server but before it is returned to user code.

        We recommend only using this `post_batch_create_notes_with_metadata`
        interceptor in new development instead of the `post_batch_create_notes` interceptor.
        When both interceptors are used, this `post_batch_create_notes_with_metadata` interceptor runs after the
        `post_batch_create_notes` interceptor. The (possibly modified) response returned by
        `post_batch_create_notes` will be passed to
        `post_batch_create_notes_with_metadata`.
        """
        return response, metadata

    def pre_batch_create_occurrences(
        self,
        request: grafeas.BatchCreateOccurrencesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        grafeas.BatchCreateOccurrencesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for batch_create_occurrences

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Grafeas server.
        """
        return request, metadata

    def post_batch_create_occurrences(
        self, response: grafeas.BatchCreateOccurrencesResponse
    ) -> grafeas.BatchCreateOccurrencesResponse:
        """Post-rpc interceptor for batch_create_occurrences

        DEPRECATED. Please use the `post_batch_create_occurrences_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Grafeas server but before
        it is returned to user code. This `post_batch_create_occurrences` interceptor runs
        before the `post_batch_create_occurrences_with_metadata` interceptor.
        """
        return response

    def post_batch_create_occurrences_with_metadata(
        self,
        response: grafeas.BatchCreateOccurrencesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        grafeas.BatchCreateOccurrencesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for batch_create_occurrences

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Grafeas server but before it is returned to user code.

        We recommend only using this `post_batch_create_occurrences_with_metadata`
        interceptor in new development instead of the `post_batch_create_occurrences` interceptor.
        When both interceptors are used, this `post_batch_create_occurrences_with_metadata` interceptor runs after the
        `post_batch_create_occurrences` interceptor. The (possibly modified) response returned by
        `post_batch_create_occurrences` will be passed to
        `post_batch_create_occurrences_with_metadata`.
        """
        return response, metadata

    def pre_create_note(
        self,
        request: grafeas.CreateNoteRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[grafeas.CreateNoteRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_note

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Grafeas server.
        """
        return request, metadata

    def post_create_note(self, response: grafeas.Note) -> grafeas.Note:
        """Post-rpc interceptor for create_note

        DEPRECATED. Please use the `post_create_note_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Grafeas server but before
        it is returned to user code. This `post_create_note` interceptor runs
        before the `post_create_note_with_metadata` interceptor.
        """
        return response

    def post_create_note_with_metadata(
        self, response: grafeas.Note, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[grafeas.Note, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_note

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Grafeas server but before it is returned to user code.

        We recommend only using this `post_create_note_with_metadata`
        interceptor in new development instead of the `post_create_note` interceptor.
        When both interceptors are used, this `post_create_note_with_metadata` interceptor runs after the
        `post_create_note` interceptor. The (possibly modified) response returned by
        `post_create_note` will be passed to
        `post_create_note_with_metadata`.
        """
        return response, metadata

    def pre_create_occurrence(
        self,
        request: grafeas.CreateOccurrenceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        grafeas.CreateOccurrenceRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_occurrence

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Grafeas server.
        """
        return request, metadata

    def post_create_occurrence(
        self, response: grafeas.Occurrence
    ) -> grafeas.Occurrence:
        """Post-rpc interceptor for create_occurrence

        DEPRECATED. Please use the `post_create_occurrence_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Grafeas server but before
        it is returned to user code. This `post_create_occurrence` interceptor runs
        before the `post_create_occurrence_with_metadata` interceptor.
        """
        return response

    def post_create_occurrence_with_metadata(
        self,
        response: grafeas.Occurrence,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[grafeas.Occurrence, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_occurrence

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Grafeas server but before it is returned to user code.

        We recommend only using this `post_create_occurrence_with_metadata`
        interceptor in new development instead of the `post_create_occurrence` interceptor.
        When both interceptors are used, this `post_create_occurrence_with_metadata` interceptor runs after the
        `post_create_occurrence` interceptor. The (possibly modified) response returned by
        `post_create_occurrence` will be passed to
        `post_create_occurrence_with_metadata`.
        """
        return response, metadata

    def pre_delete_note(
        self,
        request: grafeas.DeleteNoteRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[grafeas.DeleteNoteRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_note

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Grafeas server.
        """
        return request, metadata

    def pre_delete_occurrence(
        self,
        request: grafeas.DeleteOccurrenceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        grafeas.DeleteOccurrenceRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_occurrence

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Grafeas server.
        """
        return request, metadata

    def pre_get_note(
        self,
        request: grafeas.GetNoteRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[grafeas.GetNoteRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_note

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Grafeas server.
        """
        return request, metadata

    def post_get_note(self, response: grafeas.Note) -> grafeas.Note:
        """Post-rpc interceptor for get_note

        DEPRECATED. Please use the `post_get_note_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Grafeas server but before
        it is returned to user code. This `post_get_note` interceptor runs
        before the `post_get_note_with_metadata` interceptor.
        """
        return response

    def post_get_note_with_metadata(
        self, response: grafeas.Note, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[grafeas.Note, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_note

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Grafeas server but before it is returned to user code.

        We recommend only using this `post_get_note_with_metadata`
        interceptor in new development instead of the `post_get_note` interceptor.
        When both interceptors are used, this `post_get_note_with_metadata` interceptor runs after the
        `post_get_note` interceptor. The (possibly modified) response returned by
        `post_get_note` will be passed to
        `post_get_note_with_metadata`.
        """
        return response, metadata

    def pre_get_occurrence(
        self,
        request: grafeas.GetOccurrenceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[grafeas.GetOccurrenceRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_occurrence

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Grafeas server.
        """
        return request, metadata

    def post_get_occurrence(self, response: grafeas.Occurrence) -> grafeas.Occurrence:
        """Post-rpc interceptor for get_occurrence

        DEPRECATED. Please use the `post_get_occurrence_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Grafeas server but before
        it is returned to user code. This `post_get_occurrence` interceptor runs
        before the `post_get_occurrence_with_metadata` interceptor.
        """
        return response

    def post_get_occurrence_with_metadata(
        self,
        response: grafeas.Occurrence,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[grafeas.Occurrence, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_occurrence

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Grafeas server but before it is returned to user code.

        We recommend only using this `post_get_occurrence_with_metadata`
        interceptor in new development instead of the `post_get_occurrence` interceptor.
        When both interceptors are used, this `post_get_occurrence_with_metadata` interceptor runs after the
        `post_get_occurrence` interceptor. The (possibly modified) response returned by
        `post_get_occurrence` will be passed to
        `post_get_occurrence_with_metadata`.
        """
        return response, metadata

    def pre_get_occurrence_note(
        self,
        request: grafeas.GetOccurrenceNoteRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        grafeas.GetOccurrenceNoteRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_occurrence_note

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Grafeas server.
        """
        return request, metadata

    def post_get_occurrence_note(self, response: grafeas.Note) -> grafeas.Note:
        """Post-rpc interceptor for get_occurrence_note

        DEPRECATED. Please use the `post_get_occurrence_note_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Grafeas server but before
        it is returned to user code. This `post_get_occurrence_note` interceptor runs
        before the `post_get_occurrence_note_with_metadata` interceptor.
        """
        return response

    def post_get_occurrence_note_with_metadata(
        self, response: grafeas.Note, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[grafeas.Note, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_occurrence_note

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Grafeas server but before it is returned to user code.

        We recommend only using this `post_get_occurrence_note_with_metadata`
        interceptor in new development instead of the `post_get_occurrence_note` interceptor.
        When both interceptors are used, this `post_get_occurrence_note_with_metadata` interceptor runs after the
        `post_get_occurrence_note` interceptor. The (possibly modified) response returned by
        `post_get_occurrence_note` will be passed to
        `post_get_occurrence_note_with_metadata`.
        """
        return response, metadata

    def pre_list_note_occurrences(
        self,
        request: grafeas.ListNoteOccurrencesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        grafeas.ListNoteOccurrencesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_note_occurrences

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Grafeas server.
        """
        return request, metadata

    def post_list_note_occurrences(
        self, response: grafeas.ListNoteOccurrencesResponse
    ) -> grafeas.ListNoteOccurrencesResponse:
        """Post-rpc interceptor for list_note_occurrences

        DEPRECATED. Please use the `post_list_note_occurrences_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Grafeas server but before
        it is returned to user code. This `post_list_note_occurrences` interceptor runs
        before the `post_list_note_occurrences_with_metadata` interceptor.
        """
        return response

    def post_list_note_occurrences_with_metadata(
        self,
        response: grafeas.ListNoteOccurrencesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        grafeas.ListNoteOccurrencesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_note_occurrences

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Grafeas server but before it is returned to user code.

        We recommend only using this `post_list_note_occurrences_with_metadata`
        interceptor in new development instead of the `post_list_note_occurrences` interceptor.
        When both interceptors are used, this `post_list_note_occurrences_with_metadata` interceptor runs after the
        `post_list_note_occurrences` interceptor. The (possibly modified) response returned by
        `post_list_note_occurrences` will be passed to
        `post_list_note_occurrences_with_metadata`.
        """
        return response, metadata

    def pre_list_notes(
        self,
        request: grafeas.ListNotesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[grafeas.ListNotesRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_notes

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Grafeas server.
        """
        return request, metadata

    def post_list_notes(
        self, response: grafeas.ListNotesResponse
    ) -> grafeas.ListNotesResponse:
        """Post-rpc interceptor for list_notes

        DEPRECATED. Please use the `post_list_notes_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Grafeas server but before
        it is returned to user code. This `post_list_notes` interceptor runs
        before the `post_list_notes_with_metadata` interceptor.
        """
        return response

    def post_list_notes_with_metadata(
        self,
        response: grafeas.ListNotesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[grafeas.ListNotesResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_notes

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Grafeas server but before it is returned to user code.

        We recommend only using this `post_list_notes_with_metadata`
        interceptor in new development instead of the `post_list_notes` interceptor.
        When both interceptors are used, this `post_list_notes_with_metadata` interceptor runs after the
        `post_list_notes` interceptor. The (possibly modified) response returned by
        `post_list_notes` will be passed to
        `post_list_notes_with_metadata`.
        """
        return response, metadata

    def pre_list_occurrences(
        self,
        request: grafeas.ListOccurrencesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[grafeas.ListOccurrencesRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_occurrences

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Grafeas server.
        """
        return request, metadata

    def post_list_occurrences(
        self, response: grafeas.ListOccurrencesResponse
    ) -> grafeas.ListOccurrencesResponse:
        """Post-rpc interceptor for list_occurrences

        DEPRECATED. Please use the `post_list_occurrences_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Grafeas server but before
        it is returned to user code. This `post_list_occurrences` interceptor runs
        before the `post_list_occurrences_with_metadata` interceptor.
        """
        return response

    def post_list_occurrences_with_metadata(
        self,
        response: grafeas.ListOccurrencesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        grafeas.ListOccurrencesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_occurrences

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Grafeas server but before it is returned to user code.

        We recommend only using this `post_list_occurrences_with_metadata`
        interceptor in new development instead of the `post_list_occurrences` interceptor.
        When both interceptors are used, this `post_list_occurrences_with_metadata` interceptor runs after the
        `post_list_occurrences` interceptor. The (possibly modified) response returned by
        `post_list_occurrences` will be passed to
        `post_list_occurrences_with_metadata`.
        """
        return response, metadata

    def pre_update_note(
        self,
        request: grafeas.UpdateNoteRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[grafeas.UpdateNoteRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_note

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Grafeas server.
        """
        return request, metadata

    def post_update_note(self, response: grafeas.Note) -> grafeas.Note:
        """Post-rpc interceptor for update_note

        DEPRECATED. Please use the `post_update_note_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Grafeas server but before
        it is returned to user code. This `post_update_note` interceptor runs
        before the `post_update_note_with_metadata` interceptor.
        """
        return response

    def post_update_note_with_metadata(
        self, response: grafeas.Note, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[grafeas.Note, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_note

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Grafeas server but before it is returned to user code.

        We recommend only using this `post_update_note_with_metadata`
        interceptor in new development instead of the `post_update_note` interceptor.
        When both interceptors are used, this `post_update_note_with_metadata` interceptor runs after the
        `post_update_note` interceptor. The (possibly modified) response returned by
        `post_update_note` will be passed to
        `post_update_note_with_metadata`.
        """
        return response, metadata

    def pre_update_occurrence(
        self,
        request: grafeas.UpdateOccurrenceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        grafeas.UpdateOccurrenceRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_occurrence

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Grafeas server.
        """
        return request, metadata

    def post_update_occurrence(
        self, response: grafeas.Occurrence
    ) -> grafeas.Occurrence:
        """Post-rpc interceptor for update_occurrence

        DEPRECATED. Please use the `post_update_occurrence_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Grafeas server but before
        it is returned to user code. This `post_update_occurrence` interceptor runs
        before the `post_update_occurrence_with_metadata` interceptor.
        """
        return response

    def post_update_occurrence_with_metadata(
        self,
        response: grafeas.Occurrence,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[grafeas.Occurrence, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_occurrence

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Grafeas server but before it is returned to user code.

        We recommend only using this `post_update_occurrence_with_metadata`
        interceptor in new development instead of the `post_update_occurrence` interceptor.
        When both interceptors are used, this `post_update_occurrence_with_metadata` interceptor runs after the
        `post_update_occurrence` interceptor. The (possibly modified) response returned by
        `post_update_occurrence` will be passed to
        `post_update_occurrence_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class GrafeasRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: GrafeasRestInterceptor


class GrafeasRestTransport(_BaseGrafeasRestTransport):
    """REST backend synchronous transport for Grafeas.

    `Grafeas <https://grafeas.io>`__ API.

    Retrieves analysis results of Cloud components such as Docker
    container images.

    Analysis results are stored as a series of occurrences. An
    ``Occurrence`` contains information about a specific analysis
    instance on a resource. An occurrence refers to a ``Note``. A note
    contains details describing the analysis and is generally stored in
    a separate project, called a ``Provider``. Multiple occurrences can
    refer to the same note.

    For example, an SSL vulnerability could affect multiple images. In
    this case, there would be one note for the vulnerability and an
    occurrence for each image with the vulnerability referring to that
    note.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[GrafeasRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: '').
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
            interceptor (Optional[GrafeasRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or GrafeasRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _BatchCreateNotes(
        _BaseGrafeasRestTransport._BaseBatchCreateNotes, GrafeasRestStub
    ):
        def __hash__(self):
            return hash("GrafeasRestTransport.BatchCreateNotes")

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
            request: grafeas.BatchCreateNotesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> grafeas.BatchCreateNotesResponse:
            r"""Call the batch create notes method over HTTP.

            Args:
                request (~.grafeas.BatchCreateNotesRequest):
                    The request object. Request to create notes in batch.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.grafeas.BatchCreateNotesResponse:
                    Response for creating notes in batch.
            """

            http_options = (
                _BaseGrafeasRestTransport._BaseBatchCreateNotes._get_http_options()
            )
            request, metadata = self._interceptor.pre_batch_create_notes(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGrafeasRestTransport._BaseBatchCreateNotes,
                    "_BaseBatchCreateNotes__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for grafeas_v1.GrafeasClient.BatchCreateNotes",
                    extra={
                        "serviceName": "grafeas.v1.Grafeas",
                        "rpcName": "BatchCreateNotes",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GrafeasRestTransport._BatchCreateNotes._get_response(
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
            resp = grafeas.BatchCreateNotesResponse()
            pb_resp = grafeas.BatchCreateNotesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_create_notes(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_create_notes_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = grafeas.BatchCreateNotesResponse.to_json(
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
                    "Received response for grafeas_v1.GrafeasClient.batch_create_notes",
                    extra={
                        "serviceName": "grafeas.v1.Grafeas",
                        "rpcName": "BatchCreateNotes",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchCreateOccurrences(
        _BaseGrafeasRestTransport._BaseBatchCreateOccurrences, GrafeasRestStub
    ):
        def __hash__(self):
            return hash("GrafeasRestTransport.BatchCreateOccurrences")

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
            request: grafeas.BatchCreateOccurrencesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> grafeas.BatchCreateOccurrencesResponse:
            r"""Call the batch create occurrences method over HTTP.

            Args:
                request (~.grafeas.BatchCreateOccurrencesRequest):
                    The request object. Request to create occurrences in
                batch.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.grafeas.BatchCreateOccurrencesResponse:
                    Response for creating occurrences in
                batch.

            """

            http_options = _BaseGrafeasRestTransport._BaseBatchCreateOccurrences._get_http_options()
            request, metadata = self._interceptor.pre_batch_create_occurrences(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGrafeasRestTransport._BaseBatchCreateOccurrences,
                    "_BaseBatchCreateOccurrences__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for grafeas_v1.GrafeasClient.BatchCreateOccurrences",
                    extra={
                        "serviceName": "grafeas.v1.Grafeas",
                        "rpcName": "BatchCreateOccurrences",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GrafeasRestTransport._BatchCreateOccurrences._get_response(
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
            resp = grafeas.BatchCreateOccurrencesResponse()
            pb_resp = grafeas.BatchCreateOccurrencesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_create_occurrences(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_create_occurrences_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = grafeas.BatchCreateOccurrencesResponse.to_json(
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
                    "Received response for grafeas_v1.GrafeasClient.batch_create_occurrences",
                    extra={
                        "serviceName": "grafeas.v1.Grafeas",
                        "rpcName": "BatchCreateOccurrences",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateNote(_BaseGrafeasRestTransport._BaseCreateNote, GrafeasRestStub):
        def __hash__(self):
            return hash("GrafeasRestTransport.CreateNote")

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
            request: grafeas.CreateNoteRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> grafeas.Note:
            r"""Call the create note method over HTTP.

            Args:
                request (~.grafeas.CreateNoteRequest):
                    The request object. Request to create a new note.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.grafeas.Note:
                    A type of analysis that can be done
                for a resource.

            """

            http_options = _BaseGrafeasRestTransport._BaseCreateNote._get_http_options()
            request, metadata = self._interceptor.pre_create_note(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGrafeasRestTransport._BaseCreateNote,
                    "_BaseCreateNote__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for grafeas_v1.GrafeasClient.CreateNote",
                    extra={
                        "serviceName": "grafeas.v1.Grafeas",
                        "rpcName": "CreateNote",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GrafeasRestTransport._CreateNote._get_response(
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
            resp = grafeas.Note()
            pb_resp = grafeas.Note.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_note(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_note_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = grafeas.Note.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for grafeas_v1.GrafeasClient.create_note",
                    extra={
                        "serviceName": "grafeas.v1.Grafeas",
                        "rpcName": "CreateNote",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateOccurrence(
        _BaseGrafeasRestTransport._BaseCreateOccurrence, GrafeasRestStub
    ):
        def __hash__(self):
            return hash("GrafeasRestTransport.CreateOccurrence")

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
            request: grafeas.CreateOccurrenceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> grafeas.Occurrence:
            r"""Call the create occurrence method over HTTP.

            Args:
                request (~.grafeas.CreateOccurrenceRequest):
                    The request object. Request to create a new occurrence.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.grafeas.Occurrence:
                    An instance of an analysis type that
                has been found on a resource.

            """

            http_options = (
                _BaseGrafeasRestTransport._BaseCreateOccurrence._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_occurrence(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGrafeasRestTransport._BaseCreateOccurrence,
                    "_BaseCreateOccurrence__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for grafeas_v1.GrafeasClient.CreateOccurrence",
                    extra={
                        "serviceName": "grafeas.v1.Grafeas",
                        "rpcName": "CreateOccurrence",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GrafeasRestTransport._CreateOccurrence._get_response(
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
            resp = grafeas.Occurrence()
            pb_resp = grafeas.Occurrence.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_occurrence(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_occurrence_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = grafeas.Occurrence.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for grafeas_v1.GrafeasClient.create_occurrence",
                    extra={
                        "serviceName": "grafeas.v1.Grafeas",
                        "rpcName": "CreateOccurrence",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteNote(_BaseGrafeasRestTransport._BaseDeleteNote, GrafeasRestStub):
        def __hash__(self):
            return hash("GrafeasRestTransport.DeleteNote")

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
            request: grafeas.DeleteNoteRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete note method over HTTP.

            Args:
                request (~.grafeas.DeleteNoteRequest):
                    The request object. Request to delete a note.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseGrafeasRestTransport._BaseDeleteNote._get_http_options()
            request, metadata = self._interceptor.pre_delete_note(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGrafeasRestTransport._BaseDeleteNote,
                    "_BaseDeleteNote__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for grafeas_v1.GrafeasClient.DeleteNote",
                    extra={
                        "serviceName": "grafeas.v1.Grafeas",
                        "rpcName": "DeleteNote",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GrafeasRestTransport._DeleteNote._get_response(
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

    class _DeleteOccurrence(
        _BaseGrafeasRestTransport._BaseDeleteOccurrence, GrafeasRestStub
    ):
        def __hash__(self):
            return hash("GrafeasRestTransport.DeleteOccurrence")

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
            request: grafeas.DeleteOccurrenceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete occurrence method over HTTP.

            Args:
                request (~.grafeas.DeleteOccurrenceRequest):
                    The request object. Request to delete an occurrence.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseGrafeasRestTransport._BaseDeleteOccurrence._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_occurrence(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGrafeasRestTransport._BaseDeleteOccurrence,
                    "_BaseDeleteOccurrence__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for grafeas_v1.GrafeasClient.DeleteOccurrence",
                    extra={
                        "serviceName": "grafeas.v1.Grafeas",
                        "rpcName": "DeleteOccurrence",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GrafeasRestTransport._DeleteOccurrence._get_response(
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

    class _GetNote(_BaseGrafeasRestTransport._BaseGetNote, GrafeasRestStub):
        def __hash__(self):
            return hash("GrafeasRestTransport.GetNote")

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
            request: grafeas.GetNoteRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> grafeas.Note:
            r"""Call the get note method over HTTP.

            Args:
                request (~.grafeas.GetNoteRequest):
                    The request object. Request to get a note.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.grafeas.Note:
                    A type of analysis that can be done
                for a resource.

            """

            http_options = _BaseGrafeasRestTransport._BaseGetNote._get_http_options()
            request, metadata = self._interceptor.pre_get_note(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGrafeasRestTransport._BaseGetNote,
                    "_BaseGetNote__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for grafeas_v1.GrafeasClient.GetNote",
                    extra={
                        "serviceName": "grafeas.v1.Grafeas",
                        "rpcName": "GetNote",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GrafeasRestTransport._GetNote._get_response(
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
            resp = grafeas.Note()
            pb_resp = grafeas.Note.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_note(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_note_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = grafeas.Note.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for grafeas_v1.GrafeasClient.get_note",
                    extra={
                        "serviceName": "grafeas.v1.Grafeas",
                        "rpcName": "GetNote",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetOccurrence(_BaseGrafeasRestTransport._BaseGetOccurrence, GrafeasRestStub):
        def __hash__(self):
            return hash("GrafeasRestTransport.GetOccurrence")

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
            request: grafeas.GetOccurrenceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> grafeas.Occurrence:
            r"""Call the get occurrence method over HTTP.

            Args:
                request (~.grafeas.GetOccurrenceRequest):
                    The request object. Request to get an occurrence.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.grafeas.Occurrence:
                    An instance of an analysis type that
                has been found on a resource.

            """

            http_options = (
                _BaseGrafeasRestTransport._BaseGetOccurrence._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_occurrence(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGrafeasRestTransport._BaseGetOccurrence,
                    "_BaseGetOccurrence__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for grafeas_v1.GrafeasClient.GetOccurrence",
                    extra={
                        "serviceName": "grafeas.v1.Grafeas",
                        "rpcName": "GetOccurrence",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GrafeasRestTransport._GetOccurrence._get_response(
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
            resp = grafeas.Occurrence()
            pb_resp = grafeas.Occurrence.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_occurrence(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_occurrence_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = grafeas.Occurrence.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for grafeas_v1.GrafeasClient.get_occurrence",
                    extra={
                        "serviceName": "grafeas.v1.Grafeas",
                        "rpcName": "GetOccurrence",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetOccurrenceNote(
        _BaseGrafeasRestTransport._BaseGetOccurrenceNote, GrafeasRestStub
    ):
        def __hash__(self):
            return hash("GrafeasRestTransport.GetOccurrenceNote")

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
            request: grafeas.GetOccurrenceNoteRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> grafeas.Note:
            r"""Call the get occurrence note method over HTTP.

            Args:
                request (~.grafeas.GetOccurrenceNoteRequest):
                    The request object. Request to get the note to which the
                specified occurrence is attached.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.grafeas.Note:
                    A type of analysis that can be done
                for a resource.

            """

            http_options = (
                _BaseGrafeasRestTransport._BaseGetOccurrenceNote._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_occurrence_note(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGrafeasRestTransport._BaseGetOccurrenceNote,
                    "_BaseGetOccurrenceNote__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for grafeas_v1.GrafeasClient.GetOccurrenceNote",
                    extra={
                        "serviceName": "grafeas.v1.Grafeas",
                        "rpcName": "GetOccurrenceNote",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GrafeasRestTransport._GetOccurrenceNote._get_response(
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
            resp = grafeas.Note()
            pb_resp = grafeas.Note.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_occurrence_note(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_occurrence_note_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = grafeas.Note.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for grafeas_v1.GrafeasClient.get_occurrence_note",
                    extra={
                        "serviceName": "grafeas.v1.Grafeas",
                        "rpcName": "GetOccurrenceNote",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListNoteOccurrences(
        _BaseGrafeasRestTransport._BaseListNoteOccurrences, GrafeasRestStub
    ):
        def __hash__(self):
            return hash("GrafeasRestTransport.ListNoteOccurrences")

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
            request: grafeas.ListNoteOccurrencesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> grafeas.ListNoteOccurrencesResponse:
            r"""Call the list note occurrences method over HTTP.

            Args:
                request (~.grafeas.ListNoteOccurrencesRequest):
                    The request object. Request to list occurrences for a
                note.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.grafeas.ListNoteOccurrencesResponse:
                    Response for listing occurrences for
                a note.

            """

            http_options = (
                _BaseGrafeasRestTransport._BaseListNoteOccurrences._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_note_occurrences(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGrafeasRestTransport._BaseListNoteOccurrences,
                    "_BaseListNoteOccurrences__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for grafeas_v1.GrafeasClient.ListNoteOccurrences",
                    extra={
                        "serviceName": "grafeas.v1.Grafeas",
                        "rpcName": "ListNoteOccurrences",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GrafeasRestTransport._ListNoteOccurrences._get_response(
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
            resp = grafeas.ListNoteOccurrencesResponse()
            pb_resp = grafeas.ListNoteOccurrencesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_note_occurrences(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_note_occurrences_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = grafeas.ListNoteOccurrencesResponse.to_json(
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
                    "Received response for grafeas_v1.GrafeasClient.list_note_occurrences",
                    extra={
                        "serviceName": "grafeas.v1.Grafeas",
                        "rpcName": "ListNoteOccurrences",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListNotes(_BaseGrafeasRestTransport._BaseListNotes, GrafeasRestStub):
        def __hash__(self):
            return hash("GrafeasRestTransport.ListNotes")

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
            request: grafeas.ListNotesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> grafeas.ListNotesResponse:
            r"""Call the list notes method over HTTP.

            Args:
                request (~.grafeas.ListNotesRequest):
                    The request object. Request to list notes.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.grafeas.ListNotesResponse:
                    Response for listing notes.
            """

            http_options = _BaseGrafeasRestTransport._BaseListNotes._get_http_options()
            request, metadata = self._interceptor.pre_list_notes(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGrafeasRestTransport._BaseListNotes,
                    "_BaseListNotes__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for grafeas_v1.GrafeasClient.ListNotes",
                    extra={
                        "serviceName": "grafeas.v1.Grafeas",
                        "rpcName": "ListNotes",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GrafeasRestTransport._ListNotes._get_response(
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
            resp = grafeas.ListNotesResponse()
            pb_resp = grafeas.ListNotesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_notes(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_notes_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = grafeas.ListNotesResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for grafeas_v1.GrafeasClient.list_notes",
                    extra={
                        "serviceName": "grafeas.v1.Grafeas",
                        "rpcName": "ListNotes",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListOccurrences(
        _BaseGrafeasRestTransport._BaseListOccurrences, GrafeasRestStub
    ):
        def __hash__(self):
            return hash("GrafeasRestTransport.ListOccurrences")

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
            request: grafeas.ListOccurrencesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> grafeas.ListOccurrencesResponse:
            r"""Call the list occurrences method over HTTP.

            Args:
                request (~.grafeas.ListOccurrencesRequest):
                    The request object. Request to list occurrences.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.grafeas.ListOccurrencesResponse:
                    Response for listing occurrences.
            """

            http_options = (
                _BaseGrafeasRestTransport._BaseListOccurrences._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_occurrences(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGrafeasRestTransport._BaseListOccurrences,
                    "_BaseListOccurrences__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for grafeas_v1.GrafeasClient.ListOccurrences",
                    extra={
                        "serviceName": "grafeas.v1.Grafeas",
                        "rpcName": "ListOccurrences",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GrafeasRestTransport._ListOccurrences._get_response(
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
            resp = grafeas.ListOccurrencesResponse()
            pb_resp = grafeas.ListOccurrencesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_occurrences(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_occurrences_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = grafeas.ListOccurrencesResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for grafeas_v1.GrafeasClient.list_occurrences",
                    extra={
                        "serviceName": "grafeas.v1.Grafeas",
                        "rpcName": "ListOccurrences",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateNote(_BaseGrafeasRestTransport._BaseUpdateNote, GrafeasRestStub):
        def __hash__(self):
            return hash("GrafeasRestTransport.UpdateNote")

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
            request: grafeas.UpdateNoteRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> grafeas.Note:
            r"""Call the update note method over HTTP.

            Args:
                request (~.grafeas.UpdateNoteRequest):
                    The request object. Request to update a note.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.grafeas.Note:
                    A type of analysis that can be done
                for a resource.

            """

            http_options = _BaseGrafeasRestTransport._BaseUpdateNote._get_http_options()
            request, metadata = self._interceptor.pre_update_note(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGrafeasRestTransport._BaseUpdateNote,
                    "_BaseUpdateNote__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for grafeas_v1.GrafeasClient.UpdateNote",
                    extra={
                        "serviceName": "grafeas.v1.Grafeas",
                        "rpcName": "UpdateNote",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GrafeasRestTransport._UpdateNote._get_response(
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
            resp = grafeas.Note()
            pb_resp = grafeas.Note.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_note(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_note_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = grafeas.Note.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for grafeas_v1.GrafeasClient.update_note",
                    extra={
                        "serviceName": "grafeas.v1.Grafeas",
                        "rpcName": "UpdateNote",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateOccurrence(
        _BaseGrafeasRestTransport._BaseUpdateOccurrence, GrafeasRestStub
    ):
        def __hash__(self):
            return hash("GrafeasRestTransport.UpdateOccurrence")

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
            request: grafeas.UpdateOccurrenceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> grafeas.Occurrence:
            r"""Call the update occurrence method over HTTP.

            Args:
                request (~.grafeas.UpdateOccurrenceRequest):
                    The request object. Request to update an occurrence.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.grafeas.Occurrence:
                    An instance of an analysis type that
                has been found on a resource.

            """

            http_options = (
                _BaseGrafeasRestTransport._BaseUpdateOccurrence._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_occurrence(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseGrafeasRestTransport._BaseUpdateOccurrence,
                    "_BaseUpdateOccurrence__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for grafeas_v1.GrafeasClient.UpdateOccurrence",
                    extra={
                        "serviceName": "grafeas.v1.Grafeas",
                        "rpcName": "UpdateOccurrence",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = GrafeasRestTransport._UpdateOccurrence._get_response(
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
            resp = grafeas.Occurrence()
            pb_resp = grafeas.Occurrence.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_occurrence(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_occurrence_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = grafeas.Occurrence.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for grafeas_v1.GrafeasClient.update_occurrence",
                    extra={
                        "serviceName": "grafeas.v1.Grafeas",
                        "rpcName": "UpdateOccurrence",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def batch_create_notes(
        self,
    ) -> Callable[[grafeas.BatchCreateNotesRequest], grafeas.BatchCreateNotesResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchCreateNotes(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def batch_create_occurrences(
        self,
    ) -> Callable[
        [grafeas.BatchCreateOccurrencesRequest], grafeas.BatchCreateOccurrencesResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchCreateOccurrences(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_note(self) -> Callable[[grafeas.CreateNoteRequest], grafeas.Note]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateNote(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_occurrence(
        self,
    ) -> Callable[[grafeas.CreateOccurrenceRequest], grafeas.Occurrence]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateOccurrence(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_note(self) -> Callable[[grafeas.DeleteNoteRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteNote(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_occurrence(
        self,
    ) -> Callable[[grafeas.DeleteOccurrenceRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteOccurrence(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_note(self) -> Callable[[grafeas.GetNoteRequest], grafeas.Note]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetNote(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_occurrence(
        self,
    ) -> Callable[[grafeas.GetOccurrenceRequest], grafeas.Occurrence]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetOccurrence(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_occurrence_note(
        self,
    ) -> Callable[[grafeas.GetOccurrenceNoteRequest], grafeas.Note]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetOccurrenceNote(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_note_occurrences(
        self,
    ) -> Callable[
        [grafeas.ListNoteOccurrencesRequest], grafeas.ListNoteOccurrencesResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListNoteOccurrences(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_notes(
        self,
    ) -> Callable[[grafeas.ListNotesRequest], grafeas.ListNotesResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListNotes(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_occurrences(
        self,
    ) -> Callable[[grafeas.ListOccurrencesRequest], grafeas.ListOccurrencesResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListOccurrences(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_note(self) -> Callable[[grafeas.UpdateNoteRequest], grafeas.Note]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateNote(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_occurrence(
        self,
    ) -> Callable[[grafeas.UpdateOccurrenceRequest], grafeas.Occurrence]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateOccurrence(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("GrafeasRestTransport",)
