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
from google.cloud.retail import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.retail_v2.services.analytics_service.async_client import (
    AnalyticsServiceAsyncClient,
)
from google.cloud.retail_v2.services.analytics_service.client import (
    AnalyticsServiceClient,
)
from google.cloud.retail_v2.services.catalog_service.async_client import (
    CatalogServiceAsyncClient,
)
from google.cloud.retail_v2.services.catalog_service.client import CatalogServiceClient
from google.cloud.retail_v2.services.completion_service.async_client import (
    CompletionServiceAsyncClient,
)
from google.cloud.retail_v2.services.completion_service.client import (
    CompletionServiceClient,
)
from google.cloud.retail_v2.services.control_service.async_client import (
    ControlServiceAsyncClient,
)
from google.cloud.retail_v2.services.control_service.client import ControlServiceClient
from google.cloud.retail_v2.services.conversational_search_service.async_client import (
    ConversationalSearchServiceAsyncClient,
)
from google.cloud.retail_v2.services.conversational_search_service.client import (
    ConversationalSearchServiceClient,
)
from google.cloud.retail_v2.services.generative_question_service.async_client import (
    GenerativeQuestionServiceAsyncClient,
)
from google.cloud.retail_v2.services.generative_question_service.client import (
    GenerativeQuestionServiceClient,
)
from google.cloud.retail_v2.services.model_service.async_client import (
    ModelServiceAsyncClient,
)
from google.cloud.retail_v2.services.model_service.client import ModelServiceClient
from google.cloud.retail_v2.services.prediction_service.async_client import (
    PredictionServiceAsyncClient,
)
from google.cloud.retail_v2.services.prediction_service.client import (
    PredictionServiceClient,
)
from google.cloud.retail_v2.services.product_service.async_client import (
    ProductServiceAsyncClient,
)
from google.cloud.retail_v2.services.product_service.client import ProductServiceClient
from google.cloud.retail_v2.services.search_service.async_client import (
    SearchServiceAsyncClient,
)
from google.cloud.retail_v2.services.search_service.client import SearchServiceClient
from google.cloud.retail_v2.services.serving_config_service.async_client import (
    ServingConfigServiceAsyncClient,
)
from google.cloud.retail_v2.services.serving_config_service.client import (
    ServingConfigServiceClient,
)
from google.cloud.retail_v2.services.user_event_service.async_client import (
    UserEventServiceAsyncClient,
)
from google.cloud.retail_v2.services.user_event_service.client import (
    UserEventServiceClient,
)
from google.cloud.retail_v2.types.catalog import (
    AttributesConfig,
    Catalog,
    CatalogAttribute,
    CompletionConfig,
    ProductLevelConfig,
)
from google.cloud.retail_v2.types.catalog_service import (
    AddCatalogAttributeRequest,
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
from google.cloud.retail_v2.types.common import (
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
from google.cloud.retail_v2.types.completion_service import (
    CompleteQueryRequest,
    CompleteQueryResponse,
)
from google.cloud.retail_v2.types.control import Control
from google.cloud.retail_v2.types.control_service import (
    CreateControlRequest,
    DeleteControlRequest,
    GetControlRequest,
    ListControlsRequest,
    ListControlsResponse,
    UpdateControlRequest,
)
from google.cloud.retail_v2.types.conversational_search_service import (
    ConversationalSearchRequest,
    ConversationalSearchResponse,
)
from google.cloud.retail_v2.types.export_config import (
    BigQueryOutputResult,
    ExportAnalyticsMetricsRequest,
    ExportAnalyticsMetricsResponse,
    ExportErrorsConfig,
    ExportMetadata,
    GcsOutputResult,
    OutputConfig,
    OutputResult,
)
from google.cloud.retail_v2.types.generative_question import (
    GenerativeQuestionConfig,
    GenerativeQuestionsFeatureConfig,
)
from google.cloud.retail_v2.types.generative_question_service import (
    BatchUpdateGenerativeQuestionConfigsRequest,
    BatchUpdateGenerativeQuestionConfigsResponse,
    GetGenerativeQuestionsFeatureConfigRequest,
    ListGenerativeQuestionConfigsRequest,
    ListGenerativeQuestionConfigsResponse,
    UpdateGenerativeQuestionConfigRequest,
    UpdateGenerativeQuestionsFeatureConfigRequest,
)
from google.cloud.retail_v2.types.import_config import (
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
from google.cloud.retail_v2.types.model import Model
from google.cloud.retail_v2.types.model_service import (
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
from google.cloud.retail_v2.types.prediction_service import (
    PredictRequest,
    PredictResponse,
)
from google.cloud.retail_v2.types.product import Product
from google.cloud.retail_v2.types.product_service import (
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
from google.cloud.retail_v2.types.promotion import Promotion
from google.cloud.retail_v2.types.purge_config import (
    PurgeMetadata,
    PurgeProductsMetadata,
    PurgeProductsRequest,
    PurgeProductsResponse,
    PurgeUserEventsRequest,
    PurgeUserEventsResponse,
)
from google.cloud.retail_v2.types.safety import HarmCategory, SafetySetting
from google.cloud.retail_v2.types.search_service import (
    ExperimentInfo,
    ProductAttributeInterval,
    ProductAttributeValue,
    SearchRequest,
    SearchResponse,
    Tile,
)
from google.cloud.retail_v2.types.serving_config import ServingConfig
from google.cloud.retail_v2.types.serving_config_service import (
    AddControlRequest,
    CreateServingConfigRequest,
    DeleteServingConfigRequest,
    GetServingConfigRequest,
    ListServingConfigsRequest,
    ListServingConfigsResponse,
    RemoveControlRequest,
    UpdateServingConfigRequest,
)
from google.cloud.retail_v2.types.user_event import (
    CompletionDetail,
    ProductDetail,
    PurchaseTransaction,
    UserEvent,
)
from google.cloud.retail_v2.types.user_event_service import (
    CollectUserEventRequest,
    RejoinUserEventsMetadata,
    RejoinUserEventsRequest,
    RejoinUserEventsResponse,
    WriteUserEventRequest,
)

__all__ = (
    "AnalyticsServiceClient",
    "AnalyticsServiceAsyncClient",
    "CatalogServiceClient",
    "CatalogServiceAsyncClient",
    "CompletionServiceClient",
    "CompletionServiceAsyncClient",
    "ControlServiceClient",
    "ControlServiceAsyncClient",
    "ConversationalSearchServiceClient",
    "ConversationalSearchServiceAsyncClient",
    "GenerativeQuestionServiceClient",
    "GenerativeQuestionServiceAsyncClient",
    "ModelServiceClient",
    "ModelServiceAsyncClient",
    "PredictionServiceClient",
    "PredictionServiceAsyncClient",
    "ProductServiceClient",
    "ProductServiceAsyncClient",
    "SearchServiceClient",
    "SearchServiceAsyncClient",
    "ServingConfigServiceClient",
    "ServingConfigServiceAsyncClient",
    "UserEventServiceClient",
    "UserEventServiceAsyncClient",
    "AttributesConfig",
    "Catalog",
    "CatalogAttribute",
    "CompletionConfig",
    "ProductLevelConfig",
    "AddCatalogAttributeRequest",
    "GetAttributesConfigRequest",
    "GetCompletionConfigRequest",
    "GetDefaultBranchRequest",
    "GetDefaultBranchResponse",
    "ListCatalogsRequest",
    "ListCatalogsResponse",
    "RemoveCatalogAttributeRequest",
    "ReplaceCatalogAttributeRequest",
    "SetDefaultBranchRequest",
    "UpdateAttributesConfigRequest",
    "UpdateCatalogRequest",
    "UpdateCompletionConfigRequest",
    "Audience",
    "ColorInfo",
    "Condition",
    "CustomAttribute",
    "DoubleList",
    "FulfillmentInfo",
    "Image",
    "Interval",
    "LocalInventory",
    "PinControlMetadata",
    "PriceInfo",
    "Rating",
    "Rule",
    "StringList",
    "UserInfo",
    "AttributeConfigLevel",
    "RecommendationsFilteringOption",
    "SearchSolutionUseCase",
    "SolutionType",
    "CompleteQueryRequest",
    "CompleteQueryResponse",
    "Control",
    "CreateControlRequest",
    "DeleteControlRequest",
    "GetControlRequest",
    "ListControlsRequest",
    "ListControlsResponse",
    "UpdateControlRequest",
    "ConversationalSearchRequest",
    "ConversationalSearchResponse",
    "BigQueryOutputResult",
    "ExportAnalyticsMetricsRequest",
    "ExportAnalyticsMetricsResponse",
    "ExportErrorsConfig",
    "ExportMetadata",
    "GcsOutputResult",
    "OutputConfig",
    "OutputResult",
    "GenerativeQuestionConfig",
    "GenerativeQuestionsFeatureConfig",
    "BatchUpdateGenerativeQuestionConfigsRequest",
    "BatchUpdateGenerativeQuestionConfigsResponse",
    "GetGenerativeQuestionsFeatureConfigRequest",
    "ListGenerativeQuestionConfigsRequest",
    "ListGenerativeQuestionConfigsResponse",
    "UpdateGenerativeQuestionConfigRequest",
    "UpdateGenerativeQuestionsFeatureConfigRequest",
    "BigQuerySource",
    "CompletionDataInputConfig",
    "GcsSource",
    "ImportCompletionDataRequest",
    "ImportCompletionDataResponse",
    "ImportErrorsConfig",
    "ImportMetadata",
    "ImportProductsRequest",
    "ImportProductsResponse",
    "ImportUserEventsRequest",
    "ImportUserEventsResponse",
    "ProductInlineSource",
    "ProductInputConfig",
    "UserEventImportSummary",
    "UserEventInlineSource",
    "UserEventInputConfig",
    "Model",
    "CreateModelMetadata",
    "CreateModelRequest",
    "DeleteModelRequest",
    "GetModelRequest",
    "ListModelsRequest",
    "ListModelsResponse",
    "PauseModelRequest",
    "ResumeModelRequest",
    "TuneModelMetadata",
    "TuneModelRequest",
    "TuneModelResponse",
    "UpdateModelRequest",
    "PredictRequest",
    "PredictResponse",
    "Product",
    "AddFulfillmentPlacesMetadata",
    "AddFulfillmentPlacesRequest",
    "AddFulfillmentPlacesResponse",
    "AddLocalInventoriesMetadata",
    "AddLocalInventoriesRequest",
    "AddLocalInventoriesResponse",
    "CreateProductRequest",
    "DeleteProductRequest",
    "GetProductRequest",
    "ListProductsRequest",
    "ListProductsResponse",
    "RemoveFulfillmentPlacesMetadata",
    "RemoveFulfillmentPlacesRequest",
    "RemoveFulfillmentPlacesResponse",
    "RemoveLocalInventoriesMetadata",
    "RemoveLocalInventoriesRequest",
    "RemoveLocalInventoriesResponse",
    "SetInventoryMetadata",
    "SetInventoryRequest",
    "SetInventoryResponse",
    "UpdateProductRequest",
    "Promotion",
    "PurgeMetadata",
    "PurgeProductsMetadata",
    "PurgeProductsRequest",
    "PurgeProductsResponse",
    "PurgeUserEventsRequest",
    "PurgeUserEventsResponse",
    "SafetySetting",
    "HarmCategory",
    "ExperimentInfo",
    "ProductAttributeInterval",
    "ProductAttributeValue",
    "SearchRequest",
    "SearchResponse",
    "Tile",
    "ServingConfig",
    "AddControlRequest",
    "CreateServingConfigRequest",
    "DeleteServingConfigRequest",
    "GetServingConfigRequest",
    "ListServingConfigsRequest",
    "ListServingConfigsResponse",
    "RemoveControlRequest",
    "UpdateServingConfigRequest",
    "CompletionDetail",
    "ProductDetail",
    "PurchaseTransaction",
    "UserEvent",
    "CollectUserEventRequest",
    "RejoinUserEventsMetadata",
    "RejoinUserEventsRequest",
    "RejoinUserEventsResponse",
    "WriteUserEventRequest",
)
