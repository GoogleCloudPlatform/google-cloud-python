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

from google.cloud.documentai_v1.types import document as gcd_document
from google.cloud.documentai_v1.types import (
    document_io,
    operation_metadata,
    processor_type,
)
from google.cloud.documentai_v1.types import document_schema as gcd_document_schema
from google.cloud.documentai_v1.types import evaluation as gcd_evaluation
from google.cloud.documentai_v1.types import processor as gcd_processor

__protobuf__ = proto.module(
    package="google.cloud.documentai.v1",
    manifest={
        "ProcessOptions",
        "ProcessRequest",
        "HumanReviewStatus",
        "ProcessResponse",
        "BatchProcessRequest",
        "BatchProcessResponse",
        "BatchProcessMetadata",
        "FetchProcessorTypesRequest",
        "FetchProcessorTypesResponse",
        "ListProcessorTypesRequest",
        "ListProcessorTypesResponse",
        "ListProcessorsRequest",
        "ListProcessorsResponse",
        "GetProcessorTypeRequest",
        "GetProcessorRequest",
        "GetProcessorVersionRequest",
        "ListProcessorVersionsRequest",
        "ListProcessorVersionsResponse",
        "DeleteProcessorVersionRequest",
        "DeleteProcessorVersionMetadata",
        "DeployProcessorVersionRequest",
        "DeployProcessorVersionResponse",
        "DeployProcessorVersionMetadata",
        "UndeployProcessorVersionRequest",
        "UndeployProcessorVersionResponse",
        "UndeployProcessorVersionMetadata",
        "CreateProcessorRequest",
        "DeleteProcessorRequest",
        "DeleteProcessorMetadata",
        "EnableProcessorRequest",
        "EnableProcessorResponse",
        "EnableProcessorMetadata",
        "DisableProcessorRequest",
        "DisableProcessorResponse",
        "DisableProcessorMetadata",
        "SetDefaultProcessorVersionRequest",
        "SetDefaultProcessorVersionResponse",
        "SetDefaultProcessorVersionMetadata",
        "TrainProcessorVersionRequest",
        "TrainProcessorVersionResponse",
        "TrainProcessorVersionMetadata",
        "ReviewDocumentRequest",
        "ReviewDocumentResponse",
        "ReviewDocumentOperationMetadata",
        "EvaluateProcessorVersionRequest",
        "EvaluateProcessorVersionMetadata",
        "EvaluateProcessorVersionResponse",
        "GetEvaluationRequest",
        "ListEvaluationsRequest",
        "ListEvaluationsResponse",
    },
)


class ProcessOptions(proto.Message):
    r"""Options for Process API

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        individual_page_selector (google.cloud.documentai_v1.types.ProcessOptions.IndividualPageSelector):
            Which pages to process (1-indexed).

            This field is a member of `oneof`_ ``page_range``.
        from_start (int):
            Only process certain pages from the start.
            Process all if the document has fewer pages.

            This field is a member of `oneof`_ ``page_range``.
        from_end (int):
            Only process certain pages from the end, same
            as above.

            This field is a member of `oneof`_ ``page_range``.
        ocr_config (google.cloud.documentai_v1.types.OcrConfig):
            Only applicable to ``OCR_PROCESSOR`` and
            ``FORM_PARSER_PROCESSOR``. Returns error if set on other
            processor types.
        layout_config (google.cloud.documentai_v1.types.ProcessOptions.LayoutConfig):
            Optional. Only applicable to ``LAYOUT_PARSER_PROCESSOR``.
            Returns error if set on other processor types.
        schema_override (google.cloud.documentai_v1.types.DocumentSchema):
            Optional. Override the schema of the
            [ProcessorVersion][google.cloud.documentai.v1.ProcessorVersion].
            Will return an Invalid Argument error if this field is set
            when the underlying
            [ProcessorVersion][google.cloud.documentai.v1.ProcessorVersion]
            doesn't support schema override.
    """

    class LayoutConfig(proto.Message):
        r"""Serving config for layout parser processor.

        Attributes:
            chunking_config (google.cloud.documentai_v1.types.ProcessOptions.LayoutConfig.ChunkingConfig):
                Optional. Config for chunking in layout
                parser processor.
            return_images (bool):
                Optional. Whether to include images in layout
                parser processor response.
            return_bounding_boxes (bool):
                Optional. Whether to include bounding boxes
                in layout parser processor response.
            enable_image_annotation (bool):
                Optional. Whether to include image
                annotations in layout parser response.
            enable_table_annotation (bool):
                Optional. Whether to include table
                annotations in layout parser response.
        """

        class ChunkingConfig(proto.Message):
            r"""Serving config for chunking.

            Attributes:
                chunk_size (int):
                    Optional. The chunk sizes to use when
                    splitting documents, in order of level.
                include_ancestor_headings (bool):
                    Optional. Whether or not to include ancestor
                    headings when splitting.
            """

            chunk_size: int = proto.Field(
                proto.INT32,
                number=1,
            )
            include_ancestor_headings: bool = proto.Field(
                proto.BOOL,
                number=2,
            )

        chunking_config: "ProcessOptions.LayoutConfig.ChunkingConfig" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="ProcessOptions.LayoutConfig.ChunkingConfig",
        )
        return_images: bool = proto.Field(
            proto.BOOL,
            number=2,
        )
        return_bounding_boxes: bool = proto.Field(
            proto.BOOL,
            number=3,
        )
        enable_image_annotation: bool = proto.Field(
            proto.BOOL,
            number=4,
        )
        enable_table_annotation: bool = proto.Field(
            proto.BOOL,
            number=6,
        )

    class IndividualPageSelector(proto.Message):
        r"""A list of individual page numbers.

        Attributes:
            pages (MutableSequence[int]):
                Optional. Indices of the pages (starting from
                1).
        """

        pages: MutableSequence[int] = proto.RepeatedField(
            proto.INT32,
            number=1,
        )

    individual_page_selector: IndividualPageSelector = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="page_range",
        message=IndividualPageSelector,
    )
    from_start: int = proto.Field(
        proto.INT32,
        number=6,
        oneof="page_range",
    )
    from_end: int = proto.Field(
        proto.INT32,
        number=7,
        oneof="page_range",
    )
    ocr_config: document_io.OcrConfig = proto.Field(
        proto.MESSAGE,
        number=1,
        message=document_io.OcrConfig,
    )
    layout_config: LayoutConfig = proto.Field(
        proto.MESSAGE,
        number=9,
        message=LayoutConfig,
    )
    schema_override: gcd_document_schema.DocumentSchema = proto.Field(
        proto.MESSAGE,
        number=8,
        message=gcd_document_schema.DocumentSchema,
    )


