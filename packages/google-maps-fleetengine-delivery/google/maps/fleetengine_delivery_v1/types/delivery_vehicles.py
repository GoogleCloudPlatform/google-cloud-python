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
import google.protobuf.wrappers_pb2 as wrappers_pb2  # type: ignore
import google.type.latlng_pb2 as latlng_pb2  # type: ignore
import proto  # type: ignore

from google.maps.fleetengine_delivery_v1.types import common

__protobuf__ = proto.module(
    package="maps.fleetengine.delivery.v1",
    manifest={
        "DeliveryVehicle",
        "LocationInfo",
        "VehicleJourneySegment",
        "VehicleStop",
    },
)


class DeliveryVehicle(proto.Message):
    r"""The ``DeliveryVehicle`` message. A delivery vehicle transports
    shipments from a depot to a delivery location, and from a pickup
    location to the depot. In some cases, delivery vehicles also
    transport shipments directly from the pickup location to the
    delivery location.

    Note: gRPC and REST APIs use different field naming conventions. For
    example, the ``DeliveryVehicle.current_route_segment`` field in the
    gRPC API and the ``DeliveryVehicle.currentRouteSegment`` field in
    the REST API refer to the same field.

    Attributes:
        name (str):
            The unique name of this Delivery Vehicle. The format is
            ``providers/{provider}/deliveryVehicles/{vehicle}``.
        last_location (google.maps.fleetengine_delivery_v1.types.DeliveryVehicleLocation):
            The last reported location of the Delivery
            Vehicle.
        past_locations (MutableSequence[google.maps.fleetengine_delivery_v1.types.DeliveryVehicleLocation]):
            Input only. Locations where this Delivery Vehicle has been
            in the past that haven't yet been reported to Fleet Engine.
            This is used in ``UpdateDeliveryVehicleRequest`` to record
            locations which were previously unable to be sent to the
            server. Typically this happens when the Delivery Vehicle
            does not have internet connectivity.
        navigation_status (google.maps.fleetengine_delivery_v1.types.DeliveryVehicleNavigationStatus):
            The Delivery Vehicle's navigation status.
        current_route_segment (bytes):
            The encoded polyline specifying the route that the
            navigation recommends taking to the next waypoint. Your
            driver app updates this when a stop is reached or passed,
            and when the navigation reroutes. These ``LatLng``\ s are
            returned in
            ``Task.journey_sharing_info.remaining_vehicle_journey_segments[0].path``
            (gRPC) or
            ``Task.journeySharingInfo.remainingVehicleJourneySegments[0].path``
            (REST) for all active Tasks assigned to the Vehicle.

            There are a few cases where this field might not be used to
            populate
            ``Task.journey_sharing_info.remaining_vehicle_journey_segments[0].path``
            (gRPC) or
            ``Task.journeySharingInfo.remainingVehicleJourneySegments[0].path``
            (REST):

            - The endpoint of the ``current_route_segment`` does not
              match
              ``DeliveryVehicle.remaining_vehicle_journey_segments[0].stop``
              (gRPC) or
              ``DeliveryVehicle.remainingVehicleJourneySegments[0].stop``
              (REST).

            - The driver app has not updated its location recently, so
              the last updated value for this field might be stale.

            - The driver app has recently updated its location, but the
              ``current_route_segment`` is stale, and points to a
              previous vehicle stop.

            In these cases, Fleet Engine populates this field with a
            route from the most recently passed VehicleStop to the
            upcoming VehicleStop to ensure that the consumer of this
            field has the best available information on the current path
            of the Delivery Vehicle.
        current_route_segment_end_point (google.type.latlng_pb2.LatLng):
            The location where the ``current_route_segment`` ends. This
            is not currently populated by the driver app, but you can
            supply it on ``UpdateDeliveryVehicle`` calls. It is either
            the ``LatLng`` from the upcoming vehicle stop, or the last
            ``LatLng`` of the ``current_route_segment``. Fleet Engine
            will then do its best to interpolate to an actual
            ``VehicleStop``.

            This field is ignored in ``UpdateDeliveryVehicle`` calls if
            the ``current_route_segment`` field is empty.
        remaining_distance_meters (google.protobuf.wrappers_pb2.Int32Value):
            The remaining driving distance for the
            ``current_route_segment``. The Driver app typically provides
            this field, but there are some circumstances in which Fleet
            Engine will override the value sent by the app. For more
            information, see
            [DeliveryVehicle.current_route_segment][maps.fleetengine.delivery.v1.DeliveryVehicle.current_route_segment].
            This field is returned in
            ``Task.remaining_vehicle_journey_segments[0].driving_distance_meters``
            (gRPC) or
            ``Task.remainingVehicleJourneySegments[0].drivingDistanceMeters``
            (REST) for all active ``Task``\ s assigned to the Delivery
            Vehicle.

            Fleet Engine ignores this field in
            ``UpdateDeliveryVehicleRequest`` if the
            ``current_route_segment`` field is empty.
        remaining_duration (google.protobuf.duration_pb2.Duration):
            The remaining driving time for the
            ``current_route_segment``. The Driver app typically provides
            this field, but there are some circumstances in which Fleet
            Engine will override the value sent by the app. For more
            information, see
            [DeliveryVehicle.current_route_segment][maps.fleetengine.delivery.v1.DeliveryVehicle.current_route_segment].
            This field is returned in
            ``Task.remaining_vehicle_journey_segments[0].driving_duration``
            (gRPC) or
            ``Task.remainingVehicleJourneySegments[0].drivingDuration``
            (REST) for all active tasks assigned to the Delivery
            Vehicle.

            Fleet Engine ignores this field in
            ``UpdateDeliveryVehicleRequest`` if the
            ``current_route_segment`` field is empty.
        remaining_vehicle_journey_segments (MutableSequence[google.maps.fleetengine_delivery_v1.types.VehicleJourneySegment]):
            The journey segments assigned to this Delivery Vehicle,
            starting from the Vehicle's most recently reported location.
            This field won't be populated in the response of
            ``ListDeliveryVehicles``.
        attributes (MutableSequence[google.maps.fleetengine_delivery_v1.types.DeliveryVehicleAttribute]):
            A list of custom Delivery Vehicle attributes.
            A Delivery Vehicle can have at most 100
            attributes, and each attribute must have a
            unique key.
        type_ (google.maps.fleetengine_delivery_v1.types.DeliveryVehicle.DeliveryVehicleType):
            The type of this delivery vehicle. If unset, this will
            default to ``AUTO``.
    """

    class DeliveryVehicleType(proto.Enum):
        r"""The type of delivery vehicle.

        Values:
            DELIVERY_VEHICLE_TYPE_UNSPECIFIED (0):
                The value is unused.
            AUTO (1):
                An automobile.
            TWO_WHEELER (2):
                A motorcycle, moped, or other two-wheeled
                vehicle
            BICYCLE (3):
                Human-powered transport.
            PEDESTRIAN (4):
                A human transporter, typically walking or
                running, traveling along pedestrian pathways.
        """

        DELIVERY_VEHICLE_TYPE_UNSPECIFIED = 0
        AUTO = 1
        TWO_WHEELER = 2
        BICYCLE = 3
        PEDESTRIAN = 4

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    last_location: common.DeliveryVehicleLocation = proto.Field(
        proto.MESSAGE,
        number=2,
        message=common.DeliveryVehicleLocation,
    )
    past_locations: MutableSequence[common.DeliveryVehicleLocation] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=12,
            message=common.DeliveryVehicleLocation,
        )
    )
    navigation_status: common.DeliveryVehicleNavigationStatus = proto.Field(
        proto.ENUM,
        number=3,
        enum=common.DeliveryVehicleNavigationStatus,
    )
    current_route_segment: bytes = proto.Field(
        proto.BYTES,
        number=4,
    )
    current_route_segment_end_point: latlng_pb2.LatLng = proto.Field(
        proto.MESSAGE,
        number=5,
        message=latlng_pb2.LatLng,
    )
    remaining_distance_meters: wrappers_pb2.Int32Value = proto.Field(
        proto.MESSAGE,
        number=6,
        message=wrappers_pb2.Int32Value,
    )
    remaining_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=7,
        message=duration_pb2.Duration,
    )
    remaining_vehicle_journey_segments: MutableSequence["VehicleJourneySegment"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=8,
            message="VehicleJourneySegment",
        )
    )
    attributes: MutableSequence[common.DeliveryVehicleAttribute] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message=common.DeliveryVehicleAttribute,
    )
    type_: DeliveryVehicleType = proto.Field(
        proto.ENUM,
        number=10,
        enum=DeliveryVehicleType,
    )


