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
import google.rpc.status_pb2 as status_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.contentwarehouse_v1.types import common

__protobuf__ = proto.module(
    package="google.cloud.contentwarehouse.v1",
    manifest={
        "RunPipelineResponse",
        "RunPipelineMetadata",
        "ProcessorInfo",
        "IngestPipelineConfig",
        "GcsIngestPipeline",
        "GcsIngestWithDocAiProcessorsPipeline",
        "ExportToCdwPipeline",
        "ProcessWithDocAiPipeline",
    },
)


class RunPipelineResponse(proto.Message):
    r"""Response message of RunPipeline method."""


class RunPipelineMetadata(proto.Message):
    r"""Metadata message of RunPipeline method.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        total_file_count (int):
            Number of files that were processed by the
            pipeline.
        failed_file_count (int):
            Number of files that have failed at some
            point in the pipeline.
        user_info (google.cloud.contentwarehouse_v1.types.UserInfo):
            User unique identification and groups
            information.
        gcs_ingest_pipeline_metadata (google.cloud.contentwarehouse_v1.types.RunPipelineMetadata.GcsIngestPipelineMetadata):
            The pipeline metadata for GcsIngest pipeline.

            This field is a member of `oneof`_ ``pipeline_metadata``.
        export_to_cdw_pipeline_metadata (google.cloud.contentwarehouse_v1.types.RunPipelineMetadata.ExportToCdwPipelineMetadata):
            The pipeline metadata for Export-to-CDW
            pipeline.

            This field is a member of `oneof`_ ``pipeline_metadata``.
        process_with_doc_ai_pipeline_metadata (google.cloud.contentwarehouse_v1.types.RunPipelineMetadata.ProcessWithDocAiPipelineMetadata):
            The pipeline metadata for Process-with-DocAi
            pipeline.

            This field is a member of `oneof`_ ``pipeline_metadata``.
        individual_document_statuses (MutableSequence[google.cloud.contentwarehouse_v1.types.RunPipelineMetadata.IndividualDocumentStatus]):
            The list of response details of each
            document.
    """

    class GcsIngestPipelineMetadata(proto.Message):
        r"""The metadata message for GcsIngest pipeline.

        Attributes:
            input_path (str):
                The input Cloud Storage folder in this pipeline. Format:
                ``gs://<bucket-name>/<folder-name>``.
        """

        input_path: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class ExportToCdwPipelineMetadata(proto.Message):
        r"""The metadata message for Export-to-CDW pipeline.

        Attributes:
            documents (MutableSequence[str]):
                The input list of all the resource names of
                the documents to be exported.
            doc_ai_dataset (str):
                The output CDW dataset resource name.
            output_path (str):
                The output Cloud Storage folder in this
                pipeline.
        """

        documents: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )
        doc_ai_dataset: str = proto.Field(
            proto.STRING,
            number=2,
        )
        output_path: str = proto.Field(
            proto.STRING,
            number=3,
        )

    class ProcessWithDocAiPipelineMetadata(proto.Message):
        r"""The metadata message for Process-with-DocAi pipeline.

        Attributes:
            documents (MutableSequence[str]):
                The input list of all the resource names of
                the documents to be processed.
            processor_info (google.cloud.contentwarehouse_v1.types.ProcessorInfo):
                The DocAI processor to process the documents
                with.
        """

        documents: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )
        processor_info: "ProcessorInfo" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="ProcessorInfo",
        )

    class IndividualDocumentStatus(proto.Message):
        r"""The status of processing a document.

        Attributes:
            document_id (str):
                Document identifier of an existing document.
            status (google.rpc.status_pb2.Status):
                The status processing the document.
        """

        document_id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        status: status_pb2.Status = proto.Field(
            proto.MESSAGE,
            number=2,
            message=status_pb2.Status,
        )

    total_file_count: int = proto.Field(
        proto.INT32,
        number=1,
    )
    failed_file_count: int = proto.Field(
        proto.INT32,
        number=2,
    )
    user_info: common.UserInfo = proto.Field(
        proto.MESSAGE,
        number=3,
        message=common.UserInfo,
    )
    gcs_ingest_pipeline_metadata: GcsIngestPipelineMetadata = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="pipeline_metadata",
        message=GcsIngestPipelineMetadata,
    )
    export_to_cdw_pipeline_metadata: ExportToCdwPipelineMetadata = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="pipeline_metadata",
        message=ExportToCdwPipelineMetadata,
    )
    process_with_doc_ai_pipeline_metadata: ProcessWithDocAiPipelineMetadata = (
        proto.Field(
            proto.MESSAGE,
            number=7,
            oneof="pipeline_metadata",
            message=ProcessWithDocAiPipelineMetadata,
        )
    )
    individual_document_statuses: MutableSequence[IndividualDocumentStatus] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=5,
            message=IndividualDocumentStatus,
        )
    )


