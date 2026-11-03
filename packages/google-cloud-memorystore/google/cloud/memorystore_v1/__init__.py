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

from google.cloud.memorystore_v1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.memorystore_v1.services.memorystore",
    "google.cloud.memorystore_v1.types.memorystore",
}


from .services.memorystore import MemorystoreAsyncClient, MemorystoreClient
from .types.memorystore import (
    AclPolicy,
    AclPolicyInfo,
    AclPolicyRevision,
    AclPolicyRevisionStatus,
    AclRule,
    AddAuthTokenRequest,
    AddTokenAuthUserRequest,
    AuthToken,
    AutomatedBackupConfig,
    Backup,
    BackupCollection,
    BackupFile,
    BackupInstanceRequest,
    CertificateAuthority,
    ConnectionType,
    CreateAclPolicyRequest,
    CreateInstanceRequest,
    CrossInstanceReplicationConfig,
    DeleteAclPolicyRequest,
    DeleteAuthTokenRequest,
    DeleteBackupRequest,
    DeleteInstanceRequest,
    DeleteTokenAuthUserRequest,
    DiscoveryEndpoint,
    EncryptionInfo,
    ExportBackupRequest,
    FinishMigrationRequest,
    GetAclPolicyRequest,
    GetAclPolicyRevisionRequest,
    GetAuthTokenRequest,
    GetBackupCollectionRequest,
    GetBackupRequest,
    GetCertificateAuthorityRequest,
    GetInstanceRequest,
    GetSharedRegionalCertificateAuthorityRequest,
    GetTokenAuthUserRequest,
    Instance,
    InstanceAclPolicyAttachment,
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
    ListInstancesRequest,
    ListInstancesResponse,
    ListTokenAuthUsersRequest,
    ListTokenAuthUsersResponse,
    MaintenancePolicy,
    MaintenanceSchedule,
    MigrationConfig,
    NodeConfig,
    OperationMetadata,
    PersistenceConfig,
    PscAttachmentDetail,
    PscAutoConnection,
    PscConnection,
    PscConnectionStatus,
    RescheduleMaintenanceRequest,
    SelfManagedSource,
    SharedRegionalCertificateAuthority,
    StartMigrationRequest,
    TokenAuthUser,
    UpdateAclPolicyRequest,
    UpdateInstanceRequest,
    WeeklyMaintenanceWindow,
    ZoneDistributionConfig,
)

__all__ = (
    "MemorystoreAsyncClient",
    "AclPolicy",
    "AclPolicyInfo",
    "AclPolicyRevision",
    "AclPolicyRevisionStatus",
    "AclRule",
    "AddAuthTokenRequest",
    "AddTokenAuthUserRequest",
    "AuthToken",
    "AutomatedBackupConfig",
    "Backup",
    "BackupCollection",
    "BackupFile",
    "BackupInstanceRequest",
    "CertificateAuthority",
    "ConnectionType",
    "CreateAclPolicyRequest",
    "CreateInstanceRequest",
    "CrossInstanceReplicationConfig",
    "DeleteAclPolicyRequest",
    "DeleteAuthTokenRequest",
    "DeleteBackupRequest",
    "DeleteInstanceRequest",
    "DeleteTokenAuthUserRequest",
    "DiscoveryEndpoint",
    "EncryptionInfo",
    "ExportBackupRequest",
    "FinishMigrationRequest",
    "GetAclPolicyRequest",
    "GetAclPolicyRevisionRequest",
    "GetAuthTokenRequest",
    "GetBackupCollectionRequest",
    "GetBackupRequest",
    "GetCertificateAuthorityRequest",
    "GetInstanceRequest",
    "GetSharedRegionalCertificateAuthorityRequest",
    "GetTokenAuthUserRequest",
    "Instance",
    "InstanceAclPolicyAttachment",
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
    "ListInstancesRequest",
    "ListInstancesResponse",
    "ListTokenAuthUsersRequest",
    "ListTokenAuthUsersResponse",
    "MaintenancePolicy",
    "MaintenanceSchedule",
    "MemorystoreClient",
    "MigrationConfig",
    "NodeConfig",
    "OperationMetadata",
    "PersistenceConfig",
    "PscAttachmentDetail",
    "PscAutoConnection",
    "PscConnection",
    "PscConnectionStatus",
    "RescheduleMaintenanceRequest",
    "SelfManagedSource",
    "SharedRegionalCertificateAuthority",
    "StartMigrationRequest",
    "TokenAuthUser",
    "UpdateAclPolicyRequest",
    "UpdateInstanceRequest",
    "WeeklyMaintenanceWindow",
    "ZoneDistributionConfig",
)

api_core.check_python_version("google.cloud.memorystore_v1")
api_core.check_dependency_versions("google.cloud.memorystore_v1")
