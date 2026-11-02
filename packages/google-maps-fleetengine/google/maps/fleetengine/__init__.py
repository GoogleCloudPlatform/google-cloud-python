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
from google.maps.fleetengine import gapic_version as package_version

__version__ = package_version.__version__


from google.maps.fleetengine_v1.services.trip_service.async_client import (
    TripServiceAsyncClient,
)
from google.maps.fleetengine_v1.services.trip_service.client import TripServiceClient
from google.maps.fleetengine_v1.services.vehicle_service.async_client import (
    VehicleServiceAsyncClient,
)
from google.maps.fleetengine_v1.services.vehicle_service.client import (
    VehicleServiceClient,
)
from google.maps.fleetengine_v1.types.fleetengine import (
    LocationSensor,
    NavigationStatus,
    PolylineFormatType,
    TerminalLocation,
    TerminalPointId,
    TripAttribute,
    TripType,
    TripWaypoint,
    VehicleAttribute,
    VehicleLocation,
    WaypointType,
)
from google.maps.fleetengine_v1.types.header import RequestHeader
from google.maps.fleetengine_v1.types.traffic import (
    ConsumableTrafficPolyline,
    SpeedReadingInterval,
)
from google.maps.fleetengine_v1.types.trip_api import (
    CreateTripRequest,
    DeleteTripRequest,
    GetTripRequest,
    ReportBillableTripRequest,
    SearchTripsRequest,
    SearchTripsResponse,
    UpdateTripRequest,
)
from google.maps.fleetengine_v1.types.trips import (
    BillingPlatformIdentifier,
    StopLocation,
    Trip,
    TripStatus,
    TripView,
)
from google.maps.fleetengine_v1.types.vehicle_api import (
    CreateVehicleRequest,
    DeleteVehicleRequest,
    GetVehicleRequest,
    ListVehiclesRequest,
    ListVehiclesResponse,
    SearchVehiclesRequest,
    SearchVehiclesResponse,
    UpdateVehicleAttributesRequest,
    UpdateVehicleAttributesResponse,
    UpdateVehicleRequest,
    VehicleAttributeList,
    VehicleMatch,
    Waypoint,
)
from google.maps.fleetengine_v1.types.vehicles import (
    BatteryInfo,
    BatteryStatus,
    DeviceSettings,
    LicensePlate,
    LocationPowerSaveMode,
    PowerSource,
    TrafficPolylineData,
    Vehicle,
    VehicleState,
    VisualTrafficReportPolylineRendering,
)

__all__ = (
    "TripServiceClient",
    "TripServiceAsyncClient",
    "VehicleServiceClient",
    "VehicleServiceAsyncClient",
    "TerminalLocation",
    "TerminalPointId",
    "TripAttribute",
    "TripWaypoint",
    "VehicleAttribute",
    "VehicleLocation",
    "LocationSensor",
    "NavigationStatus",
    "PolylineFormatType",
    "TripType",
    "WaypointType",
    "RequestHeader",
    "ConsumableTrafficPolyline",
    "SpeedReadingInterval",
    "CreateTripRequest",
    "DeleteTripRequest",
    "GetTripRequest",
    "ReportBillableTripRequest",
    "SearchTripsRequest",
    "SearchTripsResponse",
    "UpdateTripRequest",
    "StopLocation",
    "Trip",
    "BillingPlatformIdentifier",
    "TripStatus",
    "TripView",
    "CreateVehicleRequest",
    "DeleteVehicleRequest",
    "GetVehicleRequest",
    "ListVehiclesRequest",
    "ListVehiclesResponse",
    "SearchVehiclesRequest",
    "SearchVehiclesResponse",
    "UpdateVehicleAttributesRequest",
    "UpdateVehicleAttributesResponse",
    "UpdateVehicleRequest",
    "VehicleAttributeList",
    "VehicleMatch",
    "Waypoint",
    "BatteryInfo",
    "DeviceSettings",
    "LicensePlate",
    "TrafficPolylineData",
    "Vehicle",
    "VisualTrafficReportPolylineRendering",
    "BatteryStatus",
    "LocationPowerSaveMode",
    "PowerSource",
    "VehicleState",
)
