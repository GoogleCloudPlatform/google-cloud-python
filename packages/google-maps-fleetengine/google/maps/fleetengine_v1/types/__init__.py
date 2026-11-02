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
from .fleetengine import (
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
from .header import (
    RequestHeader,
)
from .traffic import (
    ConsumableTrafficPolyline,
    SpeedReadingInterval,
)
from .trip_api import (
    CreateTripRequest,
    DeleteTripRequest,
    GetTripRequest,
    ReportBillableTripRequest,
    SearchTripsRequest,
    SearchTripsResponse,
    UpdateTripRequest,
)
from .trips import (
    BillingPlatformIdentifier,
    StopLocation,
    Trip,
    TripStatus,
    TripView,
)
from .vehicle_api import (
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
from .vehicles import (
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
