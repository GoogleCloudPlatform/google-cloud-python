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
import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.type.latlng_pb2 as latlng_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.maps.navconnect.v1",
    manifest={
        "Trip",
        "TripConfig",
        "AuthToken",
        "TripExecution",
        "RouteDeviation",
        "Stop",
        "Location",
        "SimplePolyline",
        "SpeedReadingInterval",
        "Route",
        "CreateTripRequest",
        "GetTripRequest",
    },
)


class Trip(proto.Message):
    r"""A trip.

    Attributes:
        name (str):
            Output only. Identifier. The resource name of the trip.
            Format: projects/{project_number}/trips/{trip_id}.
        config (google.maps.navconnect_v1.types.TripConfig):
            Immutable. The configuration for the trip.
        android_app_id (str):
            Input only. Immutable. The Android application ID of the
            mobile application that will use the trip. At least one of
            ``android_app_id`` or ``ios_app_id`` must be set.
        ios_app_id (str):
            Input only. Immutable. The iOS bundle ID of the mobile
            application that will use the trip. At least one of
            ``android_app_id`` or ``ios_app_id`` must be set.
        auth_token (google.maps.navconnect_v1.types.AuthToken):
            Output only. An opaque token that authorizes access to begin
            a NavConnect trip in Google Maps or Waze and grants these
            applications access to update the trip. Only returned by
            ``CreateTrip``.
        state (google.maps.navconnect_v1.types.Trip.State):
            Output only. The Trip state.
        execution (google.maps.navconnect_v1.types.TripExecution):
            Output only. The latest data about the
            execution of the trip. This may not be set if
            the trip is in an error state.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time according to the server
            when the trip was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time at which the server
            received the latest trip update.
    """

    class State(proto.Enum):
        r"""All possible trip states.

        Values:
            STATE_UNSPECIFIED (0):
                The trip state is unspecified.
            NEW (1):
                The trip was created but has not yet started.
            ENROUTE (2):
                The transporter is enroute to the
                destination.
            ARRIVED (3):
                The transporter arrived at the destination.
            SUSPENDED (4):
                The trip was suspended.
            FAILED (5):
                The trip failed to complete successfully.
            CLIENT_ERROR (6):
                The trip failed due to a client error.
        """

        STATE_UNSPECIFIED = 0
        NEW = 1
        ENROUTE = 2
        ARRIVED = 3
        SUSPENDED = 4
        FAILED = 5
        CLIENT_ERROR = 6

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    config: "TripConfig" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="TripConfig",
    )
    android_app_id: str = proto.Field(
        proto.STRING,
        number=8,
    )
    ios_app_id: str = proto.Field(
        proto.STRING,
        number=9,
    )
    auth_token: "AuthToken" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="AuthToken",
    )
    state: State = proto.Field(
        proto.ENUM,
        number=3,
        enum=State,
    )
    execution: "TripExecution" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="TripExecution",
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )


class TripConfig(proto.Message):
    r"""Configuration for the trip.

    Attributes:
        enable_high_frequency_updates (bool):
            Optional. Whether to enable high-frequency
            trip updates.
            NOTE: Enabling this feature logs the trip under
            Enterprise Tier usage, and is subject to
            Enterprise Tier rates.
        enable_pubsub (bool):
            Optional. Whether to enable pubsub
            notifications for the trip.
        pubsub_field_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. If set, only the specified subset of the Trip
            fields will be included in the pubsub notifications.

            If not set, all Trip fields will be included in the pubsub
            notifications (default behavior).

            The following fields are not supported:

            - ``android_app_id``
            - ``ios_app_id``
            - ``auth_token``
            - ``config``

            NOTE: This field is ignored if ``enable_pubsub`` is false.
        enable_remaining_route_reporting (bool):
            Optional. Whether to enable remaining route
            reporting for the trip.
            NOTE: Enabling this feature logs the trip under
            Enterprise Tier usage, and is subject to
            Enterprise Tier rates.
        enable_route_deviation_reporting (bool):
            Optional. Whether to enable route deviation
            reporting for the trip.
            NOTE: Enabling this feature logs the trip under
            Enterprise Tier usage, and is subject to
            Enterprise Tier rates.
    """

    enable_high_frequency_updates: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    enable_pubsub: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    pubsub_field_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=3,
        message=field_mask_pb2.FieldMask,
    )
    enable_remaining_route_reporting: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    enable_route_deviation_reporting: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class AuthToken(proto.Message):
    r"""An authentication token.

    Attributes:
        token (str):
            Output only. The authentication token that
            should be passed to the mobile application.
        expire_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time at which the authentication
            token will expire.
    """

    token: str = proto.Field(
        proto.STRING,
        number=1,
    )
    expire_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )


class TripExecution(proto.Message):
    r"""Data about the execution of the trip.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        origin (google.maps.navconnect_v1.types.Location):
            Output only. Origin of the trip which is
            generally the transporter's location at start of
            the NavConnect trip.
        destination (google.maps.navconnect_v1.types.Stop):
            Output only. The destination of the trip as
            reported by the mobile application.
        location (google.maps.navconnect_v1.types.Location):
            Output only. The location signal representing
            the last known location of the transporter. This
            will be the road snapped location if available.
        remaining_route (google.maps.navconnect_v1.types.Route):
            Output only. Provides the polyline for the
            remaining portion of the route.
        last_route_deviation (google.maps.navconnect_v1.types.RouteDeviation):
            Output only. The most recent route deviation
            event captured during the trip.
        traveled_duration (google.protobuf.duration_pb2.Duration):
            Output only. Time traveled thus far.
        remaining_duration (google.protobuf.duration_pb2.Duration):
            Output only. Time left on this trip as
            estimated by Google.
        traveled_distance_meters (int):
            Output only. Distance traveled from the
            origin in meters.

            This field is a member of `oneof`_ ``_traveled_distance_meters``.
        remaining_distance_meters (int):
            Output only. Distance remaining to the
            destination in meters.

            This field is a member of `oneof`_ ``_remaining_distance_meters``.
        stop_added_in_route (bool):
            Output only. Indicates whether a stop was
            added along the route.

            This field is a member of `oneof`_ ``_stop_added_in_route``.
    """

    origin: "Location" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Location",
    )
    destination: "Stop" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Stop",
    )
    location: "Location" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Location",
    )
    remaining_route: "Route" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="Route",
    )
    last_route_deviation: "RouteDeviation" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="RouteDeviation",
    )
    traveled_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=4,
        message=duration_pb2.Duration,
    )
    remaining_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=5,
        message=duration_pb2.Duration,
    )
    traveled_distance_meters: int = proto.Field(
        proto.INT32,
        number=6,
        optional=True,
    )
    remaining_distance_meters: int = proto.Field(
        proto.INT32,
        number=7,
        optional=True,
    )
    stop_added_in_route: bool = proto.Field(
        proto.BOOL,
        number=8,
        optional=True,
    )


class RouteDeviation(proto.Message):
    r"""Route deviation information.

    Attributes:
        location (google.maps.navconnect_v1.types.Location):
            Output only. Location where the deviation
            occurred.
        source (google.maps.navconnect_v1.types.RouteDeviation.TriggerSource):
            Output only. Source for the deviation
            trigger.
    """

    class TriggerSource(proto.Enum):
        r"""The source that triggered the route deviation.

        Values:
            TRIGGER_SOURCE_UNSPECIFIED (0):
                The trigger source is unspecified.
            DRIVER_INITIATED_REROUTE (1):
                The route deviation was triggered by the
                driver (e.g. wrong turn).
            SYSTEM_INITIATED_REROUTE (2):
                The route deviation was triggered by the
                system (e.g. traffic closure).
        """

        TRIGGER_SOURCE_UNSPECIFIED = 0
        DRIVER_INITIATED_REROUTE = 1
        SYSTEM_INITIATED_REROUTE = 2

    location: "Location" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Location",
    )
    source: TriggerSource = proto.Field(
        proto.ENUM,
        number=2,
        enum=TriggerSource,
    )


class Stop(proto.Message):
    r"""A stop in the trip where some task is to be performed.

    Attributes:
        point (google.type.latlng_pb2.LatLng):
            Required. The location of the stop as a
            lat/lng.
    """

    point: latlng_pb2.LatLng = proto.Field(
        proto.MESSAGE,
        number=1,
        message=latlng_pb2.LatLng,
    )


class Location(proto.Message):
    r"""A location as reported by the mobile application.

    Attributes:
        point (google.type.latlng_pb2.LatLng):
            Output only. The location lat/lng.
        source_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the location was
            sourced as denoted by the client.
        server_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which the server
            received this location update.
    """

    point: latlng_pb2.LatLng = proto.Field(
        proto.MESSAGE,
        number=1,
        message=latlng_pb2.LatLng,
    )
    source_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    server_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )


class SimplePolyline(proto.Message):
    r"""Represents a polyline using a simple list of points.

    Attributes:
        points (MutableSequence[google.type.latlng_pb2.LatLng]):
            Output only. Ordered list of points
            representing the polyline.
    """

    points: MutableSequence[latlng_pb2.LatLng] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=latlng_pb2.LatLng,
    )


