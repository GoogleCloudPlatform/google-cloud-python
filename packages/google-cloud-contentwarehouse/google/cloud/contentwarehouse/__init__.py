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
from google.cloud.contentwarehouse import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.contentwarehouse_v1.services.document_link_service.async_client import (
    DocumentLinkServiceAsyncClient,
)
from google.cloud.contentwarehouse_v1.services.document_link_service.client import (
    DocumentLinkServiceClient,
)
from google.cloud.contentwarehouse_v1.services.document_schema_service.async_client import (
    DocumentSchemaServiceAsyncClient,
)
from google.cloud.contentwarehouse_v1.services.document_schema_service.client import (
    DocumentSchemaServiceClient,
)
from google.cloud.contentwarehouse_v1.services.document_service.async_client import (
    DocumentServiceAsyncClient,
)
from google.cloud.contentwarehouse_v1.services.document_service.client import (
    DocumentServiceClient,
)
from google.cloud.contentwarehouse_v1.services.pipeline_service.async_client import (
    PipelineServiceAsyncClient,
)
from google.cloud.contentwarehouse_v1.services.pipeline_service.client import (
    PipelineServiceClient,
)
from google.cloud.contentwarehouse_v1.services.rule_set_service.async_client import (
    RuleSetServiceAsyncClient,
)
from google.cloud.contentwarehouse_v1.services.rule_set_service.client import (
    RuleSetServiceClient,
)
from google.cloud.contentwarehouse_v1.services.synonym_set_service.async_client import (
    SynonymSetServiceAsyncClient,
)
from google.cloud.contentwarehouse_v1.services.synonym_set_service.client import (
    SynonymSetServiceClient,
)
from google.cloud.contentwarehouse_v1.types.async_document_service_request import (
    CreateDocumentMetadata,
    UpdateDocumentMetadata,
)
from google.cloud.contentwarehouse_v1.types.common import (
    AccessControlMode,
    DatabaseType,
    DocumentCreatorDefaultRole,
    MergeFieldsOptions,
    RequestMetadata,
    ResponseMetadata,
    UpdateOptions,
    UpdateType,
    UserInfo,
)
from google.cloud.contentwarehouse_v1.types.document import (
    ContentCategory,
    DateTimeArray,
    Document,
    DocumentReference,
    EnumArray,
    EnumValue,
    FloatArray,
    IntegerArray,
    MapProperty,
    Property,
    PropertyArray,
    RawDocumentFileType,
    TextArray,
    TimestampArray,
    TimestampValue,
    Value,
)
from google.cloud.contentwarehouse_v1.types.document_link_service import (
    CreateDocumentLinkRequest,
    DeleteDocumentLinkRequest,
    DocumentLink,
    ListLinkedSourcesRequest,
    ListLinkedSourcesResponse,
    ListLinkedTargetsRequest,
    ListLinkedTargetsResponse,
)
from google.cloud.contentwarehouse_v1.types.document_schema import (
    DateTimeTypeOptions,
    DocumentSchema,
    EnumTypeOptions,
    FloatTypeOptions,
    IntegerTypeOptions,
    MapTypeOptions,
    PropertyDefinition,
    PropertyTypeOptions,
    TextTypeOptions,
    TimestampTypeOptions,
)
from google.cloud.contentwarehouse_v1.types.document_schema_service import (
    CreateDocumentSchemaRequest,
    DeleteDocumentSchemaRequest,
    GetDocumentSchemaRequest,
    ListDocumentSchemasRequest,
    ListDocumentSchemasResponse,
    UpdateDocumentSchemaRequest,
)
from google.cloud.contentwarehouse_v1.types.document_service import (
    CreateDocumentResponse,
    FetchAclResponse,
    QAResult,
    SearchDocumentsResponse,
    SetAclResponse,
    UpdateDocumentResponse,
)
from google.cloud.contentwarehouse_v1.types.document_service_request import (
    CloudAIDocumentOption,
    CreateDocumentRequest,
    DeleteDocumentRequest,
    FetchAclRequest,
    GetDocumentRequest,
    LockDocumentRequest,
    SearchDocumentsRequest,
    SetAclRequest,
    UpdateDocumentRequest,
)
from google.cloud.contentwarehouse_v1.types.filters import (
    CustomWeightsMetadata,
    DocumentQuery,
    FileTypeFilter,
    PropertyFilter,
    TimeFilter,
    WeightedSchemaProperty,
)
from google.cloud.contentwarehouse_v1.types.histogram import (
    HistogramQuery,
    HistogramQueryPropertyNameFilter,
    HistogramQueryResult,
)
from google.cloud.contentwarehouse_v1.types.pipeline_service import RunPipelineRequest
from google.cloud.contentwarehouse_v1.types.pipelines import (
    ExportToCdwPipeline,
    GcsIngestPipeline,
    GcsIngestWithDocAiProcessorsPipeline,
    IngestPipelineConfig,
    ProcessorInfo,
    ProcessWithDocAiPipeline,
    RunPipelineMetadata,
    RunPipelineResponse,
)
from google.cloud.contentwarehouse_v1.types.rule_engine import (
    AccessControlAction,
    Action,
    ActionExecutorOutput,
    ActionOutput,
    AddToFolderAction,
    DataUpdateAction,
    DataValidationAction,
    DeleteDocumentAction,
    InvalidRule,
    PublishAction,
    RemoveFromFolderAction,
    Rule,
    RuleActionsPair,
    RuleEngineOutput,
    RuleEvaluatorOutput,
    RuleSet,
)
from google.cloud.contentwarehouse_v1.types.ruleset_service_request import (
    CreateRuleSetRequest,
    DeleteRuleSetRequest,
    GetRuleSetRequest,
    ListRuleSetsRequest,
    ListRuleSetsResponse,
    UpdateRuleSetRequest,
)
from google.cloud.contentwarehouse_v1.types.synonymset import SynonymSet
from google.cloud.contentwarehouse_v1.types.synonymset_service_request import (
    CreateSynonymSetRequest,
    DeleteSynonymSetRequest,
    GetSynonymSetRequest,
    ListSynonymSetsRequest,
    ListSynonymSetsResponse,
    UpdateSynonymSetRequest,
)