class ProcessorInfo(proto.Message):
    r"""The DocAI processor information.

    Attributes:
        processor_name (str):
            The processor resource name. Format is
            ``projects/{project}/locations/{location}/processors/{processor}``,
            or
            ``projects/{project}/locations/{location}/processors/{processor}/processorVersions/{processorVersion}``
        document_type (str):
            The processor will process the documents with
            this document type.
        schema_name (str):
            The Document schema resource name. All documents processed
            by this processor will use this schema. Format:
            projects/{project_number}/locations/{location}/documentSchemas/{document_schema_id}.
    """

    processor_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    document_type: str = proto.Field(
        proto.STRING,
        number=2,
    )
    schema_name: str = proto.Field(
        proto.STRING,
        number=3,
    )


class IngestPipelineConfig(proto.Message):
    r"""The ingestion pipeline config.

    Attributes:
        document_acl_policy (google.iam.v1.policy_pb2.Policy):
            The document level acl policy config. This refers to an
            Identity and Access (IAM) policy, which specifies access
            controls for all documents ingested by the pipeline. The
            [role][google.iam.v1.Binding.role] and
            [members][google.iam.v1.Binding.role] under the policy needs
            to be specified.

            The following roles are supported for document level acl
            control:

            - roles/contentwarehouse.documentAdmin
            - roles/contentwarehouse.documentEditor
            - roles/contentwarehouse.documentViewer

            The following members are supported for document level acl
            control:

            - user:user-email@example.com
            - group:group-email@example.com Note that for documents
              searched with LLM, only single level user or group acl
              check is supported.
        enable_document_text_extraction (bool):
            The document text extraction enabled flag.
            If the flag is set to true, DWH will perform
            text extraction on the raw document.
        folder (str):
            Optional. The name of the folder to which all ingested
            documents will be linked during ingestion process. Format is
            ``projects/{project}/locations/{location}/documents/{folder_id}``
        cloud_function (str):
            The Cloud Function resource name. The Cloud Function needs
            to live inside consumer project and is accessible to
            Document AI Warehouse P4SA. Only Cloud Functions V2 is
            supported. Cloud function execution should complete within 5
            minutes or this file ingestion may fail due to timeout.
            Format:
            ``https://{region}-{project_id}.cloudfunctions.net/{cloud_function}``
            The following keys are available the request json payload.

            - display_name
            - properties
            - plain_text
            - reference_id
            - document_schema_name
            - raw_document_path
            - raw_document_file_type

            The following keys from the cloud function json response
            payload will be ingested to the Document AI Warehouse as
            part of Document proto content and/or related information.
            The original values will be overridden if any key is present
            in the response.

            - display_name
            - properties
            - plain_text
            - document_acl_policy
            - folder
    """

    document_acl_policy: policy_pb2.Policy = proto.Field(
        proto.MESSAGE,
        number=1,
        message=policy_pb2.Policy,
    )
    enable_document_text_extraction: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    folder: str = proto.Field(
        proto.STRING,
        number=3,
    )
    cloud_function: str = proto.Field(
        proto.STRING,
        number=4,
    )


class GcsIngestPipeline(proto.Message):
    r"""The configuration of the Cloud Storage Ingestion pipeline.

    Attributes:
        input_path (str):
            The input Cloud Storage folder. All files under this folder
            will be imported to Document Warehouse. Format:
            ``gs://<bucket-name>/<folder-name>``.
        schema_name (str):
            The Document Warehouse schema resource name. All documents
            processed by this pipeline will use this schema. Format:
            projects/{project_number}/locations/{location}/documentSchemas/{document_schema_id}.
        processor_type (str):
            The Doc AI processor type name. Only used
            when the format of ingested files is Doc AI
            Document proto format.
        skip_ingested_documents (bool):
            The flag whether to skip ingested documents.
            If it is set to true, documents in Cloud Storage
            contains key "status" with value
            "status=ingested" in custom metadata will be
            skipped to ingest.
        pipeline_config (google.cloud.contentwarehouse_v1.types.IngestPipelineConfig):
            Optional. The config for the Cloud Storage
            Ingestion pipeline. It provides additional
            customization options to run the pipeline and
            can be skipped if it is not applicable.
    """

    input_path: str = proto.Field(
        proto.STRING,
        number=1,
    )
    schema_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    processor_type: str = proto.Field(
        proto.STRING,
        number=3,
    )
    skip_ingested_documents: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    pipeline_config: "IngestPipelineConfig" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="IngestPipelineConfig",
    )


