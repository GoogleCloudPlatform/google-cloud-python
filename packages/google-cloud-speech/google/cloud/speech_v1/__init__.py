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

from google.cloud.speech_v1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.speech_v1.services.adaptation",
    "google.cloud.speech_v1.services.speech",
    "google.cloud.speech_v1.types.cloud_speech",
    "google.cloud.speech_v1.types.cloud_speech_adaptation",
    "google.cloud.speech_v1.types.resource",
}


from google.cloud.speech_v1.helpers import SpeechHelpers

from .services.adaptation import AdaptationAsyncClient, AdaptationClient
from .services.speech import SpeechAsyncClient, SpeechClient
from .types.cloud_speech import (
    LongRunningRecognizeMetadata,
    LongRunningRecognizeRequest,
    LongRunningRecognizeResponse,
    RecognitionAudio,
    RecognitionConfig,
    RecognitionMetadata,
    RecognizeRequest,
    RecognizeResponse,
    SpeakerDiarizationConfig,
    SpeechAdaptationInfo,
    SpeechContext,
    SpeechRecognitionAlternative,
    SpeechRecognitionResult,
    StreamingRecognitionConfig,
    StreamingRecognitionResult,
    StreamingRecognizeRequest,
    StreamingRecognizeResponse,
    TranscriptOutputConfig,
    WordInfo,
)
from .types.cloud_speech_adaptation import (
    CreateCustomClassRequest,
    CreatePhraseSetRequest,
    DeleteCustomClassRequest,
    DeletePhraseSetRequest,
    GetCustomClassRequest,
    GetPhraseSetRequest,
    ListCustomClassesRequest,
    ListCustomClassesResponse,
    ListPhraseSetRequest,
    ListPhraseSetResponse,
    UpdateCustomClassRequest,
    UpdatePhraseSetRequest,
)
from .types.resource import (
    CustomClass,
    PhraseSet,
    SpeechAdaptation,
    TranscriptNormalization,
)


# This class merges the auto-generated GAPIC client with handwritten helper methods.
# We ignore [misc] because mypy is flagging that both parent classes have a method
# named `streaming_recognize`,
# but their type signatures don't match.
# We ignore [no-redef] because of the name shadow with SpeechClient. We don't want
# to expose the GAPIC client without the helpers.
class SpeechClient(SpeechHelpers, SpeechClient):  # type: ignore[no-redef, misc]
    __doc__ = SpeechClient.__doc__


__all__ = (
    "AdaptationAsyncClient",
    "SpeechAsyncClient",
    "AdaptationClient",
    "CreateCustomClassRequest",
    "CreatePhraseSetRequest",
    "CustomClass",
    "DeleteCustomClassRequest",
    "DeletePhraseSetRequest",
    "GetCustomClassRequest",
    "GetPhraseSetRequest",
    "ListCustomClassesRequest",
    "ListCustomClassesResponse",
    "ListPhraseSetRequest",
    "ListPhraseSetResponse",
    "LongRunningRecognizeMetadata",
    "LongRunningRecognizeRequest",
    "LongRunningRecognizeResponse",
    "PhraseSet",
    "RecognitionAudio",
    "RecognitionConfig",
    "RecognitionMetadata",
    "RecognizeRequest",
    "RecognizeResponse",
    "SpeakerDiarizationConfig",
    "SpeechAdaptation",
    "SpeechAdaptationInfo",
    "SpeechClient",
    "SpeechContext",
    "SpeechRecognitionAlternative",
    "SpeechRecognitionResult",
    "StreamingRecognitionConfig",
    "StreamingRecognitionResult",
    "StreamingRecognizeRequest",
    "StreamingRecognizeResponse",
    "TranscriptNormalization",
    "TranscriptOutputConfig",
    "UpdateCustomClassRequest",
    "UpdatePhraseSetRequest",
    "WordInfo",
)

api_core.check_python_version("google.cloud.speech_v1")
api_core.check_dependency_versions("google.cloud.speech_v1")
