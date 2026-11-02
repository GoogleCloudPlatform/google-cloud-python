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
        "InlineDestination",
        "InlineSource",
    },
)


class InlineDestination(proto.Message):
    r"""Inline destination for a Dialogflow operation that writes or exports
    objects (e.g. [intents][google.cloud.dialogflow.cx.v3.Intent])
    outside of Dialogflow.

    Attributes:
        content (bytes):
            Output only. The uncompressed byte content
            for the objects. Only populated in responses.
    """

    content: bytes = proto.Field(
        proto.BYTES,
        number=1,
    )


class InlineSource(proto.Message):
    r"""Inline source for a Dialogflow operation that reads or imports
    objects (e.g. [intents][google.cloud.dialogflow.cx.v3.Intent]) into
    Dialogflow.

    Attributes:
        content (bytes):
            The uncompressed byte content for the
            objects.
    """

    content: bytes = proto.Field(
        proto.BYTES,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
