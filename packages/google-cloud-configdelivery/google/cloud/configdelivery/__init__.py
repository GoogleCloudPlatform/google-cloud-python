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
from google.cloud.configdelivery import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.configdelivery_v1alpha.services.config_delivery.async_client import (
    ConfigDeliveryAsyncClient,
)
from google.cloud.configdelivery_v1alpha.services.config_delivery.client import (
    ConfigDeliveryClient,
)
from google.cloud.configdelivery_v1alpha.types.config_delivery import (
    AbortRolloutRequest,
    AllAtOnceStrategy,
    AllAtOnceStrategyInfo,
    ClusterInfo,
    CreateFleetPackageRequest,
    CreateReleaseRequest,
    CreateResourceBundleRequest,
    CreateVariantRequest,
    DeleteFleetPackageRequest,
    DeleteReleaseRequest,
    DeleteResourceBundleRequest,
    DeleteVariantRequest,
    DeletionPropagationPolicy,
    Fleet,
    FleetPackage,
    FleetPackageError,
    FleetPackageInfo,
    GetFleetPackageRequest,
    GetReleaseRequest,
    GetResourceBundleRequest,
    GetRolloutRequest,
    GetVariantRequest,
    ListFleetPackagesRequest,
    ListFleetPackagesResponse,
    ListReleasesRequest,
    ListReleasesResponse,
    ListResourceBundlesRequest,
    ListResourceBundlesResponse,
    ListRolloutsRequest,
    ListRolloutsResponse,
    ListVariantsRequest,
    ListVariantsResponse,
    OperationMetadata,
    Release,
    ReleaseInfo,
    ResourceBundle,
    ResourceBundleDeploymentInfo,
    ResumeRolloutRequest,
    RollingStrategy,
    RollingStrategyInfo,
    Rollout,
    RolloutInfo,
    RolloutStrategy,
    RolloutStrategyInfo,
    SuspendRolloutRequest,
    UpdateFleetPackageRequest,
    UpdateReleaseRequest,
    UpdateResourceBundleRequest,
    UpdateVariantRequest,
    Variant,
)

__all__ = (
    "ConfigDeliveryClient",
    "ConfigDeliveryAsyncClient",
    "AbortRolloutRequest",
    "AllAtOnceStrategy",
    "AllAtOnceStrategyInfo",
    "ClusterInfo",
    "CreateFleetPackageRequest",
    "CreateReleaseRequest",
    "CreateResourceBundleRequest",
    "CreateVariantRequest",
    "DeleteFleetPackageRequest",
    "DeleteReleaseRequest",
    "DeleteResourceBundleRequest",
    "DeleteVariantRequest",
    "Fleet",
    "FleetPackage",
    "FleetPackageError",
    "FleetPackageInfo",
    "GetFleetPackageRequest",
    "GetReleaseRequest",
    "GetResourceBundleRequest",
    "GetRolloutRequest",
    "GetVariantRequest",
    "ListFleetPackagesRequest",
    "ListFleetPackagesResponse",
    "ListReleasesRequest",
    "ListReleasesResponse",
    "ListResourceBundlesRequest",
    "ListResourceBundlesResponse",
    "ListRolloutsRequest",
    "ListRolloutsResponse",
    "ListVariantsRequest",
    "ListVariantsResponse",
    "OperationMetadata",
    "Release",
    "ReleaseInfo",
    "ResourceBundle",
    "ResourceBundleDeploymentInfo",
    "ResumeRolloutRequest",
    "RollingStrategy",
    "RollingStrategyInfo",
    "Rollout",
    "RolloutInfo",
    "RolloutStrategy",
    "RolloutStrategyInfo",
    "SuspendRolloutRequest",
    "UpdateFleetPackageRequest",
    "UpdateReleaseRequest",
    "UpdateResourceBundleRequest",
    "UpdateVariantRequest",
    "Variant",
    "DeletionPropagationPolicy",
)
