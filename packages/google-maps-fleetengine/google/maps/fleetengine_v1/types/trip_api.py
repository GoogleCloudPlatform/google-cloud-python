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

from google.maps.fleetengine_v1.types import fleetengine
from google.maps.fleetengine_v1.types import header as mf_header
from google.maps.fleetengine_v1.types import trips as mf_trips

__protobuf__ = proto.module(
    package="maps.fleetengine.v1",
    manifest={
        "CreateTripRequest",
        "GetTripRequest",
        "DeleteTripRequest",
        "ReportBillableTripRequest",
        "UpdateTripRequest",
        "SearchTripsRequest",
        "SearchTripsResponse",
    },
)


class CreateTripRequest(proto.Message):
    r"""CreateTrip request message.

    Attributes:
        header (google.maps.fleetengine_v1.types.RequestHeader):
            The standard Fleet Engine request header.
        parent (str):
            Required. Must be in the format ``providers/{provider}``.
            The provider must be the Project ID (for example,
            ``sample-cloud-project``) of the Google Cloud Project of
            which the service account making this call is a member.
        trip_id (str):
            Required. Unique Trip ID. Subject to the following
            restrictions:

            - Must be a valid Unicode string.
            - Limited to a maximum length of 64 characters.
            - Normalized according to [Unicode Normalization Form C]
              (http://www.unicode.org/reports/tr15/).
            - May not contain any of the following ASCII characters:
              '/', ':', '?', ',', or '#'.
        trip (google.maps.fleetengine_v1.types.Trip):
            Required. Trip entity to create.

            When creating a Trip, the following fields are required:

            - ``trip_type``
            - ``pickup_point``

            The following fields are used if you provide them:

            - ``number_of_passengers``
            - ``vehicle_id``
            - ``dropoff_point``
            - ``intermediate_destinations``
            - ``vehicle_waypoints``

            All other Trip fields are ignored. For example, all trips
            start with a ``trip_status`` of ``NEW`` even if you pass in
            a ``trip_status`` of ``CANCELED`` in the creation request.

            Only ``EXCLUSIVE`` trips support
            ``intermediate_destinations``.

            When ``vehicle_id`` is set for a shared trip, you must
            supply the list of ``Trip.vehicle_waypoints`` to specify the
            order of the remaining waypoints for the vehicle, otherwise
            the waypoint order will be undetermined.

            When you specify ``Trip.vehicle_waypoints``, the list must
            contain all the remaining waypoints of the vehicle's trips,
            with no extra waypoints. You must order these waypoints such
            that for a given trip, the pickup point is before
            intermediate destinations, and all intermediate destinations
            come before the drop-off point. An ``EXCLUSIVE`` trip's
            waypoints must not interleave with any other trips.

            The ``trip_id``, ``waypoint_type`` and ``location`` fields
            are used, and all other TripWaypoint fields in
            ``vehicle_waypoints`` are ignored.
    """

    header: mf_header.RequestHeader = proto.Field(
        proto.MESSAGE,
        number=1,
        message=mf_header.RequestHeader,
    )
    parent: str = proto.Field(
        proto.STRING,
        number=3,
    )
    trip_id: str = proto.Field(
        proto.STRING,
        number=5,
    )
    trip: mf_trips.Trip = proto.Field(
        proto.MESSAGE,
        number=4,
        message=mf_trips.Trip,
    )


