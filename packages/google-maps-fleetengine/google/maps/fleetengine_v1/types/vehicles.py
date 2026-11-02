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
import proto  # type: ignore

from google.maps.fleetengine_v1.types import fleetengine

__protobuf__ = proto.module(
    package="maps.fleetengine.v1",
    manifest={
        "VehicleState",
        "LocationPowerSaveMode",
        "BatteryStatus",
        "PowerSource",
        "Vehicle",
        "BatteryInfo",
        "DeviceSettings",
        "LicensePlate",
        "VisualTrafficReportPolylineRendering",
        "TrafficPolylineData",
    },
)


class VehicleState(proto.Enum):
    r"""The state of a ``Vehicle``.

    Values:
        UNKNOWN_VEHICLE_STATE (0):
            Default, used for unspecified or unrecognized
            vehicle states.
        OFFLINE (1):
            The vehicle is not accepting new trips. Note:
            the vehicle may continue to operate in this
            state while completing a trip assigned to it.
        ONLINE (2):
            The vehicle is accepting new trips.
    """

    UNKNOWN_VEHICLE_STATE = 0
    OFFLINE = 1
    ONLINE = 2


class LocationPowerSaveMode(proto.Enum):
    r"""How location features are configured to behave on the mobile
    device when the devices "battery saver" feature is on.
    (https://developer.android.com/reference/android/os/PowerManager#getLocationPowerSaveMode())

    Values:
        UNKNOWN_LOCATION_POWER_SAVE_MODE (0):
            Undefined LocationPowerSaveMode
        LOCATION_MODE_NO_CHANGE (1):
            Either the location providers shouldn't be
            affected by battery saver, or battery saver is
            off.
        LOCATION_MODE_GPS_DISABLED_WHEN_SCREEN_OFF (2):
            The GPS based location provider should be
            disabled when battery saver is on and the device
            is non-interactive.
        LOCATION_MODE_ALL_DISABLED_WHEN_SCREEN_OFF (3):
            All location providers should be disabled
            when battery saver is on and the device is
            non-interactive.
        LOCATION_MODE_FOREGROUND_ONLY (4):
            All the location providers will be kept
            available, but location fixes should only be
            provided to foreground apps.
        LOCATION_MODE_THROTTLE_REQUESTS_WHEN_SCREEN_OFF (5):
            Location will not be turned off, but
            LocationManager will throttle all requests to
            providers when the device is non-interactive.
    """

    UNKNOWN_LOCATION_POWER_SAVE_MODE = 0
    LOCATION_MODE_NO_CHANGE = 1
    LOCATION_MODE_GPS_DISABLED_WHEN_SCREEN_OFF = 2
    LOCATION_MODE_ALL_DISABLED_WHEN_SCREEN_OFF = 3
    LOCATION_MODE_FOREGROUND_ONLY = 4
    LOCATION_MODE_THROTTLE_REQUESTS_WHEN_SCREEN_OFF = 5


class BatteryStatus(proto.Enum):
    r"""Status of the battery, whether full or charging etc.

    Values:
        UNKNOWN_BATTERY_STATUS (0):
            Battery status unknown.
        BATTERY_STATUS_CHARGING (1):
            Battery is being charged.
        BATTERY_STATUS_DISCHARGING (2):
            Battery is discharging.
        BATTERY_STATUS_FULL (3):
            Battery is full.
        BATTERY_STATUS_NOT_CHARGING (4):
            Battery is not charging.
        BATTERY_STATUS_POWER_LOW (5):
            Battery is low on power.
    """

    UNKNOWN_BATTERY_STATUS = 0
    BATTERY_STATUS_CHARGING = 1
    BATTERY_STATUS_DISCHARGING = 2
    BATTERY_STATUS_FULL = 3
    BATTERY_STATUS_NOT_CHARGING = 4
    BATTERY_STATUS_POWER_LOW = 5


class PowerSource(proto.Enum):
    r"""Type of the charger being used to charge the battery.

    Values:
        UNKNOWN_POWER_SOURCE (0):
            Power source unknown.
        POWER_SOURCE_AC (1):
            Power source is an AC charger.
        POWER_SOURCE_USB (2):
            Power source is a USB port.
        POWER_SOURCE_WIRELESS (3):
            Power source is wireless.
        POWER_SOURCE_UNPLUGGED (4):
            Battery is unplugged.
    """

    UNKNOWN_POWER_SOURCE = 0
    POWER_SOURCE_AC = 1
    POWER_SOURCE_USB = 2
    POWER_SOURCE_WIRELESS = 3
    POWER_SOURCE_UNPLUGGED = 4


