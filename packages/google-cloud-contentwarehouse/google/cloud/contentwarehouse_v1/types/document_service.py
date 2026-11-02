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

import google.iam.v1.policy_pb2 as policy_pb2  # type: ignore
import google.longrunning.operations_pb2 as operations_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.contentwarehouse_v1.types import common, histogram, rule_engine
from google.cloud.contentwarehouse_v1.types import document as gcc_document

__protobuf__ = proto.module(
    package="google.cloud.contentwarehouse.v1",
    manifest={
        "CreateDocumentResponse",
        "UpdateDocumentResponse",
        "QAResult",
        "SearchDocumentsResponse",
        "FetchAclResponse",
        "SetAclResponse",
    },
)


class CreateDocumentResponse(proto.Message):
    r"""Response message for DocumentService.CreateDocument.

    Attributes:
        document (google.cloud.contentwarehouse_v1.types.Document):
            Document created after executing create
            request.
        rule_engine_output (google.cloud.contentwarehouse_v1.types.RuleEngineOutput):
            Output from Rule Engine recording the rule evaluator and
            action executor's output.

            Refer format in:
            google/cloud/contentwarehouse/v1/rule_engine.proto
        metadata (google.cloud.contentwarehouse_v1.types.ResponseMetadata):
            Additional information for the API
            invocation, such as the request tracking id.
        long_running_operations (MutableSequence[google.longrunning.operations_pb2.Operation]):
            post-processing LROs
    """

    document: gcc_document.Document = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcc_document.Document,
    )
    rule_engine_output: rule_engine.RuleEngineOutput = proto.Field(
        proto.MESSAGE,
        number=2,
        message=rule_engine.RuleEngineOutput,
    )
    metadata: common.ResponseMetadata = proto.Field(
        proto.MESSAGE,
        number=3,
        message=common.ResponseMetadata,
    )
    long_running_operations: MutableSequence[operations_pb2.Operation] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=4,
            message=operations_pb2.Operation,
        )
    )


class UpdateDocumentResponse(proto.Message):
    r"""Response message for DocumentService.UpdateDocument.

    Attributes:
        document (google.cloud.contentwarehouse_v1.types.Document):
            Updated document after executing update
            request.
        rule_engine_output (google.cloud.contentwarehouse_v1.types.RuleEngineOutput):
            Output from Rule Engine recording the rule evaluator and
            action executor's output.

            Refer format in:
            google/cloud/contentwarehouse/v1/rule_engine.proto
        metadata (google.cloud.contentwarehouse_v1.types.ResponseMetadata):
            Additional information for the API
            invocation, such as the request tracking id.
    """

    document: gcc_document.Document = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcc_document.Document,
    )
    rule_engine_output: rule_engine.RuleEngineOutput = proto.Field(
        proto.MESSAGE,
        number=2,
        message=rule_engine.RuleEngineOutput,
    )
    metadata: common.ResponseMetadata = proto.Field(
        proto.MESSAGE,
        number=3,
        message=common.ResponseMetadata,
    )


class QAResult(proto.Message):
    r"""Additional result info for the question-answering feature.

    Attributes:
        highlights (MutableSequence[google.cloud.contentwarehouse_v1.types.QAResult.Highlight]):
            Highlighted sections in the snippet.
        confidence_score (float):
            The calibrated confidence score for this document, in the
            range [0., 1.]. This represents the confidence level for
            whether the returned document and snippet answers the user's
            query.
    """

    class Highlight(proto.Message):
        r"""A text span in the search text snippet that represents a
        highlighted section (answer context, highly relevant sentence,
        etc.).

        Attributes:
            start_index (int):
                Start index of the highlight.
            end_index (int):
                End index of the highlight, exclusive.
        """

        start_index: int = proto.Field(
            proto.INT32,
            number=1,
        )
        end_index: int = proto.Field(
            proto.INT32,
            number=2,
        )

    highlights: MutableSequence[Highlight] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=Highlight,
    )
    confidence_score: float = proto.Field(
        proto.FLOAT,
        number=2,
    )