class ProcessRequest(proto.Message):
    r"""Request message for the
    [ProcessDocument][google.cloud.documentai.v1.DocumentProcessorService.ProcessDocument]
    method.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        inline_document (google.cloud.documentai_v1.types.Document):
            An inline document proto.

            This field is a member of `oneof`_ ``source``.
        raw_document (google.cloud.documentai_v1.types.RawDocument):
            A raw document content (bytes).

            This field is a member of `oneof`_ ``source``.
        gcs_document (google.cloud.documentai_v1.types.GcsDocument):
            A raw document on Google Cloud Storage.

            This field is a member of `oneof`_ ``source``.
        name (str):
            Required. The resource name of the
            [Processor][google.cloud.documentai.v1.Processor] or
            [ProcessorVersion][google.cloud.documentai.v1.ProcessorVersion]
            to use for processing. If a
            [Processor][google.cloud.documentai.v1.Processor] is
            specified, the server will use its [default
            version][google.cloud.documentai.v1.Processor.default_processor_version].
            Format:
            ``projects/{project}/locations/{location}/processors/{processor}``,
            or
            ``projects/{project}/locations/{location}/processors/{processor}/processorVersions/{processorVersion}``
        skip_human_review (bool):
            Whether human review should be skipped for this request.
            Default to ``false``.
        field_mask (google.protobuf.field_mask_pb2.FieldMask):
            Specifies which fields to include in the
            [ProcessResponse.document][google.cloud.documentai.v1.ProcessResponse.document]
            output. Only supports top-level document and pages field, so
            it must be in the form of ``{document_field_name}`` or
            ``pages.{page_field_name}``.
        process_options (google.cloud.documentai_v1.types.ProcessOptions):
            Inference-time options for the process API
        labels (MutableMapping[str, str]):
            Optional. The labels with user-defined
            metadata for the request.
            Label keys and values can be no longer than 63
            characters (Unicode codepoints) and can only
            contain lowercase letters, numeric characters,
            underscores, and dashes. International
            characters are allowed. Label values are
            optional. Label keys must start with a letter.
        imageless_mode (bool):
            Optional. Option to remove images from the
            document.
    """

    inline_document: gcd_document.Document = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="source",
        message=gcd_document.Document,
    )
    raw_document: document_io.RawDocument = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="source",
        message=document_io.RawDocument,
    )
    gcs_document: document_io.GcsDocument = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="source",
        message=document_io.GcsDocument,
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    skip_human_review: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    field_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=6,
        message=field_mask_pb2.FieldMask,
    )
    process_options: "ProcessOptions" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="ProcessOptions",
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=10,
    )
    imageless_mode: bool = proto.Field(
        proto.BOOL,
        number=11,
    )


class HumanReviewStatus(proto.Message):
    r"""The status of human review on a processed document.

    Attributes:
        state (google.cloud.documentai_v1.types.HumanReviewStatus.State):
            The state of human review on the processing
            request.
        state_message (str):
            A message providing more details about the
            human review state.
        human_review_operation (str):
            The name of the operation triggered by the processed
            document. This field is populated only when the
            [state][google.cloud.documentai.v1.HumanReviewStatus.state]
            is ``HUMAN_REVIEW_IN_PROGRESS``. It has the same response
            type and metadata as the long-running operation returned by
            [ReviewDocument][google.cloud.documentai.v1.DocumentProcessorService.ReviewDocument].
    """

    class State(proto.Enum):
        r"""The final state of human review on a processed document.

        Values:
            STATE_UNSPECIFIED (0):
                Human review state is unspecified. Most
                likely due to an internal error.
            SKIPPED (1):
                Human review is skipped for the document.
                This can happen because human review isn't
                enabled on the processor or the processing
                request has been set to skip this document.
            VALIDATION_PASSED (2):
                Human review validation is triggered and
                passed, so no review is needed.
            IN_PROGRESS (3):
                Human review validation is triggered and the
                document is under review.
            ERROR (4):
                Some error happened during triggering human review, see the
                [state_message][google.cloud.documentai.v1.HumanReviewStatus.state_message]
                for details.
        """

        STATE_UNSPECIFIED = 0
        SKIPPED = 1
        VALIDATION_PASSED = 2
        IN_PROGRESS = 3
        ERROR = 4

    state: State = proto.Field(
        proto.ENUM,
        number=1,
        enum=State,
    )
    state_message: str = proto.Field(
        proto.STRING,
        number=2,
    )
    human_review_operation: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ProcessResponse(proto.Message):
    r"""Response message for the
    [ProcessDocument][google.cloud.documentai.v1.DocumentProcessorService.ProcessDocument]
    method.

    Attributes:
        document (google.cloud.documentai_v1.types.Document):
            The document payload, will populate fields
            based on the processor's behavior.
        human_review_status (google.cloud.documentai_v1.types.HumanReviewStatus):
            The status of human review on the processed
            document.
    """

    document: gcd_document.Document = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcd_document.Document,
    )
    human_review_status: "HumanReviewStatus" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="HumanReviewStatus",
    )