class Vehicle(proto.Message):
    r"""Vehicle metadata.

    Attributes:
        name (str):
            Output only. The unique name for this vehicle. The format is
            ``providers/{provider}/vehicles/{vehicle}``.
        vehicle_state (google.maps.fleetengine_v1.types.VehicleState):
            The vehicle state.
        supported_trip_types (MutableSequence[google.maps.fleetengine_v1.types.TripType]):
            Trip types supported by this vehicle.
        current_trips (MutableSequence[str]):
            Output only. List of ``trip_id``'s for trips currently
            assigned to this vehicle.
        last_location (google.maps.fleetengine_v1.types.VehicleLocation):
            Last reported location of the vehicle.
        past_locations (MutableSequence[google.maps.fleetengine_v1.types.VehicleLocation]):
            Input only. Locations where this vehicle has been in the
            past that haven't yet been reported to Fleet Engine. This is
            used in ``UpdateVehicleRequest`` to record locations which
            were previously unable to be sent to the server. Typically
            this happens when the vehicle does not have internet
            connectivity.
        maximum_capacity (int):
            The total numbers of riders this vehicle can
            carry.  The driver is not considered in this
            value. This value must be greater than or equal
            to one.
        attributes (MutableSequence[google.maps.fleetengine_v1.types.VehicleAttribute]):
            List of vehicle attributes. A vehicle can
            have at most 100 attributes, and each attribute
            must have a unique key.
        vehicle_type (google.maps.fleetengine_v1.types.Vehicle.VehicleType):
            Required. The type of this vehicle. Can be used to filter
            vehicles in ``SearchVehicles`` results. Also influences ETA
            and route calculations.
        license_plate (google.maps.fleetengine_v1.types.LicensePlate):
            License plate information for the vehicle.
        route (MutableSequence[google.maps.fleetengine_v1.types.TerminalLocation]):
            Deprecated: Use ``Vehicle.waypoints`` instead.
        current_route_segment (str):
            The polyline specifying the route the driver app intends to
            take to the next waypoint. This list is also returned in
            ``Trip.current_route_segment`` for all active trips assigned
            to the vehicle.

            Note: This field is intended only for use by the Driver SDK.
            Decoding is not yet supported.
        current_route_segment_traffic (google.maps.fleetengine_v1.types.TrafficPolylineData):
            Input only. Fleet Engine uses this
            information to improve journey sharing. Note:
            This field is intended only for use by the
            Driver SDK.
        current_route_segment_version (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when ``current_route_segment`` was set. It
            can be stored by the client and passed in future
            ``GetVehicle`` requests to prevent returning routes that
            haven't changed.
        current_route_segment_end_point (google.maps.fleetengine_v1.types.TripWaypoint):
            The waypoint where ``current_route_segment`` ends. This can
            be supplied by drivers on ``UpdateVehicle`` calls either as
            a full trip waypoint, a waypoint ``LatLng``, or as the last
            ``LatLng`` of the ``current_route_segment``. Fleet Engine
            will then do its best to interpolate to an actual waypoint
            if it is not fully specified. This field is ignored in
            ``UpdateVehicle`` calls unless ``current_route_segment`` is
            also specified.
        remaining_distance_meters (google.protobuf.wrappers_pb2.Int32Value):
            The remaining driving distance for the
            ``current_route_segment``. This value is also returned in
            ``Trip.remaining_distance_meters`` for all active trips
            assigned to the vehicle. The value is unspecified if the
            ``current_route_segment`` field is empty.
        eta_to_first_waypoint (google.protobuf.timestamp_pb2.Timestamp):
            The ETA to the first entry in the ``waypoints`` field. The
            value is unspecified if the ``waypoints`` field is empty or
            the ``Vehicle.current_route_segment`` field is empty.

            When updating a vehicle, ``remaining_time_seconds`` takes
            precedence over ``eta_to_first_waypoint`` in the same
            request.
        remaining_time_seconds (google.protobuf.wrappers_pb2.Int32Value):
            Input only. The remaining driving time for the
            ``current_route_segment``. The value is unspecified if the
            ``waypoints`` field is empty or the
            ``Vehicle.current_route_segment`` field is empty. This value
            should match ``eta_to_first_waypoint`` - ``current_time`` if
            all parties are using the same clock.

            When updating a vehicle, ``remaining_time_seconds`` takes
            precedence over ``eta_to_first_waypoint`` in the same
            request.
        waypoints (MutableSequence[google.maps.fleetengine_v1.types.TripWaypoint]):
            The remaining waypoints assigned to this
            Vehicle.
        waypoints_version (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Last time the ``waypoints`` field was updated.
            Clients should cache this value and pass it in
            ``GetVehicleRequest`` to ensure the ``waypoints`` field is
            only returned if it is updated.
        back_to_back_enabled (bool):
            Indicates if the driver accepts back-to-back trips. If
            ``true``, ``SearchVehicles`` may include the vehicle even if
            it is currently assigned to a trip. The default value is
            ``false``.
        navigation_status (google.maps.fleetengine_v1.types.NavigationStatus):
            The vehicle's navigation status.
        device_settings (google.maps.fleetengine_v1.types.DeviceSettings):
            Input only. Information about settings in the
            mobile device being used by the driver.
    """

    class VehicleType(proto.Message):
        r"""The type of vehicle.

        Attributes:
            category (google.maps.fleetengine_v1.types.Vehicle.VehicleType.Category):
                Vehicle type category
        """

        class Category(proto.Enum):
            r"""Vehicle type categories

            Values:
                UNKNOWN (0):
                    Default, used for unspecified or unrecognized
                    vehicle categories.
                AUTO (1):
                    An automobile.
                TAXI (2):
                    Any vehicle that acts as a taxi (typically
                    licensed or regulated).
                TRUCK (3):
                    Generally, a vehicle with a large storage
                    capacity.
                TWO_WHEELER (4):
                    A motorcycle, moped, or other two-wheeled
                    vehicle
                BICYCLE (5):
                    Human-powered transport.
                PEDESTRIAN (6):
                    A human transporter, typically walking or
                    running, traveling along pedestrian pathways.
            """

            UNKNOWN = 0
            AUTO = 1
            TAXI = 2
            TRUCK = 3
            TWO_WHEELER = 4
            BICYCLE = 5
            PEDESTRIAN = 6

        category: "Vehicle.VehicleType.Category" = proto.Field(
            proto.ENUM,
            number=1,
            enum="Vehicle.VehicleType.Category",
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    vehicle_state: "VehicleState" = proto.Field(
        proto.ENUM,
        number=2,
        enum="VehicleState",
    )
    supported_trip_types: MutableSequence[fleetengine.TripType] = proto.RepeatedField(
        proto.ENUM,
        number=3,
        enum=fleetengine.TripType,
    )
    current_trips: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    last_location: fleetengine.VehicleLocation = proto.Field(
        proto.MESSAGE,
        number=5,
        message=fleetengine.VehicleLocation,
    )
    past_locations: MutableSequence[fleetengine.VehicleLocation] = proto.RepeatedField(
        proto.MESSAGE,
        number=30,
        message=fleetengine.VehicleLocation,
    )
    maximum_capacity: int = proto.Field(
        proto.INT32,
        number=6,
    )
    attributes: MutableSequence[fleetengine.VehicleAttribute] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message=fleetengine.VehicleAttribute,
    )
    vehicle_type: VehicleType = proto.Field(
        proto.MESSAGE,
        number=9,
        message=VehicleType,
    )
    license_plate: "LicensePlate" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="LicensePlate",
    )
    route: MutableSequence[fleetengine.TerminalLocation] = proto.RepeatedField(
        proto.MESSAGE,
        number=12,
        message=fleetengine.TerminalLocation,
    )
    current_route_segment: str = proto.Field(
        proto.STRING,
        number=20,
    )
    current_route_segment_traffic: "TrafficPolylineData" = proto.Field(
        proto.MESSAGE,
        number=28,
        message="TrafficPolylineData",
    )
    current_route_segment_version: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=15,
        message=timestamp_pb2.Timestamp,
    )
    current_route_segment_end_point: fleetengine.TripWaypoint = proto.Field(
        proto.MESSAGE,
        number=24,
        message=fleetengine.TripWaypoint,
    )
    remaining_distance_meters: wrappers_pb2.Int32Value = proto.Field(
        proto.MESSAGE,
        number=18,
        message=wrappers_pb2.Int32Value,
    )
    eta_to_first_waypoint: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=19,
        message=timestamp_pb2.Timestamp,
    )
    remaining_time_seconds: wrappers_pb2.Int32Value = proto.Field(
        proto.MESSAGE,
        number=25,
        message=wrappers_pb2.Int32Value,
    )
    waypoints: MutableSequence[fleetengine.TripWaypoint] = proto.RepeatedField(
        proto.MESSAGE,
        number=22,
        message=fleetengine.TripWaypoint,
    )
    waypoints_version: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=16,
        message=timestamp_pb2.Timestamp,
    )
    back_to_back_enabled: bool = proto.Field(
        proto.BOOL,
        number=23,
    )
    navigation_status: fleetengine.NavigationStatus = proto.Field(
        proto.ENUM,
        number=26,
        enum=fleetengine.NavigationStatus,
    )
    device_settings: "DeviceSettings" = proto.Field(
        proto.MESSAGE,
        number=27,
        message="DeviceSettings",
    )


