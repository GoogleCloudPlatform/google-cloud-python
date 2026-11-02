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

from google.cloud.retail_v2beta import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.retail_v2beta.services.analytics_service",
    "google.cloud.retail_v2beta.services.catalog_service",
    "google.cloud.retail_v2beta.services.completion_service",
    "google.cloud.retail_v2beta.services.control_service",
    "google.cloud.retail_v2beta.services.conversational_search_service",
    "google.cloud.retail_v2beta.services.generative_question_service",
    "google.cloud.retail_v2beta.services.model_service",
    "google.cloud.retail_v2beta.services.prediction_service",
    "google.cloud.retail_v2beta.services.product_service",
    "google.cloud.retail_v2beta.services.project_service",
    "google.cloud.retail_v2beta.services.search_service",
    "google.cloud.retail_v2beta.services.serving_config_service",
    "google.cloud.retail_v2beta.services.user_event_service",
    "google.cloud.retail_v2beta.types.analytics_service",
    "google.cloud.retail_v2beta.types.catalog",
    "google.cloud.retail_v2beta.types.catalog_service",
    "google.cloud.retail_v2beta.types.common",
    "google.cloud.retail_v2beta.types.completion_service",
    "google.cloud.retail_v2beta.types.control",
    "google.cloud.retail_v2beta.types.control_service",
    "google.cloud.retail_v2beta.types.conversational_search_service",
    "google.cloud.retail_v2beta.types.export_config",
    "google.cloud.retail_v2beta.types.generative_question",
    "google.cloud.retail_v2beta.types.generative_question_service",
    "google.cloud.retail_v2beta.types.import_config",
    "google.cloud.retail_v2beta.types.model",
    "google.cloud.retail_v2beta.types.model_service",
    "google.cloud.retail_v2beta.types.prediction_service",
    "google.cloud.retail_v2beta.types.product",
    "google.cloud.retail_v2beta.types.product_service",
    "google.cloud.retail_v2beta.types.project",
    "google.cloud.retail_v2beta.types.project_service",
    "google.cloud.retail_v2beta.types.promotion",
    "google.cloud.retail_v2beta.types.purge_config",
    "google.cloud.retail_v2beta.types.safety",
    "google.cloud.retail_v2beta.types.search_service",
    "google.cloud.retail_v2beta.types.serving_config",
    "google.cloud.retail_v2beta.types.serving_config_service",
    "google.cloud.retail_v2beta.types.user_event",
    "google.cloud.retail_v2beta.types.user_event_service",
}


