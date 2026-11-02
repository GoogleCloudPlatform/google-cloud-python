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
from google.cloud.asset import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.asset_v1.services.asset_service.client import AssetServiceClient
from google.cloud.asset_v1.services.asset_service.async_client import AssetServiceAsyncClient

from google.cloud.asset_v1.types.asset_enrichment_resourceowners import ResourceOwners
from google.cloud.asset_v1.types.asset_service import AnalyzeIamPolicyLongrunningMetadata
from google.cloud.asset_v1.types.asset_service import AnalyzeIamPolicyLongrunningRequest
from google.cloud.asset_v1.types.asset_service import AnalyzeIamPolicyLongrunningResponse
from google.cloud.asset_v1.types.asset_service import AnalyzeIamPolicyRequest
from google.cloud.asset_v1.types.asset_service import AnalyzeIamPolicyResponse
from google.cloud.asset_v1.types.asset_service import AnalyzeMoveRequest
from google.cloud.asset_v1.types.asset_service import AnalyzeMoveResponse
from google.cloud.asset_v1.types.asset_service import AnalyzeOrgPoliciesRequest
from google.cloud.asset_v1.types.asset_service import AnalyzeOrgPoliciesResponse
from google.cloud.asset_v1.types.asset_service import AnalyzeOrgPolicyGovernedAssetsRequest
from google.cloud.asset_v1.types.asset_service import AnalyzeOrgPolicyGovernedAssetsResponse
from google.cloud.asset_v1.types.asset_service import AnalyzeOrgPolicyGovernedContainersRequest
from google.cloud.asset_v1.types.asset_service import AnalyzeOrgPolicyGovernedContainersResponse
from google.cloud.asset_v1.types.asset_service import AnalyzerOrgPolicy
from google.cloud.asset_v1.types.asset_service import AnalyzerOrgPolicyConstraint
from google.cloud.asset_v1.types.asset_service import BatchGetAssetsHistoryRequest
from google.cloud.asset_v1.types.asset_service import BatchGetAssetsHistoryResponse
from google.cloud.asset_v1.types.asset_service import BatchGetEffectiveIamPoliciesRequest
from google.cloud.asset_v1.types.asset_service import BatchGetEffectiveIamPoliciesResponse
from google.cloud.asset_v1.types.asset_service import BigQueryDestination
from google.cloud.asset_v1.types.asset_service import CreateFeedRequest
from google.cloud.asset_v1.types.asset_service import CreateSavedQueryRequest
from google.cloud.asset_v1.types.asset_service import DeleteFeedRequest
from google.cloud.asset_v1.types.asset_service import DeleteSavedQueryRequest
from google.cloud.asset_v1.types.asset_service import ExportAssetsRequest
from google.cloud.asset_v1.types.asset_service import ExportAssetsResponse
from google.cloud.asset_v1.types.asset_service import Feed
from google.cloud.asset_v1.types.asset_service import FeedOutputConfig
from google.cloud.asset_v1.types.asset_service import GcsDestination
from google.cloud.asset_v1.types.asset_service import GcsOutputResult
from google.cloud.asset_v1.types.asset_service import GetFeedRequest
from google.cloud.asset_v1.types.asset_service import GetSavedQueryRequest
from google.cloud.asset_v1.types.asset_service import IamPolicyAnalysisOutputConfig
from google.cloud.asset_v1.types.asset_service import IamPolicyAnalysisQuery
from google.cloud.asset_v1.types.asset_service import ListAssetsRequest
from google.cloud.asset_v1.types.asset_service import ListAssetsResponse
from google.cloud.asset_v1.types.asset_service import ListFeedsRequest
from google.cloud.asset_v1.types.asset_service import ListFeedsResponse
from google.cloud.asset_v1.types.asset_service import ListSavedQueriesRequest
from google.cloud.asset_v1.types.asset_service import ListSavedQueriesResponse
from google.cloud.asset_v1.types.asset_service import MoveAnalysis
from google.cloud.asset_v1.types.asset_service import MoveAnalysisResult
from google.cloud.asset_v1.types.asset_service import MoveImpact
from google.cloud.asset_v1.types.asset_service import OutputConfig
from google.cloud.asset_v1.types.asset_service import OutputResult
from google.cloud.asset_v1.types.asset_service import PartitionSpec
from google.cloud.asset_v1.types.asset_service import PubsubDestination
from google.cloud.asset_v1.types.asset_service import QueryAssetsOutputConfig
from google.cloud.asset_v1.types.asset_service import QueryAssetsRequest
from google.cloud.asset_v1.types.asset_service import QueryAssetsResponse
from google.cloud.asset_v1.types.asset_service import QueryResult
from google.cloud.asset_v1.types.asset_service import SavedQuery
from google.cloud.asset_v1.types.asset_service import SearchAllIamPoliciesRequest
from google.cloud.asset_v1.types.asset_service import SearchAllIamPoliciesResponse
from google.cloud.asset_v1.types.asset_service import SearchAllResourcesRequest
from google.cloud.asset_v1.types.asset_service import SearchAllResourcesResponse
from google.cloud.asset_v1.types.asset_service import TableFieldSchema
from google.cloud.asset_v1.types.asset_service import TableSchema
from google.cloud.asset_v1.types.asset_service import UpdateFeedRequest
from google.cloud.asset_v1.types.asset_service import UpdateSavedQueryRequest
from google.cloud.asset_v1.types.asset_service import ContentType
from google.cloud.asset_v1.types.assets import Asset
from google.cloud.asset_v1.types.assets import AssetEnrichment
from google.cloud.asset_v1.types.assets import AttachedResource
from google.cloud.asset_v1.types.assets import ConditionEvaluation
from google.cloud.asset_v1.types.assets import EffectiveTagDetails
from google.cloud.asset_v1.types.assets import IamPolicyAnalysisResult
from google.cloud.asset_v1.types.assets import IamPolicyAnalysisState
from google.cloud.asset_v1.types.assets import IamPolicySearchResult
from google.cloud.asset_v1.types.assets import RelatedAsset
from google.cloud.asset_v1.types.assets import RelatedAssets
from google.cloud.asset_v1.types.assets import RelatedResource
from google.cloud.asset_v1.types.assets import RelatedResources
from google.cloud.asset_v1.types.assets import RelationshipAttributes
from google.cloud.asset_v1.types.assets import Resource
from google.cloud.asset_v1.types.assets import ResourceSearchResult
from google.cloud.asset_v1.types.assets import Tag
from google.cloud.asset_v1.types.assets import TemporalAsset
from google.cloud.asset_v1.types.assets import TimeWindow
from google.cloud.asset_v1.types.assets import VersionedResource

