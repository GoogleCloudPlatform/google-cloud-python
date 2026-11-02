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

import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.protobuf.wrappers_pb2 as wrappers_pb2  # type: ignore
import google.type.latlng_pb2 as latlng_pb2  # type: ignore
import proto  # type: ignore

from google.maps.fleetengine_delivery_v1.types import common, delivery_vehicles, tasks

__protobuf__ = proto.module(
    package="maps.fleetengine.delivery.v1",
    manifest={
        "TaskTrackingInfo",
    },
)


class TaskTrackingInfo(proto.Message):
    r"""The ``TaskTrackingInfo`` message. The message contains task tracking
    information which will be used for display. If a tracking ID is
    associated with multiple Tasks, Fleet Engine uses a heuristic to
    decide which Task's TaskTrackingInfo to select.

    Attributes:
        name (str):
            Must be in the format
            ``providers/{provider}/taskTrackingInfo/{tracking}``, where
            ``tracking`` represents the tracking ID.
        tracking_id (str):
            Immutable. The tracking ID of a Task.

            - Must be a valid Unicode string.
            - Limited to a maximum length of 64 characters.
            - Normalized according to [Unicode Normalization Form C]
              (http://www.unicode.org/reports/tr15/).
            - May not contain any of the following ASCII characters:
              '/', ':', '?', ',', or '#'.
        vehicle_location (google.maps.fleetengine_delivery_v1.types.DeliveryVehicleLocation):
            The vehicle's last location.
        route_polyline_points (MutableSequence[google.type.latlng_pb2.LatLng]):
            A list of points which when connected forms a
            polyline of the vehicle's expected route to the
            location of this task.
        remaining_stop_count (google.protobuf.wrappers_pb2.Int32Value):
            Indicates the number of stops the vehicle
            remaining until the task stop is reached,
            including the task stop. For example, if the
            vehicle's next stop is the task stop, the value
            will be 1.
        remaining_driving_distance_meters (google.protobuf.wrappers_pb2.Int32Value):
            The total remaining distance in meters to the
            ``VehicleStop`` of interest.
        estimated_arrival_time (google.protobuf.timestamp_pb2.Timestamp):
            The timestamp that indicates the estimated
            arrival time to the stop location.
        estimated_task_completion_time (google.protobuf.timestamp_pb2.Timestamp):
            The timestamp that indicates the estimated
            completion time of a Task.
        state (google.maps.fleetengine_delivery_v1.types.Task.State):
            The current execution state of the Task.
        task_outcome (google.maps.fleetengine_delivery_v1.types.Task.TaskOutcome):
            The outcome of attempting to execute a Task.
        task_outcome_time (google.protobuf.timestamp_pb2.Timestamp):
            The timestamp that indicates when the Task's
            outcome was set by the provider.
        planned_location (google.maps.fleetengine_delivery_v1.types.LocationInfo):
            Immutable. The location where the Task will
            be completed.
        target_time_window (google.maps.fleetengine_delivery_v1.types.TimeWindow):
            The time window during which the task should
            be completed.
        attributes (MutableSequence[google.maps.fleetengine_delivery_v1.types.TaskAttribute]):
            The custom attributes set on the task.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    tracking_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    vehicle_location: common.DeliveryVehicleLocation = proto.Field(
        proto.MESSAGE,
        number=3,
        message=common.DeliveryVehicleLocation,
    )
    route_polyline_points: MutableSequence[latlng_pb2.LatLng] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=latlng_pb2.LatLng,
    )
    remaining_stop_count: wrappers_pb2.Int32Value = proto.Field(
        proto.MESSAGE,
        number=5,
        message=wrappers_pb2.Int32Value,
    )
    remaining_driving_distance_meters: wrappers_pb2.Int32Value = proto.Field(
        proto.MESSAGE,
        number=6,
        message=wrappers_pb2.Int32Value,
    )
    estimated_arrival_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    estimated_task_completion_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    state: tasks.Task.State = proto.Field(
        proto.ENUM,
        number=11,
        enum=tasks.Task.State,
    )
    task_outcome: tasks.Task.TaskOutcome = proto.Field(
        proto.ENUM,
        number=9,
        enum=tasks.Task.TaskOutcome,
    )
    task_outcome_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=12,
        message=timestamp_pb2.Timestamp,
    )
    planned_location: delivery_vehicles.LocationInfo = proto.Field(
        proto.MESSAGE,
        number=10,
        message=delivery_vehicles.LocationInfo,
    )
    target_time_window: common.TimeWindow = proto.Field(
        proto.MESSAGE,
        number=13,
        message=common.TimeWindow,
    )
    attributes: MutableSequence[common.TaskAttribute] = proto.RepeatedField(
        proto.MESSAGE,
        number=14,
        message=common.TaskAttribute,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
