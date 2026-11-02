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

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import proto  # type: ignore
from google.geo.type.types import viewport as ggt_viewport

from google.maps.fleetengine_delivery_v1.types import (
    delivery_vehicles as mfd_delivery_vehicles,
)
from google.maps.fleetengine_delivery_v1.types import header as mfd_header
from google.maps.fleetengine_delivery_v1.types import tasks as mfd_tasks

__protobuf__ = proto.module(
    package="maps.fleetengine.delivery.v1",
    manifest={
        "CreateDeliveryVehicleRequest",
        "GetDeliveryVehicleRequest",
        "DeleteDeliveryVehicleRequest",
        "ListDeliveryVehiclesRequest",
        "ListDeliveryVehiclesResponse",
        "UpdateDeliveryVehicleRequest",
        "BatchCreateTasksRequest",
        "BatchCreateTasksResponse",
        "CreateTaskRequest",
        "GetTaskRequest",
        "DeleteTaskRequest",
        "UpdateTaskRequest",
        "ListTasksRequest",
        "ListTasksResponse",
        "GetTaskTrackingInfoRequest",
    },
)


class CreateDeliveryVehicleRequest(proto.Message):
    r"""The ``CreateDeliveryVehicle`` request message.

    Attributes:
        header (google.maps.fleetengine_delivery_v1.types.DeliveryRequestHeader):
            Optional. The standard Delivery API request
            header.
        parent (str):
            Required. Must be in the format ``providers/{provider}``.
            The provider must be the Google Cloud Project ID. For
            example, ``sample-cloud-project``.
        delivery_vehicle_id (str):
            Required. The Delivery Vehicle ID must be unique and subject
            to the following restrictions:

            - Must be a valid Unicode string.
            - Limited to a maximum length of 64 characters.
            - Normalized according to [Unicode Normalization Form C]
              (http://www.unicode.org/reports/tr15/).
            - May not contain any of the following ASCII characters:
              '/', ':', '?', ',', or '#'.
        delivery_vehicle (google.maps.fleetengine_delivery_v1.types.DeliveryVehicle):
            Required. The ``DeliveryVehicle`` entity to create. When
            creating a new delivery vehicle, you may set the following
            optional fields:

            - type
            - last_location
            - attributes

            Note: The DeliveryVehicle's ``name`` field is ignored. All
            other DeliveryVehicle fields must not be set; otherwise, an
            error is returned.
    """

    header: mfd_header.DeliveryRequestHeader = proto.Field(
        proto.MESSAGE,
        number=1,
        message=mfd_header.DeliveryRequestHeader,
    )
    parent: str = proto.Field(
        proto.STRING,
        number=3,
    )
    delivery_vehicle_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    delivery_vehicle: mfd_delivery_vehicles.DeliveryVehicle = proto.Field(
        proto.MESSAGE,
        number=5,
        message=mfd_delivery_vehicles.DeliveryVehicle,
    )


