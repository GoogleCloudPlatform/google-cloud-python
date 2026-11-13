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
import google.type.date_pb2 as date_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.devicesandservices.health.v4",
    manifest={
        "User",
        "Profile",
        "PairedDevice",
        "IrnProfile",
        "Settings",
        "Identity",
        "GetProfileRequest",
        "GetIrnProfileRequest",
        "UpdateProfileRequest",
        "GetSettingsRequest",
        "UpdateSettingsRequest",
        "GetIdentityRequest",
        "GetPairedDeviceRequest",
        "ListPairedDevicesRequest",
        "ListPairedDevicesResponse",
    },
)


class User(proto.Message):
    r"""Represents a user in the Google Health API.
    It matches the parent resource of collections owned by the user.

    Clients currently do not need to interact with this resource
    directly.

    Attributes:
        name (str):
            Identifier. The resource name of the user.

            The ``{user}`` ID is a system-generated identifier, as
            described in
            [Identity.health_user_id][google.devicesandservices.health.v4.Identity.health_user_id].

            Format: ``users/{user}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class Profile(proto.Message):
    r"""Profile details.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of this Profile resource.

            Format: ``users/{user}/profile`` Example:
            ``users/1234567890/profile`` or ``users/me/profile`` The
            {user} ID is a system-generated Google Health API user ID, a
            string of 1-63 characters consisting of lowercase and
            uppercase letters, numbers, and hyphens. The literal ``me``
            can also be used to refer to the authenticated user.

            This field is read-only.
        age (int):
            Optional. The age in years based on the
            user's birth date.
            Updates to this field are currently not
            supported.
        membership_start_date (google.type.date_pb2.Date):
            Output only. The date the user created their
            account.
            Updates to this field are currently not
            supported.
        user_configured_walking_stride_length_mm (int):
            Optional. The user's user configured walking stride length,
            in millimeters.

            The user must consent to the following access scope to
            access this field:

            -

            ``https://www.googleapis.com/auth/googlehealth.activity_and_fitness.readonly``

            This field is a member of `oneof`_ ``_user_configured_walking_stride_length_mm``.
        user_configured_running_stride_length_mm (int):
            Optional. The user's user configured running stride length,
            in millimeters.

            The user must consent to the following access scope to
            access this field:

            -

            ``https://www.googleapis.com/auth/googlehealth.activity_and_fitness.readonly``

            This field is a member of `oneof`_ ``_user_configured_running_stride_length_mm``.
        auto_walking_stride_length_mm (int):
            Output only. The automatically calculated walking stride
            length, in millimeters.

            The user must consent to the following access scope to
            access this field:

            -

            ``https://www.googleapis.com/auth/googlehealth.activity_and_fitness.readonly``

            This field is a member of `oneof`_ ``_auto_walking_stride_length_mm``.
        auto_running_stride_length_mm (int):
            Output only. The automatically calculated running stride
            length, in millimeters.

            The user must consent to the following access scope to
            access this field:

            -

            ``https://www.googleapis.com/auth/googlehealth.activity_and_fitness.readonly``

            This field is a member of `oneof`_ ``_auto_running_stride_length_mm``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    age: int = proto.Field(
        proto.INT32,
        number=6,
    )
    membership_start_date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=9,
        message=date_pb2.Date,
    )
    user_configured_walking_stride_length_mm: int = proto.Field(
        proto.INT32,
        number=13,
        optional=True,
    )
    user_configured_running_stride_length_mm: int = proto.Field(
        proto.INT32,
        number=14,
        optional=True,
    )
    auto_walking_stride_length_mm: int = proto.Field(
        proto.INT32,
        number=15,
        optional=True,
    )
    auto_running_stride_length_mm: int = proto.Field(
        proto.INT32,
        number=16,
        optional=True,
    )