from .services.analytics_service import (
    AnalyticsServiceAsyncClient,
    AnalyticsServiceClient,
)
from .services.catalog_service import CatalogServiceAsyncClient, CatalogServiceClient
from .services.completion_service import (
    CompletionServiceAsyncClient,
    CompletionServiceClient,
)
from .services.control_service import ControlServiceAsyncClient, ControlServiceClient
from .services.conversational_search_service import (
    ConversationalSearchServiceAsyncClient,
    ConversationalSearchServiceClient,
)
from .services.generative_question_service import (
    GenerativeQuestionServiceAsyncClient,
    GenerativeQuestionServiceClient,
)
from .services.model_service import ModelServiceAsyncClient, ModelServiceClient
from .services.prediction_service import (
    PredictionServiceAsyncClient,
    PredictionServiceClient,
)
from .services.product_service import ProductServiceAsyncClient, ProductServiceClient
from .services.project_service import ProjectServiceAsyncClient, ProjectServiceClient
from .services.search_service import SearchServiceAsyncClient, SearchServiceClient
from .services.serving_config_service import (
    ServingConfigServiceAsyncClient,
    ServingConfigServiceClient,
)
from .services.user_event_service import (
    UserEventServiceAsyncClient,
    UserEventServiceClient,
)
from .types.catalog import (
    AttributesConfig,
    Catalog,
    CatalogAttribute,
    CompletionConfig,
    MerchantCenterFeedFilter,
    MerchantCenterLink,
    MerchantCenterLinkingConfig,
    ProductLevelConfig,
)
from .types.catalog_service import (
    AddCatalogAttributeRequest,
    BatchRemoveCatalogAttributesRequest,
    BatchRemoveCatalogAttributesResponse,
    GetAttributesConfigRequest,
    GetCompletionConfigRequest,
    GetDefaultBranchRequest,
    GetDefaultBranchResponse,
    ListCatalogsRequest,
    ListCatalogsResponse,
    RemoveCatalogAttributeRequest,
    ReplaceCatalogAttributeRequest,
    SetDefaultBranchRequest,
    UpdateAttributesConfigRequest,
    UpdateCatalogRequest,
    UpdateCompletionConfigRequest,
)
from .types.common import (
    AttributeConfigLevel,
    Audience,
    ColorInfo,
    Condition,
    CustomAttribute,
    DoubleList,
    FulfillmentInfo,
    Image,
    Interval,
    LocalInventory,
    PinControlMetadata,
    PriceInfo,
    Rating,
    RecommendationsFilteringOption,
    Rule,
    SearchSolutionUseCase,
    SolutionType,
    StringList,
    UserInfo,
)
from .types.completion_service import CompleteQueryRequest, CompleteQueryResponse
from .types.control import Control
from .types.control_service import (
    CreateControlRequest,
    DeleteControlRequest,
    GetControlRequest,
    ListControlsRequest,
    ListControlsResponse,
    UpdateControlRequest,
)
from .types.conversational_search_service import (
    ConversationalSearchRequest,
    ConversationalSearchResponse,
)
from .types.export_config import (
    BigQueryOutputResult,
    ExportAnalyticsMetricsRequest,
    ExportAnalyticsMetricsResponse,
    ExportErrorsConfig,
    ExportMetadata,
    ExportProductsRequest,
    ExportProductsResponse,
    ExportUserEventsRequest,
    ExportUserEventsResponse,
    GcsOutputResult,
    OutputConfig,
    OutputResult,
)
from .types.generative_question import (
    GenerativeQuestionConfig,
    GenerativeQuestionsFeatureConfig,
)
from .types.generative_question_service import (
    BatchUpdateGenerativeQuestionConfigsRequest,
    BatchUpdateGenerativeQuestionConfigsResponse,
    GetGenerativeQuestionsFeatureConfigRequest,
    ListGenerativeQuestionConfigsRequest,
    ListGenerativeQuestionConfigsResponse,
    UpdateGenerativeQuestionConfigRequest,
    UpdateGenerativeQuestionsFeatureConfigRequest,
)
from .types.import_config import (
    BigQuerySource,
    CompletionDataInputConfig,
    GcsSource,
    ImportCompletionDataRequest,
    ImportCompletionDataResponse,
    ImportErrorsConfig,
    ImportMetadata,
    ImportProductsRequest,
    ImportProductsResponse,
    ImportUserEventsRequest,
    ImportUserEventsResponse,
    ProductInlineSource,
    ProductInputConfig,
    UserEventImportSummary,
    UserEventInlineSource,
    UserEventInputConfig,
)
from .types.model import Model
from .types.model_service import (
    CreateModelMetadata,
    CreateModelRequest,
    DeleteModelRequest,
    GetModelRequest,
    ListModelsRequest,
    ListModelsResponse,
    PauseModelRequest,
    ResumeModelRequest,
    TuneModelMetadata,
    TuneModelRequest,
    TuneModelResponse,
    UpdateModelRequest,
)
from .types.prediction_service import PredictRequest, PredictResponse
from .types.product import Product
from .types.product_service import (
    AddFulfillmentPlacesMetadata,
    AddFulfillmentPlacesRequest,
    AddFulfillmentPlacesResponse,
    AddLocalInventoriesMetadata,
    AddLocalInventoriesRequest,
    AddLocalInventoriesResponse,
    CreateProductRequest,
    DeleteProductRequest,
    GetProductRequest,
    ListProductsRequest,
    ListProductsResponse,
    RemoveFulfillmentPlacesMetadata,
    RemoveFulfillmentPlacesRequest,
    RemoveFulfillmentPlacesResponse,
    RemoveLocalInventoriesMetadata,
    RemoveLocalInventoriesRequest,
    RemoveLocalInventoriesResponse,
    SetInventoryMetadata,
    SetInventoryRequest,
    SetInventoryResponse,
    UpdateProductRequest,
)
from .types.project import AlertConfig
from .types.project_service import GetAlertConfigRequest, UpdateAlertConfigRequest
from .types.promotion import Promotion
from .types.purge_config import (
    PurgeMetadata,
    PurgeProductsMetadata,
    PurgeProductsRequest,
    PurgeProductsResponse,
    PurgeUserEventsRequest,
    PurgeUserEventsResponse,
)
from .types.safety import HarmCategory, SafetySetting
from .types.search_service import (
    ExperimentInfo,
    ProductAttributeInterval,
    ProductAttributeValue,
    SearchRequest,
    SearchResponse,
    Tile,
)
from .types.serving_config import ServingConfig
from .types.serving_config_service import (
    AddControlRequest,
    CreateServingConfigRequest,
    DeleteServingConfigRequest,
    GetServingConfigRequest,
    ListServingConfigsRequest,
    ListServingConfigsResponse,
    RemoveControlRequest,
    UpdateServingConfigRequest,
)
from .types.user_event import (
    CompletionDetail,
    ProductDetail,
    PurchaseTransaction,
    UserEvent,
)
from .types.user_event_service import (
    CollectUserEventRequest,
    RejoinUserEventsMetadata,
    RejoinUserEventsRequest,
    RejoinUserEventsResponse,
    WriteUserEventRequest,
)

