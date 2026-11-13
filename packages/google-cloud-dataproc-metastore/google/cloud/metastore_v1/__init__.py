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

from google.cloud.metastore_v1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.metastore_v1.services.dataproc_metastore",
    "google.cloud.metastore_v1.services.dataproc_metastore_federation",
    "google.cloud.metastore_v1.types.metastore",
    "google.cloud.metastore_v1.types.metastore_federation",
}


from .services.dataproc_metastore import (
    DataprocMetastoreAsyncClient,
    DataprocMetastoreClient,
)
from .services.dataproc_metastore_federation import (
    DataprocMetastoreFederationAsyncClient,
    DataprocMetastoreFederationClient,
)
from .types.metastore import (
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
from .types.metastore_federation import (
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
    "DataprocMetastoreAsyncClient",
    "DataprocMetastoreFederationAsyncClient",
    "AlterMetadataResourceLocationRequest",
    "AlterMetadataResourceLocationResponse",
    "AuxiliaryVersionConfig",
    "BackendMetastore",
    "Backup",
    "CreateBackupRequest",
    "CreateFederationRequest",
    "CreateMetadataImportRequest",
    "CreateServiceRequest",
    "DatabaseDumpSpec",
    "DataprocMetastoreClient",
    "DataprocMetastoreFederationClient",
    "DeleteBackupRequest",
    "DeleteFederationRequest",
    "DeleteServiceRequest",
    "EncryptionConfig",
    "ErrorDetails",
    "ExportMetadataRequest",
    "Federation",
    "GetBackupRequest",
    "GetFederationRequest",
    "GetMetadataImportRequest",
    "GetServiceRequest",
    "HiveMetastoreConfig",
    "KerberosConfig",
    "ListBackupsRequest",
    "ListBackupsResponse",
    "ListFederationsRequest",
    "ListFederationsResponse",
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
    "UpdateFederationRequest",
    "UpdateMetadataImportRequest",
    "UpdateServiceRequest",
)

api_core.check_python_version("google.cloud.metastore_v1")
api_core.check_dependency_versions("google.cloud.metastore_v1")
