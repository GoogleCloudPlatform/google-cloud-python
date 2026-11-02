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
        "TlsRoute",
        "ListTlsRoutesRequest",
        "ListTlsRoutesResponse",
        "GetTlsRouteRequest",
        "CreateTlsRouteRequest",
        "UpdateTlsRouteRequest",
        "DeleteTlsRouteRequest",
    },
)


class TlsRoute(proto.Message):
    r"""TlsRoute defines how traffic should be routed based on SNI
    and other matching L3 attributes.

    Attributes:
        name (str):
            Identifier. Name of the TlsRoute resource. It matches
            pattern
            ``projects/*/locations/*/tlsRoutes/tls_route_name>``.
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
        rules (MutableSequence[google.cloud.network_services_v1.types.TlsRoute.RouteRule]):
            Required. Rules that define how traffic is
            routed and handled. At least one RouteRule must
            be supplied. If there are multiple rules then
            the action taken will be the first rule to
            match.
        meshes (MutableSequence[str]):
            Optional. Meshes defines a list of meshes this TlsRoute is
            attached to, as one of the routing rules to route the
            requests served by the mesh.

            Each mesh reference should match the pattern:
            ``projects/*/locations/*/meshes/<mesh_name>``

            The attached Mesh should be of a type SIDECAR
        gateways (MutableSequence[str]):
            Optional. Gateways defines a list of gateways this TlsRoute
            is attached to, as one of the routing rules to route the
            requests served by the gateway.

            Each gateway reference should match the pattern:
            ``projects/*/locations/*/gateways/<gateway_name>``
        target_proxies (MutableSequence[str]):
            Optional. TargetProxies defines a list of TargetTcpProxies
            this TlsRoute is attached to, as one of the routing rules to
            route the requests served by the TargetTcpProxy.

            Each TargetTcpProxy reference should match the pattern:
            ``projects/*/locations/*/targetTcpProxies/<target_tcp_proxy_name>``
        labels (MutableMapping[str, str]):
            Optional. Set of label tags associated with
            the TlsRoute resource.
    """

    class RouteRule(proto.Message):
        r"""Specifies how to match traffic and how to route traffic when
        traffic is matched.

        Attributes:
            matches (MutableSequence[google.cloud.network_services_v1.types.TlsRoute.RouteMatch]):
                Required. RouteMatch defines the predicate
                used to match requests to a given action.
                Multiple match types are "OR"ed for evaluation.
                Atleast one RouteMatch must be supplied.
            action (google.cloud.network_services_v1.types.TlsRoute.RouteAction):
                Required. The detailed rule defining how to
                route matched traffic.
        """

        matches: MutableSequence["TlsRoute.RouteMatch"] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="TlsRoute.RouteMatch",
        )
        action: "TlsRoute.RouteAction" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="TlsRoute.RouteAction",
        )

    class RouteMatch(proto.Message):
        r"""RouteMatch defines the predicate used to match requests to a
        given action. Multiple match types are "AND"ed for evaluation.

        Attributes:
            sni_host (MutableSequence[str]):
                Optional. SNI (server name indicator) to match against. SNI
                will be matched against all wildcard domains, i.e.
                ``www.example.com`` will be first matched against
                ``www.example.com``, then ``*.example.com``, then ``*.com.``
                Partial wildcards are not supported, and values like
                \*w.example.com are invalid. At least one of sni_host and
                alpn is required. Up to 100 sni hosts across all matches can
                be set.
            alpn (MutableSequence[str]):
                Optional. ALPN (Application-Layer Protocol Negotiation) to
                match against. Examples: "http/1.1", "h2". At least one of
                sni_host and alpn is required. Up to 5 alpns across all
                matches can be set.
        """

        sni_host: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )
        alpn: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )

    class RouteAction(proto.Message):
        r"""The specifications for routing traffic and applying
        associated policies.

        Attributes:
            destinations (MutableSequence[google.cloud.network_services_v1.types.TlsRoute.RouteDestination]):
                Required. The destination services to which
                traffic should be forwarded. At least one
                destination service is required.
            idle_timeout (google.protobuf.duration_pb2.Duration):
                Optional. Specifies the idle timeout for the
                selected route. The idle timeout is defined as
                the period in which there are no bytes sent or
                received on either the upstream or downstream
                connection. If not set, the default idle timeout
                is 1 hour. If set to 0s, the timeout will be
                disabled.
        """

        destinations: MutableSequence["TlsRoute.RouteDestination"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=1,
                message="TlsRoute.RouteDestination",
            )
        )
        idle_timeout: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=4,
            message=duration_pb2.Duration,
        )

    class RouteDestination(proto.Message):
        r"""Describe the destination for traffic to be routed to.

        Attributes:
            service_name (str):
                Required. The URL of a BackendService to
                route traffic to.
            weight (int):
                Optional. Specifies the proportion of requests forwarded to
                the backend referenced by the service_name field. This is
                computed as:

                - weight/Sum(weights in destinations) Weights in all
                  destinations does not need to sum up to 100.
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
        number=8,
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
        number=6,
    )
    gateways: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )
    target_proxies: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=13,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=11,
    )


class ListTlsRoutesRequest(proto.Message):
    r"""Request used with the ListTlsRoutes method.

    Attributes:
        parent (str):
            Required. The project and location from which the TlsRoutes
            should be listed, specified in the format
            ``projects/*/locations/*``.
        page_size (int):
            Maximum number of TlsRoutes to return per
            call.
        page_token (str):
            The value returned by the last ``ListTlsRoutesResponse``
            Indicates that this is a continuation of a prior
            ``ListTlsRoutes`` call, and that the system should return
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


class ListTlsRoutesResponse(proto.Message):
    r"""Response returned by the ListTlsRoutes method.

    Attributes:
        tls_routes (MutableSequence[google.cloud.network_services_v1.types.TlsRoute]):
            List of TlsRoute resources.
        next_page_token (str):
            If there might be more results than those appearing in this
            response, then ``next_page_token`` is included. To get the
            next set of results, call this method again using the value
            of ``next_page_token`` as ``page_token``.
        unreachable (MutableSequence[str]):
            Unreachable resources. Populated when the request opts into
            [return_partial_success][google.cloud.networkservices.v1.ListTlsRoutesRequest.return_partial_success]
            and reading across collections e.g. when attempting to list
            all resources across all supported locations.
    """

    @property
    def raw_page(self):
        return self

    tls_routes: MutableSequence["TlsRoute"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="TlsRoute",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetTlsRouteRequest(proto.Message):
    r"""Request used by the GetTlsRoute method.

    Attributes:
        name (str):
            Required. A name of the TlsRoute to get. Must be in the
            format ``projects/*/locations/*/tlsRoutes/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateTlsRouteRequest(proto.Message):
    r"""Request used by the TlsRoute method.

    Attributes:
        parent (str):
            Required. The parent resource of the TlsRoute. Must be in
            the format ``projects/*/locations/*``.
        tls_route_id (str):
            Required. Short name of the TlsRoute resource
            to be created.
        tls_route (google.cloud.network_services_v1.types.TlsRoute):
            Required. TlsRoute resource to be created.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    tls_route_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    tls_route: "TlsRoute" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="TlsRoute",
    )


class UpdateTlsRouteRequest(proto.Message):
    r"""Request used by the UpdateTlsRoute method.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the TlsRoute resource by the update. The
            fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. If the user does not provide a mask
            then all fields will be overwritten.
        tls_route (google.cloud.network_services_v1.types.TlsRoute):
            Required. Updated TlsRoute resource.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    tls_route: "TlsRoute" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="TlsRoute",
    )


class DeleteTlsRouteRequest(proto.Message):
    r"""Request used by the DeleteTlsRoute method.

    Attributes:
        name (str):
            Required. A name of the TlsRoute to delete. Must be in the
            format ``projects/*/locations/*/tlsRoutes/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
