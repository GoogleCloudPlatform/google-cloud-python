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

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.rpc.status_pb2 as status_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.dialogflow_v2.types import gcs

__protobuf__ = proto.module(
    package="google.cloud.dialogflow.v2",
    manifest={
        "Document",
        "GetDocumentRequest",
        "ListDocumentsRequest",
        "ListDocumentsResponse",
        "CreateDocumentRequest",
        "ImportDocumentsRequest",
        "ImportDocumentTemplate",
        "ImportDocumentsResponse",
        "DeleteDocumentRequest",
        "UpdateDocumentRequest",
        "ReloadDocumentRequest",
        "ExportDocumentRequest",
        "ExportOperationMetadata",
        "KnowledgeOperationMetadata",
    },
)


class Document(proto.Message):
    r"""A knowledge document to be used by a
    [KnowledgeBase][google.cloud.dialogflow.v2.KnowledgeBase].

    For more information, see the `knowledge base
    guide <https://cloud.google.com/dialogflow/docs/how/knowledge-bases>`__.

    Note: The ``projects.agent.knowledgeBases.documents`` resource is
    deprecated; only use ``projects.knowledgeBases.documents``.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Optional. The document resource name. The name must be empty
            when creating a document. Format:
            ``projects/<Project ID>/locations/<Location ID>/knowledgeBases/<Knowledge Base ID>/documents/<Document ID>``.
        display_name (str):
            Required. The display name of the document.
            The name must be 1024 bytes or less; otherwise,
            the creation request fails.
        mime_type (str):
            Required. The MIME type of this document.
        knowledge_types (MutableSequence[google.cloud.dialogflow_v2.types.Document.KnowledgeType]):
            Required. The knowledge type of document
            content.
        content_uri (str):
            The URI where the file content is located.

            For documents stored in Google Cloud Storage, these URIs
            must have the form ``gs://<bucket-name>/<object-name>``.

            NOTE: External URLs must correspond to public webpages,
            i.e., they must be indexed by Google Search. In particular,
            URLs for showing documents in Google Cloud Storage (i.e. the
            URL in your browser) are not supported. Instead use the
            ``gs://`` format URI described above.

            This field is a member of `oneof`_ ``source``.
        raw_content (bytes):
            The raw content of the document. This field is only
            permitted for EXTRACTIVE_QA and FAQ knowledge types.

            This field is a member of `oneof`_ ``source``.
        enable_auto_reload (bool):
            Optional. If true, we try to automatically reload the
            document every day (at a time picked by the system). If
            false or unspecified, we don't try to automatically reload
            the document.

            Currently you can only enable automatic reload for documents
            sourced from a public url, see ``source`` field for the
            source types.

            Reload status can be tracked in ``latest_reload_status``. If
            a reload fails, we will keep the document unchanged.

            If a reload fails with internal errors, the system will try
            to reload the document on the next day. If a reload fails
            with non-retriable errors (e.g. PERMISSION_DENIED), the
            system will not try to reload the document anymore. You need
            to manually reload the document successfully by calling
            ``ReloadDocument`` and clear the errors.
        latest_reload_status (google.cloud.dialogflow_v2.types.Document.ReloadStatus):
            Output only. The time and status of the
            latest reload. This reload may have been
            triggered automatically or manually and may not
            have succeeded.
        metadata (MutableMapping[str, str]):
            Optional. Metadata for the document. The metadata supports
            arbitrary key-value pairs. Suggested use cases include
            storing a document's title, an external URL distinct from
            the document's content_uri, etc. The max size of a ``key``
            or a ``value`` of the metadata is 1024 bytes.
        state (google.cloud.dialogflow_v2.types.Document.State):
            Output only. The current state of the
            document.
    """

    class KnowledgeType(proto.Enum):
        r"""The knowledge type of document content.

        Values:
            KNOWLEDGE_TYPE_UNSPECIFIED (0):
                The type is unspecified or arbitrary.
            FAQ (1):
                The document content contains question and
                answer pairs as either HTML or CSV. Typical FAQ
                HTML formats are parsed accurately, but unusual
                formats may fail to be parsed.

                CSV must have questions in the first column and
                answers in the second, with no header. Because
                of this explicit format, they are always parsed
                accurately.
            EXTRACTIVE_QA (2):
                Documents for which unstructured text is
                extracted and used for question answering.
            ARTICLE_SUGGESTION (3):
                The entire document content as a whole can be
                used for query results. Only for Contact Center
                Solutions on Dialogflow.
            AGENT_FACING_SMART_REPLY (4):
                The document contains agent-facing Smart
                Reply entries.
        """

        KNOWLEDGE_TYPE_UNSPECIFIED = 0
        FAQ = 1
        EXTRACTIVE_QA = 2
        ARTICLE_SUGGESTION = 3
        AGENT_FACING_SMART_REPLY = 4

    class State(proto.Enum):
        r"""Possible states of the document

        Values:
            STATE_UNSPECIFIED (0):
                The document state is unspecified.
            CREATING (1):
                The document creation is in progress.
            ACTIVE (2):
                The document is active and ready to use.
            UPDATING (3):
                The document updation is in progress.
            RELOADING (4):
                The document is reloading.
            DELETING (5):
                The document deletion is in progress.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        ACTIVE = 2
        UPDATING = 3
        RELOADING = 4
        DELETING = 5

    class ReloadStatus(proto.Message):
        r"""The status of a reload attempt.

        Attributes:
            time (google.protobuf.timestamp_pb2.Timestamp):
                The time of a reload attempt.
                This reload may have been triggered
                automatically or manually and may not have
                succeeded.
            status (google.rpc.status_pb2.Status):
                The status of a reload attempt or the initial
                load.
        """

        time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=1,
            message=timestamp_pb2.Timestamp,
        )
        status: status_pb2.Status = proto.Field(
            proto.MESSAGE,
            number=2,
            message=status_pb2.Status,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    mime_type: str = proto.Field(
        proto.STRING,
        number=3,
    )
    knowledge_types: MutableSequence[KnowledgeType] = proto.RepeatedField(
        proto.ENUM,
        number=4,
        enum=KnowledgeType,
    )
    content_uri: str = proto.Field(
        proto.STRING,
        number=5,
        oneof="source",
    )
    raw_content: bytes = proto.Field(
        proto.BYTES,
        number=9,
        oneof="source",
    )
    enable_auto_reload: bool = proto.Field(
        proto.BOOL,
        number=11,
    )
    latest_reload_status: ReloadStatus = proto.Field(
        proto.MESSAGE,
        number=12,
        message=ReloadStatus,
    )
    metadata: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=7,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=13,
        enum=State,
    )


class GetDocumentRequest(proto.Message):
    r"""Request message for
    [Documents.GetDocument][google.cloud.dialogflow.v2.Documents.GetDocument].

    Attributes:
        name (str):
            Required. The name of the document to retrieve. Format
            ``projects/<Project ID>/locations/<Location ID>/knowledgeBases/<Knowledge Base ID>/documents/<Document ID>``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListDocumentsRequest(proto.Message):
    r"""Request message for
    [Documents.ListDocuments][google.cloud.dialogflow.v2.Documents.ListDocuments].

    Attributes:
        parent (str):
            Required. The knowledge base to list all documents for.
            Format:
            ``projects/<Project ID>/locations/<Location ID>/knowledgeBases/<Knowledge Base ID>``.
        page_size (int):
            The maximum number of items to return in a
            single page. By default 10 and at most 100.
        page_token (str):
            The next_page_token value returned from a previous list
            request.
        filter (str):
            The filter expression used to filter documents returned by
            the list method. The expression has the following syntax:

            [AND ] ...

            The following fields and operators are supported:

            - knowledge_types with has(:) operator
            - display_name with has(:) operator
            - state with equals(=) operator

            Examples:

            - "knowledge_types:FAQ" matches documents with FAQ knowledge
              type.
            - "display_name:customer" matches documents whose display
              name contains "customer".
            - "state=ACTIVE" matches documents with ACTIVE state.
            - "knowledge_types:FAQ AND state=ACTIVE" matches all active
              FAQ documents.

            For more information about filtering, see `API
            Filtering <https://aip.dev/160>`__.
    """

    parent: str = proto.Field(
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


class ListDocumentsResponse(proto.Message):
    r"""Response message for
    [Documents.ListDocuments][google.cloud.dialogflow.v2.Documents.ListDocuments].

    Attributes:
        documents (MutableSequence[google.cloud.dialogflow_v2.types.Document]):
            The list of documents.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    documents: MutableSequence["Document"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Document",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateDocumentRequest(proto.Message):
    r"""Request message for
    [Documents.CreateDocument][google.cloud.dialogflow.v2.Documents.CreateDocument].

    Attributes:
        parent (str):
            Required. The knowledge base to create a document for.
            Format:
            ``projects/<Project ID>/locations/<Location ID>/knowledgeBases/<Knowledge Base ID>``.
        document (google.cloud.dialogflow_v2.types.Document):
            Required. The document to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    document: "Document" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Document",
    )


