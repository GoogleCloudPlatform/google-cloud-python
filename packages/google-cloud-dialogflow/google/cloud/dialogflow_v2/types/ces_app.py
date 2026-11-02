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

from google.cloud.dialogflow_v2.types import tool

__protobuf__ = proto.module(
    package="google.cloud.dialogflow.v2",
    manifest={
        "CesAppSpec",
    },
)


class CesAppSpec(proto.Message):
    r"""Deprecated: Use ``CesToolSpec`` instead. Spec of CES app that the
    generator can choose from.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        ces_app (str):
            Optional. Format:
            ``projects/<Project ID>/locations/<Location ID>/apps/<app ID>``.
        confirmation_requirement (google.cloud.dialogflow_v2.types.Tool.ConfirmationRequirement):
            Optional. Indicates whether the app requires
            human confirmation.
        proactive_enabled (bool):
            Optional. Only applicable for CompanionAgent. Indicates
            whether the ces app is enabled in proactive mode. At least
            one of ``proactive_enabled`` or ``reactive_enabled`` should
            be true; otherwise, the ces app will be ignored.

            This field is a member of `oneof`_ ``_proactive_enabled``.
        reactive_enabled (bool):
            Optional. Only applicable for CompanionAgent. Indicates
            whether the ces app is enabled in reactive mode. At least
            one of ``proactive_enabled`` or ``reactive_enabled`` should
            be true; otherwise, the ces app will be ignored.

            This field is a member of `oneof`_ ``_reactive_enabled``.
    """

    ces_app: str = proto.Field(
        proto.STRING,
        number=1,
    )
    confirmation_requirement: tool.Tool.ConfirmationRequirement = proto.Field(
        proto.ENUM,
        number=2,
        enum=tool.Tool.ConfirmationRequirement,
    )
    proactive_enabled: bool = proto.Field(
        proto.BOOL,
        number=3,
        optional=True,
    )
    reactive_enabled: bool = proto.Field(
        proto.BOOL,
        number=4,
        optional=True,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
