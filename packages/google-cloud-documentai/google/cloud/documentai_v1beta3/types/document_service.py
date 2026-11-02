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
import google.rpc.status_pb2 as status_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.documentai_v1beta3.types import dataset as gcd_dataset
from google.cloud.documentai_v1beta3.types import document as gcd_document
from google.cloud.documentai_v1beta3.types import document_io, operation_metadata

__protobuf__ = proto.module(
    package="google.cloud.documentai.v1beta3",
    manifest={
        "DatasetSplitType",
        "DocumentLabelingState",
        "UpdateDatasetRequest",
        "UpdateDatasetOperationMetadata",
        "ImportDocumentsRequest",
        "ImportDocumentsResponse",
        "ImportDocumentsMetadata",
        "GetDocumentRequest",
        "GetDocumentResponse",
        "ListDocumentsRequest",
        "ListDocumentsResponse",
        "BatchDeleteDocumentsRequest",
        "BatchDeleteDocumentsResponse",
        "BatchDeleteDocumentsMetadata",
        "GetDatasetSchemaRequest",
        "UpdateDatasetSchemaRequest",
        "DocumentPageRange",
        "DocumentMetadata",
    },
)


class DatasetSplitType(proto.Enum):
    r"""Documents belonging to a dataset will be split into different
    groups referred to as splits: train, test.

    Values:
        DATASET_SPLIT_TYPE_UNSPECIFIED (0):
            Default value if the enum is not set.
        DATASET_SPLIT_TRAIN (1):
            Identifies the train documents.
        DATASET_SPLIT_TEST (2):
            Identifies the test documents.
        DATASET_SPLIT_UNASSIGNED (3):
            Identifies the unassigned documents.
    """

    DATASET_SPLIT_TYPE_UNSPECIFIED = 0
    DATASET_SPLIT_TRAIN = 1
    DATASET_SPLIT_TEST = 2
    DATASET_SPLIT_UNASSIGNED = 3


class DocumentLabelingState(proto.Enum):
    r"""Describes the labeling status of a document.

    Values:
        DOCUMENT_LABELING_STATE_UNSPECIFIED (0):
            Default value if the enum is not set.
        DOCUMENT_LABELED (1):
            Document has been labeled.
        DOCUMENT_UNLABELED (2):
            Document has not been labeled.
        DOCUMENT_AUTO_LABELED (3):
            Document has been auto-labeled.
    """

    DOCUMENT_LABELING_STATE_UNSPECIFIED = 0
    DOCUMENT_LABELED = 1
    DOCUMENT_UNLABELED = 2
    DOCUMENT_AUTO_LABELED = 3


class UpdateDatasetRequest(proto.Message):
    r"""

    Attributes:
        dataset (google.cloud.documentai_v1beta3.types.Dataset):
            Required. The ``name`` field of the ``Dataset`` is used to
            identify the resource to be updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The update mask applies to the resource.
    """

    dataset: gcd_dataset.Dataset = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcd_dataset.Dataset,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class UpdateDatasetOperationMetadata(proto.Message):
    r"""

    Attributes:
        common_metadata (google.cloud.documentai_v1beta3.types.CommonOperationMetadata):
            The basic metadata of the long-running
            operation.
    """

    common_metadata: operation_metadata.CommonOperationMetadata = proto.Field(
        proto.MESSAGE,
        number=1,
        message=operation_metadata.CommonOperationMetadata,
    )