class SearchDocumentsResponse(proto.Message):
    r"""Response message for DocumentService.SearchDocuments.

    Attributes:
        matching_documents (MutableSequence[google.cloud.contentwarehouse_v1.types.SearchDocumentsResponse.MatchingDocument]):
            The document entities that match the specified
            [SearchDocumentsRequest][google.cloud.contentwarehouse.v1.SearchDocumentsRequest].
        next_page_token (str):
            The token that specifies the starting
            position of the next page of results. This field
            is empty if there are no more results.
        total_size (int):
            The total number of matched documents which is available
            only if the client set
            [SearchDocumentsRequest.require_total_size][google.cloud.contentwarehouse.v1.SearchDocumentsRequest.require_total_size]
            to ``true`` or set
            [SearchDocumentsRequest.total_result_size][google.cloud.contentwarehouse.v1.SearchDocumentsRequest.total_result_size]
            to ``ESTIMATED_SIZE`` or ``ACTUAL_SIZE``. Otherwise, the
            value will be ``-1``. Typically a UI would handle this
            condition by displaying "of many", for example: "Displaying
            10 of many".
        metadata (google.cloud.contentwarehouse_v1.types.ResponseMetadata):
            Additional information for the API
            invocation, such as the request tracking id.
        histogram_query_results (MutableSequence[google.cloud.contentwarehouse_v1.types.HistogramQueryResult]):
            The histogram results that match with the specified
            [SearchDocumentsRequest.histogram_queries][google.cloud.contentwarehouse.v1.SearchDocumentsRequest.histogram_queries].
        question_answer (str):
            Experimental.
            Question answer from the query against the
            document.
    """

    class MatchingDocument(proto.Message):
        r"""Document entry with metadata inside
        [SearchDocumentsResponse][google.cloud.contentwarehouse.v1.SearchDocumentsResponse]

        Attributes:
            document (google.cloud.contentwarehouse_v1.types.Document):
                Document that matches the specified
                [SearchDocumentsRequest][google.cloud.contentwarehouse.v1.SearchDocumentsRequest].
                This document only contains indexed metadata information.
            search_text_snippet (str):
                Contains snippets of text from the document full raw text
                that most closely match a search query's keywords, if
                available. All HTML tags in the original fields are stripped
                when returned in this field, and matching query keywords are
                enclosed in HTML bold tags.

                If the question-answering feature is enabled, this field
                will instead contain a snippet that answers the user's
                natural-language query. No HTML bold tags will be present,
                and highlights in the answer snippet can be found in
                [QAResult.highlights][google.cloud.contentwarehouse.v1.QAResult.highlights].
            qa_result (google.cloud.contentwarehouse_v1.types.QAResult):
                Experimental.
                Additional result info if the question-answering
                feature is enabled.
            matched_token_page_indices (MutableSequence[int]):
                Return the 1-based page indices where those
                pages have one or more matched tokens.
        """

        document: gcc_document.Document = proto.Field(
            proto.MESSAGE,
            number=1,
            message=gcc_document.Document,
        )
        search_text_snippet: str = proto.Field(
            proto.STRING,
            number=2,
        )
        qa_result: "QAResult" = proto.Field(
            proto.MESSAGE,
            number=3,
            message="QAResult",
        )
        matched_token_page_indices: MutableSequence[int] = proto.RepeatedField(
            proto.INT64,
            number=4,
        )

    @property
    def raw_page(self):
        return self

    matching_documents: MutableSequence[MatchingDocument] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=MatchingDocument,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    total_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    metadata: common.ResponseMetadata = proto.Field(
        proto.MESSAGE,
        number=4,
        message=common.ResponseMetadata,
    )
    histogram_query_results: MutableSequence[histogram.HistogramQueryResult] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=6,
            message=histogram.HistogramQueryResult,
        )
    )
    question_answer: str = proto.Field(
        proto.STRING,
        number=7,
    )


class FetchAclResponse(proto.Message):
    r"""Response message for DocumentService.FetchAcl.

    Attributes:
        policy (google.iam.v1.policy_pb2.Policy):
            The IAM policy.
        metadata (google.cloud.contentwarehouse_v1.types.ResponseMetadata):
            Additional information for the API
            invocation, such as the request tracking id.
    """

    policy: policy_pb2.Policy = proto.Field(
        proto.MESSAGE,
        number=1,
        message=policy_pb2.Policy,
    )
    metadata: common.ResponseMetadata = proto.Field(
        proto.MESSAGE,
        number=2,
        message=common.ResponseMetadata,
    )


class SetAclResponse(proto.Message):
    r"""Response message for DocumentService.SetAcl.

    Attributes:
        policy (google.iam.v1.policy_pb2.Policy):
            The policy will be attached to a resource
            (e.g. projecct, document).
        metadata (google.cloud.contentwarehouse_v1.types.ResponseMetadata):
            Additional information for the API
            invocation, such as the request tracking id.
    """

    policy: policy_pb2.Policy = proto.Field(
        proto.MESSAGE,
        number=1,
        message=policy_pb2.Policy,
    )
    metadata: common.ResponseMetadata = proto.Field(
        proto.MESSAGE,
        number=2,
        message=common.ResponseMetadata,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
