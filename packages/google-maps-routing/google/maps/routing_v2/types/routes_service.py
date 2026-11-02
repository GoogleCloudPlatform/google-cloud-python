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
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.rpc.status_pb2 as status_pb2  # type: ignore
import google.type.localized_text_pb2 as localized_text_pb2  # type: ignore
import proto  # type: ignore

from google.maps.routing_v2.types import fallback_info as gmr_fallback_info
from google.maps.routing_v2.types import geocoding_results as gmr_geocoding_results
from google.maps.routing_v2.types import polyline, route, route_travel_mode
from google.maps.routing_v2.types import route_modifiers as gmr_route_modifiers
from google.maps.routing_v2.types import routing_preference as gmr_routing_preference
from google.maps.routing_v2.types import traffic_model as gmr_traffic_model
from google.maps.routing_v2.types import transit_preferences as gmr_transit_preferences
from google.maps.routing_v2.types import units as gmr_units
from google.maps.routing_v2.types import waypoint as gmr_waypoint

__protobuf__ = proto.module(
    package="google.maps.routing.v2",
    manifest={
        "RouteMatrixElementCondition",
        "ComputeRoutesRequest",
        "ComputeRoutesResponse",
        "ComputeRouteMatrixRequest",
        "RouteMatrixOrigin",
        "RouteMatrixDestination",
        "RouteMatrixElement",
    },
)


class RouteMatrixElementCondition(proto.Enum):
    r"""The condition of the route being returned.

    Values:
        ROUTE_MATRIX_ELEMENT_CONDITION_UNSPECIFIED (0):
            Only used when the ``status`` of the element is not OK.
        ROUTE_EXISTS (1):
            A route was found, and the corresponding
            information was filled out for the element.
        ROUTE_NOT_FOUND (2):
            No route could be found. Fields containing route
            information, such as ``distance_meters`` or ``duration``,
            will not be filled out in the element.
    """

    ROUTE_MATRIX_ELEMENT_CONDITION_UNSPECIFIED = 0
    ROUTE_EXISTS = 1
    ROUTE_NOT_FOUND = 2


