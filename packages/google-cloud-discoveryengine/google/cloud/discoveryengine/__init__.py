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
from google.cloud.discoveryengine import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.discoveryengine_v1beta.services.acl_config_service.async_client import (
    AclConfigServiceAsyncClient,
)
from google.cloud.discoveryengine_v1beta.services.acl_config_service.client import (
    AclConfigServiceClient,
)
from google.cloud.discoveryengine_v1beta.services.assistant_service.async_client import (
    AssistantServiceAsyncClient,
)
from google.cloud.discoveryengine_v1beta.services.assistant_service.client import (
    AssistantServiceClient,
)
from google.cloud.discoveryengine_v1beta.services.cmek_config_service.async_client import (
    CmekConfigServiceAsyncClient,
)
from google.cloud.discoveryengine_v1beta.services.cmek_config_service.client import (
    CmekConfigServiceClient,
)
from google.cloud.discoveryengine_v1beta.services.completion_service.async_client import (
    CompletionServiceAsyncClient,
)
from google.cloud.discoveryengine_v1beta.services.completion_service.client import (
    CompletionServiceClient,
)
from google.cloud.discoveryengine_v1beta.services.control_service.async_client import (
    ControlServiceAsyncClient,
)
from google.cloud.discoveryengine_v1beta.services.control_service.client import (
    ControlServiceClient,
)
from google.cloud.discoveryengine_v1beta.services.conversational_search_service.async_client import (
    ConversationalSearchServiceAsyncClient,
)
from google.cloud.discoveryengine_v1beta.services.conversational_search_service.client import (
    ConversationalSearchServiceClient,
)
from google.cloud.discoveryengine_v1beta.services.data_store_service.async_client import (
    DataStoreServiceAsyncClient,
)
from google.cloud.discoveryengine_v1beta.services.data_store_service.client import (
    DataStoreServiceClient,
)
from google.cloud.discoveryengine_v1beta.services.document_service.async_client import (
    DocumentServiceAsyncClient,
)
from google.cloud.discoveryengine_v1beta.services.document_service.client import (
    DocumentServiceClient,
)
from google.cloud.discoveryengine_v1beta.services.engine_service.async_client import (
    EngineServiceAsyncClient,
)
from google.cloud.discoveryengine_v1beta.services.engine_service.client import (
    EngineServiceClient,
)
from google.cloud.discoveryengine_v1beta.services.evaluation_service.async_client import (
    EvaluationServiceAsyncClient,
)
from google.cloud.discoveryengine_v1beta.services.evaluation_service.client import (
    EvaluationServiceClient,
)
from google.cloud.discoveryengine_v1beta.services.grounded_generation_service.async_client import (
    GroundedGenerationServiceAsyncClient,
)
from google.cloud.discoveryengine_v1beta.services.grounded_generation_service.client import (
    GroundedGenerationServiceClient,
)
from google.cloud.discoveryengine_v1beta.services.identity_mapping_store_service.async_client import (
    IdentityMappingStoreServiceAsyncClient,
)
from google.cloud.discoveryengine_v1beta.services.identity_mapping_store_service.client import (
    IdentityMappingStoreServiceClient,
)
from google.cloud.discoveryengine_v1beta.services.license_config_service.async_client import (
    LicenseConfigServiceAsyncClient,
)
from google.cloud.discoveryengine_v1beta.services.license_config_service.client import (
    LicenseConfigServiceClient,
)
from google.cloud.discoveryengine_v1beta.services.project_service.async_client import (
    ProjectServiceAsyncClient,
)
from google.cloud.discoveryengine_v1beta.services.project_service.client import (
    ProjectServiceClient,
)
from google.cloud.discoveryengine_v1beta.services.rank_service.async_client import (
    RankServiceAsyncClient,
)
from google.cloud.discoveryengine_v1beta.services.rank_service.client import (
    RankServiceClient,
)
from google.cloud.discoveryengine_v1beta.services.recommendation_service.async_client import (
    RecommendationServiceAsyncClient,
)
from google.cloud.discoveryengine_v1beta.services.recommendation_service.client import (
    RecommendationServiceClient,
)
from google.cloud.discoveryengine_v1beta.services.sample_query_service.async_client import (
    SampleQueryServiceAsyncClient,
)
from google.cloud.discoveryengine_v1beta.services.sample_query_service.client import (
    SampleQueryServiceClient,
)
from google.cloud.discoveryengine_v1beta.services.sample_query_set_service.async_client import (
    SampleQuerySetServiceAsyncClient,
)
from google.cloud.discoveryengine_v1beta.services.sample_query_set_service.client import (
    SampleQuerySetServiceClient,
)
from google.cloud.discoveryengine_v1beta.services.schema_service.async_client import (
    SchemaServiceAsyncClient,
)
from google.cloud.discoveryengine_v1beta.services.schema_service.client import (
    SchemaServiceClient,
)
from google.cloud.discoveryengine_v1beta.services.search_service.async_client import (
    SearchServiceAsyncClient,
)
from google.cloud.discoveryengine_v1beta.services.search_service.client import (
    SearchServiceClient,
)
from google.cloud.discoveryengine_v1beta.services.search_tuning_service.async_client import (
    SearchTuningServiceAsyncClient,
)
from google.cloud.discoveryengine_v1beta.services.search_tuning_service.client import (
    SearchTuningServiceClient,
)
from google.cloud.discoveryengine_v1beta.services.serving_config_service.async_client import (
    ServingConfigServiceAsyncClient,
)
from google.cloud.discoveryengine_v1beta.services.serving_config_service.client import (
    ServingConfigServiceClient,
)
from google.cloud.discoveryengine_v1beta.services.session_service.async_client import (
    SessionServiceAsyncClient,
)
from google.cloud.discoveryengine_v1beta.services.session_service.client import (
    SessionServiceClient,
)
from google.cloud.discoveryengine_v1beta.services.site_search_engine_service.async_client import (
    SiteSearchEngineServiceAsyncClient,
)
from google.cloud.discoveryengine_v1beta.services.site_search_engine_service.client import (
    SiteSearchEngineServiceClient,
)
from google.cloud.discoveryengine_v1beta.services.user_event_service.async_client import (
    UserEventServiceAsyncClient,
)
from google.cloud.discoveryengine_v1beta.services.user_event_service.client import (
    UserEventServiceClient,
)
from google.cloud.discoveryengine_v1beta.services.user_license_service.async_client import (
    UserLicenseServiceAsyncClient,
)
from google.cloud.discoveryengine_v1beta.services.user_license_service.client import (
    UserLicenseServiceClient,
)
from google.cloud.discoveryengine_v1beta.services.user_store_service.async_client import (
    UserStoreServiceAsyncClient,
)
from google.cloud.discoveryengine_v1beta.services.user_store_service.client import (
    UserStoreServiceClient,
)
from google.cloud.discoveryengine_v1beta.types.acl_config import AclConfig
from google.cloud.discoveryengine_v1beta.types.acl_config_service import (
    GetAclConfigRequest,
    UpdateAclConfigRequest,
)
from google.cloud.discoveryengine_v1beta.types.agent_gateway_setting import (
    AgentGatewaySetting,
)
from google.cloud.discoveryengine_v1beta.types.answer import Answer
from google.cloud.discoveryengine_v1beta.types.assist_answer import (
    AssistAnswer,
    AssistantContent,
    AssistantGroundedContent,
)
from google.cloud.discoveryengine_v1beta.types.assistant import Assistant
from google.cloud.discoveryengine_v1beta.types.assistant_service import (
    AssistUserMetadata,
    CreateAssistantRequest,
    DeleteAssistantRequest,
    GetAssistantRequest,
    ListAssistantsRequest,
    ListAssistantsResponse,
    StreamAssistRequest,
    StreamAssistResponse,
    UpdateAssistantRequest,
)
from google.cloud.discoveryengine_v1beta.types.chunk import Chunk
from google.cloud.discoveryengine_v1beta.types.cmek_config_service import (
    CmekConfig,
    DeleteCmekConfigMetadata,
    DeleteCmekConfigRequest,
    GetCmekConfigRequest,
    ListCmekConfigsRequest,
    ListCmekConfigsResponse,
    SingleRegionKey,
    UpdateCmekConfigMetadata,
    UpdateCmekConfigRequest,
)
from google.cloud.discoveryengine_v1beta.types.common import (
    CustomAttribute,
    DoubleList,
    EmbeddingConfig,
    HealthcareFhirConfig,
    IdpConfig,
    IndustryVertical,
    Interval,
    Principal,
    SearchAddOn,
    SearchLinkPromotion,
    SearchTier,
    SearchUseCase,
    SolutionType,
    SubscriptionTerm,
    SubscriptionTier,
    UserInfo,
)
from google.cloud.discoveryengine_v1beta.types.completion import (
    CompletionSuggestion,
    SuggestionDenyListEntry,
)
from google.cloud.discoveryengine_v1beta.types.completion_service import (
    AdvancedCompleteQueryRequest,
    AdvancedCompleteQueryResponse,
    CompleteQueryRequest,
    CompleteQueryResponse,
    RemoveSuggestionRequest,
    RemoveSuggestionResponse,
)
from google.cloud.discoveryengine_v1beta.types.control import Condition, Control
from google.cloud.discoveryengine_v1beta.types.control_service import (
    CreateControlRequest,
    DeleteControlRequest,
    GetControlRequest,
    ListControlsRequest,
    ListControlsResponse,
    UpdateControlRequest,
)
from google.cloud.discoveryengine_v1beta.types.conversation import (
    Conversation,
    ConversationContext,
    ConversationMessage,
    Reply,
    TextInput,
)
from google.cloud.discoveryengine_v1beta.types.conversational_search_service import (
    AnswerQueryRequest,
    AnswerQueryResponse,
    ConverseConversationRequest,
    ConverseConversationResponse,
    CreateConversationRequest,
    CreateSessionRequest,
    DeleteConversationRequest,
    DeleteSessionRequest,
    GetAnswerRequest,
    GetConversationRequest,
    GetSessionRequest,
    ListConversationsRequest,
    ListConversationsResponse,
    ListSessionsRequest,
    ListSessionsResponse,
    UpdateConversationRequest,
    UpdateSessionRequest,
)
from google.cloud.discoveryengine_v1beta.types.custom_tuning_model import (
    CustomTuningModel,
)
from google.cloud.discoveryengine_v1beta.types.data_store import (
    AdvancedSiteSearchConfig,
    DataStore,
    LanguageInfo,
    NaturalLanguageQueryUnderstandingConfig,
    WorkspaceConfig,
)
from google.cloud.discoveryengine_v1beta.types.data_store_service import (
    CreateDataStoreMetadata,
    CreateDataStoreRequest,
    DeleteDataStoreMetadata,
    DeleteDataStoreRequest,
    GetDataStoreRequest,
    ListDataStoresRequest,
    ListDataStoresResponse,
    UpdateDataStoreRequest,
)
from google.cloud.discoveryengine_v1beta.types.document import Document
from google.cloud.discoveryengine_v1beta.types.document_processing_config import (
    DocumentProcessingConfig,
)
from google.cloud.discoveryengine_v1beta.types.document_service import (
    BatchGetDocumentsMetadataRequest,
    BatchGetDocumentsMetadataResponse,
    CreateDocumentRequest,
    DeleteDocumentRequest,
    GetDocumentRequest,
    ListDocumentsRequest,
    ListDocumentsResponse,
    UpdateDocumentRequest,
)
from google.cloud.discoveryengine_v1beta.types.engine import Engine
from google.cloud.discoveryengine_v1beta.types.engine_service import (
    CreateEngineMetadata,
    CreateEngineRequest,
    DeleteEngineMetadata,
    DeleteEngineRequest,
    GetEngineRequest,
    ListEnginesRequest,
    ListEnginesResponse,
    PauseEngineRequest,
    ResumeEngineRequest,
    TuneEngineMetadata,
    TuneEngineRequest,
    TuneEngineResponse,
    UpdateEngineRequest,
)
from google.cloud.discoveryengine_v1beta.types.evaluation import (
    Evaluation,
    QualityMetrics,
)
from google.cloud.discoveryengine_v1beta.types.evaluation_service import (
    CreateEvaluationMetadata,
    CreateEvaluationRequest,
    GetEvaluationRequest,
    ListEvaluationResultsRequest,
    ListEvaluationResultsResponse,
    ListEvaluationsRequest,
    ListEvaluationsResponse,
)
from google.cloud.discoveryengine_v1beta.types.feedback import Feedback
from google.cloud.discoveryengine_v1beta.types.grounded_generation_service import (
    CheckGroundingRequest,
    CheckGroundingResponse,
    CheckGroundingSpec,
    Citation,
    CitationMetadata,
    GenerateGroundedContentRequest,
    GenerateGroundedContentResponse,
    GroundedGenerationContent,
)
from google.cloud.discoveryengine_v1beta.types.grounding import (
    FactChunk,
    GroundingConfig,
    GroundingFact,
)
from google.cloud.discoveryengine_v1beta.types.identity_mapping_store import (
    IdentityMappingEntry,
    IdentityMappingStore,
)
from google.cloud.discoveryengine_v1beta.types.identity_mapping_store_service import (
    CreateIdentityMappingStoreRequest,
    DeleteIdentityMappingStoreMetadata,
    DeleteIdentityMappingStoreRequest,
    GetIdentityMappingStoreRequest,
    IdentityMappingEntryOperationMetadata,
    ImportIdentityMappingsRequest,
    ImportIdentityMappingsResponse,
    ListIdentityMappingsRequest,
    ListIdentityMappingsResponse,
    ListIdentityMappingStoresRequest,
    ListIdentityMappingStoresResponse,
    PurgeIdentityMappingsRequest,
)
from google.cloud.discoveryengine_v1beta.types.import_config import (
    AlloyDbSource,
    BigQuerySource,
    BigtableOptions,
    BigtableSource,
    CloudSqlSource,
    FhirStoreSource,
    FirestoreSource,
    GcsSource,
    ImportCompletionSuggestionsMetadata,
    ImportCompletionSuggestionsRequest,
    ImportCompletionSuggestionsResponse,
    ImportDocumentsMetadata,
    ImportDocumentsRequest,
    ImportDocumentsResponse,
    ImportErrorConfig,
    ImportSampleQueriesMetadata,
    ImportSampleQueriesRequest,
    ImportSampleQueriesResponse,
    ImportSuggestionDenyListEntriesMetadata,
    ImportSuggestionDenyListEntriesRequest,
    ImportSuggestionDenyListEntriesResponse,
    ImportUserEventsMetadata,
    ImportUserEventsRequest,
    ImportUserEventsResponse,
    SpannerSource,
)
from google.cloud.discoveryengine_v1beta.types.license_config import LicenseConfig
from google.cloud.discoveryengine_v1beta.types.license_config_service import (
    CreateLicenseConfigRequest,
    DistributeLicenseConfigRequest,
    DistributeLicenseConfigResponse,
    GetLicenseConfigRequest,
    ListLicenseConfigsRequest,
    ListLicenseConfigsResponse,
    RetractLicenseConfigRequest,
    RetractLicenseConfigResponse,
    UpdateLicenseConfigRequest,
)
from google.cloud.discoveryengine_v1beta.types.logging import ObservabilityConfig
from google.cloud.discoveryengine_v1beta.types.project import Project
from google.cloud.discoveryengine_v1beta.types.project_service import (
    ProvisionProjectMetadata,
    ProvisionProjectRequest,
)
from google.cloud.discoveryengine_v1beta.types.purge_config import (
    PurgeCompletionSuggestionsMetadata,
    PurgeCompletionSuggestionsRequest,
    PurgeCompletionSuggestionsResponse,
    PurgeDocumentsMetadata,
    PurgeDocumentsRequest,
    PurgeDocumentsResponse,
    PurgeErrorConfig,
    PurgeSuggestionDenyListEntriesMetadata,
    PurgeSuggestionDenyListEntriesRequest,
    PurgeSuggestionDenyListEntriesResponse,
    PurgeUserEventsMetadata,
    PurgeUserEventsRequest,
    PurgeUserEventsResponse,
)
from google.cloud.discoveryengine_v1beta.types.rank_service import (
    RankingRecord,
    RankRequest,
    RankResponse,
)
from google.cloud.discoveryengine_v1beta.types.recommendation_service import (
    RecommendRequest,
    RecommendResponse,
)
from google.cloud.discoveryengine_v1beta.types.safety import HarmCategory, SafetyRating
from google.cloud.discoveryengine_v1beta.types.sample_query import SampleQuery
from google.cloud.discoveryengine_v1beta.types.sample_query_service import (
    CreateSampleQueryRequest,
    DeleteSampleQueryRequest,
    GetSampleQueryRequest,
    ListSampleQueriesRequest,
    ListSampleQueriesResponse,
    UpdateSampleQueryRequest,
)
from google.cloud.discoveryengine_v1beta.types.sample_query_set import SampleQuerySet
from google.cloud.discoveryengine_v1beta.types.sample_query_set_service import (
    CreateSampleQuerySetRequest,
    DeleteSampleQuerySetRequest,
    GetSampleQuerySetRequest,
    ListSampleQuerySetsRequest,
    ListSampleQuerySetsResponse,
    UpdateSampleQuerySetRequest,
)
from google.cloud.discoveryengine_v1beta.types.schema import Schema
from google.cloud.discoveryengine_v1beta.types.schema_service import (
    CreateSchemaMetadata,
    CreateSchemaRequest,
    DeleteSchemaMetadata,
    DeleteSchemaRequest,
    GetSchemaRequest,
    ListSchemasRequest,
    ListSchemasResponse,
    UpdateSchemaMetadata,
    UpdateSchemaRequest,
)
from google.cloud.discoveryengine_v1beta.types.search_service import (
    SearchRequest,
    SearchResponse,
)
from google.cloud.discoveryengine_v1beta.types.search_tuning_service import (
    ListCustomModelsRequest,
    ListCustomModelsResponse,
    TrainCustomModelMetadata,
    TrainCustomModelRequest,
    TrainCustomModelResponse,
)
from google.cloud.discoveryengine_v1beta.types.serving_config import (
    AnswerGenerationSpec,
    ServingConfig,
)
from google.cloud.discoveryengine_v1beta.types.serving_config_service import (
    CreateServingConfigRequest,
    DeleteServingConfigRequest,
    GetServingConfigRequest,
    ListServingConfigsRequest,
    ListServingConfigsResponse,
    UpdateServingConfigRequest,
)
from google.cloud.discoveryengine_v1beta.types.session import Query, Session
from google.cloud.discoveryengine_v1beta.types.site_search_engine import (
    Sitemap,
    SiteSearchEngine,
    SiteVerificationInfo,
    TargetSite,
)
from google.cloud.discoveryengine_v1beta.types.site_search_engine_service import (
    BatchCreateTargetSiteMetadata,
    BatchCreateTargetSitesRequest,
    BatchCreateTargetSitesResponse,
    BatchVerifyTargetSitesMetadata,
    BatchVerifyTargetSitesRequest,
    BatchVerifyTargetSitesResponse,
    CreateSitemapMetadata,
    CreateSitemapRequest,
    CreateTargetSiteMetadata,
    CreateTargetSiteRequest,
    DeleteSitemapMetadata,
    DeleteSitemapRequest,
    DeleteTargetSiteMetadata,
    DeleteTargetSiteRequest,
    DisableAdvancedSiteSearchMetadata,
    DisableAdvancedSiteSearchRequest,
    DisableAdvancedSiteSearchResponse,
    EnableAdvancedSiteSearchMetadata,
    EnableAdvancedSiteSearchRequest,
    EnableAdvancedSiteSearchResponse,
    FetchDomainVerificationStatusRequest,
    FetchDomainVerificationStatusResponse,
    FetchSitemapsRequest,
    FetchSitemapsResponse,
    GetSiteSearchEngineRequest,
    GetTargetSiteRequest,
    ListTargetSitesRequest,
    ListTargetSitesResponse,
    RecrawlUrisMetadata,
    RecrawlUrisRequest,
    RecrawlUrisResponse,
    UpdateTargetSiteMetadata,
    UpdateTargetSiteRequest,
)
from google.cloud.discoveryengine_v1beta.types.user_event import (
    CompletionInfo,
    DocumentInfo,
    MediaInfo,
    PageInfo,
    PanelInfo,
    SearchInfo,
    TransactionInfo,
    UserEvent,
)
from google.cloud.discoveryengine_v1beta.types.user_event_service import (
    CollectUserEventRequest,
    WriteUserEventRequest,
)
from google.cloud.discoveryengine_v1beta.types.user_license import (
    LicenseConfigUsageStats,
    UserLicense,
)
from google.cloud.discoveryengine_v1beta.types.user_license_service import (
    BatchUpdateUserLicensesMetadata,
    BatchUpdateUserLicensesRequest,
    BatchUpdateUserLicensesResponse,
    ListLicenseConfigsUsageStatsRequest,
    ListLicenseConfigsUsageStatsResponse,
    ListUserLicensesRequest,
    ListUserLicensesResponse,
)
from google.cloud.discoveryengine_v1beta.types.user_store import UserStore
from google.cloud.discoveryengine_v1beta.types.user_store_service import (
    GetUserStoreRequest,
    UpdateUserStoreRequest,
)