class PairedDevice(proto.Message):
    r"""User's Paired 1P Device

    The PairedDevice details include information about the device
    type, battery status, battery level, last sync time, device
    version, mac address, and features.

    Attributes:
        name (str):
            Identifier. The resource name of this Device resource.

            Format: ``users/{user}/pairedDevices/{paired_device}``
            Example: ``users/1234567890/pairedDevices/123`` or
            ``users/me/pairedDevices/123``
        device_type (google.devicesandservices.health_v4.types.PairedDevice.DeviceType):
            Output only. The device type. Supported: TRACKER \| SCALE
        battery_status (str):
            Output only. The battery status of the device. Supported:
            High \| Medium \| Low \| Empty
        battery_level (int):
            Output only. The battery level of the device.
        last_sync_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time of last sync with the
            Fitbit mobile application.
        device_version (str):
            Output only. The product name of the device
        mac_address (str):
            Output only. Mac ID number of the device.
        features (MutableSequence[str]):
            Output only. Lists of unique features supported by the
            device.

            Comprehensive list of supported features:

            **Fitness Tracking**

            - ``ACTIVE_MINUTES``: Legacy active minutes.
            - ``AUTOSTRIDE``: Automatic stride length calculation.
            - ``BIKE_ONBOARDING``: Cycling UI support.
            - ``CALORIES``: Daily burned calories.
            - ``DISTANCE``: Daily distance tracking.
            - ``ELEVATION``: Floors climbed.
            - ``INACTIVITY_ALERTS``: Reminders to move.
            - ``SEDENTARY_TIME``: Tracks inactive time.
            - ``STEPS``: Daily steps.
            - ``SWIM``: Swim tracking (laps/strokes).
            - ``AUTORUN``: Automatic run detection.
            - ``ACTIVE_ZONE_MINUTES``: Active Zone Minutes (AZM).

            **Heart Rate & Health**

            - ``HEART_RATE``: Continuous heart rate (PPG).
            - ``BAT_SIGNAL``: High/Low Heart Rate Alerts.

            **Advanced Sensors**

            - ``SPO2``: Blood oxygen saturation.
            - ``NIGHTTIME_OXYGEN_SATURATION``: Sleep SpO2.
            - ``ESTIMATED_OXYGEN_VARIATION``: Estimated Oxygen
              Variation.
            - ``EDA``: Electrodermal Activity (stress).
            - ``SKIN_TEMPERATURE``: Skin temperature variation.
            - ``INTERNAL_DEVICE_TEMPERATURE``: Internal device
              temperature.

            **Sleep & Wellness**

            - ``SLEEP``: Basic sleep tracking.
            - ``SMART_SLEEP``: Advanced sleep tracking (stages/score).
            - ``BEDTIME_REMINDER``: Bedtime reminders.
            - ``SOUNDSCAPE``: Snore and noise detection.

            **Advanced Workouts**

            - ``WB``: Custom Workout Builder.
            - ``AUTOCUES``: Auto Cues / Auto Lap.
            - ``DWR_RUN``: Daily Run Recommendations.
            - ``ADVANCED_RUNNING``: Advanced Running Dynamics (e.g.,
              GCT, VO).

            **GPS & Location**

            - ``GPS``: Built-in GPS.
            - ``CONNECTED_GPS``: Connected GPS (uses phone).
            - ``LOCATION_HINT``: Location helper.

            **Payments & NFC**

            - ``PAYMENTS``: NFC payments (Fitbit Pay/Google Wallet).
            - ``FELICA``: FeliCa support (Japan payments/transit).

            **Activity Detection**

            - ``GROK``: SmartTrack automatic activity detection.
            - ``RETRO_AR``: Retroactive Activity Recognition prompts.

            **Smart Features & UI**

            - ``ALARMS``: Silent alarms.
            - ``BLE_MUSIC_CONTROL``: BLE music control.
            - ``MUSIC``: Direct music storage/control.
            - ``YOUTUBE_MUSIC_SUPPORTED``: YouTube Music support.
            - ``GALLERY``: App Gallery.
            - ``TUTORIAL_SUPPORTED``: On-screen tutorials.
            - ``SMILEY_EMOTE``: Legacy Zip face.
            - ``MOBILE_TO_DEVICE_DEEPLINK``: Mobile to device settings
              deep link.
            - ``HIDE_GALLERY``: Option to hide Gallery.
            - ``HIDE_GOAL_SELECTION``: Option to hide goal selection.
            - ``DIGITAL_WARRANTY_SUPPORTED``: Digital warranty display.
            - ``DIRECT_DEVICE_SETTINGS_SUPPORTED``: Direct device
              settings management.

            **Gym HR Broadcasting**

            - ``ASPEN_SUPPORTED``: Broadcast HR to gym equipment.
            - ``ASPEN_REMOTE_UI_SUPPORTED``: Remote UI for HR sharing.

            **Privacy & Security**

            - ``FINITE_IMPROBABILITY``: BLE Resolvable Private Address
              (RPA) privacy.
            - ``DOMAIN_KEY_SYNC``: Domain key synchronization.

            **BLE Protocol**

            - ``BONDING``: Secure BLE bonding.
            - ``ADVERTISES_SERIAL``: Advertises serial number.
            - ``STATUS_CHARACTERISTIC``: BLE Status Characteristic.
            - ``TRACKER_CHANNEL_CHARACTERISTIC``: BLE Tracker Channel
              Characteristic.
            - ``PING_CHARACTERISTIC``: BLE Ping Characteristic.

            **Cellular & Wi-Fi**

            - ``MOBILE_DATA``: LTE cellular support.
            - ``SINGLE_AP_WIFI``: Single AP Wi-Fi.
            - ``MULTI_AP_WIFI``: Multi AP Wi-Fi.
            - ``WIFI_FWUP``: Firmware updates over Wi-Fi.

            **Data Sync & Transfer**

            - ``APP_SYNC``: Background app sync.
            - ``LIVE_DATA``: Real-time data streaming.
            - ``EVENT_BASED_SYNC_SUPPORTED``: Event-based sync.
            - ``TIME_SERVICE``: Time synchronization service.
            - ``REMOTE_FILE_PROVIDER``: Remote file transfer.
            - ``DIRECT_COMMS_ALARMS``: Direct communication for alarms.
            - ``DIRECT_COMMS_EXERCISE``: Direct communication for
              exercise.
            - ``DIRECT_COMMS_BATTERY_ALERTS``: Direct communication for
              battery alerts.

            **Google Integrations**

            - ``PARROT_TREE_SUPPORTED``: Find My Device support.
    """

    class DeviceType(proto.Enum):
        r"""The type of device.

        Values:
            DEVICE_TYPE_UNSPECIFIED (0):
                Device type is not specified.
            TRACKER (1):
                Device type is tracker.
            SCALE (2):
                Device type is scale.
        """

        DEVICE_TYPE_UNSPECIFIED = 0
        TRACKER = 1
        SCALE = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    device_type: DeviceType = proto.Field(
        proto.ENUM,
        number=3,
        enum=DeviceType,
    )
    battery_status: str = proto.Field(
        proto.STRING,
        number=4,
    )
    battery_level: int = proto.Field(
        proto.INT32,
        number=5,
    )
    last_sync_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    device_version: str = proto.Field(
        proto.STRING,
        number=7,
    )
    mac_address: str = proto.Field(
        proto.STRING,
        number=8,
    )
    features: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=9,
    )