class BatchProcessRequest(proto.Message):
    r"""Request message for
    [BatchProcessDocuments][google.cloud.documentai.v1.DocumentProcessorService.BatchProcessDocuments].

    Attributes:
        name (str):
            Required. The resource name of
            [Processor][google.cloud.documentai.v1.Processor] or
            [ProcessorVersion][google.cloud.documentai.v1.ProcessorVersion].
            Format:
            ``projects/{project}/locations/{location}/processors/{processor}``,
            or
            ``projects/{project}/locations/{location}/processors/{processor}/processorVersions/{processorVersion}``
        input_documents (google.cloud.documentai_v1.types.BatchDocumentsInputConfig):
            The input documents for the
            [BatchProcessDocuments][google.cloud.documentai.v1.DocumentProcessorService.BatchProcessDocuments]
            method.
        document_output_config (google.cloud.documentai_v1.types.DocumentOutputConfig):
            The output configuration for the
            [BatchProcessDocuments][google.cloud.documentai.v1.DocumentProcessorService.BatchProcessDocuments]
            method.
        skip_human_review (bool):
            Whether human review should be skipped for this request.
            Default to ``false``.
        process_options (google.cloud.documentai_v1.types.ProcessOptions):
            Inference-time options for the process API
        labels (MutableMapping[str, str]):
            Optional. The labels with user-defined
            metadata for the request.
            Label keys and values can be no longer than 63
            characters (Unicode codepoints) and can only
            contain lowercase letters, numeric characters,
            underscores, and dashes. International
            characters are allowed. Label values are
            optional. Label keys must start with a letter.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    input_documents: document_io.BatchDocumentsInputConfig = proto.Field(
        proto.MESSAGE,
        number=5,
        message=document_io.BatchDocumentsInputConfig,
    )
    document_output_config: document_io.DocumentOutputConfig = proto.Field(
        proto.MESSAGE,
        number=6,
        message=document_io.DocumentOutputConfig,
    )
    skip_human_review: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    process_options: "ProcessOptions" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="ProcessOptions",
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=9,
    )


class BatchProcessResponse(proto.Message):
    r"""Response message for
    [BatchProcessDocuments][google.cloud.documentai.v1.DocumentProcessorService.BatchProcessDocuments].

    """


class BatchProcessMetadata(proto.Message):
    r"""The long-running operation metadata for
    [BatchProcessDocuments][google.cloud.documentai.v1.DocumentProcessorService.BatchProcessDocuments].

    Attributes:
        state (google.cloud.documentai_v1.types.BatchProcessMetadata.State):
            The state of the current batch processing.
        state_message (str):
            A message providing more details about the
            current state of processing. For example, the
            error message if the operation is failed.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            The creation time of the operation.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            The last update time of the operation.
        individual_process_statuses (MutableSequence[google.cloud.documentai_v1.types.BatchProcessMetadata.IndividualProcessStatus]):
            The list of response details of each
            document.
    """

    class State(proto.Enum):
        r"""Possible states of the batch processing operation.

        Values:
            STATE_UNSPECIFIED (0):
                The default value. This value is used if the
                state is omitted.
            WAITING (1):
                Request operation is waiting for scheduling.
            RUNNING (2):
                Request is being processed.
            SUCCEEDED (3):
                The batch processing completed successfully.
            CANCELLING (4):
                The batch processing was being cancelled.
            CANCELLED (5):
                The batch processing was cancelled.
            FAILED (6):
                The batch processing has failed.
        """

        STATE_UNSPECIFIED = 0
        WAITING = 1
        RUNNING = 2
        SUCCEEDED = 3
        CANCELLING = 4
        CANCELLED = 5
        FAILED = 6

    class IndividualProcessStatus(proto.Message):
        r"""The status of a each individual document in the batch
        process.

        Attributes:
            input_gcs_source (str):
                The source of the document, same as the
                [input_gcs_source][google.cloud.documentai.v1.BatchProcessMetadata.IndividualProcessStatus.input_gcs_source]
                field in the request when the batch process started.
            status (google.rpc.status_pb2.Status):
                The status processing the document.
            output_gcs_destination (str):
                The Cloud Storage output destination (in the request as
                [DocumentOutputConfig.GcsOutputConfig.gcs_uri][google.cloud.documentai.v1.DocumentOutputConfig.GcsOutputConfig.gcs_uri])
                of the processed document if it was successful, otherwise
                empty.
            human_review_status (google.cloud.documentai_v1.types.HumanReviewStatus):
                The status of human review on the processed
                document.
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
        output_gcs_destination: str = proto.Field(
            proto.STRING,
            number=3,
        )
        human_review_status: "HumanReviewStatus" = proto.Field(
            proto.MESSAGE,
            number=5,
            message="HumanReviewStatus",
        )

    state: State = proto.Field(
        proto.ENUM,
        number=1,
        enum=State,
    )
    state_message: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    individual_process_statuses: MutableSequence[IndividualProcessStatus] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=5,
            message=IndividualProcessStatus,
        )
    )


