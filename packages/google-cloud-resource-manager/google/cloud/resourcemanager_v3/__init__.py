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

from google.cloud.resourcemanager_v3 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.resourcemanager_v3.services.folders",
    "google.cloud.resourcemanager_v3.services.organizations",
    "google.cloud.resourcemanager_v3.services.projects",
    "google.cloud.resourcemanager_v3.services.tag_bindings",
    "google.cloud.resourcemanager_v3.services.tag_holds",
    "google.cloud.resourcemanager_v3.services.tag_keys",
    "google.cloud.resourcemanager_v3.services.tag_values",
    "google.cloud.resourcemanager_v3.types.folders",
    "google.cloud.resourcemanager_v3.types.organizations",
    "google.cloud.resourcemanager_v3.types.projects",
    "google.cloud.resourcemanager_v3.types.tag_bindings",
    "google.cloud.resourcemanager_v3.types.tag_holds",
    "google.cloud.resourcemanager_v3.types.tag_keys",
    "google.cloud.resourcemanager_v3.types.tag_values",
}


from .services.folders import FoldersAsyncClient, FoldersClient
from .services.organizations import OrganizationsAsyncClient, OrganizationsClient
from .services.projects import ProjectsAsyncClient, ProjectsClient
from .services.tag_bindings import TagBindingsAsyncClient, TagBindingsClient
from .services.tag_holds import TagHoldsAsyncClient, TagHoldsClient
from .services.tag_keys import TagKeysAsyncClient, TagKeysClient
from .services.tag_values import TagValuesAsyncClient, TagValuesClient
from .types.folders import (
    CreateFolderMetadata,
    CreateFolderRequest,
    DeleteFolderMetadata,
    DeleteFolderRequest,
    Folder,
    GetFolderRequest,
    ListFoldersRequest,
    ListFoldersResponse,
    MoveFolderMetadata,
    MoveFolderRequest,
    SearchFoldersRequest,
    SearchFoldersResponse,
    UndeleteFolderMetadata,
    UndeleteFolderRequest,
    UpdateFolderMetadata,
    UpdateFolderRequest,
)
from .types.organizations import (
    DeleteOrganizationMetadata,
    GetOrganizationRequest,
    Organization,
    SearchOrganizationsRequest,
    SearchOrganizationsResponse,
    UndeleteOrganizationMetadata,
)
from .types.projects import (
    CreateProjectMetadata,
    CreateProjectRequest,
    DeleteProjectMetadata,
    DeleteProjectRequest,
    GetProjectRequest,
    ListProjectsRequest,
    ListProjectsResponse,
    MoveProjectMetadata,
    MoveProjectRequest,
    Project,
    SearchProjectsRequest,
    SearchProjectsResponse,
    UndeleteProjectMetadata,
    UndeleteProjectRequest,
    UpdateProjectMetadata,
    UpdateProjectRequest,
)
from .types.tag_bindings import (
    CreateTagBindingMetadata,
    CreateTagBindingRequest,
    DeleteTagBindingMetadata,
    DeleteTagBindingRequest,
    EffectiveTag,
    ListEffectiveTagsRequest,
    ListEffectiveTagsResponse,
    ListTagBindingsRequest,
    ListTagBindingsResponse,
    TagBinding,
)
from .types.tag_holds import (
    CreateTagHoldMetadata,
    CreateTagHoldRequest,
    DeleteTagHoldMetadata,
    DeleteTagHoldRequest,
    ListTagHoldsRequest,
    ListTagHoldsResponse,
    TagHold,
)
from .types.tag_keys import (
    CreateTagKeyMetadata,
    CreateTagKeyRequest,
    DeleteTagKeyMetadata,
    DeleteTagKeyRequest,
    GetNamespacedTagKeyRequest,
    GetTagKeyRequest,
    ListTagKeysRequest,
    ListTagKeysResponse,
    Purpose,
    TagKey,
    UpdateTagKeyMetadata,
    UpdateTagKeyRequest,
)
from .types.tag_values import (
    CreateTagValueMetadata,
    CreateTagValueRequest,
    DeleteTagValueMetadata,
    DeleteTagValueRequest,
    GetNamespacedTagValueRequest,
    GetTagValueRequest,
    ListTagValuesRequest,
    ListTagValuesResponse,
    TagValue,
    UpdateTagValueMetadata,
    UpdateTagValueRequest,
)

