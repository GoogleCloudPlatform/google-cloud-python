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

from google.cloud.contentwarehouse_v1.types import common, pipelines

__protobuf__ = proto.module(
    package="google.cloud.contentwarehouse.v1",
    manifest={
        "RunPipelineRequest",
    },
)


class RunPipelineRequest(proto.Message):
    r"""Request message for DocumentService.RunPipeline.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Required. The resource name which owns the resources of the
            pipeline. Format:
            projects/{project_number}/locations/{location}.
        gcs_ingest_pipeline (google.cloud.contentwarehouse_v1.types.GcsIngestPipeline):
            Cloud Storage ingestion pipeline.

            This field is a member of `oneof`_ ``pipeline``.
        gcs_ingest_with_doc_ai_processors_pipeline (google.cloud.contentwarehouse_v1.types.GcsIngestWithDocAiProcessorsPipeline):
            Use DocAI processors to process documents in
            Cloud Storage and ingest them to Document
            Warehouse.

            This field is a member of `oneof`_ ``pipeline``.
        export_cdw_pipeline (google.cloud.contentwarehouse_v1.types.ExportToCdwPipeline):
            Export docuemnts from Document Warehouse to
            CDW for training purpose.

            This field is a member of `oneof`_ ``pipeline``.
        process_with_doc_ai_pipeline (google.cloud.contentwarehouse_v1.types.ProcessWithDocAiPipeline):
            Use a DocAI processor to process documents in
            Document Warehouse, and re-ingest the updated
            results into Document Warehouse.

            This field is a member of `oneof`_ ``pipeline``.
        request_metadata (google.cloud.contentwarehouse_v1.types.RequestMetadata):
            The meta information collected about the end
            user, used to enforce access control for the
            service.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    gcs_ingest_pipeline: pipelines.GcsIngestPipeline = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="pipeline",
        message=pipelines.GcsIngestPipeline,
    )
    gcs_ingest_with_doc_ai_processors_pipeline: pipelines.GcsIngestWithDocAiProcessorsPipeline = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="pipeline",
        message=pipelines.GcsIngestWithDocAiProcessorsPipeline,
    )
    export_cdw_pipeline: pipelines.ExportToCdwPipeline = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="pipeline",
        message=pipelines.ExportToCdwPipeline,
    )
    process_with_doc_ai_pipeline: pipelines.ProcessWithDocAiPipeline = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="pipeline",
        message=pipelines.ProcessWithDocAiPipeline,
    )
    request_metadata: common.RequestMetadata = proto.Field(
        proto.MESSAGE,
        number=6,
        message=common.RequestMetadata,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
