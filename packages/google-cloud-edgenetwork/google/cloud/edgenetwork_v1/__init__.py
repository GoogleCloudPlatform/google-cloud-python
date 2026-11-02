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

from google.cloud.edgenetwork_v1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.edgenetwork_v1.services.edge_network",
    "google.cloud.edgenetwork_v1.types.resources",
    "google.cloud.edgenetwork_v1.types.service",
}


from .services.edge_network import EdgeNetworkAsyncClient, EdgeNetworkClient
from .types.resources import (
    Interconnect,
    InterconnectAttachment,
    InterconnectDiagnostics,
    LinkLayerAddress,
    Network,
    RemotePeeringNetworkType,
    ResourceState,
    Router,
    RouterStatus,
    Subnet,
    SubnetStatus,
    Zone,
)
from .types.service import (
    CreateInterconnectAttachmentRequest,
    CreateNetworkRequest,
    CreateRouterRequest,
    CreateSubnetRequest,
    DeleteInterconnectAttachmentRequest,
    DeleteNetworkRequest,
    DeleteRouterRequest,
    DeleteSubnetRequest,
    DiagnoseInterconnectRequest,
    DiagnoseInterconnectResponse,
    DiagnoseNetworkRequest,
    DiagnoseNetworkResponse,
    DiagnoseRouterRequest,
    DiagnoseRouterResponse,
    GetInterconnectAttachmentRequest,
    GetInterconnectRequest,
    GetNetworkRequest,
    GetRouterRequest,
    GetSubnetRequest,
    GetZoneRequest,
    InitializeZoneRequest,
    InitializeZoneResponse,
    ListInterconnectAttachmentsRequest,
    ListInterconnectAttachmentsResponse,
    ListInterconnectsRequest,
    ListInterconnectsResponse,
    ListNetworksRequest,
    ListNetworksResponse,
    ListRoutersRequest,
    ListRoutersResponse,
    ListSubnetsRequest,
    ListSubnetsResponse,
    ListZonesRequest,
    ListZonesResponse,
    OperationMetadata,
    UpdateRouterRequest,
    UpdateSubnetRequest,
)

__all__ = (
    "EdgeNetworkAsyncClient",
    "CreateInterconnectAttachmentRequest",
    "CreateNetworkRequest",
    "CreateRouterRequest",
    "CreateSubnetRequest",
    "DeleteInterconnectAttachmentRequest",
    "DeleteNetworkRequest",
    "DeleteRouterRequest",
    "DeleteSubnetRequest",
    "DiagnoseInterconnectRequest",
    "DiagnoseInterconnectResponse",
    "DiagnoseNetworkRequest",
    "DiagnoseNetworkResponse",
    "DiagnoseRouterRequest",
    "DiagnoseRouterResponse",
    "EdgeNetworkClient",
    "GetInterconnectAttachmentRequest",
    "GetInterconnectRequest",
    "GetNetworkRequest",
    "GetRouterRequest",
    "GetSubnetRequest",
    "GetZoneRequest",
    "InitializeZoneRequest",
    "InitializeZoneResponse",
    "Interconnect",
    "InterconnectAttachment",
    "InterconnectDiagnostics",
    "LinkLayerAddress",
    "ListInterconnectAttachmentsRequest",
    "ListInterconnectAttachmentsResponse",
    "ListInterconnectsRequest",
    "ListInterconnectsResponse",
    "ListNetworksRequest",
    "ListNetworksResponse",
    "ListRoutersRequest",
    "ListRoutersResponse",
    "ListSubnetsRequest",
    "ListSubnetsResponse",
    "ListZonesRequest",
    "ListZonesResponse",
    "Network",
    "OperationMetadata",
    "RemotePeeringNetworkType",
    "ResourceState",
    "Router",
    "RouterStatus",
    "Subnet",
    "SubnetStatus",
    "UpdateRouterRequest",
    "UpdateSubnetRequest",
    "Zone",
)

api_core.check_python_version("google.cloud.edgenetwork_v1")
api_core.check_dependency_versions("google.cloud.edgenetwork_v1")
