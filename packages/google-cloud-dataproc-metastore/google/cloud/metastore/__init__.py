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
from google.cloud.metastore import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.metastore_v1.services.dataproc_metastore.async_client import (
    DataprocMetastoreAsyncClient,
)
from google.cloud.metastore_v1.services.dataproc_metastore.client import (
    DataprocMetastoreClient,
)
from google.cloud.metastore_v1.services.dataproc_metastore_federation.async_client import (
    DataprocMetastoreFederationAsyncClient,
)
from google.cloud.metastore_v1.services.dataproc_metastore_federation.client import (
    DataprocMetastoreFederationClient,
)
from google.cloud.metastore_v1.types.metastore import (
    AlterMetadataResourceLocationRequest,
    AlterMetadataResourceLocationResponse,
    AuxiliaryVersionConfig,
    Backup,
    CreateBackupRequest,
    CreateMetadataImportRequest,
    CreateServiceRequest,
    DatabaseDumpSpec,
    DeleteBackupRequest,
    DeleteServiceRequest,
    EncryptionConfig,
    ErrorDetails,
    ExportMetadataRequest,
    GetBackupRequest,
    GetMetadataImportRequest,
    GetServiceRequest,
    HiveMetastoreConfig,
    KerberosConfig,
    ListBackupsRequest,
    ListBackupsResponse,
    ListMetadataImportsRequest,
    ListMetadataImportsResponse,
    ListServicesRequest,
    ListServicesResponse,
    LocationMetadata,
    MaintenanceWindow,
    MetadataExport,
    MetadataImport,
    MetadataManagementActivity,
    MoveTableToDatabaseRequest,
    MoveTableToDatabaseResponse,
    NetworkConfig,
    OperationMetadata,
    QueryMetadataRequest,
    QueryMetadataResponse,
    Restore,
    RestoreServiceRequest,
    ScalingConfig,
    Secret,
    Service,
    TelemetryConfig,
    UpdateMetadataImportRequest,
    UpdateServiceRequest,
)
from google.cloud.metastore_v1.types.metastore_federation import (
    BackendMetastore,
    CreateFederationRequest,
    DeleteFederationRequest,
    Federation,
    GetFederationRequest,
    ListFederationsRequest,
    ListFederationsResponse,
    UpdateFederationRequest,
)

__all__ = (
    "DataprocMetastoreClient",
    "DataprocMetastoreAsyncClient",
    "DataprocMetastoreFederationClient",
    "DataprocMetastoreFederationAsyncClient",
    "AlterMetadataResourceLocationRequest",
    "AlterMetadataResourceLocationResponse",
    "AuxiliaryVersionConfig",
    "Backup",
    "CreateBackupRequest",
    "CreateMetadataImportRequest",
    "CreateServiceRequest",
    "DatabaseDumpSpec",
    "DeleteBackupRequest",
    "DeleteServiceRequest",
    "EncryptionConfig",
    "ErrorDetails",
    "ExportMetadataRequest",
    "GetBackupRequest",
    "GetMetadataImportRequest",
    "GetServiceRequest",
    "HiveMetastoreConfig",
    "KerberosConfig",
    "ListBackupsRequest",
    "ListBackupsResponse",
    "ListMetadataImportsRequest",
    "ListMetadataImportsResponse",
    "ListServicesRequest",
    "ListServicesResponse",
    "LocationMetadata",
    "MaintenanceWindow",
    "MetadataExport",
    "MetadataImport",
    "MetadataManagementActivity",
    "MoveTableToDatabaseRequest",
    "MoveTableToDatabaseResponse",
    "NetworkConfig",
    "OperationMetadata",
    "QueryMetadataRequest",
    "QueryMetadataResponse",
    "Restore",
    "RestoreServiceRequest",
    "ScalingConfig",
    "Secret",
    "Service",
    "TelemetryConfig",
    "UpdateMetadataImportRequest",
    "UpdateServiceRequest",
    "BackendMetastore",
    "CreateFederationRequest",
    "DeleteFederationRequest",
    "Federation",
    "GetFederationRequest",
    "ListFederationsRequest",
    "ListFederationsResponse",
    "UpdateFederationRequest",
)
