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

from google.apps.chat_v1.types import elements_common

__protobuf__ = proto.module(
    package="google.chat.v1",
    manifest={
        "CitedSource",
    },
)


class CitedSource(proto.Message):
    r"""A reference to a source of information.

    Attributes:
        title (str):
            Required. The plaintext title of the ``CitedSource``. Does
            not support markdown format.
        uri (str):
            Required. The URI pointing to the resource referenced by
            this ``CitedSource``.
        snippet (google.apps.chat_v1.types.CitedSource.Snippet):
            Optional. Snippet containing information
            directly from the source.
        footer (google.apps.chat_v1.types.CitedSource.Footer):
            Optional. Additional information to show
            alongside the snippet in the form of a footer.
    """

    class Snippet(proto.Message):
        r"""A snippet object representing an excerpt from a larger
        corpus.

        Attributes:
            text (str):
                Optional. A short plaintext excerpt directly from the corpus
                that is rendered in the citation hover card or source
                preview. When footer sources are automatically populated
                from inline ``citations`` (because
                ``Elements.cited_sources`` is not set), snippets are omitted
                from the deduplicated footer sources. Does not support
                markdown format, and must not exceed 1,000 characters.
            image_preview (google.apps.chat_v1.types.ElementsImage):
                Optional. Image preview of the snippet
                provided as an input when creating the citation.
        """

        text: str = proto.Field(
            proto.STRING,
            number=1,
        )
        image_preview: elements_common.ElementsImage = proto.Field(
            proto.MESSAGE,
            number=2,
            message=elements_common.ElementsImage,
        )

    class Footer(proto.Message):
        r"""A footer for a source, used for attribution.

        Attributes:
            text (str):
                Optional. The plaintext to display in the
                footer. Does not support markdown format.
        """

        text: str = proto.Field(
            proto.STRING,
            number=1,
        )

    title: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    snippet: Snippet = proto.Field(
        proto.MESSAGE,
        number=3,
        message=Snippet,
    )
    footer: Footer = proto.Field(
        proto.MESSAGE,
        number=5,
        message=Footer,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
