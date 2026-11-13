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

from google.cloud.recommendationengine_v1beta1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.recommendationengine_v1beta1.services.catalog_service",
    "google.cloud.recommendationengine_v1beta1.services.prediction_api_key_registry",
    "google.cloud.recommendationengine_v1beta1.services.prediction_service",
    "google.cloud.recommendationengine_v1beta1.services.user_event_service",
    "google.cloud.recommendationengine_v1beta1.types.catalog",
    "google.cloud.recommendationengine_v1beta1.types.catalog_service",
    "google.cloud.recommendationengine_v1beta1.types.common",
    "google.cloud.recommendationengine_v1beta1.types.import_",
    "google.cloud.recommendationengine_v1beta1.types.prediction_apikey_registry_service",
    "google.cloud.recommendationengine_v1beta1.types.prediction_service",
    "google.cloud.recommendationengine_v1beta1.types.recommendationengine_resources",
    "google.cloud.recommendationengine_v1beta1.types.user_event",
    "google.cloud.recommendationengine_v1beta1.types.user_event_service",
}


from .services.catalog_service import CatalogServiceAsyncClient, CatalogServiceClient
from .services.prediction_api_key_registry import (
    PredictionApiKeyRegistryAsyncClient,
    PredictionApiKeyRegistryClient,
)
from .services.prediction_service import (
    PredictionServiceAsyncClient,
    PredictionServiceClient,
)
from .services.user_event_service import (
    UserEventServiceAsyncClient,
    UserEventServiceClient,
)
from .types.catalog import CatalogItem, Image, ProductCatalogItem
from .types.catalog_service import (
    CreateCatalogItemRequest,
    DeleteCatalogItemRequest,
    GetCatalogItemRequest,
    ListCatalogItemsRequest,
    ListCatalogItemsResponse,
    UpdateCatalogItemRequest,
)
from .types.common import FeatureMap
from .types.import_ import (
    CatalogInlineSource,
    GcsSource,
    ImportCatalogItemsRequest,
    ImportCatalogItemsResponse,
    ImportErrorsConfig,
    ImportMetadata,
    ImportUserEventsRequest,
    ImportUserEventsResponse,
    InputConfig,
    UserEventImportSummary,
    UserEventInlineSource,
)
from .types.prediction_apikey_registry_service import (
    CreatePredictionApiKeyRegistrationRequest,
    DeletePredictionApiKeyRegistrationRequest,
    ListPredictionApiKeyRegistrationsRequest,
    ListPredictionApiKeyRegistrationsResponse,
    PredictionApiKeyRegistration,
)
from .types.prediction_service import PredictRequest, PredictResponse
from .types.user_event import (
    EventDetail,
    ProductDetail,
    ProductEventDetail,
    PurchaseTransaction,
    UserEvent,
    UserInfo,
)
from .types.user_event_service import (
    CollectUserEventRequest,
    ListUserEventsRequest,
    ListUserEventsResponse,
    PurgeUserEventsMetadata,
    PurgeUserEventsRequest,
    PurgeUserEventsResponse,
    WriteUserEventRequest,
)

__all__ = (
    "CatalogServiceAsyncClient",
    "PredictionApiKeyRegistryAsyncClient",
    "PredictionServiceAsyncClient",
    "UserEventServiceAsyncClient",
    "CatalogInlineSource",
    "CatalogItem",
    "CatalogServiceClient",
    "CollectUserEventRequest",
    "CreateCatalogItemRequest",
    "CreatePredictionApiKeyRegistrationRequest",
    "DeleteCatalogItemRequest",
    "DeletePredictionApiKeyRegistrationRequest",
    "EventDetail",
    "FeatureMap",
    "GcsSource",
    "GetCatalogItemRequest",
    "Image",
    "ImportCatalogItemsRequest",
    "ImportCatalogItemsResponse",
    "ImportErrorsConfig",
    "ImportMetadata",
    "ImportUserEventsRequest",
    "ImportUserEventsResponse",
    "InputConfig",
    "ListCatalogItemsRequest",
    "ListCatalogItemsResponse",
    "ListPredictionApiKeyRegistrationsRequest",
    "ListPredictionApiKeyRegistrationsResponse",
    "ListUserEventsRequest",
    "ListUserEventsResponse",
    "PredictRequest",
    "PredictResponse",
    "PredictionApiKeyRegistration",
    "PredictionApiKeyRegistryClient",
    "PredictionServiceClient",
    "ProductCatalogItem",
    "ProductDetail",
    "ProductEventDetail",
    "PurchaseTransaction",
    "PurgeUserEventsMetadata",
    "PurgeUserEventsRequest",
    "PurgeUserEventsResponse",
    "UpdateCatalogItemRequest",
    "UserEvent",
    "UserEventImportSummary",
    "UserEventInlineSource",
    "UserEventServiceClient",
    "UserInfo",
    "WriteUserEventRequest",
)

api_core.check_python_version("google.cloud.recommendationengine_v1beta1")
api_core.check_dependency_versions("google.cloud.recommendationengine_v1beta1")
