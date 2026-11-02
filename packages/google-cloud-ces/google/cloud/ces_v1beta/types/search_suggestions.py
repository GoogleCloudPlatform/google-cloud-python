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
    package="google.cloud.ces.v1beta",
    manifest={
        "GoogleSearchSuggestions",
        "WebSearchQuery",
    },
)


class GoogleSearchSuggestions(proto.Message):
    r"""Search suggestions from [Google Search
    Tool][google.cloud.ces.v1beta.GoogleSearchTool].

    Attributes:
        htmls (MutableSequence[str]):
            Compliant HTML and CSS styling for search suggestions. The
            provided HTML and CSS automatically adapts to your device
            settings, displaying in either light or dark mode indicated
            by ``@media(prefers-color-scheme)``.
        web_search_queries (MutableSequence[google.cloud.ces_v1beta.types.WebSearchQuery]):
            List of queries used to perform the google
            search along with the search result URIs forming
            the search suggestions.
    """

    htmls: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    web_search_queries: MutableSequence["WebSearchQuery"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="WebSearchQuery",
    )


class WebSearchQuery(proto.Message):
    r"""Represents a single web search query and its associated
    search uri.

    Attributes:
        query (str):
            The search query text.
        uri (str):
            The URI to the Google Search results page for
            the query.
    """

    query: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uri: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
