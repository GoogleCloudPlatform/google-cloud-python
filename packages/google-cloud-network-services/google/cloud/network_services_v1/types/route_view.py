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
from __future__ import annotations

from typing import MutableMapping, MutableSequence

import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.networkservices.v1",
    manifest={
        "GatewayRouteView",
        "MeshRouteView",
        "GetGatewayRouteViewRequest",
        "GetMeshRouteViewRequest",
        "ListGatewayRouteViewsRequest",
        "ListMeshRouteViewsRequest",
        "ListGatewayRouteViewsResponse",
        "ListMeshRouteViewsResponse",
    },
)


class GatewayRouteView(proto.Message):
    r"""GatewayRouteView defines view-only resource for Routes to a
    Gateway

    Attributes:
        name (str):
            Output only. Identifier. Full path name of the
            GatewayRouteView resource. Format:
            projects/{project_number}/locations/{location}/gateways/{gateway}/routeViews/{route_view}
        route_project_number (int):
            Output only. Project number where the route
            exists.
        route_location (str):
            Output only. Location where the route exists.
        route_type (str):
            Output only. Type of the route:
            HttpRoute,GrpcRoute,TcpRoute, or TlsRoute
        route_id (str):
            Output only. The resource id for the route.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    route_project_number: int = proto.Field(
        proto.INT64,
        number=2,
    )
    route_location: str = proto.Field(
        proto.STRING,
        number=3,
    )
    route_type: str = proto.Field(
        proto.STRING,
        number=4,
    )
    route_id: str = proto.Field(
        proto.STRING,
        number=5,
    )


class MeshRouteView(proto.Message):
    r"""MeshRouteView defines view-only resource for Routes to a Mesh

    Attributes:
        name (str):
            Output only. Identifier. Full path name of the MeshRouteView
            resource. Format:
            projects/{project}/locations/{location}/meshes/{mesh}/routeViews/{route_view}
        route_project_number (int):
            Output only. Project number where the route
            exists.
        route_location (str):
            Output only. Location where the route exists.
        route_type (str):
            Output only. Type of the route:
            HttpRoute,GrpcRoute,TcpRoute, or TlsRoute
        route_id (str):
            Output only. The resource id for the route.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    route_project_number: int = proto.Field(
        proto.INT64,
        number=2,
    )
    route_location: str = proto.Field(
        proto.STRING,
        number=3,
    )
    route_type: str = proto.Field(
        proto.STRING,
        number=4,
    )
    route_id: str = proto.Field(
        proto.STRING,
        number=5,
    )


class GetGatewayRouteViewRequest(proto.Message):
    r"""Request used with the GetGatewayRouteView method.

    Attributes:
        name (str):
            Required. Name of the GatewayRouteView resource. Formats:
            projects/{project}/locations/{location}/gateways/{gateway}/routeViews/{route_view}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetMeshRouteViewRequest(proto.Message):
    r"""Request used with the GetMeshRouteView method.

    Attributes:
        name (str):
            Required. Name of the MeshRouteView resource. Format:
            projects/{project}/locations/{location}/meshes/{mesh}/routeViews/{route_view}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListGatewayRouteViewsRequest(proto.Message):
    r"""Request used with the ListGatewayRouteViews method.

    Attributes:
        parent (str):
            Required. The Gateway to which a Route is
            associated. Formats:

            projects/{project}/locations/{location}/gateways/{gateway}
        page_size (int):
            Maximum number of GatewayRouteViews to return
            per call.
        page_token (str):
            The value returned by the last
            ``ListGatewayRouteViewsResponse`` Indicates that this is a
            continuation of a prior ``ListGatewayRouteViews`` call, and
            that the system should return the next page of data.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListMeshRouteViewsRequest(proto.Message):
    r"""Request used with the ListMeshRouteViews method.

    Attributes:
        parent (str):
            Required. The Mesh to which a Route is
            associated. Format:

            projects/{project}/locations/{location}/meshes/{mesh}
        page_size (int):
            Maximum number of MeshRouteViews to return
            per call.
        page_token (str):
            The value returned by the last
            ``ListMeshRouteViewsResponse`` Indicates that this is a
            continuation of a prior ``ListMeshRouteViews`` call, and
            that the system should return the next page of data.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListGatewayRouteViewsResponse(proto.Message):
    r"""Response returned by the ListGatewayRouteViews method.

    Attributes:
        gateway_route_views (MutableSequence[google.cloud.network_services_v1.types.GatewayRouteView]):
            List of GatewayRouteView resources.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Unreachable resources. Populated when the
            request attempts to list all resources across
            all supported locations, while some locations
            are temporarily unavailable.
    """

    @property
    def raw_page(self):
        return self

    gateway_route_views: MutableSequence["GatewayRouteView"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="GatewayRouteView",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class ListMeshRouteViewsResponse(proto.Message):
    r"""Response returned by the ListMeshRouteViews method.

    Attributes:
        mesh_route_views (MutableSequence[google.cloud.network_services_v1.types.MeshRouteView]):
            List of MeshRouteView resources.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Unreachable resources. Populated when the
            request attempts to list all resources across
            all supported locations, while some locations
            are temporarily unavailable.
    """

    @property
    def raw_page(self):
        return self

    mesh_route_views: MutableSequence["MeshRouteView"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="MeshRouteView",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
