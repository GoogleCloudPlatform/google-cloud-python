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

from google.maps.routing_v2 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.maps.routing_v2.services.routes",
    "google.maps.routing_v2.types.fallback_info",
    "google.maps.routing_v2.types.geocoding_results",
    "google.maps.routing_v2.types.localized_time",
    "google.maps.routing_v2.types.location",
    "google.maps.routing_v2.types.maneuver",
    "google.maps.routing_v2.types.navigation_instruction",
    "google.maps.routing_v2.types.polyline",
    "google.maps.routing_v2.types.polyline_details",
    "google.maps.routing_v2.types.route",
    "google.maps.routing_v2.types.route_label",
    "google.maps.routing_v2.types.route_modifiers",
    "google.maps.routing_v2.types.route_travel_mode",
    "google.maps.routing_v2.types.routes_service",
    "google.maps.routing_v2.types.routing_preference",
    "google.maps.routing_v2.types.speed_reading_interval",
    "google.maps.routing_v2.types.toll_info",
    "google.maps.routing_v2.types.toll_passes",
    "google.maps.routing_v2.types.traffic_model",
    "google.maps.routing_v2.types.transit",
    "google.maps.routing_v2.types.transit_preferences",
    "google.maps.routing_v2.types.units",
    "google.maps.routing_v2.types.vehicle_emission_type",
    "google.maps.routing_v2.types.vehicle_info",
    "google.maps.routing_v2.types.waypoint",
}


from .services.routes import RoutesAsyncClient, RoutesClient
from .types.fallback_info import FallbackInfo, FallbackReason, FallbackRoutingMode
from .types.geocoding_results import GeocodedWaypoint, GeocodingResults
from .types.localized_time import LocalizedTime
from .types.location import Location
from .types.maneuver import Maneuver
from .types.navigation_instruction import NavigationInstruction
from .types.polyline import Polyline, PolylineEncoding, PolylineQuality
from .types.polyline_details import PolylineDetails
from .types.route import (
    Route,
    RouteLeg,
    RouteLegStep,
    RouteLegStepTransitDetails,
    RouteLegStepTravelAdvisory,
    RouteLegTravelAdvisory,
    RouteTravelAdvisory,
)
from .types.route_label import RouteLabel
from .types.route_modifiers import RouteModifiers
from .types.route_travel_mode import RouteTravelMode
from .types.routes_service import (
    ComputeRouteMatrixRequest,
    ComputeRoutesRequest,
    ComputeRoutesResponse,
    RouteMatrixDestination,
    RouteMatrixElement,
    RouteMatrixElementCondition,
    RouteMatrixOrigin,
)
from .types.routing_preference import RoutingPreference
from .types.speed_reading_interval import SpeedReadingInterval
from .types.toll_info import TollInfo
from .types.toll_passes import TollPass
from .types.traffic_model import TrafficModel
from .types.transit import TransitAgency, TransitLine, TransitStop, TransitVehicle
from .types.transit_preferences import TransitPreferences
from .types.units import Units
from .types.vehicle_emission_type import VehicleEmissionType
from .types.vehicle_info import VehicleInfo
from .types.waypoint import Waypoint

__all__ = (
    "RoutesAsyncClient",
    "ComputeRouteMatrixRequest",
    "ComputeRoutesRequest",
    "ComputeRoutesResponse",
    "FallbackInfo",
    "FallbackReason",
    "FallbackRoutingMode",
    "GeocodedWaypoint",
    "GeocodingResults",
    "LocalizedTime",
    "Location",
    "Maneuver",
    "NavigationInstruction",
    "Polyline",
    "PolylineDetails",
    "PolylineEncoding",
    "PolylineQuality",
    "Route",
    "RouteLabel",
    "RouteLeg",
    "RouteLegStep",
    "RouteLegStepTransitDetails",
    "RouteLegStepTravelAdvisory",
    "RouteLegTravelAdvisory",
    "RouteMatrixDestination",
    "RouteMatrixElement",
    "RouteMatrixElementCondition",
    "RouteMatrixOrigin",
    "RouteModifiers",
    "RouteTravelAdvisory",
    "RouteTravelMode",
    "RoutesClient",
    "RoutingPreference",
    "SpeedReadingInterval",
    "TollInfo",
    "TollPass",
    "TrafficModel",
    "TransitAgency",
    "TransitLine",
    "TransitPreferences",
    "TransitStop",
    "TransitVehicle",
    "Units",
    "VehicleEmissionType",
    "VehicleInfo",
    "Waypoint",
)

api_core.check_python_version("google.maps.routing_v2")
api_core.check_dependency_versions("google.maps.routing_v2")
