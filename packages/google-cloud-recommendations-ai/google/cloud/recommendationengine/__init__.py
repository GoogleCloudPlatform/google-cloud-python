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
from google.cloud.recommendationengine import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.recommendationengine_v1beta1.services.catalog_service.async_client import (
    CatalogServiceAsyncClient,
)
from google.cloud.recommendationengine_v1beta1.services.catalog_service.client import (
    CatalogServiceClient,
)
from google.cloud.recommendationengine_v1beta1.services.prediction_api_key_registry.async_client import (
    PredictionApiKeyRegistryAsyncClient,
)
from google.cloud.recommendationengine_v1beta1.services.prediction_api_key_registry.client import (
    PredictionApiKeyRegistryClient,
)
from google.cloud.recommendationengine_v1beta1.services.prediction_service.async_client import (
    PredictionServiceAsyncClient,
)
from google.cloud.recommendationengine_v1beta1.services.prediction_service.client import (
    PredictionServiceClient,
)
from google.cloud.recommendationengine_v1beta1.services.user_event_service.async_client import (
    UserEventServiceAsyncClient,
)
from google.cloud.recommendationengine_v1beta1.services.user_event_service.client import (
    UserEventServiceClient,
)
from google.cloud.recommendationengine_v1beta1.types.catalog import (
    CatalogItem,
    Image,
    ProductCatalogItem,
)
from google.cloud.recommendationengine_v1beta1.types.catalog_service import (
    CreateCatalogItemRequest,
    DeleteCatalogItemRequest,
    GetCatalogItemRequest,
    ListCatalogItemsRequest,
    ListCatalogItemsResponse,
    UpdateCatalogItemRequest,
)
from google.cloud.recommendationengine_v1beta1.types.common import FeatureMap
from google.cloud.recommendationengine_v1beta1.types.import_ import (
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
from google.cloud.recommendationengine_v1beta1.types.prediction_apikey_registry_service import (
    CreatePredictionApiKeyRegistrationRequest,
    DeletePredictionApiKeyRegistrationRequest,
    ListPredictionApiKeyRegistrationsRequest,
    ListPredictionApiKeyRegistrationsResponse,
    PredictionApiKeyRegistration,
)
from google.cloud.recommendationengine_v1beta1.types.prediction_service import (
    PredictRequest,
    PredictResponse,
)
from google.cloud.recommendationengine_v1beta1.types.user_event import (
    EventDetail,
    ProductDetail,
    ProductEventDetail,
    PurchaseTransaction,
    UserEvent,
    UserInfo,
)
from google.cloud.recommendationengine_v1beta1.types.user_event_service import (
    CollectUserEventRequest,
    ListUserEventsRequest,
    ListUserEventsResponse,
    PurgeUserEventsMetadata,
    PurgeUserEventsRequest,
    PurgeUserEventsResponse,
    WriteUserEventRequest,
)

__all__ = (
    "CatalogServiceClient",
    "CatalogServiceAsyncClient",
    "PredictionApiKeyRegistryClient",
    "PredictionApiKeyRegistryAsyncClient",
    "PredictionServiceClient",
    "PredictionServiceAsyncClient",
    "UserEventServiceClient",
    "UserEventServiceAsyncClient",
    "CatalogItem",
    "Image",
    "ProductCatalogItem",
    "CreateCatalogItemRequest",
    "DeleteCatalogItemRequest",
    "GetCatalogItemRequest",
    "ListCatalogItemsRequest",
    "ListCatalogItemsResponse",
    "UpdateCatalogItemRequest",
    "FeatureMap",
    "CatalogInlineSource",
    "GcsSource",
    "ImportCatalogItemsRequest",
    "ImportCatalogItemsResponse",
    "ImportErrorsConfig",
    "ImportMetadata",
    "ImportUserEventsRequest",
    "ImportUserEventsResponse",
    "InputConfig",
    "UserEventImportSummary",
    "UserEventInlineSource",
    "CreatePredictionApiKeyRegistrationRequest",
    "DeletePredictionApiKeyRegistrationRequest",
    "ListPredictionApiKeyRegistrationsRequest",
    "ListPredictionApiKeyRegistrationsResponse",
    "PredictionApiKeyRegistration",
    "PredictRequest",
    "PredictResponse",
    "EventDetail",
    "ProductDetail",
    "ProductEventDetail",
    "PurchaseTransaction",
    "UserEvent",
    "UserInfo",
    "CollectUserEventRequest",
    "ListUserEventsRequest",
    "ListUserEventsResponse",
    "PurgeUserEventsMetadata",
    "PurgeUserEventsRequest",
    "PurgeUserEventsResponse",
    "WriteUserEventRequest",
)
