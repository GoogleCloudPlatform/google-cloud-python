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

__protobuf__ = proto.module(
    package="google.cloud.dialogflow.cx.v3",
    manifest={
        "ValidationMessage",
        "ResourceName",
    },
)


class ValidationMessage(proto.Message):
    r"""Agent/flow validation message.

    Attributes:
        resource_type (google.cloud.dialogflowcx_v3.types.ValidationMessage.ResourceType):
            The type of the resources where the message
            is found.
        resources (MutableSequence[str]):
            The names of the resources where the message
            is found.
        resource_names (MutableSequence[google.cloud.dialogflowcx_v3.types.ResourceName]):
            The resource names of the resources where the
            message is found.
        severity (google.cloud.dialogflowcx_v3.types.ValidationMessage.Severity):
            Indicates the severity of the message.
        detail (str):
            The message detail.
    """

    class ResourceType(proto.Enum):
        r"""Resource types.

        Values:
            RESOURCE_TYPE_UNSPECIFIED (0):
                Unspecified.
            AGENT (1):
                Agent.
            INTENT (2):
                Intent.
            INTENT_TRAINING_PHRASE (8):
                Intent training phrase.
            INTENT_PARAMETER (9):
                Intent parameter.
            INTENTS (10):
                Multiple intents.
            INTENT_TRAINING_PHRASES (11):
                Multiple training phrases.
            ENTITY_TYPE (3):
                Entity type.
            ENTITY_TYPES (12):
                Multiple entity types.
            WEBHOOK (4):
                Webhook.
            FLOW (5):
                Flow.
            PAGE (6):
                Page.
            PAGES (13):
                Multiple pages.
            TRANSITION_ROUTE_GROUP (7):
                Transition route group.
            AGENT_TRANSITION_ROUTE_GROUP (14):
                Agent transition route group.
        """

        RESOURCE_TYPE_UNSPECIFIED = 0
        AGENT = 1
        INTENT = 2
        INTENT_TRAINING_PHRASE = 8
        INTENT_PARAMETER = 9
        INTENTS = 10
        INTENT_TRAINING_PHRASES = 11
        ENTITY_TYPE = 3
        ENTITY_TYPES = 12
        WEBHOOK = 4
        FLOW = 5
        PAGE = 6
        PAGES = 13
        TRANSITION_ROUTE_GROUP = 7
        AGENT_TRANSITION_ROUTE_GROUP = 14

    class Severity(proto.Enum):
        r"""Severity level.

        Values:
            SEVERITY_UNSPECIFIED (0):
                Unspecified.
            INFO (1):
                The agent doesn't follow Dialogflow best
                practices.
            WARNING (2):
                The agent may not behave as expected.
            ERROR (3):
                The agent may experience failures.
        """

        SEVERITY_UNSPECIFIED = 0
        INFO = 1
        WARNING = 2
        ERROR = 3

    resource_type: ResourceType = proto.Field(
        proto.ENUM,
        number=1,
        enum=ResourceType,
    )
    resources: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    resource_names: MutableSequence["ResourceName"] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message="ResourceName",
    )
    severity: Severity = proto.Field(
        proto.ENUM,
        number=3,
        enum=Severity,
    )
    detail: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ResourceName(proto.Message):
    r"""Resource name and display name.

    Attributes:
        name (str):
            Name.
        display_name (str):
            Display name.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
