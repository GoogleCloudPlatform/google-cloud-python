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
import google.type.localized_text_pb2 as localized_text_pb2  # type: ignore
import google.type.money_pb2 as money_pb2  # type: ignore
import proto  # type: ignore
from google.geo.type.types import viewport as ggt_viewport

from google.maps.routing_v2.types import (
    localized_time,
    location,
    route_label,
    route_travel_mode,
    speed_reading_interval,
    transit,
)
from google.maps.routing_v2.types import (
    navigation_instruction as gmr_navigation_instruction,
)
from google.maps.routing_v2.types import polyline as gmr_polyline
from google.maps.routing_v2.types import polyline_details as gmr_polyline_details
from google.maps.routing_v2.types import toll_info as gmr_toll_info

__protobuf__ = proto.module(
    package="google.maps.routing.v2",
    manifest={
        "Route",
        "RouteTravelAdvisory",
        "RouteLegTravelAdvisory",
        "RouteLegStepTravelAdvisory",
        "RouteLeg",
        "RouteLegStep",
        "RouteLegStepTransitDetails",
    },
)


class Route(proto.Message):
    r"""Contains a route, which consists of a series of connected
    road segments that join beginning, ending, and intermediate
    waypoints.

    Attributes:
        route_labels (MutableSequence[google.maps.routing_v2.types.RouteLabel]):
            Labels for the ``Route`` that are useful to identify
            specific properties of the route to compare against others.
        legs (MutableSequence[google.maps.routing_v2.types.RouteLeg]):
            A collection of legs (path segments between waypoints) that
            make up the route. Each leg corresponds to the trip between
            two non-``via``
            [``Waypoints``][google.maps.routing.v2.Waypoint]. For
            example, a route with no intermediate waypoints has only one
            leg. A route that includes one non-``via`` intermediate
            waypoint has two legs. A route that includes one ``via``
            intermediate waypoint has one leg. The order of the legs
            matches the order of waypoints from ``origin`` to
            ``intermediates`` to ``destination``.
        distance_meters (int):
            The travel distance of the route, in meters.
        duration (google.protobuf.duration_pb2.Duration):
            The length of time needed to navigate the route. If you set
            the ``routing_preference`` to ``TRAFFIC_UNAWARE``, then this
            value is the same as ``static_duration``. If you set the
            ``routing_preference`` to either ``TRAFFIC_AWARE`` or
            ``TRAFFIC_AWARE_OPTIMAL``, then this value is calculated
            taking traffic conditions into account.
        static_duration (google.protobuf.duration_pb2.Duration):
            The duration of travel through the route
            without taking traffic conditions into
            consideration.
        polyline (google.maps.routing_v2.types.Polyline):
            The overall route polyline. This polyline is the combined
            polyline of all ``legs``.
        description (str):
            A description of the route.
        warnings (MutableSequence[str]):
            An array of warnings to show when displaying
            the route.
        viewport (google.geo.type.types.Viewport):
            The viewport bounding box of the polyline.
        travel_advisory (google.maps.routing_v2.types.RouteTravelAdvisory):
            Additional information about the route.
        optimized_intermediate_waypoint_index (MutableSequence[int]):
            If you set
            [``optimize_waypoint_order``][google.maps.routing.v2.ComputeRoutesRequest.optimize_waypoint_order]
            to true, this field contains the optimized ordering of
            intermediate waypoints. Otherwise, this field is empty. For
            example, if you give an input of Origin: LA; Intermediate
            waypoints: Dallas, Bangor, Phoenix; Destination: New York;
            and the optimized intermediate waypoint order is Phoenix,
            Dallas, Bangor, then this field contains the values [2, 0,
            1]. The index starts with 0 for the first intermediate
            waypoint provided in the input.
        localized_values (google.maps.routing_v2.types.Route.RouteLocalizedValues):
            Text representations of properties of the ``Route``.
        route_token (str):
            An opaque token that can be passed to `Navigation
            SDK <https://developers.google.com/maps/documentation/mobility/driver-sdk/navigation>`__
            to reconstruct the route during navigation, and, in the
            event of rerouting, honor the original intention when the
            route was created. Treat this token as an opaque blob. Don't
            compare its value across requests as its value may change
            even if the service returns the exact same route.

            NOTE: ``Route.route_token`` is only available for requests
            that have set ``ComputeRoutesRequest.routing_preference`` to
            ``TRAFFIC_AWARE`` or ``TRAFFIC_AWARE_OPTIMAL``.
            ``Route.route_token`` is not supported for requests that
            have Via waypoints.
        polyline_details (google.maps.routing_v2.types.PolylineDetails):
            Contains information about details along the
            polyline.
    """

    class RouteLocalizedValues(proto.Message):
        r"""Text representations of certain properties.

        Attributes:
            distance (google.type.localized_text_pb2.LocalizedText):
                Travel distance represented in text form.
            duration (google.type.localized_text_pb2.LocalizedText):
                Duration, represented in text form and localized to the
                region of the query. Takes traffic conditions into
                consideration. Note: If you did not request traffic
                information, this value is the same value as
                ``static_duration``.
            static_duration (google.type.localized_text_pb2.LocalizedText):
                Duration without taking traffic conditions
                into consideration, represented in text form.
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

    route_labels: MutableSequence[route_label.RouteLabel] = proto.RepeatedField(
        proto.ENUM,
        number=13,
        enum=route_label.RouteLabel,
    )
    legs: MutableSequence["RouteLeg"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="RouteLeg",
    )
    distance_meters: int = proto.Field(
        proto.INT32,
        number=2,
    )
    duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=3,
        message=duration_pb2.Duration,
    )
    static_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=4,
        message=duration_pb2.Duration,
    )
    polyline: gmr_polyline.Polyline = proto.Field(
        proto.MESSAGE,
        number=5,
        message=gmr_polyline.Polyline,
    )
    description: str = proto.Field(
        proto.STRING,
        number=6,
    )
    warnings: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )
    viewport: ggt_viewport.Viewport = proto.Field(
        proto.MESSAGE,
        number=8,
        message=ggt_viewport.Viewport,
    )
    travel_advisory: "RouteTravelAdvisory" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="RouteTravelAdvisory",
    )
    optimized_intermediate_waypoint_index: MutableSequence[int] = proto.RepeatedField(
        proto.INT32,
        number=10,
    )
    localized_values: RouteLocalizedValues = proto.Field(
        proto.MESSAGE,
        number=11,
        message=RouteLocalizedValues,
    )
    route_token: str = proto.Field(
        proto.STRING,
        number=12,
    )
    polyline_details: gmr_polyline_details.PolylineDetails = proto.Field(
        proto.MESSAGE,
        number=14,
        message=gmr_polyline_details.PolylineDetails,
    )


class RouteTravelAdvisory(proto.Message):
    r"""Contains the additional information that the user should be
    informed about, such as possible traffic zone restrictions.

    Attributes:
        toll_info (google.maps.routing_v2.types.TollInfo):
            Contains information about tolls on the route. This field is
            only populated if tolls are expected on the route and
            ``TOLLS`` is included in the request's
            [ComputeRoutesRequest.extra_computations][google.maps.routing.v2.ComputeRoutesRequest.extra_computations].
            If this field is set, but the ``estimatedPrice`` subfield is
            not populated, then the route contains tolls, but the
            estimated price is unknown. If ``toll_info`` is not set,
            then there are no tolls expected on the route.
        speed_reading_intervals (MutableSequence[google.maps.routing_v2.types.SpeedReadingInterval]):
            Speed reading intervals indicating traffic density. This
            field is only populated for requests when the request has a
            ``TRAFFIC_AWARE`` or ``TRAFFIC_AWARE_OPTIMAL``
            [ComputeRoutesRequest.routing_preference][google.maps.routing.v2.ComputeRoutesRequest.routing_preference]
            value, and ``TRAFFIC_ON_POLYLINE`` is included in the
            [ComputeRoutesRequest.extra_computations][google.maps.routing.v2.ComputeRoutesRequest.extra_computations].
            The intervals cover the entire polyline of the route without
            overlap. The start point of a specified interval is the same
            as the end point of the preceding interval.

            Example:

            ::

                polyline: A ---- B ---- C ---- D ---- E ---- F ---- G
                speed_reading_intervals: [A,C), [C,D), [D,G).
        fuel_consumption_microliters (int):
            The predicted fuel consumption in microliters. This field is
            only populated when ``FUEL_CONSUMPTION`` is included in the
            request's
            [ComputeRoutesRequest.extra_computations][google.maps.routing.v2.ComputeRoutesRequest.extra_computations].
        route_restrictions_partially_ignored (bool):
            Returned route may have restrictions that are
            not suitable for requested travel mode or route
            modifiers.
        transit_fare (google.type.money_pb2.Money):
            If present, contains the total fare or ticket costs on this
            route This property is only returned for ``TRANSIT``
            requests and only for routes where fare information is
            available for all transit steps.
    """

    toll_info: gmr_toll_info.TollInfo = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gmr_toll_info.TollInfo,
    )
    speed_reading_intervals: MutableSequence[
        speed_reading_interval.SpeedReadingInterval
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=speed_reading_interval.SpeedReadingInterval,
    )
    fuel_consumption_microliters: int = proto.Field(
        proto.INT64,
        number=5,
    )
    route_restrictions_partially_ignored: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    transit_fare: money_pb2.Money = proto.Field(
        proto.MESSAGE,
        number=7,
        message=money_pb2.Money,
    )


class RouteLegTravelAdvisory(proto.Message):
    r"""Contains the additional information that the user should be
    informed about on a leg step, such as possible traffic zone
    restrictions.

    Attributes:
        toll_info (google.maps.routing_v2.types.TollInfo):
            Contains information about tolls on the specific
            ``RouteLeg``. This field is only populated if we expect
            there are tolls on the ``RouteLeg`` and ``TOLLS`` is
            included in the request's
            [ComputeRoutesRequest.extra_computations][google.maps.routing.v2.ComputeRoutesRequest.extra_computations].
            If this field is set but the estimated_price subfield is not
            populated, we expect that road contains tolls but we do not
            know an estimated price. If ``toll_info`` does not exist,
            then there is no toll on the ``RouteLeg``.
        speed_reading_intervals (MutableSequence[google.maps.routing_v2.types.SpeedReadingInterval]):
            Speed reading intervals indicating traffic density. This
            field is only populated for requests when the request has a
            ``TRAFFIC_AWARE`` or ``TRAFFIC_AWARE_OPTIMAL``
            [ComputeRoutesRequest.routing_preference][google.maps.routing.v2.ComputeRoutesRequest.routing_preference]
            value, and ``TRAFFIC_ON_POLYLINE`` is included in the
            [ComputeRoutesRequest.extra_computations][google.maps.routing.v2.ComputeRoutesRequest.extra_computations].
            The intervals cover the entire polyline of the ``RouteLeg``
            without overlap. The start point of a specified interval is
            the same as the end point of the preceding interval.

            Example:

            ::

                polyline: A ---- B ---- C ---- D ---- E ---- F ---- G
                speed_reading_intervals: [A,C), [C,D), [D,G).
    """

    toll_info: gmr_toll_info.TollInfo = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gmr_toll_info.TollInfo,
    )
    speed_reading_intervals: MutableSequence[
        speed_reading_interval.SpeedReadingInterval
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=speed_reading_interval.SpeedReadingInterval,
    )


class RouteLegStepTravelAdvisory(proto.Message):
    r"""Contains the additional information that the user should be
    informed about, such as possible traffic zone restrictions on a
    leg step.

    Attributes:
        speed_reading_intervals (MutableSequence[google.maps.routing_v2.types.SpeedReadingInterval]):
            NOTE: This field is not currently populated.
    """

    speed_reading_intervals: MutableSequence[
        speed_reading_interval.SpeedReadingInterval
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=speed_reading_interval.SpeedReadingInterval,
    )


class RouteLeg(proto.Message):
    r"""Contains a segment between non-``via`` waypoints.

    Attributes:
        distance_meters (int):
            The travel distance of the route leg, in
            meters.
        duration (google.protobuf.duration_pb2.Duration):
            The length of time needed to navigate the leg. If the
            ``route_preference`` is set to ``TRAFFIC_UNAWARE``, then
            this value is the same as ``static_duration``. If the
            ``route_preference`` is either ``TRAFFIC_AWARE`` or
            ``TRAFFIC_AWARE_OPTIMAL``, then this value is calculated
            taking traffic conditions into account.
        static_duration (google.protobuf.duration_pb2.Duration):
            The duration of travel through the leg,
            calculated without taking traffic conditions
            into consideration.
        polyline (google.maps.routing_v2.types.Polyline):
            The overall polyline for this leg that includes each
            ``step``'s polyline.
        start_location (google.maps.routing_v2.types.Location):
            The start location of this leg. This location might be
            different from the provided ``origin``. For example, when
            the provided ``origin`` is not near a road, this is a point
            on the road.
        end_location (google.maps.routing_v2.types.Location):
            The end location of this leg. This location might be
            different from the provided ``destination``. For example,
            when the provided ``destination`` is not near a road, this
            is a point on the road.
        steps (MutableSequence[google.maps.routing_v2.types.RouteLegStep]):
            An array of steps denoting segments within
            this leg. Each step represents one navigation
            instruction.
        travel_advisory (google.maps.routing_v2.types.RouteLegTravelAdvisory):
            Contains the additional information that the
            user should be informed about, such as possible
            traffic zone restrictions, on a route leg.
        localized_values (google.maps.routing_v2.types.RouteLeg.RouteLegLocalizedValues):
            Text representations of properties of the ``RouteLeg``.
        steps_overview (google.maps.routing_v2.types.RouteLeg.StepsOverview):
            Overview information about the steps in this ``RouteLeg``.
            This field is only populated for TRANSIT routes.
    """

    class RouteLegLocalizedValues(proto.Message):
        r"""Text representations of certain properties.

        Attributes:
            distance (google.type.localized_text_pb2.LocalizedText):
                Travel distance represented in text form.
            duration (google.type.localized_text_pb2.LocalizedText):
                Duration, represented in text form and localized to the
                region of the query. Takes traffic conditions into
                consideration. Note: If you did not request traffic
                information, this value is the same value as
                static_duration.
            static_duration (google.type.localized_text_pb2.LocalizedText):
                Duration without taking traffic conditions
                into consideration, represented in text form.
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

    class StepsOverview(proto.Message):
        r"""Provides overview information about a list of ``RouteLegStep``\ s.

        Attributes:
            multi_modal_segments (MutableSequence[google.maps.routing_v2.types.RouteLeg.StepsOverview.MultiModalSegment]):
                Summarized information about different multi-modal segments
                of the ``RouteLeg.steps``. This field is not populated if
                the ``RouteLeg`` does not contain any multi-modal segments
                in the steps.
        """

        class MultiModalSegment(proto.Message):
            r"""Provides summarized information about different multi-modal segments
            of the ``RouteLeg.steps``. A multi-modal segment is defined as one
            or more contiguous ``RouteLegStep`` that have the same
            ``RouteTravelMode``. This field is not populated if the ``RouteLeg``
            does not contain any multi-modal segments in the steps.


            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                step_start_index (int):
                    The corresponding ``RouteLegStep`` index that is the start
                    of a multi-modal segment.

                    This field is a member of `oneof`_ ``_step_start_index``.
                step_end_index (int):
                    The corresponding ``RouteLegStep`` index that is the end of
                    a multi-modal segment.

                    This field is a member of `oneof`_ ``_step_end_index``.
                navigation_instruction (google.maps.routing_v2.types.NavigationInstruction):
                    NavigationInstruction for the multi-modal
                    segment.
                travel_mode (google.maps.routing_v2.types.RouteTravelMode):
                    The travel mode of the multi-modal segment.
            """

            step_start_index: int = proto.Field(
                proto.INT32,
                number=1,
                optional=True,
            )
            step_end_index: int = proto.Field(
                proto.INT32,
                number=2,
                optional=True,
            )
            navigation_instruction: gmr_navigation_instruction.NavigationInstruction = (
                proto.Field(
                    proto.MESSAGE,
                    number=3,
                    message=gmr_navigation_instruction.NavigationInstruction,
                )
            )
            travel_mode: route_travel_mode.RouteTravelMode = proto.Field(
                proto.ENUM,
                number=4,
                enum=route_travel_mode.RouteTravelMode,
            )

        multi_modal_segments: MutableSequence[
            "RouteLeg.StepsOverview.MultiModalSegment"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="RouteLeg.StepsOverview.MultiModalSegment",
        )

    distance_meters: int = proto.Field(
        proto.INT32,
        number=1,
    )
    duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=2,
        message=duration_pb2.Duration,
    )
    static_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=3,
        message=duration_pb2.Duration,
    )
    polyline: gmr_polyline.Polyline = proto.Field(
        proto.MESSAGE,
        number=4,
        message=gmr_polyline.Polyline,
    )
    start_location: location.Location = proto.Field(
        proto.MESSAGE,
        number=5,
        message=location.Location,
    )
    end_location: location.Location = proto.Field(
        proto.MESSAGE,
        number=6,
        message=location.Location,
    )
    steps: MutableSequence["RouteLegStep"] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message="RouteLegStep",
    )
    travel_advisory: "RouteLegTravelAdvisory" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="RouteLegTravelAdvisory",
    )
    localized_values: RouteLegLocalizedValues = proto.Field(
        proto.MESSAGE,
        number=9,
        message=RouteLegLocalizedValues,
    )
    steps_overview: StepsOverview = proto.Field(
        proto.MESSAGE,
        number=10,
        message=StepsOverview,
    )


