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
from __future__ import annotations

from typing import MutableMapping, MutableSequence

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.discoveryengine_v1beta.types import assist_answer, search_service
from google.cloud.discoveryengine_v1beta.types import assistant as gcd_assistant
from google.cloud.discoveryengine_v1beta.types import session as gcd_session

__protobuf__ = proto.module(
    package="google.cloud.discoveryengine.v1beta",
    manifest={
        "AssistUserMetadata",
        "StreamAssistRequest",
        "StreamAssistResponse",
        "CreateAssistantRequest",
        "DeleteAssistantRequest",
        "GetAssistantRequest",
        "ListAssistantsRequest",
        "ListAssistantsResponse",
        "UpdateAssistantRequest",
    },
)


class AssistUserMetadata(proto.Message):
    r"""User metadata of the request.

    Attributes:
        time_zone (str):
            Optional. IANA time zone, e.g.
            Europe/Budapest.
        preferred_language_code (str):
            Optional. Preferred language to be used for
            answering if language detection fails. Also used
            as the language of error messages created by
            actions, regardless of language detection
            results.
    """

    time_zone: str = proto.Field(
        proto.STRING,
        number=1,
    )
    preferred_language_code: str = proto.Field(
        proto.STRING,
        number=2,
    )


class StreamAssistRequest(proto.Message):
    r"""Request for the
    [AssistantService.StreamAssist][google.cloud.discoveryengine.v1beta.AssistantService.StreamAssist]
    method.

    Attributes:
        name (str):
            Required. The resource name of the
            [Assistant][google.cloud.discoveryengine.v1beta.Assistant].
            Format:
            ``projects/{project}/locations/{location}/collections/{collection}/engines/{engine}/assistants/{assistant}``
        query (google.cloud.discoveryengine_v1beta.types.Query):
            Optional. Current user query.

            Empty query is only supported if ``file_ids`` are provided.
            In this case, the answer will be generated based on those
            context files.
        session (str):
            Optional. The session to use for the request. If specified,
            the assistant has access to the session history, and the
            query and the answer are stored there.

            If ``-`` is specified as the session ID, or it is left
            empty, then a new session is created with an automatically
            generated ID.

            Format:
            ``projects/{project}/locations/{location}/collections/{collection}/engines/{engine}/sessions/{session}``
        user_metadata (google.cloud.discoveryengine_v1beta.types.AssistUserMetadata):
            Optional. Information about the user
            initiating the query.
        agents_spec (google.cloud.discoveryengine_v1beta.types.StreamAssistRequest.AgentsSpec):
            Optional. Specification of agents that are
            used to serve the request.
        tools_spec (google.cloud.discoveryengine_v1beta.types.StreamAssistRequest.ToolsSpec):
            Optional. Specification of tools that are
            used to serve the request.
        generation_spec (google.cloud.discoveryengine_v1beta.types.StreamAssistRequest.GenerationSpec):
            Optional. Specification of the generation
            configuration for the request.
    """

    class AgentsSpec(proto.Message):
        r"""Specification of agents that are used to serve the request.

        Attributes:
            agent_specs (MutableSequence[google.cloud.discoveryengine_v1beta.types.StreamAssistRequest.AgentsSpec.AgentSpec]):
                Optional. Specification of agents that are
                used to serve the request.
        """

        class AgentSpec(proto.Message):
            r"""Specification of an agent.

            Attributes:
                agent_id (str):
                    Required. ID to identify the agent resource serving the
                    request.

                    This field must conform to
                    `RFC-1034 <https://tools.ietf.org/html/rfc1034>`__ with a
                    length limit of 63 characters.
            """

            agent_id: str = proto.Field(
                proto.STRING,
                number=1,
            )

        agent_specs: MutableSequence["StreamAssistRequest.AgentsSpec.AgentSpec"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=1,
                message="StreamAssistRequest.AgentsSpec.AgentSpec",
            )
        )

    class ToolsSpec(proto.Message):
        r"""Specification of tools that are used to serve the request.

        Attributes:
            vertex_ai_search_spec (google.cloud.discoveryengine_v1beta.types.StreamAssistRequest.ToolsSpec.VertexAiSearchSpec):
                Optional. Specification of the Vertex AI
                Search tool.
            web_grounding_spec (google.cloud.discoveryengine_v1beta.types.StreamAssistRequest.ToolsSpec.WebGroundingSpec):
                Optional. Specification of the web grounding tool. If field
                is present, enables grounding with web search. Works only if
                [Assistant.web_grounding_type][google.cloud.discoveryengine.v1beta.Assistant.web_grounding_type]
                is
                [WEB_GROUNDING_TYPE_GOOGLE_SEARCH][google.cloud.discoveryengine.v1beta.Assistant.WebGroundingType.WEB_GROUNDING_TYPE_GOOGLE_SEARCH]
                or
                [WEB_GROUNDING_TYPE_ENTERPRISE_WEB_SEARCH][google.cloud.discoveryengine.v1beta.Assistant.WebGroundingType.WEB_GROUNDING_TYPE_ENTERPRISE_WEB_SEARCH].
            image_generation_spec (google.cloud.discoveryengine_v1beta.types.StreamAssistRequest.ToolsSpec.ImageGenerationSpec):
                Optional. Specification of the image
                generation tool.
            video_generation_spec (google.cloud.discoveryengine_v1beta.types.StreamAssistRequest.ToolsSpec.VideoGenerationSpec):
                Optional. Specification of the video
                generation tool.
        """

        class VertexAiSearchSpec(proto.Message):
            r"""Specification of the Vertex AI Search tool.

            Attributes:
                data_store_specs (MutableSequence[google.cloud.discoveryengine_v1beta.types.SearchRequest.DataStoreSpec]):
                    Optional. Specs defining
                    [DataStore][google.cloud.discoveryengine.v1beta.DataStore]s
                    to filter on in a search call and configurations for those
                    data stores. This is only considered for
                    [Engine][google.cloud.discoveryengine.v1beta.Engine]s with
                    multiple data stores.
                filter (str):
                    Optional. The filter syntax consists of an expression
                    language for constructing a predicate from one or more
                    fields of the documents being filtered. Filter expression is
                    case-sensitive.

                    If this field is unrecognizable, an ``INVALID_ARGUMENT`` is
                    returned.

                    Filtering in Vertex AI Search is done by mapping the LHS
                    filter key to a key property defined in the Vertex AI Search
                    backend -- this mapping is defined by the customer in their
                    schema. For example a media customer might have a field
                    'name' in their schema. In this case the filter would look
                    like this: filter --> name:'ANY("king kong")'

                    For more information about filtering including syntax and
                    filter operators, see
                    `Filter <https://cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata>`__
            """

            data_store_specs: MutableSequence[
                search_service.SearchRequest.DataStoreSpec
            ] = proto.RepeatedField(
                proto.MESSAGE,
                number=2,
                message=search_service.SearchRequest.DataStoreSpec,
            )
            filter: str = proto.Field(
                proto.STRING,
                number=4,
            )

        class WebGroundingSpec(proto.Message):
            r"""Specification of the web grounding tool."""

        class ImageGenerationSpec(proto.Message):
            r"""Specification of the image generation tool."""

        class VideoGenerationSpec(proto.Message):
            r"""Specification of the video generation tool."""

        vertex_ai_search_spec: "StreamAssistRequest.ToolsSpec.VertexAiSearchSpec" = (
            proto.Field(
                proto.MESSAGE,
                number=1,
                message="StreamAssistRequest.ToolsSpec.VertexAiSearchSpec",
            )
        )
        web_grounding_spec: "StreamAssistRequest.ToolsSpec.WebGroundingSpec" = (
            proto.Field(
                proto.MESSAGE,
                number=2,
                message="StreamAssistRequest.ToolsSpec.WebGroundingSpec",
            )
        )
        image_generation_spec: "StreamAssistRequest.ToolsSpec.ImageGenerationSpec" = (
            proto.Field(
                proto.MESSAGE,
                number=3,
                message="StreamAssistRequest.ToolsSpec.ImageGenerationSpec",
            )
        )
        video_generation_spec: "StreamAssistRequest.ToolsSpec.VideoGenerationSpec" = (
            proto.Field(
                proto.MESSAGE,
                number=4,
                message="StreamAssistRequest.ToolsSpec.VideoGenerationSpec",
            )
        )

    class GenerationSpec(proto.Message):
        r"""Assistant generation specification for the request.
        This allows to override the default generation configuration at
        the engine level.

        Attributes:
            model_id (str):
                Optional. The Vertex AI model_id used for the generative
                model. If not set, the default Assistant model will be used.
        """

        model_id: str = proto.Field(
            proto.STRING,
            number=1,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    query: gcd_session.Query = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcd_session.Query,
    )
    session: str = proto.Field(
        proto.STRING,
        number=3,
    )
    user_metadata: "AssistUserMetadata" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="AssistUserMetadata",
    )
    agents_spec: AgentsSpec = proto.Field(
        proto.MESSAGE,
        number=22,
        message=AgentsSpec,
    )
    tools_spec: ToolsSpec = proto.Field(
        proto.MESSAGE,
        number=18,
        message=ToolsSpec,
    )
    generation_spec: GenerationSpec = proto.Field(
        proto.MESSAGE,
        number=19,
        message=GenerationSpec,
    )


