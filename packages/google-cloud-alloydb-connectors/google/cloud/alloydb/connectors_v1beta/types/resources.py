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
    package="google.cloud.alloydb.connectors.v1beta",
    manifest={
        "MetadataExchangeRequest",
        "MetadataExchangeResponse",
    },
)


class MetadataExchangeRequest(proto.Message):
    r"""Message used by AlloyDB connectors to exchange client and
    connection metadata with the server after a successful TLS
    handshake. This metadata includes an IAM token, which is used to
    authenticate users based on their IAM identity. The sole purpose
    of this message is for the use of AlloyDB connectors. Clients
    should not rely on this message directly as there can be
    breaking changes in the future.

    Attributes:
        user_agent (str):
            Optional. Connector information.
        auth_type (google.cloud.alloydb.connectors_v1beta.types.MetadataExchangeRequest.AuthType):
            Authentication type.
        oauth2_token (str):
            IAM token used for both IAM user authentiation and
            ``alloydb.instances.connect`` permission check.
    """

    class AuthType(proto.Enum):
        r"""AuthType contains all supported authentication types.

        Values:
            AUTH_TYPE_UNSPECIFIED (0):
                Authentication type is unspecified and DB_NATIVE is used by
                default
            DB_NATIVE (1):
                Database native authentication
                (user/password)
            AUTO_IAM (2):
                Automatic IAM authentication
        """

        AUTH_TYPE_UNSPECIFIED = 0
        DB_NATIVE = 1
        AUTO_IAM = 2

    user_agent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    auth_type: AuthType = proto.Field(
        proto.ENUM,
        number=2,
        enum=AuthType,
    )
    oauth2_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class MetadataExchangeResponse(proto.Message):
    r"""Message for response to metadata exchange request. The sole
    purpose of this message is for the use of AlloyDB connectors.
    Clients should not rely on this message directly as there can be
    breaking changes in the future.

    Attributes:
        response_code (google.cloud.alloydb.connectors_v1beta.types.MetadataExchangeResponse.ResponseCode):
            Response code.
        error (str):
            Optional. Error message.
    """

    class ResponseCode(proto.Enum):
        r"""Response code.

        Values:
            RESPONSE_CODE_UNSPECIFIED (0):
                Unknown response code
            OK (1):
                Success
            ERROR (2):
                Failure
        """

        RESPONSE_CODE_UNSPECIFIED = 0
        OK = 1
        ERROR = 2

    response_code: ResponseCode = proto.Field(
        proto.ENUM,
        number=1,
        enum=ResponseCode,
    )
    error: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
