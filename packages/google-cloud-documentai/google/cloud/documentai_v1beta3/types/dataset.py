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

from google.cloud.documentai_v1beta3.types import document, document_io
from google.cloud.documentai_v1beta3.types import document_schema as gcd_document_schema

__protobuf__ = proto.module(
    package="google.cloud.documentai.v1beta3",
    manifest={
        "Dataset",
        "DocumentId",
        "DatasetSchema",
        "BatchDatasetDocuments",
    },
)


class Dataset(proto.Message):
    r"""A singleton resource under a
    [Processor][google.cloud.documentai.v1beta3.Processor] which
    configures a collection of documents.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        gcs_managed_config (google.cloud.documentai_v1beta3.types.Dataset.GCSManagedConfig):
            Optional. User-managed Cloud Storage dataset
            configuration. Use this configuration if the
            dataset documents are stored under a
            user-managed Cloud Storage location.

            This field is a member of `oneof`_ ``storage_source``.
        document_warehouse_config (google.cloud.documentai_v1beta3.types.Dataset.DocumentWarehouseConfig):
            Optional. Deprecated. Warehouse-based dataset
            configuration is not supported.

            This field is a member of `oneof`_ ``storage_source``.
        unmanaged_dataset_config (google.cloud.documentai_v1beta3.types.Dataset.UnmanagedDatasetConfig):
            Optional. Unmanaged dataset configuration.
            Use this configuration if the dataset documents
            are managed by the document service internally
            (not user-managed).

            This field is a member of `oneof`_ ``storage_source``.
        name (str):
            Dataset resource name. Format:
            ``projects/{project}/locations/{location}/processors/{processor}/dataset``
        state (google.cloud.documentai_v1beta3.types.Dataset.State):
            Required. State of the dataset. Ignored when
            updating dataset.
        satisfies_pzs (bool):
            Output only. Reserved for future use.
        satisfies_pzi (bool):
            Output only. Reserved for future use.
    """

    class State(proto.Enum):
        r"""Different states of a dataset.

        Values:
            STATE_UNSPECIFIED (0):
                Default unspecified enum, should not be used.
            UNINITIALIZED (1):
                Dataset has not been initialized.
            INITIALIZING (2):
                Dataset is being initialized.
            INITIALIZED (3):
                Dataset has been initialized.
        """

        STATE_UNSPECIFIED = 0
        UNINITIALIZED = 1
        INITIALIZING = 2
        INITIALIZED = 3

    class GCSManagedConfig(proto.Message):
        r"""Configuration specific to the Cloud Storage-based
        implementation.

        Attributes:
            gcs_prefix (google.cloud.documentai_v1beta3.types.GcsPrefix):
                Required. The Cloud Storage URI (a directory)
                where the documents belonging to the dataset
                must be stored.
        """

        gcs_prefix: document_io.GcsPrefix = proto.Field(
            proto.MESSAGE,
            number=1,
            message=document_io.GcsPrefix,
        )

    class DocumentWarehouseConfig(proto.Message):
        r"""Configuration specific to the Document AI Warehouse-based
        implementation.

        Attributes:
            collection (str):
                Output only. The collection in Document AI
                Warehouse associated with the dataset.
            schema (str):
                Output only. The schema in Document AI
                Warehouse associated with the dataset.
        """

        collection: str = proto.Field(
            proto.STRING,
            number=1,
        )
        schema: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class UnmanagedDatasetConfig(proto.Message):
        r"""Configuration specific to an unmanaged dataset."""

    gcs_managed_config: GCSManagedConfig = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="storage_source",
        message=GCSManagedConfig,
    )
    document_warehouse_config: DocumentWarehouseConfig = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="storage_source",
        message=DocumentWarehouseConfig,
    )
    unmanaged_dataset_config: UnmanagedDatasetConfig = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="storage_source",
        message=UnmanagedDatasetConfig,
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=2,
        enum=State,
    )
    satisfies_pzs: bool = proto.Field(
        proto.BOOL,
        number=8,
    )
    satisfies_pzi: bool = proto.Field(
        proto.BOOL,
        number=9,
    )


class DocumentId(proto.Message):
    r"""Document Identifier.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        gcs_managed_doc_id (google.cloud.documentai_v1beta3.types.DocumentId.GCSManagedDocumentId):
            A document id within user-managed Cloud
            Storage.

            This field is a member of `oneof`_ ``type``.
        unmanaged_doc_id (google.cloud.documentai_v1beta3.types.DocumentId.UnmanagedDocumentId):
            A document id within unmanaged dataset.

            This field is a member of `oneof`_ ``type``.
        revision_ref (google.cloud.documentai_v1beta3.types.RevisionRef):
            Points to a specific revision of the document
            if set.
    """

    class GCSManagedDocumentId(proto.Message):
        r"""Identifies a document uniquely within the scope of a dataset
        in the user-managed Cloud Storage option.

        Attributes:
            gcs_uri (str):
                Required. The Cloud Storage URI where the
                actual document is stored.
            cw_doc_id (str):
                Id of the document (indexed) managed by
                Content Warehouse.
        """

        gcs_uri: str = proto.Field(
            proto.STRING,
            number=1,
        )
        cw_doc_id: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class UnmanagedDocumentId(proto.Message):
        r"""Identifies a document uniquely within the scope of a dataset
        in unmanaged option.

        Attributes:
            doc_id (str):
                Required. The id of the document.
        """

        doc_id: str = proto.Field(
            proto.STRING,
            number=1,
        )

    gcs_managed_doc_id: GCSManagedDocumentId = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="type",
        message=GCSManagedDocumentId,
    )
    unmanaged_doc_id: UnmanagedDocumentId = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="type",
        message=UnmanagedDocumentId,
    )
    revision_ref: document.RevisionRef = proto.Field(
        proto.MESSAGE,
        number=3,
        message=document.RevisionRef,
    )


class DatasetSchema(proto.Message):
    r"""Dataset Schema.

    Attributes:
        name (str):
            Dataset schema resource name. Format:
            ``projects/{project}/locations/{location}/processors/{processor}/dataset/datasetSchema``
        document_schema (google.cloud.documentai_v1beta3.types.DocumentSchema):
            Optional. Schema of the dataset.
        satisfies_pzs (bool):
            Output only. Reserved for future use.
        satisfies_pzi (bool):
            Output only. Reserved for future use.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    document_schema: gcd_document_schema.DocumentSchema = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gcd_document_schema.DocumentSchema,
    )
    satisfies_pzs: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    satisfies_pzi: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class BatchDatasetDocuments(proto.Message):
    r"""Dataset documents that the batch operation will be applied
    to.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        individual_document_ids (google.cloud.documentai_v1beta3.types.BatchDatasetDocuments.IndividualDocumentIds):
            Document identifiers.

            This field is a member of `oneof`_ ``criteria``.
        filter (str):
            A filter matching the documents. Follows the same format and
            restriction as
            [google.cloud.documentai.master.ListDocumentsRequest.filter].

            This field is a member of `oneof`_ ``criteria``.
    """

    class IndividualDocumentIds(proto.Message):
        r"""List of individual DocumentIds.

        Attributes:
            document_ids (MutableSequence[google.cloud.documentai_v1beta3.types.DocumentId]):
                Required. List of Document IDs indicating
                where the actual documents are stored.
        """

        document_ids: MutableSequence["DocumentId"] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="DocumentId",
        )

    individual_document_ids: IndividualDocumentIds = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="criteria",
        message=IndividualDocumentIds,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="criteria",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
