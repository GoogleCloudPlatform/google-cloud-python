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
from google.cloud.storageinsights import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.storageinsights_v1.services.storage_insights.async_client import (
    StorageInsightsAsyncClient,
)
from google.cloud.storageinsights_v1.services.storage_insights.client import (
    StorageInsightsClient,
)
from google.cloud.storageinsights_v1.types.storageinsights import (
    CloudStorageDestinationOptions,
    CloudStorageFilters,
    CreateDatasetConfigRequest,
    CreateReportConfigRequest,
    CSVOptions,
    DatasetConfig,
    DeleteDatasetConfigRequest,
    DeleteReportConfigRequest,
    FrequencyOptions,
    GetDatasetConfigRequest,
    GetReportConfigRequest,
    GetReportDetailRequest,
    Identity,
    LinkDatasetRequest,
    LinkDatasetResponse,
    ListDatasetConfigsRequest,
    ListDatasetConfigsResponse,
    ListReportConfigsRequest,
    ListReportConfigsResponse,
    ListReportDetailsRequest,
    ListReportDetailsResponse,
    LocationMetadata,
    ObjectMetadataReportOptions,
    OperationMetadata,
    ParquetOptions,
    ReportConfig,
    ReportDetail,
    UnlinkDatasetRequest,
    UpdateDatasetConfigRequest,
    UpdateReportConfigRequest,
)

__all__ = (
    "StorageInsightsClient",
    "StorageInsightsAsyncClient",
    "CloudStorageDestinationOptions",
    "CloudStorageFilters",
    "CreateDatasetConfigRequest",
    "CreateReportConfigRequest",
    "CSVOptions",
    "DatasetConfig",
    "DeleteDatasetConfigRequest",
    "DeleteReportConfigRequest",
    "FrequencyOptions",
    "GetDatasetConfigRequest",
    "GetReportConfigRequest",
    "GetReportDetailRequest",
    "Identity",
    "LinkDatasetRequest",
    "LinkDatasetResponse",
    "ListDatasetConfigsRequest",
    "ListDatasetConfigsResponse",
    "ListReportConfigsRequest",
    "ListReportConfigsResponse",
    "ListReportDetailsRequest",
    "ListReportDetailsResponse",
    "LocationMetadata",
    "ObjectMetadataReportOptions",
    "OperationMetadata",
    "ParquetOptions",
    "ReportConfig",
    "ReportDetail",
    "UnlinkDatasetRequest",
    "UpdateDatasetConfigRequest",
    "UpdateReportConfigRequest",
)