class ImportDocumentsRequest(proto.Message):
    r"""Request message for
    [Documents.ImportDocuments][google.cloud.dialogflow.v2.Documents.ImportDocuments].


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        parent (str):
            Required. The knowledge base to import documents into.
            Format:
            ``projects/<Project ID>/locations/<Location ID>/knowledgeBases/<Knowledge Base ID>``.
        gcs_source (google.cloud.dialogflow_v2.types.GcsSources):
            Optional. The Google Cloud Storage location for the
            documents. The path can include a wildcard.

            These URIs may have the forms
            ``gs://<bucket-name>/<object-name>``.
            ``gs://<bucket-name>/<object-path>/*.<extension>``.

            This field is a member of `oneof`_ ``source``.
        document_template (google.cloud.dialogflow_v2.types.ImportDocumentTemplate):
            Required. Document template used for
            importing all the documents.
        import_gcs_custom_metadata (bool):
            Whether to import custom metadata from Google
            Cloud Storage. Only valid when the document
            source is Google Cloud Storage URI.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    gcs_source: gcs.GcsSources = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="source",
        message=gcs.GcsSources,
    )
    document_template: "ImportDocumentTemplate" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="ImportDocumentTemplate",
    )
    import_gcs_custom_metadata: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class ImportDocumentTemplate(proto.Message):
    r"""The template used for importing documents.

    Attributes:
        mime_type (str):
            Required. The MIME type of the document.
        knowledge_types (MutableSequence[google.cloud.dialogflow_v2.types.Document.KnowledgeType]):
            Required. The knowledge type of document
            content.
        metadata (MutableMapping[str, str]):
            Metadata for the document. The metadata supports arbitrary
            key-value pairs. Suggested use cases include storing a
            document's title, an external URL distinct from the
            document's content_uri, etc. The max size of a ``key`` or a
            ``value`` of the metadata is 1024 bytes.
    """

    mime_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    knowledge_types: MutableSequence["Document.KnowledgeType"] = proto.RepeatedField(
        proto.ENUM,
        number=2,
        enum="Document.KnowledgeType",
    )
    metadata: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=3,
    )


class ImportDocumentsResponse(proto.Message):
    r"""Response message for
    [Documents.ImportDocuments][google.cloud.dialogflow.v2.Documents.ImportDocuments].

    Attributes:
        warnings (MutableSequence[google.rpc.status_pb2.Status]):
            Includes details about skipped documents or
            any other warnings.
    """

    warnings: MutableSequence[status_pb2.Status] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=status_pb2.Status,
    )


class DeleteDocumentRequest(proto.Message):
    r"""Request message for
    [Documents.DeleteDocument][google.cloud.dialogflow.v2.Documents.DeleteDocument].

    Attributes:
        name (str):
            Required. The name of the document to delete. Format:
            ``projects/<Project ID>/locations/<Location ID>/knowledgeBases/<Knowledge Base ID>/documents/<Document ID>``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateDocumentRequest(proto.Message):
    r"""Request message for
    [Documents.UpdateDocument][google.cloud.dialogflow.v2.Documents.UpdateDocument].

    Attributes:
        document (google.cloud.dialogflow_v2.types.Document):
            Required. The document to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Not specified means ``update all``. Currently,
            only ``display_name`` can be updated, an InvalidArgument
            will be returned for attempting to update other fields.
    """

    document: "Document" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Document",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class ReloadDocumentRequest(proto.Message):
    r"""Request message for
    [Documents.ReloadDocument][google.cloud.dialogflow.v2.Documents.ReloadDocument].


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Required. The name of the document to reload. Format:
            ``projects/<Project ID>/locations/<Location ID>/knowledgeBases/<Knowledge Base ID>/documents/<Document ID>``
        content_uri (str):
            Optional. The path of gcs source file for reloading document
            content. For now, only gcs uri is supported.

            For documents stored in Google Cloud Storage, these URIs
            must have the form ``gs://<bucket-name>/<object-name>``.

            This field is a member of `oneof`_ ``source``.
        import_gcs_custom_metadata (bool):
            Optional. Whether to import custom metadata
            from Google Cloud Storage. Only valid when the
            document source is Google Cloud Storage URI.
        smart_messaging_partial_update (bool):
            Optional. When enabled, the reload request is
            to apply partial update to the smart messaging
            allowlist.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    content_uri: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="source",
    )
    import_gcs_custom_metadata: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    smart_messaging_partial_update: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class ExportDocumentRequest(proto.Message):
    r"""Request message for
    [Documents.ExportDocument][google.cloud.dialogflow.v2.Documents.ExportDocument].


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Required. The name of the document to export. Format:
            ``projects/<Project ID>/locations/<Location ID>/knowledgeBases/<Knowledge Base ID>/documents/<Document ID>``.
        gcs_destination (google.cloud.dialogflow_v2.types.GcsDestination):
            Cloud Storage file path to export the
            document.

            This field is a member of `oneof`_ ``destination``.
        export_full_content (bool):
            When enabled, export the full content of the
            document including empirical probability.
        smart_messaging_partial_update (bool):
            When enabled, export the smart messaging
            allowlist document for partial update.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    gcs_destination: gcs.GcsDestination = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="destination",
        message=gcs.GcsDestination,
    )
    export_full_content: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    smart_messaging_partial_update: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class ExportOperationMetadata(proto.Message):
    r"""Metadata related to the Export Data Operations (e.g.
    ExportDocument).

    Attributes:
        exported_gcs_destination (google.cloud.dialogflow_v2.types.GcsDestination):
            Cloud Storage file path of the exported data.
    """

    exported_gcs_destination: gcs.GcsDestination = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcs.GcsDestination,
    )