class IrnProfile(proto.Message):
    r"""Irregular Rhythm Notifications (IRN) Profile details.

    The Irregular Rhythm Notifications (IRN) feature checks for
    signs of atrial fibrillation (AFib). The IrnProfile details
    include information about the user's onboarding status,
    enrollment status, and the last update time of analyzable data
    for this feature.

    Attributes:
        name (str):
            Identifier. The resource name of this IrnProfile resource.

            Format: ``users/{user}/irnProfile`` Example:
            ``users/1234567890/irnProfile`` or ``users/me/irnProfile``
            The {user} ID is a system-generated Google Health API user
            ID, a string of 1-63 characters consisting of lowercase and
            uppercase letters, numbers, and hyphens. The literal ``me``
            can also be used to refer to the authenticated user.
        onboarding_status (bool):
            Required. Whether or not the user has
            onboarded onto the IRN feature.
        enrollment_status (bool):
            Required. Whether or not the user is
            currently enrolled in having their data
            processed for IRN alerts.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp of the last piece
            of analyzable data synced by the user.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    onboarding_status: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    enrollment_status: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )


class Settings(proto.Message):
    r"""Settings details.

    Attributes:
        name (str):
            Identifier. The resource name of this Settings resource.

            Format: ``users/{user}/settings`` Example:
            ``users/1234567890/settings`` or ``users/me/settings`` The
            {user} ID is a system-generated Google Health API user ID, a
            string of 1-63 characters consisting of lowercase and
            uppercase letters, numbers, and hyphens. The literal ``me``
            can also be used to refer to the authenticated user.

            This field is read-only.
        auto_stride_enabled (bool):
            Optional. True if the user's stride length is
            determined automatically.
            Updates to this field are currently not
            supported.
        distance_unit (google.devicesandservices.health_v4.types.Settings.DistanceUnit):
            Optional. The measurement unit defined in the
            user's account settings.
        glucose_unit (google.devicesandservices.health_v4.types.Settings.GlucoseUnit):
            Optional. The measurement unit defined in the
            user's account settings.
        height_unit (google.devicesandservices.health_v4.types.Settings.HeightUnit):
            Optional. The measurement unit defined in the
            user's account settings.
        language_locale (str):
            Optional. The locale defined in the user's
            account settings.
            Updates to this field are currently not
            supported.
        utc_offset (google.protobuf.duration_pb2.Duration):
            Optional. The user's timezone offset relative
            to UTC.
            Updates to this field are currently not
            supported.
        stride_length_walking_type (google.devicesandservices.health_v4.types.Settings.StrideLengthType):
            Optional. The stride length type defined in
            the user's account settings for walking.

            Updates to this field are currently not
            supported.
        stride_length_running_type (google.devicesandservices.health_v4.types.Settings.StrideLengthType):
            Optional. The stride length type defined in
            the user's account settings for running.

            Updates to this field are currently not
            supported.
        swim_unit (google.devicesandservices.health_v4.types.Settings.SwimUnit):
            Optional. The measurement unit defined in the
            user's account settings.
        temperature_unit (google.devicesandservices.health_v4.types.Settings.TemperatureUnit):
            Optional. The measurement unit defined in the
            user's account settings.
        time_zone (str):
            Optional. The timezone defined in the user's account
            settings. This follows the IANA `Time Zone
            Database <https://www.iana.org/time-zones>`__.

            Updates to this field are currently not supported.
        weight_unit (google.devicesandservices.health_v4.types.Settings.WeightUnit):
            Optional. The measurement unit defined in the
            user's account settings.
        water_unit (google.devicesandservices.health_v4.types.Settings.WaterUnit):
            Optional. The measurement unit defined in the
            user's account settings.
        food_language_code (str):
            Output only. The food language code derived from the user's
            food database. Possible values: ``'en-US'``, ``'en-GB'``,
            ``'de-DE'``, ``'es-ES'``, ``'fr-FR'``, ``'zh-CN'``,
            ``'zh-TW'``, ``'ja-JP'``, ``'en-AU'``, ``'en-CA'``,
            ``'it-IT'``, ``'ko-KR'``, ``'es-MX'``, ``'en-IN'``,
            ``'en-SG'``, ``'en-PH'``, ``'en-IE'``, ``'fr-CA'``.

            Updates to this field are currently not supported.
    """

    class DistanceUnit(proto.Enum):
        r"""The measurement unit defined in the user's account settings.

        Values:
            DISTANCE_UNIT_UNSPECIFIED (0):
                Distance unit is not specified.
            DISTANCE_UNIT_MILES (1):
                Distance unit is miles.
            DISTANCE_UNIT_KILOMETERS (2):
                Distance unit is kilometers.
        """

        DISTANCE_UNIT_UNSPECIFIED = 0
        DISTANCE_UNIT_MILES = 1
        DISTANCE_UNIT_KILOMETERS = 2

    class GlucoseUnit(proto.Enum):
        r"""The measurement unit defined in the user's account settings.

        Values:
            GLUCOSE_UNIT_UNSPECIFIED (0):
                Glucose unit is not specified.
            GLUCOSE_UNIT_MG_DL (1):
                Glucose unit is mg/dL.
            GLUCOSE_UNIT_MMOL_L (2):
                Glucose unit is mmol/l.
        """

        GLUCOSE_UNIT_UNSPECIFIED = 0
        GLUCOSE_UNIT_MG_DL = 1
        GLUCOSE_UNIT_MMOL_L = 2

    class HeightUnit(proto.Enum):
        r"""The measurement unit defined in the user's account settings.

        Values:
            HEIGHT_UNIT_UNSPECIFIED (0):
                Height unit is not specified.
            HEIGHT_UNIT_INCHES (1):
                Height unit is inches.
            HEIGHT_UNIT_CENTIMETERS (2):
                Height unit is cm.
        """

        HEIGHT_UNIT_UNSPECIFIED = 0
        HEIGHT_UNIT_INCHES = 1
        HEIGHT_UNIT_CENTIMETERS = 2

    class StrideLengthType(proto.Enum):
        r"""The stride length type defined in the user's account
        settings. Specifies if the user's stride length is determined
        automatically (default) or manually as defined in the user's
        account settings.

        Values:
            STRIDE_LENGTH_TYPE_UNSPECIFIED (0):
                Stride length type is not specified.
            STRIDE_LENGTH_TYPE_DEFAULT (1):
                Stride length type is computed based on the
                user's gender and height.
            STRIDE_LENGTH_TYPE_MANUAL (2):
                Stride length type is manually set by the
                user.
            STRIDE_LENGTH_TYPE_AUTO (3):
                Stride length type is determined
                automatically.
        """

        STRIDE_LENGTH_TYPE_UNSPECIFIED = 0
        STRIDE_LENGTH_TYPE_DEFAULT = 1
        STRIDE_LENGTH_TYPE_MANUAL = 2
        STRIDE_LENGTH_TYPE_AUTO = 3

    class SwimUnit(proto.Enum):
        r"""The swim unit defined in the user's account settings.

        Values:
            SWIM_UNIT_UNSPECIFIED (0):
                Swim unit is not specified.
            SWIM_UNIT_METERS (1):
                Swim unit is meters.
            SWIM_UNIT_YARDS (2):
                Swim unit is yards.
        """

        SWIM_UNIT_UNSPECIFIED = 0
        SWIM_UNIT_METERS = 1
        SWIM_UNIT_YARDS = 2

    class TemperatureUnit(proto.Enum):
        r"""The measurement unit defined in the user's account settings.

        Values:
            TEMPERATURE_UNIT_UNSPECIFIED (0):
                Temperature unit is not specified.
            TEMPERATURE_UNIT_CELSIUS (1):
                Temperature unit is Celsius.
            TEMPERATURE_UNIT_FAHRENHEIT (2):
                Temperature unit is Fahrenheit.
        """

        TEMPERATURE_UNIT_UNSPECIFIED = 0
        TEMPERATURE_UNIT_CELSIUS = 1
        TEMPERATURE_UNIT_FAHRENHEIT = 2

    class WeightUnit(proto.Enum):
        r"""The measurement unit defined in the user's account settings.

        Values:
            WEIGHT_UNIT_UNSPECIFIED (0):
                Weight unit is not specified.
            WEIGHT_UNIT_POUNDS (1):
                Weight unit is pounds.
            WEIGHT_UNIT_STONE (2):
                Weight unit is stones.
            WEIGHT_UNIT_KILOGRAMS (3):
                Weight unit is kilograms.
        """

        WEIGHT_UNIT_UNSPECIFIED = 0
        WEIGHT_UNIT_POUNDS = 1
        WEIGHT_UNIT_STONE = 2
        WEIGHT_UNIT_KILOGRAMS = 3

    class WaterUnit(proto.Enum):
        r"""The water measurement unit defined in the user's account
        settings.

        Values:
            WATER_UNIT_UNSPECIFIED (0):
                Water unit is not specified.
            WATER_UNIT_ML (1):
                Water unit is milliliters.
            WATER_UNIT_FL_OZ (2):
                Water unit is fluid ounces.
            WATER_UNIT_CUP (3):
                Water unit is cups.
        """

        WATER_UNIT_UNSPECIFIED = 0
        WATER_UNIT_ML = 1
        WATER_UNIT_FL_OZ = 2
        WATER_UNIT_CUP = 3

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    auto_stride_enabled: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    distance_unit: DistanceUnit = proto.Field(
        proto.ENUM,
        number=5,
        enum=DistanceUnit,
    )
    glucose_unit: GlucoseUnit = proto.Field(
        proto.ENUM,
        number=7,
        enum=GlucoseUnit,
    )
    height_unit: HeightUnit = proto.Field(
        proto.ENUM,
        number=8,
        enum=HeightUnit,
    )
    language_locale: str = proto.Field(
        proto.STRING,
        number=9,
    )
    utc_offset: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=10,
        message=duration_pb2.Duration,
    )
    stride_length_walking_type: StrideLengthType = proto.Field(
        proto.ENUM,
        number=13,
        enum=StrideLengthType,
    )
    stride_length_running_type: StrideLengthType = proto.Field(
        proto.ENUM,
        number=14,
        enum=StrideLengthType,
    )
    swim_unit: SwimUnit = proto.Field(
        proto.ENUM,
        number=15,
        enum=SwimUnit,
    )
    temperature_unit: TemperatureUnit = proto.Field(
        proto.ENUM,
        number=16,
        enum=TemperatureUnit,
    )
    time_zone: str = proto.Field(
        proto.STRING,
        number=17,
    )
    weight_unit: WeightUnit = proto.Field(
        proto.ENUM,
        number=18,
        enum=WeightUnit,
    )
    water_unit: WaterUnit = proto.Field(
        proto.ENUM,
        number=19,
        enum=WaterUnit,
    )
    food_language_code: str = proto.Field(
        proto.STRING,
        number=20,
    )


class Identity(proto.Message):
    r"""Represents details about the Google user's identity.

    Attributes:
        name (str):
            Identifier. The resource name of this Identity resource.
            Format: ``users/me/identity``
        legacy_user_id (str):
            Output only. The legacy Fitbit User identifier. This is the
            Fitbit ID used in the legacy Fitbit APIs (v1-v3). It can be
            referenced by clients migrating from the legacy Fitbit APIs
            to map their existing identifiers to the new Google user ID.

            It **must not** be used for any other purpose. It is not of
            any use for new clients using only the Google Health APIs.

            Valid values are strings of 1-63 characters, and valid
            characters are lowercase and uppercase letters, numbers, and
            hyphens.
        health_user_id (str):
            Output only. The Google User Identifier in the Google Health
            APIs. It matches the ``{user}`` resource ID segment in the
            resource name paths, e.g. ``users/{user}/dataTypes/steps``.

            Valid values are strings of 1-63 characters, and valid
            characters are lowercase and uppercase letters, numbers, and
            hyphens.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    legacy_user_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    health_user_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class GetProfileRequest(proto.Message):
    r"""Request message for getting Profile details.

    Attributes:
        name (str):
            Required. The name of the Profile. Format:
            ``users/me/profile``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetIrnProfileRequest(proto.Message):
    r"""Request message for getting IRN Profile details.

    Attributes:
        name (str):
            Required. The resource name of the IRN Profile. Format:
            ``users/{user}/irnProfile`` Example:
            ``users/1234567890/irnProfile`` or ``users/me/irnProfile``
            The {user} ID is a system-generated Google Health API user
            ID, a string of 1-63 characters consisting of lowercase and
            uppercase letters, numbers, and hyphens. The literal ``me``
            can also be used to refer to the authenticated user.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateProfileRequest(proto.Message):
    r"""Request message for updating Profile details.

    Attributes:
        profile (google.devicesandservices.health_v4.types.Profile):
            Required. Profile details.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to be updated.
    """

    profile: "Profile" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Profile",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class GetSettingsRequest(proto.Message):
    r"""Request message for getting Settings details.

    Attributes:
        name (str):
            Required. The name of the Settings. Format:
            ``users/me/settings``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateSettingsRequest(proto.Message):
    r"""Request message for updating Settings details.

    Attributes:
        settings (google.devicesandservices.health_v4.types.Settings):
            Required. Settings details
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to be updated.
    """

    settings: "Settings" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Settings",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class GetIdentityRequest(proto.Message):
    r"""Request message for getting Identity details.

    Attributes:
        name (str):
            Required. The resource name of the Identity. Format:
            ``users/me/identity``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetPairedDeviceRequest(proto.Message):
    r"""Request message for getting a Device.

    Attributes:
        name (str):
            Required. The name of the device to retrieve.
            Format: users/{user}/devices/{device}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListPairedDevicesRequest(proto.Message):
    r"""Request message for listing Devices.

    Attributes:
        parent (str):
            Required. The parent, which owns this
            collection of devices. Format: users/{user}
        page_size (int):
            Optional. The maximum number of devices to
            return. The service may return fewer than this
            value. If unspecified, at most 5 devices will be
            returned. The maximum value is 100. values above
            100 will be coerced to 100.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListPairedDevices`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListPairedDevices`` must match the call that provided the
            page token.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListPairedDevicesResponse(proto.Message):
    r"""Response message for ListPairedDevices.

    Attributes:
        paired_devices (MutableSequence[google.devicesandservices.health_v4.types.PairedDevice]):
            The paired devices of the user.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    paired_devices: MutableSequence["PairedDevice"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="PairedDevice",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