class FetchProcessorTypesRequest(proto.Message):
    r"""Request message for the
    [FetchProcessorTypes][google.cloud.documentai.v1.DocumentProcessorService.FetchProcessorTypes]
    method. Some processor types may require the project be added to an
    allowlist.

    Attributes:
        parent (str):
            Required. The location of processor types to list. Format:
            ``projects/{project}/locations/{location}``.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )


class FetchProcessorTypesResponse(proto.Message):
    r"""Response message for the
    [FetchProcessorTypes][google.cloud.documentai.v1.DocumentProcessorService.FetchProcessorTypes]
    method.

    Attributes:
        processor_types (MutableSequence[google.cloud.documentai_v1.types.ProcessorType]):
            The list of processor types.
    """

    processor_types: MutableSequence[processor_type.ProcessorType] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=processor_type.ProcessorType,
        )
    )


class ListProcessorTypesRequest(proto.Message):
    r"""Request message for the
    [ListProcessorTypes][google.cloud.documentai.v1.DocumentProcessorService.ListProcessorTypes]
    method. Some processor types may require the project be added to an
    allowlist.

    Attributes:
        parent (str):
            Required. The location of processor types to list. Format:
            ``projects/{project}/locations/{location}``.
        page_size (int):
            The maximum number of processor types to return. If
            unspecified, at most ``100`` processor types will be
            returned. The maximum value is ``500``. Values above ``500``
            will be coerced to ``500``.
        page_token (str):
            Used to retrieve the next page of results,
            empty if at the end of the list.
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


class ListProcessorTypesResponse(proto.Message):
    r"""Response message for the
    [ListProcessorTypes][google.cloud.documentai.v1.DocumentProcessorService.ListProcessorTypes]
    method.

    Attributes:
        processor_types (MutableSequence[google.cloud.documentai_v1.types.ProcessorType]):
            The processor types.
        next_page_token (str):
            Points to the next page, otherwise empty.
    """

    @property
    def raw_page(self):
        return self

    processor_types: MutableSequence[processor_type.ProcessorType] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=processor_type.ProcessorType,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListProcessorsRequest(proto.Message):
    r"""Request message for list all processors belongs to a project.

    Attributes:
        parent (str):
            Required. The parent (project and location) which owns this
            collection of Processors. Format:
            ``projects/{project}/locations/{location}``
        page_size (int):
            The maximum number of processors to return. If unspecified,
            at most ``50`` processors will be returned. The maximum
            value is ``100``. Values above ``100`` will be coerced to
            ``100``.
        page_token (str):
            We will return the processors sorted by
            creation time. The page token will point to the
            next processor.
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


class ListProcessorsResponse(proto.Message):
    r"""Response message for the
    [ListProcessors][google.cloud.documentai.v1.DocumentProcessorService.ListProcessors]
    method.

    Attributes:
        processors (MutableSequence[google.cloud.documentai_v1.types.Processor]):
            The list of processors.
        next_page_token (str):
            Points to the next processor, otherwise
            empty.
    """

    @property
    def raw_page(self):
        return self

    processors: MutableSequence[gcd_processor.Processor] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcd_processor.Processor,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetProcessorTypeRequest(proto.Message):
    r"""Request message for the
    [GetProcessorType][google.cloud.documentai.v1.DocumentProcessorService.GetProcessorType]
    method.

    Attributes:
        name (str):
            Required. The processor type resource name.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetProcessorRequest(proto.Message):
    r"""Request message for the
    [GetProcessor][google.cloud.documentai.v1.DocumentProcessorService.GetProcessor]
    method.

    Attributes:
        name (str):
            Required. The processor resource name.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetProcessorVersionRequest(proto.Message):
    r"""Request message for the
    [GetProcessorVersion][google.cloud.documentai.v1.DocumentProcessorService.GetProcessorVersion]
    method.

    Attributes:
        name (str):
            Required. The processor resource name.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListProcessorVersionsRequest(proto.Message):
    r"""Request message for list all processor versions belongs to a
    processor.

    Attributes:
        parent (str):
            Required. The parent (project, location and processor) to
            list all versions. Format:
            ``projects/{project}/locations/{location}/processors/{processor}``
        page_size (int):
            The maximum number of processor versions to return. If
            unspecified, at most ``10`` processor versions will be
            returned. The maximum value is ``20``. Values above ``20``
            will be coerced to ``20``.
        page_token (str):
            We will return the processor versions sorted
            by creation time. The page token will point to
            the next processor version.
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


class ListProcessorVersionsResponse(proto.Message):
    r"""Response message for the
    [ListProcessorVersions][google.cloud.documentai.v1.DocumentProcessorService.ListProcessorVersions]
    method.

    Attributes:
        processor_versions (MutableSequence[google.cloud.documentai_v1.types.ProcessorVersion]):
            The list of processors.
        next_page_token (str):
            Points to the next processor, otherwise
            empty.
    """

    @property
    def raw_page(self):
        return self

    processor_versions: MutableSequence[gcd_processor.ProcessorVersion] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=gcd_processor.ProcessorVersion,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteProcessorVersionRequest(proto.Message):
    r"""Request message for the
    [DeleteProcessorVersion][google.cloud.documentai.v1.DocumentProcessorService.DeleteProcessorVersion]
    method.

    Attributes:
        name (str):
            Required. The processor version resource name
            to be deleted.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteProcessorVersionMetadata(proto.Message):
    r"""The long-running operation metadata for the
    [DeleteProcessorVersion][google.cloud.documentai.v1.DocumentProcessorService.DeleteProcessorVersion]
    method.

    Attributes:
        common_metadata (google.cloud.documentai_v1.types.CommonOperationMetadata):
            The basic metadata of the long-running
            operation.
    """

    common_metadata: operation_metadata.CommonOperationMetadata = proto.Field(
        proto.MESSAGE,
        number=1,
        message=operation_metadata.CommonOperationMetadata,
    )


