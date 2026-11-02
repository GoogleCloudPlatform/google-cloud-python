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
        "HttpRoute",
        "ListHttpRoutesRequest",
        "ListHttpRoutesResponse",
        "GetHttpRouteRequest",
        "CreateHttpRouteRequest",
        "UpdateHttpRouteRequest",
        "DeleteHttpRouteRequest",
    },
)


class HttpRoute(proto.Message):
    r"""HttpRoute is the resource defining how HTTP traffic should be
    routed by a Mesh or Gateway resource.

    Attributes:
        name (str):
            Identifier. Name of the HttpRoute resource. It matches
            pattern
            ``projects/*/locations/*/httpRoutes/http_route_name>``.
        self_link (str):
            Output only. Server-defined URL of this
            resource
        description (str):
            Optional. A free-text description of the
            resource. Max length 1024 characters.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was updated.
        hostnames (MutableSequence[str]):
            Required. Hostnames define a set of hosts that should match
            against the HTTP host header to select a HttpRoute to
            process the request. Hostname is the fully qualified domain
            name of a network host, as defined by RFC 1123 with the
            exception that:

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

            The routes associated with a Mesh or Gateways must have
            unique hostnames. If you attempt to attach multiple routes
            with conflicting hostnames, the configuration will be
            rejected.

            For example, while it is acceptable for routes for the
            hostnames ``*.foo.bar.com`` and ``*.bar.com`` to be
            associated with the same Mesh (or Gateways under the same
            scope), it is not possible to associate two routes both with
            ``*.bar.com`` or both with ``bar.com``.
        meshes (MutableSequence[str]):
            Optional. Meshes defines a list of meshes this HttpRoute is
            attached to, as one of the routing rules to route the
            requests served by the mesh.

            Each mesh reference should match the pattern:
            ``projects/*/locations/*/meshes/<mesh_name>``

            The attached Mesh should be of a type SIDECAR
        gateways (MutableSequence[str]):
            Optional. Gateways defines a list of gateways this HttpRoute
            is attached to, as one of the routing rules to route the
            requests served by the gateway.

            Each gateway reference should match the pattern:
            ``projects/*/locations/*/gateways/<gateway_name>``
        labels (MutableMapping[str, str]):
            Optional. Set of label tags associated with
            the HttpRoute resource.
        rules (MutableSequence[google.cloud.network_services_v1.types.HttpRoute.RouteRule]):
            Required. Rules that define how traffic is
            routed and handled. Rules will be matched
            sequentially based on the RouteMatch specified
            for the rule.
    """

    class HeaderMatch(proto.Message):
        r"""Specifies how to select a route rule based on HTTP request
        headers.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            exact_match (str):
                The value of the header should match exactly the content of
                exact_match.

                This field is a member of `oneof`_ ``MatchType``.
            regex_match (str):
                The value of the header must match the regular expression
                specified in regex_match. For regular expression grammar,
                please see: https://github.com/google/re2/wiki/Syntax

                This field is a member of `oneof`_ ``MatchType``.
            prefix_match (str):
                The value of the header must start with the contents of
                prefix_match.

                This field is a member of `oneof`_ ``MatchType``.
            present_match (bool):
                A header with header_name must exist. The match takes place
                whether or not the header has a value.

                This field is a member of `oneof`_ ``MatchType``.
            suffix_match (str):
                The value of the header must end with the contents of
                suffix_match.

                This field is a member of `oneof`_ ``MatchType``.
            range_match (google.cloud.network_services_v1.types.HttpRoute.HeaderMatch.IntegerRange):
                If specified, the rule will match if the
                request header value is within the range.

                This field is a member of `oneof`_ ``MatchType``.
            header (str):
                The name of the HTTP header to match against.
            invert_match (bool):
                If specified, the match result will be
                inverted before checking. Default value is set
                to false.
        """

        class IntegerRange(proto.Message):
            r"""Represents an integer value range.

            Attributes:
                start (int):
                    Start of the range (inclusive)
                end (int):
                    End of the range (exclusive)
            """

            start: int = proto.Field(
                proto.INT32,
                number=1,
            )
            end: int = proto.Field(
                proto.INT32,
                number=2,
            )

        exact_match: str = proto.Field(
            proto.STRING,
            number=2,
            oneof="MatchType",
        )
        regex_match: str = proto.Field(
            proto.STRING,
            number=3,
            oneof="MatchType",
        )
        prefix_match: str = proto.Field(
            proto.STRING,
            number=4,
            oneof="MatchType",
        )
        present_match: bool = proto.Field(
            proto.BOOL,
            number=5,
            oneof="MatchType",
        )
        suffix_match: str = proto.Field(
            proto.STRING,
            number=6,
            oneof="MatchType",
        )
        range_match: "HttpRoute.HeaderMatch.IntegerRange" = proto.Field(
            proto.MESSAGE,
            number=7,
            oneof="MatchType",
            message="HttpRoute.HeaderMatch.IntegerRange",
        )
        header: str = proto.Field(
            proto.STRING,
            number=1,
        )
        invert_match: bool = proto.Field(
            proto.BOOL,
            number=8,
        )

    class QueryParameterMatch(proto.Message):
        r"""Specifications to match a query parameter in the request.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            exact_match (str):
                The value of the query parameter must exactly match the
                contents of exact_match.

                Only one of exact_match, regex_match, or present_match must
                be set.

                This field is a member of `oneof`_ ``MatchType``.
            regex_match (str):
                The value of the query parameter must match the regular
                expression specified by regex_match. For regular expression
                grammar, please see
                https://github.com/google/re2/wiki/Syntax

                Only one of exact_match, regex_match, or present_match must
                be set.

                This field is a member of `oneof`_ ``MatchType``.
            present_match (bool):
                Specifies that the QueryParameterMatcher matches if request
                contains query parameter, irrespective of whether the
                parameter has a value or not.

                Only one of exact_match, regex_match, or present_match must
                be set.

                This field is a member of `oneof`_ ``MatchType``.
            query_parameter (str):
                The name of the query parameter to match.
        """

        exact_match: str = proto.Field(
            proto.STRING,
            number=2,
            oneof="MatchType",
        )
        regex_match: str = proto.Field(
            proto.STRING,
            number=3,
            oneof="MatchType",
        )
        present_match: bool = proto.Field(
            proto.BOOL,
            number=4,
            oneof="MatchType",
        )
        query_parameter: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class RouteMatch(proto.Message):
        r"""RouteMatch defines specifications used to match requests. If
        multiple match types are set, this RouteMatch will match if ALL
        type of matches are matched.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            full_path_match (str):
                The HTTP request path value should exactly match this value.

                Only one of full_path_match, prefix_match, or regex_match
                should be used.

                This field is a member of `oneof`_ ``PathMatch``.
            prefix_match (str):
                The HTTP request path value must begin with specified
                prefix_match. prefix_match must begin with a /.

                Only one of full_path_match, prefix_match, or regex_match
                should be used.

                This field is a member of `oneof`_ ``PathMatch``.
            regex_match (str):
                The HTTP request path value must satisfy the regular
                expression specified by regex_match after removing any query
                parameters and anchor supplied with the original URL. For
                regular expression grammar, please see
                https://github.com/google/re2/wiki/Syntax

                Only one of full_path_match, prefix_match, or regex_match
                should be used.

                This field is a member of `oneof`_ ``PathMatch``.
            ignore_case (bool):
                Specifies if prefix_match and full_path_match matches are
                case sensitive. The default value is false.
            headers (MutableSequence[google.cloud.network_services_v1.types.HttpRoute.HeaderMatch]):
                Specifies a list of HTTP request headers to
                match against. ALL of the supplied headers must
                be matched.
            query_parameters (MutableSequence[google.cloud.network_services_v1.types.HttpRoute.QueryParameterMatch]):
                Specifies a list of query parameters to match
                against. ALL of the query parameters must be
                matched.
        """

        full_path_match: str = proto.Field(
            proto.STRING,
            number=1,
            oneof="PathMatch",
        )
        prefix_match: str = proto.Field(
            proto.STRING,
            number=2,
            oneof="PathMatch",
        )
        regex_match: str = proto.Field(
            proto.STRING,
            number=3,
            oneof="PathMatch",
        )
        ignore_case: bool = proto.Field(
            proto.BOOL,
            number=4,
        )
        headers: MutableSequence["HttpRoute.HeaderMatch"] = proto.RepeatedField(
            proto.MESSAGE,
            number=5,
            message="HttpRoute.HeaderMatch",
        )
        query_parameters: MutableSequence["HttpRoute.QueryParameterMatch"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=6,
                message="HttpRoute.QueryParameterMatch",
            )
        )

    class Destination(proto.Message):
        r"""Specifications of a destination to which the request should
        be routed to.

        Attributes:
            service_name (str):
                The URL of a BackendService to route traffic
                to.
            weight (int):
                Specifies the proportion of requests
                forwarded to the backend referenced by the
                serviceName field. This is computed as:

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
            request_header_modifier (google.cloud.network_services_v1.types.HttpRoute.HeaderModifier):
                Optional. The specification for modifying the
                headers of a matching request prior to delivery
                of the request to the destination. If
                HeaderModifiers are set on both the Destination
                and the RouteAction, they will be merged.
                Conflicts between the two will not be resolved
                on the configuration.
            response_header_modifier (google.cloud.network_services_v1.types.HttpRoute.HeaderModifier):
                Optional. The specification for modifying the
                headers of a response prior to sending the
                response back to the client. If HeaderModifiers
                are set on both the Destination and the
                RouteAction, they will be merged. Conflicts
                between the two will not be resolved on the
                configuration.
        """

        service_name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        weight: int = proto.Field(
            proto.INT32,
            number=2,
        )
        request_header_modifier: "HttpRoute.HeaderModifier" = proto.Field(
            proto.MESSAGE,
            number=3,
            message="HttpRoute.HeaderModifier",
        )
        response_header_modifier: "HttpRoute.HeaderModifier" = proto.Field(
            proto.MESSAGE,
            number=4,
            message="HttpRoute.HeaderModifier",
        )

    class Redirect(proto.Message):
        r"""The specification for redirecting traffic.

        Attributes:
            host_redirect (str):
                The host that will be used in the redirect
                response instead of the one that was supplied in
                the request.
            path_redirect (str):
                The path that will be used in the redirect response instead
                of the one that was supplied in the request. path_redirect
                can not be supplied together with prefix_redirect. Supply
                one alone or neither. If neither is supplied, the path of
                the original request will be used for the redirect.
            prefix_rewrite (str):
                Indicates that during redirection, the
                matched prefix (or path) should be swapped with
                this value. This option allows URLs be
                dynamically created based on the request.
            response_code (google.cloud.network_services_v1.types.HttpRoute.Redirect.ResponseCode):
                The HTTP Status code to use for the redirect.
            https_redirect (bool):
                If set to true, the URL scheme in the
                redirected request is set to https. If set to
                false, the URL scheme of the redirected request
                will remain the same as that of the request.

                The default is set to false.
            strip_query (bool):
                if set to true, any accompanying query
                portion of the original URL is removed prior to
                redirecting the request. If set to false, the
                query portion of the original URL is retained.

                The default is set to false.
            port_redirect (int):
                The port that will be used in the redirected
                request instead of the one that was supplied in
                the request.
        """

        class ResponseCode(proto.Enum):
            r"""Supported HTTP response code.

            Values:
                RESPONSE_CODE_UNSPECIFIED (0):
                    Default value
                MOVED_PERMANENTLY_DEFAULT (1):
                    Corresponds to 301.
                FOUND (2):
                    Corresponds to 302.
                SEE_OTHER (3):
                    Corresponds to 303.
                TEMPORARY_REDIRECT (4):
                    Corresponds to 307. In this case, the request
                    method will be retained.
                PERMANENT_REDIRECT (5):
                    Corresponds to 308. In this case, the request
                    method will be retained.
            """

            RESPONSE_CODE_UNSPECIFIED = 0
            MOVED_PERMANENTLY_DEFAULT = 1
            FOUND = 2
            SEE_OTHER = 3
            TEMPORARY_REDIRECT = 4
            PERMANENT_REDIRECT = 5

        host_redirect: str = proto.Field(
            proto.STRING,
            number=1,
        )
        path_redirect: str = proto.Field(
            proto.STRING,
            number=2,
        )
        prefix_rewrite: str = proto.Field(
            proto.STRING,
            number=3,
        )
        response_code: "HttpRoute.Redirect.ResponseCode" = proto.Field(
            proto.ENUM,
            number=4,
            enum="HttpRoute.Redirect.ResponseCode",
        )
        https_redirect: bool = proto.Field(
            proto.BOOL,
            number=5,
        )
        strip_query: bool = proto.Field(
            proto.BOOL,
            number=6,
        )
        port_redirect: int = proto.Field(
            proto.INT32,
            number=7,
        )

    class FaultInjectionPolicy(proto.Message):
        r"""The specification for fault injection introduced into traffic
        to test the resiliency of clients to destination service
        failure. As part of fault injection, when clients send requests
        to a destination, delays can be introduced by client proxy on a
        percentage of requests before sending those requests to the
        destination service. Similarly requests can be aborted by client
        proxy for a percentage of requests.

        Attributes:
            delay (google.cloud.network_services_v1.types.HttpRoute.FaultInjectionPolicy.Delay):
                The specification for injecting delay to
                client requests.
            abort (google.cloud.network_services_v1.types.HttpRoute.FaultInjectionPolicy.Abort):
                The specification for aborting to client
                requests.
        """

        class Delay(proto.Message):
            r"""Specification of how client requests are delayed as part of
            fault injection before being sent to a destination.

            Attributes:
                fixed_delay (google.protobuf.duration_pb2.Duration):
                    Specify a fixed delay before forwarding the
                    request.
                percentage (int):
                    The percentage of traffic on which delay will be injected.

                    The value must be between [0, 100]
            """

            fixed_delay: duration_pb2.Duration = proto.Field(
                proto.MESSAGE,
                number=1,
                message=duration_pb2.Duration,
            )
            percentage: int = proto.Field(
                proto.INT32,
                number=2,
            )

        class Abort(proto.Message):
            r"""Specification of how client requests are aborted as part of
            fault injection before being sent to a destination.

            Attributes:
                http_status (int):
                    The HTTP status code used to abort the
                    request.
                    The value must be between 200 and 599 inclusive.
                percentage (int):
                    The percentage of traffic which will be aborted.

                    The value must be between [0, 100]
            """

            http_status: int = proto.Field(
                proto.INT32,
                number=1,
            )
            percentage: int = proto.Field(
                proto.INT32,
                number=2,
            )

        delay: "HttpRoute.FaultInjectionPolicy.Delay" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="HttpRoute.FaultInjectionPolicy.Delay",
        )
        abort: "HttpRoute.FaultInjectionPolicy.Abort" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="HttpRoute.FaultInjectionPolicy.Abort",
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

    class HeaderModifier(proto.Message):
        r"""The specification for modifying HTTP header in HTTP request
        and HTTP response.

        Attributes:
            set (MutableMapping[str, str]):
                Completely overwrite/replace the headers with
                given map where key is the name of the header,
                value is the value of the header.
            add (MutableMapping[str, str]):
                Add the headers with given map where key is
                the name of the header, value is the value of
                the header.
            remove (MutableSequence[str]):
                Remove headers (matching by header names)
                specified in the list.
        """

        set: MutableMapping[str, str] = proto.MapField(
            proto.STRING,
            proto.STRING,
            number=1,
        )
        add: MutableMapping[str, str] = proto.MapField(
            proto.STRING,
            proto.STRING,
            number=2,
        )
        remove: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=3,
        )

    class URLRewrite(proto.Message):
        r"""The specification for modifying the URL of the request, prior
        to forwarding the request to the destination.

        Attributes:
            path_prefix_rewrite (str):
                Prior to forwarding the request to the
                selected destination, the matching portion of
                the requests path is replaced by this value.
            host_rewrite (str):
                Prior to forwarding the request to the
                selected destination, the requests host header
                is replaced by this value.
        """

        path_prefix_rewrite: str = proto.Field(
            proto.STRING,
            number=1,
        )
        host_rewrite: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class RetryPolicy(proto.Message):
        r"""The specifications for retries.

        Attributes:
            retry_conditions (MutableSequence[str]):
                Specifies one or more conditions when this retry policy
                applies. Valid values are: 5xx: Proxy will attempt a retry
                if the destination service responds with any 5xx response
                code, of if the destination service does not respond at all,
                example: disconnect, reset, read timeout, connection failure
                and refused streams.

                gateway-error: Similar to 5xx, but only applies to response
                codes 502, 503, 504.

                reset: Proxy will attempt a retry if the destination service
                does not respond at all (disconnect/reset/read timeout)

                connect-failure: Proxy will retry on failures connecting to
                destination for example due to connection timeouts.

                retriable-4xx: Proxy will retry fro retriable 4xx response
                codes. Currently the only retriable error supported is 409.

                refused-stream: Proxy will retry if the destination resets
                the stream with a REFUSED_STREAM error code. This reset type
                indicates that it is safe to retry.
            num_retries (int):
                Specifies the allowed number of retries. This
                number must be > 0. If not specified, default to
                1.
            per_try_timeout (google.protobuf.duration_pb2.Duration):
                Specifies a non-zero timeout per retry
                attempt.
        """

        retry_conditions: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )
        num_retries: int = proto.Field(
            proto.INT32,
            number=2,
        )
        per_try_timeout: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=3,
            message=duration_pb2.Duration,
        )

    class RequestMirrorPolicy(proto.Message):
        r"""Specifies the policy on how requests are shadowed to a
        separate mirrored destination service. The proxy does not wait
        for responses from the shadow service. Prior to sending traffic
        to the shadow service, the host/authority header is suffixed
        with -shadow.
        Mirroring is currently not supported for Cloud Run destinations.

        Attributes:
            destination (google.cloud.network_services_v1.types.HttpRoute.Destination):
                The destination the requests will be mirrored
                to. The weight of the destination will be
                ignored.
            mirror_percent (float):
                Optional. The percentage of requests to get
                mirrored to the desired destination.
        """

        destination: "HttpRoute.Destination" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="HttpRoute.Destination",
        )
        mirror_percent: float = proto.Field(
            proto.FLOAT,
            number=2,
        )

    class CorsPolicy(proto.Message):
        r"""The Specification for allowing client side cross-origin
        requests.

        Attributes:
            allow_origins (MutableSequence[str]):
                Specifies the list of origins that will be allowed to do
                CORS requests. An origin is allowed if it matches either an
                item in allow_origins or an item in allow_origin_regexes.
            allow_origin_regexes (MutableSequence[str]):
                Specifies the regular expression patterns
                that match allowed origins. For regular
                expression grammar, please see
                https://github.com/google/re2/wiki/Syntax.
            allow_methods (MutableSequence[str]):
                Specifies the content for
                Access-Control-Allow-Methods header.
            allow_headers (MutableSequence[str]):
                Specifies the content for
                Access-Control-Allow-Headers header.
            expose_headers (MutableSequence[str]):
                Specifies the content for
                Access-Control-Expose-Headers header.
            max_age (str):
                Specifies how long result of a preflight
                request can be cached in seconds. This
                translates to the Access-Control-Max-Age header.
            allow_credentials (bool):
                In response to a preflight request, setting
                this to true indicates that the actual request
                can include user credentials. This translates to
                the Access-Control-Allow-Credentials header.

                Default value is false.
            disabled (bool):
                If true, the CORS policy is disabled. The
                default value is false, which indicates that the
                CORS policy is in effect.
        """

        allow_origins: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )
        allow_origin_regexes: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )
        allow_methods: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=3,
        )
        allow_headers: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=4,
        )
        expose_headers: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=5,
        )
        max_age: str = proto.Field(
            proto.STRING,
            number=6,
        )
        allow_credentials: bool = proto.Field(
            proto.BOOL,
            number=7,
        )
        disabled: bool = proto.Field(
            proto.BOOL,
            number=8,
        )

    class HttpDirectResponse(proto.Message):
        r"""Static HTTP response object to be returned.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            string_body (str):
                Optional. Response body as a string. Maximum
                body length is 1024 characters.

                This field is a member of `oneof`_ ``HttpBody``.
            bytes_body (bytes):
                Optional. Response body as bytes. Maximum
                body size is 4096B.

                This field is a member of `oneof`_ ``HttpBody``.
            status (int):
                Required. Status to return as part of HTTP
                Response. Must be a positive integer.
        """

        string_body: str = proto.Field(
            proto.STRING,
            number=2,
            oneof="HttpBody",
        )
        bytes_body: bytes = proto.Field(
            proto.BYTES,
            number=3,
            oneof="HttpBody",
        )
        status: int = proto.Field(
            proto.INT32,
            number=1,
        )

    class RouteAction(proto.Message):
        r"""The specifications for routing traffic and applying
        associated policies.

        Attributes:
            destinations (MutableSequence[google.cloud.network_services_v1.types.HttpRoute.Destination]):
                The destination to which traffic should be
                forwarded.
            redirect (google.cloud.network_services_v1.types.HttpRoute.Redirect):
                If set, the request is directed as configured
                by this field.
            fault_injection_policy (google.cloud.network_services_v1.types.HttpRoute.FaultInjectionPolicy):
                The specification for fault injection introduced into
                traffic to test the resiliency of clients to backend service
                failure. As part of fault injection, when clients send
                requests to a backend service, delays can be introduced on a
                percentage of requests before sending those requests to the
                backend service. Similarly requests from clients can be
                aborted for a percentage of requests.

                timeout and retry_policy will be ignored by clients that are
                configured with a fault_injection_policy
            request_header_modifier (google.cloud.network_services_v1.types.HttpRoute.HeaderModifier):
                The specification for modifying the headers
                of a matching request prior to delivery of the
                request to the destination. If HeaderModifiers
                are set on both the Destination and the
                RouteAction, they will be merged. Conflicts
                between the two will not be resolved on the
                configuration.
            response_header_modifier (google.cloud.network_services_v1.types.HttpRoute.HeaderModifier):
                The specification for modifying the headers
                of a response prior to sending the response back
                to the client. If HeaderModifiers are set on
                both the Destination and the RouteAction, they
                will be merged. Conflicts between the two will
                not be resolved on the configuration.
            url_rewrite (google.cloud.network_services_v1.types.HttpRoute.URLRewrite):
                The specification for rewrite URL before
                forwarding requests to the destination.
            timeout (google.protobuf.duration_pb2.Duration):
                Specifies the timeout for selected route.
                Timeout is computed from the time the request
                has been fully processed (i.e. end of stream) up
                until the response has been completely
                processed. Timeout includes all retries.
            retry_policy (google.cloud.network_services_v1.types.HttpRoute.RetryPolicy):
                Specifies the retry policy associated with
                this route.
            request_mirror_policy (google.cloud.network_services_v1.types.HttpRoute.RequestMirrorPolicy):
                Specifies the policy on how requests intended
                for the routes destination are shadowed to a
                separate mirrored destination. Proxy will not
                wait for the shadow destination to respond
                before returning the response. Prior to sending
                traffic to the shadow service, the
                host/authority header is suffixed with -shadow.
            cors_policy (google.cloud.network_services_v1.types.HttpRoute.CorsPolicy):
                The specification for allowing client side
                cross-origin requests.
            stateful_session_affinity (google.cloud.network_services_v1.types.HttpRoute.StatefulSessionAffinityPolicy):
                Optional. Specifies cookie-based stateful
                session affinity.
            direct_response (google.cloud.network_services_v1.types.HttpRoute.HttpDirectResponse):
                Optional. Static HTTP Response object to be
                returned regardless of the request.
            idle_timeout (google.protobuf.duration_pb2.Duration):
                Optional. Specifies the idle timeout for the
                selected route. The idle timeout is defined as
                the period in which there are no bytes sent or
                received on either the upstream or downstream
                connection. If not set, the default idle timeout
                is 1 hour. If set to 0s, the timeout will be
                disabled.
        """

        destinations: MutableSequence["HttpRoute.Destination"] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="HttpRoute.Destination",
        )
        redirect: "HttpRoute.Redirect" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="HttpRoute.Redirect",
        )
        fault_injection_policy: "HttpRoute.FaultInjectionPolicy" = proto.Field(
            proto.MESSAGE,
            number=4,
            message="HttpRoute.FaultInjectionPolicy",
        )
        request_header_modifier: "HttpRoute.HeaderModifier" = proto.Field(
            proto.MESSAGE,
            number=5,
            message="HttpRoute.HeaderModifier",
        )
        response_header_modifier: "HttpRoute.HeaderModifier" = proto.Field(
            proto.MESSAGE,
            number=6,
            message="HttpRoute.HeaderModifier",
        )
        url_rewrite: "HttpRoute.URLRewrite" = proto.Field(
            proto.MESSAGE,
            number=7,
            message="HttpRoute.URLRewrite",
        )
        timeout: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=8,
            message=duration_pb2.Duration,
        )
        retry_policy: "HttpRoute.RetryPolicy" = proto.Field(
            proto.MESSAGE,
            number=9,
            message="HttpRoute.RetryPolicy",
        )
        request_mirror_policy: "HttpRoute.RequestMirrorPolicy" = proto.Field(
            proto.MESSAGE,
            number=10,
            message="HttpRoute.RequestMirrorPolicy",
        )
        cors_policy: "HttpRoute.CorsPolicy" = proto.Field(
            proto.MESSAGE,
            number=11,
            message="HttpRoute.CorsPolicy",
        )
        stateful_session_affinity: "HttpRoute.StatefulSessionAffinityPolicy" = (
            proto.Field(
                proto.MESSAGE,
                number=12,
                message="HttpRoute.StatefulSessionAffinityPolicy",
            )
        )
        direct_response: "HttpRoute.HttpDirectResponse" = proto.Field(
            proto.MESSAGE,
            number=13,
            message="HttpRoute.HttpDirectResponse",
        )
        idle_timeout: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=14,
            message=duration_pb2.Duration,
        )

    class RouteRule(proto.Message):
        r"""Specifies how to match traffic and how to route traffic when
        traffic is matched.

        Attributes:
            matches (MutableSequence[google.cloud.network_services_v1.types.HttpRoute.RouteMatch]):
                A list of matches define conditions used for
                matching the rule against incoming HTTP
                requests. Each match is independent, i.e. this
                rule will be matched if ANY one of the matches
                is satisfied.

                If no matches field is specified, this rule will
                unconditionally match traffic.

                If a default rule is desired to be configured,
                add a rule with no matches specified to the end
                of the rules list.
            action (google.cloud.network_services_v1.types.HttpRoute.RouteAction):
                The detailed rule defining how to route
                matched traffic.
        """

        matches: MutableSequence["HttpRoute.RouteMatch"] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="HttpRoute.RouteMatch",
        )
        action: "HttpRoute.RouteAction" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="HttpRoute.RouteAction",
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    self_link: str = proto.Field(
        proto.STRING,
        number=11,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    hostnames: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
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
    rules: MutableSequence[RouteRule] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message=RouteRule,
    )


