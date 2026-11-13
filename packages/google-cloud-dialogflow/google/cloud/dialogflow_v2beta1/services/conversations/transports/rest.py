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
from google.cloud.dialogflow_v2beta1.types import conversation, participant
from google.cloud.dialogflow_v2beta1.types import conversation as gcd_conversation

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseConversationsRestTransport

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


class ConversationsRestInterceptor:
    """Interceptor for Conversations.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the ConversationsRestTransport.

    .. code-block:: python
        class MyCustomConversationsInterceptor(ConversationsRestInterceptor):
            def pre_batch_create_messages(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_create_messages(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_complete_conversation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_complete_conversation(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_conversation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_conversation(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_generate_stateless_suggestion(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_generate_stateless_suggestion(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_generate_stateless_summary(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_generate_stateless_summary(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_generate_suggestions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_generate_suggestions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_conversation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_conversation(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_ingest_context_references(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_ingest_context_references(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_conversations(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_conversations(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_messages(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_messages(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_search_knowledge(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_search_knowledge(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_suggest_conversation_summary(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_suggest_conversation_summary(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = ConversationsRestTransport(interceptor=MyCustomConversationsInterceptor())
        client = ConversationsClient(transport=transport)


    """

    def pre_batch_create_messages(
        self,
        request: conversation.BatchCreateMessagesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        conversation.BatchCreateMessagesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for batch_create_messages

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Conversations server.
        """
        return request, metadata

    def post_batch_create_messages(
        self, response: conversation.BatchCreateMessagesResponse
    ) -> conversation.BatchCreateMessagesResponse:
        """Post-rpc interceptor for batch_create_messages

        DEPRECATED. Please use the `post_batch_create_messages_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Conversations server but before
        it is returned to user code. This `post_batch_create_messages` interceptor runs
        before the `post_batch_create_messages_with_metadata` interceptor.
        """
        return response

    def post_batch_create_messages_with_metadata(
        self,
        response: conversation.BatchCreateMessagesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        conversation.BatchCreateMessagesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_create_messages

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Conversations server but before it is returned to user code.

        We recommend only using this `post_batch_create_messages_with_metadata`
        interceptor in new development instead of the `post_batch_create_messages` interceptor.
        When both interceptors are used, this `post_batch_create_messages_with_metadata` interceptor runs after the
        `post_batch_create_messages` interceptor. The (possibly modified) response returned by
        `post_batch_create_messages` will be passed to
        `post_batch_create_messages_with_metadata`.
        """
        return response, metadata

    def pre_complete_conversation(
        self,
        request: conversation.CompleteConversationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        conversation.CompleteConversationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for complete_conversation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Conversations server.
        """
        return request, metadata

    def post_complete_conversation(
        self, response: conversation.Conversation
    ) -> conversation.Conversation:
        """Post-rpc interceptor for complete_conversation

        DEPRECATED. Please use the `post_complete_conversation_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Conversations server but before
        it is returned to user code. This `post_complete_conversation` interceptor runs
        before the `post_complete_conversation_with_metadata` interceptor.
        """
        return response

    def post_complete_conversation_with_metadata(
        self,
        response: conversation.Conversation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[conversation.Conversation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for complete_conversation

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Conversations server but before it is returned to user code.

        We recommend only using this `post_complete_conversation_with_metadata`
        interceptor in new development instead of the `post_complete_conversation` interceptor.
        When both interceptors are used, this `post_complete_conversation_with_metadata` interceptor runs after the
        `post_complete_conversation` interceptor. The (possibly modified) response returned by
        `post_complete_conversation` will be passed to
        `post_complete_conversation_with_metadata`.
        """
        return response, metadata

    def pre_create_conversation(
        self,
        request: gcd_conversation.CreateConversationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcd_conversation.CreateConversationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_conversation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Conversations server.
        """
        return request, metadata

    def post_create_conversation(
        self, response: gcd_conversation.Conversation
    ) -> gcd_conversation.Conversation:
        """Post-rpc interceptor for create_conversation

        DEPRECATED. Please use the `post_create_conversation_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Conversations server but before
        it is returned to user code. This `post_create_conversation` interceptor runs
        before the `post_create_conversation_with_metadata` interceptor.
        """
        return response

    def post_create_conversation_with_metadata(
        self,
        response: gcd_conversation.Conversation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gcd_conversation.Conversation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_conversation

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Conversations server but before it is returned to user code.

        We recommend only using this `post_create_conversation_with_metadata`
        interceptor in new development instead of the `post_create_conversation` interceptor.
        When both interceptors are used, this `post_create_conversation_with_metadata` interceptor runs after the
        `post_create_conversation` interceptor. The (possibly modified) response returned by
        `post_create_conversation` will be passed to
        `post_create_conversation_with_metadata`.
        """
        return response, metadata

    def pre_generate_stateless_suggestion(
        self,
        request: conversation.GenerateStatelessSuggestionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        conversation.GenerateStatelessSuggestionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for generate_stateless_suggestion

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Conversations server.
        """
        return request, metadata

    def post_generate_stateless_suggestion(
        self, response: conversation.GenerateStatelessSuggestionResponse
    ) -> conversation.GenerateStatelessSuggestionResponse:
        """Post-rpc interceptor for generate_stateless_suggestion

        DEPRECATED. Please use the `post_generate_stateless_suggestion_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Conversations server but before
        it is returned to user code. This `post_generate_stateless_suggestion` interceptor runs
        before the `post_generate_stateless_suggestion_with_metadata` interceptor.
        """
        return response

    def post_generate_stateless_suggestion_with_metadata(
        self,
        response: conversation.GenerateStatelessSuggestionResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        conversation.GenerateStatelessSuggestionResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for generate_stateless_suggestion

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Conversations server but before it is returned to user code.

        We recommend only using this `post_generate_stateless_suggestion_with_metadata`
        interceptor in new development instead of the `post_generate_stateless_suggestion` interceptor.
        When both interceptors are used, this `post_generate_stateless_suggestion_with_metadata` interceptor runs after the
        `post_generate_stateless_suggestion` interceptor. The (possibly modified) response returned by
        `post_generate_stateless_suggestion` will be passed to
        `post_generate_stateless_suggestion_with_metadata`.
        """
        return response, metadata

    def pre_generate_stateless_summary(
        self,
        request: conversation.GenerateStatelessSummaryRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        conversation.GenerateStatelessSummaryRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for generate_stateless_summary

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Conversations server.
        """
        return request, metadata

    def post_generate_stateless_summary(
        self, response: conversation.GenerateStatelessSummaryResponse
    ) -> conversation.GenerateStatelessSummaryResponse:
        """Post-rpc interceptor for generate_stateless_summary

        DEPRECATED. Please use the `post_generate_stateless_summary_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Conversations server but before
        it is returned to user code. This `post_generate_stateless_summary` interceptor runs
        before the `post_generate_stateless_summary_with_metadata` interceptor.
        """
        return response

    def post_generate_stateless_summary_with_metadata(
        self,
        response: conversation.GenerateStatelessSummaryResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        conversation.GenerateStatelessSummaryResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for generate_stateless_summary

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Conversations server but before it is returned to user code.

        We recommend only using this `post_generate_stateless_summary_with_metadata`
        interceptor in new development instead of the `post_generate_stateless_summary` interceptor.
        When both interceptors are used, this `post_generate_stateless_summary_with_metadata` interceptor runs after the
        `post_generate_stateless_summary` interceptor. The (possibly modified) response returned by
        `post_generate_stateless_summary` will be passed to
        `post_generate_stateless_summary_with_metadata`.
        """
        return response, metadata

    def pre_generate_suggestions(
        self,
        request: gcd_conversation.GenerateSuggestionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcd_conversation.GenerateSuggestionsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for generate_suggestions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Conversations server.
        """
        return request, metadata

    def post_generate_suggestions(
        self, response: participant.GenerateSuggestionsResponse
    ) -> participant.GenerateSuggestionsResponse:
        """Post-rpc interceptor for generate_suggestions

        DEPRECATED. Please use the `post_generate_suggestions_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Conversations server but before
        it is returned to user code. This `post_generate_suggestions` interceptor runs
        before the `post_generate_suggestions_with_metadata` interceptor.
        """
        return response

    def post_generate_suggestions_with_metadata(
        self,
        response: participant.GenerateSuggestionsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        participant.GenerateSuggestionsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for generate_suggestions

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Conversations server but before it is returned to user code.

        We recommend only using this `post_generate_suggestions_with_metadata`
        interceptor in new development instead of the `post_generate_suggestions` interceptor.
        When both interceptors are used, this `post_generate_suggestions_with_metadata` interceptor runs after the
        `post_generate_suggestions` interceptor. The (possibly modified) response returned by
        `post_generate_suggestions` will be passed to
        `post_generate_suggestions_with_metadata`.
        """
        return response, metadata

    def pre_get_conversation(
        self,
        request: conversation.GetConversationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        conversation.GetConversationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_conversation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Conversations server.
        """
        return request, metadata

    def post_get_conversation(
        self, response: conversation.Conversation
    ) -> conversation.Conversation:
        """Post-rpc interceptor for get_conversation

        DEPRECATED. Please use the `post_get_conversation_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Conversations server but before
        it is returned to user code. This `post_get_conversation` interceptor runs
        before the `post_get_conversation_with_metadata` interceptor.
        """
        return response

    def post_get_conversation_with_metadata(
        self,
        response: conversation.Conversation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[conversation.Conversation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_conversation

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Conversations server but before it is returned to user code.

        We recommend only using this `post_get_conversation_with_metadata`
        interceptor in new development instead of the `post_get_conversation` interceptor.
        When both interceptors are used, this `post_get_conversation_with_metadata` interceptor runs after the
        `post_get_conversation` interceptor. The (possibly modified) response returned by
        `post_get_conversation` will be passed to
        `post_get_conversation_with_metadata`.
        """
        return response, metadata

    def pre_ingest_context_references(
        self,
        request: gcd_conversation.IngestContextReferencesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcd_conversation.IngestContextReferencesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for ingest_context_references

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Conversations server.
        """
        return request, metadata

    def post_ingest_context_references(
        self, response: gcd_conversation.IngestContextReferencesResponse
    ) -> gcd_conversation.IngestContextReferencesResponse:
        """Post-rpc interceptor for ingest_context_references

        DEPRECATED. Please use the `post_ingest_context_references_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Conversations server but before
        it is returned to user code. This `post_ingest_context_references` interceptor runs
        before the `post_ingest_context_references_with_metadata` interceptor.
        """
        return response

    def post_ingest_context_references_with_metadata(
        self,
        response: gcd_conversation.IngestContextReferencesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcd_conversation.IngestContextReferencesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for ingest_context_references

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Conversations server but before it is returned to user code.

        We recommend only using this `post_ingest_context_references_with_metadata`
        interceptor in new development instead of the `post_ingest_context_references` interceptor.
        When both interceptors are used, this `post_ingest_context_references_with_metadata` interceptor runs after the
        `post_ingest_context_references` interceptor. The (possibly modified) response returned by
        `post_ingest_context_references` will be passed to
        `post_ingest_context_references_with_metadata`.
        """
        return response, metadata

    def pre_list_conversations(
        self,
        request: conversation.ListConversationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        conversation.ListConversationsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_conversations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Conversations server.
        """
        return request, metadata

    def post_list_conversations(
        self, response: conversation.ListConversationsResponse
    ) -> conversation.ListConversationsResponse:
        """Post-rpc interceptor for list_conversations

        DEPRECATED. Please use the `post_list_conversations_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Conversations server but before
        it is returned to user code. This `post_list_conversations` interceptor runs
        before the `post_list_conversations_with_metadata` interceptor.
        """
        return response

    def post_list_conversations_with_metadata(
        self,
        response: conversation.ListConversationsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        conversation.ListConversationsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_conversations

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Conversations server but before it is returned to user code.

        We recommend only using this `post_list_conversations_with_metadata`
        interceptor in new development instead of the `post_list_conversations` interceptor.
        When both interceptors are used, this `post_list_conversations_with_metadata` interceptor runs after the
        `post_list_conversations` interceptor. The (possibly modified) response returned by
        `post_list_conversations` will be passed to
        `post_list_conversations_with_metadata`.
        """
        return response, metadata

    def pre_list_messages(
        self,
        request: conversation.ListMessagesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        conversation.ListMessagesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_messages

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Conversations server.
        """
        return request, metadata

    def post_list_messages(
        self, response: conversation.ListMessagesResponse
    ) -> conversation.ListMessagesResponse:
        """Post-rpc interceptor for list_messages

        DEPRECATED. Please use the `post_list_messages_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Conversations server but before
        it is returned to user code. This `post_list_messages` interceptor runs
        before the `post_list_messages_with_metadata` interceptor.
        """
        return response

    def post_list_messages_with_metadata(
        self,
        response: conversation.ListMessagesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        conversation.ListMessagesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_messages

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Conversations server but before it is returned to user code.

        We recommend only using this `post_list_messages_with_metadata`
        interceptor in new development instead of the `post_list_messages` interceptor.
        When both interceptors are used, this `post_list_messages_with_metadata` interceptor runs after the
        `post_list_messages` interceptor. The (possibly modified) response returned by
        `post_list_messages` will be passed to
        `post_list_messages_with_metadata`.
        """
        return response, metadata

    def pre_search_knowledge(
        self,
        request: conversation.SearchKnowledgeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        conversation.SearchKnowledgeRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for search_knowledge

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Conversations server.
        """
        return request, metadata

    def post_search_knowledge(
        self, response: conversation.SearchKnowledgeResponse
    ) -> conversation.SearchKnowledgeResponse:
        """Post-rpc interceptor for search_knowledge

        DEPRECATED. Please use the `post_search_knowledge_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Conversations server but before
        it is returned to user code. This `post_search_knowledge` interceptor runs
        before the `post_search_knowledge_with_metadata` interceptor.
        """
        return response

    def post_search_knowledge_with_metadata(
        self,
        response: conversation.SearchKnowledgeResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        conversation.SearchKnowledgeResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for search_knowledge

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Conversations server but before it is returned to user code.

        We recommend only using this `post_search_knowledge_with_metadata`
        interceptor in new development instead of the `post_search_knowledge` interceptor.
        When both interceptors are used, this `post_search_knowledge_with_metadata` interceptor runs after the
        `post_search_knowledge` interceptor. The (possibly modified) response returned by
        `post_search_knowledge` will be passed to
        `post_search_knowledge_with_metadata`.
        """
        return response, metadata

    def pre_suggest_conversation_summary(
        self,
        request: gcd_conversation.SuggestConversationSummaryRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcd_conversation.SuggestConversationSummaryRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for suggest_conversation_summary

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Conversations server.
        """
        return request, metadata

    def post_suggest_conversation_summary(
        self, response: gcd_conversation.SuggestConversationSummaryResponse
    ) -> gcd_conversation.SuggestConversationSummaryResponse:
        """Post-rpc interceptor for suggest_conversation_summary

        DEPRECATED. Please use the `post_suggest_conversation_summary_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Conversations server but before
        it is returned to user code. This `post_suggest_conversation_summary` interceptor runs
        before the `post_suggest_conversation_summary_with_metadata` interceptor.
        """
        return response

    def post_suggest_conversation_summary_with_metadata(
        self,
        response: gcd_conversation.SuggestConversationSummaryResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcd_conversation.SuggestConversationSummaryResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for suggest_conversation_summary

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Conversations server but before it is returned to user code.

        We recommend only using this `post_suggest_conversation_summary_with_metadata`
        interceptor in new development instead of the `post_suggest_conversation_summary` interceptor.
        When both interceptors are used, this `post_suggest_conversation_summary_with_metadata` interceptor runs after the
        `post_suggest_conversation_summary` interceptor. The (possibly modified) response returned by
        `post_suggest_conversation_summary` will be passed to
        `post_suggest_conversation_summary_with_metadata`.
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
        before they are sent to the Conversations server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the Conversations server but before
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
        before they are sent to the Conversations server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the Conversations server but before
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
        before they are sent to the Conversations server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the Conversations server but before
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
        before they are sent to the Conversations server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the Conversations server but before
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
        before they are sent to the Conversations server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the Conversations server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class ConversationsRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: ConversationsRestInterceptor


class ConversationsRestTransport(_BaseConversationsRestTransport):
    """REST backend synchronous transport for Conversations.

    Service for managing
    [Conversations][google.cloud.dialogflow.v2beta1.Conversation].

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
        interceptor: Optional[ConversationsRestInterceptor] = None,
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
            interceptor (Optional[ConversationsRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or ConversationsRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _BatchCreateMessages(
        _BaseConversationsRestTransport._BaseBatchCreateMessages, ConversationsRestStub
    ):
        def __hash__(self):
            return hash("ConversationsRestTransport.BatchCreateMessages")

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
            request: conversation.BatchCreateMessagesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> conversation.BatchCreateMessagesResponse:
            r"""Call the batch create messages method over HTTP.

            Args:
                request (~.conversation.BatchCreateMessagesRequest):
                    The request object. The request message for
                [Conversations.BatchCreateMessagesRequest][].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.conversation.BatchCreateMessagesResponse:
                    The request message for
                [Conversations.BatchCreateMessagesResponse][].

            """

            http_options = _BaseConversationsRestTransport._BaseBatchCreateMessages._get_http_options()
            request, metadata = self._interceptor.pre_batch_create_messages(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConversationsRestTransport._BaseBatchCreateMessages,
                    "_BaseBatchCreateMessages__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow_v2beta1.ConversationsClient.BatchCreateMessages",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Conversations",
                        "rpcName": "BatchCreateMessages",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConversationsRestTransport._BatchCreateMessages._get_response(
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
            resp = conversation.BatchCreateMessagesResponse()
            pb_resp = conversation.BatchCreateMessagesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_create_messages(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_create_messages_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = conversation.BatchCreateMessagesResponse.to_json(
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
                    "Received response for google.cloud.dialogflow_v2beta1.ConversationsClient.batch_create_messages",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Conversations",
                        "rpcName": "BatchCreateMessages",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CompleteConversation(
        _BaseConversationsRestTransport._BaseCompleteConversation, ConversationsRestStub
    ):
        def __hash__(self):
            return hash("ConversationsRestTransport.CompleteConversation")

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
            request: conversation.CompleteConversationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> conversation.Conversation:
            r"""Call the complete conversation method over HTTP.

            Args:
                request (~.conversation.CompleteConversationRequest):
                    The request object. The request message for
                [Conversations.CompleteConversation][google.cloud.dialogflow.v2beta1.Conversations.CompleteConversation].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.conversation.Conversation:
                    Represents a conversation.
                A conversation is an interaction between
                an agent, including live agents and
                Dialogflow agents, and a support
                customer. Conversations can include
                phone calls and text-based chat
                sessions.

            """

            http_options = _BaseConversationsRestTransport._BaseCompleteConversation._get_http_options()
            request, metadata = self._interceptor.pre_complete_conversation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConversationsRestTransport._BaseCompleteConversation,
                    "_BaseCompleteConversation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow_v2beta1.ConversationsClient.CompleteConversation",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Conversations",
                        "rpcName": "CompleteConversation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConversationsRestTransport._CompleteConversation._get_response(
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
            resp = conversation.Conversation()
            pb_resp = conversation.Conversation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_complete_conversation(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_complete_conversation_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = conversation.Conversation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dialogflow_v2beta1.ConversationsClient.complete_conversation",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Conversations",
                        "rpcName": "CompleteConversation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateConversation(
        _BaseConversationsRestTransport._BaseCreateConversation, ConversationsRestStub
    ):
        def __hash__(self):
            return hash("ConversationsRestTransport.CreateConversation")

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
            request: gcd_conversation.CreateConversationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcd_conversation.Conversation:
            r"""Call the create conversation method over HTTP.

            Args:
                request (~.gcd_conversation.CreateConversationRequest):
                    The request object. The request message for
                [Conversations.CreateConversation][google.cloud.dialogflow.v2beta1.Conversations.CreateConversation].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcd_conversation.Conversation:
                    Represents a conversation.
                A conversation is an interaction between
                an agent, including live agents and
                Dialogflow agents, and a support
                customer. Conversations can include
                phone calls and text-based chat
                sessions.

            """

            http_options = _BaseConversationsRestTransport._BaseCreateConversation._get_http_options()
            request, metadata = self._interceptor.pre_create_conversation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConversationsRestTransport._BaseCreateConversation,
                    "_BaseCreateConversation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow_v2beta1.ConversationsClient.CreateConversation",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Conversations",
                        "rpcName": "CreateConversation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConversationsRestTransport._CreateConversation._get_response(
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
            resp = gcd_conversation.Conversation()
            pb_resp = gcd_conversation.Conversation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_conversation(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_conversation_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcd_conversation.Conversation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dialogflow_v2beta1.ConversationsClient.create_conversation",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Conversations",
                        "rpcName": "CreateConversation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GenerateStatelessSuggestion(
        _BaseConversationsRestTransport._BaseGenerateStatelessSuggestion,
        ConversationsRestStub,
    ):
        def __hash__(self):
            return hash("ConversationsRestTransport.GenerateStatelessSuggestion")

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
            request: conversation.GenerateStatelessSuggestionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> conversation.GenerateStatelessSuggestionResponse:
            r"""Call the generate stateless
            suggestion method over HTTP.

                Args:
                    request (~.conversation.GenerateStatelessSuggestionRequest):
                        The request object. The request message for
                    [Conversations.GenerateStatelessSuggestion][google.cloud.dialogflow.v2beta1.Conversations.GenerateStatelessSuggestion].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.conversation.GenerateStatelessSuggestionResponse:
                        The response message for
                    [Conversations.GenerateStatelessSuggestion][google.cloud.dialogflow.v2beta1.Conversations.GenerateStatelessSuggestion].

            """

            http_options = _BaseConversationsRestTransport._BaseGenerateStatelessSuggestion._get_http_options()
            request, metadata = self._interceptor.pre_generate_stateless_suggestion(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConversationsRestTransport._BaseGenerateStatelessSuggestion,
                    "_BaseGenerateStatelessSuggestion__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow_v2beta1.ConversationsClient.GenerateStatelessSuggestion",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Conversations",
                        "rpcName": "GenerateStatelessSuggestion",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ConversationsRestTransport._GenerateStatelessSuggestion._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                    body,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = conversation.GenerateStatelessSuggestionResponse()
            pb_resp = conversation.GenerateStatelessSuggestionResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_generate_stateless_suggestion(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_generate_stateless_suggestion_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        conversation.GenerateStatelessSuggestionResponse.to_json(
                            response
                        )
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dialogflow_v2beta1.ConversationsClient.generate_stateless_suggestion",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Conversations",
                        "rpcName": "GenerateStatelessSuggestion",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GenerateStatelessSummary(
        _BaseConversationsRestTransport._BaseGenerateStatelessSummary,
        ConversationsRestStub,
    ):
        def __hash__(self):
            return hash("ConversationsRestTransport.GenerateStatelessSummary")

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
            request: conversation.GenerateStatelessSummaryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> conversation.GenerateStatelessSummaryResponse:
            r"""Call the generate stateless
            summary method over HTTP.

                Args:
                    request (~.conversation.GenerateStatelessSummaryRequest):
                        The request object. The request message for
                    [Conversations.GenerateStatelessSummary][google.cloud.dialogflow.v2beta1.Conversations.GenerateStatelessSummary].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.conversation.GenerateStatelessSummaryResponse:
                        The response message for
                    [Conversations.GenerateStatelessSummary][google.cloud.dialogflow.v2beta1.Conversations.GenerateStatelessSummary].

            """

            http_options = _BaseConversationsRestTransport._BaseGenerateStatelessSummary._get_http_options()
            request, metadata = self._interceptor.pre_generate_stateless_summary(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConversationsRestTransport._BaseGenerateStatelessSummary,
                    "_BaseGenerateStatelessSummary__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow_v2beta1.ConversationsClient.GenerateStatelessSummary",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Conversations",
                        "rpcName": "GenerateStatelessSummary",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ConversationsRestTransport._GenerateStatelessSummary._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                    body,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = conversation.GenerateStatelessSummaryResponse()
            pb_resp = conversation.GenerateStatelessSummaryResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_generate_stateless_summary(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_generate_stateless_summary_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        conversation.GenerateStatelessSummaryResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dialogflow_v2beta1.ConversationsClient.generate_stateless_summary",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Conversations",
                        "rpcName": "GenerateStatelessSummary",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GenerateSuggestions(
        _BaseConversationsRestTransport._BaseGenerateSuggestions, ConversationsRestStub
    ):
        def __hash__(self):
            return hash("ConversationsRestTransport.GenerateSuggestions")

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
            request: gcd_conversation.GenerateSuggestionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> participant.GenerateSuggestionsResponse:
            r"""Call the generate suggestions method over HTTP.

            Args:
                request (~.gcd_conversation.GenerateSuggestionsRequest):
                    The request object. The request message for
                [Conversations.GenerateSuggestions][google.cloud.dialogflow.v2beta1.Conversations.GenerateSuggestions].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.participant.GenerateSuggestionsResponse:
                    The response message for
                [Conversations.GenerateSuggestions][google.cloud.dialogflow.v2beta1.Conversations.GenerateSuggestions].

            """

            http_options = _BaseConversationsRestTransport._BaseGenerateSuggestions._get_http_options()
            request, metadata = self._interceptor.pre_generate_suggestions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConversationsRestTransport._BaseGenerateSuggestions,
                    "_BaseGenerateSuggestions__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow_v2beta1.ConversationsClient.GenerateSuggestions",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Conversations",
                        "rpcName": "GenerateSuggestions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConversationsRestTransport._GenerateSuggestions._get_response(
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
            resp = participant.GenerateSuggestionsResponse()
            pb_resp = participant.GenerateSuggestionsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_generate_suggestions(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_generate_suggestions_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = participant.GenerateSuggestionsResponse.to_json(
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
                    "Received response for google.cloud.dialogflow_v2beta1.ConversationsClient.generate_suggestions",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Conversations",
                        "rpcName": "GenerateSuggestions",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetConversation(
        _BaseConversationsRestTransport._BaseGetConversation, ConversationsRestStub
    ):
        def __hash__(self):
            return hash("ConversationsRestTransport.GetConversation")

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
            request: conversation.GetConversationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> conversation.Conversation:
            r"""Call the get conversation method over HTTP.

            Args:
                request (~.conversation.GetConversationRequest):
                    The request object. The request message for
                [Conversations.GetConversation][google.cloud.dialogflow.v2beta1.Conversations.GetConversation].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.conversation.Conversation:
                    Represents a conversation.
                A conversation is an interaction between
                an agent, including live agents and
                Dialogflow agents, and a support
                customer. Conversations can include
                phone calls and text-based chat
                sessions.

            """

            http_options = (
                _BaseConversationsRestTransport._BaseGetConversation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_conversation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConversationsRestTransport._BaseGetConversation,
                    "_BaseGetConversation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow_v2beta1.ConversationsClient.GetConversation",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Conversations",
                        "rpcName": "GetConversation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConversationsRestTransport._GetConversation._get_response(
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
            resp = conversation.Conversation()
            pb_resp = conversation.Conversation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_conversation(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_conversation_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = conversation.Conversation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dialogflow_v2beta1.ConversationsClient.get_conversation",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Conversations",
                        "rpcName": "GetConversation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _IngestContextReferences(
        _BaseConversationsRestTransport._BaseIngestContextReferences,
        ConversationsRestStub,
    ):
        def __hash__(self):
            return hash("ConversationsRestTransport.IngestContextReferences")

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
            request: gcd_conversation.IngestContextReferencesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcd_conversation.IngestContextReferencesResponse:
            r"""Call the ingest context references method over HTTP.

            Args:
                request (~.gcd_conversation.IngestContextReferencesRequest):
                    The request object. The request message for
                [ConversationsService.IngestContextReferences][].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcd_conversation.IngestContextReferencesResponse:
                    The response message for
                [ConversationsService.IngestContextReferences][].

            """

            http_options = _BaseConversationsRestTransport._BaseIngestContextReferences._get_http_options()
            request, metadata = self._interceptor.pre_ingest_context_references(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConversationsRestTransport._BaseIngestContextReferences,
                    "_BaseIngestContextReferences__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow_v2beta1.ConversationsClient.IngestContextReferences",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Conversations",
                        "rpcName": "IngestContextReferences",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ConversationsRestTransport._IngestContextReferences._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                    body,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = gcd_conversation.IngestContextReferencesResponse()
            pb_resp = gcd_conversation.IngestContextReferencesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_ingest_context_references(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_ingest_context_references_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        gcd_conversation.IngestContextReferencesResponse.to_json(
                            response
                        )
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dialogflow_v2beta1.ConversationsClient.ingest_context_references",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Conversations",
                        "rpcName": "IngestContextReferences",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListConversations(
        _BaseConversationsRestTransport._BaseListConversations, ConversationsRestStub
    ):
        def __hash__(self):
            return hash("ConversationsRestTransport.ListConversations")

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
            request: conversation.ListConversationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> conversation.ListConversationsResponse:
            r"""Call the list conversations method over HTTP.

            Args:
                request (~.conversation.ListConversationsRequest):
                    The request object. The request message for
                [Conversations.ListConversations][google.cloud.dialogflow.v2beta1.Conversations.ListConversations].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.conversation.ListConversationsResponse:
                    The response message for
                [Conversations.ListConversations][google.cloud.dialogflow.v2beta1.Conversations.ListConversations].

            """

            http_options = _BaseConversationsRestTransport._BaseListConversations._get_http_options()
            request, metadata = self._interceptor.pre_list_conversations(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConversationsRestTransport._BaseListConversations,
                    "_BaseListConversations__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow_v2beta1.ConversationsClient.ListConversations",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Conversations",
                        "rpcName": "ListConversations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConversationsRestTransport._ListConversations._get_response(
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
            resp = conversation.ListConversationsResponse()
            pb_resp = conversation.ListConversationsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_conversations(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_conversations_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = conversation.ListConversationsResponse.to_json(
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
                    "Received response for google.cloud.dialogflow_v2beta1.ConversationsClient.list_conversations",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Conversations",
                        "rpcName": "ListConversations",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListMessages(
        _BaseConversationsRestTransport._BaseListMessages, ConversationsRestStub
    ):
        def __hash__(self):
            return hash("ConversationsRestTransport.ListMessages")

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
            request: conversation.ListMessagesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> conversation.ListMessagesResponse:
            r"""Call the list messages method over HTTP.

            Args:
                request (~.conversation.ListMessagesRequest):
                    The request object. The request message for
                [Conversations.ListMessages][google.cloud.dialogflow.v2beta1.Conversations.ListMessages].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.conversation.ListMessagesResponse:
                    The response message for
                [Conversations.ListMessages][google.cloud.dialogflow.v2beta1.Conversations.ListMessages].

            """

            http_options = (
                _BaseConversationsRestTransport._BaseListMessages._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_messages(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConversationsRestTransport._BaseListMessages,
                    "_BaseListMessages__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow_v2beta1.ConversationsClient.ListMessages",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Conversations",
                        "rpcName": "ListMessages",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConversationsRestTransport._ListMessages._get_response(
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
            resp = conversation.ListMessagesResponse()
            pb_resp = conversation.ListMessagesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_messages(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_messages_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = conversation.ListMessagesResponse.to_json(
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
                    "Received response for google.cloud.dialogflow_v2beta1.ConversationsClient.list_messages",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Conversations",
                        "rpcName": "ListMessages",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SearchKnowledge(
        _BaseConversationsRestTransport._BaseSearchKnowledge, ConversationsRestStub
    ):
        def __hash__(self):
            return hash("ConversationsRestTransport.SearchKnowledge")

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
            request: conversation.SearchKnowledgeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> conversation.SearchKnowledgeResponse:
            r"""Call the search knowledge method over HTTP.

            Args:
                request (~.conversation.SearchKnowledgeRequest):
                    The request object. The request message for
                [Conversations.SearchKnowledge][google.cloud.dialogflow.v2beta1.Conversations.SearchKnowledge].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.conversation.SearchKnowledgeResponse:
                    The response message for
                [Conversations.SearchKnowledge][google.cloud.dialogflow.v2beta1.Conversations.SearchKnowledge].

            """

            http_options = (
                _BaseConversationsRestTransport._BaseSearchKnowledge._get_http_options()
            )
            request, metadata = self._interceptor.pre_search_knowledge(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConversationsRestTransport._BaseSearchKnowledge,
                    "_BaseSearchKnowledge__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow_v2beta1.ConversationsClient.SearchKnowledge",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Conversations",
                        "rpcName": "SearchKnowledge",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConversationsRestTransport._SearchKnowledge._get_response(
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
            resp = conversation.SearchKnowledgeResponse()
            pb_resp = conversation.SearchKnowledgeResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_search_knowledge(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_search_knowledge_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = conversation.SearchKnowledgeResponse.to_json(
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
                    "Received response for google.cloud.dialogflow_v2beta1.ConversationsClient.search_knowledge",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Conversations",
                        "rpcName": "SearchKnowledge",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SuggestConversationSummary(
        _BaseConversationsRestTransport._BaseSuggestConversationSummary,
        ConversationsRestStub,
    ):
        def __hash__(self):
            return hash("ConversationsRestTransport.SuggestConversationSummary")

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
            request: gcd_conversation.SuggestConversationSummaryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcd_conversation.SuggestConversationSummaryResponse:
            r"""Call the suggest conversation
            summary method over HTTP.

                Args:
                    request (~.gcd_conversation.SuggestConversationSummaryRequest):
                        The request object. The request message for
                    [Conversations.SuggestConversationSummary][google.cloud.dialogflow.v2beta1.Conversations.SuggestConversationSummary].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.gcd_conversation.SuggestConversationSummaryResponse:
                        The response message for
                    [Conversations.SuggestConversationSummary][google.cloud.dialogflow.v2beta1.Conversations.SuggestConversationSummary].

            """

            http_options = _BaseConversationsRestTransport._BaseSuggestConversationSummary._get_http_options()
            request, metadata = self._interceptor.pre_suggest_conversation_summary(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConversationsRestTransport._BaseSuggestConversationSummary,
                    "_BaseSuggestConversationSummary__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow_v2beta1.ConversationsClient.SuggestConversationSummary",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Conversations",
                        "rpcName": "SuggestConversationSummary",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ConversationsRestTransport._SuggestConversationSummary._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                    body,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = gcd_conversation.SuggestConversationSummaryResponse()
            pb_resp = gcd_conversation.SuggestConversationSummaryResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_suggest_conversation_summary(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_suggest_conversation_summary_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        gcd_conversation.SuggestConversationSummaryResponse.to_json(
                            response
                        )
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dialogflow_v2beta1.ConversationsClient.suggest_conversation_summary",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Conversations",
                        "rpcName": "SuggestConversationSummary",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def batch_create_messages(
        self,
    ) -> Callable[
        [conversation.BatchCreateMessagesRequest],
        conversation.BatchCreateMessagesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchCreateMessages(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def complete_conversation(
        self,
    ) -> Callable[
        [conversation.CompleteConversationRequest], conversation.Conversation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CompleteConversation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_conversation(
        self,
    ) -> Callable[
        [gcd_conversation.CreateConversationRequest], gcd_conversation.Conversation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateConversation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def generate_stateless_suggestion(
        self,
    ) -> Callable[
        [conversation.GenerateStatelessSuggestionRequest],
        conversation.GenerateStatelessSuggestionResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GenerateStatelessSuggestion(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def generate_stateless_summary(
        self,
    ) -> Callable[
        [conversation.GenerateStatelessSummaryRequest],
        conversation.GenerateStatelessSummaryResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GenerateStatelessSummary(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def generate_suggestions(
        self,
    ) -> Callable[
        [gcd_conversation.GenerateSuggestionsRequest],
        participant.GenerateSuggestionsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GenerateSuggestions(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_conversation(
        self,
    ) -> Callable[[conversation.GetConversationRequest], conversation.Conversation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetConversation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def ingest_context_references(
        self,
    ) -> Callable[
        [gcd_conversation.IngestContextReferencesRequest],
        gcd_conversation.IngestContextReferencesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._IngestContextReferences(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_conversations(
        self,
    ) -> Callable[
        [conversation.ListConversationsRequest], conversation.ListConversationsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListConversations(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_messages(
        self,
    ) -> Callable[
        [conversation.ListMessagesRequest], conversation.ListMessagesResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListMessages(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def search_knowledge(
        self,
    ) -> Callable[
        [conversation.SearchKnowledgeRequest], conversation.SearchKnowledgeResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SearchKnowledge(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def suggest_conversation_summary(
        self,
    ) -> Callable[
        [gcd_conversation.SuggestConversationSummaryRequest],
        gcd_conversation.SuggestConversationSummaryResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SuggestConversationSummary(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(
        _BaseConversationsRestTransport._BaseGetLocation, ConversationsRestStub
    ):
        def __hash__(self):
            return hash("ConversationsRestTransport.GetLocation")

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
                _BaseConversationsRestTransport._BaseGetLocation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConversationsRestTransport._BaseGetLocation,
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
                    f"Sending request for google.cloud.dialogflow_v2beta1.ConversationsClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Conversations",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConversationsRestTransport._GetLocation._get_response(
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
                    "Received response for google.cloud.dialogflow_v2beta1.ConversationsAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Conversations",
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
        _BaseConversationsRestTransport._BaseListLocations, ConversationsRestStub
    ):
        def __hash__(self):
            return hash("ConversationsRestTransport.ListLocations")

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
                _BaseConversationsRestTransport._BaseListLocations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConversationsRestTransport._BaseListLocations,
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
                    f"Sending request for google.cloud.dialogflow_v2beta1.ConversationsClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Conversations",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConversationsRestTransport._ListLocations._get_response(
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
                    "Received response for google.cloud.dialogflow_v2beta1.ConversationsAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Conversations",
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
        _BaseConversationsRestTransport._BaseCancelOperation, ConversationsRestStub
    ):
        def __hash__(self):
            return hash("ConversationsRestTransport.CancelOperation")

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
                _BaseConversationsRestTransport._BaseCancelOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConversationsRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.dialogflow_v2beta1.ConversationsClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Conversations",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConversationsRestTransport._CancelOperation._get_response(
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
        _BaseConversationsRestTransport._BaseGetOperation, ConversationsRestStub
    ):
        def __hash__(self):
            return hash("ConversationsRestTransport.GetOperation")

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
                _BaseConversationsRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConversationsRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.dialogflow_v2beta1.ConversationsClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Conversations",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConversationsRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.dialogflow_v2beta1.ConversationsAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Conversations",
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
        _BaseConversationsRestTransport._BaseListOperations, ConversationsRestStub
    ):
        def __hash__(self):
            return hash("ConversationsRestTransport.ListOperations")

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
                _BaseConversationsRestTransport._BaseListOperations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConversationsRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.dialogflow_v2beta1.ConversationsClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Conversations",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConversationsRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.dialogflow_v2beta1.ConversationsAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Conversations",
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


__all__ = ("ConversationsRestTransport",)
