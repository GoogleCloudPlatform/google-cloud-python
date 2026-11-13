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

from google.cloud.biglake_v1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.biglake_v1.services.iceberg_catalog_service",
    "google.cloud.biglake_v1.types.iceberg_rest_catalog",
}


from .services.iceberg_catalog_service import (
    IcebergCatalogServiceAsyncClient,
    IcebergCatalogServiceClient,
)
from .types.iceberg_rest_catalog import (
    CreateIcebergCatalogRequest,
    FailoverIcebergCatalogRequest,
    FailoverIcebergCatalogResponse,
    GetIcebergCatalogRequest,
    IcebergCatalog,
    IcebergNamespaceUpdate,
    ListIcebergCatalogsRequest,
    ListIcebergCatalogsResponse,
    StorageCredential,
    TableIdentifier,
    UpdateIcebergCatalogRequest,
)

__all__ = (
    "IcebergCatalogServiceAsyncClient",
    "CreateIcebergCatalogRequest",
    "FailoverIcebergCatalogRequest",
    "FailoverIcebergCatalogResponse",
    "GetIcebergCatalogRequest",
    "IcebergCatalog",
    "IcebergCatalogServiceClient",
    "IcebergNamespaceUpdate",
    "ListIcebergCatalogsRequest",
    "ListIcebergCatalogsResponse",
    "StorageCredential",
    "TableIdentifier",
    "UpdateIcebergCatalogRequest",
)

api_core.check_python_version("google.cloud.biglake_v1")
api_core.check_dependency_versions("google.cloud.biglake_v1")
