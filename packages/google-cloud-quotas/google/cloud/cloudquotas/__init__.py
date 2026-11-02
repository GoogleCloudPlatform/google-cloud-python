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
from google.cloud.cloudquotas import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.cloudquotas_v1.services.cloud_quotas.async_client import (
    CloudQuotasAsyncClient,
)
from google.cloud.cloudquotas_v1.services.cloud_quotas.client import CloudQuotasClient
from google.cloud.cloudquotas_v1.services.quota_adjuster_settings_manager.async_client import (
    QuotaAdjusterSettingsManagerAsyncClient,
)
from google.cloud.cloudquotas_v1.services.quota_adjuster_settings_manager.client import (
    QuotaAdjusterSettingsManagerClient,
)
from google.cloud.cloudquotas_v1.types.cloudquotas import (
    CreateQuotaPreferenceRequest,
    GetQuotaInfoRequest,
    GetQuotaPreferenceRequest,
    ListQuotaInfosRequest,
    ListQuotaInfosResponse,
    ListQuotaPreferencesRequest,
    ListQuotaPreferencesResponse,
    UpdateQuotaPreferenceRequest,
)
from google.cloud.cloudquotas_v1.types.quota_adjuster_settings import (
    GetQuotaAdjusterSettingsRequest,
    QuotaAdjusterSettings,
    UpdateQuotaAdjusterSettingsRequest,
)
from google.cloud.cloudquotas_v1.types.resources import (
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
    "CloudQuotasClient",
    "CloudQuotasAsyncClient",
    "QuotaAdjusterSettingsManagerClient",
    "QuotaAdjusterSettingsManagerAsyncClient",
    "CreateQuotaPreferenceRequest",
    "GetQuotaInfoRequest",
    "GetQuotaPreferenceRequest",
    "ListQuotaInfosRequest",
    "ListQuotaInfosResponse",
    "ListQuotaPreferencesRequest",
    "ListQuotaPreferencesResponse",
    "UpdateQuotaPreferenceRequest",
    "GetQuotaAdjusterSettingsRequest",
    "QuotaAdjusterSettings",
    "UpdateQuotaAdjusterSettingsRequest",
    "DimensionsInfo",
    "QuotaConfig",
    "QuotaDetails",
    "QuotaIncreaseEligibility",
    "QuotaInfo",
    "QuotaPreference",
    "RolloutInfo",
    "QuotaSafetyCheck",
)