class DeployProcessorVersionRequest(proto.Message):
    r"""Request message for the
    [DeployProcessorVersion][google.cloud.documentai.v1.DocumentProcessorService.DeployProcessorVersion]
    method.

    Attributes:
        name (str):
            Required. The processor version resource name
            to be deployed.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeployProcessorVersionResponse(proto.Message):
    r"""Response message for the
    [DeployProcessorVersion][google.cloud.documentai.v1.DocumentProcessorService.DeployProcessorVersion]
    method.

    """


class DeployProcessorVersionMetadata(proto.Message):
    r"""The long-running operation metadata for the
    [DeployProcessorVersion][google.cloud.documentai.v1.DocumentProcessorService.DeployProcessorVersion]
    method.

    Attributes:
        common_metadata (google.cloud.documentai_v1.types.CommonOperationMetadata):
            The basic metadata of the long-running
            operation.
    """

    common_metadata: operation_metadata.CommonOperationMetadata = proto.Field(
        proto.MESSAGE,
        number=1,
        message=operation_metadata.CommonOperationMetadata,
    )


class UndeployProcessorVersionRequest(proto.Message):
    r"""Request message for the
    [UndeployProcessorVersion][google.cloud.documentai.v1.DocumentProcessorService.UndeployProcessorVersion]
    method.

    Attributes:
        name (str):
            Required. The processor version resource name
            to be undeployed.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UndeployProcessorVersionResponse(proto.Message):
    r"""Response message for the
    [UndeployProcessorVersion][google.cloud.documentai.v1.DocumentProcessorService.UndeployProcessorVersion]
    method.

    """


class UndeployProcessorVersionMetadata(proto.Message):
    r"""The long-running operation metadata for the
    [UndeployProcessorVersion][google.cloud.documentai.v1.DocumentProcessorService.UndeployProcessorVersion]
    method.

    Attributes:
        common_metadata (google.cloud.documentai_v1.types.CommonOperationMetadata):
            The basic metadata of the long-running
            operation.
    """

    common_metadata: operation_metadata.CommonOperationMetadata = proto.Field(
        proto.MESSAGE,
        number=1,
        message=operation_metadata.CommonOperationMetadata,
    )


class CreateProcessorRequest(proto.Message):
    r"""Request message for the
    [CreateProcessor][google.cloud.documentai.v1.DocumentProcessorService.CreateProcessor]
    method. Notice this request is sent to a regionalized backend
    service. If the
    [ProcessorType][google.cloud.documentai.v1.ProcessorType] isn't
    available in that region, the creation fails.

    Attributes:
        parent (str):
            Required. The parent (project and location) under which to
            create the processor. Format:
            ``projects/{project}/locations/{location}``
        processor (google.cloud.documentai_v1.types.Processor):
            Required. The processor to be created, requires
            [Processor.type][google.cloud.documentai.v1.Processor.type]
            and
            [Processor.display_name][google.cloud.documentai.v1.Processor.display_name]
            to be set. Also, the
            [Processor.kms_key_name][google.cloud.documentai.v1.Processor.kms_key_name]
            field must be set if the processor is under CMEK.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    processor: gcd_processor.Processor = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcd_processor.Processor,
    )


class DeleteProcessorRequest(proto.Message):
    r"""Request message for the
    [DeleteProcessor][google.cloud.documentai.v1.DocumentProcessorService.DeleteProcessor]
    method.

    Attributes:
        name (str):
            Required. The processor resource name to be
            deleted.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteProcessorMetadata(proto.Message):
    r"""The long-running operation metadata for the
    [DeleteProcessor][google.cloud.documentai.v1.DocumentProcessorService.DeleteProcessor]
    method.

    Attributes:
        common_metadata (google.cloud.documentai_v1.types.CommonOperationMetadata):
            The basic metadata of the long-running
            operation.
    """

    common_metadata: operation_metadata.CommonOperationMetadata = proto.Field(
        proto.MESSAGE,
        number=5,
        message=operation_metadata.CommonOperationMetadata,
    )


class EnableProcessorRequest(proto.Message):
    r"""Request message for the
    [EnableProcessor][google.cloud.documentai.v1.DocumentProcessorService.EnableProcessor]
    method.

    Attributes:
        name (str):
            Required. The processor resource name to be
            enabled.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class EnableProcessorResponse(proto.Message):
    r"""Response message for the
    [EnableProcessor][google.cloud.documentai.v1.DocumentProcessorService.EnableProcessor]
    method. Intentionally empty proto for adding fields in future.

    """


class EnableProcessorMetadata(proto.Message):
    r"""The long-running operation metadata for the
    [EnableProcessor][google.cloud.documentai.v1.DocumentProcessorService.EnableProcessor]
    method.

    Attributes:
        common_metadata (google.cloud.documentai_v1.types.CommonOperationMetadata):
            The basic metadata of the long-running
            operation.
    """

    common_metadata: operation_metadata.CommonOperationMetadata = proto.Field(
        proto.MESSAGE,
        number=5,
        message=operation_metadata.CommonOperationMetadata,
    )


class DisableProcessorRequest(proto.Message):
    r"""Request message for the
    [DisableProcessor][google.cloud.documentai.v1.DocumentProcessorService.DisableProcessor]
    method.

    Attributes:
        name (str):
            Required. The processor resource name to be
            disabled.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DisableProcessorResponse(proto.Message):
    r"""Response message for the
    [DisableProcessor][google.cloud.documentai.v1.DocumentProcessorService.DisableProcessor]
    method. Intentionally empty proto for adding fields in future.

    """