class SpeedReadingInterval(proto.Message):
    r"""Traffic density indicator on a contiguous segment of a path. Given a
    path with points P_0, P_1, ... , P_N (zero-based index), the
    SpeedReadingInterval defines an interval and describes its traffic
    using the ``Speed`` categories.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        start_polyline_point_index (int):
            Output only. The starting index of this
            interval in the path.

            This field is a member of `oneof`_ ``_start_polyline_point_index``.
        end_polyline_point_index (int):
            Output only. The ending index of this
            interval in the path.

            This field is a member of `oneof`_ ``_end_polyline_point_index``.
        speed (google.maps.navconnect_v1.types.SpeedReadingInterval.Speed):
            Output only. Traffic speed in this interval.
    """

    class Speed(proto.Enum):
        r"""The classification of polyline speed based on traffic data.

        Values:
            SPEED_UNSPECIFIED (0):
                The speed is unspecified.
            NORMAL (1):
                Normal speed, no traffic delays.
            SLOW (2):
                Slowdown detected, light to medium amount of
                traffic.
            TRAFFIC_JAM (3):
                Traffic delays, including standstill traffic.
        """

        SPEED_UNSPECIFIED = 0
        NORMAL = 1
        SLOW = 2
        TRAFFIC_JAM = 3

    start_polyline_point_index: int = proto.Field(
        proto.INT32,
        number=1,
        optional=True,
    )
    end_polyline_point_index: int = proto.Field(
        proto.INT32,
        number=2,
        optional=True,
    )
    speed: Speed = proto.Field(
        proto.ENUM,
        number=3,
        enum=Speed,
    )


class Route(proto.Message):
    r"""A route polyline.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        simple_polyline (google.maps.navconnect_v1.types.SimplePolyline):
            Output only. The route as a simple list of
            latlngs.

            This field is a member of `oneof`_ ``format``.
        encoded_polyline (str):
            Output only. The route as an encoded
            polyline. See
            https://developers.google.com/maps/documentation/utilities/polylinealgorithm.

            This field is a member of `oneof`_ ``format``.
        s2_polyline (bytes):
            Output only. The route as an encoded S2Polyline. See
            https://s2geometry.io/devguide/basic_types.html.

            This field is a member of `oneof`_ ``format``.
        geo_json (google.protobuf.struct_pb2.Struct):
            Output only. The route as a GeoJSON
            LineString. See
            https://tools.ietf.org/html/rfc7946#section-3.1.4.

            This field is a member of `oneof`_ ``format``.
        traffic_information (MutableSequence[google.maps.navconnect_v1.types.SpeedReadingInterval]):
            Output only. Traffic information on the polyline described
            as speed reading intervals.

            NOTES:

            - The intervals are non-overlapping.
            - The intervals are contiguous.
            - The intervals cover the entire polyline.
            - The intervals are sorted by increasing index.
            - Speed is specified for each interval.
    """

    simple_polyline: "SimplePolyline" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="format",
        message="SimplePolyline",
    )
    encoded_polyline: str = proto.Field(
        proto.STRING,
        number=5,
        oneof="format",
    )
    s2_polyline: bytes = proto.Field(
        proto.BYTES,
        number=2,
        oneof="format",
    )
    geo_json: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="format",
        message=struct_pb2.Struct,
    )
    traffic_information: MutableSequence["SpeedReadingInterval"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="SpeedReadingInterval",
    )


class CreateTripRequest(proto.Message):
    r"""Request message for NavConnectService.CreateTrip.

    Attributes:
        parent (str):
            Required. The parent resource under which this trip will be
            created. Format: projects/{project_number}
        trip_id (str):
            Required. The ID to use for the trip, which
            will become the final component of the trip's
            resource name.

            This value must be a valid RFC-4122 UUID.
        trip (google.maps.navconnect_v1.types.Trip):
            Required. The trip to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    trip_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    trip: "Trip" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Trip",
    )


class GetTripRequest(proto.Message):
    r"""Request message for NavConnectService.GetTrip.

    Attributes:
        name (str):
            Required. The resource name of the trip to get. Format:
            projects/{project}/trips/{trip_id}
        route_polyline_format (google.maps.navconnect_v1.types.GetTripRequest.RoutePolylineFormat):
            Optional. The format of the route polyline to return. If not
            set, ``SIMPLE`` route polyline will be returned.
    """

    class RoutePolylineFormat(proto.Enum):
        r"""Specifies the format of the route polyline.

        Values:
            ROUTE_POLYLINE_FORMAT_UNSPECIFIED (0):
                The route polyline format is unspecified.
            SIMPLE (1):
                The route polyline is returned as a simple array of points
                represented as ``google.type.LatLng``.
            ENCODED (4):
                The route polyline is returned as an encoded
                string. See
                https://developers.google.com/maps/documentation/utilities/polylinealgorithm.
            S2ENCODED (2):
                The route polyline is encoded as a S2Polyline. See
                https://s2geometry.io/devguide/basic_types.html.
            GEO_JSON (3):
                The route polyline is returned as a GeoJSON
                LineString. See
                https://tools.ietf.org/html/rfc7946#section-3.1.4.
        """

        ROUTE_POLYLINE_FORMAT_UNSPECIFIED = 0
        SIMPLE = 1
        ENCODED = 4
        S2ENCODED = 2
        GEO_JSON = 3

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    route_polyline_format: RoutePolylineFormat = proto.Field(
        proto.ENUM,
        number=2,
        enum=RoutePolylineFormat,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
