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
    package="google.cloud.dialogflow.v2",
    manifest={
        "GroundingMetadata",
        "SearchEntryPoint",
        "GroundingChunk",
        "Segment",
        "GroundingSupport",
    },
)


class GroundingMetadata(proto.Message):
    r"""Grounding metadata contains sources, citations, and search
    entry points used to ground a generated answer or suggestion.

    Attributes:
        web_search_queries (MutableSequence[str]):
            Optional. The web search queries that were
            used to generate the content.
        search_entry_point (google.cloud.dialogflow_v2.types.SearchEntryPoint):
            Optional. A web search entry point that can
            be used to display search results.
        grounding_chunks (MutableSequence[google.cloud.dialogflow_v2.types.GroundingChunk]):
            Optional. A list of supporting references
            retrieved from the grounding source.
        grounding_supports (MutableSequence[google.cloud.dialogflow_v2.types.GroundingSupport]):
            Optional. A list of grounding supports that
            connect the generated content to the grounding
            chunks.
    """

    web_search_queries: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    search_entry_point: "SearchEntryPoint" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="SearchEntryPoint",
    )
    grounding_chunks: MutableSequence["GroundingChunk"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="GroundingChunk",
    )
    grounding_supports: MutableSequence["GroundingSupport"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="GroundingSupport",
    )


class SearchEntryPoint(proto.Message):
    r"""A web search entry point that can be used to display search
    results.

    Attributes:
        rendered_content (str):
            Optional. An HTML snippet that can be
            embedded in a web page or an application's
            webview. This snippet displays a search result,
            including the title, URL, and a brief
            description of the search result.
    """

    rendered_content: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GroundingChunk(proto.Message):
    r"""A piece of evidence that supports a claim made by the model.

    This is used to show a citation for a claim made by the model.
    It contains a reference to the source of the information.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        web (google.cloud.dialogflow_v2.types.GroundingChunk.Web):
            Optional. A grounding chunk from a web page, typically from
            web search. See the ``Web`` message for details.

            This field is a member of `oneof`_ ``chunk_type``.
        retrieved_context (google.cloud.dialogflow_v2.types.GroundingChunk.RetrievedContext):
            Optional. A grounding chunk from a data
            source retrieved by a data store tool.

            This field is a member of `oneof`_ ``chunk_type``.
    """

    class Web(proto.Message):
        r"""A ``Web`` chunk is a piece of evidence that comes from a web page.
        It contains the URI of the web page, the title of the page, and the
        domain of the page. This is used to provide the user with a link to
        the source of the information.

        Attributes:
            uri (str):
                Output only. The URI of the web page that
                contains the evidence.
            title (str):
                Output only. The title of the web page that
                contains the evidence.
            domain (str):
                Output only. The domain of the web page that
                contains the evidence. This can be used to
                filter out low-quality sources.
        """

        uri: str = proto.Field(
            proto.STRING,
            number=1,
        )
        title: str = proto.Field(
            proto.STRING,
            number=2,
        )
        domain: str = proto.Field(
            proto.STRING,
            number=3,
        )

    class RetrievedContext(proto.Message):
        r"""Context retrieved from a data source to ground the model's
        response. This is used when a retrieval tool fetches information
        from a user-provided corpus or a public dataset.

        Attributes:
            uri (str):
                Output only. The URI of the retrieved data
                source.
            title (str):
                Output only. The title of the retrieved data
                source.
            text (str):
                Output only. The content of the retrieved
                data source.
        """

        uri: str = proto.Field(
            proto.STRING,
            number=1,
        )
        title: str = proto.Field(
            proto.STRING,
            number=2,
        )
        text: str = proto.Field(
            proto.STRING,
            number=3,
        )

    web: Web = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="chunk_type",
        message=Web,
    )
    retrieved_context: RetrievedContext = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="chunk_type",
        message=RetrievedContext,
    )


class Segment(proto.Message):
    r"""A segment of the content.

    Attributes:
        start_index (int):
            Output only. The start index of the segment,
            measured in bytes. This marks the beginning of
            the segment and is inclusive, meaning the byte
            at this index is the first byte of the segment.
        end_index (int):
            Output only. The end index of the segment,
            measured in bytes. This marks the end of the
            segment and is exclusive, meaning the segment
            includes content up to, but not including, the
            byte at this index.
        text (str):
            Output only. The text of the segment.
    """

    start_index: int = proto.Field(
        proto.INT32,
        number=1,
    )
    end_index: int = proto.Field(
        proto.INT32,
        number=2,
    )
    text: str = proto.Field(
        proto.STRING,
        number=3,
    )


class GroundingSupport(proto.Message):
    r"""A collection of supporting references for a segment or part
    of the model's response.

    Attributes:
        segment (google.cloud.dialogflow_v2.types.Segment):
            Optional. Segment of the content this support
            belongs to.
        grounding_chunk_indices (MutableSequence[int]):
            Optional. A list of indices into ``grounding_chunks`` field
            specifying the citations associated with the claim. For
            instance [1, 3] means that grounding_chunks[1] and
            grounding_chunks[3] are the retrieved contents attributed to
            the claim.
    """

    segment: "Segment" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Segment",
    )
    grounding_chunk_indices: MutableSequence[int] = proto.RepeatedField(
        proto.INT32,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
