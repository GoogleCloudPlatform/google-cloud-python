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

from google.cloud.modelarmor_v1beta import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.modelarmor_v1beta.services.model_armor",
    "google.cloud.modelarmor_v1beta.types.service",
}


from .services.model_armor import ModelArmorAsyncClient, ModelArmorClient
from .types.service import (
    AiPlatformFloorSetting,
    ByteDataItem,
    CreateTemplateRequest,
    CsamFilterResult,
    DataItem,
    DeleteTemplateRequest,
    DetectionConfidenceLevel,
    FilterConfig,
    FilterExecutionState,
    FilterMatchState,
    FilterResult,
    FloorSetting,
    GetFloorSettingRequest,
    GetTemplateRequest,
    InvocationResult,
    ListTemplatesRequest,
    ListTemplatesResponse,
    MaliciousUriFilterResult,
    MaliciousUriFilterSettings,
    McpServerFloorSetting,
    MessageItem,
    MultiLanguageDetectionMetadata,
    PiAndJailbreakFilterResult,
    PiAndJailbreakFilterSettings,
    RaiFilterResult,
    RaiFilterSettings,
    RaiFilterType,
    RangeInfo,
    SanitizationResult,
    SanitizeModelResponseRequest,
    SanitizeModelResponseResponse,
    SanitizeUserPromptRequest,
    SanitizeUserPromptResponse,
    SdpAdvancedConfig,
    SdpBasicConfig,
    SdpDeidentifyResult,
    SdpFilterResult,
    SdpFilterSettings,
    SdpFinding,
    SdpFindingLikelihood,
    SdpInspectResult,
    StreamingMode,
    Template,
    UpdateFloorSettingRequest,
    UpdateTemplateRequest,
    VirusDetail,
    VirusScanFilterResult,
)

__all__ = (
    "ModelArmorAsyncClient",
    "AiPlatformFloorSetting",
    "ByteDataItem",
    "CreateTemplateRequest",
    "CsamFilterResult",
    "DataItem",
    "DeleteTemplateRequest",
    "DetectionConfidenceLevel",
    "FilterConfig",
    "FilterExecutionState",
    "FilterMatchState",
    "FilterResult",
    "FloorSetting",
    "GetFloorSettingRequest",
    "GetTemplateRequest",
    "InvocationResult",
    "ListTemplatesRequest",
    "ListTemplatesResponse",
    "MaliciousUriFilterResult",
    "MaliciousUriFilterSettings",
    "McpServerFloorSetting",
    "MessageItem",
    "ModelArmorClient",
    "MultiLanguageDetectionMetadata",
    "PiAndJailbreakFilterResult",
    "PiAndJailbreakFilterSettings",
    "RaiFilterResult",
    "RaiFilterSettings",
    "RaiFilterType",
    "RangeInfo",
    "SanitizationResult",
    "SanitizeModelResponseRequest",
    "SanitizeModelResponseResponse",
    "SanitizeUserPromptRequest",
    "SanitizeUserPromptResponse",
    "SdpAdvancedConfig",
    "SdpBasicConfig",
    "SdpDeidentifyResult",
    "SdpFilterResult",
    "SdpFilterSettings",
    "SdpFinding",
    "SdpFindingLikelihood",
    "SdpInspectResult",
    "StreamingMode",
    "Template",
    "UpdateFloorSettingRequest",
    "UpdateTemplateRequest",
    "VirusDetail",
    "VirusScanFilterResult",
)

api_core.check_python_version("google.cloud.modelarmor_v1beta")
api_core.check_dependency_versions("google.cloud.modelarmor_v1beta")
