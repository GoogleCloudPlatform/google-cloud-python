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
from google.cloud.asset_v1 import gapic_version as package_version

import google.api_core as api_core

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
"google.cloud.asset_v1.services.asset_service",
"google.cloud.asset_v1.types.asset_enrichment_resourceowners",
"google.cloud.asset_v1.types.asset_service",
"google.cloud.asset_v1.types.assets",
}


from .services.asset_service import AssetServiceClient
from .services.asset_service import AssetServiceAsyncClient

from .types.asset_enrichment_resourceowners import ResourceOwners
from .types.asset_service import AnalyzeIamPolicyLongrunningMetadata
from .types.asset_service import AnalyzeIamPolicyLongrunningRequest
from .types.asset_service import AnalyzeIamPolicyLongrunningResponse
from .types.asset_service import AnalyzeIamPolicyRequest
from .types.asset_service import AnalyzeIamPolicyResponse
from .types.asset_service import AnalyzeMoveRequest
from .types.asset_service import AnalyzeMoveResponse
from .types.asset_service import AnalyzeOrgPoliciesRequest
from .types.asset_service import AnalyzeOrgPoliciesResponse
from .types.asset_service import AnalyzeOrgPolicyGovernedAssetsRequest
from .types.asset_service import AnalyzeOrgPolicyGovernedAssetsResponse
from .types.asset_service import AnalyzeOrgPolicyGovernedContainersRequest
from .types.asset_service import AnalyzeOrgPolicyGovernedContainersResponse
from .types.asset_service import AnalyzerOrgPolicy
from .types.asset_service import AnalyzerOrgPolicyConstraint
from .types.asset_service import BatchGetAssetsHistoryRequest
from .types.asset_service import BatchGetAssetsHistoryResponse
from .types.asset_service import BatchGetEffectiveIamPoliciesRequest
from .types.asset_service import BatchGetEffectiveIamPoliciesResponse
from .types.asset_service import BigQueryDestination
from .types.asset_service import CreateFeedRequest
from .types.asset_service import CreateSavedQueryRequest
from .types.asset_service import DeleteFeedRequest
from .types.asset_service import DeleteSavedQueryRequest
from .types.asset_service import ExportAssetsRequest
from .types.asset_service import ExportAssetsResponse
from .types.asset_service import Feed
from .types.asset_service import FeedOutputConfig
from .types.asset_service import GcsDestination
from .types.asset_service import GcsOutputResult
from .types.asset_service import GetFeedRequest
from .types.asset_service import GetSavedQueryRequest
from .types.asset_service import IamPolicyAnalysisOutputConfig
from .types.asset_service import IamPolicyAnalysisQuery
from .types.asset_service import ListAssetsRequest
from .types.asset_service import ListAssetsResponse
from .types.asset_service import ListFeedsRequest
from .types.asset_service import ListFeedsResponse
from .types.asset_service import ListSavedQueriesRequest
from .types.asset_service import ListSavedQueriesResponse
from .types.asset_service import MoveAnalysis
from .types.asset_service import MoveAnalysisResult
from .types.asset_service import MoveImpact
from .types.asset_service import OutputConfig
from .types.asset_service import OutputResult
from .types.asset_service import PartitionSpec
from .types.asset_service import PubsubDestination
from .types.asset_service import QueryAssetsOutputConfig
from .types.asset_service import QueryAssetsRequest
from .types.asset_service import QueryAssetsResponse
from .types.asset_service import QueryResult
from .types.asset_service import SavedQuery
from .types.asset_service import SearchAllIamPoliciesRequest
from .types.asset_service import SearchAllIamPoliciesResponse
from .types.asset_service import SearchAllResourcesRequest
from .types.asset_service import SearchAllResourcesResponse
from .types.asset_service import TableFieldSchema
from .types.asset_service import TableSchema
from .types.asset_service import UpdateFeedRequest
from .types.asset_service import UpdateSavedQueryRequest
from .types.asset_service import ContentType
from .types.assets import Asset
from .types.assets import AssetEnrichment
from .types.assets import AttachedResource
from .types.assets import ConditionEvaluation
from .types.assets import EffectiveTagDetails
from .types.assets import IamPolicyAnalysisResult
from .types.assets import IamPolicyAnalysisState
from .types.assets import IamPolicySearchResult
from .types.assets import RelatedAsset
from .types.assets import RelatedAssets
from .types.assets import RelatedResource
from .types.assets import RelatedResources
from .types.assets import RelationshipAttributes
from .types.assets import Resource
from .types.assets import ResourceSearchResult
from .types.assets import Tag
from .types.assets import TemporalAsset
from .types.assets import TimeWindow
from .types.assets import VersionedResource

__all__ = (
    'AssetServiceAsyncClient',
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
'Asset',
'AssetEnrichment',
'AssetServiceClient',
'AttachedResource',
'BatchGetAssetsHistoryRequest',
'BatchGetAssetsHistoryResponse',
'BatchGetEffectiveIamPoliciesRequest',
'BatchGetEffectiveIamPoliciesResponse',
'BigQueryDestination',
'ConditionEvaluation',
'ContentType',
'CreateFeedRequest',
'CreateSavedQueryRequest',
'DeleteFeedRequest',
'DeleteSavedQueryRequest',
'EffectiveTagDetails',
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
'IamPolicyAnalysisResult',
'IamPolicyAnalysisState',
'IamPolicySearchResult',
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
'RelatedAsset',
'RelatedAssets',
'RelatedResource',
'RelatedResources',
'RelationshipAttributes',
'Resource',
'ResourceOwners',
'ResourceSearchResult',
'SavedQuery',
'SearchAllIamPoliciesRequest',
'SearchAllIamPoliciesResponse',
'SearchAllResourcesRequest',
'SearchAllResourcesResponse',
'TableFieldSchema',
'TableSchema',
'Tag',
'TemporalAsset',
'TimeWindow',
'UpdateFeedRequest',
'UpdateSavedQueryRequest',
'VersionedResource',
)

api_core.check_python_version("google.cloud.asset_v1")
api_core.check_dependency_versions("google.cloud.asset_v1")
