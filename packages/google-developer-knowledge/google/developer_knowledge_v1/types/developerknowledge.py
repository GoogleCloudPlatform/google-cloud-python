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

import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.developers.knowledge.v1",
    manifest={
        "DocumentView",
        "Document",
        "SearchDocumentChunksRequest",
        "SearchDocumentChunksResponse",
        "GetDocumentRequest",
        "BatchGetDocumentsRequest",
        "BatchGetDocumentsResponse",
        "AnswerQueryRequest",
        "AnswerQueryResponse",
        "Answer",
        "DocumentChunk",
    },
)


class DocumentView(proto.Enum):
    r"""Specifies which fields of the
    [Document][google.developers.knowledge.v1.Document] are included.

    Values:
        DOCUMENT_VIEW_UNSPECIFIED (0):
            The default / unset value. See each API method for its
            default value if
            [DocumentView][google.developers.knowledge.v1.DocumentView]
            is not specified.
        DOCUMENT_VIEW_BASIC (1):
            Includes only the basic metadata fields:

            - ``name``
            - ``uri``
            - ``data_source``
            - ``title``
            - ``description``
            - ``update_time``
            - ``view``
            - ``content_length_bytes``

            This is the default of view for
            [DeveloperKnowledge.SearchDocumentChunks][google.developers.knowledge.v1.DeveloperKnowledge.SearchDocumentChunks].
        DOCUMENT_VIEW_FULL (2):
            Includes all
            [Document][google.developers.knowledge.v1.Document] fields.
        DOCUMENT_VIEW_CONTENT (3):
            Includes the ``DOCUMENT_VIEW_BASIC`` fields and the
            ``content`` field.

            This is the default of view for
            [DeveloperKnowledge.GetDocument][google.developers.knowledge.v1.DeveloperKnowledge.GetDocument]
            and
            [DeveloperKnowledge.BatchGetDocuments][google.developers.knowledge.v1.DeveloperKnowledge.BatchGetDocuments].
    """

    DOCUMENT_VIEW_UNSPECIFIED = 0
    DOCUMENT_VIEW_BASIC = 1
    DOCUMENT_VIEW_FULL = 2
    DOCUMENT_VIEW_CONTENT = 3


