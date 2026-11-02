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
    package="google.cloud.agentregistry.v1",
    manifest={
        "Interface",
    },
)


class Interface(proto.Message):
    r"""Represents the connection details for an Agent or MCP Server.

    Attributes:
        url (str):
            Required. The destination URL.
        protocol_binding (google.cloud.agentregistry_v1.types.Interface.ProtocolBinding):
            Required. The protocol binding of the
            interface.
    """

    class ProtocolBinding(proto.Enum):
        r"""The protocol binding of the interface.

        Values:
            PROTOCOL_BINDING_UNSPECIFIED (0):
                Unspecified transport protocol.
            JSONRPC (1):
                JSON-RPC specification.
            GRPC (2):
                gRPC specification.
            HTTP_JSON (3):
                HTTP+JSON specification.
        """

        PROTOCOL_BINDING_UNSPECIFIED = 0
        JSONRPC = 1
        GRPC = 2
        HTTP_JSON = 3

    url: str = proto.Field(
        proto.STRING,
        number=1,
    )
    protocol_binding: ProtocolBinding = proto.Field(
        proto.ENUM,
        number=2,
        enum=ProtocolBinding,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
