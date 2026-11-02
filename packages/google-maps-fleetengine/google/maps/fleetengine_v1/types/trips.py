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
import google.protobuf.wrappers_pb2 as wrappers_pb2  # type: ignore
import google.type.latlng_pb2 as latlng_pb2  # type: ignore
import proto  # type: ignore

from google.maps.fleetengine_v1.types import fleetengine, traffic

__protobuf__ = proto.module(
    package="maps.fleetengine.v1",
    manifest={
        "TripStatus",
        "BillingPlatformIdentifier",
        "TripView",
        "Trip",
        "StopLocation",
    },
)


class TripStatus(proto.Enum):
    r"""The status of a trip indicating its progression.

    Values:
        UNKNOWN_TRIP_STATUS (0):
            Default, used for unspecified or unrecognized
            trip status.
        NEW (1):
            Newly created trip.
        ENROUTE_TO_PICKUP (2):
            The driver is on their way to the pickup
            point.
        ARRIVED_AT_PICKUP (3):
            The driver has arrived at the pickup point.
        ARRIVED_AT_INTERMEDIATE_DESTINATION (7):
            The driver has arrived at an intermediate
            destination and is waiting for the rider.
        ENROUTE_TO_INTERMEDIATE_DESTINATION (8):
            The driver is on their way to an intermediate
            destination (not the dropoff point).
        ENROUTE_TO_DROPOFF (4):
            The driver has picked up the rider and is on
            their way to the next destination.
        COMPLETE (5):
            The rider has been dropped off and the trip
            is complete.
        CANCELED (6):
            The trip was canceled prior to pickup by the
            driver, rider, or rideshare provider.
    """

    UNKNOWN_TRIP_STATUS = 0
    NEW = 1
    ENROUTE_TO_PICKUP = 2
    ARRIVED_AT_PICKUP = 3
    ARRIVED_AT_INTERMEDIATE_DESTINATION = 7
    ENROUTE_TO_INTERMEDIATE_DESTINATION = 8
    ENROUTE_TO_DROPOFF = 4
    COMPLETE = 5
    CANCELED = 6


class BillingPlatformIdentifier(proto.Enum):
    r"""A set of values that indicate upon which platform the request
    was issued.

    Values:
        BILLING_PLATFORM_IDENTIFIER_UNSPECIFIED (0):
            Default. Used for unspecified platforms.
        SERVER (1):
            The platform is a client server.
        WEB (2):
            The platform is a web browser.
        ANDROID (3):
            The platform is an Android mobile device.
        IOS (4):
            The platform is an IOS mobile device.
        OTHERS (5):
            Other platforms that are not listed in this
            enumeration.
    """

    BILLING_PLATFORM_IDENTIFIER_UNSPECIFIED = 0
    SERVER = 1
    WEB = 2
    ANDROID = 3
    IOS = 4
    OTHERS = 5


class TripView(proto.Enum):
    r"""Selector for different sets of Trip fields in a ``GetTrip``
    response. See `AIP-157 <https://google.aip.dev/157>`__ for context.
    Additional views are likely to be added.

    Values:
        TRIP_VIEW_UNSPECIFIED (0):
            The default value. For backwards-compatibility, the API will
            default to an SDK view. To ensure stability and support,
            customers are advised to select a ``TripView`` other than
            ``SDK``.
        SDK (1):
            Includes fields that may not be interpretable
            or supportable using publicly available
            libraries.
        JOURNEY_SHARING_V1S (2):
            Trip fields are populated for the Journey
            Sharing use case. This view is intended for
            server-to-server communications.
    """

    TRIP_VIEW_UNSPECIFIED = 0
    SDK = 1
    JOURNEY_SHARING_V1S = 2


