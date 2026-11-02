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
from google.cloud.datastore_admin import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.datastore_admin_v1.services.datastore_admin.async_client import (
    DatastoreAdminAsyncClient,
)
from google.cloud.datastore_admin_v1.services.datastore_admin.client import (
    DatastoreAdminClient,
)
from google.cloud.datastore_admin_v1.types.datastore_admin import (
    CommonMetadata,
    CreateIndexRequest,
    DatastoreFirestoreMigrationMetadata,
    DeleteIndexRequest,
    EntityFilter,
    ExportEntitiesMetadata,
    ExportEntitiesRequest,
    ExportEntitiesResponse,
    GetIndexRequest,
    ImportEntitiesMetadata,
    ImportEntitiesRequest,
    IndexOperationMetadata,
    ListIndexesRequest,
    ListIndexesResponse,
    OperationType,
    Progress,
)
from google.cloud.datastore_admin_v1.types.index import Index
from google.cloud.datastore_admin_v1.types.migration import (
    MigrationProgressEvent,
    MigrationState,
    MigrationStateEvent,
    MigrationStep,
)

__all__ = (
    "DatastoreAdminClient",
    "DatastoreAdminAsyncClient",
    "CommonMetadata",
    "CreateIndexRequest",
    "DatastoreFirestoreMigrationMetadata",
    "DeleteIndexRequest",
    "EntityFilter",
    "ExportEntitiesMetadata",
    "ExportEntitiesRequest",
    "ExportEntitiesResponse",
    "GetIndexRequest",
    "ImportEntitiesMetadata",
    "ImportEntitiesRequest",
    "IndexOperationMetadata",
    "ListIndexesRequest",
    "ListIndexesResponse",
    "Progress",
    "OperationType",
    "Index",
    "MigrationProgressEvent",
    "MigrationStateEvent",
    "MigrationState",
    "MigrationStep",
)
