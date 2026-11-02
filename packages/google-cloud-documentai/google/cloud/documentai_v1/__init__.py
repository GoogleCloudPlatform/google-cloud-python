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

from google.cloud.documentai_v1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.documentai_v1.services.document_processor_service",
    "google.cloud.documentai_v1.types.barcode",
    "google.cloud.documentai_v1.types.document",
    "google.cloud.documentai_v1.types.document_io",
    "google.cloud.documentai_v1.types.document_processor_service",
    "google.cloud.documentai_v1.types.document_schema",
    "google.cloud.documentai_v1.types.evaluation",
    "google.cloud.documentai_v1.types.geometry",
    "google.cloud.documentai_v1.types.operation_metadata",
    "google.cloud.documentai_v1.types.processor",
    "google.cloud.documentai_v1.types.processor_type",
}


from .services.document_processor_service import (
    DocumentProcessorServiceAsyncClient,
    DocumentProcessorServiceClient,
)
from .types.barcode import Barcode
from .types.document import Document
from .types.document_io import (
    BatchDocumentsInputConfig,
    DocumentOutputConfig,
    GcsDocument,
    GcsDocuments,
    GcsPrefix,
    OcrConfig,
    RawDocument,
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
from .types.document_schema import DocumentSchema
from .types.evaluation import Evaluation, EvaluationReference
from .types.geometry import BoundingPoly, NormalizedVertex, Vertex
from .types.operation_metadata import CommonOperationMetadata
from .types.processor import Processor, ProcessorVersion, ProcessorVersionAlias
from .types.processor_type import ProcessorType

__all__ = (
    "DocumentProcessorServiceAsyncClient",
    "Barcode",
    "BatchDocumentsInputConfig",
    "BatchProcessMetadata",
    "BatchProcessRequest",
    "BatchProcessResponse",
    "BoundingPoly",
    "CommonOperationMetadata",
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
    "Document",
    "DocumentOutputConfig",
    "DocumentProcessorServiceClient",
    "DocumentSchema",
    "EnableProcessorMetadata",
    "EnableProcessorRequest",
    "EnableProcessorResponse",
    "EvaluateProcessorVersionMetadata",
    "EvaluateProcessorVersionRequest",
    "EvaluateProcessorVersionResponse",
    "Evaluation",
    "EvaluationReference",
    "FetchProcessorTypesRequest",
    "FetchProcessorTypesResponse",
    "GcsDocument",
    "GcsDocuments",
    "GcsPrefix",
    "GetEvaluationRequest",
    "GetProcessorRequest",
    "GetProcessorTypeRequest",
    "GetProcessorVersionRequest",
    "HumanReviewStatus",
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
    "RawDocument",
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
    "Vertex",
)

api_core.check_python_version("google.cloud.documentai_v1")
api_core.check_dependency_versions("google.cloud.documentai_v1")