class Trip(proto.Message):
    r"""Trip metadata.

    Attributes:
        name (str):
            Output only. In the format
            "providers/{provider}/trips/{trip}".
        vehicle_id (str):
            ID of the vehicle making this trip.
        trip_status (google.maps.fleetengine_v1.types.TripStatus):
            Current status of the trip.
        trip_type (google.maps.fleetengine_v1.types.TripType):
            The type of the trip.
        pickup_point (google.maps.fleetengine_v1.types.TerminalLocation):
            Location where customer indicates they will
            be picked up.
        actual_pickup_point (google.maps.fleetengine_v1.types.StopLocation):
            Input only. The actual location when and
            where customer was picked up. This field is for
            provider to provide feedback on actual pickup
            information.
        actual_pickup_arrival_point (google.maps.fleetengine_v1.types.StopLocation):
            Input only. The actual time and location of
            the driver arrival at the pickup point.
            This field is for provider to provide feedback
            on actual arrival information at the pickup
            point.
        pickup_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Either the estimated future time
            when the rider(s) will be picked up, or the
            actual time when they were picked up.
        intermediate_destinations (MutableSequence[google.maps.fleetengine_v1.types.TerminalLocation]):
            Intermediate stops in order that the trip
            requests (in addition to pickup and dropoff).
            Initially this will not be supported for shared
            trips.
        intermediate_destinations_version (google.protobuf.timestamp_pb2.Timestamp):
            Indicates the last time the ``intermediate_destinations``
            was modified. Your server should cache this value and pass
            it in ``UpdateTripRequest`` when update
            ``intermediate_destination_index`` to ensure the
            ``intermediate_destinations`` is not changed.
        intermediate_destination_index (int):
            When ``TripStatus`` is
            ``ENROUTE_TO_INTERMEDIATE_DESTINATION``, a number between
            [0..N-1] indicating which intermediate destination the
            vehicle will cross next. When ``TripStatus`` is
            ``ARRIVED_AT_INTERMEDIATE_DESTINATION``, a number between
            [0..N-1] indicating which intermediate destination the
            vehicle is at. The provider sets this value. If there are no
            ``intermediate_destinations``, this field is ignored.
        actual_intermediate_destination_arrival_points (MutableSequence[google.maps.fleetengine_v1.types.StopLocation]):
            Input only. The actual time and location of
            the driver's arrival at an intermediate
            destination. This field is for provider to
            provide feedback on actual arrival information
            at intermediate destinations.
        actual_intermediate_destinations (MutableSequence[google.maps.fleetengine_v1.types.StopLocation]):
            Input only. The actual time and location when
            and where the customer was picked up from an
            intermediate destination. This field is for
            provider to provide feedback on actual pickup
            information at intermediate destinations.
        dropoff_point (google.maps.fleetengine_v1.types.TerminalLocation):
            Location where customer indicates they will
            be dropped off.
        actual_dropoff_point (google.maps.fleetengine_v1.types.StopLocation):
            Input only. The actual time and location when
            and where customer was dropped off. This field
            is for provider to provide feedback on actual
            dropoff information.
        dropoff_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Either the estimated future time
            when the rider(s) will be dropped off at the
            final destination, or the actual time when they
            were dropped off.
        remaining_waypoints (MutableSequence[google.maps.fleetengine_v1.types.TripWaypoint]):
            Output only. The full path from the current
            location to the dropoff point, inclusive. This
            path could include waypoints from other trips.
        vehicle_waypoints (MutableSequence[google.maps.fleetengine_v1.types.TripWaypoint]):
            This field supports manual ordering of the waypoints for the
            trip. It contains all of the remaining waypoints for the
            assigned vehicle, as well as the pickup and drop-off
            waypoints for this trip. If the trip hasn't been assigned to
            a vehicle, then Fleet Engine ignores this field. For privacy
            reasons, this field is only populated by the server on
            ``UpdateTrip`` and ``CreateTrip`` calls, NOT on ``GetTrip``
            calls.
        route (MutableSequence[google.type.latlng_pb2.LatLng]):
            Output only. Anticipated route for this trip to the first
            entry in remaining_waypoints. Note that the first waypoint
            may belong to a different trip.
        current_route_segment (str):
            Output only. An encoded path to the next
            waypoint.
            Note: This field is intended only for use by the
            Driver SDK and Consumer SDK. Decoding is not yet
            supported.
        current_route_segment_version (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Indicates the last time the
            route was modified.
            Note: This field is intended only for use by the
            Driver SDK and Consumer SDK.
        current_route_segment_traffic (google.maps.fleetengine_v1.types.ConsumableTrafficPolyline):
            Output only. Indicates the traffic conditions along the
            ``current_route_segment`` when they're available.

            Note: This field is intended only for use by the Driver SDK
            and Consumer SDK.
        current_route_segment_traffic_version (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Indicates the last time the
            ``current_route_segment_traffic`` was modified.

            Note: This field is intended only for use by the Driver SDK
            and Consumer SDK.
        current_route_segment_end_point (google.maps.fleetengine_v1.types.TripWaypoint):
            Output only. The waypoint where ``current_route_segment``
            ends.
        remaining_distance_meters (google.protobuf.wrappers_pb2.Int32Value):
            Output only. The remaining driving distance in the
            ``current_route_segment`` field. The value is unspecified if
            the trip is not assigned to a vehicle, or the trip is
            completed or cancelled.
        eta_to_first_waypoint (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The ETA to the next waypoint (the first entry
            in the ``remaining_waypoints`` field). The value is
            unspecified if the trip is not assigned to a vehicle, or the
            trip is inactive (completed or cancelled).
        remaining_time_to_first_waypoint (google.protobuf.duration_pb2.Duration):
            Output only. The duration from when the Trip data is
            returned to the time in ``Trip.eta_to_first_waypoint``. The
            value is unspecified if the trip is not assigned to a
            vehicle, or the trip is inactive (completed or cancelled).
        remaining_waypoints_version (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Indicates the last time that
            ``remaining_waypoints`` was changed (a waypoint was added,
            removed, or changed).
        remaining_waypoints_route_version (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Indicates the last time the
            ``remaining_waypoints.path_to_waypoint`` and
            ``remaining_waypoints.traffic_to_waypoint`` were modified.
            Your client app should cache this value and pass it in
            ``GetTripRequest`` to ensure the paths and traffic for
            ``remaining_waypoints`` are only returned if updated.
        number_of_passengers (int):
            Immutable. Indicates the number of passengers on this trip
            and does not include the driver. A vehicle must have
            available capacity to be returned in a ``SearchVehicles``
            response.
        last_location (google.maps.fleetengine_v1.types.VehicleLocation):
            Output only. Indicates the last reported
            location of the vehicle along the route.
        last_location_snappable (bool):
            Output only. Indicates whether the vehicle's
            ``last_location`` can be snapped to the
            current_route_segment. False if ``last_location`` or
            ``current_route_segment`` doesn't exist. It is computed by
            Fleet Engine. Any update from clients will be ignored.
        view (google.maps.fleetengine_v1.types.TripView):
            The subset of Trip fields that are populated
            and how they should be interpreted.
        attributes (MutableSequence[google.maps.fleetengine_v1.types.TripAttribute]):
            A list of custom Trip attributes. Each
            attribute must have a unique key.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    vehicle_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    trip_status: "TripStatus" = proto.Field(
        proto.ENUM,
        number=3,
        enum="TripStatus",
    )
    trip_type: fleetengine.TripType = proto.Field(
        proto.ENUM,
        number=4,
        enum=fleetengine.TripType,
    )
    pickup_point: fleetengine.TerminalLocation = proto.Field(
        proto.MESSAGE,
        number=5,
        message=fleetengine.TerminalLocation,
    )
    actual_pickup_point: "StopLocation" = proto.Field(
        proto.MESSAGE,
        number=22,
        message="StopLocation",
    )
    actual_pickup_arrival_point: "StopLocation" = proto.Field(
        proto.MESSAGE,
        number=32,
        message="StopLocation",
    )
    pickup_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    intermediate_destinations: MutableSequence[fleetengine.TerminalLocation] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=14,
            message=fleetengine.TerminalLocation,
        )
    )
    intermediate_destinations_version: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=25,
        message=timestamp_pb2.Timestamp,
    )
    intermediate_destination_index: int = proto.Field(
        proto.INT32,
        number=15,
    )
    actual_intermediate_destination_arrival_points: MutableSequence["StopLocation"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=33,
            message="StopLocation",
        )
    )
    actual_intermediate_destinations: MutableSequence["StopLocation"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=34,
            message="StopLocation",
        )
    )
    dropoff_point: fleetengine.TerminalLocation = proto.Field(
        proto.MESSAGE,
        number=7,
        message=fleetengine.TerminalLocation,
    )
    actual_dropoff_point: "StopLocation" = proto.Field(
        proto.MESSAGE,
        number=23,
        message="StopLocation",
    )
    dropoff_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    remaining_waypoints: MutableSequence[fleetengine.TripWaypoint] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=16,
            message=fleetengine.TripWaypoint,
        )
    )
    vehicle_waypoints: MutableSequence[fleetengine.TripWaypoint] = proto.RepeatedField(
        proto.MESSAGE,
        number=20,
        message=fleetengine.TripWaypoint,
    )
    route: MutableSequence[latlng_pb2.LatLng] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message=latlng_pb2.LatLng,
    )
    current_route_segment: str = proto.Field(
        proto.STRING,
        number=21,
    )
    current_route_segment_version: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=17,
        message=timestamp_pb2.Timestamp,
    )
    current_route_segment_traffic: traffic.ConsumableTrafficPolyline = proto.Field(
        proto.MESSAGE,
        number=28,
        message=traffic.ConsumableTrafficPolyline,
    )
    current_route_segment_traffic_version: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=30,
        message=timestamp_pb2.Timestamp,
    )
    current_route_segment_end_point: fleetengine.TripWaypoint = proto.Field(
        proto.MESSAGE,
        number=24,
        message=fleetengine.TripWaypoint,
    )
    remaining_distance_meters: wrappers_pb2.Int32Value = proto.Field(
        proto.MESSAGE,
        number=12,
        message=wrappers_pb2.Int32Value,
    )
    eta_to_first_waypoint: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=13,
        message=timestamp_pb2.Timestamp,
    )
    remaining_time_to_first_waypoint: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=27,
        message=duration_pb2.Duration,
    )
    remaining_waypoints_version: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=19,
        message=timestamp_pb2.Timestamp,
    )
    remaining_waypoints_route_version: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=29,
        message=timestamp_pb2.Timestamp,
    )
    number_of_passengers: int = proto.Field(
        proto.INT32,
        number=10,
    )
    last_location: fleetengine.VehicleLocation = proto.Field(
        proto.MESSAGE,
        number=11,
        message=fleetengine.VehicleLocation,
    )
    last_location_snappable: bool = proto.Field(
        proto.BOOL,
        number=26,
    )
    view: "TripView" = proto.Field(
        proto.ENUM,
        number=31,
        enum="TripView",
    )
    attributes: MutableSequence[fleetengine.TripAttribute] = proto.RepeatedField(
        proto.MESSAGE,
        number=35,
        message=fleetengine.TripAttribute,
    )


class StopLocation(proto.Message):
    r"""The actual location where a stop (pickup/dropoff) happened.

    Attributes:
        point (google.type.latlng_pb2.LatLng):
            Required. Denotes the actual location.
        timestamp (google.protobuf.timestamp_pb2.Timestamp):
            Indicates when the stop happened.
        stop_time (google.protobuf.timestamp_pb2.Timestamp):
            Input only. Deprecated.  Use the timestamp
            field.
    """

    point: latlng_pb2.LatLng = proto.Field(
        proto.MESSAGE,
        number=1,
        message=latlng_pb2.LatLng,
    )
    timestamp: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    stop_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
