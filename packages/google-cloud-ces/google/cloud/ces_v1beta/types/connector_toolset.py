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

from google.cloud.ces_v1beta.types import auth, connector_tool

__protobuf__ = proto.module(
    package="google.cloud.ces.v1beta",
    manifest={
        "ConnectorToolset",
    },
)


class ConnectorToolset(proto.Message):
    r"""A toolset that generates tools from an Integration Connectors
    Connection.

    Attributes:
        connection (str):
            Required. The full resource name of the referenced
            Integration Connectors Connection. Format:
            ``projects/{project}/locations/{location}/connections/{connection}``
        auth_config (google.cloud.ces_v1beta.types.EndUserAuthConfig):
            Optional. Configures how authentication is handled in
            Integration Connectors. By default, an admin authentication
            is passed in the Integration Connectors API requests. You
            can override it with a different end-user authentication
            config. **Note**: The Connection must have authentication
            override enabled in order to specify an EUC configuration
            here - otherwise, the Toolset creation will fail. See:
            https://cloud.google.com/application-integration/docs/configure-connectors-task#configure-authentication-override
        connector_actions (MutableSequence[google.cloud.ces_v1beta.types.Action]):
            Required. The list of connector
            actions/entity operations to generate tools for.
    """

    connection: str = proto.Field(
        proto.STRING,
        number=1,
    )
    auth_config: auth.EndUserAuthConfig = proto.Field(
        proto.MESSAGE,
        number=2,
        message=auth.EndUserAuthConfig,
    )
    connector_actions: MutableSequence[connector_tool.Action] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=connector_tool.Action,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