__all__ = (
    "AnalyticsServiceAsyncClient",
    "CatalogServiceAsyncClient",
    "CompletionServiceAsyncClient",
    "ControlServiceAsyncClient",
    "ConversationalSearchServiceAsyncClient",
    "GenerativeQuestionServiceAsyncClient",
    "ModelServiceAsyncClient",
    "PredictionServiceAsyncClient",
    "ProductServiceAsyncClient",
    "ProjectServiceAsyncClient",
    "SearchServiceAsyncClient",
    "ServingConfigServiceAsyncClient",
    "UserEventServiceAsyncClient",
    "AddCatalogAttributeRequest",
    "AddControlRequest",
    "AddFulfillmentPlacesMetadata",
    "AddFulfillmentPlacesRequest",
    "AddFulfillmentPlacesResponse",
    "AddLocalInventoriesMetadata",
    "AddLocalInventoriesRequest",
    "AddLocalInventoriesResponse",
    "AlertConfig",
    "AnalyticsServiceClient",
    "AttributeConfigLevel",
    "AttributesConfig",
    "Audience",
    "BatchRemoveCatalogAttributesRequest",
    "BatchRemoveCatalogAttributesResponse",
    "BatchUpdateGenerativeQuestionConfigsRequest",
    "BatchUpdateGenerativeQuestionConfigsResponse",
    "BigQueryOutputResult",
    "BigQuerySource",
    "Catalog",
    "CatalogAttribute",
    "CatalogServiceClient",
    "CollectUserEventRequest",
    "ColorInfo",
    "CompleteQueryRequest",
    "CompleteQueryResponse",
    "CompletionConfig",
    "CompletionDataInputConfig",
    "CompletionDetail",
    "CompletionServiceClient",
    "Condition",
    "Control",
    "ControlServiceClient",
    "ConversationalSearchRequest",
    "ConversationalSearchResponse",
    "ConversationalSearchServiceClient",
    "CreateControlRequest",
    "CreateModelMetadata",
    "CreateModelRequest",
    "CreateProductRequest",
    "CreateServingConfigRequest",
    "CustomAttribute",
    "DeleteControlRequest",
    "DeleteModelRequest",
    "DeleteProductRequest",
    "DeleteServingConfigRequest",
    "DoubleList",
    "ExperimentInfo",
    "ExportAnalyticsMetricsRequest",
    "ExportAnalyticsMetricsResponse",
    "ExportErrorsConfig",
    "ExportMetadata",
    "ExportProductsRequest",
    "ExportProductsResponse",
    "ExportUserEventsRequest",
    "ExportUserEventsResponse",
    "FulfillmentInfo",
    "GcsOutputResult",
    "GcsSource",
    "GenerativeQuestionConfig",
    "GenerativeQuestionServiceClient",
    "GenerativeQuestionsFeatureConfig",
    "GetAlertConfigRequest",
    "GetAttributesConfigRequest",
    "GetCompletionConfigRequest",
    "GetControlRequest",
    "GetDefaultBranchRequest",
    "GetDefaultBranchResponse",
    "GetGenerativeQuestionsFeatureConfigRequest",
    "GetModelRequest",
    "GetProductRequest",
    "GetServingConfigRequest",
    "HarmCategory",
    "Image",
    "ImportCompletionDataRequest",
    "ImportCompletionDataResponse",
    "ImportErrorsConfig",
    "ImportMetadata",
    "ImportProductsRequest",
    "ImportProductsResponse",
    "ImportUserEventsRequest",
    "ImportUserEventsResponse",
    "Interval",
    "ListCatalogsRequest",
    "ListCatalogsResponse",
    "ListControlsRequest",
    "ListControlsResponse",
    "ListGenerativeQuestionConfigsRequest",
    "ListGenerativeQuestionConfigsResponse",
    "ListModelsRequest",
    "ListModelsResponse",
    "ListProductsRequest",
    "ListProductsResponse",
    "ListServingConfigsRequest",
    "ListServingConfigsResponse",
    "LocalInventory",
    "MerchantCenterFeedFilter",
    "MerchantCenterLink",
    "MerchantCenterLinkingConfig",
    "Model",
    "ModelServiceClient",
    "OutputConfig",
    "OutputResult",
    "PauseModelRequest",
    "PinControlMetadata",
    "PredictRequest",
    "PredictResponse",
    "PredictionServiceClient",
    "PriceInfo",
    "Product",
    "ProductAttributeInterval",
    "ProductAttributeValue",
    "ProductDetail",
    "ProductInlineSource",
    "ProductInputConfig",
    "ProductLevelConfig",
    "ProductServiceClient",
    "ProjectServiceClient",
    "Promotion",
    "PurchaseTransaction",
    "PurgeMetadata",
    "PurgeProductsMetadata",
    "PurgeProductsRequest",
    "PurgeProductsResponse",
    "PurgeUserEventsRequest",
    "PurgeUserEventsResponse",
    "Rating",
    "RecommendationsFilteringOption",
    "RejoinUserEventsMetadata",
    "RejoinUserEventsRequest",
    "RejoinUserEventsResponse",
    "RemoveCatalogAttributeRequest",
    "RemoveControlRequest",
    "RemoveFulfillmentPlacesMetadata",
    "RemoveFulfillmentPlacesRequest",
    "RemoveFulfillmentPlacesResponse",
    "RemoveLocalInventoriesMetadata",
    "RemoveLocalInventoriesRequest",
    "RemoveLocalInventoriesResponse",
    "ReplaceCatalogAttributeRequest",
    "ResumeModelRequest",
    "Rule",
    "SafetySetting",
    "SearchRequest",
    "SearchResponse",
    "SearchServiceClient",
    "SearchSolutionUseCase",
    "ServingConfig",
    "ServingConfigServiceClient",
    "SetDefaultBranchRequest",
    "SetInventoryMetadata",
    "SetInventoryRequest",
    "SetInventoryResponse",
    "SolutionType",
    "StringList",
    "Tile",
    "TuneModelMetadata",
    "TuneModelRequest",
    "TuneModelResponse",
    "UpdateAlertConfigRequest",
    "UpdateAttributesConfigRequest",
    "UpdateCatalogRequest",
    "UpdateCompletionConfigRequest",
    "UpdateControlRequest",
    "UpdateGenerativeQuestionConfigRequest",
    "UpdateGenerativeQuestionsFeatureConfigRequest",
    "UpdateModelRequest",
    "UpdateProductRequest",
    "UpdateServingConfigRequest",
    "UserEvent",
    "UserEventImportSummary",
    "UserEventInlineSource",
    "UserEventInputConfig",
    "UserEventServiceClient",
    "UserInfo",
    "WriteUserEventRequest",
)

api_core.check_python_version("google.cloud.retail_v2beta")
api_core.check_dependency_versions("google.cloud.retail_v2beta")