class Document(proto.Message):
    r"""A Document represents a page of documentation in the
    Developer Knowledge corpus, like the page at
    https://docs.cloud.google.com/storage/docs/creating-buckets.

    Attributes:
        name (str):
            Identifier. Contains the resource name of the document.
            Format: ``documents/{uri_without_scheme}`` Example:
            ``documents/docs.cloud.google.com/storage/docs/creating-buckets``
        uri (str):
            Output only. Provides the URI of the content, such as
            ``https://docs.cloud.google.com/storage/docs/creating-buckets``.
        content (str):
            Output only. Contains the full content of the
            document in Markdown format.
        description (str):
            Output only. Provides a description of the
            document.
        data_source (str):
            Output only. Specifies the data source of the document.
            Example data source: ``firebase.google.com``
        title (str):
            Output only. Provides the title of the
            document.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Represents the timestamp when
            the content or metadata of the document was last
            updated.
        view (google.developer_knowledge_v1.types.DocumentView):
            Output only. Specifies the
            [DocumentView][google.developers.knowledge.v1.DocumentView]
            of the document.
        content_length_bytes (int):
            Output only. The length of the ``content`` field in bytes.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    content: str = proto.Field(
        proto.STRING,
        number=3,
    )
    description: str = proto.Field(
        proto.STRING,
        number=4,
    )
    data_source: str = proto.Field(
        proto.STRING,
        number=5,
    )
    title: str = proto.Field(
        proto.STRING,
        number=6,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    view: "DocumentView" = proto.Field(
        proto.ENUM,
        number=8,
        enum="DocumentView",
    )
    content_length_bytes: int = proto.Field(
        proto.INT32,
        number=9,
    )


class SearchDocumentChunksRequest(proto.Message):
    r"""Request message for
    [DeveloperKnowledge.SearchDocumentChunks][google.developers.knowledge.v1.DeveloperKnowledge.SearchDocumentChunks].

    Attributes:
        query (str):
            Required. Provides the raw query string provided by the
            user, such as "How to create a Cloud Storage bucket?". The
            query must not exceed 500 characters; values longer than 500
            characters will result in an ``INVALID_ARGUMENT`` error.
        page_size (int):
            Optional. Specifies the maximum number of
            results to return. The service may return fewer
            than this value.

            If unspecified, at most 5 results will be
            returned.

            The maximum value is 100; values above 100 will
            be coerced to 100.
        page_token (str):
            Optional. Contains a page token, received from a previous
            ``SearchDocumentChunks`` call. Provide this to retrieve the
            subsequent page.
        filter (str):
            Optional. Applies a strict filter to the search results. The
            expression supports a subset of the syntax described at
            https://google.aip.dev/160.

            While ``SearchDocumentChunks`` returns
            [DocumentChunk][google.developers.knowledge.v1.DocumentChunk]s,
            the filter is applied to ``DocumentChunk.document`` fields.

            Supported fields for filtering:

            - ``content_length_bytes`` (INTEGER): The length of the
              ``Document.content`` field in bytes.
            - ``data_source`` (STRING): The source of the document, e.g.
              ``docs.cloud.google.com``. See
              https://developers.google.com/knowledge/reference/corpus-reference
              for the complete list of data sources in the corpus.
            - ``update_time`` (TIMESTAMP): The timestamp of when the
              document was last meaningfully updated. A meaningful
              update is one that changes document's markdown content or
              metadata.
            - ``uri`` (STRING): The document URI, e.g.
              ``https://docs.cloud.google.com/bigquery/docs/tables``.

            INTEGER fields support ``=``, ``<``, ``<=``, ``>``, and
            ``>=`` operators.

            STRING fields support ``=`` (equals) and ``!=`` (not equals)
            operators for **exact match** on the whole string. Partial
            match, prefix match, and regexp match are not supported.

            TIMESTAMP fields support ``=``, ``<``, ``<=``, ``>``, and
            ``>=`` operators. Timestamps must be in RFC-3339 format,
            e.g., ``"2025-01-01T00:00:00Z"``.

            Note: Field names must be in ``snake_case`` (e.g.,
            ``data_source``). Values on the right-hand side of filtering
            expressions must be string literals enclosed in double
            quotes (e.g., ``"docs.cloud.google.com"``).

            You can combine expressions using ``AND``, ``OR``, and
            ``NOT`` (or ``-``) logical operators. ``OR`` has higher
            precedence than ``AND``. Use parentheses for explicit
            precedence grouping.

            Examples:

            - Filter by ``Document.content_length_bytes``:
              ``content_length_bytes < 50000``
            - ``data_source = "docs.cloud.google.com" OR data_source = "firebase.google.com"``
            - ``data_source != "firebase.google.com"``
            - ``update_time < "2024-01-01T00:00:00Z"``
            - ``update_time >= "2025-01-22T00:00:00Z" AND (data_source = "developer.chrome.com" OR data_source = "web.dev")``
            - ``uri = "https://docs.cloud.google.com/release-notes"``

            The ``filter`` string must not exceed 500 characters; values
            longer than 500 characters will result in an
            ``INVALID_ARGUMENT`` error.
    """

    query: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )


class SearchDocumentChunksResponse(proto.Message):
    r"""Response message for
    [DeveloperKnowledge.SearchDocumentChunks][google.developers.knowledge.v1.DeveloperKnowledge.SearchDocumentChunks].

    Attributes:
        results (MutableSequence[google.developer_knowledge_v1.types.DocumentChunk]):
            Contains the search results for the given query. Each
            [DocumentChunk][google.developers.knowledge.v1.DocumentChunk]
            in this list contains a snippet of content relevant to the
            search query. Use the
            [DocumentChunk.parent][google.developers.knowledge.v1.DocumentChunk.parent]
            field of each result with
            [DeveloperKnowledge.GetDocument][google.developers.knowledge.v1.DeveloperKnowledge.GetDocument]
            or
            [DeveloperKnowledge.BatchGetDocuments][google.developers.knowledge.v1.DeveloperKnowledge.BatchGetDocuments]
            to retrieve the full document content.
        next_page_token (str):
            Provides a token that can be sent as ``page_token`` to
            retrieve the next page. If this field is omitted, there are
            no subsequent pages.
    """

    @property
    def raw_page(self):
        return self

    results: MutableSequence["DocumentChunk"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="DocumentChunk",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetDocumentRequest(proto.Message):
    r"""Request message for
    [DeveloperKnowledge.GetDocument][google.developers.knowledge.v1.DeveloperKnowledge.GetDocument].

    Attributes:
        name (str):
            Required. Specifies the name of the document to retrieve.
            Format: ``documents/{uri_without_scheme}`` Example:
            ``documents/docs.cloud.google.com/storage/docs/creating-buckets``

            The name must not exceed 500 characters; values longer than
            500 characters will result in an ``INVALID_ARGUMENT`` error.
        view (google.developer_knowledge_v1.types.DocumentView):
            Optional. Specifies the
            [DocumentView][google.developers.knowledge.v1.DocumentView]
            of the document. If unspecified,
            [DeveloperKnowledge.GetDocument][google.developers.knowledge.v1.DeveloperKnowledge.GetDocument]
            defaults to ``DOCUMENT_VIEW_CONTENT``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    view: "DocumentView" = proto.Field(
        proto.ENUM,
        number=2,
        enum="DocumentView",
    )


