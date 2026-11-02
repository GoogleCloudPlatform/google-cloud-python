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

from google.cloud.dataqna_v1alpha.types import annotated_string

__protobuf__ = proto.module(
    package="google.cloud.dataqna.v1alpha",
    manifest={
        "SuggestionType",
        "SuggestQueriesRequest",
        "Suggestion",
        "SuggestionInfo",
        "SuggestQueriesResponse",
    },
)


class SuggestionType(proto.Enum):
    r"""The type of suggestion.

    Values:
        SUGGESTION_TYPE_UNSPECIFIED (0):
            No suggestiont type is specified.
        ENTITY (1):
            Entity suggestion type. Suggestions are for
            single entities.
        TEMPLATE (2):
            Template suggestion type. Suggestions are for
            full sentences.
    """

    SUGGESTION_TYPE_UNSPECIFIED = 0
    ENTITY = 1
    TEMPLATE = 2


class SuggestQueriesRequest(proto.Message):
    r"""Request for query suggestions.

    Attributes:
        parent (str):
            Required. The parent of the suggestion query
            is the resource denoting the project and
            location.
        scopes (MutableSequence[str]):
            The scopes to which this search is restricted. The only
            supported scope pattern is
            ``//bigquery.googleapis.com/projects/{GCP-PROJECT-ID}/datasets/{DATASET-ID}/tables/{TABLE-ID}``.
        query (str):
            User query for which to generate suggestions.
            If the query is empty, zero state suggestions
            are returned. This allows UIs to display
            suggestions right away, helping the user to get
            a sense of what a query might look like.
        suggestion_types (MutableSequence[google.cloud.dataqna_v1alpha.types.SuggestionType]):
            The requested suggestion type. Multiple
            suggestion types can be requested, but there is
            no guarantee that the service will return
            suggestions for each type. Suggestions for a
            requested type might rank lower than suggestions
            for other types and the service may decide to
            cut these suggestions off.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    scopes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    query: str = proto.Field(
        proto.STRING,
        number=3,
    )
    suggestion_types: MutableSequence["SuggestionType"] = proto.RepeatedField(
        proto.ENUM,
        number=4,
        enum="SuggestionType",
    )


class Suggestion(proto.Message):
    r"""A suggestion for a query with a ranking score.

    Attributes:
        suggestion_info (google.cloud.dataqna_v1alpha.types.SuggestionInfo):
            Detailed information about the suggestion.
        ranking_score (float):
            The score of the suggestion. This can be used to define
            ordering in UI. The score represents confidence in the
            suggestion where higher is better. All score values must be
            in the range [0, 1).
        suggestion_type (google.cloud.dataqna_v1alpha.types.SuggestionType):
            The type of the suggestion.
    """

    suggestion_info: "SuggestionInfo" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="SuggestionInfo",
    )
    ranking_score: float = proto.Field(
        proto.DOUBLE,
        number=2,
    )
    suggestion_type: "SuggestionType" = proto.Field(
        proto.ENUM,
        number=3,
        enum="SuggestionType",
    )


class SuggestionInfo(proto.Message):
    r"""Detailed information about the suggestion.

    Attributes:
        annotated_suggestion (google.cloud.dataqna_v1alpha.types.AnnotatedString):
            Annotations for the suggestion. This provides
            information about which part of the suggestion
            corresponds to what semantic meaning (e.g. a
            metric).
        query_matches (MutableSequence[google.cloud.dataqna_v1alpha.types.SuggestionInfo.MatchInfo]):
            Matches between user query and the annotated
            string.
    """

    class MatchInfo(proto.Message):
        r"""MatchInfo describes which part of suggestion matched with data in
        user typed query. This can be used to highlight matching parts in
        the UI. This is different from the annotations provided in
        annotated_suggestion. The annotated_suggestion provides information
        about the semantic meaning, while this provides information about
        how it relates to the input.

        Example: user query: ``top products``

        ::

           annotated_suggestion {
            text_formatted = "top product_group"
            html_formatted = "top <b>product_group</b>"
            markups {
             {type: TEXT, start_char_index: 0, length: 3}
             {type: DIMENSION, start_char_index: 4, length: 13}
            }
           }

           query_matches {
            { start_char_index: 0, length: 3 }
            { start_char_index: 4, length: 7}
           }

        Attributes:
            start_char_index (int):
                Unicode character index of the string
                annotation.
            length (int):
                Count of unicode characters of this
                substring.
        """

        start_char_index: int = proto.Field(
            proto.INT32,
            number=1,
        )
        length: int = proto.Field(
            proto.INT32,
            number=2,
        )

    annotated_suggestion: annotated_string.AnnotatedString = proto.Field(
        proto.MESSAGE,
        number=1,
        message=annotated_string.AnnotatedString,
    )
    query_matches: MutableSequence[MatchInfo] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=MatchInfo,
    )


class SuggestQueriesResponse(proto.Message):
    r"""Response to SuggestQueries.

    Attributes:
        suggestions (MutableSequence[google.cloud.dataqna_v1alpha.types.Suggestion]):
            A list of suggestions.
    """

    suggestions: MutableSequence["Suggestion"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Suggestion",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
