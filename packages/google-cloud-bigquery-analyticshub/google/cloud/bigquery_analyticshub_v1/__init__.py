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

from google.cloud.bigquery_analyticshub_v1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.bigquery_analyticshub_v1.services.analytics_hub_service",
    "google.cloud.bigquery_analyticshub_v1.types.analyticshub",
    "google.cloud.bigquery_analyticshub_v1.types.pubsub",
}


from .services.analytics_hub_service import (
    AnalyticsHubServiceAsyncClient,
    AnalyticsHubServiceClient,
)
from .types.analyticshub import (
    ApproveQueryTemplateRequest,
    CreateDataExchangeRequest,
    CreateListingRequest,
    CreateQueryTemplateRequest,
    DataExchange,
    DataProvider,
    DeleteDataExchangeRequest,
    DeleteListingRequest,
    DeleteQueryTemplateRequest,
    DeleteSubscriptionRequest,
    DestinationDataset,
    DestinationDatasetReference,
    DestinationPubSubSubscription,
    DiscoveryType,
    GetDataExchangeRequest,
    GetListingRequest,
    GetQueryTemplateRequest,
    GetSubscriptionRequest,
    ListDataExchangesRequest,
    ListDataExchangesResponse,
    Listing,
    ListListingsRequest,
    ListListingsResponse,
    ListOrgDataExchangesRequest,
    ListOrgDataExchangesResponse,
    ListQueryTemplatesRequest,
    ListQueryTemplatesResponse,
    ListSharedResourceSubscriptionsRequest,
    ListSharedResourceSubscriptionsResponse,
    ListSubscriptionsRequest,
    ListSubscriptionsResponse,
    OperationMetadata,
    Publisher,
    QueryTemplate,
    RefreshSubscriptionRequest,
    RefreshSubscriptionResponse,
    RevokeSubscriptionRequest,
    RevokeSubscriptionResponse,
    Routine,
    SharedResourceType,
    SharingEnvironmentConfig,
    StoredProcedureConfig,
    SubmitQueryTemplateRequest,
    SubscribeDataExchangeRequest,
    SubscribeDataExchangeResponse,
    SubscribeListingRequest,
    SubscribeListingResponse,
    Subscription,
    UpdateDataExchangeRequest,
    UpdateListingRequest,
    UpdateQueryTemplateRequest,
)
from .types.pubsub import (
    BigQueryConfig,
    CloudStorageConfig,
    DeadLetterPolicy,
    ExpirationPolicy,
    JavaScriptUDF,
    MessageTransform,
    PubSubSubscription,
    PushConfig,
    RetryPolicy,
)

__all__ = (
    "AnalyticsHubServiceAsyncClient",
    "AnalyticsHubServiceClient",
    "ApproveQueryTemplateRequest",
    "BigQueryConfig",
    "CloudStorageConfig",
    "CreateDataExchangeRequest",
    "CreateListingRequest",
    "CreateQueryTemplateRequest",
    "DataExchange",
    "DataProvider",
    "DeadLetterPolicy",
    "DeleteDataExchangeRequest",
    "DeleteListingRequest",
    "DeleteQueryTemplateRequest",
    "DeleteSubscriptionRequest",
    "DestinationDataset",
    "DestinationDatasetReference",
    "DestinationPubSubSubscription",
    "DiscoveryType",
    "ExpirationPolicy",
    "GetDataExchangeRequest",
    "GetListingRequest",
    "GetQueryTemplateRequest",
    "GetSubscriptionRequest",
    "JavaScriptUDF",
    "ListDataExchangesRequest",
    "ListDataExchangesResponse",
    "ListListingsRequest",
    "ListListingsResponse",
    "ListOrgDataExchangesRequest",
    "ListOrgDataExchangesResponse",
    "ListQueryTemplatesRequest",
    "ListQueryTemplatesResponse",
    "ListSharedResourceSubscriptionsRequest",
    "ListSharedResourceSubscriptionsResponse",
    "ListSubscriptionsRequest",
    "ListSubscriptionsResponse",
    "Listing",
    "MessageTransform",
    "OperationMetadata",
    "PubSubSubscription",
    "Publisher",
    "PushConfig",
    "QueryTemplate",
    "RefreshSubscriptionRequest",
    "RefreshSubscriptionResponse",
    "RetryPolicy",
    "RevokeSubscriptionRequest",
    "RevokeSubscriptionResponse",
    "Routine",
    "SharedResourceType",
    "SharingEnvironmentConfig",
    "StoredProcedureConfig",
    "SubmitQueryTemplateRequest",
    "SubscribeDataExchangeRequest",
    "SubscribeDataExchangeResponse",
    "SubscribeListingRequest",
    "SubscribeListingResponse",
    "Subscription",
    "UpdateDataExchangeRequest",
    "UpdateListingRequest",
    "UpdateQueryTemplateRequest",
)

api_core.check_python_version("google.cloud.bigquery_analyticshub_v1")
api_core.check_dependency_versions("google.cloud.bigquery_analyticshub_v1")