__all__ = (
    "DocumentLinkServiceClient",
    "DocumentLinkServiceAsyncClient",
    "DocumentSchemaServiceClient",
    "DocumentSchemaServiceAsyncClient",
    "DocumentServiceClient",
    "DocumentServiceAsyncClient",
    "PipelineServiceClient",
    "PipelineServiceAsyncClient",
    "RuleSetServiceClient",
    "RuleSetServiceAsyncClient",
    "SynonymSetServiceClient",
    "SynonymSetServiceAsyncClient",
    "CreateDocumentMetadata",
    "UpdateDocumentMetadata",
    "MergeFieldsOptions",
    "RequestMetadata",
    "ResponseMetadata",
    "UpdateOptions",
    "UserInfo",
    "AccessControlMode",
    "DatabaseType",
    "DocumentCreatorDefaultRole",
    "UpdateType",
    "DateTimeArray",
    "Document",
    "DocumentReference",
    "EnumArray",
    "EnumValue",
    "FloatArray",
    "IntegerArray",
    "MapProperty",
    "Property",
    "PropertyArray",
    "TextArray",
    "TimestampArray",
    "TimestampValue",
    "Value",
    "ContentCategory",
    "RawDocumentFileType",
    "CreateDocumentLinkRequest",
    "DeleteDocumentLinkRequest",
    "DocumentLink",
    "ListLinkedSourcesRequest",
    "ListLinkedSourcesResponse",
    "ListLinkedTargetsRequest",
    "ListLinkedTargetsResponse",
    "DateTimeTypeOptions",
    "DocumentSchema",
    "EnumTypeOptions",
    "FloatTypeOptions",
    "IntegerTypeOptions",
    "MapTypeOptions",
    "PropertyDefinition",
    "PropertyTypeOptions",
    "TextTypeOptions",
    "TimestampTypeOptions",
    "CreateDocumentSchemaRequest",
    "DeleteDocumentSchemaRequest",
    "GetDocumentSchemaRequest",
    "ListDocumentSchemasRequest",
    "ListDocumentSchemasResponse",
    "UpdateDocumentSchemaRequest",
    "CreateDocumentResponse",
    "FetchAclResponse",
    "QAResult",
    "SearchDocumentsResponse",
    "SetAclResponse",
    "UpdateDocumentResponse",
    "CloudAIDocumentOption",
    "CreateDocumentRequest",
    "DeleteDocumentRequest",
    "FetchAclRequest",
    "GetDocumentRequest",
    "LockDocumentRequest",
    "SearchDocumentsRequest",
    "SetAclRequest",
    "UpdateDocumentRequest",
    "CustomWeightsMetadata",
    "DocumentQuery",
    "FileTypeFilter",
    "PropertyFilter",
    "TimeFilter",
    "WeightedSchemaProperty",
    "HistogramQuery",
    "HistogramQueryPropertyNameFilter",
    "HistogramQueryResult",
    "RunPipelineRequest",
    "ExportToCdwPipeline",
    "GcsIngestPipeline",
    "GcsIngestWithDocAiProcessorsPipeline",
    "IngestPipelineConfig",
    "ProcessorInfo",
    "ProcessWithDocAiPipeline",
    "RunPipelineMetadata",
    "RunPipelineResponse",
    "AccessControlAction",
    "Action",
    "ActionExecutorOutput",
    "ActionOutput",
    "AddToFolderAction",
    "DataUpdateAction",
    "DataValidationAction",
    "DeleteDocumentAction",
    "InvalidRule",
    "PublishAction",
    "RemoveFromFolderAction",
    "Rule",
    "RuleActionsPair",
    "RuleEngineOutput",
    "RuleEvaluatorOutput",
    "RuleSet",
    "CreateRuleSetRequest",
    "DeleteRuleSetRequest",
    "GetRuleSetRequest",
    "ListRuleSetsRequest",
    "ListRuleSetsResponse",
    "UpdateRuleSetRequest",
    "SynonymSet",
    "CreateSynonymSetRequest",
    "DeleteSynonymSetRequest",
    "GetSynonymSetRequest",
    "ListSynonymSetsRequest",
    "ListSynonymSetsResponse",
    "UpdateSynonymSetRequest",
)
