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
import google.protobuf.wrappers_pb2 as wrappers_pb2  # type: ignore
import google.type.latlng_pb2 as latlng_pb2  # type: ignore
import proto  # type: ignore
from google.geo.type.types import viewport as ggt_viewport

from google.maps.fleetengine_v1.types import fleetengine
from google.maps.fleetengine_v1.types import header as mf_header
from google.maps.fleetengine_v1.types import vehicles as mf_vehicles

__protobuf__ = proto.module(
    package="maps.fleetengine.v1",
    manifest={
        "CreateVehicleRequest",
        "GetVehicleRequest",
        "DeleteVehicleRequest",
        "UpdateVehicleRequest",
        "UpdateVehicleAttributesRequest",
        "UpdateVehicleAttributesResponse",
        "SearchVehiclesRequest",
        "SearchVehiclesResponse",
        "ListVehiclesRequest",
        "ListVehiclesResponse",
        "Waypoint",
        "VehicleMatch",
        "VehicleAttributeList",
    },
)


class CreateVehicleRequest(proto.Message):
    r"""``CreateVehicle`` request message.

    Attributes:
        header (google.maps.fleetengine_v1.types.RequestHeader):
            The standard Fleet Engine request header.
        parent (str):
            Required. Must be in the format ``providers/{provider}``.
            The provider must be the Project ID (for example,
            ``sample-cloud-project``) of the Google Cloud Project of
            which the service account making this call is a member.
        vehicle_id (str):
            Required. Unique Vehicle ID. Subject to the following
            restrictions:

            - Must be a valid Unicode string.
            - Limited to a maximum length of 64 characters.
            - Normalized according to [Unicode Normalization Form C]
              (http://www.unicode.org/reports/tr15/).
            - May not contain any of the following ASCII characters:
              '/', ':', '?', ',', or '#'.
        vehicle (google.maps.fleetengine_v1.types.Vehicle):
            Required. The Vehicle entity to create. When creating a
            Vehicle, the following fields are required:

            - ``vehicleState``
            - ``supportedTripTypes``
            - ``maximumCapacity``
            - ``vehicleType``

            When creating a Vehicle, the following fields are ignored:

            - ``name``
            - ``currentTrips``
            - ``availableCapacity``
            - ``current_route_segment``
            - ``current_route_segment_end_point``
            - ``current_route_segment_version``
            - ``current_route_segment_traffic``
            - ``route``
            - ``waypoints``
            - ``waypoints_version``
            - ``remaining_distance_meters``
            - ``remaining_time_seconds``
            - ``eta_to_next_waypoint``
            - ``navigation_status``

            All other fields are optional and used if provided.
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
    vehicle: mf_vehicles.Vehicle = proto.Field(
        proto.MESSAGE,
        number=5,
        message=mf_vehicles.Vehicle,
    )


class GetVehicleRequest(proto.Message):
    r"""``GetVehicle`` request message.

    Attributes:
        header (google.maps.fleetengine_v1.types.RequestHeader):
            The standard Fleet Engine request header.
        name (str):
            Required. Must be in the format
            ``providers/{provider}/vehicles/{vehicle}``. The provider
            must be the Project ID (for example,
            ``sample-cloud-project``) of the Google Cloud Project of
            which the service account making this call is a member.
        current_route_segment_version (google.protobuf.timestamp_pb2.Timestamp):
            Indicates the minimum timestamp (exclusive) for which
            ``Vehicle.current_route_segment`` is retrieved. If the route
            is unchanged since this timestamp, the
            ``current_route_segment`` field is not set in the response.
            If a minimum is unspecified, the ``current_route_segment``
            is always retrieved.
        waypoints_version (google.protobuf.timestamp_pb2.Timestamp):
            Indicates the minimum timestamp (exclusive) for which
            ``Vehicle.waypoints`` data is retrieved. If the waypoints
            are unchanged since this timestamp, the
            ``vehicle.waypoints`` data is not set in the response. If
            this field is unspecified, ``vehicle.waypoints`` is always
            retrieved.
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
    current_route_segment_version: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    waypoints_version: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )


class DeleteVehicleRequest(proto.Message):
    r"""DeleteVehicle request message.

    Attributes:
        header (google.maps.fleetengine_v1.types.RequestHeader):
            Optional. The standard Fleet Engine request
            header.
        name (str):
            Required. Must be in the format
            ``providers/{provider}/vehicles/{vehicle}``. The {provider}
            must be the Project ID (for example,
            ``sample-cloud-project``) of the Google Cloud Project of
            which the service account making this call is a member.
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


class UpdateVehicleRequest(proto.Message):
    r"""\`UpdateVehicle request message.

    Attributes:
        header (google.maps.fleetengine_v1.types.RequestHeader):
            The standard Fleet Engine request header.
        name (str):
            Required. Must be in the format
            ``providers/{provider}/vehicles/{vehicle}``. The {provider}
            must be the Project ID (for example,
            ``sample-cloud-project``) of the Google Cloud Project of
            which the service account making this call is a member.
        vehicle (google.maps.fleetengine_v1.types.Vehicle):
            Required. The ``Vehicle`` entity values to apply. When
            updating a ``Vehicle``, the following fields may not be
            updated as they are managed by the server.

            - ``available_capacity``
            - ``current_route_segment_version``
            - ``current_trips``
            - ``name``
            - ``waypoints_version``

            If the ``attributes`` field is updated, **all** the
            vehicle's attributes are replaced with the attributes
            provided in the request. If you want to update only some
            attributes, see the ``UpdateVehicleAttributes`` method.

            Likewise, the ``waypoints`` field can be updated, but must
            contain all the waypoints currently on the vehicle, and no
            other waypoints.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. A field mask indicating which fields of the
            ``Vehicle`` to update. At least one field name must be
            provided.
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
    vehicle: mf_vehicles.Vehicle = proto.Field(
        proto.MESSAGE,
        number=4,
        message=mf_vehicles.Vehicle,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=5,
        message=field_mask_pb2.FieldMask,
    )


class UpdateVehicleAttributesRequest(proto.Message):
    r"""``UpdateVehicleAttributes`` request message.

    Attributes:
        header (google.maps.fleetengine_v1.types.RequestHeader):
            The standard Fleet Engine request header.
        name (str):
            Required. Must be in the format
            ``providers/{provider}/vehicles/{vehicle}``. The provider
            must be the Project ID (for example,
            ``sample-cloud-project``) of the Google Cloud Project of
            which the service account making this call is a member.
        attributes (MutableSequence[google.maps.fleetengine_v1.types.VehicleAttribute]):
            Required. The vehicle attributes to update.
            Unmentioned attributes are not altered or
            removed.
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
    attributes: MutableSequence[fleetengine.VehicleAttribute] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=fleetengine.VehicleAttribute,
    )


class UpdateVehicleAttributesResponse(proto.Message):
    r"""``UpdateVehicleAttributes`` response message.

    Attributes:
        attributes (MutableSequence[google.maps.fleetengine_v1.types.VehicleAttribute]):
            Required. The updated full list of vehicle
            attributes, including new, altered, and
            untouched attributes.
    """

    attributes: MutableSequence[fleetengine.VehicleAttribute] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=fleetengine.VehicleAttribute,
    )


class SearchVehiclesRequest(proto.Message):
    r"""``SearchVehicles`` request message.

    Attributes:
        header (google.maps.fleetengine_v1.types.RequestHeader):
            The standard Fleet Engine request header.
        parent (str):
            Required. Must be in the format ``providers/{provider}``.
            The provider must be the Project ID (for example,
            ``sample-cloud-project``) of the Google Cloud Project of
            which the service account making this call is a member.
        pickup_point (google.maps.fleetengine_v1.types.TerminalLocation):
            Required. The pickup point to search near.
        dropoff_point (google.maps.fleetengine_v1.types.TerminalLocation):
            The customer's intended dropoff location. The field is
            required if ``trip_types`` contains ``TripType.SHARED``.
        pickup_radius_meters (int):
            Required. Defines the vehicle search radius
            around the pickup point. Only vehicles within
            the search radius will be returned. Value must
            be between 400 and 10000 meters (inclusive).
        count (int):
            Required. Specifies the maximum number of
            vehicles to return. The value must be between 1
            and 50 (inclusive).
        minimum_capacity (int):
            Required. Specifies the number of passengers
            being considered for a trip. The value must be
            greater than or equal to one. The driver is not
            considered in the capacity value.
        trip_types (MutableSequence[google.maps.fleetengine_v1.types.TripType]):
            Required. Represents the type of proposed trip. Must include
            exactly one type. ``UNKNOWN_TRIP_TYPE`` is not allowed.
            Restricts the search to only those vehicles that can support
            that trip type.
        maximum_staleness (google.protobuf.duration_pb2.Duration):
            Restricts the search to only those vehicles
            that have sent location updates to Fleet Engine
            within the specified duration. Stationary
            vehicles still transmitting their locations are
            not considered stale. If this field is not set,
            the server uses five minutes as the default
            value.
        vehicle_types (MutableSequence[google.maps.fleetengine_v1.types.Vehicle.VehicleType]):
            Required. Restricts the search to vehicles with one of the
            specified types. At least one vehicle type must be
            specified. VehicleTypes with a category of ``UNKNOWN`` are
            not allowed.
        required_attributes (MutableSequence[google.maps.fleetengine_v1.types.VehicleAttribute]):
            Callers can form complex logical operations using any
            combination of the ``required_attributes``,
            ``required_one_of_attributes``, and
            ``required_one_of_attribute_sets`` fields.

            ``required_attributes`` is a list;
            ``required_one_of_attributes`` uses a message which allows a
            list of lists. In combination, the two fields allow the
            composition of this expression:

            ::

               (required_attributes[0] AND required_attributes[1] AND ...)
               AND
               (required_one_of_attributes[0][0] OR required_one_of_attributes[0][1] OR
               ...)
               AND
               (required_one_of_attributes[1][0] OR required_one_of_attributes[1][1] OR
               ...)

            Restricts the search to only those vehicles with the
            specified attributes. This field is a conjunction/AND
            operation. A max of 50 required_attributes is allowed. This
            matches the maximum number of attributes allowed on a
            vehicle.
        required_one_of_attributes (MutableSequence[google.maps.fleetengine_v1.types.VehicleAttributeList]):
            Restricts the search to only those vehicles with at least
            one of the specified attributes in each
            ``VehicleAttributeList``. Within each list, a vehicle must
            match at least one of the attributes. This field is an
            inclusive disjunction/OR operation in each
            ``VehicleAttributeList`` and a conjunction/AND operation
            across the collection of ``VehicleAttributeList``.
        required_one_of_attribute_sets (MutableSequence[google.maps.fleetengine_v1.types.VehicleAttributeList]):
            ``required_one_of_attribute_sets`` provides additional
            functionality.

            Similar to ``required_one_of_attributes``,
            ``required_one_of_attribute_sets`` uses a message which
            allows a list of lists, allowing expressions such as this
            one:

            ::

               (required_attributes[0] AND required_attributes[1] AND ...)
               AND
               (
                 (required_one_of_attribute_sets[0][0] AND
                 required_one_of_attribute_sets[0][1] AND
                 ...)
                 OR
                 (required_one_of_attribute_sets[1][0] AND
                 required_one_of_attribute_sets[1][1] AND
                 ...)
               )

            Restricts the search to only those vehicles with all the
            attributes in a ``VehicleAttributeList``. Within each list,
            a vehicle must match all of the attributes. This field is a
            conjunction/AND operation in each ``VehicleAttributeList``
            and inclusive disjunction/OR operation across the collection
            of ``VehicleAttributeList``.
        order_by (google.maps.fleetengine_v1.types.SearchVehiclesRequest.VehicleMatchOrder):
            Required. Specifies the desired ordering
            criterion for results.
        include_back_to_back (bool):
            This indicates if vehicles with a single active trip are
            eligible for this search. This field is only used when
            ``current_trips_present`` is unspecified. When
            ``current_trips_present`` is unspecified and this field is
            ``false``, vehicles with assigned trips are excluded from
            the search results. When ``current_trips_present`` is
            unspecified and this field is ``true``, search results can
            include vehicles with one active trip that has a status of
            ``ENROUTE_TO_DROPOFF``. When ``current_trips_present`` is
            specified, this field cannot be set to true.

            The default value is ``false``.
        trip_id (str):
            Indicates the trip associated with this
            ``SearchVehicleRequest``.
        current_trips_present (google.maps.fleetengine_v1.types.SearchVehiclesRequest.CurrentTripsPresent):
            This indicates if vehicles with active trips are eligible
            for this search. This must be set to something other than
            ``CURRENT_TRIPS_PRESENT_UNSPECIFIED`` if ``trip_type``
            includes ``SHARED``.
        filter (str):
            Optional. A filter query to apply when searching vehicles.
            See http://aip.dev/160 for examples of the filter syntax.

            This field is designed to replace the
            ``required_attributes``, ``required_one_of_attributes``, and
            ``required_one_of_attributes_sets`` fields. If a non-empty
            value is specified here, the following fields must be empty:
            ``required_attributes``, ``required_one_of_attributes``, and
            ``required_one_of_attributes_sets``.

            This filter functions as an AND clause with other
            constraints, such as ``minimum_capacity`` or
            ``vehicle_types``.

            Note that the only queries supported are on vehicle
            attributes (for example, ``attributes.<key> = <value>`` or
            ``attributes.<key1> = <value1> AND attributes.<key2> = <value2>``).
            The maximum number of restrictions allowed in a filter query
            is 50.

            Also, all attributes are stored as strings, so the only
            supported comparisons against attributes are string
            comparisons. In order to compare against number or boolean
            values, the values must be explicitly quoted to be treated
            as strings (for example, ``attributes.<key> = "10"`` or
            ``attributes.<key> = "true"``).
    """

    class VehicleMatchOrder(proto.Enum):
        r"""Specifies the order of the vehicle matches in the response.

        Values:
            UNKNOWN_VEHICLE_MATCH_ORDER (0):
                Default, used for unspecified or unrecognized
                vehicle matches order.
            PICKUP_POINT_ETA (1):
                Ascending order by vehicle driving time to
                the pickup point.
            PICKUP_POINT_DISTANCE (2):
                Ascending order by vehicle driving distance
                to the pickup point.
            DROPOFF_POINT_ETA (3):
                Ascending order by vehicle driving time to
                the dropoff point. This order can only be used
                if the dropoff point is specified in the
                request.
            PICKUP_POINT_STRAIGHT_DISTANCE (4):
                Ascending order by straight-line distance
                from the vehicle's last reported location to the
                pickup point.
            COST (5):
                Ascending order by the configured match cost.
                Match cost is defined as a weighted calculation
                between straight-line distance and ETA. Weights
                are set with default values and can be modified
                per customer. Please contact Google support if
                these weights need to be modified for your
                project.
        """

        UNKNOWN_VEHICLE_MATCH_ORDER = 0
        PICKUP_POINT_ETA = 1
        PICKUP_POINT_DISTANCE = 2
        DROPOFF_POINT_ETA = 3
        PICKUP_POINT_STRAIGHT_DISTANCE = 4
        COST = 5

    class CurrentTripsPresent(proto.Enum):
        r"""Specifies the types of restrictions on a vehicle's current
        trips.

        Values:
            CURRENT_TRIPS_PRESENT_UNSPECIFIED (0):
                The availability of vehicles with trips present is governed
                by the ``include_back_to_back`` field.
            NONE (1):
                Vehicles without trips can appear in search results. When
                this value is used, ``include_back_to_back`` cannot be
                ``true``.
            ANY (2):
                Vehicles with at most 5 current trips and 10 waypoints are
                included in the search results. When this value is used,
                ``include_back_to_back`` cannot be ``true``.
        """

        CURRENT_TRIPS_PRESENT_UNSPECIFIED = 0
        NONE = 1
        ANY = 2

    header: mf_header.RequestHeader = proto.Field(
        proto.MESSAGE,
        number=1,
        message=mf_header.RequestHeader,
    )
    parent: str = proto.Field(
        proto.STRING,
        number=3,
    )
    pickup_point: fleetengine.TerminalLocation = proto.Field(
        proto.MESSAGE,
        number=4,
        message=fleetengine.TerminalLocation,
    )
    dropoff_point: fleetengine.TerminalLocation = proto.Field(
        proto.MESSAGE,
        number=5,
        message=fleetengine.TerminalLocation,
    )
    pickup_radius_meters: int = proto.Field(
        proto.INT32,
        number=6,
    )
    count: int = proto.Field(
        proto.INT32,
        number=7,
    )
    minimum_capacity: int = proto.Field(
        proto.INT32,
        number=8,
    )
    trip_types: MutableSequence[fleetengine.TripType] = proto.RepeatedField(
        proto.ENUM,
        number=9,
        enum=fleetengine.TripType,
    )
    maximum_staleness: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=10,
        message=duration_pb2.Duration,
    )
    vehicle_types: MutableSequence[mf_vehicles.Vehicle.VehicleType] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=14,
            message=mf_vehicles.Vehicle.VehicleType,
        )
    )
    required_attributes: MutableSequence[fleetengine.VehicleAttribute] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=12,
            message=fleetengine.VehicleAttribute,
        )
    )
    required_one_of_attributes: MutableSequence["VehicleAttributeList"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=15,
            message="VehicleAttributeList",
        )
    )
    required_one_of_attribute_sets: MutableSequence["VehicleAttributeList"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=20,
            message="VehicleAttributeList",
        )
    )
    order_by: VehicleMatchOrder = proto.Field(
        proto.ENUM,
        number=13,
        enum=VehicleMatchOrder,
    )
    include_back_to_back: bool = proto.Field(
        proto.BOOL,
        number=18,
    )
    trip_id: str = proto.Field(
        proto.STRING,
        number=19,
    )
    current_trips_present: CurrentTripsPresent = proto.Field(
        proto.ENUM,
        number=21,
        enum=CurrentTripsPresent,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=22,
    )


class SearchVehiclesResponse(proto.Message):
    r"""``SearchVehicles`` response message.

    Attributes:
        matches (MutableSequence[google.maps.fleetengine_v1.types.VehicleMatch]):
            List of vehicles that match the ``SearchVehiclesRequest``
            criteria, ordered according to
            ``SearchVehiclesRequest.order_by`` field.
    """

    matches: MutableSequence["VehicleMatch"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="VehicleMatch",
    )


class ListVehiclesRequest(proto.Message):
    r"""``ListVehicles`` request message.

    Attributes:
        header (google.maps.fleetengine_v1.types.RequestHeader):
            The standard Fleet Engine request header.
        parent (str):
            Required. Must be in the format ``providers/{provider}``.
            The provider must be the Project ID (for example,
            ``sample-cloud-project``) of the Google Cloud Project of
            which the service account making this call is a member.
        page_size (int):
            The maximum number of vehicles to return.
            Default value: 100.
        page_token (str):
            The value of the ``next_page_token`` provided by a previous
            call to ``ListVehicles`` so that you can paginate through
            groups of vehicles. The value is undefined if the filter
            criteria of the request is not the same as the filter
            criteria for the previous call to ``ListVehicles``.
        minimum_capacity (google.protobuf.wrappers_pb2.Int32Value):
            Specifies the required minimum capacity of the vehicle. All
            vehicles returned will have a ``maximum_capacity`` greater
            than or equal to this value. If set, must be greater or
            equal to 0.
        trip_types (MutableSequence[google.maps.fleetengine_v1.types.TripType]):
            Restricts the response to vehicles that
            support at least one of the specified trip
            types.
        maximum_staleness (google.protobuf.duration_pb2.Duration):
            Restricts the response to vehicles that have
            sent location updates to Fleet Engine within the
            specified duration. Stationary vehicles still
            transmitting their locations are not considered
            stale. If present, must be a valid positive
            duration.
        vehicle_type_categories (MutableSequence[google.maps.fleetengine_v1.types.Vehicle.VehicleType.Category]):
            Required. Restricts the response to vehicles with one of the
            specified type categories. ``UNKNOWN`` is not allowed.
        required_attributes (MutableSequence[str]):
            Callers can form complex logical operations using any
            combination of the ``required_attributes``,
            ``required_one_of_attributes``, and
            ``required_one_of_attribute_sets`` fields.

            ``required_attributes`` is a list;
            ``required_one_of_attributes`` uses a message which allows a
            list of lists. In combination, the two fields allow the
            composition of this expression:

            ::

               (required_attributes[0] AND required_attributes[1] AND ...)
               AND
               (required_one_of_attributes[0][0] OR required_one_of_attributes[0][1] OR
               ...)
               AND
               (required_one_of_attributes[1][0] OR required_one_of_attributes[1][1] OR
               ...)

            Restricts the response to vehicles with the specified
            attributes. This field is a conjunction/AND operation. A max
            of 50 required_attributes is allowed. This matches the
            maximum number of attributes allowed on a vehicle. Each
            repeated string should be of the format "key:value".
        required_one_of_attributes (MutableSequence[str]):
            Restricts the response to vehicles with at least one of the
            specified attributes in each ``VehicleAttributeList``.
            Within each list, a vehicle must match at least one of the
            attributes. This field is an inclusive disjunction/OR
            operation in each ``VehicleAttributeList`` and a
            conjunction/AND operation across the collection of
            ``VehicleAttributeList``. Each repeated string should be of
            the format "key1:value1|key2:value2|key3:value3".
        required_one_of_attribute_sets (MutableSequence[str]):
            ``required_one_of_attribute_sets`` provides additional
            functionality.

            Similar to ``required_one_of_attributes``,
            ``required_one_of_attribute_sets`` uses a message which
            allows a list of lists, allowing expressions such as this
            one:

            ::

               (required_attributes[0] AND required_attributes[1] AND ...)
               AND
               (
                 (required_one_of_attribute_sets[0][0] AND
                 required_one_of_attribute_sets[0][1] AND
                 ...)
                 OR
                 (required_one_of_attribute_sets[1][0] AND
                 required_one_of_attribute_sets[1][1] AND
                 ...)
               )

            Restricts the response to vehicles that match all the
            attributes in a ``VehicleAttributeList``. Within each list,
            a vehicle must match all of the attributes. This field is a
            conjunction/AND operation in each ``VehicleAttributeList``
            and inclusive disjunction/OR operation across the collection
            of ``VehicleAttributeList``. Each repeated string should be
            of the format "key1:value1|key2:value2|key3:value3".
        vehicle_state (google.maps.fleetengine_v1.types.VehicleState):
            Restricts the response to vehicles that have
            this vehicle state.
        on_trip_only (bool):
            Only return the vehicles with current
            trip(s).
        filter (str):
            Optional. A filter query to apply when listing vehicles. See
            http://aip.dev/160 for examples of the filter syntax.

            This field is designed to replace the
            ``required_attributes``, ``required_one_of_attributes``, and
            ``required_one_of_attributes_sets`` fields. If a non-empty
            value is specified here, the following fields must be empty:
            ``required_attributes``, ``required_one_of_attributes``, and
            ``required_one_of_attributes_sets``.

            This filter functions as an AND clause with other
            constraints, such as ``vehicle_state`` or ``on_trip_only``.

            Note that the only queries supported are on vehicle
            attributes (for example, ``attributes.<key> = <value>`` or
            ``attributes.<key1> = <value1> AND attributes.<key2> = <value2>``).
            The maximum number of restrictions allowed in a filter query
            is 50.

            Also, all attributes are stored as strings, so the only
            supported comparisons against attributes are string
            comparisons. In order to compare against number or boolean
            values, the values must be explicitly quoted to be treated
            as strings (for example, ``attributes.<key> = "10"`` or
            ``attributes.<key> = "true"``).
        viewport (google.geo.type.types.Viewport):
            Optional. A filter that limits the vehicles
            returned to those whose last known location was
            in the rectangular area defined by the viewport.
    """

    header: mf_header.RequestHeader = proto.Field(
        proto.MESSAGE,
        number=12,
        message=mf_header.RequestHeader,
    )
    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )
    minimum_capacity: wrappers_pb2.Int32Value = proto.Field(
        proto.MESSAGE,
        number=6,
        message=wrappers_pb2.Int32Value,
    )
    trip_types: MutableSequence[fleetengine.TripType] = proto.RepeatedField(
        proto.ENUM,
        number=7,
        enum=fleetengine.TripType,
    )
    maximum_staleness: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=8,
        message=duration_pb2.Duration,
    )
    vehicle_type_categories: MutableSequence[
        mf_vehicles.Vehicle.VehicleType.Category
    ] = proto.RepeatedField(
        proto.ENUM,
        number=9,
        enum=mf_vehicles.Vehicle.VehicleType.Category,
    )
    required_attributes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=10,
    )
    required_one_of_attributes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=13,
    )
    required_one_of_attribute_sets: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=15,
    )
    vehicle_state: mf_vehicles.VehicleState = proto.Field(
        proto.ENUM,
        number=11,
        enum=mf_vehicles.VehicleState,
    )
    on_trip_only: bool = proto.Field(
        proto.BOOL,
        number=14,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=16,
    )
    viewport: ggt_viewport.Viewport = proto.Field(
        proto.MESSAGE,
        number=17,
        message=ggt_viewport.Viewport,
    )


class ListVehiclesResponse(proto.Message):
    r"""``ListVehicles`` response message.

    Attributes:
        vehicles (MutableSequence[google.maps.fleetengine_v1.types.Vehicle]):
            Vehicles matching the criteria in the request. The maximum
            number of vehicles returned is determined by the
            ``page_size`` field in the request.
        next_page_token (str):
            Token to retrieve the next page of vehicles,
            or empty if there are no more vehicles that meet
            the request criteria.
        total_size (int):
            Required. Total number of vehicles matching
            the request criteria across all pages.
    """

    @property
    def raw_page(self):
        return self

    vehicles: MutableSequence[mf_vehicles.Vehicle] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=mf_vehicles.Vehicle,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    total_size: int = proto.Field(
        proto.INT64,
        number=3,
    )


class Waypoint(proto.Message):
    r"""Describes intermediate points along a route for a ``VehicleMatch``
    in a ``SearchVehiclesResponse``. This concept is represented as a
    ``TripWaypoint`` in all other endpoints.

    Attributes:
        lat_lng (google.type.latlng_pb2.LatLng):
            The location of this waypoint.
        eta (google.protobuf.timestamp_pb2.Timestamp):
            The estimated time that the vehicle will
            arrive at this waypoint.
    """

    lat_lng: latlng_pb2.LatLng = proto.Field(
        proto.MESSAGE,
        number=1,
        message=latlng_pb2.LatLng,
    )
    eta: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )


class VehicleMatch(proto.Message):
    r"""Contains the vehicle and related estimates for a vehicle that match
    the points of active trips for the vehicle
    ``SearchVehiclesRequest``.

    Attributes:
        vehicle (google.maps.fleetengine_v1.types.Vehicle):
            Required. A vehicle that matches the request.
        vehicle_pickup_eta (google.protobuf.timestamp_pb2.Timestamp):
            The vehicle's driving ETA to the pickup point specified in
            the request. An empty value indicates a failure in
            calculating ETA for the vehicle. If
            ``SearchVehiclesRequest.include_back_to_back`` was ``true``
            and this vehicle has an active trip, ``vehicle_pickup_eta``
            includes the time required to complete the current active
            trip.
        vehicle_pickup_distance_meters (google.protobuf.wrappers_pb2.Int32Value):
            The distance from the Vehicle's current
            location to the pickup point specified in the
            request, including any intermediate pickup or
            dropoff points for existing trips. This distance
            comprises the calculated driving (route)
            distance, plus the straight line distance
            between the navigation end point and the
            requested pickup point. (The distance between
            the navigation end point and the requested
            pickup point is typically small.) An empty value
            indicates an error in calculating the distance.
        vehicle_pickup_straight_line_distance_meters (google.protobuf.wrappers_pb2.Int32Value):
            Required. The straight-line distance between
            the vehicle and the pickup point specified in
            the request.
        vehicle_dropoff_eta (google.protobuf.timestamp_pb2.Timestamp):
            The complete vehicle's driving ETA to the drop off point
            specified in the request. The ETA includes stopping at any
            waypoints before the ``dropoff_point`` specified in the
            request. The value will only be populated when a drop off
            point is specified in the request. An empty value indicates
            an error calculating the ETA.
        vehicle_pickup_to_dropoff_distance_meters (google.protobuf.wrappers_pb2.Int32Value):
            The vehicle's driving distance (in meters) from the pickup
            point to the drop off point specified in the request. The
            distance is only between the two points and does not include
            the vehicle location or any other points that must be
            visited before the vehicle visits either the pickup point or
            dropoff point. The value will only be populated when a
            ``dropoff_point`` is specified in the request. An empty
            value indicates a failure in calculating the distance from
            the pickup to drop off point specified in the request.
        trip_type (google.maps.fleetengine_v1.types.TripType):
            Required. The trip type of the request that
            was used to calculate the ETA to the pickup
            point.
        vehicle_trips_waypoints (MutableSequence[google.maps.fleetengine_v1.types.Waypoint]):
            The ordered list of waypoints used to
            calculate the ETA. The list includes vehicle
            location, the pickup points of active trips for
            the vehicle, and the pickup points provided in
            the request. An empty list indicates a failure
            in calculating ETA for the vehicle.
        vehicle_match_type (google.maps.fleetengine_v1.types.VehicleMatch.VehicleMatchType):
            Type of the vehicle match.
        requested_ordered_by (google.maps.fleetengine_v1.types.SearchVehiclesRequest.VehicleMatchOrder):
            The order requested for sorting vehicle matches. Equivalent
            to ``ordered_by``.
        ordered_by (google.maps.fleetengine_v1.types.SearchVehiclesRequest.VehicleMatchOrder):
            The order requested for sorting vehicle matches. Equivalent
            to ``requested_ordered_by``.
    """

    class VehicleMatchType(proto.Enum):
        r"""Type of vehicle match.

        Values:
            UNKNOWN (0):
                Unknown vehicle match type
            EXCLUSIVE (1):
                The vehicle currently has no trip assigned to
                it and can proceed to the pickup point.
            BACK_TO_BACK (2):
                The vehicle is currently assigned to a trip,
                but can proceed to the pickup point after
                completing the in-progress trip.  ETA and
                distance calculations take the existing trip
                into account.
            CARPOOL (3):
                The vehicle has sufficient capacity for a
                shared ride.
            CARPOOL_BACK_TO_BACK (4):
                The vehicle will finish its current, active
                trip before proceeding to the pickup point.  ETA
                and distance calculations take the existing trip
                into account.
        """

        UNKNOWN = 0
        EXCLUSIVE = 1
        BACK_TO_BACK = 2
        CARPOOL = 3
        CARPOOL_BACK_TO_BACK = 4

    vehicle: mf_vehicles.Vehicle = proto.Field(
        proto.MESSAGE,
        number=1,
        message=mf_vehicles.Vehicle,
    )
    vehicle_pickup_eta: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    vehicle_pickup_distance_meters: wrappers_pb2.Int32Value = proto.Field(
        proto.MESSAGE,
        number=3,
        message=wrappers_pb2.Int32Value,
    )
    vehicle_pickup_straight_line_distance_meters: wrappers_pb2.Int32Value = proto.Field(
        proto.MESSAGE,
        number=11,
        message=wrappers_pb2.Int32Value,
    )
    vehicle_dropoff_eta: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    vehicle_pickup_to_dropoff_distance_meters: wrappers_pb2.Int32Value = proto.Field(
        proto.MESSAGE,
        number=5,
        message=wrappers_pb2.Int32Value,
    )
    trip_type: fleetengine.TripType = proto.Field(
        proto.ENUM,
        number=6,
        enum=fleetengine.TripType,
    )
    vehicle_trips_waypoints: MutableSequence["Waypoint"] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message="Waypoint",
    )
    vehicle_match_type: VehicleMatchType = proto.Field(
        proto.ENUM,
        number=8,
        enum=VehicleMatchType,
    )
    requested_ordered_by: "SearchVehiclesRequest.VehicleMatchOrder" = proto.Field(
        proto.ENUM,
        number=9,
        enum="SearchVehiclesRequest.VehicleMatchOrder",
    )
    ordered_by: "SearchVehiclesRequest.VehicleMatchOrder" = proto.Field(
        proto.ENUM,
        number=10,
        enum="SearchVehiclesRequest.VehicleMatchOrder",
    )


class VehicleAttributeList(proto.Message):
    r"""A list-of-lists datatype for vehicle attributes.

    Attributes:
        attributes (MutableSequence[google.maps.fleetengine_v1.types.VehicleAttribute]):
            A list of attributes in this collection.
    """

    attributes: MutableSequence[fleetengine.VehicleAttribute] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=fleetengine.VehicleAttribute,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