__all__ = (
    "AclConfigServiceClient",
    "AclConfigServiceAsyncClient",
    "AssistantServiceClient",
    "AssistantServiceAsyncClient",
    "CmekConfigServiceClient",
    "CmekConfigServiceAsyncClient",
    "CompletionServiceClient",
    "CompletionServiceAsyncClient",
    "ControlServiceClient",
    "ControlServiceAsyncClient",
    "ConversationalSearchServiceClient",
    "ConversationalSearchServiceAsyncClient",
    "DataStoreServiceClient",
    "DataStoreServiceAsyncClient",
    "DocumentServiceClient",
    "DocumentServiceAsyncClient",
    "EngineServiceClient",
    "EngineServiceAsyncClient",
    "EvaluationServiceClient",
    "EvaluationServiceAsyncClient",
    "GroundedGenerationServiceClient",
    "GroundedGenerationServiceAsyncClient",
    "IdentityMappingStoreServiceClient",
    "IdentityMappingStoreServiceAsyncClient",
    "LicenseConfigServiceClient",
    "LicenseConfigServiceAsyncClient",
    "ProjectServiceClient",
    "ProjectServiceAsyncClient",
    "RankServiceClient",
    "RankServiceAsyncClient",
    "RecommendationServiceClient",
    "RecommendationServiceAsyncClient",
    "SampleQueryServiceClient",
    "SampleQueryServiceAsyncClient",
    "SampleQuerySetServiceClient",
    "SampleQuerySetServiceAsyncClient",
    "SchemaServiceClient",
    "SchemaServiceAsyncClient",
    "SearchServiceClient",
    "SearchServiceAsyncClient",
    "SearchTuningServiceClient",
    "SearchTuningServiceAsyncClient",
    "ServingConfigServiceClient",
    "ServingConfigServiceAsyncClient",
    "SessionServiceClient",
    "SessionServiceAsyncClient",
    "SiteSearchEngineServiceClient",
    "SiteSearchEngineServiceAsyncClient",
    "UserEventServiceClient",
    "UserEventServiceAsyncClient",
    "UserLicenseServiceClient",
    "UserLicenseServiceAsyncClient",
    "UserStoreServiceClient",
    "UserStoreServiceAsyncClient",
    "AclConfig",
    "GetAclConfigRequest",
    "UpdateAclConfigRequest",
    "AgentGatewaySetting",
    "Answer",
    "AssistAnswer",
    "AssistantContent",
    "AssistantGroundedContent",
    "Assistant",
    "AssistUserMetadata",
    "CreateAssistantRequest",
    "DeleteAssistantRequest",
    "GetAssistantRequest",
    "ListAssistantsRequest",
    "ListAssistantsResponse",
    "StreamAssistRequest",
    "StreamAssistResponse",
    "UpdateAssistantRequest",
    "Chunk",
    "CmekConfig",
    "DeleteCmekConfigMetadata",
    "DeleteCmekConfigRequest",
    "GetCmekConfigRequest",
    "ListCmekConfigsRequest",
    "ListCmekConfigsResponse",
    "SingleRegionKey",
    "UpdateCmekConfigMetadata",
    "UpdateCmekConfigRequest",
    "CustomAttribute",
    "DoubleList",
    "EmbeddingConfig",
    "HealthcareFhirConfig",
    "IdpConfig",
    "Interval",
    "Principal",
    "SearchLinkPromotion",
    "UserInfo",
    "IndustryVertical",
    "SearchAddOn",
    "SearchTier",
    "SearchUseCase",
    "SolutionType",
    "SubscriptionTerm",
    "SubscriptionTier",
    "CompletionSuggestion",
    "SuggestionDenyListEntry",
    "AdvancedCompleteQueryRequest",
    "AdvancedCompleteQueryResponse",
    "CompleteQueryRequest",
    "CompleteQueryResponse",
    "RemoveSuggestionRequest",
    "RemoveSuggestionResponse",
    "Condition",
    "Control",
    "CreateControlRequest",
    "DeleteControlRequest",
    "GetControlRequest",
    "ListControlsRequest",
    "ListControlsResponse",
    "UpdateControlRequest",
    "Conversation",
    "ConversationContext",
    "ConversationMessage",
    "Reply",
    "TextInput",
    "AnswerQueryRequest",
    "AnswerQueryResponse",
    "ConverseConversationRequest",
    "ConverseConversationResponse",
    "CreateConversationRequest",
    "CreateSessionRequest",
    "DeleteConversationRequest",
    "DeleteSessionRequest",
    "GetAnswerRequest",
    "GetConversationRequest",
    "GetSessionRequest",
    "ListConversationsRequest",
    "ListConversationsResponse",
    "ListSessionsRequest",
    "ListSessionsResponse",
    "UpdateConversationRequest",
    "UpdateSessionRequest",
    "CustomTuningModel",
    "AdvancedSiteSearchConfig",
    "DataStore",
    "LanguageInfo",
    "NaturalLanguageQueryUnderstandingConfig",
    "WorkspaceConfig",
    "CreateDataStoreMetadata",
    "CreateDataStoreRequest",
    "DeleteDataStoreMetadata",
    "DeleteDataStoreRequest",
    "GetDataStoreRequest",
    "ListDataStoresRequest",
    "ListDataStoresResponse",
    "UpdateDataStoreRequest",
    "Document",
    "DocumentProcessingConfig",
    "BatchGetDocumentsMetadataRequest",
    "BatchGetDocumentsMetadataResponse",
    "CreateDocumentRequest",
    "DeleteDocumentRequest",
    "GetDocumentRequest",
    "ListDocumentsRequest",
    "ListDocumentsResponse",
    "UpdateDocumentRequest",
    "Engine",
    "CreateEngineMetadata",
    "CreateEngineRequest",
    "DeleteEngineMetadata",
    "DeleteEngineRequest",
    "GetEngineRequest",
    "ListEnginesRequest",
    "ListEnginesResponse",
    "PauseEngineRequest",
    "ResumeEngineRequest",
    "TuneEngineMetadata",
    "TuneEngineRequest",
    "TuneEngineResponse",
    "UpdateEngineRequest",
    "Evaluation",
    "QualityMetrics",
    "CreateEvaluationMetadata",
    "CreateEvaluationRequest",
    "GetEvaluationRequest",
    "ListEvaluationResultsRequest",
    "ListEvaluationResultsResponse",
    "ListEvaluationsRequest",
    "ListEvaluationsResponse",
    "Feedback",
    "CheckGroundingRequest",
    "CheckGroundingResponse",
    "CheckGroundingSpec",
    "Citation",
    "CitationMetadata",
    "GenerateGroundedContentRequest",
    "GenerateGroundedContentResponse",
    "GroundedGenerationContent",
    "FactChunk",
    "GroundingConfig",
    "GroundingFact",
    "IdentityMappingEntry",
    "IdentityMappingStore",
    "CreateIdentityMappingStoreRequest",
    "DeleteIdentityMappingStoreMetadata",
    "DeleteIdentityMappingStoreRequest",
    "GetIdentityMappingStoreRequest",
    "IdentityMappingEntryOperationMetadata",
    "ImportIdentityMappingsRequest",
    "ImportIdentityMappingsResponse",
    "ListIdentityMappingsRequest",
    "ListIdentityMappingsResponse",
    "ListIdentityMappingStoresRequest",
    "ListIdentityMappingStoresResponse",
    "PurgeIdentityMappingsRequest",
    "AlloyDbSource",
    "BigQuerySource",
    "BigtableOptions",
    "BigtableSource",
    "CloudSqlSource",
    "FhirStoreSource",
    "FirestoreSource",
    "GcsSource",
    "ImportCompletionSuggestionsMetadata",
    "ImportCompletionSuggestionsRequest",
    "ImportCompletionSuggestionsResponse",
    "ImportDocumentsMetadata",
    "ImportDocumentsRequest",
    "ImportDocumentsResponse",
    "ImportErrorConfig",
    "ImportSampleQueriesMetadata",
    "ImportSampleQueriesRequest",
    "ImportSampleQueriesResponse",
    "ImportSuggestionDenyListEntriesMetadata",
    "ImportSuggestionDenyListEntriesRequest",
    "ImportSuggestionDenyListEntriesResponse",
    "ImportUserEventsMetadata",
    "ImportUserEventsRequest",
    "ImportUserEventsResponse",
    "SpannerSource",
    "LicenseConfig",
    "CreateLicenseConfigRequest",
    "DistributeLicenseConfigRequest",
    "DistributeLicenseConfigResponse",
    "GetLicenseConfigRequest",
    "ListLicenseConfigsRequest",
    "ListLicenseConfigsResponse",
    "RetractLicenseConfigRequest",
    "RetractLicenseConfigResponse",
    "UpdateLicenseConfigRequest",
    "ObservabilityConfig",
    "Project",
    "ProvisionProjectMetadata",
    "ProvisionProjectRequest",
    "PurgeCompletionSuggestionsMetadata",
    "PurgeCompletionSuggestionsRequest",
    "PurgeCompletionSuggestionsResponse",
    "PurgeDocumentsMetadata",
    "PurgeDocumentsRequest",
    "PurgeDocumentsResponse",
    "PurgeErrorConfig",
    "PurgeSuggestionDenyListEntriesMetadata",
    "PurgeSuggestionDenyListEntriesRequest",
    "PurgeSuggestionDenyListEntriesResponse",
    "PurgeUserEventsMetadata",
    "PurgeUserEventsRequest",
    "PurgeUserEventsResponse",
    "RankingRecord",
    "RankRequest",
    "RankResponse",
    "RecommendRequest",
    "RecommendResponse",
    "SafetyRating",
    "HarmCategory",
    "SampleQuery",
    "CreateSampleQueryRequest",
    "DeleteSampleQueryRequest",
    "GetSampleQueryRequest",
    "ListSampleQueriesRequest",
    "ListSampleQueriesResponse",
    "UpdateSampleQueryRequest",
    "SampleQuerySet",
    "CreateSampleQuerySetRequest",
    "DeleteSampleQuerySetRequest",
    "GetSampleQuerySetRequest",
    "ListSampleQuerySetsRequest",
    "ListSampleQuerySetsResponse",
    "UpdateSampleQuerySetRequest",
    "Schema",
    "CreateSchemaMetadata",
    "CreateSchemaRequest",
    "DeleteSchemaMetadata",
    "DeleteSchemaRequest",
    "GetSchemaRequest",
    "ListSchemasRequest",
    "ListSchemasResponse",
    "UpdateSchemaMetadata",
    "UpdateSchemaRequest",
    "SearchRequest",
    "SearchResponse",
    "ListCustomModelsRequest",
    "ListCustomModelsResponse",
    "TrainCustomModelMetadata",
    "TrainCustomModelRequest",
    "TrainCustomModelResponse",
    "AnswerGenerationSpec",
    "ServingConfig",
    "CreateServingConfigRequest",
    "DeleteServingConfigRequest",
    "GetServingConfigRequest",
    "ListServingConfigsRequest",
    "ListServingConfigsResponse",
    "UpdateServingConfigRequest",
    "Query",
    "Session",
    "Sitemap",
    "SiteSearchEngine",
    "SiteVerificationInfo",
    "TargetSite",
    "BatchCreateTargetSiteMetadata",
    "BatchCreateTargetSitesRequest",
    "BatchCreateTargetSitesResponse",
    "BatchVerifyTargetSitesMetadata",
    "BatchVerifyTargetSitesRequest",
    "BatchVerifyTargetSitesResponse",
    "CreateSitemapMetadata",
    "CreateSitemapRequest",
    "CreateTargetSiteMetadata",
    "CreateTargetSiteRequest",
    "DeleteSitemapMetadata",
    "DeleteSitemapRequest",
    "DeleteTargetSiteMetadata",
    "DeleteTargetSiteRequest",
    "DisableAdvancedSiteSearchMetadata",
    "DisableAdvancedSiteSearchRequest",
    "DisableAdvancedSiteSearchResponse",
    "EnableAdvancedSiteSearchMetadata",
    "EnableAdvancedSiteSearchRequest",
    "EnableAdvancedSiteSearchResponse",
    "FetchDomainVerificationStatusRequest",
    "FetchDomainVerificationStatusResponse",
    "FetchSitemapsRequest",
    "FetchSitemapsResponse",
    "GetSiteSearchEngineRequest",
    "GetTargetSiteRequest",
    "ListTargetSitesRequest",
    "ListTargetSitesResponse",
    "RecrawlUrisMetadata",
    "RecrawlUrisRequest",
    "RecrawlUrisResponse",
    "UpdateTargetSiteMetadata",
    "UpdateTargetSiteRequest",
    "CompletionInfo",
    "DocumentInfo",
    "MediaInfo",
    "PageInfo",
    "PanelInfo",
    "SearchInfo",
    "TransactionInfo",
    "UserEvent",
    "CollectUserEventRequest",
    "WriteUserEventRequest",
    "LicenseConfigUsageStats",
    "UserLicense",
    "BatchUpdateUserLicensesMetadata",
    "BatchUpdateUserLicensesRequest",
    "BatchUpdateUserLicensesResponse",
    "ListLicenseConfigsUsageStatsRequest",
    "ListLicenseConfigsUsageStatsResponse",
    "ListUserLicensesRequest",
    "ListUserLicensesResponse",
    "UserStore",
    "GetUserStoreRequest",
    "UpdateUserStoreRequest",
)