class ImportDocumentsRequest(proto.Message):
    r"""

    Attributes:
        dataset (str):
            Required. The dataset resource name.
            Format:

            projects/{project}/locations/{location}/processors/{processor}/dataset
        batch_documents_import_configs (MutableSequence[google.cloud.documentai_v1beta3.types.ImportDocumentsRequest.BatchDocumentsImportConfig]):
            Required. The Cloud Storage uri containing
            raw documents that must be imported.
    """

    class BatchDocumentsImportConfig(proto.Message):
        r"""Config for importing documents.
        Each batch can have its own dataset split type.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            dataset_split (google.cloud.documentai_v1beta3.types.DatasetSplitType):
                Target dataset split where the documents must
                be stored.

                This field is a member of `oneof`_ ``split_type_config``.
            auto_split_config (google.cloud.documentai_v1beta3.types.ImportDocumentsRequest.BatchDocumentsImportConfig.AutoSplitConfig):
                If set, documents will be automatically split
                into training and test split category with the
                specified ratio.

                This field is a member of `oneof`_ ``split_type_config``.
            batch_input_config (google.cloud.documentai_v1beta3.types.BatchDocumentsInputConfig):
                The common config to specify a set of
                documents used as input.
            document_type (str):
                Optional. If set, determines the type of the documents to be
                imported in this batch. It can be used to auto-label the
                documents with a single entity of the provided type. This
                field can only be used with a classifier or splitter
                processor. Providing this field is mutually exclusive with
                ``entities`` and ``auto_labeling_config``.
        """

        class AutoSplitConfig(proto.Message):
            r"""The config for auto-split.

            Attributes:
                training_split_ratio (float):
                    Ratio of training dataset split.
            """

            training_split_ratio: float = proto.Field(
                proto.FLOAT,
                number=1,
            )

        dataset_split: "DatasetSplitType" = proto.Field(
            proto.ENUM,
            number=2,
            oneof="split_type_config",
            enum="DatasetSplitType",
        )
        auto_split_config: "ImportDocumentsRequest.BatchDocumentsImportConfig.AutoSplitConfig" = proto.Field(
            proto.MESSAGE,
            number=3,
            oneof="split_type_config",
            message="ImportDocumentsRequest.BatchDocumentsImportConfig.AutoSplitConfig",
        )
        batch_input_config: document_io.BatchDocumentsInputConfig = proto.Field(
            proto.MESSAGE,
            number=1,
            message=document_io.BatchDocumentsInputConfig,
        )
        document_type: str = proto.Field(
            proto.STRING,
            number=6,
        )

    dataset: str = proto.Field(
        proto.STRING,
        number=1,
    )
    batch_documents_import_configs: MutableSequence[BatchDocumentsImportConfig] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=4,
            message=BatchDocumentsImportConfig,
        )
    )


class ImportDocumentsResponse(proto.Message):
    r"""Response of the import document operation."""


class ImportDocumentsMetadata(proto.Message):
    r"""Metadata of the import document operation.

    Attributes:
        common_metadata (google.cloud.documentai_v1beta3.types.CommonOperationMetadata):
            The basic metadata of the long-running
            operation.
        individual_import_statuses (MutableSequence[google.cloud.documentai_v1beta3.types.ImportDocumentsMetadata.IndividualImportStatus]):
            The list of response details of each
            document.
        import_config_validation_results (MutableSequence[google.cloud.documentai_v1beta3.types.ImportDocumentsMetadata.ImportConfigValidationResult]):
            Validation statuses of the batch documents
            import config.
        total_document_count (int):
            Total number of the documents that are
            qualified for importing.
    """

    class IndividualImportStatus(proto.Message):
        r"""The status of each individual document in the import process.

        Attributes:
            input_gcs_source (str):
                The source Cloud Storage URI of the document.
            status (google.rpc.status_pb2.Status):
                The status of the importing of the document.
            output_document_id (google.cloud.documentai_v1beta3.types.DocumentId):
                The document id of imported document if it
                was successful, otherwise empty.
        """

        input_gcs_source: str = proto.Field(
            proto.STRING,
            number=1,
        )
        status: status_pb2.Status = proto.Field(
            proto.MESSAGE,
            number=2,
            message=status_pb2.Status,
        )
        output_document_id: gcd_dataset.DocumentId = proto.Field(
            proto.MESSAGE,
            number=4,
            message=gcd_dataset.DocumentId,
        )

    class ImportConfigValidationResult(proto.Message):
        r"""The validation status of each import config. Status is set to an
        error if there are no documents to import in the ``import_config``,
        or ``OK`` if the operation will try to proceed with at least one
        document.

        Attributes:
            input_gcs_source (str):
                The source Cloud Storage URI specified in the
                import config.
            status (google.rpc.status_pb2.Status):
                The validation status of import config.
        """

        input_gcs_source: str = proto.Field(
            proto.STRING,
            number=1,
        )
        status: status_pb2.Status = proto.Field(
            proto.MESSAGE,
            number=2,
            message=status_pb2.Status,
        )

    common_metadata: operation_metadata.CommonOperationMetadata = proto.Field(
        proto.MESSAGE,
        number=1,
        message=operation_metadata.CommonOperationMetadata,
    )
    individual_import_statuses: MutableSequence[IndividualImportStatus] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message=IndividualImportStatus,
        )
    )
    import_config_validation_results: MutableSequence[ImportConfigValidationResult] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=4,
            message=ImportConfigValidationResult,
        )
    )
    total_document_count: int = proto.Field(
        proto.INT32,
        number=3,
    )


