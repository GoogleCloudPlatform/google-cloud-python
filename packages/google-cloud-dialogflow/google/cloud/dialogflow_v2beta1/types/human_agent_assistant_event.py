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

import proto  # type: ignore

from google.cloud.dialogflow_v2beta1.types import participant as gcd_participant

__protobuf__ = proto.module(
    package="google.cloud.dialogflow.v2beta1",
    manifest={
        "HumanAgentAssistantEvent",
    },
)


class HumanAgentAssistantEvent(proto.Message):
    r"""Output only. Represents a notification sent to Pub/Sub
    subscribers for agent assistant events in a specific
    conversation.

    Attributes:
        conversation (str):
            The conversation this notification refers to. Format:
            ``projects/<Project ID>/conversations/<Conversation ID>``.
        participant (str):
            The participant that the suggestion is compiled for. And
            This field is used to call
            [Participants.ListSuggestions][google.cloud.dialogflow.v2beta1.Participants.ListSuggestions]
            API. Format:
            ``projects/<Project ID>/conversations/<Conversation ID>/participants/<Participant ID>``.
            It will not be set in legacy workflow.
            [HumanAgentAssistantConfig.name][google.cloud.dialogflow.v2beta1.HumanAgentAssistantConfig.name]
            for more information.
        suggestion_results (MutableSequence[google.cloud.dialogflow_v2beta1.types.SuggestionResult]):
            The suggestion results payload that this notification refers
            to. It will only be set when
            [HumanAgentAssistantConfig.SuggestionConfig.group_suggestion_responses][google.cloud.dialogflow.v2beta1.HumanAgentAssistantConfig.SuggestionConfig.group_suggestion_responses]
            sets to true.
    """

    conversation: str = proto.Field(
        proto.STRING,
        number=1,
    )
    participant: str = proto.Field(
        proto.STRING,
        number=3,
    )
    suggestion_results: MutableSequence[gcd_participant.SuggestionResult] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=5,
            message=gcd_participant.SuggestionResult,
        )
    )


__all__ = tuple(sorted(__protobuf__.manifest))