class ComputeRoutesRequest(proto.Message):
    r"""ComputeRoutes request message.

    Attributes:
        origin (google.maps.routing_v2.types.Waypoint):
            Required. Origin waypoint.
        destination (google.maps.routing_v2.types.Waypoint):
            Required. Destination waypoint.
        intermediates (MutableSequence[google.maps.routing_v2.types.Waypoint]):
            Optional. A set of waypoints along the route
            (excluding terminal points), for either stopping
            at or passing by. Up to 25 intermediate
            waypoints are supported.
        travel_mode (google.maps.routing_v2.types.RouteTravelMode):
            Optional. Specifies the mode of
            transportation.
        routing_preference (google.maps.routing_v2.types.RoutingPreference):
            Optional. Specifies how to compute the route. The server
            attempts to use the selected routing preference to compute
            the route. If the routing preference results in an error or
            an extra long latency, then an error is returned. You can
            specify this option only when the ``travel_mode`` is
            ``DRIVE`` or ``TWO_WHEELER``, otherwise the request fails.
        polyline_quality (google.maps.routing_v2.types.PolylineQuality):
            Optional. Specifies your preference for the
            quality of the polyline.
        polyline_encoding (google.maps.routing_v2.types.PolylineEncoding):
            Optional. Specifies the preferred encoding
            for the polyline.
        departure_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. The departure time. If you don't set this value,
            then this value defaults to the time that you made the
            request. NOTE: You can only specify a ``departure_time`` in
            the past when
            [``RouteTravelMode``][google.maps.routing.v2.RouteTravelMode]
            is set to ``TRANSIT``. Transit trips are available for up to
            7 days in the past or 100 days in the future.
        arrival_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. The arrival time. NOTE: This field is ignored when
            requests specify a
            [RouteTravelMode][google.maps.routing.v2.RouteTravelMode]
            other than ``TRANSIT``. You can specify either
            ``departure_time`` or ``arrival_time``, but not both.
            Transit trips are available for up to 7 days in the past or
            100 days in the future.
        compute_alternative_routes (bool):
            Optional. Specifies whether to calculate
            alternate routes in addition to the route. No
            alternative routes are returned for requests
            that have intermediate waypoints.
        route_modifiers (google.maps.routing_v2.types.RouteModifiers):
            Optional. A set of conditions to satisfy that
            affect the way routes are calculated.
        language_code (str):
            Optional. The BCP-47 language code, such as "en-US" or
            "sr-Latn". For more information, see `Unicode Locale
            Identifier <http://www.unicode.org/reports/tr35/#Unicode_locale_identifier>`__.
            See `Language
            Support <https://developers.google.com/maps/faq#languagesupport>`__
            for the list of supported languages. When you don't provide
            this value, the display language is inferred from the
            location of the route request.
        region_code (str):
            Optional. The region code, specified as a ccTLD ("top-level
            domain") two-character value. For more information see
            `Country code top-level
            domains <https://en.wikipedia.org/wiki/List_of_Internet_top-level_domains#Country_code_top-level_domains>`__.
        units (google.maps.routing_v2.types.Units):
            Optional. Specifies the units of measure for the display
            fields. These fields include the ``instruction`` field in
            [``NavigationInstruction``][google.maps.routing.v2.NavigationInstruction].
            The units of measure used for the route, leg, step distance,
            and duration are not affected by this value. If you don't
            provide this value, then the display units are inferred from
            the location of the first origin.
        optimize_waypoint_order (bool):
            Optional. If set to true, the service attempts to minimize
            the overall cost of the route by re-ordering the specified
            intermediate waypoints. The request fails if any of the
            intermediate waypoints is a ``via`` waypoint. Use
            ``ComputeRoutesResponse.routes.optimized_intermediate_waypoint_index``
            to find the new ordering. If
            ``ComputeRoutesResponse.routes.optimized_intermediate_waypoint_index``
            is not requested in the ``X-Goog-FieldMask`` header, the
            request fails. If ``optimize_waypoint_order`` is set to
            false,
            ``ComputeRoutesResponse.optimized_intermediate_waypoint_index``
            will be empty.
        requested_reference_routes (MutableSequence[google.maps.routing_v2.types.ComputeRoutesRequest.ReferenceRoute]):
            Optional. Specifies what reference routes to calculate as
            part of the request in addition to the default route. A
            reference route is a route with a different route
            calculation objective than the default route. For example a
            ``FUEL_EFFICIENT`` reference route calculation takes into
            account various parameters that would generate an optimal
            fuel efficient route. When using this feature, look for
            [``route_labels``][google.maps.routing.v2.Route.route_labels]
            on the resulting routes.
        extra_computations (MutableSequence[google.maps.routing_v2.types.ComputeRoutesRequest.ExtraComputation]):
            Optional. A list of extra computations which
            may be used to complete the request. Note: These
            extra computations may return extra fields on
            the response. These extra fields must also be
            specified in the field mask to be returned in
            the response.
        traffic_model (google.maps.routing_v2.types.TrafficModel):
            Optional. Specifies the assumptions to use when calculating
            time in traffic. This setting affects the value returned in
            the duration field in the
            [``Route``][google.maps.routing.v2.Route] and
            [``RouteLeg``][google.maps.routing.v2.RouteLeg] which
            contains the predicted time in traffic based on historical
            averages. ``TrafficModel`` is only available for requests
            that have set
            [``RoutingPreference``][google.maps.routing.v2.RoutingPreference]
            to ``TRAFFIC_AWARE_OPTIMAL`` and
            [``RouteTravelMode``][google.maps.routing.v2.RouteTravelMode]
            to ``DRIVE``. Defaults to ``BEST_GUESS`` if traffic is
            requested and ``TrafficModel`` is not specified.
        transit_preferences (google.maps.routing_v2.types.TransitPreferences):
            Optional. Specifies preferences that influence the route
            returned for ``TRANSIT`` routes. NOTE: You can only specify
            a ``transit_preferences`` when
            [``RouteTravelMode``][google.maps.routing.v2.RouteTravelMode]
            is set to ``TRANSIT``.
    """

    class ReferenceRoute(proto.Enum):
        r"""A supported reference route on the ComputeRoutesRequest.

        Values:
            REFERENCE_ROUTE_UNSPECIFIED (0):
                Not used. Requests containing this value
                fail.
            FUEL_EFFICIENT (1):
                Fuel efficient route.
            SHORTER_DISTANCE (2):
                Route with shorter travel distance. This is an experimental
                feature.

                For ``DRIVE`` requests, this feature prioritizes shorter
                distance over driving comfort. For example, it may prefer
                local roads instead of highways, take dirt roads, cut
                through parking lots, etc. This feature does not return any
                maneuvers that Google Maps knows to be illegal.

                For ``BICYCLE`` and ``TWO_WHEELER`` requests, this feature
                returns routes similar to those returned when you don't
                specify ``requested_reference_routes``.

                This feature is not compatible with any other travel modes,
                via intermediate waypoints, or ``optimize_waypoint_order``;
                such requests will fail. However, you can use it with any
                ``routing_preference``.
        """

        REFERENCE_ROUTE_UNSPECIFIED = 0
        FUEL_EFFICIENT = 1
        SHORTER_DISTANCE = 2

    class ExtraComputation(proto.Enum):
        r"""Extra computations to perform while completing the request.
        Additional values may be added in the future.

        Values:
            EXTRA_COMPUTATION_UNSPECIFIED (0):
                Not used. Requests containing this value will
                fail.
            TOLLS (1):
                Toll information for the route(s).
            FUEL_CONSUMPTION (2):
                Estimated fuel consumption for the route(s).
            TRAFFIC_ON_POLYLINE (3):
                Traffic aware polylines for the route(s).
            HTML_FORMATTED_NAVIGATION_INSTRUCTIONS (4):
                [``NavigationInstruction``][google.maps.routing.v2.NavigationInstruction]
                presented as a formatted HTML text string. This content is
                meant to be read as-is. This content is for display only. Do
                not programmatically parse it.
            FLYOVER_INFO_ON_POLYLINE (7):
                Flyover information for the route(s). The
                ``routes.polyline_details.flyover_info`` fieldmask must be
                specified to return this information. This data will
                currently only be populated for certain metros in India.
                This feature is experimental, and the SKU/charge is subject
                to change.
            NARROW_ROAD_INFO_ON_POLYLINE (8):
                Narrow road information for the route(s). The
                ``routes.polyline_details.narrow_road_info`` fieldmask must
                be specified to return this information. This data will
                currently only be populated for certain metros in India.
                This feature is experimental, and the SKU/charge is subject
                to change.
            TUNNEL_INFO_ON_POLYLINE (9):
                Tunnel information for the route(s). The
                ``routes.polyline_details.tunnel_info`` fieldmask must be
                specified to return this information.
            BRIDGE_INFO_ON_POLYLINE (10):
                Bridge information for the route(s). The
                ``routes.polyline_details.bridge_info`` fieldmask must be
                specified to return this information.
            SKYWAY_INFO_ON_POLYLINE (11):
                Skyway information for the route(s). The
                ``routes.polyline_details.skyway_info`` fieldmask must be
                specified to return this information.
        """

        EXTRA_COMPUTATION_UNSPECIFIED = 0
        TOLLS = 1
        FUEL_CONSUMPTION = 2
        TRAFFIC_ON_POLYLINE = 3
        HTML_FORMATTED_NAVIGATION_INSTRUCTIONS = 4
        FLYOVER_INFO_ON_POLYLINE = 7
        NARROW_ROAD_INFO_ON_POLYLINE = 8
        TUNNEL_INFO_ON_POLYLINE = 9
        BRIDGE_INFO_ON_POLYLINE = 10
        SKYWAY_INFO_ON_POLYLINE = 11

    origin: gmr_waypoint.Waypoint = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gmr_waypoint.Waypoint,
    )
    destination: gmr_waypoint.Waypoint = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gmr_waypoint.Waypoint,
    )
    intermediates: MutableSequence[gmr_waypoint.Waypoint] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=gmr_waypoint.Waypoint,
    )
    travel_mode: route_travel_mode.RouteTravelMode = proto.Field(
        proto.ENUM,
        number=4,
        enum=route_travel_mode.RouteTravelMode,
    )
    routing_preference: gmr_routing_preference.RoutingPreference = proto.Field(
        proto.ENUM,
        number=5,
        enum=gmr_routing_preference.RoutingPreference,
    )
    polyline_quality: polyline.PolylineQuality = proto.Field(
        proto.ENUM,
        number=6,
        enum=polyline.PolylineQuality,
    )
    polyline_encoding: polyline.PolylineEncoding = proto.Field(
        proto.ENUM,
        number=12,
        enum=polyline.PolylineEncoding,
    )
    departure_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    arrival_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=19,
        message=timestamp_pb2.Timestamp,
    )
    compute_alternative_routes: bool = proto.Field(
        proto.BOOL,
        number=8,
    )
    route_modifiers: gmr_route_modifiers.RouteModifiers = proto.Field(
        proto.MESSAGE,
        number=9,
        message=gmr_route_modifiers.RouteModifiers,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=10,
    )
    region_code: str = proto.Field(
        proto.STRING,
        number=16,
    )
    units: gmr_units.Units = proto.Field(
        proto.ENUM,
        number=11,
        enum=gmr_units.Units,
    )
    optimize_waypoint_order: bool = proto.Field(
        proto.BOOL,
        number=13,
    )
    requested_reference_routes: MutableSequence[ReferenceRoute] = proto.RepeatedField(
        proto.ENUM,
        number=14,
        enum=ReferenceRoute,
    )
    extra_computations: MutableSequence[ExtraComputation] = proto.RepeatedField(
        proto.ENUM,
        number=15,
        enum=ExtraComputation,
    )
    traffic_model: gmr_traffic_model.TrafficModel = proto.Field(
        proto.ENUM,
        number=18,
        enum=gmr_traffic_model.TrafficModel,
    )
    transit_preferences: gmr_transit_preferences.TransitPreferences = proto.Field(
        proto.MESSAGE,
        number=20,
        message=gmr_transit_preferences.TransitPreferences,
    )


