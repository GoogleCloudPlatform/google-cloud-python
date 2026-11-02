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

import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.dialogflow.cx.v3beta1",
    manifest={
        "DataStoreType",
        "DocumentProcessingMode",
        "DataStoreConnection",
        "DataStoreConnectionSignals",
    },
)


class DataStoreType(proto.Enum):
    r"""Type of a data store.
    Determines how search is performed in the data store.

    Values:
        DATA_STORE_TYPE_UNSPECIFIED (0):
            Not specified. This value indicates that the
            data store type is not specified, so it will not
            be used during search.
        PUBLIC_WEB (1):
            A data store that contains public web
            content.
        UNSTRUCTURED (2):
            A data store that contains unstructured
            private data.
        STRUCTURED (3):
            A data store that contains structured data
            (for example FAQ).
    """

    DATA_STORE_TYPE_UNSPECIFIED = 0
    PUBLIC_WEB = 1
    UNSTRUCTURED = 2
    STRUCTURED = 3


class DocumentProcessingMode(proto.Enum):
    r"""The document processing mode of the data store.

    Values:
        DOCUMENT_PROCESSING_MODE_UNSPECIFIED (0):
            Not specified. This should be set for STRUCTURED type data
            stores. Due to legacy reasons this is considered as
            DOCUMENTS for STRUCTURED and PUBLIC_WEB data stores.
        DOCUMENTS (1):
            Documents are processed as documents.
        CHUNKS (2):
            Documents are converted to chunks.
    """

    DOCUMENT_PROCESSING_MODE_UNSPECIFIED = 0
    DOCUMENTS = 1
    CHUNKS = 2


class DataStoreConnection(proto.Message):
    r"""A data store connection. It represents a data store in
    Discovery Engine and the type of the contents it contains.

    Attributes:
        data_store_type (google.cloud.dialogflowcx_v3beta1.types.DataStoreType):
            The type of the connected data store.
        data_store (str):
            The full name of the referenced data store. Formats:
            ``projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}``
            ``projects/{project}/locations/{location}/dataStores/{data_store}``
        document_processing_mode (google.cloud.dialogflowcx_v3beta1.types.DocumentProcessingMode):
            The document processing mode for the data store connection.
            Should only be set for PUBLIC_WEB and UNSTRUCTURED data
            stores. If not set it is considered as DOCUMENTS, as this is
            the legacy mode.
    """

    data_store_type: "DataStoreType" = proto.Field(
        proto.ENUM,
        number=1,
        enum="DataStoreType",
    )
    data_store: str = proto.Field(
        proto.STRING,
        number=2,
    )
    document_processing_mode: "DocumentProcessingMode" = proto.Field(
        proto.ENUM,
        number=4,
        enum="DocumentProcessingMode",
    )