class GetTripRequest(proto.Message):
    r"""GetTrip request message.

    Attributes:
        header (google.maps.fleetengine_v1.types.RequestHeader):
            The standard Fleet Engine request header.
        name (str):
            Required. Must be in the format
            ``providers/{provider}/trips/{trip}``. The provider must be
            the Project ID (for example, ``sample-cloud-project``) of
            the Google Cloud Project of which the service account making
            this call is a member.
        view (google.maps.fleetengine_v1.types.TripView):
            The subset of Trip fields that should be
            returned and their interpretation.
        current_route_segment_version (google.protobuf.timestamp_pb2.Timestamp):
            Indicates the minimum timestamp (exclusive) for which
            ``Trip.route`` or ``Trip.current_route_segment`` data are
            retrieved. If route data are unchanged since this timestamp,
            the route field is not set in the response. If a minimum is
            unspecified, the route data are always retrieved.
        remaining_waypoints_version (google.protobuf.timestamp_pb2.Timestamp):
            Deprecated: ``Trip.remaining_waypoints`` are always
            retrieved. Use ``remaining_waypoints_route_version`` to
            control when
            ``Trip.remaining_waypoints.traffic_to_waypoint`` and
            ``Trip.remaining_waypoints.path_to_waypoint`` data are
            retrieved.
        route_format_type (google.maps.fleetengine_v1.types.PolylineFormatType):
            The returned current route format, ``LAT_LNG_LIST_TYPE`` (in
            ``Trip.route``), or ``ENCODED_POLYLINE_TYPE`` (in
            ``Trip.current_route_segment``). The default is
            ``LAT_LNG_LIST_TYPE``.
        current_route_segment_traffic_version (google.protobuf.timestamp_pb2.Timestamp):
            Indicates the minimum timestamp (exclusive) for which
            ``Trip.current_route_segment_traffic`` is retrieved. If
            traffic data are unchanged since this timestamp, the
            ``current_route_segment_traffic`` field is not set in the
            response. If a minimum is unspecified, the traffic data are
            always retrieved. Note that traffic is only available for
            On-Demand Rides and Deliveries Solution customers.
        remaining_waypoints_route_version (google.protobuf.timestamp_pb2.Timestamp):
            Indicates the minimum timestamp (exclusive) for which
            ``Trip.remaining_waypoints.traffic_to_waypoint`` and
            ``Trip.remaining_waypoints.path_to_waypoint`` data are
            retrieved. If data are unchanged since this timestamp, the
            fields above are not set in the response. If
            ``remaining_waypoints_route_version`` is unspecified,
            traffic and path are always retrieved.
    """

    header: mf_header.RequestHeader = proto.Field(
        proto.MESSAGE,
        number=1,
        message=mf_header.RequestHeader,
    )
    name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    view: mf_trips.TripView = proto.Field(
        proto.ENUM,
        number=11,
        enum=mf_trips.TripView,
    )
    current_route_segment_version: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    remaining_waypoints_version: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    route_format_type: fleetengine.PolylineFormatType = proto.Field(
        proto.ENUM,
        number=8,
        enum=fleetengine.PolylineFormatType,
    )
    current_route_segment_traffic_version: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    remaining_waypoints_route_version: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )


class DeleteTripRequest(proto.Message):
    r"""DeleteTrip request message.

    Attributes:
        header (google.maps.fleetengine_v1.types.RequestHeader):
            Optional. The standard Fleet Engine request
            header.
        name (str):
            Required. Must be in the format
            ``providers/{provider}/trips/{trip}``. The provider must be
            the Project ID (for example, ``sample-cloud-project``) of
            the Google Cloud Project of which the service account making
            this call is a member.
    """

    header: mf_header.RequestHeader = proto.Field(
        proto.MESSAGE,
        number=1,
        message=mf_header.RequestHeader,
    )
    name: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ReportBillableTripRequest(proto.Message):
    r"""ReportBillableTrip request message.

    Attributes:
        name (str):
            Required. Must be in the format
            ``providers/{provider}/billableTrips/{billable_trip}``. The
            provider must be the Project ID (for example,
            ``sample-cloud-project``) of the Google Cloud Project of
            which the service account making this call is a member.
        country_code (str):
            Required. Two letter country code of the
            country where the trip takes place. Price is
            defined according to country code.
        platform (google.maps.fleetengine_v1.types.BillingPlatformIdentifier):
            The platform upon which the request was
            issued.
        related_ids (MutableSequence[str]):
            The identifiers that are directly related to the trip being
            reported. These are usually IDs (for example, session IDs)
            of pre-booking operations done before the trip ID is
            available. The number of ``related_ids`` is limited to 50.
        solution_type (google.maps.fleetengine_v1.types.ReportBillableTripRequest.SolutionType):
            The type of GMP product solution (for example,
            ``ON_DEMAND_RIDESHARING_AND_DELIVERIES``) used for the
            reported trip.
    """

    class SolutionType(proto.Enum):
        r"""Selector for different solution types of a reported trip.

        Values:
            SOLUTION_TYPE_UNSPECIFIED (0):
                The default value. For backwards-compatibility, the API will
                use ``ON_DEMAND_RIDESHARING_AND_DELIVERIES`` by default
                which is the first supported solution type.
            ON_DEMAND_RIDESHARING_AND_DELIVERIES (1):
                The solution is an on-demand ridesharing and
                deliveries trip.
        """

        SOLUTION_TYPE_UNSPECIFIED = 0
        ON_DEMAND_RIDESHARING_AND_DELIVERIES = 1

    name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    country_code: str = proto.Field(
        proto.STRING,
        number=3,
    )
    platform: mf_trips.BillingPlatformIdentifier = proto.Field(
        proto.ENUM,
        number=5,
        enum=mf_trips.BillingPlatformIdentifier,
    )
    related_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    solution_type: SolutionType = proto.Field(
        proto.ENUM,
        number=7,
        enum=SolutionType,
    )


