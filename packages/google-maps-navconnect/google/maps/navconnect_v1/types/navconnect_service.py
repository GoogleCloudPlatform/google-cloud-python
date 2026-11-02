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
import google.type.latlng_pb2 as latlng_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.maps.navconnect.v1",
    manifest={
        "Trip",
        "TripConfig",
        "AuthToken",
        "TripExecution",
        "Stop",
        "Location",
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
            Optional. Whether to enable high frequency
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
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