class DataStoreConnectionSignals(proto.Message):
    r"""Data store connection feature output signals.
    Might be only partially field if processing stop before the
    final answer. Reasons for this can be, but are not limited to:
    empty UCS search results, positive RAI check outcome, grounding
    failure, ...

    Attributes:
        rewriter_model_call_signals (google.cloud.dialogflowcx_v3beta1.types.DataStoreConnectionSignals.RewriterModelCallSignals):
            Optional. Diagnostic info related to the
            rewriter model call.
        rewritten_query (str):
            Optional. Rewritten string query used for
            search.
        search_snippets (MutableSequence[google.cloud.dialogflowcx_v3beta1.types.DataStoreConnectionSignals.SearchSnippet]):
            Optional. Search snippets included in the
            answer generation prompt.
        answer_generation_model_call_signals (google.cloud.dialogflowcx_v3beta1.types.DataStoreConnectionSignals.AnswerGenerationModelCallSignals):
            Optional. Diagnostic info related to the
            answer generation model call.
        answer (str):
            Optional. The final compiled answer.
        answer_parts (MutableSequence[google.cloud.dialogflowcx_v3beta1.types.DataStoreConnectionSignals.AnswerPart]):
            Optional. Answer parts with relevant citations.
            Concatenation of texts should add up the ``answer`` (not
            counting whitespaces).
        cited_snippets (MutableSequence[google.cloud.dialogflowcx_v3beta1.types.DataStoreConnectionSignals.CitedSnippet]):
            Optional. Snippets cited by the answer
            generation model from the most to least
            relevant.
        grounding_signals (google.cloud.dialogflowcx_v3beta1.types.DataStoreConnectionSignals.GroundingSignals):
            Optional. Grounding signals.
        safety_signals (google.cloud.dialogflowcx_v3beta1.types.DataStoreConnectionSignals.SafetySignals):
            Optional. Safety check result.
    """

    class RewriterModelCallSignals(proto.Message):
        r"""Diagnostic info related to the rewriter model call.

        Attributes:
            rendered_prompt (str):
                Prompt as sent to the model.
            model_output (str):
                Output of the generative model.
            model (str):
                Name of the generative model. For example,
                "gemini-ultra", "gemini-pro", "gemini-1.5-flash"
                etc. Defaults to "Other" if the model is
                unknown.
        """

        rendered_prompt: str = proto.Field(
            proto.STRING,
            number=1,
        )
        model_output: str = proto.Field(
            proto.STRING,
            number=2,
        )
        model: str = proto.Field(
            proto.STRING,
            number=3,
        )

    class SearchSnippet(proto.Message):
        r"""Search snippet details.

        Attributes:
            document_title (str):
                Title of the enclosing document.
            document_uri (str):
                Uri for the document. Present if specified
                for the document.
            text (str):
                Text included in the prompt.
            metadata (google.protobuf.struct_pb2.Struct):
                Metadata associated with the document.
        """

        document_title: str = proto.Field(
            proto.STRING,
            number=1,
        )
        document_uri: str = proto.Field(
            proto.STRING,
            number=2,
        )
        text: str = proto.Field(
            proto.STRING,
            number=3,
        )
        metadata: struct_pb2.Struct = proto.Field(
            proto.MESSAGE,
            number=5,
            message=struct_pb2.Struct,
        )

    class AnswerGenerationModelCallSignals(proto.Message):
        r"""Diagnostic info related to the answer generation model call.

        Attributes:
            rendered_prompt (str):
                Prompt as sent to the model.
            model_output (str):
                Output of the generative model.
            model (str):
                Name of the generative model. For example,
                "gemini-ultra", "gemini-pro", "gemini-1.5-flash"
                etc. Defaults to "Other" if the model is
                unknown.
        """

        rendered_prompt: str = proto.Field(
            proto.STRING,
            number=1,
        )
        model_output: str = proto.Field(
            proto.STRING,
            number=2,
        )
        model: str = proto.Field(
            proto.STRING,
            number=3,
        )

    class AnswerPart(proto.Message):
        r"""Answer part with citation.

        Attributes:
            text (str):
                Substring of the answer.
            supporting_indices (MutableSequence[int]):
                Citations for this answer part. Indices of
                ``search_snippets``.
        """

        text: str = proto.Field(
            proto.STRING,
            number=1,
        )
        supporting_indices: MutableSequence[int] = proto.RepeatedField(
            proto.INT32,
            number=2,
        )

    class CitedSnippet(proto.Message):
        r"""Snippet cited by the answer generation model.

        Attributes:
            search_snippet (google.cloud.dialogflowcx_v3beta1.types.DataStoreConnectionSignals.SearchSnippet):
                Details of the snippet.
            snippet_index (int):
                Index of the snippet in ``search_snippets`` field.
        """

        search_snippet: "DataStoreConnectionSignals.SearchSnippet" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="DataStoreConnectionSignals.SearchSnippet",
        )
        snippet_index: int = proto.Field(
            proto.INT32,
            number=2,
        )

    class GroundingSignals(proto.Message):
        r"""Grounding signals.

        Attributes:
            decision (google.cloud.dialogflowcx_v3beta1.types.DataStoreConnectionSignals.GroundingSignals.GroundingDecision):
                Represents the decision of the grounding
                check.
            score (google.cloud.dialogflowcx_v3beta1.types.DataStoreConnectionSignals.GroundingSignals.GroundingScoreBucket):
                Grounding score bucket setting.
        """

        class GroundingDecision(proto.Enum):
            r"""Represents the decision of the grounding check.

            Values:
                GROUNDING_DECISION_UNSPECIFIED (0):
                    Decision not specified.
                ACCEPTED_BY_GROUNDING (1):
                    Grounding have accepted the answer.
                REJECTED_BY_GROUNDING (2):
                    Grounding have rejected the answer.
            """

            GROUNDING_DECISION_UNSPECIFIED = 0
            ACCEPTED_BY_GROUNDING = 1
            REJECTED_BY_GROUNDING = 2

        class GroundingScoreBucket(proto.Enum):
            r"""Grounding score buckets.

            Values:
                GROUNDING_SCORE_BUCKET_UNSPECIFIED (0):
                    Score not specified.
                VERY_LOW (1):
                    We have very low confidence that the answer
                    is grounded.
                LOW (3):
                    We have low confidence that the answer is
                    grounded.
                MEDIUM (4):
                    We have medium confidence that the answer is
                    grounded.
                HIGH (5):
                    We have high confidence that the answer is
                    grounded.
                VERY_HIGH (6):
                    We have very high confidence that the answer
                    is grounded.
            """

            GROUNDING_SCORE_BUCKET_UNSPECIFIED = 0
            VERY_LOW = 1
            LOW = 3
            MEDIUM = 4
            HIGH = 5
            VERY_HIGH = 6

        decision: "DataStoreConnectionSignals.GroundingSignals.GroundingDecision" = (
            proto.Field(
                proto.ENUM,
                number=1,
                enum="DataStoreConnectionSignals.GroundingSignals.GroundingDecision",
            )
        )
        score: "DataStoreConnectionSignals.GroundingSignals.GroundingScoreBucket" = (
            proto.Field(
                proto.ENUM,
                number=2,
                enum="DataStoreConnectionSignals.GroundingSignals.GroundingScoreBucket",
            )
        )

    class SafetySignals(proto.Message):
        r"""Safety check results.

        Attributes:
            decision (google.cloud.dialogflowcx_v3beta1.types.DataStoreConnectionSignals.SafetySignals.SafetyDecision):
                Safety decision.
            banned_phrase_match (google.cloud.dialogflowcx_v3beta1.types.DataStoreConnectionSignals.SafetySignals.BannedPhraseMatch):
                Specifies banned phrase match subject.
            matched_banned_phrase (str):
                The matched banned phrase if there was a
                match.
        """

        class SafetyDecision(proto.Enum):
            r"""Safety decision.
            All kinds of check are incorporated into this final decision,
            including banned phrases check.

            Values:
                SAFETY_DECISION_UNSPECIFIED (0):
                    Decision not specified.
                ACCEPTED_BY_SAFETY_CHECK (1):
                    No manual or automatic safety check fired.
                REJECTED_BY_SAFETY_CHECK (2):
                    One ore more safety checks fired.
            """

            SAFETY_DECISION_UNSPECIFIED = 0
            ACCEPTED_BY_SAFETY_CHECK = 1
            REJECTED_BY_SAFETY_CHECK = 2

        class BannedPhraseMatch(proto.Enum):
            r"""Specifies banned phrase match subject.

            Values:
                BANNED_PHRASE_MATCH_UNSPECIFIED (0):
                    No banned phrase check was executed.
                BANNED_PHRASE_MATCH_NONE (1):
                    All banned phrase checks led to no match.
                BANNED_PHRASE_MATCH_QUERY (2):
                    A banned phrase matched the query.
                BANNED_PHRASE_MATCH_RESPONSE (3):
                    A banned phrase matched the response.
            """

            BANNED_PHRASE_MATCH_UNSPECIFIED = 0
            BANNED_PHRASE_MATCH_NONE = 1
            BANNED_PHRASE_MATCH_QUERY = 2
            BANNED_PHRASE_MATCH_RESPONSE = 3

        decision: "DataStoreConnectionSignals.SafetySignals.SafetyDecision" = (
            proto.Field(
                proto.ENUM,
                number=1,
                enum="DataStoreConnectionSignals.SafetySignals.SafetyDecision",
            )
        )
        banned_phrase_match: "DataStoreConnectionSignals.SafetySignals.BannedPhraseMatch" = proto.Field(
            proto.ENUM,
            number=2,
            enum="DataStoreConnectionSignals.SafetySignals.BannedPhraseMatch",
        )
        matched_banned_phrase: str = proto.Field(
            proto.STRING,
            number=3,
        )

    rewriter_model_call_signals: RewriterModelCallSignals = proto.Field(
        proto.MESSAGE,
        number=1,
        message=RewriterModelCallSignals,
    )
    rewritten_query: str = proto.Field(
        proto.STRING,
        number=2,
    )
    search_snippets: MutableSequence[SearchSnippet] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=SearchSnippet,
    )
    answer_generation_model_call_signals: AnswerGenerationModelCallSignals = (
        proto.Field(
            proto.MESSAGE,
            number=4,
            message=AnswerGenerationModelCallSignals,
        )
    )
    answer: str = proto.Field(
        proto.STRING,
        number=5,
    )
    answer_parts: MutableSequence[AnswerPart] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message=AnswerPart,
    )
    cited_snippets: MutableSequence[CitedSnippet] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message=CitedSnippet,
    )
    grounding_signals: GroundingSignals = proto.Field(
        proto.MESSAGE,
        number=8,
        message=GroundingSignals,
    )
    safety_signals: SafetySignals = proto.Field(
        proto.MESSAGE,
        number=9,
        message=SafetySignals,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
