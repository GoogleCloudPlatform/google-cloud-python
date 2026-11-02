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
    package="google.cloud.discoveryengine.v1beta",
    manifest={
        "AgentGatewaySetting",
    },
)


class AgentGatewaySetting(proto.Message):
    r"""Agent Gateway setting, which may be attached to Gemini
    Enterprise resources for egress control of Gemini Enterprise
    agents to agents and tools outside of Gemini Enterprise.

    Attributes:
        default_egress_agent_gateway (google.cloud.discoveryengine_v1beta.types.AgentGatewaySetting.AgentGatewayReference):
            Optional. The default egress agent gateway to use, when this
            setting is applied to a Gemini Enterprise resource.

            The deployment mode must be GOOGLE_MANAGED, and the governed
            access path must be AGENT_TO_ANYWHERE.
    """

    class AgentGatewayReference(proto.Message):
        r"""Reference to an Agent Gateway resource.

        Attributes:
            name (str):
                Required. Immutable. The resource name of the agent gateway.

                Expected format:
                ``projects/{project_number}/locations/{location}/agentGateways/{agent_gateway}``.
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )

    default_egress_agent_gateway: AgentGatewayReference = proto.Field(
        proto.MESSAGE,
        number=1,
        message=AgentGatewayReference,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