class BatchGetDocumentsRequest(proto.Message):
    r"""Request message for
    [DeveloperKnowledge.BatchGetDocuments][google.developers.knowledge.v1.DeveloperKnowledge.BatchGetDocuments].

    Attributes:
        names (MutableSequence[str]):
            Required. Specifies the names of the documents to retrieve.
            A maximum of 20 documents can be retrieved in a batch. The
            documents are returned in the same order as the ``names`` in
            the request.

            Format: ``documents/{uri_without_scheme}`` Example:
            ``documents/docs.cloud.google.com/storage/docs/creating-buckets``

            Each name must not exceed 500 characters; values longer than
            500 characters will result in an ``INVALID_ARGUMENT`` error.
        view (google.developer_knowledge_v1.types.DocumentView):
            Optional. Specifies the
            [DocumentView][google.developers.knowledge.v1.DocumentView]
            of the document. If unspecified,
            [DeveloperKnowledge.BatchGetDocuments][google.developers.knowledge.v1.DeveloperKnowledge.BatchGetDocuments]
            defaults to ``DOCUMENT_VIEW_CONTENT``.
    """

    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    view: "DocumentView" = proto.Field(
        proto.ENUM,
        number=2,
        enum="DocumentView",
    )


class BatchGetDocumentsResponse(proto.Message):
    r"""Response message for
    [DeveloperKnowledge.BatchGetDocuments][google.developers.knowledge.v1.DeveloperKnowledge.BatchGetDocuments].

    Attributes:
        documents (MutableSequence[google.developer_knowledge_v1.types.Document]):
            Contains the documents requested.
    """

    documents: MutableSequence["Document"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Document",
    )