class LocationInfo(proto.Message):
    r"""A location with any additional identifiers.

    Attributes:
        point (google.type.latlng_pb2.LatLng):
            The location's coordinates.
    """

    point: latlng_pb2.LatLng = proto.Field(
        proto.MESSAGE,
        number=1,
        message=latlng_pb2.LatLng,
    )


class VehicleJourneySegment(proto.Message):
    r"""Represents a Vehicle’s travel segment - from its previous
    stop to the current stop. If it is the first active stop, then
    it is from the Vehicle’s current location to this stop.

    Attributes:
        stop (google.maps.fleetengine_delivery_v1.types.VehicleStop):
            Specifies the stop location, along with the ``Task``\ s
            associated with the stop. Some fields of the VehicleStop
            might not be present if this journey segment is part of
            ``JourneySharingInfo``.
        driving_distance_meters (google.protobuf.wrappers_pb2.Int32Value):
            Output only. The travel distance from the previous stop to
            this stop. If the current stop is the first stop in the list
            of journey segments, then the starting point is the
            vehicle's location recorded at the time that this stop was
            added to the list. This field might not be present if this
            journey segment is part of ``JourneySharingInfo``.
        driving_duration (google.protobuf.duration_pb2.Duration):
            Output only. The travel time from the previous stop to this
            stop. If the current stop is the first stop in the list of
            journey segments, then the starting point is the Vehicle's
            location recorded at the time that this stop was added to
            the list.

            If this field is defined in the path
            ``Task.remaining_vehicle_journey_segments[0].driving_duration``
            (gRPC) or
            ``Task.remainingVehicleJourneySegments[0].drivingDuration``
            (REST), then it may be populated with the value from
            ``DeliveryVehicle.remaining_duration`` (gRPC) or
            ``DeliveryVehicle.remainingDuration`` (REST). This provides
            the remaining driving duration from the driver app's latest
            known location rather than the driving time from the
            previous stop.
        path (MutableSequence[google.type.latlng_pb2.LatLng]):
            Output only. The path from the previous stop to this stop.
            If the current stop is the first stop in the list of journey
            segments, then this is the path from the vehicle's current
            location to this stop at the time that the stop was added to
            the list. This field might not be present if this journey
            segment is part of ``JourneySharingInfo``.

            If this field is defined in the path
            ``Task.journey_sharing_info.remaining_vehicle_journey_segments[0].path``
            (gRPC) or
            ``Task.journeySharingInfo.remainingVehicleJourneySegments[0].path``
            (REST), then it may be populated with the ``LatLng``\ s
            decoded from ``DeliveryVehicle.current_route_segment``
            (gRPC) or ``DeliveryVehicle.currentRouteSegment`` (REST).
            This provides the driving path from the driver app's latest
            known location rather than the path from the previous stop.
    """

    stop: "VehicleStop" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="VehicleStop",
    )
    driving_distance_meters: wrappers_pb2.Int32Value = proto.Field(
        proto.MESSAGE,
        number=2,
        message=wrappers_pb2.Int32Value,
    )
    driving_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=3,
        message=duration_pb2.Duration,
    )
    path: MutableSequence[latlng_pb2.LatLng] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message=latlng_pb2.LatLng,
    )


