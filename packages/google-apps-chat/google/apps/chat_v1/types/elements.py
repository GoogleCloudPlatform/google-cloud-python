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

from google.apps.chat_v1.types import citation, cited_source

__protobuf__ = proto.module(
    package="google.chat.v1",
    manifest={
        "Elements",
    },
)


class Elements(proto.Message):
    r"""Elements are additional message components, including inline
    ``citations`` (where each citation is associated with a specific
    portion of the message text) and ``cited_sources`` (which are
    general references used to generate the response and are not
    directly linked to specific segments of the text). Both
    ``citations`` and ``cited_sources`` can be provided as input when
    creating or updating a message and are populated on output when
    reading a message.

    Attributes:
        cited_sources (MutableSequence[google.apps.chat_v1.types.CitedSource]):
            Optional. A list of sources to be displayed under the
            message as footer links. These are not referenced inline.
            For inline references, use ``citations``.
        citations (MutableSequence[google.apps.chat_v1.types.Citation]):
            Optional. A list of inline citations referenced within the
            message text (via ``<chat-citation>`` tags) that render as
            interactive hover cards.
    """

    cited_sources: MutableSequence[cited_source.CitedSource] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=cited_source.CitedSource,
    )
    citations: MutableSequence[citation.Citation] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=citation.Citation,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
