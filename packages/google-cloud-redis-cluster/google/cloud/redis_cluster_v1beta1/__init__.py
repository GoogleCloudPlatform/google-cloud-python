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

from google.cloud.redis_cluster_v1beta1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster",
    "google.cloud.redis_cluster_v1beta1.types.cloud_redis_cluster",
}


from .services.cloud_redis_cluster import (
    CloudRedisClusterAsyncClient,
    CloudRedisClusterClient,
)
from .types.cloud_redis_cluster import (
    AclPolicy,
    AclPolicyInfo,
    AclPolicyRevision,
    AclPolicyRevisionStatus,
    AclRule,
    AddAuthTokenRequest,
    AddTokenAuthUserRequest,
    AuthorizationMode,
    AuthToken,
    AutomatedBackupConfig,
    Backup,
    BackupClusterRequest,
    BackupCollection,
    BackupFile,
    CertificateAuthority,
    Cluster,
    ClusterAclPolicyAttachment,
    ClusterEndpoint,
    ClusterMaintenancePolicy,
    ClusterMaintenanceSchedule,
    ClusterPersistenceConfig,
    ClusterWeeklyMaintenanceWindow,
    ConnectionDetail,
    ConnectionType,
    CreateAclPolicyRequest,
    CreateClusterRequest,
    CrossClusterReplicationConfig,
    DeleteAclPolicyRequest,
    DeleteAuthTokenRequest,
    DeleteBackupRequest,
    DeleteClusterRequest,
    DeleteTokenAuthUserRequest,
    DiscoveryEndpoint,
    EncryptionInfo,
    ExportBackupRequest,
    GetAclPolicyRequest,
    GetAclPolicyRevisionRequest,
    GetAuthTokenRequest,
    GetBackupCollectionRequest,
    GetBackupRequest,
    GetClusterCertificateAuthorityRequest,
    GetClusterRequest,
    GetSharedRegionalCertificateAuthorityRequest,
    GetTokenAuthUserRequest,
    ListAclPoliciesRequest,
    ListAclPoliciesResponse,
    ListAclPolicyRevisionsRequest,
    ListAclPolicyRevisionsResponse,
    ListAuthTokensRequest,
    ListAuthTokensResponse,
    ListBackupCollectionsRequest,
    ListBackupCollectionsResponse,
    ListBackupsRequest,
    ListBackupsResponse,
    ListClustersRequest,
    ListClustersResponse,
    ListTokenAuthUsersRequest,
    ListTokenAuthUsersResponse,
    NodeType,
    OperationMetadata,
    PscAutoConnection,
    PscConfig,
    PscConnection,
    PscConnectionStatus,
    PscServiceAttachment,
    RescheduleClusterMaintenanceRequest,
    ServerCaMode,
    SharedRegionalCertificateAuthority,
    TokenAuthUser,
    TransitEncryptionMode,
    UpdateAclPolicyRequest,
    UpdateClusterRequest,
    ZoneDistributionConfig,
)

__all__ = (
    "CloudRedisClusterAsyncClient",
    "AclPolicy",
    "AclPolicyInfo",
    "AclPolicyRevision",
    "AclPolicyRevisionStatus",
    "AclRule",
    "AddAuthTokenRequest",
    "AddTokenAuthUserRequest",
    "AuthToken",
    "AuthorizationMode",
    "AutomatedBackupConfig",
    "Backup",
    "BackupClusterRequest",
    "BackupCollection",
    "BackupFile",
    "CertificateAuthority",
    "CloudRedisClusterClient",
    "Cluster",
    "ClusterAclPolicyAttachment",
    "ClusterEndpoint",
    "ClusterMaintenancePolicy",
    "ClusterMaintenanceSchedule",
    "ClusterPersistenceConfig",
    "ClusterWeeklyMaintenanceWindow",
    "ConnectionDetail",
    "ConnectionType",
    "CreateAclPolicyRequest",
    "CreateClusterRequest",
    "CrossClusterReplicationConfig",
    "DeleteAclPolicyRequest",
    "DeleteAuthTokenRequest",
    "DeleteBackupRequest",
    "DeleteClusterRequest",
    "DeleteTokenAuthUserRequest",
    "DiscoveryEndpoint",
    "EncryptionInfo",
    "ExportBackupRequest",
    "GetAclPolicyRequest",
    "GetAclPolicyRevisionRequest",
    "GetAuthTokenRequest",
    "GetBackupCollectionRequest",
    "GetBackupRequest",
    "GetClusterCertificateAuthorityRequest",
    "GetClusterRequest",
    "GetSharedRegionalCertificateAuthorityRequest",
    "GetTokenAuthUserRequest",
    "ListAclPoliciesRequest",
    "ListAclPoliciesResponse",
    "ListAclPolicyRevisionsRequest",
    "ListAclPolicyRevisionsResponse",
    "ListAuthTokensRequest",
    "ListAuthTokensResponse",
    "ListBackupCollectionsRequest",
    "ListBackupCollectionsResponse",
    "ListBackupsRequest",
    "ListBackupsResponse",
    "ListClustersRequest",
    "ListClustersResponse",
    "ListTokenAuthUsersRequest",
    "ListTokenAuthUsersResponse",
    "NodeType",
    "OperationMetadata",
    "PscAutoConnection",
    "PscConfig",
    "PscConnection",
    "PscConnectionStatus",
    "PscServiceAttachment",
    "RescheduleClusterMaintenanceRequest",
    "ServerCaMode",
    "SharedRegionalCertificateAuthority",
    "TokenAuthUser",
    "TransitEncryptionMode",
    "UpdateAclPolicyRequest",
    "UpdateClusterRequest",
    "ZoneDistributionConfig",
)

api_core.check_python_version("google.cloud.redis_cluster_v1beta1")
api_core.check_dependency_versions("google.cloud.redis_cluster_v1beta1")