class UpdateTripRequest(proto.Message):
    r"""UpdateTrip request message.

    Attributes:
        header (google.maps.fleetengine_v1.types.RequestHeader):
            The standard Fleet Engine request header.
        name (str):
            Required. Must be in the format
            ``providers/{provider}/trips/{trip}``. The provider must be
            the Project ID (for example, ``sample-consumer-project``) of
            the Google Cloud Project of which the service account making
            this call is a member.
        trip (google.maps.fleetengine_v1.types.Trip):
            Required. The Trip associated with the update.

            The following fields are maintained by the Fleet Engine. Do
            not update them using Trip.update.

            - ``current_route_segment``
            - ``current_route_segment_end_point``
            - ``current_route_segment_traffic``
            - ``current_route_segment_traffic_version``
            - ``current_route_segment_version``
            - ``dropoff_time``
            - ``eta_to_next_waypoint``
            - ``intermediate_destinations_version``
            - ``last_location``
            - ``name``
            - ``number_of_passengers``
            - ``pickup_time``
            - ``remaining_distance_meters``
            - ``remaining_time_to_first_waypoint``
            - ``remaining_waypoints``
            - ``remaining_waypoints_version``
            - ``route``

            When you update the ``Trip.vehicle_id`` for a shared trip,
            you must supply the list of ``Trip.vehicle_waypoints`` to
            specify the order of the remaining waypoints, otherwise the
            order will be undetermined.

            When you specify ``Trip.vehicle_waypoints``, the list must
            contain all the remaining waypoints of the vehicle's trips,
            with no extra waypoints. You must order these waypoints such
            that for a given trip, the pickup point is before
            intermediate destinations, and all intermediate destinations
            come before the drop-off point. An ``EXCLUSIVE`` trip's
            waypoints must not interleave with any other trips. The
            ``trip_id``, ``waypoint_type`` and ``location`` fields are
            used, and all other TripWaypoint fields in
            ``vehicle_waypoints`` are ignored.

            To avoid a race condition for trips with multiple
            destinations, you should provide
            ``Trip.intermediate_destinations_version`` when updating the
            trip status to ``ENROUTE_TO_INTERMEDIATE_DESTINATION``. The
            ``Trip.intermediate_destinations_version`` passed must be
            consistent with Fleet Engine's version. If it isn't, the
            request fails.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The field mask indicating which fields in Trip to
            update. The ``update_mask`` must contain at least one field.
    """

    header: mf_header.RequestHeader = proto.Field(
        proto.MESSAGE,
        number=1,
        message=mf_header.RequestHeader,
    )
    name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    trip: mf_trips.Trip = proto.Field(
        proto.MESSAGE,
        number=4,
        message=mf_trips.Trip,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=5,
        message=field_mask_pb2.FieldMask,
    )


class SearchTripsRequest(proto.Message):
    r"""SearchTrips request message.

    Attributes:
        header (google.maps.fleetengine_v1.types.RequestHeader):
            The standard Fleet Engine request header.
        parent (str):
            Required. Must be in the format ``providers/{provider}``.
            The provider must be the Project ID (for example,
            ``sample-cloud-project``) of the Google Cloud Project of
            which the service account making this call is a member.
        vehicle_id (str):
            The vehicle associated with the trips in the request. If
            unspecified, the returned trips do not contain:

            - ``current_route_segment``
            - ``remaining_waypoints``
            - ``remaining_distance_meters``
            - ``eta_to_first_waypoint``
        active_trips_only (bool):
            If set to true, the response includes Trips
            that influence a driver's route.
        page_size (int):
            If not set, the server decides the number of
            results to return.
        page_token (str):
            Set this to a value previously returned in the
            ``SearchTripsResponse`` to continue from previous results.
        minimum_staleness (google.protobuf.duration_pb2.Duration):
            If specified, returns the trips that have not been updated
            after the time ``(current - minimum_staleness)``.
    """

    header: mf_header.RequestHeader = proto.Field(
        proto.MESSAGE,
        number=1,
        message=mf_header.RequestHeader,
    )
    parent: str = proto.Field(
        proto.STRING,
        number=3,
    )
    vehicle_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    active_trips_only: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=6,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=7,
    )
    minimum_staleness: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=8,
        message=duration_pb2.Duration,
    )


class SearchTripsResponse(proto.Message):
    r"""SearchTrips response message.

    Attributes:
        trips (MutableSequence[google.maps.fleetengine_v1.types.Trip]):
            The list of trips for the requested vehicle.
        next_page_token (str):
            Pass this token in the SearchTripsRequest to
            page through list results. The API returns a
            trip list on each call, and when no more results
            remain the trip list is empty.
    """

    @property
    def raw_page(self):
        return self

    trips: MutableSequence[mf_trips.Trip] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=mf_trips.Trip,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