class GetDocumentRequest(proto.Message):
    r"""

    Attributes:
        dataset (str):
            Required. The resource name of the dataset
            that the document belongs to . Format:

            projects/{project}/locations/{location}/processors/{processor}/dataset
        document_id (google.cloud.documentai_v1beta3.types.DocumentId):
            Required. Document identifier.
        read_mask (google.protobuf.field_mask_pb2.FieldMask):
            If set, only fields listed here will be
            returned. Otherwise, all fields will be returned
            by default.
        page_range (google.cloud.documentai_v1beta3.types.DocumentPageRange):
            List of pages for which the fields specified in the
            ``read_mask`` must be served.
    """

    dataset: str = proto.Field(
        proto.STRING,
        number=1,
    )
    document_id: gcd_dataset.DocumentId = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcd_dataset.DocumentId,
    )
    read_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=3,
        message=field_mask_pb2.FieldMask,
    )
    page_range: "DocumentPageRange" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="DocumentPageRange",
    )


class GetDocumentResponse(proto.Message):
    r"""

    Attributes:
        document (google.cloud.documentai_v1beta3.types.Document):

    """

    document: gcd_document.Document = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcd_document.Document,
    )


class ListDocumentsRequest(proto.Message):
    r"""

    Attributes:
        dataset (str):
            Required. The resource name of the dataset to
            be listed. Format:

            projects/{project}/locations/{location}/processors/{processor}/dataset
        page_size (int):
            The maximum number of documents to return.
            The service may return fewer than this value. If
            unspecified, at most 20 documents will be
            returned. The maximum value is 100; values above
            100 will be coerced to 100.
        page_token (str):
            A page token, received from a previous ``ListDocuments``
            call. Provide this to retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``ListDocuments`` must match the call that provided the page
            token.
        filter (str):
            Optional. Query to filter the documents based on
            https://google.aip.dev/160.

            Currently support query strings are:
            ------------------------------------

            ``SplitType=DATASET_SPLIT_TEST|DATASET_SPLIT_TRAIN|DATASET_SPLIT_UNASSIGNED``

            - ``LabelingState=DOCUMENT_LABELED|DOCUMENT_UNLABELED|DOCUMENT_AUTO_LABELED``
            - ``DisplayName=\"file_name.pdf\"``
            - ``EntityType=abc/def``
            - ``TagName=\"auto-labeling-running\"|\"sampled\"``

            Note:

            - Only ``AND``, ``=`` and ``!=`` are supported. e.g.
              ``DisplayName=file_name AND EntityType!=abc`` IS
              supported.
            - Wildcard ``*`` is supported only in ``DisplayName`` filter
            - No duplicate filter keys are allowed, e.g.
              ``EntityType=a AND EntityType=b`` is NOT supported.
            - String match is case sensitive (for filter ``DisplayName``
              & ``EntityType``).
        return_total_size (bool):
            Optional. Controls if the request requires a total size of
            matched documents. See
            [ListDocumentsResponse.total_size][google.cloud.documentai.v1beta3.ListDocumentsResponse.total_size].

            Enabling this flag may adversely impact performance.

            Defaults to false.
        skip (int):
            Optional. Number of results to skip beginning from the
            ``page_token`` if provided.
            https://google.aip.dev/158#skipping-results. It must be a
            non-negative integer. Negative values will be rejected. Note
            that this is not the number of pages to skip. If this value
            causes the cursor to move past the end of results,
            [ListDocumentsResponse.document_metadata][google.cloud.documentai.v1beta3.ListDocumentsResponse.document_metadata]
            and
            [ListDocumentsResponse.next_page_token][google.cloud.documentai.v1beta3.ListDocumentsResponse.next_page_token]
            will be empty.
    """

    dataset: str = proto.Field(
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
    return_total_size: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    skip: int = proto.Field(
        proto.INT32,
        number=8,
    )


class ListDocumentsResponse(proto.Message):
    r"""

    Attributes:
        document_metadata (MutableSequence[google.cloud.documentai_v1beta3.types.DocumentMetadata]):
            Document metadata corresponding to the listed
            documents.
        next_page_token (str):
            A token, which can be sent as
            [ListDocumentsRequest.page_token][google.cloud.documentai.v1beta3.ListDocumentsRequest.page_token]
            to retrieve the next page. If this field is omitted, there
            are no subsequent pages.
        total_size (int):
            Total count of documents queried.
    """

    @property
    def raw_page(self):
        return self

    document_metadata: MutableSequence["DocumentMetadata"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="DocumentMetadata",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    total_size: int = proto.Field(
        proto.INT32,
        number=3,
    )


class BatchDeleteDocumentsRequest(proto.Message):
    r"""

    Attributes:
        dataset (str):
            Required. The dataset resource name.
            Format:

            projects/{project}/locations/{location}/processors/{processor}/dataset
        dataset_documents (google.cloud.documentai_v1beta3.types.BatchDatasetDocuments):
            Required. Dataset documents input. If given ``filter``, all
            documents satisfying the filter will be deleted. If given
            documentIds, a maximum of 50 documents can be deleted in a
            batch. The request will be rejected if more than 50
            document_ids are provided.
    """

    dataset: str = proto.Field(
        proto.STRING,
        number=1,
    )
    dataset_documents: gcd_dataset.BatchDatasetDocuments = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gcd_dataset.BatchDatasetDocuments,
    )


class BatchDeleteDocumentsResponse(proto.Message):
    r"""Response of the delete documents operation."""


class BatchDeleteDocumentsMetadata(proto.Message):
    r"""

    Attributes:
        common_metadata (google.cloud.documentai_v1beta3.types.CommonOperationMetadata):
            The basic metadata of the long-running
            operation.
        individual_batch_delete_statuses (MutableSequence[google.cloud.documentai_v1beta3.types.BatchDeleteDocumentsMetadata.IndividualBatchDeleteStatus]):
            The list of response details of each
            document.
        total_document_count (int):
            Total number of documents deleting from
            dataset.
        error_document_count (int):
            Total number of documents that failed to be
            deleted in storage.
    """

    class IndividualBatchDeleteStatus(proto.Message):
        r"""The status of each individual document in the batch delete
        process.

        Attributes:
            document_id (google.cloud.documentai_v1beta3.types.DocumentId):
                The document id of the document.
            status (google.rpc.status_pb2.Status):
                The status of deleting the document in
                storage.
        """

        document_id: gcd_dataset.DocumentId = proto.Field(
            proto.MESSAGE,
            number=1,
            message=gcd_dataset.DocumentId,
        )
        status: status_pb2.Status = proto.Field(
            proto.MESSAGE,
            number=2,
            message=status_pb2.Status,
        )

    common_metadata: operation_metadata.CommonOperationMetadata = proto.Field(
        proto.MESSAGE,
        number=1,
        message=operation_metadata.CommonOperationMetadata,
    )
    individual_batch_delete_statuses: MutableSequence[IndividualBatchDeleteStatus] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message=IndividualBatchDeleteStatus,
        )
    )
    total_document_count: int = proto.Field(
        proto.INT32,
        number=3,
    )
    error_document_count: int = proto.Field(
        proto.INT32,
        number=4,
    )


