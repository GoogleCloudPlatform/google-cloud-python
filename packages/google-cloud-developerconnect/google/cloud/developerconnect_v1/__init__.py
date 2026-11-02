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

from google.cloud.developerconnect_v1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.developerconnect_v1.services.developer_connect",
    "google.cloud.developerconnect_v1.services.insights_config_service",
    "google.cloud.developerconnect_v1.types.developer_connect",
    "google.cloud.developerconnect_v1.types.insights_config",
}


from .services.developer_connect import (
    DeveloperConnectAsyncClient,
    DeveloperConnectClient,
)
from .services.insights_config_service import (
    InsightsConfigServiceAsyncClient,
    InsightsConfigServiceClient,
)
from .types.developer_connect import (
    AccountConnector,
    BitbucketCloudConfig,
    BitbucketDataCenterConfig,
    Connection,
    CreateAccountConnectorRequest,
    CreateConnectionRequest,
    CreateGitRepositoryLinkRequest,
    CryptoKeyConfig,
    DeleteAccountConnectorRequest,
    DeleteConnectionRequest,
    DeleteGitRepositoryLinkRequest,
    DeleteSelfRequest,
    DeleteUserRequest,
    ExchangeError,
    FetchAccessTokenRequest,
    FetchAccessTokenResponse,
    FetchGitHubInstallationsRequest,
    FetchGitHubInstallationsResponse,
    FetchGitRefsRequest,
    FetchGitRefsResponse,
    FetchLinkableGitRepositoriesRequest,
    FetchLinkableGitRepositoriesResponse,
    FetchReadTokenRequest,
    FetchReadTokenResponse,
    FetchReadWriteTokenRequest,
    FetchReadWriteTokenResponse,
    FetchSelfRequest,
    FinishOAuthRequest,
    FinishOAuthResponse,
    GenericHTTPEndpointConfig,
    GetAccountConnectorRequest,
    GetConnectionRequest,
    GetGitRepositoryLinkRequest,
    GitHubConfig,
    GitHubEnterpriseConfig,
    GitLabConfig,
    GitLabEnterpriseConfig,
    GitProxyConfig,
    GitRepositoryLink,
    InstallationState,
    LinkableGitRepository,
    ListAccountConnectorsRequest,
    ListAccountConnectorsResponse,
    ListConnectionsRequest,
    ListConnectionsResponse,
    ListGitRepositoryLinksRequest,
    ListGitRepositoryLinksResponse,
    ListUsersRequest,
    ListUsersResponse,
    OAuthCredential,
    OperationMetadata,
    ProviderOAuthConfig,
    SecureSourceManagerInstanceConfig,
    ServiceDirectoryConfig,
    StartOAuthRequest,
    StartOAuthResponse,
    SystemProvider,
    UpdateAccountConnectorRequest,
    UpdateConnectionRequest,
    User,
    UserCredential,
)
from .types.insights_config import (
    AppHubService,
    AppHubWorkload,
    ArtifactConfig,
    ArtifactDeployment,
    CreateInsightsConfigRequest,
    DeleteInsightsConfigRequest,
    DeploymentEvent,
    GetDeploymentEventRequest,
    GetInsightsConfigRequest,
    GKEWorkload,
    GoogleArtifactAnalysis,
    GoogleArtifactRegistry,
    GoogleCloudRun,
    InsightsConfig,
    ListDeploymentEventsRequest,
    ListDeploymentEventsResponse,
    ListInsightsConfigsRequest,
    ListInsightsConfigsResponse,
    Projects,
    RuntimeConfig,
    UpdateInsightsConfigRequest,
)

__all__ = (
    "DeveloperConnectAsyncClient",
    "InsightsConfigServiceAsyncClient",
    "AccountConnector",
    "AppHubService",
    "AppHubWorkload",
    "ArtifactConfig",
    "ArtifactDeployment",
    "BitbucketCloudConfig",
    "BitbucketDataCenterConfig",
    "Connection",
    "CreateAccountConnectorRequest",
    "CreateConnectionRequest",
    "CreateGitRepositoryLinkRequest",
    "CreateInsightsConfigRequest",
    "CryptoKeyConfig",
    "DeleteAccountConnectorRequest",
    "DeleteConnectionRequest",
    "DeleteGitRepositoryLinkRequest",
    "DeleteInsightsConfigRequest",
    "DeleteSelfRequest",
    "DeleteUserRequest",
    "DeploymentEvent",
    "DeveloperConnectClient",
    "ExchangeError",
    "FetchAccessTokenRequest",
    "FetchAccessTokenResponse",
    "FetchGitHubInstallationsRequest",
    "FetchGitHubInstallationsResponse",
    "FetchGitRefsRequest",
    "FetchGitRefsResponse",
    "FetchLinkableGitRepositoriesRequest",
    "FetchLinkableGitRepositoriesResponse",
    "FetchReadTokenRequest",
    "FetchReadTokenResponse",
    "FetchReadWriteTokenRequest",
    "FetchReadWriteTokenResponse",
    "FetchSelfRequest",
    "FinishOAuthRequest",
    "FinishOAuthResponse",
    "GKEWorkload",
    "GenericHTTPEndpointConfig",
    "GetAccountConnectorRequest",
    "GetConnectionRequest",
    "GetDeploymentEventRequest",
    "GetGitRepositoryLinkRequest",
    "GetInsightsConfigRequest",
    "GitHubConfig",
    "GitHubEnterpriseConfig",
    "GitLabConfig",
    "GitLabEnterpriseConfig",
    "GitProxyConfig",
    "GitRepositoryLink",
    "GoogleArtifactAnalysis",
    "GoogleArtifactRegistry",
    "GoogleCloudRun",
    "InsightsConfig",
    "InsightsConfigServiceClient",
    "InstallationState",
    "LinkableGitRepository",
    "ListAccountConnectorsRequest",
    "ListAccountConnectorsResponse",
    "ListConnectionsRequest",
    "ListConnectionsResponse",
    "ListDeploymentEventsRequest",
    "ListDeploymentEventsResponse",
    "ListGitRepositoryLinksRequest",
    "ListGitRepositoryLinksResponse",
    "ListInsightsConfigsRequest",
    "ListInsightsConfigsResponse",
    "ListUsersRequest",
    "ListUsersResponse",
    "OAuthCredential",
    "OperationMetadata",
    "Projects",
    "ProviderOAuthConfig",
    "RuntimeConfig",
    "SecureSourceManagerInstanceConfig",
    "ServiceDirectoryConfig",
    "StartOAuthRequest",
    "StartOAuthResponse",
    "SystemProvider",
    "UpdateAccountConnectorRequest",
    "UpdateConnectionRequest",
    "UpdateInsightsConfigRequest",
    "User",
    "UserCredential",
)

api_core.check_python_version("google.cloud.developerconnect_v1")
api_core.check_dependency_versions("google.cloud.developerconnect_v1")