__all__ = (
    "FoldersAsyncClient",
    "OrganizationsAsyncClient",
    "ProjectsAsyncClient",
    "TagBindingsAsyncClient",
    "TagHoldsAsyncClient",
    "TagKeysAsyncClient",
    "TagValuesAsyncClient",
    "CreateFolderMetadata",
    "CreateFolderRequest",
    "CreateProjectMetadata",
    "CreateProjectRequest",
    "CreateTagBindingMetadata",
    "CreateTagBindingRequest",
    "CreateTagHoldMetadata",
    "CreateTagHoldRequest",
    "CreateTagKeyMetadata",
    "CreateTagKeyRequest",
    "CreateTagValueMetadata",
    "CreateTagValueRequest",
    "DeleteFolderMetadata",
    "DeleteFolderRequest",
    "DeleteOrganizationMetadata",
    "DeleteProjectMetadata",
    "DeleteProjectRequest",
    "DeleteTagBindingMetadata",
    "DeleteTagBindingRequest",
    "DeleteTagHoldMetadata",
    "DeleteTagHoldRequest",
    "DeleteTagKeyMetadata",
    "DeleteTagKeyRequest",
    "DeleteTagValueMetadata",
    "DeleteTagValueRequest",
    "EffectiveTag",
    "Folder",
    "FoldersClient",
    "GetFolderRequest",
    "GetNamespacedTagKeyRequest",
    "GetNamespacedTagValueRequest",
    "GetOrganizationRequest",
    "GetProjectRequest",
    "GetTagKeyRequest",
    "GetTagValueRequest",
    "ListEffectiveTagsRequest",
    "ListEffectiveTagsResponse",
    "ListFoldersRequest",
    "ListFoldersResponse",
    "ListProjectsRequest",
    "ListProjectsResponse",
    "ListTagBindingsRequest",
    "ListTagBindingsResponse",
    "ListTagHoldsRequest",
    "ListTagHoldsResponse",
    "ListTagKeysRequest",
    "ListTagKeysResponse",
    "ListTagValuesRequest",
    "ListTagValuesResponse",
    "MoveFolderMetadata",
    "MoveFolderRequest",
    "MoveProjectMetadata",
    "MoveProjectRequest",
    "Organization",
    "OrganizationsClient",
    "Project",
    "ProjectsClient",
    "Purpose",
    "SearchFoldersRequest",
    "SearchFoldersResponse",
    "SearchOrganizationsRequest",
    "SearchOrganizationsResponse",
    "SearchProjectsRequest",
    "SearchProjectsResponse",
    "TagBinding",
    "TagBindingsClient",
    "TagHold",
    "TagHoldsClient",
    "TagKey",
    "TagKeysClient",
    "TagValue",
    "TagValuesClient",
    "UndeleteFolderMetadata",
    "UndeleteFolderRequest",
    "UndeleteOrganizationMetadata",
    "UndeleteProjectMetadata",
    "UndeleteProjectRequest",
    "UpdateFolderMetadata",
    "UpdateFolderRequest",
    "UpdateProjectMetadata",
    "UpdateProjectRequest",
    "UpdateTagKeyMetadata",
    "UpdateTagKeyRequest",
    "UpdateTagValueMetadata",
    "UpdateTagValueRequest",
)

api_core.check_python_version("google.cloud.resourcemanager_v3")
api_core.check_dependency_versions("google.cloud.resourcemanager_v3")
