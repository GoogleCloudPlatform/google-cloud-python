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

from google.cloud.devtools.cloudbuild_v1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.devtools.cloudbuild_v1.services.cloud_build",
    "google.cloud.devtools.cloudbuild_v1.types.cloudbuild",
}


from .services.cloud_build import CloudBuildAsyncClient, CloudBuildClient
from .types.cloudbuild import (
    ApprovalConfig,
    ApprovalResult,
    ApproveBuildRequest,
    ArtifactResult,
    Artifacts,
    Build,
    BuildApproval,
    BuildOperationMetadata,
    BuildOptions,
    BuildStep,
    BuildTrigger,
    BuiltImage,
    CancelBuildRequest,
    ConnectedRepository,
    CreateBuildRequest,
    CreateBuildTriggerRequest,
    CreateWorkerPoolOperationMetadata,
    CreateWorkerPoolRequest,
    DefaultServiceAccount,
    DeleteBuildTriggerRequest,
    DeleteWorkerPoolOperationMetadata,
    DeleteWorkerPoolRequest,
    Dependency,
    FileHashes,
    GetBuildRequest,
    GetBuildTriggerRequest,
    GetDefaultServiceAccountRequest,
    GetWorkerPoolRequest,
    GitConfig,
    GitFileSource,
    GitHubEnterpriseConfig,
    GitHubEnterpriseSecrets,
    GitHubEventsConfig,
    GitRepoSource,
    GitSource,
    Hash,
    InlineSecret,
    ListBuildsRequest,
    ListBuildsResponse,
    ListBuildTriggersRequest,
    ListBuildTriggersResponse,
    ListWorkerPoolsRequest,
    ListWorkerPoolsResponse,
    PrivatePoolV1Config,
    PubsubConfig,
    PullRequestFilter,
    PushFilter,
    ReceiveTriggerWebhookRequest,
    ReceiveTriggerWebhookResponse,
    RepositoryEventConfig,
    RepoSource,
    Results,
    RetryBuildRequest,
    RunBuildTriggerRequest,
    Secret,
    SecretManagerSecret,
    Secrets,
    Source,
    SourceProvenance,
    StorageSource,
    StorageSourceManifest,
    TimeSpan,
    UpdateBuildTriggerRequest,
    UpdateWorkerPoolOperationMetadata,
    UpdateWorkerPoolRequest,
    UploadedGoModule,
    UploadedMavenArtifact,
    UploadedNpmPackage,
    UploadedPythonPackage,
    Volume,
    WebhookConfig,
    WorkerPool,
)

__all__ = (
    "CloudBuildAsyncClient",
    "ApprovalConfig",
    "ApprovalResult",
    "ApproveBuildRequest",
    "ArtifactResult",
    "Artifacts",
    "Build",
    "BuildApproval",
    "BuildOperationMetadata",
    "BuildOptions",
    "BuildStep",
    "BuildTrigger",
    "BuiltImage",
    "CancelBuildRequest",
    "CloudBuildClient",
    "ConnectedRepository",
    "CreateBuildRequest",
    "CreateBuildTriggerRequest",
    "CreateWorkerPoolOperationMetadata",
    "CreateWorkerPoolRequest",
    "DefaultServiceAccount",
    "DeleteBuildTriggerRequest",
    "DeleteWorkerPoolOperationMetadata",
    "DeleteWorkerPoolRequest",
    "Dependency",
    "FileHashes",
    "GetBuildRequest",
    "GetBuildTriggerRequest",
    "GetDefaultServiceAccountRequest",
    "GetWorkerPoolRequest",
    "GitConfig",
    "GitFileSource",
    "GitHubEnterpriseConfig",
    "GitHubEnterpriseSecrets",
    "GitHubEventsConfig",
    "GitRepoSource",
    "GitSource",
    "Hash",
    "InlineSecret",
    "ListBuildTriggersRequest",
    "ListBuildTriggersResponse",
    "ListBuildsRequest",
    "ListBuildsResponse",
    "ListWorkerPoolsRequest",
    "ListWorkerPoolsResponse",
    "PrivatePoolV1Config",
    "PubsubConfig",
    "PullRequestFilter",
    "PushFilter",
    "ReceiveTriggerWebhookRequest",
    "ReceiveTriggerWebhookResponse",
    "RepoSource",
    "RepositoryEventConfig",
    "Results",
    "RetryBuildRequest",
    "RunBuildTriggerRequest",
    "Secret",
    "SecretManagerSecret",
    "Secrets",
    "Source",
    "SourceProvenance",
    "StorageSource",
    "StorageSourceManifest",
    "TimeSpan",
    "UpdateBuildTriggerRequest",
    "UpdateWorkerPoolOperationMetadata",
    "UpdateWorkerPoolRequest",
    "UploadedGoModule",
    "UploadedMavenArtifact",
    "UploadedNpmPackage",
    "UploadedPythonPackage",
    "Volume",
    "WebhookConfig",
    "WorkerPool",
)

api_core.check_python_version("google.cloud.devtools.cloudbuild_v1")
api_core.check_dependency_versions("google.cloud.devtools.cloudbuild_v1")