class StreamAssistResponse(proto.Message):
    r"""Response for the
    [AssistantService.StreamAssist][google.cloud.discoveryengine.v1beta.AssistantService.StreamAssist]
    method.

    Attributes:
        answer (google.cloud.discoveryengine_v1beta.types.AssistAnswer):
            Assist answer resource object containing parts of the
            assistant's final answer for the user's query.

            Not present if the current response doesn't add anything to
            previously sent
            [AssistAnswer.replies][google.cloud.discoveryengine.v1beta.AssistAnswer.replies].

            Observe
            [AssistAnswer.state][google.cloud.discoveryengine.v1beta.AssistAnswer.state]
            to see if more parts are to be expected. While the state is
            ``IN_PROGRESS``, the
            [AssistAnswer.replies][google.cloud.discoveryengine.v1beta.AssistAnswer.replies]
            field in each response will contain replies (reply
            fragments) to be appended to the ones received in previous
            responses.
            [AssistAnswer.name][google.cloud.discoveryengine.v1beta.AssistAnswer.name]
            won't be filled.

            If the state is ``SUCCEEDED``, ``FAILED`` or ``SKIPPED``,
            the response is the last response and
            [AssistAnswer.name][google.cloud.discoveryengine.v1beta.AssistAnswer.name]
            will have a value.
        session_info (google.cloud.discoveryengine_v1beta.types.StreamAssistResponse.SessionInfo):
            Session information. Only included in the
            final StreamAssistResponse of the response
            stream.
        assist_token (str):
            A global unique ID that identifies the
            current pair of request and stream of responses.
            Used for feedback and support.
        invocation_tools (MutableSequence[str]):
            The tool names of the tools that were
            invoked.
        invoked_skills (MutableSequence[google.cloud.discoveryengine_v1beta.types.StreamAssistResponse.InvokedSkill]):
            The skills executed during the turn.
    """

    class SessionInfo(proto.Message):
        r"""Information about the session.

        Attributes:
            session (str):
                Name of the newly generated or continued session.

                Format:
                ``projects/{project}/locations/{location}/collections/{collection}/engines/{engine}/sessions/{session}``.
        """

        session: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class InvokedSkill(proto.Message):
        r"""Represents a skill used during the assist call.

        Attributes:
            name (str):
                The resource name of the skill.
            display_name (str):
                The display name of the skill.
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        display_name: str = proto.Field(
            proto.STRING,
            number=2,
        )

    answer: assist_answer.AssistAnswer = proto.Field(
        proto.MESSAGE,
        number=1,
        message=assist_answer.AssistAnswer,
    )
    session_info: SessionInfo = proto.Field(
        proto.MESSAGE,
        number=2,
        message=SessionInfo,
    )
    assist_token: str = proto.Field(
        proto.STRING,
        number=4,
    )
    invocation_tools: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=8,
    )
    invoked_skills: MutableSequence[InvokedSkill] = proto.RepeatedField(
        proto.MESSAGE,
        number=10,
        message=InvokedSkill,
    )


class CreateAssistantRequest(proto.Message):
    r"""Request for the
    [AssistantService.CreateAssistant][google.cloud.discoveryengine.v1beta.AssistantService.CreateAssistant]
    method.

    Attributes:
        parent (str):
            Required. The parent resource name. Format:
            ``projects/{project}/locations/{location}/collections/{collection}/engines/{engine}``
        assistant (google.cloud.discoveryengine_v1beta.types.Assistant):
            Required. The
            [Assistant][google.cloud.discoveryengine.v1beta.Assistant]
            to create.
        assistant_id (str):
            Required. The ID to use for the
            [Assistant][google.cloud.discoveryengine.v1beta.Assistant],
            which will become the final component of the
            [Assistant][google.cloud.discoveryengine.v1beta.Assistant]'s
            resource name.

            This field must conform to
            `RFC-1034 <https://tools.ietf.org/html/rfc1034>`__ with a
            length limit of 63 characters.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    assistant: gcd_assistant.Assistant = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcd_assistant.Assistant,
    )
    assistant_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteAssistantRequest(proto.Message):
    r"""Request message for the
    [AssistantService.DeleteAssistant][google.cloud.discoveryengine.v1beta.AssistantService.DeleteAssistant]
    method.

    Attributes:
        name (str):
            Required. Resource name of
            [Assistant][google.cloud.discoveryengine.v1beta.Assistant].
            Format:
            ``projects/{project}/locations/{location}/collections/{collection}/engines/{engine}/assistants/{assistant}``

            If the caller does not have permission to delete the
            [Assistant][google.cloud.discoveryengine.v1beta.Assistant],
            regardless of whether or not it exists, a PERMISSION_DENIED
            error is returned.

            If the
            [Assistant][google.cloud.discoveryengine.v1beta.Assistant]
            to delete does not exist, a NOT_FOUND error is returned.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetAssistantRequest(proto.Message):
    r"""Request message for the
    [AssistantService.GetAssistant][google.cloud.discoveryengine.v1beta.AssistantService.GetAssistant]
    method.

    Attributes:
        name (str):
            Required. Resource name of
            [Assistant][google.cloud.discoveryengine.v1beta.Assistant].
            Format:
            ``projects/{project}/locations/{location}/collections/{collection}/engines/{engine}/assistants/{assistant}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListAssistantsRequest(proto.Message):
    r"""Request message for the
    [AssistantService.ListAssistants][google.cloud.discoveryengine.v1beta.AssistantService.ListAssistants]
    method.

    Attributes:
        parent (str):
            Required. The parent resource name. Format:
            ``projects/{project}/locations/{location}/collections/{collection}/engines/{engine}``
        page_size (int):
            Maximum number of
            [Assistant][google.cloud.discoveryengine.v1beta.Assistant]s
            to return. If unspecified, defaults to 100. The maximum
            allowed value is 1000; anything above that will be coerced
            down to 1000.
        page_token (str):
            A page token
            [ListAssistantsResponse.next_page_token][google.cloud.discoveryengine.v1beta.ListAssistantsResponse.next_page_token],
            received from a previous
            [AssistantService.ListAssistants][google.cloud.discoveryengine.v1beta.AssistantService.ListAssistants]
            call. Provide this to retrieve the subsequent page.

            When paginating, all other parameters provided to
            [ListAssistants][google.cloud.discoveryengine.v1beta.AssistantService.ListAssistants]
            must match the call that provided the page token.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListAssistantsResponse(proto.Message):
    r"""Response message for the
    [AssistantService.ListAssistants][google.cloud.discoveryengine.v1beta.AssistantService.ListAssistants]
    method.

    Attributes:
        assistants (MutableSequence[google.cloud.discoveryengine_v1beta.types.Assistant]):
            All the customer's
            [Assistant][google.cloud.discoveryengine.v1beta.Assistant]s.
        next_page_token (str):
            A token that can be sent as
            [ListAssistantsRequest.page_token][google.cloud.discoveryengine.v1beta.ListAssistantsRequest.page_token]
            to retrieve the next page. If this field is omitted, there
            are no subsequent pages.
    """

    @property
    def raw_page(self):
        return self

    assistants: MutableSequence[gcd_assistant.Assistant] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcd_assistant.Assistant,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UpdateAssistantRequest(proto.Message):
    r"""Request message for the
    [AssistantService.UpdateAssistant][google.cloud.discoveryengine.v1beta.AssistantService.UpdateAssistant]
    method.

    Attributes:
        assistant (google.cloud.discoveryengine_v1beta.types.Assistant):
            Required. The
            [Assistant][google.cloud.discoveryengine.v1beta.Assistant]
            to update.

            The
            [Assistant][google.cloud.discoveryengine.v1beta.Assistant]'s
            ``name`` field is used to identify the
            [Assistant][google.cloud.discoveryengine.v1beta.Assistant]
            to update. Format:
            ``projects/{project}/locations/{location}/collections/{collection}/engines/{engine}/assistants/{assistant}``

            If the caller does not have permission to update the
            [Assistant][google.cloud.discoveryengine.v1beta.Assistant],
            regardless of whether or not it exists, a PERMISSION_DENIED
            error is returned.

            If the
            [Assistant][google.cloud.discoveryengine.v1beta.Assistant]
            to update does not exist, a NOT_FOUND error is returned.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The list of fields to update.
    """

    assistant: gcd_assistant.Assistant = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcd_assistant.Assistant,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