class BatteryInfo(proto.Message):
    r"""Information about the device's battery.

    Attributes:
        battery_status (google.maps.fleetengine_v1.types.BatteryStatus):
            Status of the battery, whether full or
            charging etc.
        power_source (google.maps.fleetengine_v1.types.PowerSource):
            Status of battery power source.
        battery_percentage (float):
            Current battery percentage [0-100].
    """

    battery_status: "BatteryStatus" = proto.Field(
        proto.ENUM,
        number=1,
        enum="BatteryStatus",
    )
    power_source: "PowerSource" = proto.Field(
        proto.ENUM,
        number=2,
        enum="PowerSource",
    )
    battery_percentage: float = proto.Field(
        proto.FLOAT,
        number=3,
    )


class DeviceSettings(proto.Message):
    r"""Information about various settings on the mobile device.

    Attributes:
        location_power_save_mode (google.maps.fleetengine_v1.types.LocationPowerSaveMode):
            How location features are set to behave on
            the device when battery saver is on.
        is_power_save_mode (bool):
            Whether the device is currently in power save
            mode.
        is_interactive (bool):
            Whether the device is in an interactive
            state.
        battery_info (google.maps.fleetengine_v1.types.BatteryInfo):
            Information about the battery state.
    """

    location_power_save_mode: "LocationPowerSaveMode" = proto.Field(
        proto.ENUM,
        number=1,
        enum="LocationPowerSaveMode",
    )
    is_power_save_mode: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    is_interactive: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    battery_info: "BatteryInfo" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="BatteryInfo",
    )


