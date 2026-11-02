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
from google.maps.fleetengine_delivery import gapic_version as package_version

__version__ = package_version.__version__


from google.maps.fleetengine_delivery_v1.services.delivery_service.async_client import (
    DeliveryServiceAsyncClient,
)
from google.maps.fleetengine_delivery_v1.services.delivery_service.client import (
    DeliveryServiceClient,
)
from google.maps.fleetengine_delivery_v1.types.common import (
    DeliveryVehicleAttribute,
    DeliveryVehicleLocation,
    DeliveryVehicleLocationSensor,
    DeliveryVehicleNavigationStatus,
    TaskAttribute,
    TimeWindow,
)
from google.maps.fleetengine_delivery_v1.types.delivery_api import (
    BatchCreateTasksRequest,
    BatchCreateTasksResponse,
    CreateDeliveryVehicleRequest,
    CreateTaskRequest,
    DeleteDeliveryVehicleRequest,
    DeleteTaskRequest,
    GetDeliveryVehicleRequest,
    GetTaskRequest,
    GetTaskTrackingInfoRequest,
    ListDeliveryVehiclesRequest,
    ListDeliveryVehiclesResponse,
    ListTasksRequest,
    ListTasksResponse,
    UpdateDeliveryVehicleRequest,
    UpdateTaskRequest,
)
from google.maps.fleetengine_delivery_v1.types.delivery_vehicles import (
    DeliveryVehicle,
    LocationInfo,
    VehicleJourneySegment,
    VehicleStop,
)
from google.maps.fleetengine_delivery_v1.types.header import DeliveryRequestHeader
from google.maps.fleetengine_delivery_v1.types.task_tracking_info import (
    TaskTrackingInfo,
)
from google.maps.fleetengine_delivery_v1.types.tasks import Task, TaskTrackingViewConfig

__all__ = (
    "DeliveryServiceClient",
    "DeliveryServiceAsyncClient",
    "DeliveryVehicleAttribute",
    "DeliveryVehicleLocation",
    "TaskAttribute",
    "TimeWindow",
    "DeliveryVehicleLocationSensor",
    "DeliveryVehicleNavigationStatus",
    "BatchCreateTasksRequest",
    "BatchCreateTasksResponse",
    "CreateDeliveryVehicleRequest",
    "CreateTaskRequest",
    "DeleteDeliveryVehicleRequest",
    "DeleteTaskRequest",
    "GetDeliveryVehicleRequest",
    "GetTaskRequest",
    "GetTaskTrackingInfoRequest",
    "ListDeliveryVehiclesRequest",
    "ListDeliveryVehiclesResponse",
    "ListTasksRequest",
    "ListTasksResponse",
    "UpdateDeliveryVehicleRequest",
    "UpdateTaskRequest",
    "DeliveryVehicle",
    "LocationInfo",
    "VehicleJourneySegment",
    "VehicleStop",
    "DeliveryRequestHeader",
    "TaskTrackingInfo",
    "Task",
    "TaskTrackingViewConfig",
)
