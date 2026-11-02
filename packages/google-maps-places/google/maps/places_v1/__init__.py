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

from google.maps.places_v1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.maps.places_v1.services.places",
    "google.maps.places_v1.types.address_descriptor",
    "google.maps.places_v1.types.attribution",
    "google.maps.places_v1.types.content_block",
    "google.maps.places_v1.types.contextual_content",
    "google.maps.places_v1.types.ev_charging",
    "google.maps.places_v1.types.fuel_options",
    "google.maps.places_v1.types.geometry",
    "google.maps.places_v1.types.photo",
    "google.maps.places_v1.types.place",
    "google.maps.places_v1.types.places_service",
    "google.maps.places_v1.types.polyline",
    "google.maps.places_v1.types.price_range",
    "google.maps.places_v1.types.reference",
    "google.maps.places_v1.types.review",
    "google.maps.places_v1.types.route_modifiers",
    "google.maps.places_v1.types.routing_preference",
    "google.maps.places_v1.types.routing_summary",
    "google.maps.places_v1.types.transit",
    "google.maps.places_v1.types.travel_mode",
}


from .services.places import PlacesAsyncClient, PlacesClient
from .types.address_descriptor import AddressDescriptor
from .types.attribution import AuthorAttribution
from .types.content_block import ContentBlock
from .types.contextual_content import ContextualContent
from .types.ev_charging import EVChargeOptions, EVConnectorType
from .types.fuel_options import FuelOptions
from .types.geometry import Circle
from .types.photo import Photo
from .types.place import Place, PriceLevel
from .types.places_service import (
    AutocompletePlacesRequest,
    AutocompletePlacesResponse,
    GetPhotoMediaRequest,
    GetPlaceRequest,
    PhotoMedia,
    RoutingParameters,
    SearchNearbyRequest,
    SearchNearbyResponse,
    SearchTextRequest,
    SearchTextResponse,
)
from .types.polyline import Polyline
from .types.price_range import PriceRange
from .types.reference import References
from .types.review import Review
from .types.route_modifiers import RouteModifiers
from .types.routing_preference import RoutingPreference
from .types.routing_summary import RoutingSummary
from .types.transit import (
    TransitAgency,
    TransitIcon,
    TransitLine,
    TransitStation,
    TransitStop,
)
from .types.travel_mode import TravelMode

__all__ = (
    "PlacesAsyncClient",
    "AddressDescriptor",
    "AuthorAttribution",
    "AutocompletePlacesRequest",
    "AutocompletePlacesResponse",
    "Circle",
    "ContentBlock",
    "ContextualContent",
    "EVChargeOptions",
    "EVConnectorType",
    "FuelOptions",
    "GetPhotoMediaRequest",
    "GetPlaceRequest",
    "Photo",
    "PhotoMedia",
    "Place",
    "PlacesClient",
    "Polyline",
    "PriceLevel",
    "PriceRange",
    "References",
    "Review",
    "RouteModifiers",
    "RoutingParameters",
    "RoutingPreference",
    "RoutingSummary",
    "SearchNearbyRequest",
    "SearchNearbyResponse",
    "SearchTextRequest",
    "SearchTextResponse",
    "TransitAgency",
    "TransitIcon",
    "TransitLine",
    "TransitStation",
    "TransitStop",
    "TravelMode",
)

api_core.check_python_version("google.maps.places_v1")
api_core.check_dependency_versions("google.maps.places_v1")