class GetDeliveryVehicleRequest(proto.Message):
    r"""The ``GetDeliveryVehicle`` request message.

    Attributes:
        header (google.maps.fleetengine_delivery_v1.types.DeliveryRequestHeader):
            Optional. The standard Delivery API request
            header.
        name (str):
            Required. Must be in the format
            ``providers/{provider}/deliveryVehicles/{delivery_vehicle}``.
            The ``provider`` must be the Google Cloud Project ID. For
            example, ``sample-cloud-project``.
    """

    header: mfd_header.DeliveryRequestHeader = proto.Field(
        proto.MESSAGE,
        number=1,
        message=mfd_header.DeliveryRequestHeader,
    )
    name: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteDeliveryVehicleRequest(proto.Message):
    r"""DeleteDeliveryVehicle request message.

    Attributes:
        header (google.maps.fleetengine_delivery_v1.types.DeliveryRequestHeader):
            Optional. The standard Delivery API request
            header.
        name (str):
            Required. Must be in the format
            ``providers/{provider}/deliveryVehicles/{delivery_vehicle}``.
            The ``provider`` must be the Google Cloud Project ID. For
            example, ``sample-cloud-project``.
    """

    header: mfd_header.DeliveryRequestHeader = proto.Field(
        proto.MESSAGE,
        number=1,
        message=mfd_header.DeliveryRequestHeader,
    )
    name: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListDeliveryVehiclesRequest(proto.Message):
    r"""The ``ListDeliveryVehicles`` request message.

    Attributes:
        header (google.maps.fleetengine_delivery_v1.types.DeliveryRequestHeader):
            Optional. The standard Delivery API request
            header.
        parent (str):
            Required. Must be in the format ``providers/{provider}``.
            The ``provider`` must be the Google Cloud Project ID. For
            example, ``sample-cloud-project``.
        page_size (int):
            Optional. The maximum number of vehicles to
            return. The service may return fewer than this
            number. If you don't specify this number, then
            the server determines the number of results to
            return.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListDeliveryVehicles`` call. You must provide this in
            order to retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``ListDeliveryVehicles`` must match the call that provided
            the page token.
        filter (str):
            Optional. A filter query to apply when listing delivery
            vehicles. See http://aip.dev/160 for examples of the filter
            syntax. If you don't specify a value, or if you specify an
            empty string for the filter, then all delivery vehicles are
            returned.

            Note that the only queries supported for
            ``ListDeliveryVehicles`` are on vehicle attributes (for
            example, ``attributes.<key> = <value>`` or
            ``attributes.<key1> = <value1> AND attributes.<key2> = <value2>``).
            Also, all attributes are stored as strings, so the only
            supported comparisons against attributes are string
            comparisons. In order to compare against number or boolean
            values, the values must be explicitly quoted to be treated
            as strings (for example, ``attributes.<key> = "10"`` or
            ``attributes.<key> = "true"``).

            The maximum number of restrictions allowed in a filter query
            is 50. A restriction is a part of the query of the form
            ``attribute.<KEY> <COMPARATOR> <VALUE>``, for example
            ``attributes.foo = bar`` is 1 restriction.
        viewport (google.geo.type.types.Viewport):
            Optional. A filter that limits the vehicles
            returned to those whose last known location was
            in the rectangular area defined by the viewport.
    """

    header: mfd_header.DeliveryRequestHeader = proto.Field(
        proto.MESSAGE,
        number=1,
        message=mfd_header.DeliveryRequestHeader,
    )
    parent: str = proto.Field(
        proto.STRING,
        number=3,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=4,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=5,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=6,
    )
    viewport: ggt_viewport.Viewport = proto.Field(
        proto.MESSAGE,
        number=7,
        message=ggt_viewport.Viewport,
    )


class ListDeliveryVehiclesResponse(proto.Message):
    r"""The ``ListDeliveryVehicles`` response message.

    Attributes:
        delivery_vehicles (MutableSequence[google.maps.fleetengine_delivery_v1.types.DeliveryVehicle]):
            The set of delivery vehicles that meet the
            requested filtering criteria. When no filter is
            specified, the request returns all delivery
            vehicles. A successful response can also be
            empty. An empty response indicates that no
            delivery vehicles were found meeting the
            requested filter criteria.
        next_page_token (str):
            You can pass this token in the
            ``ListDeliveryVehiclesRequest`` to continue to list results.
            When all of the results are returned, this field won't be in
            the response, or it will be an empty string.
        total_size (int):
            The total number of delivery vehicles that
            match the request criteria, across all pages.
    """

    @property
    def raw_page(self):
        return self

    delivery_vehicles: MutableSequence[mfd_delivery_vehicles.DeliveryVehicle] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=mfd_delivery_vehicles.DeliveryVehicle,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    total_size: int = proto.Field(
        proto.INT64,
        number=3,
    )


class UpdateDeliveryVehicleRequest(proto.Message):
    r"""The ``UpdateDeliveryVehicle`` request message.

    Attributes:
        header (google.maps.fleetengine_delivery_v1.types.DeliveryRequestHeader):
            Optional. The standard Delivery API request
            header.
        delivery_vehicle (google.maps.fleetengine_delivery_v1.types.DeliveryVehicle):
            Required. The ``DeliveryVehicle`` entity update to apply.
            Note: You cannot update the name of the ``DeliveryVehicle``.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. A field mask that indicates which
            ``DeliveryVehicle`` fields to update. Note that the
            update_mask must contain at least one field.

            This is a comma-separated list of fully qualified names of
            fields. Example: ``"remaining_vehicle_journey_segments"``.
    """

    header: mfd_header.DeliveryRequestHeader = proto.Field(
        proto.MESSAGE,
        number=1,
        message=mfd_header.DeliveryRequestHeader,
    )
    delivery_vehicle: mfd_delivery_vehicles.DeliveryVehicle = proto.Field(
        proto.MESSAGE,
        number=3,
        message=mfd_delivery_vehicles.DeliveryVehicle,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=4,
        message=field_mask_pb2.FieldMask,
    )


