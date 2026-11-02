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

from google.ai.generativelanguage_v1beta2 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.ai.generativelanguage_v1beta2.services.discuss_service",
    "google.ai.generativelanguage_v1beta2.services.model_service",
    "google.ai.generativelanguage_v1beta2.services.text_service",
    "google.ai.generativelanguage_v1beta2.types.citation",
    "google.ai.generativelanguage_v1beta2.types.discuss_service",
    "google.ai.generativelanguage_v1beta2.types.model",
    "google.ai.generativelanguage_v1beta2.types.model_service",
    "google.ai.generativelanguage_v1beta2.types.safety",
    "google.ai.generativelanguage_v1beta2.types.text_service",
}


from .services.discuss_service import DiscussServiceAsyncClient, DiscussServiceClient
from .services.model_service import ModelServiceAsyncClient, ModelServiceClient
from .services.text_service import TextServiceAsyncClient, TextServiceClient
from .types.citation import CitationMetadata, CitationSource
from .types.discuss_service import (
    CountMessageTokensRequest,
    CountMessageTokensResponse,
    Example,
    GenerateMessageRequest,
    GenerateMessageResponse,
    Message,
    MessagePrompt,
)
from .types.model import Model
from .types.model_service import GetModelRequest, ListModelsRequest, ListModelsResponse
from .types.safety import (
    ContentFilter,
    HarmCategory,
    SafetyFeedback,
    SafetyRating,
    SafetySetting,
)
from .types.text_service import (
    Embedding,
    EmbedTextRequest,
    EmbedTextResponse,
    GenerateTextRequest,
    GenerateTextResponse,
    TextCompletion,
    TextPrompt,
)

__all__ = (
    "DiscussServiceAsyncClient",
    "ModelServiceAsyncClient",
    "TextServiceAsyncClient",
    "CitationMetadata",
    "CitationSource",
    "ContentFilter",
    "CountMessageTokensRequest",
    "CountMessageTokensResponse",
    "DiscussServiceClient",
    "EmbedTextRequest",
    "EmbedTextResponse",
    "Embedding",
    "Example",
    "GenerateMessageRequest",
    "GenerateMessageResponse",
    "GenerateTextRequest",
    "GenerateTextResponse",
    "GetModelRequest",
    "HarmCategory",
    "ListModelsRequest",
    "ListModelsResponse",
    "Message",
    "MessagePrompt",
    "Model",
    "ModelServiceClient",
    "SafetyFeedback",
    "SafetyRating",
    "SafetySetting",
    "TextCompletion",
    "TextPrompt",
    "TextServiceClient",
)

api_core.check_python_version("google.ai.generativelanguage_v1beta2")
api_core.check_dependency_versions("google.ai.generativelanguage_v1beta2")