class KnowledgeOperationMetadata(proto.Message):
    r"""Metadata in google::longrunning::Operation for Knowledge
    operations.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        state (google.cloud.dialogflow_v2.types.KnowledgeOperationMetadata.State):
            Output only. The current state of this
            operation.
        knowledge_base (str):
            The name of the knowledge base interacted
            with during the operation.
        export_operation_metadata (google.cloud.dialogflow_v2.types.ExportOperationMetadata):
            Metadata for the Export Data Operation such
            as the destination of export.

            This field is a member of `oneof`_ ``operation_metadata``.
        done_time (google.protobuf.timestamp_pb2.Timestamp):
            The time when the operation finished.
    """

    class State(proto.Enum):
        r"""States of the operation.

        Values:
            STATE_UNSPECIFIED (0):
                State unspecified.
            PENDING (1):
                The operation has been created.
            RUNNING (2):
                The operation is currently running.
            DONE (3):
                The operation is done, either cancelled or
                completed.
        """

        STATE_UNSPECIFIED = 0
        PENDING = 1
        RUNNING = 2
        DONE = 3

    state: State = proto.Field(
        proto.ENUM,
        number=1,
        enum=State,
    )
    knowledge_base: str = proto.Field(
        proto.STRING,
        number=3,
    )
    export_operation_metadata: "ExportOperationMetadata" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="operation_metadata",
        message="ExportOperationMetadata",
    )
    done_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
