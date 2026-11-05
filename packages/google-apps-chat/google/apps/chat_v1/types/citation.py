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

from google.apps.chat_v1.types import cited_source

__protobuf__ = proto.module(
    package="google.chat.v1",
    manifest={
        "Citation",
    },
)


class Citation(proto.Message):
    r"""Citations are inline references that can provide users more detailed
    information about the inline reference. Corresponding inline
    citations should be present in the message text in a markup format
    of ``<chat-citation data-id="{id}">{text}</chat-citation>``.
    Citations are only supported when the message's ``markup_syntax`` is
    set to ``MARKDOWN``.

    Unreferenced citations in ``Elements.citations`` (those without a
    matching ``<chat-citation>`` tag in the message text) are ignored
    and do not cause the message to be rejected.

    Attributes:
        id (str):
            Required. The ID of the citation. This ID is defined by the
            app creating the citation and must match the ``data-id``
            attribute of the ``<chat-citation>`` tag in the message
            text. Must contain only ASCII letters and numbers, and less
            than 63 characters.
        cited_sources (MutableSequence[google.apps.chat_v1.types.CitedSource]):
            Optional. A list of sources that are relevant
            to the citation. Sources are displayed in the
            citation hover card.
    """

    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    cited_sources: MutableSequence[cited_source.CitedSource] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=cited_source.CitedSource,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