__all__ = ('AssetServiceClient',
    'AssetServiceAsyncClient',
    'ResourceOwners',
    'AnalyzeIamPolicyLongrunningMetadata',
    'AnalyzeIamPolicyLongrunningRequest',
    'AnalyzeIamPolicyLongrunningResponse',
    'AnalyzeIamPolicyRequest',
    'AnalyzeIamPolicyResponse',
    'AnalyzeMoveRequest',
    'AnalyzeMoveResponse',
    'AnalyzeOrgPoliciesRequest',
    'AnalyzeOrgPoliciesResponse',
    'AnalyzeOrgPolicyGovernedAssetsRequest',
    'AnalyzeOrgPolicyGovernedAssetsResponse',
    'AnalyzeOrgPolicyGovernedContainersRequest',
    'AnalyzeOrgPolicyGovernedContainersResponse',
    'AnalyzerOrgPolicy',
    'AnalyzerOrgPolicyConstraint',
    'BatchGetAssetsHistoryRequest',
    'BatchGetAssetsHistoryResponse',
    'BatchGetEffectiveIamPoliciesRequest',
    'BatchGetEffectiveIamPoliciesResponse',
    'BigQueryDestination',
    'CreateFeedRequest',
    'CreateSavedQueryRequest',
    'DeleteFeedRequest',
    'DeleteSavedQueryRequest',
    'ExportAssetsRequest',
    'ExportAssetsResponse',
    'Feed',
    'FeedOutputConfig',
    'GcsDestination',
    'GcsOutputResult',
    'GetFeedRequest',
    'GetSavedQueryRequest',
    'IamPolicyAnalysisOutputConfig',
    'IamPolicyAnalysisQuery',
    'ListAssetsRequest',
    'ListAssetsResponse',
    'ListFeedsRequest',
    'ListFeedsResponse',
    'ListSavedQueriesRequest',
    'ListSavedQueriesResponse',
    'MoveAnalysis',
    'MoveAnalysisResult',
    'MoveImpact',
    'OutputConfig',
    'OutputResult',
    'PartitionSpec',
    'PubsubDestination',
    'QueryAssetsOutputConfig',
    'QueryAssetsRequest',
    'QueryAssetsResponse',
    'QueryResult',
    'SavedQuery',
    'SearchAllIamPoliciesRequest',
    'SearchAllIamPoliciesResponse',
    'SearchAllResourcesRequest',
    'SearchAllResourcesResponse',
    'TableFieldSchema',
    'TableSchema',
    'UpdateFeedRequest',
    'UpdateSavedQueryRequest',
    'ContentType',
    'Asset',
    'AssetEnrichment',
    'AttachedResource',
    'ConditionEvaluation',
    'EffectiveTagDetails',
    'IamPolicyAnalysisResult',
    'IamPolicyAnalysisState',
    'IamPolicySearchResult',
    'RelatedAsset',
    'RelatedAssets',
    'RelatedResource',
    'RelatedResources',
    'RelationshipAttributes',
    'Resource',
    'ResourceSearchResult',
    'Tag',
    'TemporalAsset',
    'TimeWindow',
    'VersionedResource',
)
