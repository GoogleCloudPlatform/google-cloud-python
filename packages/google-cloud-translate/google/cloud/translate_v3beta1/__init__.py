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

from google.cloud.translate_v3beta1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.translate_v3beta1.services.translation_service",
    "google.cloud.translate_v3beta1.types.translation_service",
}


from .services.translation_service import (
    TranslationServiceAsyncClient,
    TranslationServiceClient,
)
from .types.translation_service import (
    BatchDocumentInputConfig,
    BatchDocumentOutputConfig,
    BatchTranslateDocumentMetadata,
    BatchTranslateDocumentRequest,
    BatchTranslateDocumentResponse,
    BatchTranslateMetadata,
    BatchTranslateResponse,
    BatchTranslateTextRequest,
    CreateGlossaryMetadata,
    CreateGlossaryRequest,
    DeleteGlossaryMetadata,
    DeleteGlossaryRequest,
    DeleteGlossaryResponse,
    DetectedLanguage,
    DetectLanguageRequest,
    DetectLanguageResponse,
    DocumentInputConfig,
    DocumentOutputConfig,
    DocumentTranslation,
    GcsDestination,
    GcsSource,
    GetGlossaryRequest,
    GetSupportedLanguagesRequest,
    Glossary,
    GlossaryInputConfig,
    InputConfig,
    ListGlossariesRequest,
    ListGlossariesResponse,
    OutputConfig,
    RefinementEntry,
    RefineTextRequest,
    RefineTextResponse,
    SupportedLanguage,
    SupportedLanguages,
    TranslateDocumentRequest,
    TranslateDocumentResponse,
    TranslateTextGlossaryConfig,
    TranslateTextRequest,
    TranslateTextResponse,
    Translation,
)

__all__ = (
    "TranslationServiceAsyncClient",
    "BatchDocumentInputConfig",
    "BatchDocumentOutputConfig",
    "BatchTranslateDocumentMetadata",
    "BatchTranslateDocumentRequest",
    "BatchTranslateDocumentResponse",
    "BatchTranslateMetadata",
    "BatchTranslateResponse",
    "BatchTranslateTextRequest",
    "CreateGlossaryMetadata",
    "CreateGlossaryRequest",
    "DeleteGlossaryMetadata",
    "DeleteGlossaryRequest",
    "DeleteGlossaryResponse",
    "DetectLanguageRequest",
    "DetectLanguageResponse",
    "DetectedLanguage",
    "DocumentInputConfig",
    "DocumentOutputConfig",
    "DocumentTranslation",
    "GcsDestination",
    "GcsSource",
    "GetGlossaryRequest",
    "GetSupportedLanguagesRequest",
    "Glossary",
    "GlossaryInputConfig",
    "InputConfig",
    "ListGlossariesRequest",
    "ListGlossariesResponse",
    "OutputConfig",
    "RefineTextRequest",
    "RefineTextResponse",
    "RefinementEntry",
    "SupportedLanguage",
    "SupportedLanguages",
    "TranslateDocumentRequest",
    "TranslateDocumentResponse",
    "TranslateTextGlossaryConfig",
    "TranslateTextRequest",
    "TranslateTextResponse",
    "Translation",
    "TranslationServiceClient",
)

api_core.check_python_version("google.cloud.translate_v3beta1")
api_core.check_dependency_versions("google.cloud.translate_v3beta1")
