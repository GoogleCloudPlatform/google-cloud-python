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
from google.cloud.firestore_admin_v1.services.firestore_admin import (
    FirestoreAdminClient,
)
from google.cloud.firestore_admin_v1.types.field import Field
from google.cloud.firestore_admin_v1.types.firestore_admin import (
    CreateIndexRequest,
    DeleteIndexRequest,
    ExportDocumentsRequest,
    GetFieldRequest,
    GetIndexRequest,
    ImportDocumentsRequest,
    ListFieldsRequest,
    ListFieldsResponse,
    ListIndexesRequest,
    ListIndexesResponse,
    UpdateFieldRequest,
)
from google.cloud.firestore_admin_v1.types.index import Index
from google.cloud.firestore_admin_v1.types.location import LocationMetadata
from google.cloud.firestore_admin_v1.types.operation import (
    ExportDocumentsMetadata,
    ExportDocumentsResponse,
    FieldOperationMetadata,
    ImportDocumentsMetadata,
    IndexOperationMetadata,
    OperationState,
    Progress,
)

__all__ = (
    "CreateIndexRequest",
    "DeleteIndexRequest",
    "ExportDocumentsMetadata",
    "ExportDocumentsRequest",
    "ExportDocumentsResponse",
    "Field",
    "FieldOperationMetadata",
    "GetFieldRequest",
    "GetIndexRequest",
    "ImportDocumentsMetadata",
    "ImportDocumentsRequest",
    "Index",
    "IndexOperationMetadata",
    "ListFieldsRequest",
    "ListFieldsResponse",
    "ListIndexesRequest",
    "ListIndexesResponse",
    "LocationMetadata",
    "OperationState",
    "Progress",
    "UpdateFieldRequest",
    "FirestoreAdminClient",
)
