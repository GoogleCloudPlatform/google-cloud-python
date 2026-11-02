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
from google.cloud.memcache import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.memcache_v1.services.cloud_memcache.async_client import (
    CloudMemcacheAsyncClient,
)
from google.cloud.memcache_v1.services.cloud_memcache.client import CloudMemcacheClient
from google.cloud.memcache_v1.types.cloud_memcache import (
    ApplyParametersRequest,
    CreateInstanceRequest,
    DeleteInstanceRequest,
    GetInstanceRequest,
    Instance,
    ListInstancesRequest,
    ListInstancesResponse,
    LocationMetadata,
    MaintenancePolicy,
    MaintenanceSchedule,
    MemcacheParameters,
    MemcacheVersion,
    OperationMetadata,
    RescheduleMaintenanceRequest,
    UpdateInstanceRequest,
    UpdateParametersRequest,
    WeeklyMaintenanceWindow,
    ZoneMetadata,
)

__all__ = (
    "CloudMemcacheClient",
    "CloudMemcacheAsyncClient",
    "ApplyParametersRequest",
    "CreateInstanceRequest",
    "DeleteInstanceRequest",
    "GetInstanceRequest",
    "Instance",
    "ListInstancesRequest",
    "ListInstancesResponse",
    "LocationMetadata",
    "MaintenancePolicy",
    "MaintenanceSchedule",
    "MemcacheParameters",
    "OperationMetadata",
    "RescheduleMaintenanceRequest",
    "UpdateInstanceRequest",
    "UpdateParametersRequest",
    "WeeklyMaintenanceWindow",
    "ZoneMetadata",
    "MemcacheVersion",
)