class ListHttpRoutesRequest(proto.Message):
    r"""Request used with the ListHttpRoutes method.

    Attributes:
        parent (str):
            Required. The project and location from which the HttpRoutes
            should be listed, specified in the format
            ``projects/*/locations/*``.
        page_size (int):
            Maximum number of HttpRoutes to return per
            call.
        page_token (str):
            The value returned by the last ``ListHttpRoutesResponse``
            Indicates that this is a continuation of a prior
            ``ListHttpRoutes`` call, and that the system should return
            the next page of data.
        return_partial_success (bool):
            Optional. If true, allow partial responses
            for multi-regional Aggregated List requests.
            Otherwise if one of the locations is down or
            unreachable, the Aggregated List request will
            fail.
        filter (str):
            Optional. Filter expression to restrict the
            list.
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
    filter: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListHttpRoutesResponse(proto.Message):
    r"""Response returned by the ListHttpRoutes method.

    Attributes:
        http_routes (MutableSequence[google.cloud.network_services_v1.types.HttpRoute]):
            List of HttpRoute resources.
        next_page_token (str):
            If there might be more results than those appearing in this
            response, then ``next_page_token`` is included. To get the
            next set of results, call this method again using the value
            of ``next_page_token`` as ``page_token``.
        unreachable (MutableSequence[str]):
            Unreachable resources. Populated when the request opts into
            [return_partial_success][google.cloud.networkservices.v1.ListHttpRoutesRequest.return_partial_success]
            and reading across collections e.g. when attempting to list
            all resources across all supported locations.
    """

    @property
    def raw_page(self):
        return self

    http_routes: MutableSequence["HttpRoute"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="HttpRoute",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetHttpRouteRequest(proto.Message):
    r"""Request used by the GetHttpRoute method.

    Attributes:
        name (str):
            Required. A name of the HttpRoute to get. Must be in the
            format ``projects/*/locations/*/httpRoutes/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateHttpRouteRequest(proto.Message):
    r"""Request used by the HttpRoute method.

    Attributes:
        parent (str):
            Required. The parent resource of the HttpRoute. Must be in
            the format ``projects/*/locations/*``.
        http_route_id (str):
            Required. Short name of the HttpRoute
            resource to be created.
        http_route (google.cloud.network_services_v1.types.HttpRoute):
            Required. HttpRoute resource to be created.
        request_id (str):
            Optional. Idempotent request UUID.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    http_route_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    http_route: "HttpRoute" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="HttpRoute",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateHttpRouteRequest(proto.Message):
    r"""Request used by the UpdateHttpRoute method.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the HttpRoute resource by the update. The
            fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. If the user does not provide a mask
            then all fields will be overwritten.
        http_route (google.cloud.network_services_v1.types.HttpRoute):
            Required. Updated HttpRoute resource.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    http_route: "HttpRoute" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="HttpRoute",
    )


class DeleteHttpRouteRequest(proto.Message):
    r"""Request used by the DeleteHttpRoute method.

    Attributes:
        name (str):
            Required. A name of the HttpRoute to delete. Must be in the
            format ``projects/*/locations/*/httpRoutes/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
