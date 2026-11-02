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
    package="google.ads.admanager.v1",
    manifest={
        "DaiAuthenticationKeyStatusEnum",
        "DaiAuthenticationKeyTypeEnum",
    },
)


class DaiAuthenticationKeyStatusEnum(proto.Message):
    r"""Wrapper message for
    [DaiAuthenticationKeyStatus][google.ads.admanager.v1.DaiAuthenticationKeyStatusEnum.DaiAuthenticationKeyStatus]

    """

    class DaiAuthenticationKeyStatus(proto.Enum):
        r"""Statuses associated with DaiAuthenticationKey objects.

        Values:
            DAI_AUTHENTICATION_KEY_STATUS_UNSPECIFIED (0):
                Default value. This value is unused.
            ACTIVE (1):
                Indicates that the API key is actively in use
                and that the IMA SDK API should accept it as a
                valid key in requests.
            INACTIVE (2):
                Indicates that the API key is no longer is
                use and that the IMA SDK API should not accept
                it as a valid key in requests.
        """

        DAI_AUTHENTICATION_KEY_STATUS_UNSPECIFIED = 0
        ACTIVE = 1
        INACTIVE = 2


class DaiAuthenticationKeyTypeEnum(proto.Message):
    r"""Wrapper message for
    [DaiAuthenticationKeyType][google.ads.admanager.v1.DaiAuthenticationKeyTypeEnum.DaiAuthenticationKeyType]

    """

    class DaiAuthenticationKeyType(proto.Enum):
        r"""Key types associated with DaiAuthenticationKey objects.

        Values:
            DAI_AUTHENTICATION_KEY_TYPE_UNSPECIFIED (0):
                Default value. This value is unused.
            API (1):
                Indicates that the key is a standard API key
                and should be used with the api-key SDK
                parameter when authenticating stream create
                requests.
            HMAC (2):
                Indicates that the key is an HMAC key and
                should be used to generate a signature for the
                stream create request with the auth-token SDK
                parameter.
        """

        DAI_AUTHENTICATION_KEY_TYPE_UNSPECIFIED = 0
        API = 1
        HMAC = 2


__all__ = tuple(sorted(__protobuf__.manifest))