class BatchCreateTasksRequest(proto.Message):
    r"""The ``BatchCreateTask`` request message.

    Attributes:
        header (google.maps.fleetengine_delivery_v1.types.DeliveryRequestHeader):
            Optional. The standard Delivery API request header. Note: If
            you set this field, then the header field in the
            ``CreateTaskRequest`` messages must either be empty, or it
            must match this field.
        parent (str):
            Required. The parent resource shared by all tasks. This
            value must be in the format ``providers/{provider}``. The
            ``provider`` must be the Google Cloud Project ID. For
            example, ``sample-cloud-project``. The parent field in the
            ``CreateTaskRequest`` messages must either be empty, or it
            must match this field.
        requests (MutableSequence[google.maps.fleetengine_delivery_v1.types.CreateTaskRequest]):
            Required. The request message that specifies
            the resources to create. Note: You can create a
            maximum of 500 tasks in a batch.
    """

    header: mfd_header.DeliveryRequestHeader = proto.Field(
        proto.MESSAGE,
        number=1,
        message=mfd_header.DeliveryRequestHeader,
    )
    parent: str = proto.Field(
        proto.STRING,
        number=3,
    )
    requests: MutableSequence["CreateTaskRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="CreateTaskRequest",
    )


class BatchCreateTasksResponse(proto.Message):
    r"""The ``BatchCreateTask`` response message.

    Attributes:
        tasks (MutableSequence[google.maps.fleetengine_delivery_v1.types.Task]):
            The created Tasks.
    """

    tasks: MutableSequence[mfd_tasks.Task] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=mfd_tasks.Task,
    )


class CreateTaskRequest(proto.Message):
    r"""The ``CreateTask`` request message.

    Attributes:
        header (google.maps.fleetengine_delivery_v1.types.DeliveryRequestHeader):
            Optional. The standard Delivery API request
            header.
        parent (str):
            Required. Must be in the format ``providers/{provider}``.
            The ``provider`` must be the Google Cloud Project ID. For
            example, ``sample-cloud-project``.
        task_id (str):
            Required. The Task ID must be unique, but it should be not a
            shipment tracking ID. To store a shipment tracking ID, use
            the ``tracking_id`` field. Note that multiple tasks can have
            the same ``tracking_id``. Task IDs are subject to the
            following restrictions:

            - Must be a valid Unicode string.
            - Limited to a maximum length of 64 characters.
            - Normalized according to [Unicode Normalization Form C]
              (http://www.unicode.org/reports/tr15/).
            - May not contain any of the following ASCII characters:
              '/', ':', '?', ',', or '#'.
        task (google.maps.fleetengine_delivery_v1.types.Task):
            Required. The Task entity to create. When creating a Task,
            the following fields are required:

            - ``type``
            - ``state`` (must be set to ``OPEN``)
            - ``tracking_id`` (must not be set for ``UNAVAILABLE`` or
              ``SCHEDULED_STOP`` tasks, but required for all other task
              types)
            - ``planned_location`` (optional for ``UNAVAILABLE`` tasks)
            - ``task_duration``

            The following fields can be optionally set:

            - ``target_time_window``
            - ``task_tracking_view_config``
            - ``attributes``

            Note: The Task's ``name`` field is ignored. All other Task
            fields must not be set; otherwise, an error is returned.
    """

    header: mfd_header.DeliveryRequestHeader = proto.Field(
        proto.MESSAGE,
        number=1,
        message=mfd_header.DeliveryRequestHeader,
    )
    parent: str = proto.Field(
        proto.STRING,
        number=3,
    )
    task_id: str = proto.Field(
        proto.STRING,
        number=5,
    )
    task: mfd_tasks.Task = proto.Field(
        proto.MESSAGE,
        number=4,
        message=mfd_tasks.Task,
    )


class GetTaskRequest(proto.Message):
    r"""The ``GetTask`` request message.

    Attributes:
        header (google.maps.fleetengine_delivery_v1.types.DeliveryRequestHeader):
            Optional. The standard Delivery API request
            header.
        name (str):
            Required. Must be in the format
            ``providers/{provider}/tasks/{task}``. The ``provider`` must
            be the Google Cloud Project ID. For example,
            ``sample-cloud-project``.
    """

    header: mfd_header.DeliveryRequestHeader = proto.Field(
        proto.MESSAGE,
        number=1,
        message=mfd_header.DeliveryRequestHeader,
    )
    name: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteTaskRequest(proto.Message):
    r"""DeleteTask request message.

    Attributes:
        header (google.maps.fleetengine_delivery_v1.types.DeliveryRequestHeader):
            Optional. The standard Delivery API request
            header.
        name (str):
            Required. Must be in the format
            ``providers/{provider}/tasks/{task}``. The ``provider`` must
            be the Google Cloud Project ID. For example,
            ``sample-cloud-project``.
    """

    header: mfd_header.DeliveryRequestHeader = proto.Field(
        proto.MESSAGE,
        number=1,
        message=mfd_header.DeliveryRequestHeader,
    )
    name: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UpdateTaskRequest(proto.Message):
    r"""The ``UpdateTask`` request message.

    Attributes:
        header (google.maps.fleetengine_delivery_v1.types.DeliveryRequestHeader):
            Optional. The standard Delivery API request
            header.
        task (google.maps.fleetengine_delivery_v1.types.Task):
            Required. The Task associated with the update. The following
            fields are maintained by Fleet Engine. Do not update them
            using ``Task.update``.

            - ``last_location``.
            - ``last_location_snappable``.
            - ``name``.
            - ``remaining_vehicle_journey_segments``.
            - ``task_outcome_location_source``.

            Note: You cannot change the value of ``task_outcome`` once
            you set it.

            If the Task has been assigned to a delivery vehicle, then
            don't set the Task state to CLOSED using ``Task.update``.
            Instead, remove the ``VehicleStop`` that contains the Task
            from the delivery vehicle, which automatically sets the Task
            state to CLOSED.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The field mask that indicates which Task fields to
            update. Note: The ``update_mask`` must contain at least one
            field.

            This is a comma-separated list of fully qualified names of
            fields. Example:
            ``"task_outcome,task_outcome_time,task_outcome_location"``.
    """

    header: mfd_header.DeliveryRequestHeader = proto.Field(
        proto.MESSAGE,
        number=1,
        message=mfd_header.DeliveryRequestHeader,
    )
    task: mfd_tasks.Task = proto.Field(
        proto.MESSAGE,
        number=3,
        message=mfd_tasks.Task,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=4,
        message=field_mask_pb2.FieldMask,
    )


