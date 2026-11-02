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

from google.cloud.artifactregistry_v1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.artifactregistry_v1.services.artifact_registry",
    "google.cloud.artifactregistry_v1.types.apt_artifact",
    "google.cloud.artifactregistry_v1.types.artifact",
    "google.cloud.artifactregistry_v1.types.attachment",
    "google.cloud.artifactregistry_v1.types.export",
    "google.cloud.artifactregistry_v1.types.file",
    "google.cloud.artifactregistry_v1.types.generic",
    "google.cloud.artifactregistry_v1.types.go",
    "google.cloud.artifactregistry_v1.types.kfp_artifact",
    "google.cloud.artifactregistry_v1.types.package",
    "google.cloud.artifactregistry_v1.types.repository",
    "google.cloud.artifactregistry_v1.types.rule",
    "google.cloud.artifactregistry_v1.types.service",
    "google.cloud.artifactregistry_v1.types.settings",
    "google.cloud.artifactregistry_v1.types.tag",
    "google.cloud.artifactregistry_v1.types.version",
    "google.cloud.artifactregistry_v1.types.vpcsc_config",
    "google.cloud.artifactregistry_v1.types.yum_artifact",
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
from .types.artifact import (
    DockerImage,
    GetDockerImageRequest,
    GetMavenArtifactRequest,
    GetNpmPackageRequest,
    GetPythonPackageRequest,
    ImageManifest,
    ListDockerImagesRequest,
    ListDockerImagesResponse,
    ListMavenArtifactsRequest,
    ListMavenArtifactsResponse,
    ListNpmPackagesRequest,
    ListNpmPackagesResponse,
    ListPythonPackagesRequest,
    ListPythonPackagesResponse,
    MavenArtifact,
    NpmPackage,
    PythonPackage,
)
from .types.attachment import (
    Attachment,
    CreateAttachmentRequest,
    DeleteAttachmentRequest,
    GetAttachmentRequest,
    ListAttachmentsRequest,
    ListAttachmentsResponse,
)
from .types.export import (
    ExportArtifactMetadata,
    ExportArtifactRequest,
    ExportArtifactResponse,
)
from .types.file import (
    DeleteFileRequest,
    File,
    GetFileRequest,
    Hash,
    ListFilesRequest,
    ListFilesResponse,
    UpdateFileRequest,
)
from .types.generic import GenericArtifact
from .types.go import GoModule
from .types.kfp_artifact import KfpArtifact
from .types.package import (
    DeletePackageRequest,
    GetPackageRequest,
    ListPackagesRequest,
    ListPackagesResponse,
    Package,
    UpdatePackageRequest,
)
from .types.repository import (
    CleanupPolicy,
    CleanupPolicyCondition,
    CleanupPolicyMostRecentVersions,
    CreateRepositoryRequest,
    DeleteRepositoryRequest,
    GetRepositoryRequest,
    ListRepositoriesRequest,
    ListRepositoriesResponse,
    RemoteRepositoryConfig,
    Repository,
    UpdateRepositoryRequest,
    UpstreamPolicy,
    VirtualRepositoryConfig,
)
from .types.rule import (
    CreateRuleRequest,
    DeleteRuleRequest,
    GetRuleRequest,
    ListRulesRequest,
    ListRulesResponse,
    Rule,
    UpdateRuleRequest,
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
    BatchDeleteVersionsMetadata,
    BatchDeleteVersionsRequest,
    DeleteVersionRequest,
    GetVersionRequest,
    ListVersionsRequest,
    ListVersionsResponse,
    UpdateVersionRequest,
    Version,
    VersionView,
)
from .types.vpcsc_config import (
    GetVPCSCConfigRequest,
    UpdateVPCSCConfigRequest,
    VPCSCConfig,
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
    "Attachment",
    "BatchDeleteVersionsMetadata",
    "BatchDeleteVersionsRequest",
    "CleanupPolicy",
    "CleanupPolicyCondition",
    "CleanupPolicyMostRecentVersions",
    "CreateAttachmentRequest",
    "CreateRepositoryRequest",
    "CreateRuleRequest",
    "CreateTagRequest",
    "DeleteAttachmentRequest",
    "DeleteFileRequest",
    "DeletePackageRequest",
    "DeleteRepositoryRequest",
    "DeleteRuleRequest",
    "DeleteTagRequest",
    "DeleteVersionRequest",
    "DockerImage",
    "ExportArtifactMetadata",
    "ExportArtifactRequest",
    "ExportArtifactResponse",
    "File",
    "GenericArtifact",
    "GetAttachmentRequest",
    "GetDockerImageRequest",
    "GetFileRequest",
    "GetMavenArtifactRequest",
    "GetNpmPackageRequest",
    "GetPackageRequest",
    "GetProjectSettingsRequest",
    "GetPythonPackageRequest",
    "GetRepositoryRequest",
    "GetRuleRequest",
    "GetTagRequest",
    "GetVPCSCConfigRequest",
    "GetVersionRequest",
    "GoModule",
    "Hash",
    "ImageManifest",
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
    "KfpArtifact",
    "ListAttachmentsRequest",
    "ListAttachmentsResponse",
    "ListDockerImagesRequest",
    "ListDockerImagesResponse",
    "ListFilesRequest",
    "ListFilesResponse",
    "ListMavenArtifactsRequest",
    "ListMavenArtifactsResponse",
    "ListNpmPackagesRequest",
    "ListNpmPackagesResponse",
    "ListPackagesRequest",
    "ListPackagesResponse",
    "ListPythonPackagesRequest",
    "ListPythonPackagesResponse",
    "ListRepositoriesRequest",
    "ListRepositoriesResponse",
    "ListRulesRequest",
    "ListRulesResponse",
    "ListTagsRequest",
    "ListTagsResponse",
    "ListVersionsRequest",
    "ListVersionsResponse",
    "MavenArtifact",
    "NpmPackage",
    "OperationMetadata",
    "Package",
    "ProjectSettings",
    "PythonPackage",
    "RemoteRepositoryConfig",
    "Repository",
    "Rule",
    "Tag",
    "UpdateFileRequest",
    "UpdatePackageRequest",
    "UpdateProjectSettingsRequest",
    "UpdateRepositoryRequest",
    "UpdateRuleRequest",
    "UpdateTagRequest",
    "UpdateVPCSCConfigRequest",
    "UpdateVersionRequest",
    "UpstreamPolicy",
    "VPCSCConfig",
    "Version",
    "VersionView",
    "VirtualRepositoryConfig",
    "YumArtifact",
)

api_core.check_python_version("google.cloud.artifactregistry_v1")
api_core.check_dependency_versions("google.cloud.artifactregistry_v1")
