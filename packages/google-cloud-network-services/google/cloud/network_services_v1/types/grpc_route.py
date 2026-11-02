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
        "GrpcRoute",
        "ListGrpcRoutesRequest",
        "ListGrpcRoutesResponse",
        "GetGrpcRouteRequest",
        "CreateGrpcRouteRequest",
        "UpdateGrpcRouteRequest",
        "DeleteGrpcRouteRequest",
    },
)


class GrpcRoute(proto.Message):
    r"""GrpcRoute is the resource defining how gRPC traffic routed by
    a Mesh or Gateway resource is routed.

    Attributes:
        name (str):
            Identifier. Name of the GrpcRoute resource. It matches
            pattern
            ``projects/*/locations/*/grpcRoutes/<grpc_route_name>``
        self_link (str):
            Output only. Server-defined URL of this
            resource
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was updated.
        labels (MutableMapping[str, str]):
            Optional. Set of label tags associated with
            the GrpcRoute resource.
        description (str):
            Optional. A free-text description of the
            resource. Max length 1024 characters.
        hostnames (MutableSequence[str]):
            Required. Service hostnames with an optional port for which
            this route describes traffic.

            Format: [:]

            Hostname is the fully qualified domain name of a network
            host. This matches the RFC 1123 definition of a hostname
            with 2 notable exceptions:

            - IPs are not allowed.
            - A hostname may be prefixed with a wildcard label (``*.``).
              The wildcard label must appear by itself as the first
              label.

            Hostname can be "precise" which is a domain name without the
            terminating dot of a network host (e.g. ``foo.example.com``)
            or "wildcard", which is a domain name prefixed with a single
            wildcard label (e.g. ``*.example.com``).

            Note that as per RFC1035 and RFC1123, a label must consist
            of lower case alphanumeric characters or '-', and must start
            and end with an alphanumeric character. No other punctuation
            is allowed.

            The routes associated with a Mesh or Gateway must have
            unique hostnames. If you attempt to attach multiple routes
            with conflicting hostnames, the configuration will be
            rejected.

            For example, while it is acceptable for routes for the
            hostnames ``*.foo.bar.com`` and ``*.bar.com`` to be
            associated with the same route, it is not possible to
            associate two routes both with ``*.bar.com`` or both with
            ``bar.com``.

            If a port is specified, then gRPC clients must use the
            channel URI with the port to match this rule (i.e.
            "xds:///service:123"), otherwise they must supply the URI
            without a port (i.e. "xds:///service").
        meshes (MutableSequence[str]):
            Optional. Meshes defines a list of meshes this GrpcRoute is
            attached to, as one of the routing rules to route the
            requests served by the mesh.

            Each mesh reference should match the pattern:
            ``projects/*/locations/*/meshes/<mesh_name>``
        gateways (MutableSequence[str]):
            Optional. Gateways defines a list of gateways this GrpcRoute
            is attached to, as one of the routing rules to route the
            requests served by the gateway.

            Each gateway reference should match the pattern:
            ``projects/*/locations/*/gateways/<gateway_name>``
        rules (MutableSequence[google.cloud.network_services_v1.types.GrpcRoute.RouteRule]):
            Required. A list of detailed rules defining
            how to route traffic.
            Within a single GrpcRoute, the
            GrpcRoute.RouteAction associated with the first
            matching GrpcRoute.RouteRule will be executed.
            At least one rule must be supplied.
    """

    class MethodMatch(proto.Message):
        r"""Specifies a match against a method.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            type_ (google.cloud.network_services_v1.types.GrpcRoute.MethodMatch.Type):
                Optional. Specifies how to match against the
                name. If not specified, a default value of
                "EXACT" is used.
            grpc_service (str):
                Required. Name of the service to match
                against. If unspecified, will match all
                services.
            grpc_method (str):
                Required. Name of the method to match
                against. If unspecified, will match all methods.
            case_sensitive (bool):
                Optional. Specifies that matches are case sensitive. The
                default value is true. case_sensitive must not be used with
                a type of REGULAR_EXPRESSION.

                This field is a member of `oneof`_ ``_case_sensitive``.
        """

        class Type(proto.Enum):
            r"""The type of the match.

            Values:
                TYPE_UNSPECIFIED (0):
                    Unspecified.
                EXACT (1):
                    Will only match the exact name provided.
                REGULAR_EXPRESSION (2):
                    Will interpret grpc_method and grpc_service as regexes. RE2
                    syntax is supported.
            """

            TYPE_UNSPECIFIED = 0
            EXACT = 1
            REGULAR_EXPRESSION = 2

        type_: "GrpcRoute.MethodMatch.Type" = proto.Field(
            proto.ENUM,
            number=1,
            enum="GrpcRoute.MethodMatch.Type",
        )
        grpc_service: str = proto.Field(
            proto.STRING,
            number=2,
        )
        grpc_method: str = proto.Field(
            proto.STRING,
            number=3,
        )
        case_sensitive: bool = proto.Field(
            proto.BOOL,
            number=4,
            optional=True,
        )

    class HeaderMatch(proto.Message):
        r"""A match against a collection of headers.

        Attributes:
            type_ (google.cloud.network_services_v1.types.GrpcRoute.HeaderMatch.Type):
                Optional. Specifies how to match against the
                value of the header. If not specified, a default
                value of EXACT is used.
            key (str):
                Required. The key of the header.
            value (str):
                Required. The value of the header.
        """

        class Type(proto.Enum):
            r"""The type of match.

            Values:
                TYPE_UNSPECIFIED (0):
                    Unspecified.
                EXACT (1):
                    Will only match the exact value provided.
                REGULAR_EXPRESSION (2):
                    Will match paths conforming to the prefix
                    specified by value. RE2 syntax is supported.
            """

            TYPE_UNSPECIFIED = 0
            EXACT = 1
            REGULAR_EXPRESSION = 2

        type_: "GrpcRoute.HeaderMatch.Type" = proto.Field(
            proto.ENUM,
            number=1,
            enum="GrpcRoute.HeaderMatch.Type",
        )
        key: str = proto.Field(
            proto.STRING,
            number=2,
        )
        value: str = proto.Field(
            proto.STRING,
            number=3,
        )

    class RouteMatch(proto.Message):
        r"""Criteria for matching traffic. A RouteMatch will be
        considered to match when all supplied fields match.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            method (google.cloud.network_services_v1.types.GrpcRoute.MethodMatch):
                Optional. A gRPC method to match against. If
                this field is empty or omitted, will match all
                methods.

                This field is a member of `oneof`_ ``_method``.
            headers (MutableSequence[google.cloud.network_services_v1.types.GrpcRoute.HeaderMatch]):
                Optional. Specifies a collection of headers
                to match.
        """

        method: "GrpcRoute.MethodMatch" = proto.Field(
            proto.MESSAGE,
            number=1,
            optional=True,
            message="GrpcRoute.MethodMatch",
        )
        headers: MutableSequence["GrpcRoute.HeaderMatch"] = proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="GrpcRoute.HeaderMatch",
        )

    class Destination(proto.Message):
        r"""The destination to which traffic will be routed.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            service_name (str):
                Required. The URL of a destination service to
                which to route traffic. Must refer to either a
                BackendService or ServiceDirectoryService.

                This field is a member of `oneof`_ ``destination_type``.
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

                This field is a member of `oneof`_ ``_weight``.
        """

        service_name: str = proto.Field(
            proto.STRING,
            number=1,
            oneof="destination_type",
        )
        weight: int = proto.Field(
            proto.INT32,
            number=2,
            optional=True,
        )

    class FaultInjectionPolicy(proto.Message):
        r"""The specification for fault injection introduced into traffic
        to test the resiliency of clients to destination service
        failure. As part of fault injection, when clients send requests
        to a destination, delays can be introduced on a percentage of
        requests before sending those requests to the destination
        service. Similarly requests from clients can be aborted by for a
        percentage of requests.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            delay (google.cloud.network_services_v1.types.GrpcRoute.FaultInjectionPolicy.Delay):
                The specification for injecting delay to
                client requests.

                This field is a member of `oneof`_ ``_delay``.
            abort (google.cloud.network_services_v1.types.GrpcRoute.FaultInjectionPolicy.Abort):
                The specification for aborting to client
                requests.

                This field is a member of `oneof`_ ``_abort``.
        """

        class Delay(proto.Message):
            r"""Specification of how client requests are delayed as part of
            fault injection before being sent to a destination.


            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                fixed_delay (google.protobuf.duration_pb2.Duration):
                    Specify a fixed delay before forwarding the
                    request.

                    This field is a member of `oneof`_ ``_fixed_delay``.
                percentage (int):
                    The percentage of traffic on which delay will be injected.

                    The value must be between [0, 100]

                    This field is a member of `oneof`_ ``_percentage``.
            """

            fixed_delay: duration_pb2.Duration = proto.Field(
                proto.MESSAGE,
                number=1,
                optional=True,
                message=duration_pb2.Duration,
            )
            percentage: int = proto.Field(
                proto.INT32,
                number=2,
                optional=True,
            )

        class Abort(proto.Message):
            r"""Specification of how client requests are aborted as part of
            fault injection before being sent to a destination.


            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                http_status (int):
                    The HTTP status code used to abort the
                    request.
                    The value must be between 200 and 599 inclusive.

                    This field is a member of `oneof`_ ``_http_status``.
                percentage (int):
                    The percentage of traffic which will be aborted.

                    The value must be between [0, 100]

                    This field is a member of `oneof`_ ``_percentage``.
            """

            http_status: int = proto.Field(
                proto.INT32,
                number=1,
                optional=True,
            )
            percentage: int = proto.Field(
                proto.INT32,
                number=2,
                optional=True,
            )

        delay: "GrpcRoute.FaultInjectionPolicy.Delay" = proto.Field(
            proto.MESSAGE,
            number=1,
            optional=True,
            message="GrpcRoute.FaultInjectionPolicy.Delay",
        )
        abort: "GrpcRoute.FaultInjectionPolicy.Abort" = proto.Field(
            proto.MESSAGE,
            number=2,
            optional=True,
            message="GrpcRoute.FaultInjectionPolicy.Abort",
        )

    class StatefulSessionAffinityPolicy(proto.Message):
        r"""The specification for cookie-based stateful session affinity
        where the date plane supplies a “session cookie”  with the name
        "GSSA" which encodes a specific destination host and each
        request containing that cookie will be directed to that host as
        long as the destination host remains up and healthy.

        The gRPC proxyless mesh library or sidecar proxy will manage the
        session cookie but the client application code is responsible
        for copying the cookie from each RPC in the session to the next.

        Attributes:
            cookie_ttl (google.protobuf.duration_pb2.Duration):
                Required. The cookie TTL value for the
                Set-Cookie header generated by the data plane.
                The lifetime of the cookie may be set to a value
                from 0 to 86400 seconds (24 hours) inclusive.

                Set this to 0s to use a session cookie and
                disable cookie expiration.
        """

        cookie_ttl: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=1,
            message=duration_pb2.Duration,
        )

    class RetryPolicy(proto.Message):
        r"""The specifications for retries.
        Specifies one or more conditions for which this retry rule
        applies. Valid values are:

        Attributes:
            retry_conditions (MutableSequence[str]):
                - connect-failure: Router will retry on failures connecting
                  to Backend Services, for example due to connection
                  timeouts.
                - refused-stream: Router will retry if the backend service
                  resets the stream with a REFUSED_STREAM error code. This
                  reset type indicates that it is safe to retry.
                - cancelled: Router will retry if the gRPC status code in
                  the response header is set to cancelled
                - deadline-exceeded: Router will retry if the gRPC status
                  code in the response header is set to deadline-exceeded
                - resource-exhausted: Router will retry if the gRPC status
                  code in the response header is set to resource-exhausted
                - unavailable: Router will retry if the gRPC status code in
                  the response header is set to unavailable
            num_retries (int):
                Specifies the allowed number of retries. This
                number must be > 0. If not specified, default to
                1.
        """

        retry_conditions: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )
        num_retries: int = proto.Field(
            proto.UINT32,
            number=2,
        )

    class RouteAction(proto.Message):
        r"""Specifies how to route matched traffic.

        Attributes:
            destinations (MutableSequence[google.cloud.network_services_v1.types.GrpcRoute.Destination]):
                Optional. The destination services to which
                traffic should be forwarded. If multiple
                destinations are specified, traffic will be
                split between Backend Service(s) according to
                the weight field of these destinations.
            fault_injection_policy (google.cloud.network_services_v1.types.GrpcRoute.FaultInjectionPolicy):
                Optional. The specification for fault injection introduced
                into traffic to test the resiliency of clients to
                destination service failure. As part of fault injection,
                when clients send requests to a destination, delays can be
                introduced on a percentage of requests before sending those
                requests to the destination service. Similarly requests from
                clients can be aborted by for a percentage of requests.

                timeout and retry_policy will be ignored by clients that are
                configured with a fault_injection_policy
            timeout (google.protobuf.duration_pb2.Duration):
                Optional. Specifies the timeout for selected
                route. Timeout is computed from the time the
                request has been fully processed (i.e. end of
                stream) up until the response has been
                completely processed. Timeout includes all
                retries.
            retry_policy (google.cloud.network_services_v1.types.GrpcRoute.RetryPolicy):
                Optional. Specifies the retry policy
                associated with this route.
            stateful_session_affinity (google.cloud.network_services_v1.types.GrpcRoute.StatefulSessionAffinityPolicy):
                Optional. Specifies cookie-based stateful
                session affinity.
            idle_timeout (google.protobuf.duration_pb2.Duration):
                Optional. Specifies the idle timeout for the
                selected route. The idle timeout is defined as
                the period in which there are no bytes sent or
                received on either the upstream or downstream
                connection. If not set, the default idle timeout
                is 1 hour. If set to 0s, the timeout will be
                disabled.
        """

        destinations: MutableSequence["GrpcRoute.Destination"] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="GrpcRoute.Destination",
        )
        fault_injection_policy: "GrpcRoute.FaultInjectionPolicy" = proto.Field(
            proto.MESSAGE,
            number=3,
            message="GrpcRoute.FaultInjectionPolicy",
        )
        timeout: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=7,
            message=duration_pb2.Duration,
        )
        retry_policy: "GrpcRoute.RetryPolicy" = proto.Field(
            proto.MESSAGE,
            number=8,
            message="GrpcRoute.RetryPolicy",
        )
        stateful_session_affinity: "GrpcRoute.StatefulSessionAffinityPolicy" = (
            proto.Field(
                proto.MESSAGE,
                number=11,
                message="GrpcRoute.StatefulSessionAffinityPolicy",
            )
        )
        idle_timeout: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=12,
            message=duration_pb2.Duration,
        )

    class RouteRule(proto.Message):
        r"""Describes how to route traffic.

        Attributes:
            matches (MutableSequence[google.cloud.network_services_v1.types.GrpcRoute.RouteMatch]):
                Optional. Matches define conditions used for
                matching the rule against incoming gRPC
                requests. Each match is independent, i.e. this
                rule will be matched if ANY one of the matches
                is satisfied.  If no matches field is specified,
                this rule will unconditionally match traffic.
            action (google.cloud.network_services_v1.types.GrpcRoute.RouteAction):
                Required. A detailed rule defining how to
                route traffic. This field is required.
        """

        matches: MutableSequence["GrpcRoute.RouteMatch"] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="GrpcRoute.RouteMatch",
        )
        action: "GrpcRoute.RouteAction" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="GrpcRoute.RouteAction",
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    self_link: str = proto.Field(
        proto.STRING,
        number=12,
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
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    description: str = proto.Field(
        proto.STRING,
        number=5,
    )
    hostnames: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    meshes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=9,
    )
    gateways: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=10,
    )
    rules: MutableSequence[RouteRule] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message=RouteRule,
    )


