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

from google.cloud.datacatalog_v1beta1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.datacatalog_v1beta1.services.data_catalog",
    "google.cloud.datacatalog_v1beta1.services.policy_tag_manager",
    "google.cloud.datacatalog_v1beta1.services.policy_tag_manager_serialization",
    "google.cloud.datacatalog_v1beta1.types.common",
    "google.cloud.datacatalog_v1beta1.types.datacatalog",
    "google.cloud.datacatalog_v1beta1.types.gcs_fileset_spec",
    "google.cloud.datacatalog_v1beta1.types.policytagmanager",
    "google.cloud.datacatalog_v1beta1.types.policytagmanagerserialization",
    "google.cloud.datacatalog_v1beta1.types.schema",
    "google.cloud.datacatalog_v1beta1.types.search",
    "google.cloud.datacatalog_v1beta1.types.table_spec",
    "google.cloud.datacatalog_v1beta1.types.tags",
    "google.cloud.datacatalog_v1beta1.types.timestamps",
    "google.cloud.datacatalog_v1beta1.types.usage",
}


from .services.data_catalog import DataCatalogAsyncClient, DataCatalogClient
from .services.policy_tag_manager import (
    PolicyTagManagerAsyncClient,
    PolicyTagManagerClient,
)
from .services.policy_tag_manager_serialization import (
    PolicyTagManagerSerializationAsyncClient,
    PolicyTagManagerSerializationClient,
)
from .types.common import IntegratedSystem, ManagingSystem
from .types.datacatalog import (
    CreateEntryGroupRequest,
    CreateEntryRequest,
    CreateTagRequest,
    CreateTagTemplateFieldRequest,
    CreateTagTemplateRequest,
    DeleteEntryGroupRequest,
    DeleteEntryRequest,
    DeleteTagRequest,
    DeleteTagTemplateFieldRequest,
    DeleteTagTemplateRequest,
    Entry,
    EntryGroup,
    EntryType,
    GetEntryGroupRequest,
    GetEntryRequest,
    GetTagTemplateRequest,
    ListEntriesRequest,
    ListEntriesResponse,
    ListEntryGroupsRequest,
    ListEntryGroupsResponse,
    ListTagsRequest,
    ListTagsResponse,
    LookupEntryRequest,
    RenameTagTemplateFieldEnumValueRequest,
    RenameTagTemplateFieldRequest,
    SearchCatalogRequest,
    SearchCatalogResponse,
    UpdateEntryGroupRequest,
    UpdateEntryRequest,
    UpdateTagRequest,
    UpdateTagTemplateFieldRequest,
    UpdateTagTemplateRequest,
)
from .types.gcs_fileset_spec import GcsFilesetSpec, GcsFileSpec
from .types.policytagmanager import (
    CreatePolicyTagRequest,
    CreateTaxonomyRequest,
    DeletePolicyTagRequest,
    DeleteTaxonomyRequest,
    GetPolicyTagRequest,
    GetTaxonomyRequest,
    ListPolicyTagsRequest,
    ListPolicyTagsResponse,
    ListTaxonomiesRequest,
    ListTaxonomiesResponse,
    PolicyTag,
    Taxonomy,
    UpdatePolicyTagRequest,
    UpdateTaxonomyRequest,
)
from .types.policytagmanagerserialization import (
    ExportTaxonomiesRequest,
    ExportTaxonomiesResponse,
    ImportTaxonomiesRequest,
    ImportTaxonomiesResponse,
    InlineSource,
    SerializedPolicyTag,
    SerializedTaxonomy,
)
from .types.schema import ColumnSchema, Schema
from .types.search import SearchCatalogResult, SearchResultType
from .types.table_spec import (
    BigQueryDateShardedSpec,
    BigQueryTableSpec,
    TableSourceType,
    TableSpec,
    ViewSpec,
)
from .types.tags import FieldType, Tag, TagField, TagTemplate, TagTemplateField
from .types.timestamps import SystemTimestamps
from .types.usage import UsageSignal, UsageStats

__all__ = (
    "DataCatalogAsyncClient",
    "PolicyTagManagerAsyncClient",
    "PolicyTagManagerSerializationAsyncClient",
    "BigQueryDateShardedSpec",
    "BigQueryTableSpec",
    "ColumnSchema",
    "CreateEntryGroupRequest",
    "CreateEntryRequest",
    "CreatePolicyTagRequest",
    "CreateTagRequest",
    "CreateTagTemplateFieldRequest",
    "CreateTagTemplateRequest",
    "CreateTaxonomyRequest",
    "DataCatalogClient",
    "DeleteEntryGroupRequest",
    "DeleteEntryRequest",
    "DeletePolicyTagRequest",
    "DeleteTagRequest",
    "DeleteTagTemplateFieldRequest",
    "DeleteTagTemplateRequest",
    "DeleteTaxonomyRequest",
    "Entry",
    "EntryGroup",
    "EntryType",
    "ExportTaxonomiesRequest",
    "ExportTaxonomiesResponse",
    "FieldType",
    "GcsFileSpec",
    "GcsFilesetSpec",
    "GetEntryGroupRequest",
    "GetEntryRequest",
    "GetPolicyTagRequest",
    "GetTagTemplateRequest",
    "GetTaxonomyRequest",
    "ImportTaxonomiesRequest",
    "ImportTaxonomiesResponse",
    "InlineSource",
    "IntegratedSystem",
    "ListEntriesRequest",
    "ListEntriesResponse",
    "ListEntryGroupsRequest",
    "ListEntryGroupsResponse",
    "ListPolicyTagsRequest",
    "ListPolicyTagsResponse",
    "ListTagsRequest",
    "ListTagsResponse",
    "ListTaxonomiesRequest",
    "ListTaxonomiesResponse",
    "LookupEntryRequest",
    "ManagingSystem",
    "PolicyTag",
    "PolicyTagManagerClient",
    "PolicyTagManagerSerializationClient",
    "RenameTagTemplateFieldEnumValueRequest",
    "RenameTagTemplateFieldRequest",
    "Schema",
    "SearchCatalogRequest",
    "SearchCatalogResponse",
    "SearchCatalogResult",
    "SearchResultType",
    "SerializedPolicyTag",
    "SerializedTaxonomy",
    "SystemTimestamps",
    "TableSourceType",
    "TableSpec",
    "Tag",
    "TagField",
    "TagTemplate",
    "TagTemplateField",
    "Taxonomy",
    "UpdateEntryGroupRequest",
    "UpdateEntryRequest",
    "UpdatePolicyTagRequest",
    "UpdateTagRequest",
    "UpdateTagTemplateFieldRequest",
    "UpdateTagTemplateRequest",
    "UpdateTaxonomyRequest",
    "UsageSignal",
    "UsageStats",
    "ViewSpec",
)

api_core.check_python_version("google.cloud.datacatalog_v1beta1")
api_core.check_dependency_versions("google.cloud.datacatalog_v1beta1")
