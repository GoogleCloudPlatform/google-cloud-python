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
from google.api_core import gapic_v1, rest_helpers, rest_streaming
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.requests import AuthorizedSession  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.dialogflow_v2beta1._compat import transcode_request
from google.cloud.dialogflow_v2beta1.types import participant
from google.cloud.dialogflow_v2beta1.types import participant as gcd_participant

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseParticipantsRestTransport

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


class ParticipantsRestInterceptor:
    """Interceptor for Participants.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the ParticipantsRestTransport.

    .. code-block:: python
        class MyCustomParticipantsInterceptor(ParticipantsRestInterceptor):
            def pre_analyze_content(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_analyze_content(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_compile_suggestion(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_compile_suggestion(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_participant(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_participant(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_participant(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_participant(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_participants(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_participants(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_suggestions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_suggestions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_suggest_articles(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_suggest_articles(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_suggest_faq_answers(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_suggest_faq_answers(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_suggest_knowledge_assist(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_suggest_knowledge_assist(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_suggest_smart_replies(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_suggest_smart_replies(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_participant(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_participant(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = ParticipantsRestTransport(interceptor=MyCustomParticipantsInterceptor())
        client = ParticipantsClient(transport=transport)


    """

    def pre_analyze_content(
        self,
        request: gcd_participant.AnalyzeContentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcd_participant.AnalyzeContentRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for analyze_content

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Participants server.
        """
        return request, metadata

    def post_analyze_content(
        self, response: gcd_participant.AnalyzeContentResponse
    ) -> gcd_participant.AnalyzeContentResponse:
        """Post-rpc interceptor for analyze_content

        DEPRECATED. Please use the `post_analyze_content_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Participants server but before
        it is returned to user code. This `post_analyze_content` interceptor runs
        before the `post_analyze_content_with_metadata` interceptor.
        """
        return response

    def post_analyze_content_with_metadata(
        self,
        response: gcd_participant.AnalyzeContentResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcd_participant.AnalyzeContentResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for analyze_content

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Participants server but before it is returned to user code.

        We recommend only using this `post_analyze_content_with_metadata`
        interceptor in new development instead of the `post_analyze_content` interceptor.
        When both interceptors are used, this `post_analyze_content_with_metadata` interceptor runs after the
        `post_analyze_content` interceptor. The (possibly modified) response returned by
        `post_analyze_content` will be passed to
        `post_analyze_content_with_metadata`.
        """
        return response, metadata

    def pre_compile_suggestion(
        self,
        request: participant.CompileSuggestionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        participant.CompileSuggestionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for compile_suggestion

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Participants server.
        """
        return request, metadata

    def post_compile_suggestion(
        self, response: participant.CompileSuggestionResponse
    ) -> participant.CompileSuggestionResponse:
        """Post-rpc interceptor for compile_suggestion

        DEPRECATED. Please use the `post_compile_suggestion_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Participants server but before
        it is returned to user code. This `post_compile_suggestion` interceptor runs
        before the `post_compile_suggestion_with_metadata` interceptor.
        """
        return response

    def post_compile_suggestion_with_metadata(
        self,
        response: participant.CompileSuggestionResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        participant.CompileSuggestionResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for compile_suggestion

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Participants server but before it is returned to user code.

        We recommend only using this `post_compile_suggestion_with_metadata`
        interceptor in new development instead of the `post_compile_suggestion` interceptor.
        When both interceptors are used, this `post_compile_suggestion_with_metadata` interceptor runs after the
        `post_compile_suggestion` interceptor. The (possibly modified) response returned by
        `post_compile_suggestion` will be passed to
        `post_compile_suggestion_with_metadata`.
        """
        return response, metadata

    def pre_create_participant(
        self,
        request: gcd_participant.CreateParticipantRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcd_participant.CreateParticipantRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_participant

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Participants server.
        """
        return request, metadata

    def post_create_participant(
        self, response: gcd_participant.Participant
    ) -> gcd_participant.Participant:
        """Post-rpc interceptor for create_participant

        DEPRECATED. Please use the `post_create_participant_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Participants server but before
        it is returned to user code. This `post_create_participant` interceptor runs
        before the `post_create_participant_with_metadata` interceptor.
        """
        return response

    def post_create_participant_with_metadata(
        self,
        response: gcd_participant.Participant,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gcd_participant.Participant, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_participant

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Participants server but before it is returned to user code.

        We recommend only using this `post_create_participant_with_metadata`
        interceptor in new development instead of the `post_create_participant` interceptor.
        When both interceptors are used, this `post_create_participant_with_metadata` interceptor runs after the
        `post_create_participant` interceptor. The (possibly modified) response returned by
        `post_create_participant` will be passed to
        `post_create_participant_with_metadata`.
        """
        return response, metadata

    def pre_get_participant(
        self,
        request: participant.GetParticipantRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        participant.GetParticipantRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_participant

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Participants server.
        """
        return request, metadata

    def post_get_participant(
        self, response: participant.Participant
    ) -> participant.Participant:
        """Post-rpc interceptor for get_participant

        DEPRECATED. Please use the `post_get_participant_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Participants server but before
        it is returned to user code. This `post_get_participant` interceptor runs
        before the `post_get_participant_with_metadata` interceptor.
        """
        return response

    def post_get_participant_with_metadata(
        self,
        response: participant.Participant,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[participant.Participant, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_participant

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Participants server but before it is returned to user code.

        We recommend only using this `post_get_participant_with_metadata`
        interceptor in new development instead of the `post_get_participant` interceptor.
        When both interceptors are used, this `post_get_participant_with_metadata` interceptor runs after the
        `post_get_participant` interceptor. The (possibly modified) response returned by
        `post_get_participant` will be passed to
        `post_get_participant_with_metadata`.
        """
        return response, metadata

    def pre_list_participants(
        self,
        request: participant.ListParticipantsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        participant.ListParticipantsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_participants

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Participants server.
        """
        return request, metadata

    def post_list_participants(
        self, response: participant.ListParticipantsResponse
    ) -> participant.ListParticipantsResponse:
        """Post-rpc interceptor for list_participants

        DEPRECATED. Please use the `post_list_participants_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Participants server but before
        it is returned to user code. This `post_list_participants` interceptor runs
        before the `post_list_participants_with_metadata` interceptor.
        """
        return response

    def post_list_participants_with_metadata(
        self,
        response: participant.ListParticipantsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        participant.ListParticipantsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_participants

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Participants server but before it is returned to user code.

        We recommend only using this `post_list_participants_with_metadata`
        interceptor in new development instead of the `post_list_participants` interceptor.
        When both interceptors are used, this `post_list_participants_with_metadata` interceptor runs after the
        `post_list_participants` interceptor. The (possibly modified) response returned by
        `post_list_participants` will be passed to
        `post_list_participants_with_metadata`.
        """
        return response, metadata

    def pre_list_suggestions(
        self,
        request: participant.ListSuggestionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        participant.ListSuggestionsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_suggestions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Participants server.
        """
        return request, metadata

    def post_list_suggestions(
        self, response: participant.ListSuggestionsResponse
    ) -> participant.ListSuggestionsResponse:
        """Post-rpc interceptor for list_suggestions

        DEPRECATED. Please use the `post_list_suggestions_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Participants server but before
        it is returned to user code. This `post_list_suggestions` interceptor runs
        before the `post_list_suggestions_with_metadata` interceptor.
        """
        return response

    def post_list_suggestions_with_metadata(
        self,
        response: participant.ListSuggestionsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        participant.ListSuggestionsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_suggestions

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Participants server but before it is returned to user code.

        We recommend only using this `post_list_suggestions_with_metadata`
        interceptor in new development instead of the `post_list_suggestions` interceptor.
        When both interceptors are used, this `post_list_suggestions_with_metadata` interceptor runs after the
        `post_list_suggestions` interceptor. The (possibly modified) response returned by
        `post_list_suggestions` will be passed to
        `post_list_suggestions_with_metadata`.
        """
        return response, metadata

    def pre_suggest_articles(
        self,
        request: participant.SuggestArticlesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        participant.SuggestArticlesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for suggest_articles

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Participants server.
        """
        return request, metadata

    def post_suggest_articles(
        self, response: participant.SuggestArticlesResponse
    ) -> participant.SuggestArticlesResponse:
        """Post-rpc interceptor for suggest_articles

        DEPRECATED. Please use the `post_suggest_articles_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Participants server but before
        it is returned to user code. This `post_suggest_articles` interceptor runs
        before the `post_suggest_articles_with_metadata` interceptor.
        """
        return response

    def post_suggest_articles_with_metadata(
        self,
        response: participant.SuggestArticlesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        participant.SuggestArticlesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for suggest_articles

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Participants server but before it is returned to user code.

        We recommend only using this `post_suggest_articles_with_metadata`
        interceptor in new development instead of the `post_suggest_articles` interceptor.
        When both interceptors are used, this `post_suggest_articles_with_metadata` interceptor runs after the
        `post_suggest_articles` interceptor. The (possibly modified) response returned by
        `post_suggest_articles` will be passed to
        `post_suggest_articles_with_metadata`.
        """
        return response, metadata

    def pre_suggest_faq_answers(
        self,
        request: participant.SuggestFaqAnswersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        participant.SuggestFaqAnswersRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for suggest_faq_answers

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Participants server.
        """
        return request, metadata

    def post_suggest_faq_answers(
        self, response: participant.SuggestFaqAnswersResponse
    ) -> participant.SuggestFaqAnswersResponse:
        """Post-rpc interceptor for suggest_faq_answers

        DEPRECATED. Please use the `post_suggest_faq_answers_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Participants server but before
        it is returned to user code. This `post_suggest_faq_answers` interceptor runs
        before the `post_suggest_faq_answers_with_metadata` interceptor.
        """
        return response

    def post_suggest_faq_answers_with_metadata(
        self,
        response: participant.SuggestFaqAnswersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        participant.SuggestFaqAnswersResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for suggest_faq_answers

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Participants server but before it is returned to user code.

        We recommend only using this `post_suggest_faq_answers_with_metadata`
        interceptor in new development instead of the `post_suggest_faq_answers` interceptor.
        When both interceptors are used, this `post_suggest_faq_answers_with_metadata` interceptor runs after the
        `post_suggest_faq_answers` interceptor. The (possibly modified) response returned by
        `post_suggest_faq_answers` will be passed to
        `post_suggest_faq_answers_with_metadata`.
        """
        return response, metadata

    def pre_suggest_knowledge_assist(
        self,
        request: participant.SuggestKnowledgeAssistRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        participant.SuggestKnowledgeAssistRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for suggest_knowledge_assist

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Participants server.
        """
        return request, metadata

    def post_suggest_knowledge_assist(
        self, response: participant.SuggestKnowledgeAssistResponse
    ) -> participant.SuggestKnowledgeAssistResponse:
        """Post-rpc interceptor for suggest_knowledge_assist

        DEPRECATED. Please use the `post_suggest_knowledge_assist_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Participants server but before
        it is returned to user code. This `post_suggest_knowledge_assist` interceptor runs
        before the `post_suggest_knowledge_assist_with_metadata` interceptor.
        """
        return response

    def post_suggest_knowledge_assist_with_metadata(
        self,
        response: participant.SuggestKnowledgeAssistResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        participant.SuggestKnowledgeAssistResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for suggest_knowledge_assist

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Participants server but before it is returned to user code.

        We recommend only using this `post_suggest_knowledge_assist_with_metadata`
        interceptor in new development instead of the `post_suggest_knowledge_assist` interceptor.
        When both interceptors are used, this `post_suggest_knowledge_assist_with_metadata` interceptor runs after the
        `post_suggest_knowledge_assist` interceptor. The (possibly modified) response returned by
        `post_suggest_knowledge_assist` will be passed to
        `post_suggest_knowledge_assist_with_metadata`.
        """
        return response, metadata

    def pre_suggest_smart_replies(
        self,
        request: participant.SuggestSmartRepliesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        participant.SuggestSmartRepliesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for suggest_smart_replies

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Participants server.
        """
        return request, metadata

    def post_suggest_smart_replies(
        self, response: participant.SuggestSmartRepliesResponse
    ) -> participant.SuggestSmartRepliesResponse:
        """Post-rpc interceptor for suggest_smart_replies

        DEPRECATED. Please use the `post_suggest_smart_replies_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Participants server but before
        it is returned to user code. This `post_suggest_smart_replies` interceptor runs
        before the `post_suggest_smart_replies_with_metadata` interceptor.
        """
        return response

    def post_suggest_smart_replies_with_metadata(
        self,
        response: participant.SuggestSmartRepliesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        participant.SuggestSmartRepliesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for suggest_smart_replies

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Participants server but before it is returned to user code.

        We recommend only using this `post_suggest_smart_replies_with_metadata`
        interceptor in new development instead of the `post_suggest_smart_replies` interceptor.
        When both interceptors are used, this `post_suggest_smart_replies_with_metadata` interceptor runs after the
        `post_suggest_smart_replies` interceptor. The (possibly modified) response returned by
        `post_suggest_smart_replies` will be passed to
        `post_suggest_smart_replies_with_metadata`.
        """
        return response, metadata

    def pre_update_participant(
        self,
        request: gcd_participant.UpdateParticipantRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcd_participant.UpdateParticipantRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_participant

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Participants server.
        """
        return request, metadata

    def post_update_participant(
        self, response: gcd_participant.Participant
    ) -> gcd_participant.Participant:
        """Post-rpc interceptor for update_participant

        DEPRECATED. Please use the `post_update_participant_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Participants server but before
        it is returned to user code. This `post_update_participant` interceptor runs
        before the `post_update_participant_with_metadata` interceptor.
        """
        return response

    def post_update_participant_with_metadata(
        self,
        response: gcd_participant.Participant,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gcd_participant.Participant, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_participant

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Participants server but before it is returned to user code.

        We recommend only using this `post_update_participant_with_metadata`
        interceptor in new development instead of the `post_update_participant` interceptor.
        When both interceptors are used, this `post_update_participant_with_metadata` interceptor runs after the
        `post_update_participant` interceptor. The (possibly modified) response returned by
        `post_update_participant` will be passed to
        `post_update_participant_with_metadata`.
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
        before they are sent to the Participants server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the Participants server but before
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
        before they are sent to the Participants server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the Participants server but before
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
        before they are sent to the Participants server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the Participants server but before
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
        before they are sent to the Participants server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the Participants server but before
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
        before they are sent to the Participants server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the Participants server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class ParticipantsRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: ParticipantsRestInterceptor


class ParticipantsRestTransport(_BaseParticipantsRestTransport):
    """REST backend synchronous transport for Participants.

    Service for managing
    [Participants][google.cloud.dialogflow.v2beta1.Participant].

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "dialogflow.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[ParticipantsRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'dialogflow.googleapis.com').
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
            interceptor (Optional[ParticipantsRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or ParticipantsRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _AnalyzeContent(
        _BaseParticipantsRestTransport._BaseAnalyzeContent, ParticipantsRestStub
    ):
        def __hash__(self):
            return hash("ParticipantsRestTransport.AnalyzeContent")

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
            request: gcd_participant.AnalyzeContentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcd_participant.AnalyzeContentResponse:
            r"""Call the analyze content method over HTTP.

            Args:
                request (~.gcd_participant.AnalyzeContentRequest):
                    The request object. The request message for
                [Participants.AnalyzeContent][google.cloud.dialogflow.v2beta1.Participants.AnalyzeContent].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcd_participant.AnalyzeContentResponse:
                    The response message for
                [Participants.AnalyzeContent][google.cloud.dialogflow.v2beta1.Participants.AnalyzeContent].

            """

            http_options = (
                _BaseParticipantsRestTransport._BaseAnalyzeContent._get_http_options()
            )
            request, metadata = self._interceptor.pre_analyze_content(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseParticipantsRestTransport._BaseAnalyzeContent,
                    "_BaseAnalyzeContent__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow_v2beta1.ParticipantsClient.AnalyzeContent",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Participants",
                        "rpcName": "AnalyzeContent",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ParticipantsRestTransport._AnalyzeContent._get_response(
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
            resp = gcd_participant.AnalyzeContentResponse()
            pb_resp = gcd_participant.AnalyzeContentResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_analyze_content(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_analyze_content_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcd_participant.AnalyzeContentResponse.to_json(
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
                    "Received response for google.cloud.dialogflow_v2beta1.ParticipantsClient.analyze_content",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Participants",
                        "rpcName": "AnalyzeContent",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BidiStreamingAnalyzeContent(
        _BaseParticipantsRestTransport._BaseBidiStreamingAnalyzeContent,
        ParticipantsRestStub,
    ):
        def __hash__(self):
            return hash("ParticipantsRestTransport.BidiStreamingAnalyzeContent")

        def __call__(
            self,
            request: participant.BidiStreamingAnalyzeContentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> rest_streaming.ResponseIterator:
            raise NotImplementedError(
                "Method BidiStreamingAnalyzeContent is not available over REST transport"
            )

    class _CompileSuggestion(
        _BaseParticipantsRestTransport._BaseCompileSuggestion, ParticipantsRestStub
    ):
        def __hash__(self):
            return hash("ParticipantsRestTransport.CompileSuggestion")

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
            request: participant.CompileSuggestionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> participant.CompileSuggestionResponse:
            r"""Call the compile suggestion method over HTTP.

            Args:
                request (~.participant.CompileSuggestionRequest):
                    The request object. The request message for
                [Participants.CompileSuggestion][google.cloud.dialogflow.v2beta1.Participants.CompileSuggestion].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.participant.CompileSuggestionResponse:
                    The response message for
                [Participants.CompileSuggestion][google.cloud.dialogflow.v2beta1.Participants.CompileSuggestion].

            """

            http_options = _BaseParticipantsRestTransport._BaseCompileSuggestion._get_http_options()
            request, metadata = self._interceptor.pre_compile_suggestion(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseParticipantsRestTransport._BaseCompileSuggestion,
                    "_BaseCompileSuggestion__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow_v2beta1.ParticipantsClient.CompileSuggestion",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Participants",
                        "rpcName": "CompileSuggestion",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ParticipantsRestTransport._CompileSuggestion._get_response(
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
            resp = participant.CompileSuggestionResponse()
            pb_resp = participant.CompileSuggestionResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_compile_suggestion(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_compile_suggestion_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = participant.CompileSuggestionResponse.to_json(
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
                    "Received response for google.cloud.dialogflow_v2beta1.ParticipantsClient.compile_suggestion",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Participants",
                        "rpcName": "CompileSuggestion",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateParticipant(
        _BaseParticipantsRestTransport._BaseCreateParticipant, ParticipantsRestStub
    ):
        def __hash__(self):
            return hash("ParticipantsRestTransport.CreateParticipant")

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
            request: gcd_participant.CreateParticipantRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcd_participant.Participant:
            r"""Call the create participant method over HTTP.

            Args:
                request (~.gcd_participant.CreateParticipantRequest):
                    The request object. The request message for
                [Participants.CreateParticipant][google.cloud.dialogflow.v2beta1.Participants.CreateParticipant].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcd_participant.Participant:
                    Represents a conversation participant
                (human agent, virtual agent, end-user).

            """

            http_options = _BaseParticipantsRestTransport._BaseCreateParticipant._get_http_options()
            request, metadata = self._interceptor.pre_create_participant(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseParticipantsRestTransport._BaseCreateParticipant,
                    "_BaseCreateParticipant__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow_v2beta1.ParticipantsClient.CreateParticipant",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Participants",
                        "rpcName": "CreateParticipant",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ParticipantsRestTransport._CreateParticipant._get_response(
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
            resp = gcd_participant.Participant()
            pb_resp = gcd_participant.Participant.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_participant(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_participant_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcd_participant.Participant.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dialogflow_v2beta1.ParticipantsClient.create_participant",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Participants",
                        "rpcName": "CreateParticipant",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetParticipant(
        _BaseParticipantsRestTransport._BaseGetParticipant, ParticipantsRestStub
    ):
        def __hash__(self):
            return hash("ParticipantsRestTransport.GetParticipant")

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
            request: participant.GetParticipantRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> participant.Participant:
            r"""Call the get participant method over HTTP.

            Args:
                request (~.participant.GetParticipantRequest):
                    The request object. The request message for
                [Participants.GetParticipant][google.cloud.dialogflow.v2beta1.Participants.GetParticipant].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.participant.Participant:
                    Represents a conversation participant
                (human agent, virtual agent, end-user).

            """

            http_options = (
                _BaseParticipantsRestTransport._BaseGetParticipant._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_participant(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseParticipantsRestTransport._BaseGetParticipant,
                    "_BaseGetParticipant__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow_v2beta1.ParticipantsClient.GetParticipant",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Participants",
                        "rpcName": "GetParticipant",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ParticipantsRestTransport._GetParticipant._get_response(
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
            resp = participant.Participant()
            pb_resp = participant.Participant.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_participant(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_participant_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = participant.Participant.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dialogflow_v2beta1.ParticipantsClient.get_participant",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Participants",
                        "rpcName": "GetParticipant",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListParticipants(
        _BaseParticipantsRestTransport._BaseListParticipants, ParticipantsRestStub
    ):
        def __hash__(self):
            return hash("ParticipantsRestTransport.ListParticipants")

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
            request: participant.ListParticipantsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> participant.ListParticipantsResponse:
            r"""Call the list participants method over HTTP.

            Args:
                request (~.participant.ListParticipantsRequest):
                    The request object. The request message for
                [Participants.ListParticipants][google.cloud.dialogflow.v2beta1.Participants.ListParticipants].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.participant.ListParticipantsResponse:
                    The response message for
                [Participants.ListParticipants][google.cloud.dialogflow.v2beta1.Participants.ListParticipants].

            """

            http_options = (
                _BaseParticipantsRestTransport._BaseListParticipants._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_participants(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseParticipantsRestTransport._BaseListParticipants,
                    "_BaseListParticipants__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow_v2beta1.ParticipantsClient.ListParticipants",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Participants",
                        "rpcName": "ListParticipants",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ParticipantsRestTransport._ListParticipants._get_response(
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
            resp = participant.ListParticipantsResponse()
            pb_resp = participant.ListParticipantsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_participants(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_participants_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = participant.ListParticipantsResponse.to_json(
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
                    "Received response for google.cloud.dialogflow_v2beta1.ParticipantsClient.list_participants",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Participants",
                        "rpcName": "ListParticipants",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListSuggestions(
        _BaseParticipantsRestTransport._BaseListSuggestions, ParticipantsRestStub
    ):
        def __hash__(self):
            return hash("ParticipantsRestTransport.ListSuggestions")

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
            request: participant.ListSuggestionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> participant.ListSuggestionsResponse:
            r"""Call the list suggestions method over HTTP.

            Args:
                request (~.participant.ListSuggestionsRequest):
                    The request object. The request message for
                [Participants.ListSuggestions][google.cloud.dialogflow.v2beta1.Participants.ListSuggestions].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.participant.ListSuggestionsResponse:
                    The response message for
                [Participants.ListSuggestions][google.cloud.dialogflow.v2beta1.Participants.ListSuggestions].

            """

            http_options = (
                _BaseParticipantsRestTransport._BaseListSuggestions._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_suggestions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseParticipantsRestTransport._BaseListSuggestions,
                    "_BaseListSuggestions__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow_v2beta1.ParticipantsClient.ListSuggestions",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Participants",
                        "rpcName": "ListSuggestions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ParticipantsRestTransport._ListSuggestions._get_response(
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
            resp = participant.ListSuggestionsResponse()
            pb_resp = participant.ListSuggestionsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_suggestions(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_suggestions_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = participant.ListSuggestionsResponse.to_json(
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
                    "Received response for google.cloud.dialogflow_v2beta1.ParticipantsClient.list_suggestions",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Participants",
                        "rpcName": "ListSuggestions",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _StreamingAnalyzeContent(
        _BaseParticipantsRestTransport._BaseStreamingAnalyzeContent,
        ParticipantsRestStub,
    ):
        def __hash__(self):
            return hash("ParticipantsRestTransport.StreamingAnalyzeContent")

        def __call__(
            self,
            request: participant.StreamingAnalyzeContentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> rest_streaming.ResponseIterator:
            raise NotImplementedError(
                "Method StreamingAnalyzeContent is not available over REST transport"
            )

    class _StreamingReactiveCompanionSuggestions(
        _BaseParticipantsRestTransport._BaseStreamingReactiveCompanionSuggestions,
        ParticipantsRestStub,
    ):
        def __hash__(self):
            return hash(
                "ParticipantsRestTransport.StreamingReactiveCompanionSuggestions"
            )

        def __call__(
            self,
            request: participant.StreamingReactiveCompanionSuggestionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> rest_streaming.ResponseIterator:
            raise NotImplementedError(
                "Method StreamingReactiveCompanionSuggestions is not available over REST transport"
            )

    class _SuggestArticles(
        _BaseParticipantsRestTransport._BaseSuggestArticles, ParticipantsRestStub
    ):
        def __hash__(self):
            return hash("ParticipantsRestTransport.SuggestArticles")

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
            request: participant.SuggestArticlesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> participant.SuggestArticlesResponse:
            r"""Call the suggest articles method over HTTP.

            Args:
                request (~.participant.SuggestArticlesRequest):
                    The request object. The request message for
                [Participants.SuggestArticles][google.cloud.dialogflow.v2beta1.Participants.SuggestArticles].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.participant.SuggestArticlesResponse:
                    The response message for
                [Participants.SuggestArticles][google.cloud.dialogflow.v2beta1.Participants.SuggestArticles].

            """

            http_options = (
                _BaseParticipantsRestTransport._BaseSuggestArticles._get_http_options()
            )
            request, metadata = self._interceptor.pre_suggest_articles(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseParticipantsRestTransport._BaseSuggestArticles,
                    "_BaseSuggestArticles__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow_v2beta1.ParticipantsClient.SuggestArticles",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Participants",
                        "rpcName": "SuggestArticles",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ParticipantsRestTransport._SuggestArticles._get_response(
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
            resp = participant.SuggestArticlesResponse()
            pb_resp = participant.SuggestArticlesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_suggest_articles(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_suggest_articles_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = participant.SuggestArticlesResponse.to_json(
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
                    "Received response for google.cloud.dialogflow_v2beta1.ParticipantsClient.suggest_articles",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Participants",
                        "rpcName": "SuggestArticles",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SuggestFaqAnswers(
        _BaseParticipantsRestTransport._BaseSuggestFaqAnswers, ParticipantsRestStub
    ):
        def __hash__(self):
            return hash("ParticipantsRestTransport.SuggestFaqAnswers")

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
            request: participant.SuggestFaqAnswersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> participant.SuggestFaqAnswersResponse:
            r"""Call the suggest faq answers method over HTTP.

            Args:
                request (~.participant.SuggestFaqAnswersRequest):
                    The request object. The request message for
                [Participants.SuggestFaqAnswers][google.cloud.dialogflow.v2beta1.Participants.SuggestFaqAnswers].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.participant.SuggestFaqAnswersResponse:
                    The request message for
                [Participants.SuggestFaqAnswers][google.cloud.dialogflow.v2beta1.Participants.SuggestFaqAnswers].

            """

            http_options = _BaseParticipantsRestTransport._BaseSuggestFaqAnswers._get_http_options()
            request, metadata = self._interceptor.pre_suggest_faq_answers(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseParticipantsRestTransport._BaseSuggestFaqAnswers,
                    "_BaseSuggestFaqAnswers__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow_v2beta1.ParticipantsClient.SuggestFaqAnswers",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Participants",
                        "rpcName": "SuggestFaqAnswers",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ParticipantsRestTransport._SuggestFaqAnswers._get_response(
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
            resp = participant.SuggestFaqAnswersResponse()
            pb_resp = participant.SuggestFaqAnswersResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_suggest_faq_answers(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_suggest_faq_answers_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = participant.SuggestFaqAnswersResponse.to_json(
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
                    "Received response for google.cloud.dialogflow_v2beta1.ParticipantsClient.suggest_faq_answers",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Participants",
                        "rpcName": "SuggestFaqAnswers",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SuggestKnowledgeAssist(
        _BaseParticipantsRestTransport._BaseSuggestKnowledgeAssist, ParticipantsRestStub
    ):
        def __hash__(self):
            return hash("ParticipantsRestTransport.SuggestKnowledgeAssist")

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
            request: participant.SuggestKnowledgeAssistRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> participant.SuggestKnowledgeAssistResponse:
            r"""Call the suggest knowledge assist method over HTTP.

            Args:
                request (~.participant.SuggestKnowledgeAssistRequest):
                    The request object. The request message for
                [Participants.SuggestKnowledgeAssist][google.cloud.dialogflow.v2beta1.Participants.SuggestKnowledgeAssist].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.participant.SuggestKnowledgeAssistResponse:
                    The response message for
                [Participants.SuggestKnowledgeAssist][google.cloud.dialogflow.v2beta1.Participants.SuggestKnowledgeAssist].

            """

            http_options = _BaseParticipantsRestTransport._BaseSuggestKnowledgeAssist._get_http_options()
            request, metadata = self._interceptor.pre_suggest_knowledge_assist(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseParticipantsRestTransport._BaseSuggestKnowledgeAssist,
                    "_BaseSuggestKnowledgeAssist__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow_v2beta1.ParticipantsClient.SuggestKnowledgeAssist",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Participants",
                        "rpcName": "SuggestKnowledgeAssist",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ParticipantsRestTransport._SuggestKnowledgeAssist._get_response(
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
            resp = participant.SuggestKnowledgeAssistResponse()
            pb_resp = participant.SuggestKnowledgeAssistResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_suggest_knowledge_assist(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_suggest_knowledge_assist_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        participant.SuggestKnowledgeAssistResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dialogflow_v2beta1.ParticipantsClient.suggest_knowledge_assist",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Participants",
                        "rpcName": "SuggestKnowledgeAssist",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SuggestSmartReplies(
        _BaseParticipantsRestTransport._BaseSuggestSmartReplies, ParticipantsRestStub
    ):
        def __hash__(self):
            return hash("ParticipantsRestTransport.SuggestSmartReplies")

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
            request: participant.SuggestSmartRepliesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> participant.SuggestSmartRepliesResponse:
            r"""Call the suggest smart replies method over HTTP.

            Args:
                request (~.participant.SuggestSmartRepliesRequest):
                    The request object. The request message for
                [Participants.SuggestSmartReplies][google.cloud.dialogflow.v2beta1.Participants.SuggestSmartReplies].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.participant.SuggestSmartRepliesResponse:
                    The response message for
                [Participants.SuggestSmartReplies][google.cloud.dialogflow.v2beta1.Participants.SuggestSmartReplies].

            """

            http_options = _BaseParticipantsRestTransport._BaseSuggestSmartReplies._get_http_options()
            request, metadata = self._interceptor.pre_suggest_smart_replies(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseParticipantsRestTransport._BaseSuggestSmartReplies,
                    "_BaseSuggestSmartReplies__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow_v2beta1.ParticipantsClient.SuggestSmartReplies",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Participants",
                        "rpcName": "SuggestSmartReplies",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ParticipantsRestTransport._SuggestSmartReplies._get_response(
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
            resp = participant.SuggestSmartRepliesResponse()
            pb_resp = participant.SuggestSmartRepliesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_suggest_smart_replies(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_suggest_smart_replies_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = participant.SuggestSmartRepliesResponse.to_json(
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
                    "Received response for google.cloud.dialogflow_v2beta1.ParticipantsClient.suggest_smart_replies",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Participants",
                        "rpcName": "SuggestSmartReplies",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateParticipant(
        _BaseParticipantsRestTransport._BaseUpdateParticipant, ParticipantsRestStub
    ):
        def __hash__(self):
            return hash("ParticipantsRestTransport.UpdateParticipant")

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
            request: gcd_participant.UpdateParticipantRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcd_participant.Participant:
            r"""Call the update participant method over HTTP.

            Args:
                request (~.gcd_participant.UpdateParticipantRequest):
                    The request object. The request message for
                [Participants.UpdateParticipant][google.cloud.dialogflow.v2beta1.Participants.UpdateParticipant].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcd_participant.Participant:
                    Represents a conversation participant
                (human agent, virtual agent, end-user).

            """

            http_options = _BaseParticipantsRestTransport._BaseUpdateParticipant._get_http_options()
            request, metadata = self._interceptor.pre_update_participant(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseParticipantsRestTransport._BaseUpdateParticipant,
                    "_BaseUpdateParticipant__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow_v2beta1.ParticipantsClient.UpdateParticipant",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Participants",
                        "rpcName": "UpdateParticipant",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ParticipantsRestTransport._UpdateParticipant._get_response(
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
            resp = gcd_participant.Participant()
            pb_resp = gcd_participant.Participant.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_participant(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_participant_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcd_participant.Participant.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dialogflow_v2beta1.ParticipantsClient.update_participant",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Participants",
                        "rpcName": "UpdateParticipant",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def analyze_content(
        self,
    ) -> Callable[
        [gcd_participant.AnalyzeContentRequest], gcd_participant.AnalyzeContentResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._AnalyzeContent(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def bidi_streaming_analyze_content(
        self,
    ) -> Callable[
        [participant.BidiStreamingAnalyzeContentRequest],
        participant.BidiStreamingAnalyzeContentResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BidiStreamingAnalyzeContent(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def compile_suggestion(
        self,
    ) -> Callable[
        [participant.CompileSuggestionRequest], participant.CompileSuggestionResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CompileSuggestion(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_participant(
        self,
    ) -> Callable[
        [gcd_participant.CreateParticipantRequest], gcd_participant.Participant
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateParticipant(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_participant(
        self,
    ) -> Callable[[participant.GetParticipantRequest], participant.Participant]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetParticipant(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_participants(
        self,
    ) -> Callable[
        [participant.ListParticipantsRequest], participant.ListParticipantsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListParticipants(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_suggestions(
        self,
    ) -> Callable[
        [participant.ListSuggestionsRequest], participant.ListSuggestionsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListSuggestions(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def streaming_analyze_content(
        self,
    ) -> Callable[
        [participant.StreamingAnalyzeContentRequest],
        participant.StreamingAnalyzeContentResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._StreamingAnalyzeContent(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def streaming_reactive_companion_suggestions(
        self,
    ) -> Callable[
        [participant.StreamingReactiveCompanionSuggestionsRequest],
        participant.StreamingReactiveCompanionSuggestionsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._StreamingReactiveCompanionSuggestions(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def suggest_articles(
        self,
    ) -> Callable[
        [participant.SuggestArticlesRequest], participant.SuggestArticlesResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SuggestArticles(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def suggest_faq_answers(
        self,
    ) -> Callable[
        [participant.SuggestFaqAnswersRequest], participant.SuggestFaqAnswersResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SuggestFaqAnswers(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def suggest_knowledge_assist(
        self,
    ) -> Callable[
        [participant.SuggestKnowledgeAssistRequest],
        participant.SuggestKnowledgeAssistResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SuggestKnowledgeAssist(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def suggest_smart_replies(
        self,
    ) -> Callable[
        [participant.SuggestSmartRepliesRequest],
        participant.SuggestSmartRepliesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SuggestSmartReplies(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_participant(
        self,
    ) -> Callable[
        [gcd_participant.UpdateParticipantRequest], gcd_participant.Participant
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateParticipant(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(
        _BaseParticipantsRestTransport._BaseGetLocation, ParticipantsRestStub
    ):
        def __hash__(self):
            return hash("ParticipantsRestTransport.GetLocation")

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
                _BaseParticipantsRestTransport._BaseGetLocation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseParticipantsRestTransport._BaseGetLocation,
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
                    f"Sending request for google.cloud.dialogflow_v2beta1.ParticipantsClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Participants",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ParticipantsRestTransport._GetLocation._get_response(
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
                    "Received response for google.cloud.dialogflow_v2beta1.ParticipantsAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Participants",
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
        _BaseParticipantsRestTransport._BaseListLocations, ParticipantsRestStub
    ):
        def __hash__(self):
            return hash("ParticipantsRestTransport.ListLocations")

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
                _BaseParticipantsRestTransport._BaseListLocations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseParticipantsRestTransport._BaseListLocations,
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
                    f"Sending request for google.cloud.dialogflow_v2beta1.ParticipantsClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Participants",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ParticipantsRestTransport._ListLocations._get_response(
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
                    "Received response for google.cloud.dialogflow_v2beta1.ParticipantsAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Participants",
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
        _BaseParticipantsRestTransport._BaseCancelOperation, ParticipantsRestStub
    ):
        def __hash__(self):
            return hash("ParticipantsRestTransport.CancelOperation")

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
                _BaseParticipantsRestTransport._BaseCancelOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseParticipantsRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.dialogflow_v2beta1.ParticipantsClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Participants",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ParticipantsRestTransport._CancelOperation._get_response(
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

            return self._interceptor.post_cancel_operation(None)

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(
        _BaseParticipantsRestTransport._BaseGetOperation, ParticipantsRestStub
    ):
        def __hash__(self):
            return hash("ParticipantsRestTransport.GetOperation")

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
                _BaseParticipantsRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseParticipantsRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.dialogflow_v2beta1.ParticipantsClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Participants",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ParticipantsRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.dialogflow_v2beta1.ParticipantsAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Participants",
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
        _BaseParticipantsRestTransport._BaseListOperations, ParticipantsRestStub
    ):
        def __hash__(self):
            return hash("ParticipantsRestTransport.ListOperations")

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
                _BaseParticipantsRestTransport._BaseListOperations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseParticipantsRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.dialogflow_v2beta1.ParticipantsClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Participants",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ParticipantsRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.dialogflow_v2beta1.ParticipantsAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Participants",
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


__all__ = ("ParticipantsRestTransport",)