class DisableProcessorMetadata(proto.Message):
    r"""The long-running operation metadata for the
    [DisableProcessor][google.cloud.documentai.v1.DocumentProcessorService.DisableProcessor]
    method.

    Attributes:
        common_metadata (google.cloud.documentai_v1.types.CommonOperationMetadata):
            The basic metadata of the long-running
            operation.
    """

    common_metadata: operation_metadata.CommonOperationMetadata = proto.Field(
        proto.MESSAGE,
        number=5,
        message=operation_metadata.CommonOperationMetadata,
    )


class SetDefaultProcessorVersionRequest(proto.Message):
    r"""Request message for the
    [SetDefaultProcessorVersion][google.cloud.documentai.v1.DocumentProcessorService.SetDefaultProcessorVersion]
    method.

    Attributes:
        processor (str):
            Required. The resource name of the
            [Processor][google.cloud.documentai.v1.Processor] to change
            default version.
        default_processor_version (str):
            Required. The resource name of child
            [ProcessorVersion][google.cloud.documentai.v1.ProcessorVersion]
            to use as default. Format:
            ``projects/{project}/locations/{location}/processors/{processor}/processorVersions/{version}``
    """

    processor: str = proto.Field(
        proto.STRING,
        number=1,
    )
    default_processor_version: str = proto.Field(
        proto.STRING,
        number=2,
    )


class SetDefaultProcessorVersionResponse(proto.Message):
    r"""Response message for the
    [SetDefaultProcessorVersion][google.cloud.documentai.v1.DocumentProcessorService.SetDefaultProcessorVersion]
    method.

    """


class SetDefaultProcessorVersionMetadata(proto.Message):
    r"""The long-running operation metadata for the
    [SetDefaultProcessorVersion][google.cloud.documentai.v1.DocumentProcessorService.SetDefaultProcessorVersion]
    method.

    Attributes:
        common_metadata (google.cloud.documentai_v1.types.CommonOperationMetadata):
            The basic metadata of the long-running
            operation.
    """

    common_metadata: operation_metadata.CommonOperationMetadata = proto.Field(
        proto.MESSAGE,
        number=1,
        message=operation_metadata.CommonOperationMetadata,
    )


class TrainProcessorVersionRequest(proto.Message):
    r"""Request message for the
    [TrainProcessorVersion][google.cloud.documentai.v1.DocumentProcessorService.TrainProcessorVersion]
    method.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        custom_document_extraction_options (google.cloud.documentai_v1.types.TrainProcessorVersionRequest.CustomDocumentExtractionOptions):
            Options to control Custom Document Extraction
            (CDE) Processor.

            This field is a member of `oneof`_ ``processor_flags``.
        foundation_model_tuning_options (google.cloud.documentai_v1.types.TrainProcessorVersionRequest.FoundationModelTuningOptions):
            Options to control foundation model tuning of
            a processor.

            This field is a member of `oneof`_ ``processor_flags``.
        parent (str):
            Required. The parent (project, location and processor) to
            create the new version for. Format:
            ``projects/{project}/locations/{location}/processors/{processor}``.
        processor_version (google.cloud.documentai_v1.types.ProcessorVersion):
            Required. The processor version to be
            created.
        document_schema (google.cloud.documentai_v1.types.DocumentSchema):
            Optional. The schema the processor version
            will be trained with.
        input_data (google.cloud.documentai_v1.types.TrainProcessorVersionRequest.InputData):
            Optional. The input data used to train the
            [ProcessorVersion][google.cloud.documentai.v1.ProcessorVersion].
        base_processor_version (str):
            Optional. The processor version to use as a base for
            training. This processor version must be a child of
            ``parent``. Format:
            ``projects/{project}/locations/{location}/processors/{processor}/processorVersions/{processorVersion}``.
    """

    class InputData(proto.Message):
        r"""The input data used to train a new
        [ProcessorVersion][google.cloud.documentai.v1.ProcessorVersion].

        Attributes:
            training_documents (google.cloud.documentai_v1.types.BatchDocumentsInputConfig):
                The documents used for training the new
                version.
            test_documents (google.cloud.documentai_v1.types.BatchDocumentsInputConfig):
                The documents used for testing the trained
                version.
        """

        training_documents: document_io.BatchDocumentsInputConfig = proto.Field(
            proto.MESSAGE,
            number=3,
            message=document_io.BatchDocumentsInputConfig,
        )
        test_documents: document_io.BatchDocumentsInputConfig = proto.Field(
            proto.MESSAGE,
            number=4,
            message=document_io.BatchDocumentsInputConfig,
        )

    class CustomDocumentExtractionOptions(proto.Message):
        r"""Options to control the training of the Custom Document
        Extraction (CDE) Processor.

        Attributes:
            training_method (google.cloud.documentai_v1.types.TrainProcessorVersionRequest.CustomDocumentExtractionOptions.TrainingMethod):
                Optional. Training method to use for CDE
                training.
        """

        class TrainingMethod(proto.Enum):
            r"""Training Method for CDE. ``TRAINING_METHOD_UNSPECIFIED`` will fall
            back to ``MODEL_BASED``.

            Values:
                TRAINING_METHOD_UNSPECIFIED (0):
                    No description available.
                MODEL_BASED (1):
                    No description available.
                TEMPLATE_BASED (2):
                    No description available.
            """

            TRAINING_METHOD_UNSPECIFIED = 0
            MODEL_BASED = 1
            TEMPLATE_BASED = 2

        training_method: "TrainProcessorVersionRequest.CustomDocumentExtractionOptions.TrainingMethod" = proto.Field(
            proto.ENUM,
            number=3,
            enum="TrainProcessorVersionRequest.CustomDocumentExtractionOptions.TrainingMethod",
        )

    class FoundationModelTuningOptions(proto.Message):
        r"""Options to control foundation model tuning of the processor.

        Attributes:
            train_steps (int):
                Optional. The number of steps to run for
                model tuning. Valid values are between 1 and
                400. If not provided, recommended steps will be
                used.
            learning_rate_multiplier (float):
                Optional. The multiplier to apply to the
                recommended learning rate. Valid values are
                between 0.1 and 10. If not provided, recommended
                learning rate will be used.
        """

        train_steps: int = proto.Field(
            proto.INT32,
            number=2,
        )
        learning_rate_multiplier: float = proto.Field(
            proto.FLOAT,
            number=3,
        )

    custom_document_extraction_options: CustomDocumentExtractionOptions = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="processor_flags",
        message=CustomDocumentExtractionOptions,
    )
    foundation_model_tuning_options: FoundationModelTuningOptions = proto.Field(
        proto.MESSAGE,
        number=12,
        oneof="processor_flags",
        message=FoundationModelTuningOptions,
    )
    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    processor_version: gcd_processor.ProcessorVersion = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcd_processor.ProcessorVersion,
    )
    document_schema: gcd_document_schema.DocumentSchema = proto.Field(
        proto.MESSAGE,
        number=10,
        message=gcd_document_schema.DocumentSchema,
    )
    input_data: InputData = proto.Field(
        proto.MESSAGE,
        number=4,
        message=InputData,
    )
    base_processor_version: str = proto.Field(
        proto.STRING,
        number=8,
    )


