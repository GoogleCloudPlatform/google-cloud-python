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

import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.networkservices.v1",
    manifest={
        "TcpRoute",
        "ListTcpRoutesRequest",
        "ListTcpRoutesResponse",
        "GetTcpRouteRequest",
        "CreateTcpRouteRequest",
        "UpdateTcpRouteRequest",
        "DeleteTcpRouteRequest",
    },
)


class TcpRoute(proto.Message):
    r"""TcpRoute is the resource defining how TCP traffic should be
    routed by a Mesh/Gateway resource.

    Attributes:
        name (str):
            Identifier. Name of the TcpRoute resource. It matches
            pattern
            ``projects/*/locations/*/tcpRoutes/tcp_route_name>``.
        self_link (str):
            Output only. Server-defined URL of this
            resource
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was updated.
        description (str):
            Optional. A free-text description of the
            resource. Max length 1024 characters.
        rules (MutableSequence[google.cloud.network_services_v1.types.TcpRoute.RouteRule]):
            Required. Rules that define how traffic is
            routed and handled. At least one RouteRule must
            be supplied. If there are multiple rules then
            the action taken will be the first rule to
            match.
        meshes (MutableSequence[str]):
            Optional. Meshes defines a list of meshes this TcpRoute is
            attached to, as one of the routing rules to route the
            requests served by the mesh.

            Each mesh reference should match the pattern:
            ``projects/*/locations/*/meshes/<mesh_name>``

            The attached Mesh should be of a type SIDECAR
        gateways (MutableSequence[str]):
            Optional. Gateways defines a list of gateways this TcpRoute
            is attached to, as one of the routing rules to route the
            requests served by the gateway.

            Each gateway reference should match the pattern:
            ``projects/*/locations/*/gateways/<gateway_name>``
        labels (MutableMapping[str, str]):
            Optional. Set of label tags associated with
            the TcpRoute resource.
    """

    class RouteRule(proto.Message):
        r"""Specifies how to match traffic and how to route traffic when
        traffic is matched.

        Attributes:
            matches (MutableSequence[google.cloud.network_services_v1.types.TcpRoute.RouteMatch]):
                Optional. RouteMatch defines the predicate
                used to match requests to a given action.
                Multiple match types are "OR"ed for evaluation.
                If no routeMatch field is specified, this rule
                will unconditionally match traffic.
            action (google.cloud.network_services_v1.types.TcpRoute.RouteAction):
                Required. The detailed rule defining how to
                route matched traffic.
        """

        matches: MutableSequence["TcpRoute.RouteMatch"] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="TcpRoute.RouteMatch",
        )
        action: "TcpRoute.RouteAction" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="TcpRoute.RouteAction",
        )

    class RouteMatch(proto.Message):
        r"""RouteMatch defines the predicate used to match requests to a
        given action. Multiple match types are "OR"ed for evaluation. If
        no routeMatch field is specified, this rule will unconditionally
        match traffic.

        Attributes:
            address (str):
                Required. Must be specified in the CIDR range
                format. A CIDR range consists of an IP Address
                and a prefix length to construct the subnet
                mask. By default, the prefix length is 32 (i.e.
                matches a single IP address). Only IPV4
                addresses are supported. Examples: "10.0.0.1" -
                matches against this exact IP address.
                "10.0.0.0/8" - matches against any IP address
                within the 10.0.0.0 subnet and 255.255.255.0
                mask. "0.0.0.0/0"
                - matches against any IP address'.
            port (str):
                Required. Specifies the destination port to
                match against.
        """

        address: str = proto.Field(
            proto.STRING,
            number=1,
        )
        port: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class RouteAction(proto.Message):
        r"""The specifications for routing traffic and applying
        associated policies.

        Attributes:
            destinations (MutableSequence[google.cloud.network_services_v1.types.TcpRoute.RouteDestination]):
                Optional. The destination services to which
                traffic should be forwarded. At least one
                destination service is required. Only one of
                route destination or original destination can be
                set.
            original_destination (bool):
                Optional. If true, Router will use the
                destination IP and port of the original
                connection as the destination of the request.
                Default is false. Only one of route destinations
                or original destination can be set.
            idle_timeout (google.protobuf.duration_pb2.Duration):
                Optional. Specifies the idle timeout for the
                selected route. The idle timeout is defined as
                the period in which there are no bytes sent or
                received on either the upstream or downstream
                connection. If not set, the default idle timeout
                is 30 seconds. If set to 0s, the timeout will be
                disabled.
        """

        destinations: MutableSequence["TcpRoute.RouteDestination"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=1,
                message="TcpRoute.RouteDestination",
            )
        )
        original_destination: bool = proto.Field(
            proto.BOOL,
            number=3,
        )
        idle_timeout: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=5,
            message=duration_pb2.Duration,
        )

    class RouteDestination(proto.Message):
        r"""Describe the destination for traffic to be routed to.

        Attributes:
            service_name (str):
                Required. The URL of a BackendService to
                route traffic to.
            weight (int):
                Optional. Specifies the proportion of
                requests forwarded to the backend referenced by
                the serviceName field. This is computed as:

                - weight/Sum(weights in this destination list).
                  For non-zero values, there may be some epsilon
                  from the exact proportion defined here
                  depending on the precision an implementation
                  supports.

                If only one serviceName is specified and it has
                a weight greater than 0, 100% of the traffic is
                forwarded to that backend.

                If weights are specified for any one service
                name, they need to be specified for all of them.

                If weights are unspecified for all services,
                then, traffic is distributed in equal
                proportions to all of them.
        """

        service_name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        weight: int = proto.Field(
            proto.INT32,
            number=2,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    self_link: str = proto.Field(
        proto.STRING,
        number=11,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    description: str = proto.Field(
        proto.STRING,
        number=4,
    )
    rules: MutableSequence[RouteRule] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message=RouteRule,
    )
    meshes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=8,
    )
    gateways: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=9,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=10,
    )