class GetDatasetSchemaRequest(proto.Message):
    r"""Request for ``GetDatasetSchema``.

    Attributes:
        name (str):
            Required. The dataset schema resource name.
            Format:

            projects/{project}/locations/{location}/processors/{processor}/dataset/datasetSchema
        visible_fields_only (bool):
            If set, only returns the visible fields of
            the schema.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    visible_fields_only: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class UpdateDatasetSchemaRequest(proto.Message):
    r"""Request for ``UpdateDatasetSchema``.

    Attributes:
        dataset_schema (google.cloud.documentai_v1beta3.types.DatasetSchema):
            Required. The name field of the ``DatasetSchema`` is used to
            identify the resource to be updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The update mask applies to the resource.
    """

    dataset_schema: gcd_dataset.DatasetSchema = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcd_dataset.DatasetSchema,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DocumentPageRange(proto.Message):
    r"""Range of pages present in a document.

    Attributes:
        start (int):
            First page number (one-based index) to be
            returned.
        end (int):
            Last page number (one-based index) to be
            returned.
    """

    start: int = proto.Field(
        proto.INT32,
        number=1,
    )
    end: int = proto.Field(
        proto.INT32,
        number=2,
    )


class DocumentMetadata(proto.Message):
    r"""Metadata about a document.

    Attributes:
        document_id (google.cloud.documentai_v1beta3.types.DocumentId):
            Document identifier.
        page_count (int):
            Number of pages in the document.
        dataset_type (google.cloud.documentai_v1beta3.types.DatasetSplitType):
            Type of the dataset split to which the
            document belongs.
        labeling_state (google.cloud.documentai_v1beta3.types.DocumentLabelingState):
            Labeling state of the document.
        display_name (str):
            The display name of the document.
    """

    document_id: gcd_dataset.DocumentId = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcd_dataset.DocumentId,
    )
    page_count: int = proto.Field(
        proto.INT32,
        number=2,
    )
    dataset_type: "DatasetSplitType" = proto.Field(
        proto.ENUM,
        number=3,
        enum="DatasetSplitType",
    )
    labeling_state: "DocumentLabelingState" = proto.Field(
        proto.ENUM,
        number=5,
        enum="DocumentLabelingState",
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=6,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
