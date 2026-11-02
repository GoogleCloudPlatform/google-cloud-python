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
import proto  # type: ignore

from google.maps.fleetengine_delivery_v1.types import common, delivery_vehicles

__protobuf__ = proto.module(
    package="maps.fleetengine.delivery.v1",
    manifest={
        "Task",
        "TaskTrackingViewConfig",
    },
)


class Task(proto.Message):
    r"""A Task in the Delivery API represents a single action to track. In
    general, there is a distinction between shipment-related Tasks and
    break Tasks. A shipment can have multiple Tasks associated with it.
    For example, there could be one Task for the pickup, and one for the
    drop-off or transfer. Also, different Tasks for a given shipment can
    be handled by different vehicles. For example, one vehicle could
    handle the pickup, driving the shipment to the hub, while another
    vehicle drives the same shipment from the hub to the drop-off
    location.

    Note: gRPC and REST APIs use different field naming conventions. For
    example, the ``Task.journey_sharing_info`` field in the gRPC API and
    the ``Task.journeySharingInfo`` field in the REST API refer to the
    same field.

    Attributes:
        name (str):
            Must be in the format ``providers/{provider}/tasks/{task}``.
        type_ (google.maps.fleetengine_delivery_v1.types.Task.Type):
            Required. Immutable. Defines the type of the
            Task. For example, a break or shipment.
        state (google.maps.fleetengine_delivery_v1.types.Task.State):
            Required. The current execution state of the
            Task.
        task_outcome (google.maps.fleetengine_delivery_v1.types.Task.TaskOutcome):
            The outcome of the Task.
        task_outcome_time (google.protobuf.timestamp_pb2.Timestamp):
            The timestamp that indicates when the ``Task``'s outcome was
            set by the provider.
        task_outcome_location (google.maps.fleetengine_delivery_v1.types.LocationInfo):
            The location where the ``Task``'s outcome was set. This
            value is updated as part of ``UpdateTask``. If this value
            isn't explicitly updated by the provider, then Fleet Engine
            populates it by default with the last known vehicle location
            (the *raw* location).
        task_outcome_location_source (google.maps.fleetengine_delivery_v1.types.Task.TaskOutcomeLocationSource):
            Indicates where the value of the ``task_outcome_location``
            came from.
        tracking_id (str):
            Immutable. This field facilitates the storing of an ID so
            you can avoid using a complicated mapping. You cannot set
            ``tracking_id`` for Tasks of type ``UNAVAILABLE`` and
            ``SCHEDULED_STOP``. These IDs are subject to the following
            restrictions:

            - Must be a valid Unicode string.
            - Limited to a maximum length of 64 characters.
            - Normalized according to [Unicode Normalization Form C]
              (http://www.unicode.org/reports/tr15/).
            - May not contain any of the following ASCII characters:
              '/', ':', '?', ',', or '#'.
        delivery_vehicle_id (str):
            Output only. The ID of the vehicle that is executing this
            Task. Delivery Vehicle IDs are subject to the following
            restrictions:

            - Must be a valid Unicode string.
            - Limited to a maximum length of 64 characters.
            - Normalized according to [Unicode Normalization Form C]
              (http://www.unicode.org/reports/tr15/).
            - May not contain any of the following ASCII characters:
              '/', ':', '?', ',', or '#'.
        planned_location (google.maps.fleetengine_delivery_v1.types.LocationInfo):
            Immutable. The location where the Task will be completed.
            Optional for ``UNAVAILABLE`` Tasks, but required for all
            other Tasks.
        task_duration (google.protobuf.duration_pb2.Duration):
            Required. Immutable. The time needed to
            execute a Task at this location.
        target_time_window (google.maps.fleetengine_delivery_v1.types.TimeWindow):
            The time window during which the task should
            be completed.
        journey_sharing_info (google.maps.fleetengine_delivery_v1.types.Task.JourneySharingInfo):
            Output only. Journey sharing-specific fields. Not populated
            when state is ``CLOSED``.
        task_tracking_view_config (google.maps.fleetengine_delivery_v1.types.TaskTrackingViewConfig):
            The configuration for task tracking that
            specifies which data elements are visible to the
            end users under what circumstances.
        attributes (MutableSequence[google.maps.fleetengine_delivery_v1.types.TaskAttribute]):
            A list of custom Task attributes. Each
            attribute must have a unique key.
    """

    class Type(proto.Enum):
        r"""The type of Task.

        Values:
            TYPE_UNSPECIFIED (0):
                Default, the Task type is unknown.
            PICKUP (1):
                A pickup Task is the action taken for picking up a shipment
                from a customer. Depot or feeder vehicle pickups should use
                the ``SCHEDULED_STOP`` type.
            DELIVERY (2):
                A delivery Task is the action taken for delivering a
                shipment to an end customer. Depot or feeder vehicle
                dropoffs should use the ``SCHEDULED_STOP`` type.
            SCHEDULED_STOP (3):
                A scheduled stop Task is used for planning
                purposes. For example, it could represent
                picking up or dropping off shipments from feeder
                vehicles or depots. It shouldn't be used for any
                shipments that are picked up or dropped off from
                an end customer.
            UNAVAILABLE (4):
                A Task that means the Vehicle is not
                available for service. For example, this can
                happen when the driver takes a break, or when
                the vehicle is being refueled.
        """

        TYPE_UNSPECIFIED = 0
        PICKUP = 1
        DELIVERY = 2
        SCHEDULED_STOP = 3
        UNAVAILABLE = 4

    class State(proto.Enum):
        r"""The state of a Task. This indicates the Tasks's progress.

        Values:
            STATE_UNSPECIFIED (0):
                Default. Used for an unspecified or
                unrecognized Task state.
            OPEN (1):
                Either the Task has not yet been assigned to a delivery
                vehicle, or the delivery vehicle has not yet passed the
                ``Task``'s assigned vehicle stop.
            CLOSED (2):
                When the vehicle passes the vehicle stop for
                this Task.
        """

        STATE_UNSPECIFIED = 0
        OPEN = 1
        CLOSED = 2

    class TaskOutcome(proto.Enum):
        r"""The outcome of attempting to execute a Task. When ``TaskState`` is
        closed, ``TaskOutcome`` indicates whether it was completed
        successfully.

        Values:
            TASK_OUTCOME_UNSPECIFIED (0):
                The Task outcome before its value is set.
            SUCCEEDED (1):
                The Task completed successfully.
            FAILED (2):
                Either the Task couldn't be completed, or it
                was cancelled.
        """

        TASK_OUTCOME_UNSPECIFIED = 0
        SUCCEEDED = 1
        FAILED = 2

    class TaskOutcomeLocationSource(proto.Enum):
        r"""The identity of the source that populated the
        ``task_outcome_location``.

        Values:
            TASK_OUTCOME_LOCATION_SOURCE_UNSPECIFIED (0):
                The task outcome before it is set.
            PROVIDER (2):
                The provider-specified the ``task_outcome_location``.
            LAST_VEHICLE_LOCATION (3):
                The provider didn't specify the ``task_outcome_location``,
                so Fleet Engine used the last known vehicle location.
        """

        TASK_OUTCOME_LOCATION_SOURCE_UNSPECIFIED = 0
        PROVIDER = 2
        LAST_VEHICLE_LOCATION = 3

    class JourneySharingInfo(proto.Message):
        r"""Journey sharing specific fields.

        Attributes:
            remaining_vehicle_journey_segments (MutableSequence[google.maps.fleetengine_delivery_v1.types.VehicleJourneySegment]):
                Tracking information for the stops that the assigned vehicle
                will make before it completes this Task. Note that this list
                can contain stops from other tasks.

                The first segment,
                ``Task.journey_sharing_info.remaining_vehicle_journey_segments[0]``
                (gRPC) or
                ``Task.journeySharingInfo.remainingVehicleJourneySegments[0]``
                (REST), contains route information from the driver's last
                known location to the upcoming ``VehicleStop``. Current
                route information usually comes from the driver app, except
                for some cases noted in the documentation for
                [DeliveryVehicle.current_route_segment][maps.fleetengine.delivery.v1.DeliveryVehicle.current_route_segment].
                The other segments in
                ``Task.journey_sharing_info.remaining_vehicle_journey_segments``
                (gRPC) or
                ``Task.journeySharingInfo.remainingVehicleJourneySegments``
                (REST) are populated by Fleet Engine. They provide route
                information between the remaining ``VehicleStops``.
            last_location (google.maps.fleetengine_delivery_v1.types.DeliveryVehicleLocation):
                Indicates the vehicle's last reported
                location of the assigned vehicle.
            last_location_snappable (bool):
                Indicates whether the vehicle's lastLocation can be snapped
                to the ``current_route_segment``. This value is False if
                either ``last_location`` or ``current_route_segment`` don't
                exist. This value is computed by Fleet Engine. Updates from
                clients are ignored.
        """

        remaining_vehicle_journey_segments: MutableSequence[
            delivery_vehicles.VehicleJourneySegment
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=delivery_vehicles.VehicleJourneySegment,
        )
        last_location: common.DeliveryVehicleLocation = proto.Field(
            proto.MESSAGE,
            number=2,
            message=common.DeliveryVehicleLocation,
        )
        last_location_snappable: bool = proto.Field(
            proto.BOOL,
            number=3,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_: Type = proto.Field(
        proto.ENUM,
        number=2,
        enum=Type,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=3,
        enum=State,
    )
    task_outcome: TaskOutcome = proto.Field(
        proto.ENUM,
        number=9,
        enum=TaskOutcome,
    )
    task_outcome_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )
    task_outcome_location: delivery_vehicles.LocationInfo = proto.Field(
        proto.MESSAGE,
        number=11,
        message=delivery_vehicles.LocationInfo,
    )
    task_outcome_location_source: TaskOutcomeLocationSource = proto.Field(
        proto.ENUM,
        number=12,
        enum=TaskOutcomeLocationSource,
    )
    tracking_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    delivery_vehicle_id: str = proto.Field(
        proto.STRING,
        number=5,
    )
    planned_location: delivery_vehicles.LocationInfo = proto.Field(
        proto.MESSAGE,
        number=6,
        message=delivery_vehicles.LocationInfo,
    )
    task_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=7,
        message=duration_pb2.Duration,
    )
    target_time_window: common.TimeWindow = proto.Field(
        proto.MESSAGE,
        number=14,
        message=common.TimeWindow,
    )
    journey_sharing_info: JourneySharingInfo = proto.Field(
        proto.MESSAGE,
        number=8,
        message=JourneySharingInfo,
    )
    task_tracking_view_config: "TaskTrackingViewConfig" = proto.Field(
        proto.MESSAGE,
        number=13,
        message="TaskTrackingViewConfig",
    )
    attributes: MutableSequence[common.TaskAttribute] = proto.RepeatedField(
        proto.MESSAGE,
        number=15,
        message=common.TaskAttribute,
    )


