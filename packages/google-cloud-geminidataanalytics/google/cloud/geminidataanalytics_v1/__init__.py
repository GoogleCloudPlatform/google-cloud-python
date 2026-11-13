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

from google.cloud.geminidataanalytics_v1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.geminidataanalytics_v1.services.data_agent_service",
    "google.cloud.geminidataanalytics_v1.services.data_chat_service",
    "google.cloud.geminidataanalytics_v1.types.context",
    "google.cloud.geminidataanalytics_v1.types.conversation",
    "google.cloud.geminidataanalytics_v1.types.credentials",
    "google.cloud.geminidataanalytics_v1.types.data_agent",
    "google.cloud.geminidataanalytics_v1.types.data_agent_service",
    "google.cloud.geminidataanalytics_v1.types.data_analytics_agent",
    "google.cloud.geminidataanalytics_v1.types.data_chat_service",
    "google.cloud.geminidataanalytics_v1.types.datasource",
}


from .services.data_agent_service import (
    DataAgentServiceAsyncClient,
    DataAgentServiceClient,
)
from .services.data_chat_service import (
    DataChatServiceAsyncClient,
    DataChatServiceClient,
)
from .types.context import (
    AnalysisOptions,
    BigQueryRoutine,
    BigQueryRoutineReference,
    Citation,
    CitationAnchor,
    CitationSource,
    Context,
    ConversationOptions,
    DatasourceOptions,
    DynamicField,
    ExampleQuery,
    GlossaryTerm,
    LookerGoldenQuery,
    LookerQuery,
    MatchedQuery,
    QueryParameter,
    QueryParameterValues,
    UserFunctions,
)
from .types.conversation import (
    Conversation,
    CreateConversationRequest,
    DeleteConversationRequest,
    GetConversationRequest,
    ListConversationsRequest,
    ListConversationsResponse,
    UpdateConversationRequest,
)
from .types.credentials import Credentials, OAuthCredentials
from .types.data_agent import DataAgent
from .types.data_agent_service import (
    CreateDataAgentRequest,
    DeleteDataAgentRequest,
    GetDataAgentRequest,
    ListAccessibleDataAgentsRequest,
    ListAccessibleDataAgentsResponse,
    ListDataAgentsRequest,
    ListDataAgentsResponse,
    OperationMetadata,
    RetrieveAgentOpsObservabilityRequest,
    RetrieveAgentOpsObservabilityResponse,
    SetAgentOpsObservabilityMetadata,
    SetAgentOpsObservabilityRequest,
    SetAgentOpsObservabilityResponse,
    UpdateDataAgentRequest,
)
from .types.data_analytics_agent import DataAnalyticsAgent
from .types.data_chat_service import (
    AnalysisEvent,
    AnalysisMessage,
    AnalysisQuery,
    BigQueryJob,
    Blob,
    ChartMessage,
    ChartQuery,
    ChartResult,
    ChatRequest,
    ClientManagedResourceContext,
    ConversationReference,
    DataAgentContext,
    DataMessage,
    DataQuery,
    DataResult,
    ErrorMessage,
    ExampleQueries,
    ListMessagesRequest,
    ListMessagesResponse,
    LookerSettings,
    Message,
    SchemaMessage,
    SchemaQuery,
    SchemaResult,
    StorageMessage,
    SystemMessage,
    TextMessage,
    UserMessage,
)
from .types.datasource import (
    BigQueryDatasetReference,
    BigQueryPropertyGraphReference,
    BigQueryTableReference,
    BigQueryTableReferences,
    DataFilter,
    DataFilterType,
    Datasource,
    DatasourceReferences,
    Field,
    LookerExploreReference,
    LookerExploreReferences,
    PrivateLookerInstanceInfo,
    Schema,
    SearchScope,
    StudioDatasourceReference,
    StudioDatasourceReferences,
)

__all__ = (
    "DataAgentServiceAsyncClient",
    "DataChatServiceAsyncClient",
    "AnalysisEvent",
    "AnalysisMessage",
    "AnalysisOptions",
    "AnalysisQuery",
    "BigQueryDatasetReference",
    "BigQueryJob",
    "BigQueryPropertyGraphReference",
    "BigQueryRoutine",
    "BigQueryRoutineReference",
    "BigQueryTableReference",
    "BigQueryTableReferences",
    "Blob",
    "ChartMessage",
    "ChartQuery",
    "ChartResult",
    "ChatRequest",
    "Citation",
    "CitationAnchor",
    "CitationSource",
    "ClientManagedResourceContext",
    "Context",
    "Conversation",
    "ConversationOptions",
    "ConversationReference",
    "CreateConversationRequest",
    "CreateDataAgentRequest",
    "Credentials",
    "DataAgent",
    "DataAgentContext",
    "DataAgentServiceClient",
    "DataAnalyticsAgent",
    "DataChatServiceClient",
    "DataFilter",
    "DataFilterType",
    "DataMessage",
    "DataQuery",
    "DataResult",
    "Datasource",
    "DatasourceOptions",
    "DatasourceReferences",
    "DeleteConversationRequest",
    "DeleteDataAgentRequest",
    "DynamicField",
    "ErrorMessage",
    "ExampleQueries",
    "ExampleQuery",
    "Field",
    "GetConversationRequest",
    "GetDataAgentRequest",
    "GlossaryTerm",
    "ListAccessibleDataAgentsRequest",
    "ListAccessibleDataAgentsResponse",
    "ListConversationsRequest",
    "ListConversationsResponse",
    "ListDataAgentsRequest",
    "ListDataAgentsResponse",
    "ListMessagesRequest",
    "ListMessagesResponse",
    "LookerExploreReference",
    "LookerExploreReferences",
    "LookerGoldenQuery",
    "LookerQuery",
    "LookerSettings",
    "MatchedQuery",
    "Message",
    "OAuthCredentials",
    "OperationMetadata",
    "PrivateLookerInstanceInfo",
    "QueryParameter",
    "QueryParameterValues",
    "RetrieveAgentOpsObservabilityRequest",
    "RetrieveAgentOpsObservabilityResponse",
    "Schema",
    "SchemaMessage",
    "SchemaQuery",
    "SchemaResult",
    "SearchScope",
    "SetAgentOpsObservabilityMetadata",
    "SetAgentOpsObservabilityRequest",
    "SetAgentOpsObservabilityResponse",
    "StorageMessage",
    "StudioDatasourceReference",
    "StudioDatasourceReferences",
    "SystemMessage",
    "TextMessage",
    "UpdateConversationRequest",
    "UpdateDataAgentRequest",
    "UserFunctions",
    "UserMessage",
)

api_core.check_python_version("google.cloud.geminidataanalytics_v1")
api_core.check_dependency_versions("google.cloud.geminidataanalytics_v1")
