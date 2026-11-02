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
import google.api_core as api_core

from google.cloud.documentai_v1beta3 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.documentai_v1beta3.services.document_processor_service",
    "google.cloud.documentai_v1beta3.services.document_service",
    "google.cloud.documentai_v1beta3.types.barcode",
    "google.cloud.documentai_v1beta3.types.dataset",
    "google.cloud.documentai_v1beta3.types.document",
    "google.cloud.documentai_v1beta3.types.document_io",
    "google.cloud.documentai_v1beta3.types.document_processor_service",
    "google.cloud.documentai_v1beta3.types.document_schema",
    "google.cloud.documentai_v1beta3.types.document_service",
    "google.cloud.documentai_v1beta3.types.evaluation",
    "google.cloud.documentai_v1beta3.types.geometry",
    "google.cloud.documentai_v1beta3.types.operation_metadata",
    "google.cloud.documentai_v1beta3.types.processor",
    "google.cloud.documentai_v1beta3.types.processor_type",
}


from .services.document_processor_service import (
    DocumentProcessorServiceAsyncClient,
    DocumentProcessorServiceClient,
)
from .services.document_service import DocumentServiceAsyncClient, DocumentServiceClient
from .types.barcode import Barcode
from .types.dataset import BatchDatasetDocuments, Dataset, DatasetSchema, DocumentId
from .types.document import Document, RevisionRef
from .types.document_io import (
    BatchDocumentsInputConfig,
    DocumentOutputConfig,
    Documents,
    GcsDocument,
    GcsDocuments,
    GcsPrefix,
    OcrConfig,
    RawDocument,
    RawDocuments,
)
from .types.document_processor_service import (
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
    ImportProcessorVersionMetadata,
    ImportProcessorVersionRequest,
    ImportProcessorVersionResponse,
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
    UpdateProcessorVersionMetadata,
)
from .types.document_schema import (
    DocumentSchema,
    EntityTypeMetadata,
    FieldExtractionMetadata,
    PropertyMetadata,
    SummaryOptions,
)
from .types.document_service import (
    BatchDeleteDocumentsMetadata,
    BatchDeleteDocumentsRequest,
    BatchDeleteDocumentsResponse,
    DatasetSplitType,
    DocumentLabelingState,
    DocumentMetadata,
    DocumentPageRange,
    GetDatasetSchemaRequest,
    GetDocumentRequest,
    GetDocumentResponse,
    ImportDocumentsMetadata,
    ImportDocumentsRequest,
    ImportDocumentsResponse,
    ListDocumentsRequest,
    ListDocumentsResponse,
    UpdateDatasetOperationMetadata,
    UpdateDatasetRequest,
    UpdateDatasetSchemaRequest,
)
from .types.evaluation import Evaluation, EvaluationReference
from .types.geometry import BoundingPoly, NormalizedVertex, Vertex
from .types.operation_metadata import CommonOperationMetadata
from .types.processor import (
    GroundingSettings,
    Processor,
    ProcessorVersion,
    ProcessorVersionAlias,
    ProcessorVersionOverrides,
)
from .types.processor_type import ProcessorType

__all__ = (
    "DocumentProcessorServiceAsyncClient",
    "DocumentServiceAsyncClient",
    "Barcode",
    "BatchDatasetDocuments",
    "BatchDeleteDocumentsMetadata",
    "BatchDeleteDocumentsRequest",
    "BatchDeleteDocumentsResponse",
    "BatchDocumentsInputConfig",
    "BatchProcessMetadata",
    "BatchProcessRequest",
    "BatchProcessResponse",
    "BoundingPoly",
    "CommonOperationMetadata",
    "CreateProcessorRequest",
    "Dataset",
    "DatasetSchema",
    "DatasetSplitType",
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
    "Document",
    "DocumentId",
    "DocumentLabelingState",
    "DocumentMetadata",
    "DocumentOutputConfig",
    "DocumentPageRange",
    "DocumentProcessorServiceClient",
    "DocumentSchema",
    "DocumentServiceClient",
    "Documents",
    "EnableProcessorMetadata",
    "EnableProcessorRequest",
    "EnableProcessorResponse",
    "EntityTypeMetadata",
    "EvaluateProcessorVersionMetadata",
    "EvaluateProcessorVersionRequest",
    "EvaluateProcessorVersionResponse",
    "Evaluation",
    "EvaluationReference",
    "FetchProcessorTypesRequest",
    "FetchProcessorTypesResponse",
    "FieldExtractionMetadata",
    "GcsDocument",
    "GcsDocuments",
    "GcsPrefix",
    "GetDatasetSchemaRequest",
    "GetDocumentRequest",
    "GetDocumentResponse",
    "GetEvaluationRequest",
    "GetProcessorRequest",
    "GetProcessorTypeRequest",
    "GetProcessorVersionRequest",
    "GroundingSettings",
    "HumanReviewStatus",
    "ImportDocumentsMetadata",
    "ImportDocumentsRequest",
    "ImportDocumentsResponse",
    "ImportProcessorVersionMetadata",
    "ImportProcessorVersionRequest",
    "ImportProcessorVersionResponse",
    "ListDocumentsRequest",
    "ListDocumentsResponse",
    "ListEvaluationsRequest",
    "ListEvaluationsResponse",
    "ListProcessorTypesRequest",
    "ListProcessorTypesResponse",
    "ListProcessorVersionsRequest",
    "ListProcessorVersionsResponse",
    "ListProcessorsRequest",
    "ListProcessorsResponse",
    "NormalizedVertex",
    "OcrConfig",
    "ProcessOptions",
    "ProcessRequest",
    "ProcessResponse",
    "Processor",
    "ProcessorType",
    "ProcessorVersion",
    "ProcessorVersionAlias",
    "ProcessorVersionOverrides",
    "PropertyMetadata",
    "RawDocument",
    "RawDocuments",
    "ReviewDocumentOperationMetadata",
    "ReviewDocumentRequest",
    "ReviewDocumentResponse",
    "RevisionRef",
    "SetDefaultProcessorVersionMetadata",
    "SetDefaultProcessorVersionRequest",
    "SetDefaultProcessorVersionResponse",
    "SummaryOptions",
    "TrainProcessorVersionMetadata",
    "TrainProcessorVersionRequest",
    "TrainProcessorVersionResponse",
    "UndeployProcessorVersionMetadata",
    "UndeployProcessorVersionRequest",
    "UndeployProcessorVersionResponse",
    "UpdateDatasetOperationMetadata",
    "UpdateDatasetRequest",
    "UpdateDatasetSchemaRequest",
    "UpdateProcessorVersionMetadata",
    "Vertex",
)

api_core.check_python_version("google.cloud.documentai_v1beta3")
api_core.check_dependency_versions("google.cloud.documentai_v1beta3")