class RouteLegStep(proto.Message):
    r"""Contains a segment of a
    [``RouteLeg``][google.maps.routing.v2.RouteLeg]. A step corresponds
    to a single navigation instruction. Route legs are made up of steps.

    Attributes:
        distance_meters (int):
            The travel distance of this step, in meters.
            In some circumstances, this field might not have
            a value.
        static_duration (google.protobuf.duration_pb2.Duration):
            The duration of travel through this step
            without taking traffic conditions into
            consideration. In some circumstances, this field
            might not have a value.
        polyline (google.maps.routing_v2.types.Polyline):
            The polyline associated with this step.
        start_location (google.maps.routing_v2.types.Location):
            The start location of this step.
        end_location (google.maps.routing_v2.types.Location):
            The end location of this step.
        navigation_instruction (google.maps.routing_v2.types.NavigationInstruction):
            Navigation instructions.
        travel_advisory (google.maps.routing_v2.types.RouteLegStepTravelAdvisory):
            Contains the additional information that the
            user should be informed about, such as possible
            traffic zone restrictions, on a leg step.
        localized_values (google.maps.routing_v2.types.RouteLegStep.RouteLegStepLocalizedValues):
            Text representations of properties of the ``RouteLegStep``.
        transit_details (google.maps.routing_v2.types.RouteLegStepTransitDetails):
            Details pertaining to this step if the travel mode is
            ``TRANSIT``.
        travel_mode (google.maps.routing_v2.types.RouteTravelMode):
            The travel mode used for this step.
    """

    class RouteLegStepLocalizedValues(proto.Message):
        r"""Text representations of certain properties.

        Attributes:
            distance (google.type.localized_text_pb2.LocalizedText):
                Travel distance represented in text form.
            static_duration (google.type.localized_text_pb2.LocalizedText):
                Duration without taking traffic conditions
                into consideration, represented in text form.
        """

        distance: localized_text_pb2.LocalizedText = proto.Field(
            proto.MESSAGE,
            number=1,
            message=localized_text_pb2.LocalizedText,
        )
        static_duration: localized_text_pb2.LocalizedText = proto.Field(
            proto.MESSAGE,
            number=3,
            message=localized_text_pb2.LocalizedText,
        )

    distance_meters: int = proto.Field(
        proto.INT32,
        number=1,
    )
    static_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=2,
        message=duration_pb2.Duration,
    )
    polyline: gmr_polyline.Polyline = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gmr_polyline.Polyline,
    )
    start_location: location.Location = proto.Field(
        proto.MESSAGE,
        number=4,
        message=location.Location,
    )
    end_location: location.Location = proto.Field(
        proto.MESSAGE,
        number=5,
        message=location.Location,
    )
    navigation_instruction: gmr_navigation_instruction.NavigationInstruction = (
        proto.Field(
            proto.MESSAGE,
            number=6,
            message=gmr_navigation_instruction.NavigationInstruction,
        )
    )
    travel_advisory: "RouteLegStepTravelAdvisory" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="RouteLegStepTravelAdvisory",
    )
    localized_values: RouteLegStepLocalizedValues = proto.Field(
        proto.MESSAGE,
        number=8,
        message=RouteLegStepLocalizedValues,
    )
    transit_details: "RouteLegStepTransitDetails" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="RouteLegStepTransitDetails",
    )
    travel_mode: route_travel_mode.RouteTravelMode = proto.Field(
        proto.ENUM,
        number=10,
        enum=route_travel_mode.RouteTravelMode,
    )


