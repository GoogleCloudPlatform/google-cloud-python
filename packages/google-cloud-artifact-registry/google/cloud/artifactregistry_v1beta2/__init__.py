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

from google.cloud.artifactregistry_v1beta2 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.artifactregistry_v1beta2.services.artifact_registry",
    "google.cloud.artifactregistry_v1beta2.types.apt_artifact",
    "google.cloud.artifactregistry_v1beta2.types.file",
    "google.cloud.artifactregistry_v1beta2.types.package",
    "google.cloud.artifactregistry_v1beta2.types.repository",
    "google.cloud.artifactregistry_v1beta2.types.service",
    "google.cloud.artifactregistry_v1beta2.types.settings",
    "google.cloud.artifactregistry_v1beta2.types.tag",
    "google.cloud.artifactregistry_v1beta2.types.version",
    "google.cloud.artifactregistry_v1beta2.types.yum_artifact",
}


from .services.artifact_registry import (
    ArtifactRegistryAsyncClient,
    ArtifactRegistryClient,
)
from .types.apt_artifact import (
    AptArtifact,
    ImportAptArtifactsErrorInfo,
    ImportAptArtifactsGcsSource,
    ImportAptArtifactsMetadata,
    ImportAptArtifactsRequest,
    ImportAptArtifactsResponse,
)
from .types.file import File, GetFileRequest, Hash, ListFilesRequest, ListFilesResponse
from .types.package import (
    DeletePackageRequest,
    GetPackageRequest,
    ListPackagesRequest,
    ListPackagesResponse,
    Package,
)
from .types.repository import (
    CreateRepositoryRequest,
    DeleteRepositoryRequest,
    GetRepositoryRequest,
    ListRepositoriesRequest,
    ListRepositoriesResponse,
    Repository,
    UpdateRepositoryRequest,
)
from .types.service import OperationMetadata
from .types.settings import (
    GetProjectSettingsRequest,
    ProjectSettings,
    UpdateProjectSettingsRequest,
)
from .types.tag import (
    CreateTagRequest,
    DeleteTagRequest,
    GetTagRequest,
    ListTagsRequest,
    ListTagsResponse,
    Tag,
    UpdateTagRequest,
)
from .types.version import (
    DeleteVersionRequest,
    GetVersionRequest,
    ListVersionsRequest,
    ListVersionsResponse,
    Version,
    VersionView,
)
from .types.yum_artifact import (
    ImportYumArtifactsErrorInfo,
    ImportYumArtifactsGcsSource,
    ImportYumArtifactsMetadata,
    ImportYumArtifactsRequest,
    ImportYumArtifactsResponse,
    YumArtifact,
)

__all__ = (
    "ArtifactRegistryAsyncClient",
    "AptArtifact",
    "ArtifactRegistryClient",
    "CreateRepositoryRequest",
    "CreateTagRequest",
    "DeletePackageRequest",
    "DeleteRepositoryRequest",
    "DeleteTagRequest",
    "DeleteVersionRequest",
    "File",
    "GetFileRequest",
    "GetPackageRequest",
    "GetProjectSettingsRequest",
    "GetRepositoryRequest",
    "GetTagRequest",
    "GetVersionRequest",
    "Hash",
    "ImportAptArtifactsErrorInfo",
    "ImportAptArtifactsGcsSource",
    "ImportAptArtifactsMetadata",
    "ImportAptArtifactsRequest",
    "ImportAptArtifactsResponse",
    "ImportYumArtifactsErrorInfo",
    "ImportYumArtifactsGcsSource",
    "ImportYumArtifactsMetadata",
    "ImportYumArtifactsRequest",
    "ImportYumArtifactsResponse",
    "ListFilesRequest",
    "ListFilesResponse",
    "ListPackagesRequest",
    "ListPackagesResponse",
    "ListRepositoriesRequest",
    "ListRepositoriesResponse",
    "ListTagsRequest",
    "ListTagsResponse",
    "ListVersionsRequest",
    "ListVersionsResponse",
    "OperationMetadata",
    "Package",
    "ProjectSettings",
    "Repository",
    "Tag",
    "UpdateProjectSettingsRequest",
    "UpdateRepositoryRequest",
    "UpdateTagRequest",
    "Version",
    "VersionView",
    "YumArtifact",
)

api_core.check_python_version("google.cloud.artifactregistry_v1beta2")
api_core.check_dependency_versions("google.cloud.artifactregistry_v1beta2")
