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
from google.maps.geocode import gapic_version as package_version

__version__ = package_version.__version__


from google.maps.geocode_v4.services.destination_service.async_client import (
    DestinationServiceAsyncClient,
)
from google.maps.geocode_v4.services.destination_service.client import (
    DestinationServiceClient,
)
from google.maps.geocode_v4.services.geocode_service.async_client import (
    GeocodeServiceAsyncClient,
)
from google.maps.geocode_v4.services.geocode_service.client import GeocodeServiceClient
from google.maps.geocode_v4.types.destination_service import (
    Destination,
    Entrance,
    Landmark,
    NavigationPoint,
    PlaceView,
    SearchDestinationsRequest,
    SearchDestinationsResponse,
)
from google.maps.geocode_v4.types.geocode_service import (
    GeocodeAddressRequest,
    GeocodeAddressResponse,
    GeocodeLocationRequest,
    GeocodeLocationResponse,
    GeocodePlaceRequest,
    GeocodeResult,
    PlusCode,
)

__all__ = (
    "DestinationServiceClient",
    "DestinationServiceAsyncClient",
    "GeocodeServiceClient",
    "GeocodeServiceAsyncClient",
    "Destination",
    "Entrance",
    "Landmark",
    "NavigationPoint",
    "PlaceView",
    "SearchDestinationsRequest",
    "SearchDestinationsResponse",
    "GeocodeAddressRequest",
    "GeocodeAddressResponse",
    "GeocodeLocationRequest",
    "GeocodeLocationResponse",
    "GeocodePlaceRequest",
    "GeocodeResult",
    "PlusCode",
)