class RouteLegStepTransitDetails(proto.Message):
    r"""Additional information for the ``RouteLegStep`` related to
    ``TRANSIT`` routes.

    Attributes:
        stop_details (google.maps.routing_v2.types.RouteLegStepTransitDetails.TransitStopDetails):
            Information about the arrival and departure
            stops for the step.
        localized_values (google.maps.routing_v2.types.RouteLegStepTransitDetails.TransitDetailsLocalizedValues):
            Text representations of properties of the
            ``RouteLegStepTransitDetails``.
        headsign (str):
            Specifies the direction in which to travel on
            this line as marked on the vehicle or at the
            departure stop. The direction is often the
            terminus station.
        headway (google.protobuf.duration_pb2.Duration):
            Specifies the expected time as a duration
            between departures from the same stop at this
            time. For example, with a headway seconds value
            of 600, you would expect a ten minute wait if
            you should miss your bus.
        transit_line (google.maps.routing_v2.types.TransitLine):
            Information about the transit line used in
            this step.
        stop_count (int):
            The number of stops from the departure to the arrival stop.
            This count includes the arrival stop, but excludes the
            departure stop. For example, if your route leaves from Stop
            A, passes through stops B and C, and arrives at stop D,
            stop_count returns 3.
        trip_short_text (str):
            The text that appears in schedules and sign boards to
            identify a transit trip to passengers. The text should
            uniquely identify a trip within a service day. For example,
            "538" is the ``trip_short_text`` of the Amtrak train that
            leaves San Jose, CA at 15:10 on weekdays to Sacramento, CA.
    """

    class TransitStopDetails(proto.Message):
        r"""Details about the transit stops for the ``RouteLegStep``.

        Attributes:
            arrival_stop (google.maps.routing_v2.types.TransitStop):
                Information about the arrival stop for the
                step.
            arrival_time (google.protobuf.timestamp_pb2.Timestamp):
                The estimated time of arrival for the step.
            departure_stop (google.maps.routing_v2.types.TransitStop):
                Information about the departure stop for the
                step.
            departure_time (google.protobuf.timestamp_pb2.Timestamp):
                The estimated time of departure for the step.
        """

        arrival_stop: transit.TransitStop = proto.Field(
            proto.MESSAGE,
            number=1,
            message=transit.TransitStop,
        )
        arrival_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=2,
            message=timestamp_pb2.Timestamp,
        )
        departure_stop: transit.TransitStop = proto.Field(
            proto.MESSAGE,
            number=3,
            message=transit.TransitStop,
        )
        departure_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=4,
            message=timestamp_pb2.Timestamp,
        )

    class TransitDetailsLocalizedValues(proto.Message):
        r"""Localized descriptions of values for ``RouteTransitDetails``.

        Attributes:
            arrival_time (google.maps.routing_v2.types.LocalizedTime):
                Time in its formatted text representation
                with a corresponding time zone.
            departure_time (google.maps.routing_v2.types.LocalizedTime):
                Time in its formatted text representation
                with a corresponding time zone.
        """

        arrival_time: localized_time.LocalizedTime = proto.Field(
            proto.MESSAGE,
            number=1,
            message=localized_time.LocalizedTime,
        )
        departure_time: localized_time.LocalizedTime = proto.Field(
            proto.MESSAGE,
            number=2,
            message=localized_time.LocalizedTime,
        )

    stop_details: TransitStopDetails = proto.Field(
        proto.MESSAGE,
        number=1,
        message=TransitStopDetails,
    )
    localized_values: TransitDetailsLocalizedValues = proto.Field(
        proto.MESSAGE,
        number=2,
        message=TransitDetailsLocalizedValues,
    )
    headsign: str = proto.Field(
        proto.STRING,
        number=3,
    )
    headway: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=4,
        message=duration_pb2.Duration,
    )
    transit_line: transit.TransitLine = proto.Field(
        proto.MESSAGE,
        number=5,
        message=transit.TransitLine,
    )
    stop_count: int = proto.Field(
        proto.INT32,
        number=6,
    )
    trip_short_text: str = proto.Field(
        proto.STRING,
        number=7,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
