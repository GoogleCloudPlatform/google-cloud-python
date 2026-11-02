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
from google.cloud.redis import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.redis_v1.services.cloud_redis.client import CloudRedisClient
from google.cloud.redis_v1.services.cloud_redis.async_client import CloudRedisAsyncClient

from google.cloud.redis_v1.types.cloud_redis import CreateInstanceRequest
from google.cloud.redis_v1.types.cloud_redis import DeleteInstanceRequest
from google.cloud.redis_v1.types.cloud_redis import ExportInstanceRequest
from google.cloud.redis_v1.types.cloud_redis import FailoverInstanceRequest
from google.cloud.redis_v1.types.cloud_redis import GcsDestination
from google.cloud.redis_v1.types.cloud_redis import GcsSource
from google.cloud.redis_v1.types.cloud_redis import GetInstanceAuthStringRequest
from google.cloud.redis_v1.types.cloud_redis import GetInstanceRequest
from google.cloud.redis_v1.types.cloud_redis import ImportInstanceRequest
from google.cloud.redis_v1.types.cloud_redis import InputConfig
from google.cloud.redis_v1.types.cloud_redis import Instance
from google.cloud.redis_v1.types.cloud_redis import InstanceAuthString
from google.cloud.redis_v1.types.cloud_redis import ListInstancesRequest
from google.cloud.redis_v1.types.cloud_redis import ListInstancesResponse
from google.cloud.redis_v1.types.cloud_redis import LocationMetadata
from google.cloud.redis_v1.types.cloud_redis import MaintenancePolicy
from google.cloud.redis_v1.types.cloud_redis import MaintenanceSchedule
from google.cloud.redis_v1.types.cloud_redis import NodeInfo
from google.cloud.redis_v1.types.cloud_redis import OperationMetadata
from google.cloud.redis_v1.types.cloud_redis import OutputConfig
from google.cloud.redis_v1.types.cloud_redis import PersistenceConfig
from google.cloud.redis_v1.types.cloud_redis import RescheduleMaintenanceRequest
from google.cloud.redis_v1.types.cloud_redis import TlsCertificate
from google.cloud.redis_v1.types.cloud_redis import UpdateInstanceRequest
from google.cloud.redis_v1.types.cloud_redis import UpgradeInstanceRequest
from google.cloud.redis_v1.types.cloud_redis import WeeklyMaintenanceWindow
from google.cloud.redis_v1.types.cloud_redis import ZoneMetadata

__all__ = ('CloudRedisClient',
    'CloudRedisAsyncClient',
    'CreateInstanceRequest',
    'DeleteInstanceRequest',
    'ExportInstanceRequest',
    'FailoverInstanceRequest',
    'GcsDestination',
    'GcsSource',
    'GetInstanceAuthStringRequest',
    'GetInstanceRequest',
    'ImportInstanceRequest',
    'InputConfig',
    'Instance',
    'InstanceAuthString',
    'ListInstancesRequest',
    'ListInstancesResponse',
    'LocationMetadata',
    'MaintenancePolicy',
    'MaintenanceSchedule',
    'NodeInfo',
    'OperationMetadata',
    'OutputConfig',
    'PersistenceConfig',
    'RescheduleMaintenanceRequest',
    'TlsCertificate',
    'UpdateInstanceRequest',
    'UpgradeInstanceRequest',
    'WeeklyMaintenanceWindow',
    'ZoneMetadata',
)
