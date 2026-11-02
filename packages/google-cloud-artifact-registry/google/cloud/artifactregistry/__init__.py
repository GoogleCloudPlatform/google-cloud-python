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
from google.cloud.artifactregistry import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.artifactregistry_v1.services.artifact_registry.async_client import (
    ArtifactRegistryAsyncClient,
)
from google.cloud.artifactregistry_v1.services.artifact_registry.client import (
    ArtifactRegistryClient,
)
from google.cloud.artifactregistry_v1.types.apt_artifact import (
    AptArtifact,
    ImportAptArtifactsErrorInfo,
    ImportAptArtifactsGcsSource,
    ImportAptArtifactsMetadata,
    ImportAptArtifactsRequest,
    ImportAptArtifactsResponse,
)
from google.cloud.artifactregistry_v1.types.artifact import (
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
from google.cloud.artifactregistry_v1.types.attachment import (
    Attachment,
    CreateAttachmentRequest,
    DeleteAttachmentRequest,
    GetAttachmentRequest,
    ListAttachmentsRequest,
    ListAttachmentsResponse,
)
from google.cloud.artifactregistry_v1.types.export import (
    ExportArtifactMetadata,
    ExportArtifactRequest,
    ExportArtifactResponse,
)
from google.cloud.artifactregistry_v1.types.file import (
    DeleteFileRequest,
    File,
    GetFileRequest,
    Hash,
    ListFilesRequest,
    ListFilesResponse,
    UpdateFileRequest,
)
from google.cloud.artifactregistry_v1.types.generic import GenericArtifact
from google.cloud.artifactregistry_v1.types.go import GoModule
from google.cloud.artifactregistry_v1.types.kfp_artifact import KfpArtifact
from google.cloud.artifactregistry_v1.types.package import (
    DeletePackageRequest,
    GetPackageRequest,
    ListPackagesRequest,
    ListPackagesResponse,
    Package,
    UpdatePackageRequest,
)
from google.cloud.artifactregistry_v1.types.repository import (
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
from google.cloud.artifactregistry_v1.types.rule import (
    CreateRuleRequest,
    DeleteRuleRequest,
    GetRuleRequest,
    ListRulesRequest,
    ListRulesResponse,
    Rule,
    UpdateRuleRequest,
)
from google.cloud.artifactregistry_v1.types.service import OperationMetadata
from google.cloud.artifactregistry_v1.types.settings import (
    GetProjectSettingsRequest,
    ProjectSettings,
    UpdateProjectSettingsRequest,
)
from google.cloud.artifactregistry_v1.types.tag import (
    CreateTagRequest,
    DeleteTagRequest,
    GetTagRequest,
    ListTagsRequest,
    ListTagsResponse,
    Tag,
    UpdateTagRequest,
)
from google.cloud.artifactregistry_v1.types.version import (
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
from google.cloud.artifactregistry_v1.types.vpcsc_config import (
    GetVPCSCConfigRequest,
    UpdateVPCSCConfigRequest,
    VPCSCConfig,
)
from google.cloud.artifactregistry_v1.types.yum_artifact import (
    ImportYumArtifactsErrorInfo,
    ImportYumArtifactsGcsSource,
    ImportYumArtifactsMetadata,
    ImportYumArtifactsRequest,
    ImportYumArtifactsResponse,
    YumArtifact,
)

__all__ = (
    "ArtifactRegistryClient",
    "ArtifactRegistryAsyncClient",
    "AptArtifact",
    "ImportAptArtifactsErrorInfo",
    "ImportAptArtifactsGcsSource",
    "ImportAptArtifactsMetadata",
    "ImportAptArtifactsRequest",
    "ImportAptArtifactsResponse",
    "DockerImage",
    "GetDockerImageRequest",
    "GetMavenArtifactRequest",
    "GetNpmPackageRequest",
    "GetPythonPackageRequest",
    "ImageManifest",
    "ListDockerImagesRequest",
    "ListDockerImagesResponse",
    "ListMavenArtifactsRequest",
    "ListMavenArtifactsResponse",
    "ListNpmPackagesRequest",
    "ListNpmPackagesResponse",
    "ListPythonPackagesRequest",
    "ListPythonPackagesResponse",
    "MavenArtifact",
    "NpmPackage",
    "PythonPackage",
    "Attachment",
    "CreateAttachmentRequest",
    "DeleteAttachmentRequest",
    "GetAttachmentRequest",
    "ListAttachmentsRequest",
    "ListAttachmentsResponse",
    "ExportArtifactMetadata",
    "ExportArtifactRequest",
    "ExportArtifactResponse",
    "DeleteFileRequest",
    "File",
    "GetFileRequest",
    "Hash",
    "ListFilesRequest",
    "ListFilesResponse",
    "UpdateFileRequest",
    "GenericArtifact",
    "GoModule",
    "KfpArtifact",
    "DeletePackageRequest",
    "GetPackageRequest",
    "ListPackagesRequest",
    "ListPackagesResponse",
    "Package",
    "UpdatePackageRequest",
    "CleanupPolicy",
    "CleanupPolicyCondition",
    "CleanupPolicyMostRecentVersions",
    "CreateRepositoryRequest",
    "DeleteRepositoryRequest",
    "GetRepositoryRequest",
    "ListRepositoriesRequest",
    "ListRepositoriesResponse",
    "RemoteRepositoryConfig",
    "Repository",
    "UpdateRepositoryRequest",
    "UpstreamPolicy",
    "VirtualRepositoryConfig",
    "CreateRuleRequest",
    "DeleteRuleRequest",
    "GetRuleRequest",
    "ListRulesRequest",
    "ListRulesResponse",
    "Rule",
    "UpdateRuleRequest",
    "OperationMetadata",
    "GetProjectSettingsRequest",
    "ProjectSettings",
    "UpdateProjectSettingsRequest",
    "CreateTagRequest",
    "DeleteTagRequest",
    "GetTagRequest",
    "ListTagsRequest",
    "ListTagsResponse",
    "Tag",
    "UpdateTagRequest",
    "BatchDeleteVersionsMetadata",
    "BatchDeleteVersionsRequest",
    "DeleteVersionRequest",
    "GetVersionRequest",
    "ListVersionsRequest",
    "ListVersionsResponse",
    "UpdateVersionRequest",
    "Version",
    "VersionView",
    "GetVPCSCConfigRequest",
    "UpdateVPCSCConfigRequest",
    "VPCSCConfig",
    "ImportYumArtifactsErrorInfo",
    "ImportYumArtifactsGcsSource",
    "ImportYumArtifactsMetadata",
    "ImportYumArtifactsRequest",
    "ImportYumArtifactsResponse",
    "YumArtifact",
)
