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

from google.cloud.cloudquotas_v1beta import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.cloudquotas_v1beta.services.cloud_quotas",
    "google.cloud.cloudquotas_v1beta.services.quota_adjuster_settings_manager",
    "google.cloud.cloudquotas_v1beta.types.cloudquotas",
    "google.cloud.cloudquotas_v1beta.types.quota_adjuster_settings",
    "google.cloud.cloudquotas_v1beta.types.resources",
}


from .services.cloud_quotas import CloudQuotasAsyncClient, CloudQuotasClient
from .services.quota_adjuster_settings_manager import (
    QuotaAdjusterSettingsManagerAsyncClient,
    QuotaAdjusterSettingsManagerClient,
)
from .types.cloudquotas import (
    CreateQuotaPreferenceRequest,
    GetQuotaInfoRequest,
    GetQuotaPreferenceRequest,
    ListQuotaInfosRequest,
    ListQuotaInfosResponse,
    ListQuotaPreferencesRequest,
    ListQuotaPreferencesResponse,
    UpdateQuotaPreferenceRequest,
)
from .types.quota_adjuster_settings import (
    GetQuotaAdjusterSettingsRequest,
    QuotaAdjusterSettings,
    UpdateQuotaAdjusterSettingsRequest,
)
from .types.resources import (
    DimensionsInfo,
    QuotaConfig,
    QuotaDetails,
    QuotaIncreaseEligibility,
    QuotaInfo,
    QuotaPreference,
    QuotaSafetyCheck,
    RolloutInfo,
)

__all__ = (
    "CloudQuotasAsyncClient",
    "QuotaAdjusterSettingsManagerAsyncClient",
    "CloudQuotasClient",
    "CreateQuotaPreferenceRequest",
    "DimensionsInfo",
    "GetQuotaAdjusterSettingsRequest",
    "GetQuotaInfoRequest",
    "GetQuotaPreferenceRequest",
    "ListQuotaInfosRequest",
    "ListQuotaInfosResponse",
    "ListQuotaPreferencesRequest",
    "ListQuotaPreferencesResponse",
    "QuotaAdjusterSettings",
    "QuotaAdjusterSettingsManagerClient",
    "QuotaConfig",
    "QuotaDetails",
    "QuotaIncreaseEligibility",
    "QuotaInfo",
    "QuotaPreference",
    "QuotaSafetyCheck",
    "RolloutInfo",
    "UpdateQuotaAdjusterSettingsRequest",
    "UpdateQuotaPreferenceRequest",
)

api_core.check_python_version("google.cloud.cloudquotas_v1beta")
api_core.check_dependency_versions("google.cloud.cloudquotas_v1beta")
