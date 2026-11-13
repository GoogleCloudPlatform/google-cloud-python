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

from google.cloud.speech_v2 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.speech_v2.services.speech",
    "google.cloud.speech_v2.types.cloud_speech",
    "google.cloud.speech_v2.types.locations_metadata",
}


from .services.speech import SpeechAsyncClient, SpeechClient
from .types.cloud_speech import (
    AutoDetectDecodingConfig,
    BatchRecognizeFileMetadata,
    BatchRecognizeFileResult,
    BatchRecognizeMetadata,
    BatchRecognizeRequest,
    BatchRecognizeResponse,
    BatchRecognizeResults,
    BatchRecognizeTranscriptionMetadata,
    CloudStorageResult,
    Config,
    CreateCustomClassRequest,
    CreatePhraseSetRequest,
    CreateRecognizerRequest,
    CustomClass,
    CustomPromptConfig,
    DeleteCustomClassRequest,
    DeletePhraseSetRequest,
    DeleteRecognizerRequest,
    DenoiserConfig,
    ExplicitDecodingConfig,
    GcsOutputConfig,
    GetConfigRequest,
    GetCustomClassRequest,
    GetPhraseSetRequest,
    GetRecognizerRequest,
    InlineOutputConfig,
    InlineResult,
    ListCustomClassesRequest,
    ListCustomClassesResponse,
    ListPhraseSetsRequest,
    ListPhraseSetsResponse,
    ListRecognizersRequest,
    ListRecognizersResponse,
    NativeOutputFileFormatConfig,
    OperationMetadata,
    OutputFormatConfig,
    PhraseSet,
    RecognitionConfig,
    RecognitionFeatures,
    RecognitionOutputConfig,
    RecognitionResponseMetadata,
    Recognizer,
    RecognizeRequest,
    RecognizeResponse,
    SpeakerDiarizationConfig,
    SpeechAdaptation,
    SpeechRecognitionAlternative,
    SpeechRecognitionResult,
    SrtOutputFileFormatConfig,
    StreamingRecognitionConfig,
    StreamingRecognitionFeatures,
    StreamingRecognitionResult,
    StreamingRecognizeRequest,
    StreamingRecognizeResponse,
    TranscriptNormalization,
    TranslationConfig,
    UndeleteCustomClassRequest,
    UndeletePhraseSetRequest,
    UndeleteRecognizerRequest,
    UpdateConfigRequest,
    UpdateCustomClassRequest,
    UpdatePhraseSetRequest,
    UpdateRecognizerRequest,
    VttOutputFileFormatConfig,
    WordInfo,
)
from .types.locations_metadata import (
    AccessMetadata,
    LanguageMetadata,
    LocationsMetadata,
    ModelFeature,
    ModelFeatures,
    ModelMetadata,
)

__all__ = (
    "SpeechAsyncClient",
    "AccessMetadata",
    "AutoDetectDecodingConfig",
    "BatchRecognizeFileMetadata",
    "BatchRecognizeFileResult",
    "BatchRecognizeMetadata",
    "BatchRecognizeRequest",
    "BatchRecognizeResponse",
    "BatchRecognizeResults",
    "BatchRecognizeTranscriptionMetadata",
    "CloudStorageResult",
    "Config",
    "CreateCustomClassRequest",
    "CreatePhraseSetRequest",
    "CreateRecognizerRequest",
    "CustomClass",
    "CustomPromptConfig",
    "DeleteCustomClassRequest",
    "DeletePhraseSetRequest",
    "DeleteRecognizerRequest",
    "DenoiserConfig",
    "ExplicitDecodingConfig",
    "GcsOutputConfig",
    "GetConfigRequest",
    "GetCustomClassRequest",
    "GetPhraseSetRequest",
    "GetRecognizerRequest",
    "InlineOutputConfig",
    "InlineResult",
    "LanguageMetadata",
    "ListCustomClassesRequest",
    "ListCustomClassesResponse",
    "ListPhraseSetsRequest",
    "ListPhraseSetsResponse",
    "ListRecognizersRequest",
    "ListRecognizersResponse",
    "LocationsMetadata",
    "ModelFeature",
    "ModelFeatures",
    "ModelMetadata",
    "NativeOutputFileFormatConfig",
    "OperationMetadata",
    "OutputFormatConfig",
    "PhraseSet",
    "RecognitionConfig",
    "RecognitionFeatures",
    "RecognitionOutputConfig",
    "RecognitionResponseMetadata",
    "RecognizeRequest",
    "RecognizeResponse",
    "Recognizer",
    "SpeakerDiarizationConfig",
    "SpeechAdaptation",
    "SpeechClient",
    "SpeechRecognitionAlternative",
    "SpeechRecognitionResult",
    "SrtOutputFileFormatConfig",
    "StreamingRecognitionConfig",
    "StreamingRecognitionFeatures",
    "StreamingRecognitionResult",
    "StreamingRecognizeRequest",
    "StreamingRecognizeResponse",
    "TranscriptNormalization",
    "TranslationConfig",
    "UndeleteCustomClassRequest",
    "UndeletePhraseSetRequest",
    "UndeleteRecognizerRequest",
    "UpdateConfigRequest",
    "UpdateCustomClassRequest",
    "UpdatePhraseSetRequest",
    "UpdateRecognizerRequest",
    "VttOutputFileFormatConfig",
    "WordInfo",
)

api_core.check_python_version("google.cloud.speech_v2")
api_core.check_dependency_versions("google.cloud.speech_v2")