class TrainProcessorVersionResponse(proto.Message):
    r"""The response for
    [TrainProcessorVersion][google.cloud.documentai.v1.DocumentProcessorService.TrainProcessorVersion].

    Attributes:
        processor_version (str):
            The resource name of the processor version
            produced by training.
    """

    processor_version: str = proto.Field(
        proto.STRING,
        number=1,
    )


class TrainProcessorVersionMetadata(proto.Message):
    r"""The metadata that represents a processor version being
    created.

    Attributes:
        common_metadata (google.cloud.documentai_v1.types.CommonOperationMetadata):
            The basic metadata of the long-running
            operation.
        training_dataset_validation (google.cloud.documentai_v1.types.TrainProcessorVersionMetadata.DatasetValidation):
            The training dataset validation information.
        test_dataset_validation (google.cloud.documentai_v1.types.TrainProcessorVersionMetadata.DatasetValidation):
            The test dataset validation information.
    """

    class DatasetValidation(proto.Message):
        r"""The dataset validation information.
        This includes any and all errors with documents and the dataset.

        Attributes:
            document_error_count (int):
                The total number of document errors.
            dataset_error_count (int):
                The total number of dataset errors.
            document_errors (MutableSequence[google.rpc.status_pb2.Status]):
                Error information pertaining to specific
                documents. A maximum of 10 document errors will
                be returned. Any document with errors will not
                be used throughout training.
            dataset_errors (MutableSequence[google.rpc.status_pb2.Status]):
                Error information for the dataset as a whole.
                A maximum of 10 dataset errors will be returned.
                A single dataset error is terminal for training.
        """

        document_error_count: int = proto.Field(
            proto.INT32,
            number=3,
        )
        dataset_error_count: int = proto.Field(
            proto.INT32,
            number=4,
        )
        document_errors: MutableSequence[status_pb2.Status] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=status_pb2.Status,
        )
        dataset_errors: MutableSequence[status_pb2.Status] = proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message=status_pb2.Status,
        )

    common_metadata: operation_metadata.CommonOperationMetadata = proto.Field(
        proto.MESSAGE,
        number=1,
        message=operation_metadata.CommonOperationMetadata,
    )
    training_dataset_validation: DatasetValidation = proto.Field(
        proto.MESSAGE,
        number=2,
        message=DatasetValidation,
    )
    test_dataset_validation: DatasetValidation = proto.Field(
        proto.MESSAGE,
        number=3,
        message=DatasetValidation,
    )


class ReviewDocumentRequest(proto.Message):
    r"""Request message for the
    [ReviewDocument][google.cloud.documentai.v1.DocumentProcessorService.ReviewDocument]
    method.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        inline_document (google.cloud.documentai_v1.types.Document):
            An inline document proto.

            This field is a member of `oneof`_ ``source``.
        human_review_config (str):
            Required. The resource name of the
            [HumanReviewConfig][google.cloud.documentai.v1.HumanReviewConfig]
            that the document will be reviewed with.
        enable_schema_validation (bool):
            Whether the validation should be performed on
            the ad-hoc review request.
        priority (google.cloud.documentai_v1.types.ReviewDocumentRequest.Priority):
            The priority of the human review task.
        document_schema (google.cloud.documentai_v1.types.DocumentSchema):
            The document schema of the human review task.
    """

    class Priority(proto.Enum):
        r"""The priority level of the human review task.

        Values:
            DEFAULT (0):
                The default priority level.
            URGENT (1):
                The urgent priority level. The labeling
                manager should allocate labeler resource to the
                urgent task queue to respect this priority
                level.
        """

        DEFAULT = 0
        URGENT = 1

    inline_document: gcd_document.Document = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="source",
        message=gcd_document.Document,
    )
    human_review_config: str = proto.Field(
        proto.STRING,
        number=1,
    )
    enable_schema_validation: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    priority: Priority = proto.Field(
        proto.ENUM,
        number=5,
        enum=Priority,
    )
    document_schema: gcd_document_schema.DocumentSchema = proto.Field(
        proto.MESSAGE,
        number=6,
        message=gcd_document_schema.DocumentSchema,
    )