class ListGrpcRoutesRequest(proto.Message):
    r"""Request used with the ListGrpcRoutes method.

    Attributes:
        parent (str):
            Required. The project and location from which the GrpcRoutes
            should be listed, specified in the format
            ``projects/*/locations/*``.
        page_size (int):
            Maximum number of GrpcRoutes to return per
            call.
        page_token (str):
            The value returned by the last ``ListGrpcRoutesResponse``
            Indicates that this is a continuation of a prior
            ``ListGrpcRoutes`` call, and that the system should return
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


class ListGrpcRoutesResponse(proto.Message):
    r"""Response returned by the ListGrpcRoutes method.

    Attributes:
        grpc_routes (MutableSequence[google.cloud.network_services_v1.types.GrpcRoute]):
            List of GrpcRoute resources.
        next_page_token (str):
            If there might be more results than those appearing in this
            response, then ``next_page_token`` is included. To get the
            next set of results, call this method again using the value
            of ``next_page_token`` as ``page_token``.
        unreachable (MutableSequence[str]):
            Unreachable resources. Populated when the request opts into
            [return_partial_success][google.cloud.networkservices.v1.ListGrpcRoutesRequest.return_partial_success]
            and reading across collections e.g. when attempting to list
            all resources across all supported locations.
    """

    @property
    def raw_page(self):
        return self

    grpc_routes: MutableSequence["GrpcRoute"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="GrpcRoute",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetGrpcRouteRequest(proto.Message):
    r"""Request used by the GetGrpcRoute method.

    Attributes:
        name (str):
            Required. A name of the GrpcRoute to get. Must be in the
            format ``projects/*/locations/*/grpcRoutes/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateGrpcRouteRequest(proto.Message):
    r"""Request used by the CreateGrpcRoute method.

    Attributes:
        parent (str):
            Required. The parent resource of the GrpcRoute. Must be in
            the format ``projects/*/locations/*``.
        grpc_route_id (str):
            Required. Short name of the GrpcRoute
            resource to be created.
        grpc_route (google.cloud.network_services_v1.types.GrpcRoute):
            Required. GrpcRoute resource to be created.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    grpc_route_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    grpc_route: "GrpcRoute" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="GrpcRoute",
    )


class UpdateGrpcRouteRequest(proto.Message):
    r"""Request used by the UpdateGrpcRoute method.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the GrpcRoute resource by the update. The
            fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. If the user does not provide a mask
            then all fields will be overwritten.
        grpc_route (google.cloud.network_services_v1.types.GrpcRoute):
            Required. Updated GrpcRoute resource.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    grpc_route: "GrpcRoute" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="GrpcRoute",
    )


class DeleteGrpcRouteRequest(proto.Message):
    r"""Request used by the DeleteGrpcRoute method.

    Attributes:
        name (str):
            Required. A name of the GrpcRoute to delete. Must be in the
            format ``projects/*/locations/*/grpcRoutes/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