class AnswerQueryRequest(proto.Message):
    r"""Request message for
    [DeveloperKnowledge.AnswerQuery][google.developers.knowledge.v1.DeveloperKnowledge.AnswerQuery].

    Attributes:
        query (str):
            Required. The query to answer.
        filter (str):
            Optional. Applies a strict filter to the search results used
            to ground the answer. The expression supports a subset of
            the syntax described at https://google.aip.dev/160.

            Supported fields for filtering:

            - ``content_length_bytes`` (INTEGER): The length of the
              ``Document.content`` field in bytes.
            - ``data_source`` (STRING): The source of the document, e.g.
              ``docs.cloud.google.com``. See
              https://developers.google.com/knowledge/reference/corpus-reference
              for the complete list of data sources in the corpus.
            - ``update_time`` (TIMESTAMP): The timestamp of when the
              document was last meaningfully updated. A meaningful
              update is one that changes document's markdown content or
              metadata.
            - ``uri`` (STRING): The document URI, e.g.
              ``https://docs.cloud.google.com/bigquery/docs/tables``.

            INTEGER fields support ``=``, ``<``, ``<=``, ``>``, and
            ``>=`` operators.

            STRING fields support ``=`` (equals) and ``!=`` (not equals)
            operators for **exact match** on the whole string. Partial
            match, prefix match, and regexp match are not supported.

            TIMESTAMP fields support ``=``, ``<``, ``<=``, ``>``, and
            ``>=`` operators. Timestamps must be in RFC-3339 format,
            e.g., ``"2025-01-01T00:00:00Z"``.

            You can combine expressions using ``AND``, ``OR``, and
            ``NOT`` (or ``-``) logical operators. ``OR`` has higher
            precedence than ``AND``. Use parentheses for explicit
            precedence grouping.

            Examples:

            - Filter by ``Document.content_length_bytes``:
              ``content_length_bytes < 50000``
            - ``data_source = "docs.cloud.google.com" OR data_source = "firebase.google.com"``
            - ``data_source != "firebase.google.com"``
            - ``update_time < "2024-01-01T00:00:00Z"``
            - ``update_time >= "2025-01-22T00:00:00Z" AND (data_source = "developer.chrome.com" OR data_source = "web.dev")``
            - ``uri = "https://docs.cloud.google.com/release-notes"``

            The ``filter`` string must not exceed 500 characters; values
            longer than 500 characters will result in an
            ``INVALID_ARGUMENT`` error.
    """

    query: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )


class AnswerQueryResponse(proto.Message):
    r"""Response message for
    [DeveloperKnowledge.AnswerQuery][google.developers.knowledge.v1.DeveloperKnowledge.AnswerQuery].

    Attributes:
        answer (google.developer_knowledge_v1.types.Answer):
            The answer to the query.
    """

    answer: "Answer" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Answer",
    )


class Answer(proto.Message):
    r"""An answer to a query.

    Attributes:
        answer_text (str):
            Contains the text of the answer.
        citations (MutableSequence[google.developer_knowledge_v1.types.Answer.AnswerCitation]):
            Output only. Contains citations for the
            answer.
        references (MutableSequence[google.developer_knowledge_v1.types.Answer.AnswerReference]):
            Output only. Contains references for the
            answer.
    """

    class AnswerCitation(proto.Message):
        r"""Citation info for a segment.

        Attributes:
            start_index (int):
                Output only. Indicates the start of the
                segment, measured in bytes (UTF-8 unicode),
                inclusive. If there are multi-byte characters,
                such as non-ASCII characters, the index
                measurement is longer than the string length.
            end_index (int):
                Output only. Indicates the end of the
                segment, measured in bytes (UTF-8 unicode),
                exclusive. If there are multi-byte characters,
                such as non-ASCII characters, the index
                measurement is longer than the string length.
            sources (MutableSequence[google.developer_knowledge_v1.types.Answer.CitationSource]):
                Output only. Contains citation sources for
                the attributed segment.
        """

        start_index: int = proto.Field(
            proto.INT32,
            number=1,
        )
        end_index: int = proto.Field(
            proto.INT32,
            number=2,
        )
        sources: MutableSequence["Answer.CitationSource"] = proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message="Answer.CitationSource",
        )

    class CitationSource(proto.Message):
        r"""Citation source.

        Attributes:
            reference_index (int):
                Output only. Contains the index of the
                [Answer.AnswerReference][google.developers.knowledge.v1.Answer.AnswerReference]
                in the ``references`` repeated field.
        """

        reference_index: int = proto.Field(
            proto.INT32,
            number=1,
        )

    class AnswerReference(proto.Message):
        r"""Represents a reference to a source.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            document_reference (google.developer_knowledge_v1.types.Answer.DocumentReference):
                Output only. The reference document.

                This field is a member of `oneof`_ ``content``.
        """

        document_reference: "Answer.DocumentReference" = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="content",
            message="Answer.DocumentReference",
        )

    class DocumentReference(proto.Message):
        r"""Represents a reference to a document.

        Attributes:
            document_chunk (google.developer_knowledge_v1.types.DocumentChunk):
                Output only. Contains the document chunk. The
                ``document_chunk.id`` field is not set and will be empty.
        """

        document_chunk: "DocumentChunk" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="DocumentChunk",
        )

    answer_text: str = proto.Field(
        proto.STRING,
        number=1,
    )
    citations: MutableSequence[AnswerCitation] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=AnswerCitation,
    )
    references: MutableSequence[AnswerReference] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=AnswerReference,
    )


