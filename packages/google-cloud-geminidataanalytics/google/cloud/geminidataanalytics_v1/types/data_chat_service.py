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

import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.geminidataanalytics_v1.types import context, datasource
from google.cloud.geminidataanalytics_v1.types import credentials as gcg_credentials

__protobuf__ = proto.module(
    package="google.cloud.geminidataanalytics.v1",
    manifest={
        "ListMessagesRequest",
        "ListMessagesResponse",
        "StorageMessage",
        "ChatRequest",
        "DataAgentContext",
        "ConversationReference",
        "ClientManagedResourceContext",
        "Message",
        "LookerSettings",
        "UserMessage",
        "SystemMessage",
        "TextMessage",
        "SchemaMessage",
        "SchemaQuery",
        "SchemaResult",
        "DataMessage",
        "DataQuery",
        "DataResult",
        "BigQueryJob",
        "AnalysisMessage",
        "AnalysisQuery",
        "AnalysisEvent",
        "ChartMessage",
        "ChartQuery",
        "ChartResult",
        "ErrorMessage",
        "ExampleQueries",
        "Blob",
    },
)


class ListMessagesRequest(proto.Message):
    r"""Request for listing chat messages based on parent and
    conversation_id.

    Attributes:
        parent (str):
            Required. The conversation to list messages under. Format:
            ``projects/{project}/locations/{location}/conversations/{conversation_id}``
        page_size (int):
            Optional. Requested page size. Server may return fewer items
            than requested. The max page size is ``100``. All larger
            page sizes will be coerced to ``100``. If unspecified,
            server will pick ``50`` as an appropriate default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. Filtering results. See
            `AIP-160 <https://google.aip.dev/160>`__ for syntax.

            ListMessages allows filtering by:

            - create_time (e.g.,
              ``createTime > "2025-01-28T06:51:56-08:00"``)
            - update_time
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListMessagesResponse(proto.Message):
    r"""Response for listing chat messages.

    Attributes:
        messages (MutableSequence[google.cloud.geminidataanalytics_v1.types.StorageMessage]):
            The list of chat messages.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
    """

    @property
    def raw_page(self):
        return self

    messages: MutableSequence["StorageMessage"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="StorageMessage",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class StorageMessage(proto.Message):
    r"""A stored message containing user message or system message.

    Attributes:
        message_id (str):
            The unique resource name of a chat message.
        message (google.cloud.geminidataanalytics_v1.types.Message):
            The message content.
    """

    message_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    message: "Message" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Message",
    )


class ChatRequest(proto.Message):
    r"""Request for Chat.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        inline_context (google.cloud.geminidataanalytics_v1.types.Context):
            Optional. Inline context for the chat
            request. Use this to chat statelessly (without
            managed conversation persistence and without an
            Agent) by passing all context inline.

            This field is a member of `oneof`_ ``context_provider``.
        conversation_reference (google.cloud.geminidataanalytics_v1.types.ConversationReference):
            Optional. Reference to a persisted
            conversation and agent context. Use this to chat
            with an Agent using managed conversation
            persistence.

            This field is a member of `oneof`_ ``context_provider``.
        data_agent_context (google.cloud.geminidataanalytics_v1.types.DataAgentContext):
            Optional. Context for the chat request. Use
            this to chat with an Agent statelessly, without
            managed conversation persistence.

            This field is a member of `oneof`_ ``context_provider``.
        client_managed_resource_context (google.cloud.geminidataanalytics_v1.types.ClientManagedResourceContext):
            Optional. Context with client managed
            resources. Some clients may not use GDA managed
            resources including conversations and agents,
            instead they create and manage their own
            conversations and agents resources.

            This field is a member of `oneof`_ ``context_provider``.
        looker_settings (google.cloud.geminidataanalytics_v1.types.LookerSettings):
            Optional. Looker specific settings.

            This field is a member of `oneof`_ ``datasource_settings``.
        parent (str):
            Required. The parent value for chat request. Pattern:
            ``projects/{project}/locations/{location}``
        messages (MutableSequence[google.cloud.geminidataanalytics_v1.types.Message]):
            Required. Content of current conversation.
        credentials (google.cloud.geminidataanalytics_v1.types.Credentials):
            Optional. The credentials to use when calling the data
            source(s) specified in the context.

            This field can be used to provide credentials for various
            data sources. For example, when connecting to Looker, it
            currently supports both OAuth token and API key-based
            credentials, as described in `Authentication with an
            SDK <https://cloud.google.com/looker/docs/api-auth#authentication_with_an_sdk>`__.
        thinking_mode (google.cloud.geminidataanalytics_v1.types.ChatRequest.ThinkingMode):
            Optional. The thinking mode to use for the agent loop.
            Defaults to THINKING_MODE_UNSPECIFIED if not specified.
        model (google.cloud.geminidataanalytics_v1.types.ChatRequest.Model):
            Optional. The model to use for the agent loop
            when processing the request. This setting only
            has an effect when context.options.model is not
            set.
    """

    class ThinkingMode(proto.Enum):
        r"""Mode of thinking for the agent.

        Values:
            THINKING_MODE_UNSPECIFIED (0):
                The default value. For BigQuery and Looker
                data sources, the agent uses FAST. For all other
                data sources, the agent uses THINKING.
            FAST (1):
                Fast mode, answers quickly.
            THINKING (2):
                Thinking mode, solves complex problems.
        """

        THINKING_MODE_UNSPECIFIED = 0
        FAST = 1
        THINKING = 2

    class Model(proto.Enum):
        r"""Model selection for the agent for BigQuery users.

        Values:
            MODEL_UNSPECIFIED (0):
                No model specified. Either preview or non
                preview model can be used.
            LATEST_GA_MODEL (1):
                Use the most up-to-date non-preview model.
                This may constrain certain request level
                settings.
        """

        MODEL_UNSPECIFIED = 0
        LATEST_GA_MODEL = 1

    inline_context: context.Context = proto.Field(
        proto.MESSAGE,
        number=101,
        oneof="context_provider",
        message=context.Context,
    )
    conversation_reference: "ConversationReference" = proto.Field(
        proto.MESSAGE,
        number=103,
        oneof="context_provider",
        message="ConversationReference",
    )
    data_agent_context: "DataAgentContext" = proto.Field(
        proto.MESSAGE,
        number=104,
        oneof="context_provider",
        message="DataAgentContext",
    )
    client_managed_resource_context: "ClientManagedResourceContext" = proto.Field(
        proto.MESSAGE,
        number=105,
        oneof="context_provider",
        message="ClientManagedResourceContext",
    )
    looker_settings: "LookerSettings" = proto.Field(
        proto.MESSAGE,
        number=13,
        oneof="datasource_settings",
        message="LookerSettings",
    )
    parent: str = proto.Field(
        proto.STRING,
        number=3,
    )
    messages: MutableSequence["Message"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="Message",
    )
    credentials: gcg_credentials.Credentials = proto.Field(
        proto.MESSAGE,
        number=7,
        message=gcg_credentials.Credentials,
    )
    thinking_mode: ThinkingMode = proto.Field(
        proto.ENUM,
        number=9,
        enum=ThinkingMode,
    )
    model: Model = proto.Field(
        proto.ENUM,
        number=11,
        enum=Model,
    )


class DataAgentContext(proto.Message):
    r"""Context for the chat request using a data agent.

    Attributes:
        data_agent (str):
            Required. The name of the data agent
            resource.
        context_version (google.cloud.geminidataanalytics_v1.types.DataAgentContext.ContextVersion):
            Optional. Version of context to be used by
            DCS (e.g. STAGING, PUBLISHED)
    """

    class ContextVersion(proto.Enum):
        r"""List of context versions supported by DCS.
        There are two versions of context. This is to maintain
        versioning for the data agent.

        Values:
            CONTEXT_VERSION_UNSPECIFIED (0):
                Unspecified or unrecognized.
            STAGING (1):
                Using this version, DCS will use the latest
                staging context for the data agent.
            PUBLISHED (2):
                Using this version, DCS will use the latest
                published context for the data agent.
        """

        CONTEXT_VERSION_UNSPECIFIED = 0
        STAGING = 1
        PUBLISHED = 2

    data_agent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    context_version: ContextVersion = proto.Field(
        proto.ENUM,
        number=3,
        enum=ContextVersion,
    )


class ConversationReference(proto.Message):
    r"""Reference to a persisted conversation and agent context.

    Attributes:
        conversation (str):
            Required. Name of the conversation resource. Format:
            ``projects/{project}/locations/{location}/conversations/{conversation_id}``
        data_agent_context (google.cloud.geminidataanalytics_v1.types.DataAgentContext):
            Required. Context for the chat request using
            a data agent.
    """

    conversation: str = proto.Field(
        proto.STRING,
        number=1,
    )
    data_agent_context: "DataAgentContext" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="DataAgentContext",
    )


class ClientManagedResourceContext(proto.Message):
    r"""Context with client managed resources.
    Some clients may not use GDA managed resources including
    conversations and agents, instead they create and manage their
    own conversations and agents resources.

    Attributes:
        inline_context (google.cloud.geminidataanalytics_v1.types.Context):
            Required. Context for the chat request. Use
            this to chat without GDA API managed
            conversation and agent persistence by passing
            all context inline.
        conversation_id (str):
            Optional. The client managed conversation id.
        agent_id (str):
            Optional. The client managed agent id.
    """

    inline_context: context.Context = proto.Field(
        proto.MESSAGE,
        number=1,
        message=context.Context,
    )
    conversation_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    agent_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class Message(proto.Message):
    r"""A message from an interaction between the user and the
    system.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        user_message (google.cloud.geminidataanalytics_v1.types.UserMessage):
            A message from the user that is interacting
            with the system.

            This field is a member of `oneof`_ ``kind``.
        system_message (google.cloud.geminidataanalytics_v1.types.SystemMessage):
            A message from the system in response to the
            user.

            This field is a member of `oneof`_ ``kind``.
        timestamp (google.protobuf.timestamp_pb2.Timestamp):
            Output only. For user messages, this is the
            time at which the system received the message.
            For system messages, this is the time at which
            the system generated the message.
        message_id (str):
            Optional. unique id of the message in the
            conversation for persistence.
    """

    user_message: "UserMessage" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="kind",
        message="UserMessage",
    )
    system_message: "SystemMessage" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="kind",
        message="SystemMessage",
    )
    timestamp: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    message_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class LookerSettings(proto.Message):
    r"""Message to hold Looker specific custom settings.

    Attributes:
        enable_dev_mode (bool):
            Optional. Whether to operate in Looker's
            Development Mode. If true, the API session will
            be switched to the "dev" workspace, allowing
            interaction with LookML changes in the user's
            development branch. If false or unset, the
            session remains in the default state (Production
            Mode).
            See
            https://cloud.google.com/looker/docs/dev-mode-prod-mode.
    """

    enable_dev_mode: bool = proto.Field(
        proto.BOOL,
        number=1,
    )


class UserMessage(proto.Message):
    r"""A message from the user that is interacting with the system.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        text (str):
            Text should use this field instead of blob.

            This field is a member of `oneof`_ ``kind``.
    """

    text: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="kind",
    )


class SystemMessage(proto.Message):
    r"""A message from the system in response to the user. This
    message can also be a message from the user as historical
    context for multi-turn conversations with the system.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        text (google.cloud.geminidataanalytics_v1.types.TextMessage):
            A direct natural language response to the
            user message.

            This field is a member of `oneof`_ ``kind``.
        schema (google.cloud.geminidataanalytics_v1.types.SchemaMessage):
            A message produced during schema resolution.

            This field is a member of `oneof`_ ``kind``.
        data (google.cloud.geminidataanalytics_v1.types.DataMessage):
            A message produced during data retrieval.

            This field is a member of `oneof`_ ``kind``.
        analysis (google.cloud.geminidataanalytics_v1.types.AnalysisMessage):
            A message produced during analysis.

            This field is a member of `oneof`_ ``kind``.
        chart (google.cloud.geminidataanalytics_v1.types.ChartMessage):
            A message produced during chart generation.

            This field is a member of `oneof`_ ``kind``.
        error (google.cloud.geminidataanalytics_v1.types.ErrorMessage):
            An error message.

            This field is a member of `oneof`_ ``kind``.
        example_queries (google.cloud.geminidataanalytics_v1.types.ExampleQueries):
            Optional. A message containing example
            queries.

            This field is a member of `oneof`_ ``kind``.
        group_id (int):
            Identifies the group that the event belongs
            to. Similar events are deemed to be logically
            relevant to each other and should be shown
            together in the UI.

            This field is a member of `oneof`_ ``_group_id``.
        citation (google.cloud.geminidataanalytics_v1.types.Citation):
            Output only. Citation information for the
            system message.
    """

    text: "TextMessage" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="kind",
        message="TextMessage",
    )
    schema: "SchemaMessage" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="kind",
        message="SchemaMessage",
    )
    data: "DataMessage" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="kind",
        message="DataMessage",
    )
    analysis: "AnalysisMessage" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="kind",
        message="AnalysisMessage",
    )
    chart: "ChartMessage" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="kind",
        message="ChartMessage",
    )
    error: "ErrorMessage" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="kind",
        message="ErrorMessage",
    )
    example_queries: "ExampleQueries" = proto.Field(
        proto.MESSAGE,
        number=13,
        oneof="kind",
        message="ExampleQueries",
    )
    group_id: int = proto.Field(
        proto.INT32,
        number=12,
        optional=True,
    )
    citation: context.Citation = proto.Field(
        proto.MESSAGE,
        number=15,
        message=context.Citation,
    )


class TextMessage(proto.Message):
    r"""A multi-part text message.

    Attributes:
        parts (MutableSequence[str]):
            Optional. The parts of the message.
        text_type (google.cloud.geminidataanalytics_v1.types.TextMessage.TextType):
            Optional. The type of the text message.
        thought_signature (bytes):
            Optional. An opaque signature for a thought
            so it can be reused in subsequent requests.
    """

    class TextType(proto.Enum):
        r"""The type of the text message.

        Values:
            TEXT_TYPE_UNSPECIFIED (0):
                The default text type.
            FINAL_RESPONSE (1):
                The text is a final response to the user
                question.
            THOUGHT (2):
                The text is a thought from the model.
            PROGRESS (3):
                The text is an informational message about the agent's
                progress, such as a tool being invoked. This is distinct
                from the agent's internal thought process (``THOUGHT``) and
                the final answer to the user (``FINAL_RESPONSE``). These
                messages provide insight into the agent's actions.
            FOLLOWUP_QUESTIONS (4):
                The text is a list of follow-up questions
                suggested. Each item in parts is a follow-up
                question.
        """

        TEXT_TYPE_UNSPECIFIED = 0
        FINAL_RESPONSE = 1
        THOUGHT = 2
        PROGRESS = 3
        FOLLOWUP_QUESTIONS = 4

    parts: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    text_type: TextType = proto.Field(
        proto.ENUM,
        number=2,
        enum=TextType,
    )
    thought_signature: bytes = proto.Field(
        proto.BYTES,
        number=3,
    )


class SchemaMessage(proto.Message):
    r"""A message produced during schema resolution.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        query (google.cloud.geminidataanalytics_v1.types.SchemaQuery):
            A schema resolution query.

            This field is a member of `oneof`_ ``kind``.
        result (google.cloud.geminidataanalytics_v1.types.SchemaResult):
            The result of a schema resolution query.

            This field is a member of `oneof`_ ``kind``.
    """

    query: "SchemaQuery" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="kind",
        message="SchemaQuery",
    )
    result: "SchemaResult" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="kind",
        message="SchemaResult",
    )


class SchemaQuery(proto.Message):
    r"""A query for resolving the schema relevant to the posed
    question.

    Attributes:
        question (str):
            Optional. The question to send to the system
            for schema resolution.
    """

    question: str = proto.Field(
        proto.STRING,
        number=1,
    )


class SchemaResult(proto.Message):
    r"""The result of schema resolution.

    Attributes:
        datasources (MutableSequence[google.cloud.geminidataanalytics_v1.types.Datasource]):
            Optional. The datasources used to resolve the
            schema query.
    """

    datasources: MutableSequence[datasource.Datasource] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=datasource.Datasource,
    )


class DataMessage(proto.Message):
    r"""A message produced during data retrieval.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        query (google.cloud.geminidataanalytics_v1.types.DataQuery):
            A data retrieval query.

            This field is a member of `oneof`_ ``kind``.
        generated_sql (str):
            SQL generated by the system to retrieve data.

            This field is a member of `oneof`_ ``kind``.
        result (google.cloud.geminidataanalytics_v1.types.DataResult):
            Retrieved data.

            This field is a member of `oneof`_ ``kind``.
        big_query_job (google.cloud.geminidataanalytics_v1.types.BigQueryJob):
            A BigQuery job executed by the system to
            retrieve data.

            This field is a member of `oneof`_ ``kind``.
        matched_query (google.cloud.geminidataanalytics_v1.types.MatchedQuery):
            A pre-existing query that was matched to
            retrieve data.

            This field is a member of `oneof`_ ``kind``.
    """

    query: "DataQuery" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="kind",
        message="DataQuery",
    )
    generated_sql: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="kind",
    )
    result: "DataResult" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="kind",
        message="DataResult",
    )
    big_query_job: "BigQueryJob" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="kind",
        message="BigQueryJob",
    )
    matched_query: context.MatchedQuery = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="kind",
        message=context.MatchedQuery,
    )


class DataQuery(proto.Message):
    r"""A query for retrieving data.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        looker (google.cloud.geminidataanalytics_v1.types.LookerQuery):
            Optional. A query for retrieving data from a
            Looker explore.

            This field is a member of `oneof`_ ``query_type``.
        question (str):
            Optional. A natural language question to
            answer.
        name (str):
            Optional. A snake-case name for the query that reflects its
            intent. It is used to name the corresponding data result, so
            that it can be referenced in later steps.

            - Example: "total_sales_by_product"
            - Example: "sales_for_product_12345".
        datasources (MutableSequence[google.cloud.geminidataanalytics_v1.types.Datasource]):
            Optional. The datasources available to answer
            the question.
    """

    looker: context.LookerQuery = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="query_type",
        message=context.LookerQuery,
    )
    question: str = proto.Field(
        proto.STRING,
        number=1,
    )
    name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    datasources: MutableSequence[datasource.Datasource] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=datasource.Datasource,
    )


class DataResult(proto.Message):
    r"""Retrieved data.

    Attributes:
        name (str):
            Optional. A snake-case name for the data result that
            reflects its contents. The name is used to pass the result
            around by reference, and serves as a signal about its
            meaning.

            - Example: "total_sales_by_product"
            - Example: "sales_for_product_12345".
        schema (google.cloud.geminidataanalytics_v1.types.Schema):
            Optional. The schema of the data.
        data (MutableSequence[google.protobuf.struct_pb2.Struct]):
            Optional. The content of the data. Each row
            is a struct that matches the schema. Simple
            values are represented as strings, while nested
            structures are represented as lists or structs.
        formatted_data (MutableSequence[google.protobuf.struct_pb2.Struct]):
            Optional. Formatted representation of the data, when
            applicable. Each row is a struct that directly corresponds
            to the row at the same index within the ``data`` field. Its
            values are string representations of the original data,
            formatted according to data source specifications (e.g.,
            "$1,234.56" for currency). Columns without formatting will
            default to their raw value representation. If no columns
            have formatting rules, this field will be empty.
    """

    name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    schema: datasource.Schema = proto.Field(
        proto.MESSAGE,
        number=5,
        message=datasource.Schema,
    )
    data: MutableSequence[struct_pb2.Struct] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=struct_pb2.Struct,
    )
    formatted_data: MutableSequence[struct_pb2.Struct] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message=struct_pb2.Struct,
    )


class BigQueryJob(proto.Message):
    r"""A BigQuery job executed by the system.

    Attributes:
        project_id (str):
            Required. The project that the job belongs to.

            See
            `JobReference <https://cloud.google.com/bigquery/docs/reference/rest/v2/JobReference>`__.
        job_id (str):
            Required. The ID of the job.

            See
            `JobReference <https://cloud.google.com/bigquery/docs/reference/rest/v2/JobReference>`__.
        location (str):
            Optional. The location of the job.

            See
            `JobReference <https://cloud.google.com/bigquery/docs/reference/rest/v2/JobReference>`__.
        destination_table (google.cloud.geminidataanalytics_v1.types.BigQueryTableReference):
            Optional. A reference to the destination table of the job's
            query results.

            See
            `JobConfigurationQuery <https://cloud.google.com/bigquery/docs/reference/rest/v2/Job#jobconfigurationquery>`__.
        schema (google.cloud.geminidataanalytics_v1.types.Schema):
            Optional. The schema of the job's query results.

            See
            `JobStatistics2 <https://cloud.google.com/bigquery/docs/reference/rest/v2/Job#jobstatistics2>`__.
    """

    project_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    job_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    location: str = proto.Field(
        proto.STRING,
        number=5,
    )
    destination_table: datasource.BigQueryTableReference = proto.Field(
        proto.MESSAGE,
        number=3,
        message=datasource.BigQueryTableReference,
    )
    schema: datasource.Schema = proto.Field(
        proto.MESSAGE,
        number=7,
        message=datasource.Schema,
    )


class AnalysisMessage(proto.Message):
    r"""A message produced during analysis.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        query (google.cloud.geminidataanalytics_v1.types.AnalysisQuery):
            An analysis query.

            This field is a member of `oneof`_ ``kind``.
        progress_event (google.cloud.geminidataanalytics_v1.types.AnalysisEvent):
            An event indicating the progress of the
            analysis.

            This field is a member of `oneof`_ ``kind``.
    """

    query: "AnalysisQuery" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="kind",
        message="AnalysisQuery",
    )
    progress_event: "AnalysisEvent" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="kind",
        message="AnalysisEvent",
    )


class AnalysisQuery(proto.Message):
    r"""A query for performing an analysis.

    Attributes:
        question (str):
            Optional. An analysis question to help answer
            the user's original question.
        data_result_names (MutableSequence[str]):
            Optional. The names of previously retrieved
            data results to analyze.
    """

    question: str = proto.Field(
        proto.STRING,
        number=1,
    )
    data_result_names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class AnalysisEvent(proto.Message):
    r"""An event indicating the progress of an analysis.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        planner_reasoning (str):
            Python codegen planner's reasoning.

            This field is a member of `oneof`_ ``kind``.
        coder_instruction (str):
            Instructions issued for code generation.

            This field is a member of `oneof`_ ``kind``.
        code (str):
            Generated code.

            This field is a member of `oneof`_ ``kind``.
        execution_output (str):
            Output from code execution.

            This field is a member of `oneof`_ ``kind``.
        execution_error (str):
            An error from code execution.

            This field is a member of `oneof`_ ``kind``.
        result_vega_chart_json (str):
            Result as Vega chart JSON string.

            This field is a member of `oneof`_ ``kind``.
        result_natural_language (str):
            Result as NL string.

            This field is a member of `oneof`_ ``kind``.
        result_csv_data (str):
            Result as CSV string.

            This field is a member of `oneof`_ ``kind``.
        result_reference_data (str):
            Result as a reference to a data source.

            This field is a member of `oneof`_ ``kind``.
        error (str):
            A generic error message.

            This field is a member of `oneof`_ ``kind``.
    """

    planner_reasoning: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="kind",
    )
    coder_instruction: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="kind",
    )
    code: str = proto.Field(
        proto.STRING,
        number=4,
        oneof="kind",
    )
    execution_output: str = proto.Field(
        proto.STRING,
        number=5,
        oneof="kind",
    )
    execution_error: str = proto.Field(
        proto.STRING,
        number=6,
        oneof="kind",
    )
    result_vega_chart_json: str = proto.Field(
        proto.STRING,
        number=7,
        oneof="kind",
    )
    result_natural_language: str = proto.Field(
        proto.STRING,
        number=8,
        oneof="kind",
    )
    result_csv_data: str = proto.Field(
        proto.STRING,
        number=9,
        oneof="kind",
    )
    result_reference_data: str = proto.Field(
        proto.STRING,
        number=10,
        oneof="kind",
    )
    error: str = proto.Field(
        proto.STRING,
        number=11,
        oneof="kind",
    )


class ChartMessage(proto.Message):
    r"""A message produced during chart generation.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        query (google.cloud.geminidataanalytics_v1.types.ChartQuery):
            A query for generating a chart.

            This field is a member of `oneof`_ ``kind``.
        result (google.cloud.geminidataanalytics_v1.types.ChartResult):
            The result of a chart generation query.

            This field is a member of `oneof`_ ``kind``.
    """

    query: "ChartQuery" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="kind",
        message="ChartQuery",
    )
    result: "ChartResult" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="kind",
        message="ChartResult",
    )


class ChartQuery(proto.Message):
    r"""A query for generating a chart.

    Attributes:
        instructions (str):
            Optional. Natural language instructions for
            generating the chart.
        data_result_name (str):
            Optional. The name of a previously retrieved
            data result to use in the chart.
    """

    instructions: str = proto.Field(
        proto.STRING,
        number=1,
    )
    data_result_name: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ChartResult(proto.Message):
    r"""The result of a chart generation query.

    Attributes:
        vega_config (google.protobuf.struct_pb2.Struct):
            Optional. A generated Vega chart config.
            See https://vega.github.io/vega/docs/config/
        image (google.cloud.geminidataanalytics_v1.types.Blob):
            Optional. A rendering of the chart if this
            was requested in the context.
    """

    vega_config: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=2,
        message=struct_pb2.Struct,
    )
    image: "Blob" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Blob",
    )


class ErrorMessage(proto.Message):
    r"""An error message from a tool call. This message is used to represent
    an error that occurred while an agent was trying to use a tool. It's
    important to note that not all errors are terminal. Many are
    recoverable, and the agent may use the information from this error
    message to self-correct and retry the tool call or try a different
    approach.

    For example, if a data query fails, the agent might receive an
    ``ErrorMessage``, analyze it, and then generate a corrected query.

    Clients should be cautious about interpreting this message as a
    definitive failure. It can be part of the agent's normal, iterative
    process of completing a task. Surfacing these errors directly to
    end-users without context (e.g., as a "hard failure") may be
    misleading.

    Attributes:
        text (str):
            Output only. The text of the error.
    """

    text: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ExampleQueries(proto.Message):
    r"""A message containing derived and authored example queries.

    Attributes:
        example_queries (MutableSequence[google.cloud.geminidataanalytics_v1.types.ExampleQuery]):
            Optional. A list of derived and authored
            example queries, providing examples of relevant
            and commonly used SQL queries and their
            corresponding natural language queries
            optionally present. Currently only used for
            BigQuery data sources.
    """

    example_queries: MutableSequence[context.ExampleQuery] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=context.ExampleQuery,
    )


class Blob(proto.Message):
    r"""A blob of data with a MIME type.

    Attributes:
        mime_type (str):
            Required. The IANA standard MIME type of the
            message data.
        data (bytes):
            Required. The data represented as bytes.
    """

    mime_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    data: bytes = proto.Field(
        proto.BYTES,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