class ComputeRoutesResponse(proto.Message):
    r"""ComputeRoutes the response message.

    Attributes:
        routes (MutableSequence[google.maps.routing_v2.types.Route]):
            Contains an array of computed routes (up to three) when you
            specify ``compute_alternatives_routes``, and contains just
            one route when you don't. When this array contains multiple
            entries, the first one is the most recommended route. If the
            array is empty, then it means no route could be found.
        fallback_info (google.maps.routing_v2.types.FallbackInfo):
            In some cases when the server is not able to
            compute the route results with all of the input
            preferences, it may fallback to using a
            different way of computation. When fallback mode
            is used, this field contains detailed info about
            the fallback response. Otherwise this field is
            unset.
        geocoding_results (google.maps.routing_v2.types.GeocodingResults):
            Contains geocoding response info for
            waypoints specified as addresses.
    """

    routes: MutableSequence[route.Route] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=route.Route,
    )
    fallback_info: gmr_fallback_info.FallbackInfo = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gmr_fallback_info.FallbackInfo,
    )
    geocoding_results: gmr_geocoding_results.GeocodingResults = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gmr_geocoding_results.GeocodingResults,
    )


class ComputeRouteMatrixRequest(proto.Message):
    r"""ComputeRouteMatrix request message

    Attributes:
        origins (MutableSequence[google.maps.routing_v2.types.RouteMatrixOrigin]):
            Required. Array of origins, which determines the rows of the
            response matrix. Several size restrictions apply to the
            cardinality of origins and destinations:

            - The sum of the number of origins + the number of
              destinations specified as either ``place_id`` or
              ``address`` must be no greater than 50.
            - The product of number of origins × number of destinations
              must be no greater than 625 in any case.
            - The product of the number of origins × number of
              destinations must be no greater than 100 if
              routing_preference is set to ``TRAFFIC_AWARE_OPTIMAL``.
            - The product of the number of origins × number of
              destinations must be no greater than 100 if travel_mode is
              set to ``TRANSIT``.
        destinations (MutableSequence[google.maps.routing_v2.types.RouteMatrixDestination]):
            Required. Array of destinations, which
            determines the columns of the response matrix.
        travel_mode (google.maps.routing_v2.types.RouteTravelMode):
            Optional. Specifies the mode of
            transportation.
        routing_preference (google.maps.routing_v2.types.RoutingPreference):
            Optional. Specifies how to compute the route. The server
            attempts to use the selected routing preference to compute
            the route. If the routing preference results in an error or
            an extra long latency, an error is returned. You can specify
            this option only when the ``travel_mode`` is ``DRIVE`` or
            ``TWO_WHEELER``, otherwise the request fails.
        departure_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. The departure time. If you don't set this value,
            then this value defaults to the time that you made the
            request. NOTE: You can only specify a ``departure_time`` in
            the past when
            [``RouteTravelMode``][google.maps.routing.v2.RouteTravelMode]
            is set to ``TRANSIT``.
        arrival_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. The arrival time. NOTE: Can only be set when
            [``RouteTravelMode``][google.maps.routing.v2.RouteTravelMode]
            is set to ``TRANSIT``. You can specify either
            ``departure_time`` or ``arrival_time``, but not both.
        language_code (str):
            Optional. The BCP-47 language code, such as "en-US" or
            "sr-Latn". For more information, see `Unicode Locale
            Identifier <http://www.unicode.org/reports/tr35/#Unicode_locale_identifier>`__.
            See `Language
            Support <https://developers.google.com/maps/faq#languagesupport>`__
            for the list of supported languages. When you don't provide
            this value, the display language is inferred from the
            location of the first origin.
        region_code (str):
            Optional. The region code, specified as a ccTLD ("top-level
            domain") two-character value. For more information see
            `Country code top-level
            domains <https://en.wikipedia.org/wiki/List_of_Internet_top-level_domains#Country_code_top-level_domains>`__.
        units (google.maps.routing_v2.types.Units):
            Optional. Specifies the units of measure for
            the display fields.
        extra_computations (MutableSequence[google.maps.routing_v2.types.ComputeRouteMatrixRequest.ExtraComputation]):
            Optional. A list of extra computations which
            may be used to complete the request. Note: These
            extra computations may return extra fields on
            the response. These extra fields must also be
            specified in the field mask to be returned in
            the response.
        traffic_model (google.maps.routing_v2.types.TrafficModel):
            Optional. Specifies the assumptions to use when calculating
            time in traffic. This setting affects the value returned in
            the duration field in the
            [RouteMatrixElement][google.maps.routing.v2.RouteMatrixElement]
            which contains the predicted time in traffic based on
            historical averages. ``TrafficModel`` is only available for
            requests that have set
            [RoutingPreference][google.maps.routing.v2.RoutingPreference]
            to ``TRAFFIC_AWARE_OPTIMAL`` and
            [RouteTravelMode][google.maps.routing.v2.RouteTravelMode] to
            ``DRIVE``. Defaults to ``BEST_GUESS`` if traffic is
            requested and ``TrafficModel`` is not specified.
        transit_preferences (google.maps.routing_v2.types.TransitPreferences):
            Optional. Specifies preferences that influence the route
            returned for ``TRANSIT`` routes. NOTE: You can only specify
            a ``transit_preferences`` when
            [RouteTravelMode][google.maps.routing.v2.RouteTravelMode] is
            set to ``TRANSIT``.
    """

    class ExtraComputation(proto.Enum):
        r"""Extra computations to perform while completing the request.

        Values:
            EXTRA_COMPUTATION_UNSPECIFIED (0):
                Not used. Requests containing this value will
                fail.
            TOLLS (1):
                Toll information for the matrix element(s).
        """

        EXTRA_COMPUTATION_UNSPECIFIED = 0
        TOLLS = 1

    origins: MutableSequence["RouteMatrixOrigin"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="RouteMatrixOrigin",
    )
    destinations: MutableSequence["RouteMatrixDestination"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="RouteMatrixDestination",
    )
    travel_mode: route_travel_mode.RouteTravelMode = proto.Field(
        proto.ENUM,
        number=3,
        enum=route_travel_mode.RouteTravelMode,
    )
    routing_preference: gmr_routing_preference.RoutingPreference = proto.Field(
        proto.ENUM,
        number=4,
        enum=gmr_routing_preference.RoutingPreference,
    )
    departure_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    arrival_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=11,
        message=timestamp_pb2.Timestamp,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=6,
    )
    region_code: str = proto.Field(
        proto.STRING,
        number=9,
    )
    units: gmr_units.Units = proto.Field(
        proto.ENUM,
        number=7,
        enum=gmr_units.Units,
    )
    extra_computations: MutableSequence[ExtraComputation] = proto.RepeatedField(
        proto.ENUM,
        number=8,
        enum=ExtraComputation,
    )
    traffic_model: gmr_traffic_model.TrafficModel = proto.Field(
        proto.ENUM,
        number=10,
        enum=gmr_traffic_model.TrafficModel,
    )
    transit_preferences: gmr_transit_preferences.TransitPreferences = proto.Field(
        proto.MESSAGE,
        number=12,
        message=gmr_transit_preferences.TransitPreferences,
    )