class DocumentChunk(proto.Message):
    r"""A DocumentChunk represents a piece of content from a
    [Document][google.developers.knowledge.v1.Document] in the
    DeveloperKnowledge corpus. To fetch the entire document content,
    pass the ``parent`` to
    [DeveloperKnowledge.GetDocument][google.developers.knowledge.v1.DeveloperKnowledge.GetDocument]
    or
    [DeveloperKnowledge.BatchGetDocuments][google.developers.knowledge.v1.DeveloperKnowledge.BatchGetDocuments].


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        parent (str):
            Output only. Contains the resource name of the document this
            chunk is from. Format: ``documents/{uri_without_scheme}``
            Example:
            ``documents/docs.cloud.google.com/storage/docs/creating-buckets``
        id (str):
            Output only. Specifies the ID of this chunk
            within the document. The chunk ID is unique
            within a document, but not globally unique
            across documents. The chunk ID is not stable and
            may change over time.
        content (str):
            Output only. Contains the content of the
            document chunk.
        document (google.developer_knowledge_v1.types.Document):
            Output only. Represents metadata about the
            [Document][google.developers.knowledge.v1.Document] this
            chunk is from. The
            [DocumentView][google.developers.knowledge.v1.DocumentView]
            of this [Document][google.developers.knowledge.v1.Document]
            message will be set to ``DOCUMENT_VIEW_BASIC``. It is
            included here for convenience so that clients do not need to
            call
            [DeveloperKnowledge.GetDocument][google.developers.knowledge.v1.DeveloperKnowledge.GetDocument]
            or
            [DeveloperKnowledge.BatchGetDocuments][google.developers.knowledge.v1.DeveloperKnowledge.BatchGetDocuments]
            if they only need the metadata fields. Otherwise, clients
            should use
            [DeveloperKnowledge.GetDocument][google.developers.knowledge.v1.DeveloperKnowledge.GetDocument]
            or
            [DeveloperKnowledge.BatchGetDocuments][google.developers.knowledge.v1.DeveloperKnowledge.BatchGetDocuments]
            to fetch the full document content.
        relevance_score (float):
            Output only. Represents the relevance score of the chunk to
            the search query. Higher score indicates higher chunk
            relevance. The score is in range [0.0, 1.0].

            This field is a member of `oneof`_ ``_relevance_score``.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    content: str = proto.Field(
        proto.STRING,
        number=3,
    )
    document: "Document" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="Document",
    )
    relevance_score: float = proto.Field(
        proto.DOUBLE,
        number=5,
        optional=True,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