class TaskTrackingViewConfig(proto.Message):
    r"""The configuration message that defines when a data element of
    a Task should be visible to the end users.

    Attributes:
        route_polyline_points_visibility (google.maps.fleetengine_delivery_v1.types.TaskTrackingViewConfig.VisibilityOption):
            The field that specifies when route polyline
            points can be visible. If this field is not
            specified, the project level default visibility
            configuration for this data will be used.
        estimated_arrival_time_visibility (google.maps.fleetengine_delivery_v1.types.TaskTrackingViewConfig.VisibilityOption):
            The field that specifies when estimated
            arrival time can be visible. If this field is
            not specified, the project level default
            visibility configuration for this data will be
            used.
        estimated_task_completion_time_visibility (google.maps.fleetengine_delivery_v1.types.TaskTrackingViewConfig.VisibilityOption):
            The field that specifies when estimated task
            completion time can be visible. If this field is
            not specified, the project level default
            visibility configuration for this data will be
            used.
        remaining_driving_distance_visibility (google.maps.fleetengine_delivery_v1.types.TaskTrackingViewConfig.VisibilityOption):
            The field that specifies when remaining
            driving distance can be visible. If this field
            is not specified, the project level default
            visibility configuration for this data will be
            used.
        remaining_stop_count_visibility (google.maps.fleetengine_delivery_v1.types.TaskTrackingViewConfig.VisibilityOption):
            The field that specifies when remaining stop
            count can be visible. If this field is not
            specified, the project level default visibility
            configuration for this data will be used.
        vehicle_location_visibility (google.maps.fleetengine_delivery_v1.types.TaskTrackingViewConfig.VisibilityOption):
            The field that specifies when vehicle
            location can be visible. If this field is not
            specified, the project level default visibility
            configuration for this data will be used.
    """

    class VisibilityOption(proto.Message):
        r"""The option message that defines when a data element should be
        visible to the end users.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            remaining_stop_count_threshold (int):
                This data element is visible to the end users if the
                remaining stop count <= remaining_stop_count_threshold.

                This field is a member of `oneof`_ ``visibility_option``.
            duration_until_estimated_arrival_time_threshold (google.protobuf.duration_pb2.Duration):
                This data element is visible to the end users if the ETA to
                the stop <= duration_until_estimated_arrival_time_threshold.

                This field is a member of `oneof`_ ``visibility_option``.
            remaining_driving_distance_meters_threshold (int):
                This data element is visible to the end users if the
                remaining driving distance in meters <=
                remaining_driving_distance_meters_threshold.

                This field is a member of `oneof`_ ``visibility_option``.
            always (bool):
                If set to true, this data element is always
                visible to the end users with no thresholds.
                This field cannot be set to false.

                This field is a member of `oneof`_ ``visibility_option``.
            never (bool):
                If set to true, this data element is always
                hidden from the end users with no thresholds.
                This field cannot be set to false.

                This field is a member of `oneof`_ ``visibility_option``.
        """

        remaining_stop_count_threshold: int = proto.Field(
            proto.INT32,
            number=1,
            oneof="visibility_option",
        )
        duration_until_estimated_arrival_time_threshold: duration_pb2.Duration = (
            proto.Field(
                proto.MESSAGE,
                number=2,
                oneof="visibility_option",
                message=duration_pb2.Duration,
            )
        )
        remaining_driving_distance_meters_threshold: int = proto.Field(
            proto.INT32,
            number=3,
            oneof="visibility_option",
        )
        always: bool = proto.Field(
            proto.BOOL,
            number=4,
            oneof="visibility_option",
        )
        never: bool = proto.Field(
            proto.BOOL,
            number=5,
            oneof="visibility_option",
        )

    route_polyline_points_visibility: VisibilityOption = proto.Field(
        proto.MESSAGE,
        number=1,
        message=VisibilityOption,
    )
    estimated_arrival_time_visibility: VisibilityOption = proto.Field(
        proto.MESSAGE,
        number=2,
        message=VisibilityOption,
    )
    estimated_task_completion_time_visibility: VisibilityOption = proto.Field(
        proto.MESSAGE,
        number=3,
        message=VisibilityOption,
    )
    remaining_driving_distance_visibility: VisibilityOption = proto.Field(
        proto.MESSAGE,
        number=4,
        message=VisibilityOption,
    )
    remaining_stop_count_visibility: VisibilityOption = proto.Field(
        proto.MESSAGE,
        number=5,
        message=VisibilityOption,
    )
    vehicle_location_visibility: VisibilityOption = proto.Field(
        proto.MESSAGE,
        number=6,
        message=VisibilityOption,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