class GcsIngestWithDocAiProcessorsPipeline(proto.Message):
    r"""The configuration of the Cloud Storage Ingestion with DocAI
    Processors pipeline.

    Attributes:
        input_path (str):
            The input Cloud Storage folder. All files under this folder
            will be imported to Document Warehouse. Format:
            ``gs://<bucket-name>/<folder-name>``.
        split_classify_processor_info (google.cloud.contentwarehouse_v1.types.ProcessorInfo):
            The split and classify processor information.
            The split and classify result will be used to
            find a matched extract processor.
        extract_processor_infos (MutableSequence[google.cloud.contentwarehouse_v1.types.ProcessorInfo]):
            The extract processors information.
            One matched extract processor will be used to
            process documents based on the classify
            processor result. If no classify processor is
            specified, the first extract processor will be
            used.
        processor_results_folder_path (str):
            The Cloud Storage folder path used to store the raw results
            from processors. Format:
            ``gs://<bucket-name>/<folder-name>``.
        skip_ingested_documents (bool):
            The flag whether to skip ingested documents.
            If it is set to true, documents in Cloud Storage
            contains key "status" with value
            "status=ingested" in custom metadata will be
            skipped to ingest.
        pipeline_config (google.cloud.contentwarehouse_v1.types.IngestPipelineConfig):
            Optional. The config for the Cloud Storage
            Ingestion with DocAI Processors pipeline. It
            provides additional customization options to run
            the pipeline and can be skipped if it is not
            applicable.
    """

    input_path: str = proto.Field(
        proto.STRING,
        number=1,
    )
    split_classify_processor_info: "ProcessorInfo" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ProcessorInfo",
    )
    extract_processor_infos: MutableSequence["ProcessorInfo"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="ProcessorInfo",
    )
    processor_results_folder_path: str = proto.Field(
        proto.STRING,
        number=4,
    )
    skip_ingested_documents: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    pipeline_config: "IngestPipelineConfig" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="IngestPipelineConfig",
    )


class ExportToCdwPipeline(proto.Message):
    r"""The configuration of exporting documents from the Document
    Warehouse to CDW pipeline.

    Attributes:
        documents (MutableSequence[str]):
            The list of all the resource names of the documents to be
            processed. Format:
            projects/{project_number}/locations/{location}/documents/{document_id}.
        export_folder_path (str):
            The Cloud Storage folder path used to store the exported
            documents before being sent to CDW. Format:
            ``gs://<bucket-name>/<folder-name>``.
        doc_ai_dataset (str):
            Optional. The CDW dataset resource name. This
            field is optional. If not set, the documents
            will be exported to Cloud Storage only. Format:

            projects/{project}/locations/{location}/processors/{processor}/dataset
        training_split_ratio (float):
            Ratio of training dataset split. When importing into
            Document AI Workbench, documents will be automatically split
            into training and test split category with the specified
            ratio. This field is required if doc_ai_dataset is set.
    """

    documents: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    export_folder_path: str = proto.Field(
        proto.STRING,
        number=2,
    )
    doc_ai_dataset: str = proto.Field(
        proto.STRING,
        number=3,
    )
    training_split_ratio: float = proto.Field(
        proto.FLOAT,
        number=4,
    )


class ProcessWithDocAiPipeline(proto.Message):
    r"""The configuration of processing documents in Document
    Warehouse with DocAi processors pipeline.

    Attributes:
        documents (MutableSequence[str]):
            The list of all the resource names of the documents to be
            processed. Format:
            projects/{project_number}/locations/{location}/documents/{document_id}.
        export_folder_path (str):
            The Cloud Storage folder path used to store the exported
            documents before being sent to CDW. Format:
            ``gs://<bucket-name>/<folder-name>``.
        processor_info (google.cloud.contentwarehouse_v1.types.ProcessorInfo):
            The CDW processor information.
        processor_results_folder_path (str):
            The Cloud Storage folder path used to store the raw results
            from processors. Format:
            ``gs://<bucket-name>/<folder-name>``.
    """

    documents: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    export_folder_path: str = proto.Field(
        proto.STRING,
        number=2,
    )
    processor_info: "ProcessorInfo" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="ProcessorInfo",
    )
    processor_results_folder_path: str = proto.Field(
        proto.STRING,
        number=4,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
