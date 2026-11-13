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

from google.cloud.orchestration.airflow.service_v1beta1 import (
    gapic_version as package_version,
)

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.orchestration.airflow.service_v1beta1.services.environments",
    "google.cloud.orchestration.airflow.service_v1beta1.services.image_versions",
    "google.cloud.orchestration.airflow.service_v1beta1.types.environments",
    "google.cloud.orchestration.airflow.service_v1beta1.types.image_versions",
    "google.cloud.orchestration.airflow.service_v1beta1.types.operations",
}


from .services.environments import EnvironmentsAsyncClient, EnvironmentsClient
from .services.image_versions import ImageVersionsAsyncClient, ImageVersionsClient
from .types.environments import (
    AirflowMetadataRetentionPolicyConfig,
    CheckUpgradeRequest,
    CheckUpgradeResponse,
    CloudDataLineageIntegration,
    CreateEnvironmentRequest,
    CreateUserWorkloadsConfigMapRequest,
    CreateUserWorkloadsSecretRequest,
    DatabaseConfig,
    DatabaseFailoverRequest,
    DatabaseFailoverResponse,
    DataRetentionConfig,
    DeleteEnvironmentRequest,
    DeleteUserWorkloadsConfigMapRequest,
    DeleteUserWorkloadsSecretRequest,
    EncryptionConfig,
    Environment,
    EnvironmentConfig,
    ExecuteAirflowCommandRequest,
    ExecuteAirflowCommandResponse,
    FetchDatabasePropertiesRequest,
    FetchDatabasePropertiesResponse,
    GetEnvironmentRequest,
    GetUserWorkloadsConfigMapRequest,
    GetUserWorkloadsSecretRequest,
    IPAllocationPolicy,
    ListEnvironmentsRequest,
    ListEnvironmentsResponse,
    ListUserWorkloadsConfigMapsRequest,
    ListUserWorkloadsConfigMapsResponse,
    ListUserWorkloadsSecretsRequest,
    ListUserWorkloadsSecretsResponse,
    ListWorkloadsRequest,
    ListWorkloadsResponse,
    LoadSnapshotRequest,
    LoadSnapshotResponse,
    MaintenanceWindow,
    MasterAuthorizedNetworksConfig,
    NetworkingConfig,
    NodeConfig,
    PollAirflowCommandRequest,
    PollAirflowCommandResponse,
    PrivateClusterConfig,
    PrivateEnvironmentConfig,
    RecoveryConfig,
    RestartWebServerRequest,
    SaveSnapshotRequest,
    SaveSnapshotResponse,
    ScheduledSnapshotsConfig,
    SoftwareConfig,
    StopAirflowCommandRequest,
    StopAirflowCommandResponse,
    StorageConfig,
    TaskLogsRetentionConfig,
    UpdateEnvironmentRequest,
    UpdateUserWorkloadsConfigMapRequest,
    UpdateUserWorkloadsSecretRequest,
    UserWorkloadsConfigMap,
    UserWorkloadsSecret,
    WebServerConfig,
    WebServerNetworkAccessControl,
    WorkloadsConfig,
)
from .types.image_versions import (
    ImageVersion,
    ListImageVersionsRequest,
    ListImageVersionsResponse,
)
from .types.operations import OperationMetadata

__all__ = (
    "EnvironmentsAsyncClient",
    "ImageVersionsAsyncClient",
    "AirflowMetadataRetentionPolicyConfig",
    "CheckUpgradeRequest",
    "CheckUpgradeResponse",
    "CloudDataLineageIntegration",
    "CreateEnvironmentRequest",
    "CreateUserWorkloadsConfigMapRequest",
    "CreateUserWorkloadsSecretRequest",
    "DataRetentionConfig",
    "DatabaseConfig",
    "DatabaseFailoverRequest",
    "DatabaseFailoverResponse",
    "DeleteEnvironmentRequest",
    "DeleteUserWorkloadsConfigMapRequest",
    "DeleteUserWorkloadsSecretRequest",
    "EncryptionConfig",
    "Environment",
    "EnvironmentConfig",
    "EnvironmentsClient",
    "ExecuteAirflowCommandRequest",
    "ExecuteAirflowCommandResponse",
    "FetchDatabasePropertiesRequest",
    "FetchDatabasePropertiesResponse",
    "GetEnvironmentRequest",
    "GetUserWorkloadsConfigMapRequest",
    "GetUserWorkloadsSecretRequest",
    "IPAllocationPolicy",
    "ImageVersion",
    "ImageVersionsClient",
    "ListEnvironmentsRequest",
    "ListEnvironmentsResponse",
    "ListImageVersionsRequest",
    "ListImageVersionsResponse",
    "ListUserWorkloadsConfigMapsRequest",
    "ListUserWorkloadsConfigMapsResponse",
    "ListUserWorkloadsSecretsRequest",
    "ListUserWorkloadsSecretsResponse",
    "ListWorkloadsRequest",
    "ListWorkloadsResponse",
    "LoadSnapshotRequest",
    "LoadSnapshotResponse",
    "MaintenanceWindow",
    "MasterAuthorizedNetworksConfig",
    "NetworkingConfig",
    "NodeConfig",
    "OperationMetadata",
    "PollAirflowCommandRequest",
    "PollAirflowCommandResponse",
    "PrivateClusterConfig",
    "PrivateEnvironmentConfig",
    "RecoveryConfig",
    "RestartWebServerRequest",
    "SaveSnapshotRequest",
    "SaveSnapshotResponse",
    "ScheduledSnapshotsConfig",
    "SoftwareConfig",
    "StopAirflowCommandRequest",
    "StopAirflowCommandResponse",
    "StorageConfig",
    "TaskLogsRetentionConfig",
    "UpdateEnvironmentRequest",
    "UpdateUserWorkloadsConfigMapRequest",
    "UpdateUserWorkloadsSecretRequest",
    "UserWorkloadsConfigMap",
    "UserWorkloadsSecret",
    "WebServerConfig",
    "WebServerNetworkAccessControl",
    "WorkloadsConfig",
)

api_core.check_python_version("google.cloud.orchestration.airflow.service_v1beta1")
api_core.check_dependency_versions("google.cloud.orchestration.airflow.service_v1beta1")