class RouteMatrixOrigin(proto.Message):
    r"""A single origin for ComputeRouteMatrixRequest

    Attributes:
        waypoint (google.maps.routing_v2.types.Waypoint):
            Required. Origin waypoint
        route_modifiers (google.maps.routing_v2.types.RouteModifiers):
            Optional. Modifiers for every route that
            takes this as the origin
    """

    waypoint: gmr_waypoint.Waypoint = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gmr_waypoint.Waypoint,
    )
    route_modifiers: gmr_route_modifiers.RouteModifiers = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gmr_route_modifiers.RouteModifiers,
    )


class RouteMatrixDestination(proto.Message):
    r"""A single destination for ComputeRouteMatrixRequest

    Attributes:
        waypoint (google.maps.routing_v2.types.Waypoint):
            Required. Destination waypoint
    """

    waypoint: gmr_waypoint.Waypoint = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gmr_waypoint.Waypoint,
    )


class RouteMatrixElement(proto.Message):
    r"""Contains route information computed for an origin/destination
    pair in the ComputeRouteMatrix API. This proto can be streamed
    to the client.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        origin_index (int):
            Zero-based index of the origin in the
            request.

            This field is a member of `oneof`_ ``_origin_index``.
        destination_index (int):
            Zero-based index of the destination in the
            request.

            This field is a member of `oneof`_ ``_destination_index``.
        status (google.rpc.status_pb2.Status):
            Error status code for this element.
        condition (google.maps.routing_v2.types.RouteMatrixElementCondition):
            Indicates whether the route was found or not.
            Independent of status.
        distance_meters (int):
            The travel distance of the route, in meters.
        duration (google.protobuf.duration_pb2.Duration):
            The length of time needed to navigate the route. If you set
            the
            [routing_preference][google.maps.routing.v2.ComputeRouteMatrixRequest.routing_preference]
            to ``TRAFFIC_UNAWARE``, then this value is the same as
            ``static_duration``. If you set the ``routing_preference``
            to either ``TRAFFIC_AWARE`` or ``TRAFFIC_AWARE_OPTIMAL``,
            then this value is calculated taking traffic conditions into
            account.
        static_duration (google.protobuf.duration_pb2.Duration):
            The duration of traveling through the route
            without taking traffic conditions into
            consideration.
        travel_advisory (google.maps.routing_v2.types.RouteTravelAdvisory):
            Additional information about the route. For
            example: restriction information and toll
            information
        fallback_info (google.maps.routing_v2.types.FallbackInfo):
            In some cases when the server is not able to
            compute the route with the given preferences for
            this particular origin/destination pair, it may
            fall back to using a different mode of
            computation. When fallback mode is used, this
            field contains detailed information about the
            fallback response. Otherwise this field is
            unset.
        localized_values (google.maps.routing_v2.types.RouteMatrixElement.LocalizedValues):
            Text representations of properties of the
            ``RouteMatrixElement``.
    """

    class LocalizedValues(proto.Message):
        r"""Text representations of certain properties.

        Attributes:
            distance (google.type.localized_text_pb2.LocalizedText):
                Travel distance represented in text form.
            duration (google.type.localized_text_pb2.LocalizedText):
                Duration represented in text form taking traffic conditions
                into consideration. Note: If traffic information was not
                requested, this value is the same value as static_duration.
            static_duration (google.type.localized_text_pb2.LocalizedText):
                Duration represented in text form without
                taking traffic conditions into consideration.
            transit_fare (google.type.localized_text_pb2.LocalizedText):
                Transit fare represented in text form.
        """

        distance: localized_text_pb2.LocalizedText = proto.Field(
            proto.MESSAGE,
            number=1,
            message=localized_text_pb2.LocalizedText,
        )
        duration: localized_text_pb2.LocalizedText = proto.Field(
            proto.MESSAGE,
            number=2,
            message=localized_text_pb2.LocalizedText,
        )
        static_duration: localized_text_pb2.LocalizedText = proto.Field(
            proto.MESSAGE,
            number=3,
            message=localized_text_pb2.LocalizedText,
        )
        transit_fare: localized_text_pb2.LocalizedText = proto.Field(
            proto.MESSAGE,
            number=4,
            message=localized_text_pb2.LocalizedText,
        )

    origin_index: int = proto.Field(
        proto.INT32,
        number=1,
        optional=True,
    )
    destination_index: int = proto.Field(
        proto.INT32,
        number=2,
        optional=True,
    )
    status: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=3,
        message=status_pb2.Status,
    )
    condition: "RouteMatrixElementCondition" = proto.Field(
        proto.ENUM,
        number=9,
        enum="RouteMatrixElementCondition",
    )
    distance_meters: int = proto.Field(
        proto.INT32,
        number=4,
    )
    duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=5,
        message=duration_pb2.Duration,
    )
    static_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=6,
        message=duration_pb2.Duration,
    )
    travel_advisory: route.RouteTravelAdvisory = proto.Field(
        proto.MESSAGE,
        number=7,
        message=route.RouteTravelAdvisory,
    )
    fallback_info: gmr_fallback_info.FallbackInfo = proto.Field(
        proto.MESSAGE,
        number=8,
        message=gmr_fallback_info.FallbackInfo,
    )
    localized_values: LocalizedValues = proto.Field(
        proto.MESSAGE,
        number=10,
        message=LocalizedValues,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
