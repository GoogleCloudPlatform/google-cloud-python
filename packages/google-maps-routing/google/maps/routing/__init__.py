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
from google.maps.routing import gapic_version as package_version

__version__ = package_version.__version__


from google.maps.routing_v2.services.routes.async_client import RoutesAsyncClient
from google.maps.routing_v2.services.routes.client import RoutesClient
from google.maps.routing_v2.types.fallback_info import (
    FallbackInfo,
    FallbackReason,
    FallbackRoutingMode,
)
from google.maps.routing_v2.types.geocoding_results import (
    GeocodedWaypoint,
    GeocodingResults,
)
from google.maps.routing_v2.types.localized_time import LocalizedTime
from google.maps.routing_v2.types.location import Location
from google.maps.routing_v2.types.maneuver import Maneuver
from google.maps.routing_v2.types.navigation_instruction import NavigationInstruction
from google.maps.routing_v2.types.polyline import (
    Polyline,
    PolylineEncoding,
    PolylineQuality,
)
from google.maps.routing_v2.types.polyline_details import PolylineDetails
from google.maps.routing_v2.types.route import (
    Route,
    RouteLeg,
    RouteLegStep,
    RouteLegStepTransitDetails,
    RouteLegStepTravelAdvisory,
    RouteLegTravelAdvisory,
    RouteTravelAdvisory,
)
from google.maps.routing_v2.types.route_label import RouteLabel
from google.maps.routing_v2.types.route_modifiers import RouteModifiers
from google.maps.routing_v2.types.route_travel_mode import RouteTravelMode
from google.maps.routing_v2.types.routes_service import (
    ComputeRouteMatrixRequest,
    ComputeRoutesRequest,
    ComputeRoutesResponse,
    RouteMatrixDestination,
    RouteMatrixElement,
    RouteMatrixElementCondition,
    RouteMatrixOrigin,
)
from google.maps.routing_v2.types.routing_preference import RoutingPreference
from google.maps.routing_v2.types.speed_reading_interval import SpeedReadingInterval
from google.maps.routing_v2.types.toll_info import TollInfo
from google.maps.routing_v2.types.toll_passes import TollPass
from google.maps.routing_v2.types.traffic_model import TrafficModel
from google.maps.routing_v2.types.transit import (
    TransitAgency,
    TransitLine,
    TransitStop,
    TransitVehicle,
)
from google.maps.routing_v2.types.transit_preferences import TransitPreferences
from google.maps.routing_v2.types.units import Units
from google.maps.routing_v2.types.vehicle_emission_type import VehicleEmissionType
from google.maps.routing_v2.types.vehicle_info import VehicleInfo
from google.maps.routing_v2.types.waypoint import Waypoint

__all__ = (
    "RoutesClient",
    "RoutesAsyncClient",
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
    "PolylineEncoding",
    "PolylineQuality",
    "PolylineDetails",
    "Route",
    "RouteLeg",
    "RouteLegStep",
    "RouteLegStepTransitDetails",
    "RouteLegStepTravelAdvisory",
    "RouteLegTravelAdvisory",
    "RouteTravelAdvisory",
    "RouteLabel",
    "RouteModifiers",
    "RouteTravelMode",
    "ComputeRouteMatrixRequest",
    "ComputeRoutesRequest",
    "ComputeRoutesResponse",
    "RouteMatrixDestination",
    "RouteMatrixElement",
    "RouteMatrixOrigin",
    "RouteMatrixElementCondition",
    "RoutingPreference",
    "SpeedReadingInterval",
    "TollInfo",
    "TollPass",
    "TrafficModel",
    "TransitAgency",
    "TransitLine",
    "TransitStop",
    "TransitVehicle",
    "TransitPreferences",
    "Units",
    "VehicleEmissionType",
    "VehicleInfo",
    "Waypoint",
)
