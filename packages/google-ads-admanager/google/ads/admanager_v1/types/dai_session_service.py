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
        "GetDaiSessionRequest",
    },
)


class GetDaiSessionRequest(proto.Message):
    r"""Request object for ``GetDaiSession`` method.

    Attributes:
        name (str):
            Required. The resource name of the DaiSession. The
            dai_session can be either the session ID or debug key, that
            DAI returns on stream create. For details, see `Locate a DAI
            session ID or debug
            key <https://support.google.com/admanager/answer/7257678>`__.

            Format:
            ``networks/{network_code}/daiSessions/{dai_session}``
            Format: ``networks/{network_code}/daiSessions/{session_id}``
            Format: ``networks/{network_code}/daiSessions/{debug_key}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
