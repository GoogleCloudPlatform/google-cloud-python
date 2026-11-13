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
import google.api_core as api_core

from google.maps.fleetengine_v1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.maps.fleetengine_v1.services.trip_service",
    "google.maps.fleetengine_v1.services.vehicle_service",
    "google.maps.fleetengine_v1.types.fleetengine",
    "google.maps.fleetengine_v1.types.header",
    "google.maps.fleetengine_v1.types.traffic",
    "google.maps.fleetengine_v1.types.trip_api",
    "google.maps.fleetengine_v1.types.trips",
    "google.maps.fleetengine_v1.types.vehicle_api",
    "google.maps.fleetengine_v1.types.vehicles",
}


from .services.trip_service import TripServiceAsyncClient, TripServiceClient
from .services.vehicle_service import VehicleServiceAsyncClient, VehicleServiceClient
from .types.fleetengine import (
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
from .types.header import RequestHeader
from .types.traffic import ConsumableTrafficPolyline, SpeedReadingInterval
from .types.trip_api import (
    CreateTripRequest,
    DeleteTripRequest,
    GetTripRequest,
    ReportBillableTripRequest,
    SearchTripsRequest,
    SearchTripsResponse,
    UpdateTripRequest,
)
from .types.trips import (
    BillingPlatformIdentifier,
    StopLocation,
    Trip,
    TripStatus,
    TripView,
)
from .types.vehicle_api import (
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
from .types.vehicles import (
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
    "TripServiceAsyncClient",
    "VehicleServiceAsyncClient",
    "BatteryInfo",
    "BatteryStatus",
    "BillingPlatformIdentifier",
    "ConsumableTrafficPolyline",
    "CreateTripRequest",
    "CreateVehicleRequest",
    "DeleteTripRequest",
    "DeleteVehicleRequest",
    "DeviceSettings",
    "GetTripRequest",
    "GetVehicleRequest",
    "LicensePlate",
    "ListVehiclesRequest",
    "ListVehiclesResponse",
    "LocationPowerSaveMode",
    "LocationSensor",
    "NavigationStatus",
    "PolylineFormatType",
    "PowerSource",
    "ReportBillableTripRequest",
    "RequestHeader",
    "SearchTripsRequest",
    "SearchTripsResponse",
    "SearchVehiclesRequest",
    "SearchVehiclesResponse",
    "SpeedReadingInterval",
    "StopLocation",
    "TerminalLocation",
    "TerminalPointId",
    "TrafficPolylineData",
    "Trip",
    "TripAttribute",
    "TripServiceClient",
    "TripStatus",
    "TripType",
    "TripView",
    "TripWaypoint",
    "UpdateTripRequest",
    "UpdateVehicleAttributesRequest",
    "UpdateVehicleAttributesResponse",
    "UpdateVehicleRequest",
    "Vehicle",
    "VehicleAttribute",
    "VehicleAttributeList",
    "VehicleLocation",
    "VehicleMatch",
    "VehicleServiceClient",
    "VehicleState",
    "VisualTrafficReportPolylineRendering",
    "Waypoint",
    "WaypointType",
)

api_core.check_python_version("google.maps.fleetengine_v1")
api_core.check_dependency_versions("google.maps.fleetengine_v1")
