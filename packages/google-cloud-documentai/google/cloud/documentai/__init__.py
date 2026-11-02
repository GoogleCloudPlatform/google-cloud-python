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
from google.cloud.documentai import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.documentai_v1.services.document_processor_service.async_client import (
    DocumentProcessorServiceAsyncClient,
)
from google.cloud.documentai_v1.services.document_processor_service.client import (
    DocumentProcessorServiceClient,
)
from google.cloud.documentai_v1.types.barcode import Barcode
from google.cloud.documentai_v1.types.document import Document
from google.cloud.documentai_v1.types.document_io import (
    BatchDocumentsInputConfig,
    DocumentOutputConfig,
    GcsDocument,
    GcsDocuments,
    GcsPrefix,
    OcrConfig,
    RawDocument,
)
from google.cloud.documentai_v1.types.document_processor_service import (
    BatchProcessMetadata,
    BatchProcessRequest,
    BatchProcessResponse,
    CreateProcessorRequest,
    DeleteProcessorMetadata,
    DeleteProcessorRequest,
    DeleteProcessorVersionMetadata,
    DeleteProcessorVersionRequest,
    DeployProcessorVersionMetadata,
    DeployProcessorVersionRequest,
    DeployProcessorVersionResponse,
    DisableProcessorMetadata,
    DisableProcessorRequest,
    DisableProcessorResponse,
    EnableProcessorMetadata,
    EnableProcessorRequest,
    EnableProcessorResponse,
    EvaluateProcessorVersionMetadata,
    EvaluateProcessorVersionRequest,
    EvaluateProcessorVersionResponse,
    FetchProcessorTypesRequest,
    FetchProcessorTypesResponse,
    GetEvaluationRequest,
    GetProcessorRequest,
    GetProcessorTypeRequest,
    GetProcessorVersionRequest,
    HumanReviewStatus,
    ListEvaluationsRequest,
    ListEvaluationsResponse,
    ListProcessorsRequest,
    ListProcessorsResponse,
    ListProcessorTypesRequest,
    ListProcessorTypesResponse,
    ListProcessorVersionsRequest,
    ListProcessorVersionsResponse,
    ProcessOptions,
    ProcessRequest,
    ProcessResponse,
    ReviewDocumentOperationMetadata,
    ReviewDocumentRequest,
    ReviewDocumentResponse,
    SetDefaultProcessorVersionMetadata,
    SetDefaultProcessorVersionRequest,
    SetDefaultProcessorVersionResponse,
    TrainProcessorVersionMetadata,
    TrainProcessorVersionRequest,
    TrainProcessorVersionResponse,
    UndeployProcessorVersionMetadata,
    UndeployProcessorVersionRequest,
    UndeployProcessorVersionResponse,
)
from google.cloud.documentai_v1.types.document_schema import DocumentSchema
from google.cloud.documentai_v1.types.evaluation import Evaluation, EvaluationReference
from google.cloud.documentai_v1.types.geometry import (
    BoundingPoly,
    NormalizedVertex,
    Vertex,
)
from google.cloud.documentai_v1.types.operation_metadata import CommonOperationMetadata
from google.cloud.documentai_v1.types.processor import (
    Processor,
    ProcessorVersion,
    ProcessorVersionAlias,
)
from google.cloud.documentai_v1.types.processor_type import ProcessorType

__all__ = (
    "DocumentProcessorServiceClient",
    "DocumentProcessorServiceAsyncClient",
    "Barcode",
    "Document",
    "BatchDocumentsInputConfig",
    "DocumentOutputConfig",
    "GcsDocument",
    "GcsDocuments",
    "GcsPrefix",
    "OcrConfig",
    "RawDocument",
    "BatchProcessMetadata",
    "BatchProcessRequest",
    "BatchProcessResponse",
    "CreateProcessorRequest",
    "DeleteProcessorMetadata",
    "DeleteProcessorRequest",
    "DeleteProcessorVersionMetadata",
    "DeleteProcessorVersionRequest",
    "DeployProcessorVersionMetadata",
    "DeployProcessorVersionRequest",
    "DeployProcessorVersionResponse",
    "DisableProcessorMetadata",
    "DisableProcessorRequest",
    "DisableProcessorResponse",
    "EnableProcessorMetadata",
    "EnableProcessorRequest",
    "EnableProcessorResponse",
    "EvaluateProcessorVersionMetadata",
    "EvaluateProcessorVersionRequest",
    "EvaluateProcessorVersionResponse",
    "FetchProcessorTypesRequest",
    "FetchProcessorTypesResponse",
    "GetEvaluationRequest",
    "GetProcessorRequest",
    "GetProcessorTypeRequest",
    "GetProcessorVersionRequest",
    "HumanReviewStatus",
    "ListEvaluationsRequest",
    "ListEvaluationsResponse",
    "ListProcessorsRequest",
    "ListProcessorsResponse",
    "ListProcessorTypesRequest",
    "ListProcessorTypesResponse",
    "ListProcessorVersionsRequest",
    "ListProcessorVersionsResponse",
    "ProcessOptions",
    "ProcessRequest",
    "ProcessResponse",
    "ReviewDocumentOperationMetadata",
    "ReviewDocumentRequest",
    "ReviewDocumentResponse",
    "SetDefaultProcessorVersionMetadata",
    "SetDefaultProcessorVersionRequest",
    "SetDefaultProcessorVersionResponse",
    "TrainProcessorVersionMetadata",
    "TrainProcessorVersionRequest",
    "TrainProcessorVersionResponse",
    "UndeployProcessorVersionMetadata",
    "UndeployProcessorVersionRequest",
    "UndeployProcessorVersionResponse",
    "DocumentSchema",
    "Evaluation",
    "EvaluationReference",
    "BoundingPoly",
    "NormalizedVertex",
    "Vertex",
    "CommonOperationMetadata",
    "Processor",
    "ProcessorVersion",
    "ProcessorVersionAlias",
    "ProcessorType",
)
