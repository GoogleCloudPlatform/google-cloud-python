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
from google.shopping.merchant_conversions import gapic_version as package_version

__version__ = package_version.__version__


from google.shopping.merchant_conversions_v1.services.conversion_sources_service.async_client import (
    ConversionSourcesServiceAsyncClient,
)
from google.shopping.merchant_conversions_v1.services.conversion_sources_service.client import (
    ConversionSourcesServiceClient,
)
from google.shopping.merchant_conversions_v1.types.conversionsources import (
    AttributionSettings,
    ConversionSource,
    CreateConversionSourceRequest,
    DeleteConversionSourceRequest,
    GetConversionSourceRequest,
    GoogleAnalyticsLink,
    ListConversionSourcesRequest,
    ListConversionSourcesResponse,
    MerchantCenterDestination,
    UndeleteConversionSourceRequest,
    UpdateConversionSourceRequest,
)

__all__ = (
    "ConversionSourcesServiceClient",
    "ConversionSourcesServiceAsyncClient",
    "AttributionSettings",
    "ConversionSource",
    "CreateConversionSourceRequest",
    "DeleteConversionSourceRequest",
    "GetConversionSourceRequest",
    "GoogleAnalyticsLink",
    "ListConversionSourcesRequest",
    "ListConversionSourcesResponse",
    "MerchantCenterDestination",
    "UndeleteConversionSourceRequest",
    "UpdateConversionSourceRequest",
)