class VehicleStop(proto.Message):
    r"""Describes a point where a Vehicle stops to perform one or more
    ``Task``\ s.

    Attributes:
        planned_location (google.maps.fleetengine_delivery_v1.types.LocationInfo):
            Required. The location of the stop. Note that the locations
            in the ``Task``\ s might not exactly match this location,
            but will be within a short distance of it. This field won't
            be populated in the response of a ``GetTask`` call.
        tasks (MutableSequence[google.maps.fleetengine_delivery_v1.types.VehicleStop.TaskInfo]):
            The list of ``Task``\ s to be performed at this stop. This
            field won't be populated in the response of a ``GetTask``
            call.
        state (google.maps.fleetengine_delivery_v1.types.VehicleStop.State):
            The state of the ``VehicleStop``. This field won't be
            populated in the response of a ``GetTask`` call.
    """

    class State(proto.Enum):
        r"""The current state of a ``VehicleStop``.

        Values:
            STATE_UNSPECIFIED (0):
                Unknown.
            NEW (1):
                Created, but not actively routing.
            ENROUTE (2):
                Assigned and actively routing.
            ARRIVED (3):
                Arrived at stop. Assumes that when the
                Vehicle is routing to the next stop, that all
                previous stops have been completed.
        """

        STATE_UNSPECIFIED = 0
        NEW = 1
        ENROUTE = 2
        ARRIVED = 3

    class TaskInfo(proto.Message):
        r"""Additional information about the Task performed at this stop.

        Attributes:
            task_id (str):
                The Task ID. This field won't be populated in the response
                of a ``GetTask`` call. Task IDs are subject to the following
                restrictions:

                - Must be a valid Unicode string.
                - Limited to a maximum length of 64 characters.
                - Normalized according to [Unicode Normalization Form C]
                  (http://www.unicode.org/reports/tr15/).
                - May not contain any of the following ASCII characters:
                  '/', ':', '?', ',', or '#'.
            task_duration (google.protobuf.duration_pb2.Duration):
                Output only. The time required to perform the
                Task.
            target_time_window (google.maps.fleetengine_delivery_v1.types.TimeWindow):
                Output only. The time window during which the task should be
                completed. This is only set in the response to
                ``GetDeliveryVehicle``.
        """

        task_id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        task_duration: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=2,
            message=duration_pb2.Duration,
        )
        target_time_window: common.TimeWindow = proto.Field(
            proto.MESSAGE,
            number=3,
            message=common.TimeWindow,
        )

    planned_location: "LocationInfo" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="LocationInfo",
    )
    tasks: MutableSequence[TaskInfo] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=TaskInfo,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=3,
        enum=State,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
