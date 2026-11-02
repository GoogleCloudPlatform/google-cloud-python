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
from .datasources import (
    CreateDataSourceRequest,
    DataSource,
    DeleteDataSourceRequest,
    FetchDataSourceRequest,
    GetDataSourceRequest,
    ListDataSourcesRequest,
    ListDataSourcesResponse,
    UpdateDataSourceRequest,
)
from .datasourcetypes import (
    DataSourceReference,
    LocalInventoryDataSource,
    MerchantReviewDataSource,
    PrimaryProductDataSource,
    ProductReviewDataSource,
    PromotionDataSource,
    RegionalInventoryDataSource,
    SupplementalProductDataSource,
)
from .fileinputs import (
    FileInput,
)
from .fileuploads import (
    FileUpload,
    GetFileUploadRequest,
)

__all__ = (
    "CreateDataSourceRequest",
    "DataSource",
    "DeleteDataSourceRequest",
    "FetchDataSourceRequest",
    "GetDataSourceRequest",
    "ListDataSourcesRequest",
    "ListDataSourcesResponse",
    "UpdateDataSourceRequest",
    "DataSourceReference",
    "LocalInventoryDataSource",
    "MerchantReviewDataSource",
    "PrimaryProductDataSource",
    "ProductReviewDataSource",
    "PromotionDataSource",
    "RegionalInventoryDataSource",
    "SupplementalProductDataSource",
    "FileInput",
    "FileUpload",
    "GetFileUploadRequest",
)