class LicensePlate(proto.Message):
    r"""The license plate information of the Vehicle.  To avoid
    storing personally-identifiable information, only the minimum
    information about the license plate is stored as part of the
    entity.

    Attributes:
        country_code (str):
            Required. CLDR Country/Region Code. For example, ``US`` for
            United States, or ``IN`` for India.
        last_character (str):
            The last digit of the license plate or "-1" to denote no
            numeric value is present in the license plate.

            - "ABC 1234" -> "4"
            - "AB 123 CD" -> "3"
            - "ABCDEF" -> "-1".
    """

    country_code: str = proto.Field(
        proto.STRING,
        number=1,
    )
    last_character: str = proto.Field(
        proto.STRING,
        number=2,
    )


class VisualTrafficReportPolylineRendering(proto.Message):
    r"""Describes how clients should color one portion of the
    polyline along the route.

    Attributes:
        road_stretch (MutableSequence[google.maps.fleetengine_v1.types.VisualTrafficReportPolylineRendering.RoadStretch]):
            Optional. Road stretches that should be
            rendered along the polyline. Stretches are
            guaranteed to not overlap, and do not
            necessarily span the full route.

            In the absence of a road stretch to style, the
            client should apply the default for the route.
    """

    class RoadStretch(proto.Message):
        r"""One road stretch that should be rendered.

        Attributes:
            style (google.maps.fleetengine_v1.types.VisualTrafficReportPolylineRendering.RoadStretch.Style):
                Required. The style to apply.
            offset_meters (int):
                Required. The style should be applied between
                ``[offset_meters, offset_meters + length_meters)``.
            length_meters (int):
                Required. The length of the path where to
                apply the style.
        """

        class Style(proto.Enum):
            r"""The traffic style, indicating traffic speed.

            Values:
                STYLE_UNSPECIFIED (0):
                    No style selected.
                SLOWER_TRAFFIC (1):
                    Traffic is slowing down.
                TRAFFIC_JAM (2):
                    There is a traffic jam.
            """

            STYLE_UNSPECIFIED = 0
            SLOWER_TRAFFIC = 1
            TRAFFIC_JAM = 2

        style: "VisualTrafficReportPolylineRendering.RoadStretch.Style" = proto.Field(
            proto.ENUM,
            number=1,
            enum="VisualTrafficReportPolylineRendering.RoadStretch.Style",
        )
        offset_meters: int = proto.Field(
            proto.INT32,
            number=2,
        )
        length_meters: int = proto.Field(
            proto.INT32,
            number=3,
        )

    road_stretch: MutableSequence[RoadStretch] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=RoadStretch,
    )


class TrafficPolylineData(proto.Message):
    r"""Traffic conditions along the expected vehicle route.

    Attributes:
        traffic_rendering (google.maps.fleetengine_v1.types.VisualTrafficReportPolylineRendering):
            A polyline rendering of how fast traffic is
            for all regions along one stretch of a customer
            ride.
    """

    traffic_rendering: "VisualTrafficReportPolylineRendering" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="VisualTrafficReportPolylineRendering",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