class ReviewDocumentResponse(proto.Message):
    r"""Response message for the
    [ReviewDocument][google.cloud.documentai.v1.DocumentProcessorService.ReviewDocument]
    method.

    Attributes:
        gcs_destination (str):
            The Cloud Storage uri for the human reviewed
            document if the review is succeeded.
        state (google.cloud.documentai_v1.types.ReviewDocumentResponse.State):
            The state of the review operation.
        rejection_reason (str):
            The reason why the review is rejected by
            reviewer.
    """

    class State(proto.Enum):
        r"""Possible states of the review operation.

        Values:
            STATE_UNSPECIFIED (0):
                The default value. This value is used if the
                state is omitted.
            REJECTED (1):
                The review operation is rejected by the
                reviewer.
            SUCCEEDED (2):
                The review operation is succeeded.
        """

        STATE_UNSPECIFIED = 0
        REJECTED = 1
        SUCCEEDED = 2

    gcs_destination: str = proto.Field(
        proto.STRING,
        number=1,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=2,
        enum=State,
    )
    rejection_reason: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ReviewDocumentOperationMetadata(proto.Message):
    r"""The long-running operation metadata for the
    [ReviewDocument][google.cloud.documentai.v1.DocumentProcessorService.ReviewDocument]
    method.

    Attributes:
        common_metadata (google.cloud.documentai_v1.types.CommonOperationMetadata):
            The basic metadata of the long-running
            operation.
        question_id (str):
            The Crowd Compute question ID.
    """

    common_metadata: operation_metadata.CommonOperationMetadata = proto.Field(
        proto.MESSAGE,
        number=5,
        message=operation_metadata.CommonOperationMetadata,
    )
    question_id: str = proto.Field(
        proto.STRING,
        number=6,
    )


class EvaluateProcessorVersionRequest(proto.Message):
    r"""Evaluates the given
    [ProcessorVersion][google.cloud.documentai.v1.ProcessorVersion]
    against the supplied documents.

    Attributes:
        processor_version (str):
            Required. The resource name of the
            [ProcessorVersion][google.cloud.documentai.v1.ProcessorVersion]
            to evaluate.
            ``projects/{project}/locations/{location}/processors/{processor}/processorVersions/{processorVersion}``
        evaluation_documents (google.cloud.documentai_v1.types.BatchDocumentsInputConfig):
            Optional. The documents used in the
            evaluation. If unspecified, use the processor's
            dataset as evaluation input.
    """

    processor_version: str = proto.Field(
        proto.STRING,
        number=1,
    )
    evaluation_documents: document_io.BatchDocumentsInputConfig = proto.Field(
        proto.MESSAGE,
        number=3,
        message=document_io.BatchDocumentsInputConfig,
    )


class EvaluateProcessorVersionMetadata(proto.Message):
    r"""Metadata of the
    [EvaluateProcessorVersion][google.cloud.documentai.v1.DocumentProcessorService.EvaluateProcessorVersion]
    method.

    Attributes:
        common_metadata (google.cloud.documentai_v1.types.CommonOperationMetadata):
            The basic metadata of the long-running
            operation.
    """

    common_metadata: operation_metadata.CommonOperationMetadata = proto.Field(
        proto.MESSAGE,
        number=1,
        message=operation_metadata.CommonOperationMetadata,
    )


class EvaluateProcessorVersionResponse(proto.Message):
    r"""Response of the
    [EvaluateProcessorVersion][google.cloud.documentai.v1.DocumentProcessorService.EvaluateProcessorVersion]
    method.

    Attributes:
        evaluation (str):
            The resource name of the created evaluation.
    """

    evaluation: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetEvaluationRequest(proto.Message):
    r"""Retrieves a specific Evaluation.

    Attributes:
        name (str):
            Required. The resource name of the
            [Evaluation][google.cloud.documentai.v1.Evaluation] to get.
            ``projects/{project}/locations/{location}/processors/{processor}/processorVersions/{processorVersion}/evaluations/{evaluation}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListEvaluationsRequest(proto.Message):
    r"""Retrieves a list of evaluations for a given
    [ProcessorVersion][google.cloud.documentai.v1.ProcessorVersion].

    Attributes:
        parent (str):
            Required. The resource name of the
            [ProcessorVersion][google.cloud.documentai.v1.ProcessorVersion]
            to list evaluations for.
            ``projects/{project}/locations/{location}/processors/{processor}/processorVersions/{processorVersion}``
        page_size (int):
            The standard list page size. If unspecified, at most ``5``
            evaluations are returned. The maximum value is ``100``.
            Values above ``100`` are coerced to ``100``.
        page_token (str):
            A page token, received from a previous ``ListEvaluations``
            call. Provide this to retrieve the subsequent page.
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


class ListEvaluationsResponse(proto.Message):
    r"""The response from ``ListEvaluations``.

    Attributes:
        evaluations (MutableSequence[google.cloud.documentai_v1.types.Evaluation]):
            The evaluations requested.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    evaluations: MutableSequence[gcd_evaluation.Evaluation] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcd_evaluation.Evaluation,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