class ListTasksRequest(proto.Message):
    r"""The ``ListTasks`` request message.

    Attributes:
        header (google.maps.fleetengine_delivery_v1.types.DeliveryRequestHeader):
            Optional. The standard Delivery API request
            header.
        parent (str):
            Required. Must be in the format ``providers/{provider}``.
            The ``provider`` must be the Google Cloud Project ID. For
            example, ``sample-cloud-project``.
        page_size (int):
            Optional. The maximum number of Tasks to
            return. The service may return fewer than this
            value. If you don't specify this value, then the
            server determines the number of results to
            return.
        page_token (str):
            Optional. A page token received from a previous
            ``ListTasks`` call. You can provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListTasks`` must match the call that provided the page
            token.
        filter (str):
            Optional. A filter query to apply when listing Tasks. See
            http://aip.dev/160 for examples of filter syntax. If you
            don't specify a value, or if you filter on an empty string,
            then all Tasks are returned. For information about the Task
            properties that you can filter on, see `List
            tasks <https://developers.google.com/maps/documentation/mobility/fleet-engine/journeys/tasks/find-tasks#filter_listed_tasks>`__.
    """

    header: mfd_header.DeliveryRequestHeader = proto.Field(
        proto.MESSAGE,
        number=1,
        message=mfd_header.DeliveryRequestHeader,
    )
    parent: str = proto.Field(
        proto.STRING,
        number=3,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=4,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=5,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=6,
    )


class ListTasksResponse(proto.Message):
    r"""The ``ListTasks`` response that contains the set of Tasks that meet
    the filter criteria in the ``ListTasksRequest``.

    Attributes:
        tasks (MutableSequence[google.maps.fleetengine_delivery_v1.types.Task]):
            The set of Tasks that meet the requested
            filtering criteria. When no filter is specified,
            the request returns all tasks. A successful
            response can also be empty. An empty response
            indicates that no Tasks were found meeting the
            requested filter criteria.
        next_page_token (str):
            Pass this token in the ``ListTasksRequest`` to continue to
            list results. If all results have been returned, then this
            field is either an empty string, or it doesn't appear in the
            response.
        total_size (int):
            The total number of Tasks that match the
            request criteria, across all pages.
    """

    @property
    def raw_page(self):
        return self

    tasks: MutableSequence[mfd_tasks.Task] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=mfd_tasks.Task,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    total_size: int = proto.Field(
        proto.INT64,
        number=3,
    )


class GetTaskTrackingInfoRequest(proto.Message):
    r"""The ``GetTaskTrackingInfoRequest`` request message.

    Attributes:
        header (google.maps.fleetengine_delivery_v1.types.DeliveryRequestHeader):
            Optional. The standard Delivery API request
            header.
        name (str):
            Required. Must be in the format
            ``providers/{provider}/taskTrackingInfo/{tracking_id}``. The
            ``provider`` must be the Google Cloud Project ID, and the
            ``tracking_id`` must be the tracking ID associated with the
            task. An example name can be
            ``providers/sample-cloud-project/taskTrackingInfo/sample-tracking-id``.
    """

    header: mfd_header.DeliveryRequestHeader = proto.Field(
        proto.MESSAGE,
        number=1,
        message=mfd_header.DeliveryRequestHeader,
    )
    name: str = proto.Field(
        proto.STRING,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
