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
from google.cloud.licensemanager import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.licensemanager_v1.services.license_manager.async_client import (
    LicenseManagerAsyncClient,
)
from google.cloud.licensemanager_v1.services.license_manager.client import (
    LicenseManagerClient,
)
from google.cloud.licensemanager_v1.types.api_entities import (
    ActivationState,
    BillingInfo,
    Configuration,
    Instance,
    LicenseType,
    Product,
    Usage,
    UserCountBillingInfo,
    UserCountUsage,
)
from google.cloud.licensemanager_v1.types.licensemanager import (
    AggregateUsageRequest,
    AggregateUsageResponse,
    CreateConfigurationRequest,
    DeactivateConfigurationRequest,
    DeleteConfigurationRequest,
    GetConfigurationRequest,
    GetInstanceRequest,
    GetProductRequest,
    ListConfigurationsRequest,
    ListConfigurationsResponse,
    ListInstancesRequest,
    ListInstancesResponse,
    ListProductsRequest,
    ListProductsResponse,
    OperationMetadata,
    QueryConfigurationLicenseUsageRequest,
    QueryConfigurationLicenseUsageResponse,
    ReactivateConfigurationRequest,
    UpdateConfigurationRequest,
)

__all__ = (
    "LicenseManagerClient",
    "LicenseManagerAsyncClient",
    "BillingInfo",
    "Configuration",
    "Instance",
    "Product",
    "Usage",
    "UserCountBillingInfo",
    "UserCountUsage",
    "ActivationState",
    "LicenseType",
    "AggregateUsageRequest",
    "AggregateUsageResponse",
    "CreateConfigurationRequest",
    "DeactivateConfigurationRequest",
    "DeleteConfigurationRequest",
    "GetConfigurationRequest",
    "GetInstanceRequest",
    "GetProductRequest",
    "ListConfigurationsRequest",
    "ListConfigurationsResponse",
    "ListInstancesRequest",
    "ListInstancesResponse",
    "ListProductsRequest",
    "ListProductsResponse",
    "OperationMetadata",
    "QueryConfigurationLicenseUsageRequest",
    "QueryConfigurationLicenseUsageResponse",
    "ReactivateConfigurationRequest",
    "UpdateConfigurationRequest",
)