class ListTcpRoutesRequest(proto.Message):
    r"""Request used with the ListTcpRoutes method.

    Attributes:
        parent (str):
            Required. The project and location from which the TcpRoutes
            should be listed, specified in the format
            ``projects/*/locations/*``.
        page_size (int):
            Maximum number of TcpRoutes to return per
            call.
        page_token (str):
            The value returned by the last ``ListTcpRoutesResponse``
            Indicates that this is a continuation of a prior
            ``ListTcpRoutes`` call, and that the system should return
            the next page of data.
        return_partial_success (bool):
            Optional. If true, allow partial responses
            for multi-regional Aggregated List requests.
            Otherwise if one of the locations is down or
            unreachable, the Aggregated List request will
            fail.
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
    return_partial_success: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class ListTcpRoutesResponse(proto.Message):
    r"""Response returned by the ListTcpRoutes method.

    Attributes:
        tcp_routes (MutableSequence[google.cloud.network_services_v1.types.TcpRoute]):
            List of TcpRoute resources.
        next_page_token (str):
            If there might be more results than those appearing in this
            response, then ``next_page_token`` is included. To get the
            next set of results, call this method again using the value
            of ``next_page_token`` as ``page_token``.
        unreachable (MutableSequence[str]):
            Unreachable resources. Populated when the request opts into
            [return_partial_success][google.cloud.networkservices.v1.ListTcpRoutesRequest.return_partial_success]
            and reading across collections e.g. when attempting to list
            all resources across all supported locations.
    """

    @property
    def raw_page(self):
        return self

    tcp_routes: MutableSequence["TcpRoute"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="TcpRoute",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetTcpRouteRequest(proto.Message):
    r"""Request used by the GetTcpRoute method.

    Attributes:
        name (str):
            Required. A name of the TcpRoute to get. Must be in the
            format ``projects/*/locations/*/tcpRoutes/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateTcpRouteRequest(proto.Message):
    r"""Request used by the TcpRoute method.

    Attributes:
        parent (str):
            Required. The parent resource of the TcpRoute. Must be in
            the format ``projects/*/locations/*``.
        tcp_route_id (str):
            Required. Short name of the TcpRoute resource
            to be created.
        tcp_route (google.cloud.network_services_v1.types.TcpRoute):
            Required. TcpRoute resource to be created.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    tcp_route_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    tcp_route: "TcpRoute" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="TcpRoute",
    )


class UpdateTcpRouteRequest(proto.Message):
    r"""Request used by the UpdateTcpRoute method.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the TcpRoute resource by the update. The
            fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. If the user does not provide a mask
            then all fields will be overwritten.
        tcp_route (google.cloud.network_services_v1.types.TcpRoute):
            Required. Updated TcpRoute resource.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    tcp_route: "TcpRoute" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="TcpRoute",
    )


class DeleteTcpRouteRequest(proto.Message):
    r"""Request used by the DeleteTcpRoute method.

    Attributes:
        name (str):
            Required. A name of the TcpRoute to delete. Must be in the
            format ``projects/*/locations/*/tcpRoutes/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
