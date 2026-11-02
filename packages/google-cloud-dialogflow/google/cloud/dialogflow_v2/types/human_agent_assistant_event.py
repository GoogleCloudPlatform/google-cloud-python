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

from google.cloud.dialogflow_v2.types import participant as gcd_participant

__protobuf__ = proto.module(
    package="google.cloud.dialogflow.v2",
    manifest={
        "HumanAgentAssistantEvent",
    },
)


class HumanAgentAssistantEvent(proto.Message):
    r"""Represents a notification sent to Cloud Pub/Sub subscribers
    for human agent assistant events in a specific conversation.

    Attributes:
        conversation (str):
            The conversation this notification refers to. Format:
            ``projects/<Project ID>/conversations/<Conversation ID>``.
        participant (str):
            The participant that the suggestion is compiled for. Format:
            ``projects/<Project ID>/conversations/<Conversation ID>/participants/<Participant ID>``.
            It will not be set in legacy workflow.
        suggestion_results (MutableSequence[google.cloud.dialogflow_v2.types.SuggestionResult]):
            The suggestion results payload that this
            notification refers to.
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
