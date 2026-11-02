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
from google.cloud.capacityplanner import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.capacityplanner_v1beta.services.usage_service.async_client import (
    UsageServiceAsyncClient,
)
from google.cloud.capacityplanner_v1beta.services.usage_service.client import (
    UsageServiceClient,
)
from google.cloud.capacityplanner_v1beta.types.allocation import Allocation
from google.cloud.capacityplanner_v1beta.types.future_reservation import (
    FutureReservation,
)
from google.cloud.capacityplanner_v1beta.types.location import (
    LocationIdentifier,
    LocationLevel,
)
from google.cloud.capacityplanner_v1beta.types.resource import (
    ResourceAttribute,
    ResourceContainer,
    ResourceIdentifier,
    ResourceIdKey,
    ResourceValue,
    Unit,
    Value,
)
from google.cloud.capacityplanner_v1beta.types.usage_service import (
    BigQueryDestination,
    ExportForecastsRequest,
    ExportForecastsResponse,
    ExportReservationsUsageRequest,
    ExportReservationsUsageResponse,
    ExportUsageHistoriesRequest,
    ExportUsageHistoriesResponse,
    Forecast,
    GcsDestination,
    MachineShape,
    OperationMetadata,
    OutputConfig,
    Point,
    QueryForecastsRequest,
    QueryForecastsResponse,
    QueryReservationsRequest,
    QueryReservationsResponse,
    QueryUsageHistoriesRequest,
    QueryUsageHistoriesResponse,
    ReservationData,
    TimeSeries,
    UsageHistory,
)

__all__ = (
    "UsageServiceClient",
    "UsageServiceAsyncClient",
    "Allocation",
    "FutureReservation",
    "LocationIdentifier",
    "LocationLevel",
    "ResourceAttribute",
    "ResourceContainer",
    "ResourceIdentifier",
    "ResourceIdKey",
    "ResourceValue",
    "Value",
    "Unit",
    "BigQueryDestination",
    "ExportForecastsRequest",
    "ExportForecastsResponse",
    "ExportReservationsUsageRequest",
    "ExportReservationsUsageResponse",
    "ExportUsageHistoriesRequest",
    "ExportUsageHistoriesResponse",
    "Forecast",
    "GcsDestination",
    "MachineShape",
    "OperationMetadata",
    "OutputConfig",
    "Point",
    "QueryForecastsRequest",
    "QueryForecastsResponse",
    "QueryReservationsRequest",
    "QueryReservationsResponse",
    "QueryUsageHistoriesRequest",
    "QueryUsageHistoriesResponse",
    "ReservationData",
    "TimeSeries",
    "UsageHistory",
)
