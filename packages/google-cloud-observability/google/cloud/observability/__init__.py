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
from google.cloud.observability import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.observability_v1.services.observability.async_client import (
    ObservabilityAsyncClient,
)
from google.cloud.observability_v1.services.observability.client import (
    ObservabilityClient,
)
from google.cloud.observability_v1.types.observability import (
    Bucket,
    CmekSettings,
    CreateBucketRequest,
    CreateLinkRequest,
    CreateTraceScopeRequest,
    Dataset,
    DeleteLinkRequest,
    DeleteTraceScopeRequest,
    GetBucketRequest,
    GetDatasetRequest,
    GetLinkRequest,
    GetScopeRequest,
    GetSettingsRequest,
    GetTraceScopeRequest,
    GetViewRequest,
    Link,
    ListBucketsRequest,
    ListBucketsResponse,
    ListDatasetsRequest,
    ListDatasetsResponse,
    ListLinksRequest,
    ListLinksResponse,
    ListTraceScopesRequest,
    ListTraceScopesResponse,
    ListViewsRequest,
    ListViewsResponse,
    OperationMetadata,
    Scope,
    Settings,
    TraceScope,
    UpdateBucketRequest,
    UpdateLinkRequest,
    UpdateScopeRequest,
    UpdateSettingsRequest,
    UpdateTraceScopeRequest,
    View,
)

__all__ = (
    "ObservabilityClient",
    "ObservabilityAsyncClient",
    "Bucket",
    "CmekSettings",
    "CreateBucketRequest",
    "CreateLinkRequest",
    "CreateTraceScopeRequest",
    "Dataset",
    "DeleteLinkRequest",
    "DeleteTraceScopeRequest",
    "GetBucketRequest",
    "GetDatasetRequest",
    "GetLinkRequest",
    "GetScopeRequest",
    "GetSettingsRequest",
    "GetTraceScopeRequest",
    "GetViewRequest",
    "Link",
    "ListBucketsRequest",
    "ListBucketsResponse",
    "ListDatasetsRequest",
    "ListDatasetsResponse",
    "ListLinksRequest",
    "ListLinksResponse",
    "ListTraceScopesRequest",
    "ListTraceScopesResponse",
    "ListViewsRequest",
    "ListViewsResponse",
    "OperationMetadata",
    "Scope",
    "Settings",
    "TraceScope",
    "UpdateBucketRequest",
    "UpdateLinkRequest",
    "UpdateScopeRequest",
    "UpdateSettingsRequest",
    "UpdateTraceScopeRequest",
    "View",
)
