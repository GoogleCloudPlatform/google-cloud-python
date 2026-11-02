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
from google.cloud.beyondcorp_clientconnectorservices import (
    gapic_version as package_version,
)

__version__ = package_version.__version__


from google.cloud.beyondcorp_clientconnectorservices_v1.services.client_connector_services_service.async_client import (
    ClientConnectorServicesServiceAsyncClient,
)
from google.cloud.beyondcorp_clientconnectorservices_v1.services.client_connector_services_service.client import (
    ClientConnectorServicesServiceClient,
)
from google.cloud.beyondcorp_clientconnectorservices_v1.types.client_connector_services_service import (
    ClientConnectorService,
    ClientConnectorServiceOperationMetadata,
    CreateClientConnectorServiceRequest,
    DeleteClientConnectorServiceRequest,
    GetClientConnectorServiceRequest,
    ListClientConnectorServicesRequest,
    ListClientConnectorServicesResponse,
    UpdateClientConnectorServiceRequest,
)

__all__ = (
    "ClientConnectorServicesServiceClient",
    "ClientConnectorServicesServiceAsyncClient",
    "ClientConnectorService",
    "ClientConnectorServiceOperationMetadata",
    "CreateClientConnectorServiceRequest",
    "DeleteClientConnectorServiceRequest",
    "GetClientConnectorServiceRequest",
    "ListClientConnectorServicesRequest",
    "ListClientConnectorServicesResponse",
    "UpdateClientConnectorServiceRequest",
)
