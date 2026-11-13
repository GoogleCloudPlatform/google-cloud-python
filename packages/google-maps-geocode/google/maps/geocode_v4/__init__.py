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

from google.maps.geocode_v4 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.maps.geocode_v4.services.destination_service",
    "google.maps.geocode_v4.services.geocode_service",
    "google.maps.geocode_v4.types.destination_service",
    "google.maps.geocode_v4.types.geocode_service",
}


from .services.destination_service import (
    DestinationServiceAsyncClient,
    DestinationServiceClient,
)
from .services.geocode_service import GeocodeServiceAsyncClient, GeocodeServiceClient
from .types.destination_service import (
    Destination,
    Entrance,
    Landmark,
    NavigationPoint,
    PlaceView,
    SearchDestinationsRequest,
    SearchDestinationsResponse,
)
from .types.geocode_service import (
    GeocodeAddressRequest,
    GeocodeAddressResponse,
    GeocodeLocationRequest,
    GeocodeLocationResponse,
    GeocodePlaceRequest,
    GeocodeResult,
    PlusCode,
)

__all__ = (
    "DestinationServiceAsyncClient",
    "GeocodeServiceAsyncClient",
    "Destination",
    "DestinationServiceClient",
    "Entrance",
    "GeocodeAddressRequest",
    "GeocodeAddressResponse",
    "GeocodeLocationRequest",
    "GeocodeLocationResponse",
    "GeocodePlaceRequest",
    "GeocodeResult",
    "GeocodeServiceClient",
    "Landmark",
    "NavigationPoint",
    "PlaceView",
    "PlusCode",
    "SearchDestinationsRequest",
    "SearchDestinationsResponse",
)

api_core.check_python_version("google.maps.geocode_v4")
api_core.check_dependency_versions("google.maps.geocode_v4")
