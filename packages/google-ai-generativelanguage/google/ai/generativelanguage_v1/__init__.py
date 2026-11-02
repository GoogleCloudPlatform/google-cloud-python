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

from google.ai.generativelanguage_v1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.ai.generativelanguage_v1.services.generative_service",
    "google.ai.generativelanguage_v1.services.model_service",
    "google.ai.generativelanguage_v1.types.citation",
    "google.ai.generativelanguage_v1.types.content",
    "google.ai.generativelanguage_v1.types.generative_service",
    "google.ai.generativelanguage_v1.types.model",
    "google.ai.generativelanguage_v1.types.model_service",
    "google.ai.generativelanguage_v1.types.safety",
}


from .services.generative_service import (
    GenerativeServiceAsyncClient,
    GenerativeServiceClient,
)
from .services.model_service import ModelServiceAsyncClient, ModelServiceClient
from .types.citation import CitationMetadata, CitationSource
from .types.content import (
    Blob,
    Content,
    Modality,
    ModalityTokenCount,
    Part,
    VideoMetadata,
)
from .types.generative_service import (
    BatchEmbedContentsRequest,
    BatchEmbedContentsResponse,
    Candidate,
    ContentEmbedding,
    CountTokensRequest,
    CountTokensResponse,
    EmbedContentRequest,
    EmbedContentResponse,
    GenerateContentRequest,
    GenerateContentResponse,
    GenerationConfig,
    GroundingChunk,
    GroundingMetadata,
    GroundingSupport,
    LogprobsResult,
    RetrievalMetadata,
    SearchEntryPoint,
    Segment,
    TaskType,
    UrlContextMetadata,
    UrlMetadata,
)
from .types.model import Model
from .types.model_service import GetModelRequest, ListModelsRequest, ListModelsResponse
from .types.safety import HarmCategory, SafetyRating, SafetySetting

__all__ = (
    "GenerativeServiceAsyncClient",
    "ModelServiceAsyncClient",
    "BatchEmbedContentsRequest",
    "BatchEmbedContentsResponse",
    "Blob",
    "Candidate",
    "CitationMetadata",
    "CitationSource",
    "Content",
    "ContentEmbedding",
    "CountTokensRequest",
    "CountTokensResponse",
    "EmbedContentRequest",
    "EmbedContentResponse",
    "GenerateContentRequest",
    "GenerateContentResponse",
    "GenerationConfig",
    "GenerativeServiceClient",
    "GetModelRequest",
    "GroundingChunk",
    "GroundingMetadata",
    "GroundingSupport",
    "HarmCategory",
    "ListModelsRequest",
    "ListModelsResponse",
    "LogprobsResult",
    "Modality",
    "ModalityTokenCount",
    "Model",
    "ModelServiceClient",
    "Part",
    "RetrievalMetadata",
    "SafetyRating",
    "SafetySetting",
    "SearchEntryPoint",
    "Segment",
    "TaskType",
    "UrlContextMetadata",
    "UrlMetadata",
    "VideoMetadata",
)

api_core.check_python_version("google.ai.generativelanguage_v1")
api_core.check_dependency_versions("google.ai.generativelanguage_v1")
