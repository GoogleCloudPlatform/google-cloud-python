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
from google.cloud.bigquery_biglake import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.bigquery_biglake_v1.services.metastore_service.async_client import (
    MetastoreServiceAsyncClient,
)
from google.cloud.bigquery_biglake_v1.services.metastore_service.client import (
    MetastoreServiceClient,
)
from google.cloud.bigquery_biglake_v1.types.metastore import (
    Catalog,
    CreateCatalogRequest,
    CreateDatabaseRequest,
    CreateTableRequest,
    Database,
    DeleteCatalogRequest,
    DeleteDatabaseRequest,
    DeleteTableRequest,
    GetCatalogRequest,
    GetDatabaseRequest,
    GetTableRequest,
    HiveDatabaseOptions,
    HiveTableOptions,
    ListCatalogsRequest,
    ListCatalogsResponse,
    ListDatabasesRequest,
    ListDatabasesResponse,
    ListTablesRequest,
    ListTablesResponse,
    RenameTableRequest,
    Table,
    TableView,
    UpdateDatabaseRequest,
    UpdateTableRequest,
)

__all__ = (
    "MetastoreServiceClient",
    "MetastoreServiceAsyncClient",
    "Catalog",
    "CreateCatalogRequest",
    "CreateDatabaseRequest",
    "CreateTableRequest",
    "Database",
    "DeleteCatalogRequest",
    "DeleteDatabaseRequest",
    "DeleteTableRequest",
    "GetCatalogRequest",
    "GetDatabaseRequest",
    "GetTableRequest",
    "HiveDatabaseOptions",
    "HiveTableOptions",
    "ListCatalogsRequest",
    "ListCatalogsResponse",
    "ListDatabasesRequest",
    "ListDatabasesResponse",
    "ListTablesRequest",
    "ListTablesResponse",
    "RenameTableRequest",
    "Table",
    "UpdateDatabaseRequest",
    "UpdateTableRequest",
    "TableView",
)
