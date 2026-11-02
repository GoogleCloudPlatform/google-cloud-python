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

import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.ces_v1beta.types import common, example

__protobuf__ = proto.module(
    package="google.cloud.ces.v1beta",
    manifest={
        "Conversation",
    },
)


class Conversation(proto.Message):
    r"""A conversation represents an interaction between an end user
    and the CES app.

    Attributes:
        name (str):
            Identifier. The unique identifier of the conversation.
            Format:
            ``projects/{project}/locations/{location}/apps/{app}/conversations/{conversation}``
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the conversation
            was created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the conversation
            was completed.
        turns (MutableSequence[google.cloud.ces_v1beta.types.Conversation.Turn]):
            Required. The turns in the conversation.
        turn_count (int):
            Output only. The number of turns in the
            conversation.
        channel_type (google.cloud.ces_v1beta.types.Conversation.ChannelType):
            DEPRECATED. Please use
            [input_types][google.cloud.ces.v1beta.Conversation.input_types]
            instead.
        source (google.cloud.ces_v1beta.types.Conversation.Source):
            Output only. Indicate the source of the
            conversation.
        input_types (MutableSequence[google.cloud.ces_v1beta.types.Conversation.InputType]):
            Output only. The input types of the
            conversation.
        entry_agent (str):
            Output only. The agent that initially handles the
            conversation. If not specified, the conversation is handled
            by the root agent. Format:
            ``projects/{project}/locations/{location}/apps/{app}/agents/{agent}``
        deployment (str):
            Output only. The deployment of the app used for processing
            the conversation. Format:
            ``projects/{project}/locations/{location}/apps/{app}/deployments/{deployment}``
        app_version (str):
            Output only. The version of the app used for processing the
            conversation. Format:
            ``projects/{project}/locations/{location}/apps/{app}/versions/{version}``
        language_code (str):
            Output only. The language code of the
            conversation.
        messages (MutableSequence[google.cloud.ces_v1beta.types.Message]):
            Deprecated. Use turns instead.
    """

    class ChannelType(proto.Enum):
        r"""The channel type of the conversation.

        Values:
            CHANNEL_TYPE_UNSPECIFIED (0):
                Unspecified channel type.
            TEXT (1):
                The conversation only contains text messages
                between the end user and the agent.
            AUDIO (2):
                The conversation contains audio messages
                between the end user and the agent.
            MULTIMODAL (3):
                The conversation multi-modal messages (e.g.
                image) between the end user and the agent.
        """

        CHANNEL_TYPE_UNSPECIFIED = 0
        TEXT = 1
        AUDIO = 2
        MULTIMODAL = 3

    class Source(proto.Enum):
        r"""The source of the conversation.

        Values:
            SOURCE_UNSPECIFIED (0):
                Unspecified source.
            LIVE (1):
                The conversation is from the live end user.
            SIMULATOR (2):
                The conversation is from the simulator.
            EVAL (3):
                The conversation is from the evaluation.
            AGENT_TOOL (4):
                The conversation is from an agent tool. Agent
                tool runs the agent in a separate session, which
                is persisted for testing and debugging purposes.
        """

        SOURCE_UNSPECIFIED = 0
        LIVE = 1
        SIMULATOR = 2
        EVAL = 3
        AGENT_TOOL = 4

    class InputType(proto.Enum):
        r"""Type of the input message.

        Values:
            INPUT_TYPE_UNSPECIFIED (0):
                Unspecified input type.
            INPUT_TYPE_TEXT (1):
                Text input.
            INPUT_TYPE_EVENT (7):
                Event input.
            INPUT_TYPE_AUDIO (2):
                Audio input.
            INPUT_TYPE_IMAGE (3):
                Image input.
            INPUT_TYPE_BLOB (4):
                Blob input.
            INPUT_TYPE_TOOL_RESPONSE (5):
                Client function tool response input.
            INPUT_TYPE_VARIABLES (6):
                Variables input.
        """

        INPUT_TYPE_UNSPECIFIED = 0
        INPUT_TYPE_TEXT = 1
        INPUT_TYPE_EVENT = 7
        INPUT_TYPE_AUDIO = 2
        INPUT_TYPE_IMAGE = 3
        INPUT_TYPE_BLOB = 4
        INPUT_TYPE_TOOL_RESPONSE = 5
        INPUT_TYPE_VARIABLES = 6

    class Turn(proto.Message):
        r"""All information about a single turn in the conversation.

        Attributes:
            messages (MutableSequence[google.cloud.ces_v1beta.types.Message]):
                Optional. List of messages in the
                conversation turn, including user input, agent
                responses and intermediate events during the
                processing.
            root_span (google.cloud.ces_v1beta.types.Span):
                Optional. The root span of the action
                processing.
        """

        messages: MutableSequence[example.Message] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=example.Message,
        )
        root_span: common.Span = proto.Field(
            proto.MESSAGE,
            number=2,
            message=common.Span,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    turns: MutableSequence[Turn] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message=Turn,
    )
    turn_count: int = proto.Field(
        proto.INT32,
        number=7,
    )
    channel_type: ChannelType = proto.Field(
        proto.ENUM,
        number=8,
        enum=ChannelType,
    )
    source: Source = proto.Field(
        proto.ENUM,
        number=9,
        enum=Source,
    )
    input_types: MutableSequence[InputType] = proto.RepeatedField(
        proto.ENUM,
        number=10,
        enum=InputType,
    )
    entry_agent: str = proto.Field(
        proto.STRING,
        number=11,
    )
    deployment: str = proto.Field(
        proto.STRING,
        number=12,
    )
    app_version: str = proto.Field(
        proto.STRING,
        number=13,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=14,
    )
    messages: MutableSequence[example.Message] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=example.Message,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
