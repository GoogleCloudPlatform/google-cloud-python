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
import google.type.date_pb2 as date_pb2  # type: ignore
import proto  # type: ignore

from google.devicesandservices.health_v4.types import data_coordinates
from google.devicesandservices.health_v4.types import (
    medical_device_info as gdh_medical_device_info,
)

__protobuf__ = proto.module(
    package="google.devicesandservices.health.v4",
    manifest={
        "HeartRateZoneType",
        "FoodAccessLevel",
        "MealType",
        "EnergyUnit",
        "Nutrient",
        "WeightUnit",
        "VolumeUnit",
        "OvulationTestResult",
        "ActiveZoneMinutes",
        "ActiveZoneMinutesRollupValue",
        "ActiveMinutes",
        "ActiveMinutesRollupValue",
        "ActivityLevel",
        "ActivityLevelRollupValue",
        "Altitude",
        "BasalEnergyBurned",
        "BodyFat",
        "BodyFatRollupValue",
        "CoreBodyTemperature",
        "CoreBodyTemperatureRollupValue",
        "CaloriesInHeartRateZoneRollupValue",
        "DailyHeartRateZones",
        "DailyHeartRateVariability",
        "DailyRespiratoryRate",
        "DailyOxygenSaturation",
        "DailyRestingHeartRate",
        "DailySleepTemperatureDerivations",
        "DailyVO2Max",
        "Distance",
        "DistanceRollupValue",
        "Electrocardiogram",
        "Exercise",
        "Floors",
        "FloorsRollupValue",
        "AltitudeRollupValue",
        "HeartRate",
        "HeartRateRollupValue",
        "RunVO2MaxRollupValue",
        "RunVO2Max",
        "HeartRateVariabilityPersonalRangeRollupValue",
        "Height",
        "HeartRateVariability",
        "VolumeQuantity",
        "HydrationLog",
        "HydrationLogRollupValue",
        "IrregularRhythmNotification",
        "MetricsSummary",
        "WeightQuantity",
        "EnergyQuantity",
        "NutrientQuantity",
        "NutritionLog",
        "Food",
        "NutritionLogRollupValue",
        "OxygenSaturation",
        "RestingHeartRatePersonalRangeRollupValue",
        "FoodMeasurementUnit",
        "RespiratoryRateSleepSummary",
        "Sleep",
        "Steps",
        "StepsRollupValue",
        "SwimLengthsData",
        "SwimLengthsDataRollupValue",
        "TimeInHeartRateZone",
        "TimeInHeartRateZoneRollupValue",
        "TotalCaloriesRollupValue",
        "VO2Max",
        "Weight",
        "WeightRollupValue",
        "BloodGlucose",
        "BloodGlucoseRollupValue",
        "SedentaryPeriod",
        "SedentaryPeriodRollupValue",
        "ActiveEnergyBurned",
        "ActiveEnergyBurnedRollupValue",
        "MenstrualPeriod",
        "OvulationTest",
        "Symptoms",
        "Moods",
    },
)


class HeartRateZoneType(proto.Enum):
    r"""The heart rate zone type.

    Values:
        HEART_RATE_ZONE_TYPE_UNSPECIFIED (0):
            Unspecified heart rate zone.
        LIGHT (1):
            The light heart rate zone.
        MODERATE (2):
            The moderate heart rate zone.
        VIGOROUS (3):
            The vigorous heart rate zone.
        PEAK (4):
            The peak heart rate zone.
    """

    HEART_RATE_ZONE_TYPE_UNSPECIFIED = 0
    LIGHT = 1
    MODERATE = 2
    VIGOROUS = 3
    PEAK = 4


class FoodAccessLevel(proto.Enum):
    r"""Enum representing the access level of a food item.

    Values:
        FOOD_ACCESS_LEVEL_UNSPECIFIED (0):
            Unspecified food access level.
        FOOD_ACCESS_LEVEL_PUBLIC (1):
            Public food access level.
        FOOD_ACCESS_LEVEL_PRIVATE (2):
            Private food access level.
    """

    FOOD_ACCESS_LEVEL_UNSPECIFIED = 0
    FOOD_ACCESS_LEVEL_PUBLIC = 1
    FOOD_ACCESS_LEVEL_PRIVATE = 2


class MealType(proto.Enum):
    r"""Enum representing the meal type.

    Values:
        MEAL_TYPE_UNSPECIFIED (0):
            Unspecified meal type.
        BEFORE_BREAKFAST (1):
            Value representing a meal before breakfast.
        BREAKFAST (2):
            Value representing a breakfast.
        BEFORE_LUNCH (3):
            Value representing a morning snack.
        LUNCH (4):
            Value representing a lunch.
        BEFORE_DINNER (5):
            Value representing an afternoon snack.
        DINNER (6):
            Value representing dinner.
        AFTER_DINNER (7):
            Value representing an evening snack.
        SNACK (8):
            Value representing any meal outside of the
            usual three meals per day.
        ANYTIME (9):
            Value representing any time (legacy NA).
    """

    MEAL_TYPE_UNSPECIFIED = 0
    BEFORE_BREAKFAST = 1
    BREAKFAST = 2
    BEFORE_LUNCH = 3
    LUNCH = 4
    BEFORE_DINNER = 5
    DINNER = 6
    AFTER_DINNER = 7
    SNACK = 8
    ANYTIME = 9


class EnergyUnit(proto.Enum):
    r"""Enum representing the unit of energy.

    Values:
        ENERGY_UNIT_UNSPECIFIED (0):
            Unspecified energy unit.
        JOULE (1):
            Value representing joule.
        KILOJOULE (2):
            Value representing kilojoule.
        KILOCALORIE (3):
            Value representing kilocalorie.
        SMALL_CALORIE (4):
            Value representing small calorie.
        CALORIE (5):
            Value representing calorie.
    """

    ENERGY_UNIT_UNSPECIFIED = 0
    JOULE = 1
    KILOJOULE = 2
    KILOCALORIE = 3
    SMALL_CALORIE = 4
    CALORIE = 5


class Nutrient(proto.Enum):
    r"""Holds information about a user logged food.

    Values:
        NUTRIENT_UNSPECIFIED (0):
            Unspecified nutrient.
        BIOTIN (1):
            Value representing biotin nutrient.
        CAFFEINE (2):
            Value representing caffeine nutrient.
        CALCIUM (3):
            Value representing calcium nutrient.
        CHLORIDE (4):
            Value representing chloride nutrient.
        CARBOHYDRATES (5):
            Value representing carbohydrates nutrient.
        CHOLESTEROL (6):
            Value representing cholesterol nutrient.
        CHROMIUM (7):
            Value representing chromium nutrient.
        COPPER (8):
            Value representing copper nutrient.
        DIETARY_FIBER (9):
            Value representing dietary fiber nutrient.
        FOLIC_ACID (10):
            Value representing folic acid nutrient.
        IODINE (11):
            Value representing iodine nutrient.
        IRON (12):
            Value representing iron nutrient.
        MAGNESIUM (13):
            Value representing magnesium nutrient.
        MANGANESE (14):
            Value representing manganese nutrient.
        MOLYBDENUM (15):
            Value representing molybdenum nutrient.
        MONOUNSATURATED_FAT (16):
            Value representing monounsaturated fat
            nutrient.
        NIACIN (17):
            Value representing niacin nutrient.
        PANTOTHENIC_ACID (18):
            Value representing pantothenic acid nutrient.
        PHOSPHORUS (19):
            Value representing phosphorus nutrient.
        POLYUNSATURATED_FAT (20):
            Value representing polyunsaturated fat
            nutrient.
        POTASSIUM (21):
            Value representing potassium nutrient.
        PROTEIN (22):
            Value representing protein nutrient.
        RIBOFLAVIN (23):
            Value representing riboflavin nutrient.
        SATURATED_FAT (24):
            Value representing saturated fat nutrient.
        SELENIUM (25):
            Value representing selenium nutrient.
        SODIUM (26):
            Value representing sodium nutrient.
        SUGAR (27):
            Value representing sugar nutrient.
        THIAMIN (28):
            Value representing thiamin nutrient.
        TRANS_FAT (29):
            Value representing trans fat nutrient.
        UNSATURATED_FAT (30):
            Value representing unsaturated fat nutrient.
        VITAMIN_A (31):
            Value representing vitamin A nutrient.
        VITAMIN_B12 (32):
            Value representing vitamin B12 nutrient.
        VITAMIN_B6 (33):
            Value representing vitamin B6 nutrient.
        VITAMIN_C (34):
            Value representing vitamin C nutrient.
        VITAMIN_D (35):
            Value representing vitamin D nutrient.
        VITAMIN_E (36):
            Value representing vitamin E nutrient.
        VITAMIN_K (37):
            Value representing vitamin K nutrient.
        ZINC (38):
            Value representing zinc nutrient.
        FOLATE (39):
            Value representing folate nutrient.
    """

    NUTRIENT_UNSPECIFIED = 0
    BIOTIN = 1
    CAFFEINE = 2
    CALCIUM = 3
    CHLORIDE = 4
    CARBOHYDRATES = 5
    CHOLESTEROL = 6
    CHROMIUM = 7
    COPPER = 8
    DIETARY_FIBER = 9
    FOLIC_ACID = 10
    IODINE = 11
    IRON = 12
    MAGNESIUM = 13
    MANGANESE = 14
    MOLYBDENUM = 15
    MONOUNSATURATED_FAT = 16
    NIACIN = 17
    PANTOTHENIC_ACID = 18
    PHOSPHORUS = 19
    POLYUNSATURATED_FAT = 20
    POTASSIUM = 21
    PROTEIN = 22
    RIBOFLAVIN = 23
    SATURATED_FAT = 24
    SELENIUM = 25
    SODIUM = 26
    SUGAR = 27
    THIAMIN = 28
    TRANS_FAT = 29
    UNSATURATED_FAT = 30
    VITAMIN_A = 31
    VITAMIN_B12 = 32
    VITAMIN_B6 = 33
    VITAMIN_C = 34
    VITAMIN_D = 35
    VITAMIN_E = 36
    VITAMIN_K = 37
    ZINC = 38
    FOLATE = 39


class WeightUnit(proto.Enum):
    r"""Enum representing the unit of weight.

    Values:
        WEIGHT_UNIT_UNSPECIFIED (0):
            Unspecified weight unit.
        GRAM (1):
            Value representing gram.
        KILOGRAM (2):
            Value representing kilogram.
        OUNCE (3):
            Value representing ounce.
        POUND (4):
            Value representing pound.
        STONE (5):
            Value representing stone.
        MILLIGRAM (6):
            Value representing milligram.
        MICROGRAM (7):
            Value representing microgram.
        NANOGRAM (8):
            Value representing nanogram.
    """

    WEIGHT_UNIT_UNSPECIFIED = 0
    GRAM = 1
    KILOGRAM = 2
    OUNCE = 3
    POUND = 4
    STONE = 5
    MILLIGRAM = 6
    MICROGRAM = 7
    NANOGRAM = 8


class VolumeUnit(proto.Enum):
    r"""Enum representing the unit of volume.

    Values:
        VOLUME_UNIT_UNSPECIFIED (0):
            Unspecified volume unit.
        CUP_IMPERIAL (1):
            Cup (imperial)
        CUP_US (2):
            Cup (US)
        FLUID_OUNCE_IMPERIAL (3):
            Fluid ounce (imperial)
        FLUID_OUNCE_US (4):
            Fluid ounce (US)
        LITER (5):
            Liter
        MILLILITER (6):
            Milliliter
        PINT_IMPERIAL (7):
            Pint (imperial)
        PINT_US (8):
            Pint (US)
    """

    VOLUME_UNIT_UNSPECIFIED = 0
    CUP_IMPERIAL = 1
    CUP_US = 2
    FLUID_OUNCE_IMPERIAL = 3
    FLUID_OUNCE_US = 4
    LITER = 5
    MILLILITER = 6
    PINT_IMPERIAL = 7
    PINT_US = 8


class OvulationTestResult(proto.Enum):
    r"""Ovulation test result.

    Values:
        OVULATION_TEST_RESULT_UNSPECIFIED (0):
            Unspecified result.
        NEGATIVE (1):
            Negative result.
        LUTEINIZING_HORMONE_SURGE (2):
            Luteinizing hormone surge.
        ESTROGEN_SURGE (3):
            Estrogen surge.
        POSITIVE (4):
            Positive result.
        INDETERMINATE (5):
            Indeterminate result.
    """

    OVULATION_TEST_RESULT_UNSPECIFIED = 0
    NEGATIVE = 1
    LUTEINIZING_HORMONE_SURGE = 2
    ESTROGEN_SURGE = 3
    POSITIVE = 4
    INDETERMINATE = 5


class ActiveZoneMinutes(proto.Message):
    r"""Record of active zone minutes in a given time interval.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        interval (google.devicesandservices.health_v4.types.ObservationTimeInterval):
            Required. Observed interval.
        heart_rate_zone (google.devicesandservices.health_v4.types.ActiveZoneMinutes.HeartRateZone):
            Required. Heart rate zone in which the active
            zone minutes have been earned, in the given time
            interval.
        active_zone_minutes (int):
            Required. Number of Active Zone Minutes earned in the given
            time interval. Note: active_zone_minutes equals to 1 for low
            intensity (fat burn) zones or 2 for high intensity zones
            (cardio, peak).

            This field is a member of `oneof`_ ``_active_zone_minutes``.
    """

    class HeartRateZone(proto.Enum):
        r"""Represents different heart rate zones.

        Values:
            HEART_RATE_ZONE_UNSPECIFIED (0):
                Unspecified heart rate zone.
            FAT_BURN (1):
                The fat burn heart rate zone.
            CARDIO (2):
                The cardio heart rate zone.
            PEAK (3):
                The peak heart rate zone.
        """

        HEART_RATE_ZONE_UNSPECIFIED = 0
        FAT_BURN = 1
        CARDIO = 2
        PEAK = 3

    interval: data_coordinates.ObservationTimeInterval = proto.Field(
        proto.MESSAGE,
        number=1,
        message=data_coordinates.ObservationTimeInterval,
    )
    heart_rate_zone: HeartRateZone = proto.Field(
        proto.ENUM,
        number=2,
        enum=HeartRateZone,
    )
    active_zone_minutes: int = proto.Field(
        proto.INT64,
        number=3,
        optional=True,
    )


class ActiveZoneMinutesRollupValue(proto.Message):
    r"""Represents the result of the rollup of the active zone
    minutes data type.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        sum_in_cardio_heart_zone (int):
            Active zone minutes in ``HeartRateZone.CARDIO``.

            This field is a member of `oneof`_ ``_sum_in_cardio_heart_zone``.
        sum_in_peak_heart_zone (int):
            Active zone minutes in ``HeartRateZone.PEAK``.

            This field is a member of `oneof`_ ``_sum_in_peak_heart_zone``.
        sum_in_fat_burn_heart_zone (int):
            Active zone minutes in ``HeartRateZone.FAT_BURN``.

            This field is a member of `oneof`_ ``_sum_in_fat_burn_heart_zone``.
    """

    sum_in_cardio_heart_zone: int = proto.Field(
        proto.INT64,
        number=1,
        optional=True,
    )
    sum_in_peak_heart_zone: int = proto.Field(
        proto.INT64,
        number=2,
        optional=True,
    )
    sum_in_fat_burn_heart_zone: int = proto.Field(
        proto.INT64,
        number=3,
        optional=True,
    )


class ActiveMinutes(proto.Message):
    r"""Record of active minutes in a given time interval.

    Attributes:
        interval (google.devicesandservices.health_v4.types.ObservationTimeInterval):
            Required. Observed interval.
        active_minutes_by_activity_level (MutableSequence[google.devicesandservices.health_v4.types.ActiveMinutes.ActiveMinutesByActivityLevel]):
            Required. Active minutes by activity level.
            At most one record per activity level is
            allowed.
    """

    class ActivityLevel(proto.Enum):
        r"""Activity level.

        Values:
            ACTIVITY_LEVEL_UNSPECIFIED (0):
                Activity level is unspecified.
            LIGHT (1):
                Light activity level.
            MODERATE (2):
                Moderate activity level.
            VIGOROUS (3):
                Vigorous activity level.
        """

        ACTIVITY_LEVEL_UNSPECIFIED = 0
        LIGHT = 1
        MODERATE = 2
        VIGOROUS = 3

    class ActiveMinutesByActivityLevel(proto.Message):
        r"""Active minutes at a given activity level.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            activity_level (google.devicesandservices.health_v4.types.ActiveMinutes.ActivityLevel):
                Required. The level of activity.
            active_minutes (int):
                Required. Number of whole minutes spent in
                activity.

                This field is a member of `oneof`_ ``_active_minutes``.
        """

        activity_level: "ActiveMinutes.ActivityLevel" = proto.Field(
            proto.ENUM,
            number=1,
            enum="ActiveMinutes.ActivityLevel",
        )
        active_minutes: int = proto.Field(
            proto.INT64,
            number=2,
            optional=True,
        )

    interval: data_coordinates.ObservationTimeInterval = proto.Field(
        proto.MESSAGE,
        number=1,
        message=data_coordinates.ObservationTimeInterval,
    )
    active_minutes_by_activity_level: MutableSequence[ActiveMinutesByActivityLevel] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message=ActiveMinutesByActivityLevel,
        )
    )


class ActiveMinutesRollupValue(proto.Message):
    r"""Represents the result of the rollup of the active minutes
    data type.

    Attributes:
        active_minutes_rollup_by_activity_level (MutableSequence[google.devicesandservices.health_v4.types.ActiveMinutesRollupValue.ActiveMinutesRollupByActivityLevel]):
            Active minutes by activity level. At most one
            record per activity level is allowed.
    """

    class ActiveMinutesRollupByActivityLevel(proto.Message):
        r"""Active minutes by activity level.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            activity_level (google.devicesandservices.health_v4.types.ActiveMinutes.ActivityLevel):
                The level of activity.
            active_minutes_sum (int):
                Number of whole minutes spent in activity.

                This field is a member of `oneof`_ ``_active_minutes_sum``.
        """

        activity_level: "ActiveMinutes.ActivityLevel" = proto.Field(
            proto.ENUM,
            number=1,
            enum="ActiveMinutes.ActivityLevel",
        )
        active_minutes_sum: int = proto.Field(
            proto.INT64,
            number=2,
            optional=True,
        )

    active_minutes_rollup_by_activity_level: MutableSequence[
        ActiveMinutesRollupByActivityLevel
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=ActiveMinutesRollupByActivityLevel,
    )


class ActivityLevel(proto.Message):
    r"""Internal type to capture activity level during a certain time
    interval.

    Attributes:
        interval (google.devicesandservices.health_v4.types.ObservationTimeInterval):
            Required. Observed interval.
        activity_level_type (google.devicesandservices.health_v4.types.ActivityLevel.ActivityLevelType):
            Required. Activity level type in the given
            time interval.
    """

    class ActivityLevelType(proto.Enum):
        r"""Represents different activity level types.

        Values:
            ACTIVITY_LEVEL_TYPE_UNSPECIFIED (0):
                Unspecified activity level type.
            SEDENTARY (1):
                Sedentary activity level.
            LIGHTLY_ACTIVE (2):
                Lightly active activity level.
            MODERATELY_ACTIVE (3):
                Moderately active activity level.
            VERY_ACTIVE (4):
                Very active activity level.
        """

        ACTIVITY_LEVEL_TYPE_UNSPECIFIED = 0
        SEDENTARY = 1
        LIGHTLY_ACTIVE = 2
        MODERATELY_ACTIVE = 3
        VERY_ACTIVE = 4

    interval: data_coordinates.ObservationTimeInterval = proto.Field(
        proto.MESSAGE,
        number=1,
        message=data_coordinates.ObservationTimeInterval,
    )
    activity_level_type: ActivityLevelType = proto.Field(
        proto.ENUM,
        number=2,
        enum=ActivityLevelType,
    )


class ActivityLevelRollupValue(proto.Message):
    r"""Represents the result of the rollup of the activity level
    data type.

    Attributes:
        activity_level_rollups_by_activity_level_type (MutableSequence[google.devicesandservices.health_v4.types.ActivityLevelRollupValue.ActivityLevelRollupByActivityLevelType]):
            List of total durations in each activity
            level type.
    """

    class ActivityLevelRollupByActivityLevelType(proto.Message):
        r"""Represents the total duration in a specific activity level
        type.

        Attributes:
            activity_level_type (google.devicesandservices.health_v4.types.ActivityLevel.ActivityLevelType):
                Activity level type.
            total_duration (google.protobuf.duration_pb2.Duration):
                Total duration in the activity level type.
        """

        activity_level_type: "ActivityLevel.ActivityLevelType" = proto.Field(
            proto.ENUM,
            number=1,
            enum="ActivityLevel.ActivityLevelType",
        )
        total_duration: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=2,
            message=duration_pb2.Duration,
        )

    activity_level_rollups_by_activity_level_type: MutableSequence[
        ActivityLevelRollupByActivityLevelType
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=ActivityLevelRollupByActivityLevelType,
    )


class Altitude(proto.Message):
    r"""Captures the altitude gain (i.e. deltas), and not level above
    sea, for a user in millimeters.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        interval (google.devicesandservices.health_v4.types.ObservationTimeInterval):
            Required. Observed interval.
        gain_millimeters (int):
            Required. Altitude gain in millimeters over the observed
            interval. Must be in the range
            ``[-1000000000, 1000000000]``.

            This field is a member of `oneof`_ ``_gain_millimeters``.
    """

    interval: data_coordinates.ObservationTimeInterval = proto.Field(
        proto.MESSAGE,
        number=2,
        message=data_coordinates.ObservationTimeInterval,
    )
    gain_millimeters: int = proto.Field(
        proto.INT64,
        number=3,
        optional=True,
    )


class BasalEnergyBurned(proto.Message):
    r"""Number of calories burned due to basal metabolic rate (BMR)
    over a period of time.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        interval (google.devicesandservices.health_v4.types.ObservationTimeInterval):
            Required. Observed interval.
        kcal (float):
            Required. Number of calories burned due to
            basal metabolic rate in kilocalories over the
            observed interval.

            This field is a member of `oneof`_ ``_kcal``.
    """

    interval: data_coordinates.ObservationTimeInterval = proto.Field(
        proto.MESSAGE,
        number=1,
        message=data_coordinates.ObservationTimeInterval,
    )
    kcal: float = proto.Field(
        proto.DOUBLE,
        number=2,
        optional=True,
    )


class BodyFat(proto.Message):
    r"""Body fat measurement.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        sample_time (google.devicesandservices.health_v4.types.ObservationSampleTime):
            Required. The time at which body fat was
            measured.
        percentage (float):
            Required. Body fat percentage. Must be in the range
            ``[0, 100]``.

            This field is a member of `oneof`_ ``_percentage``.
    """

    sample_time: data_coordinates.ObservationSampleTime = proto.Field(
        proto.MESSAGE,
        number=2,
        message=data_coordinates.ObservationSampleTime,
    )
    percentage: float = proto.Field(
        proto.DOUBLE,
        number=3,
        optional=True,
    )


class BodyFatRollupValue(proto.Message):
    r"""Represents the result of the rollup of the body fat data
    type.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        body_fat_percentage_avg (float):
            Average body fat percentage.

            This field is a member of `oneof`_ ``_body_fat_percentage_avg``.
    """

    body_fat_percentage_avg: float = proto.Field(
        proto.DOUBLE,
        number=1,
        optional=True,
    )


class CoreBodyTemperature(proto.Message):
    r"""Core body temperature measurement, distinct from peripheral
    body temperature, reflects the temperature of the body's
    internal organs.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        sample_time (google.devicesandservices.health_v4.types.ObservationSampleTime):
            Required. The time at which core body
            temperature was measured.
        temperature_celsius (float):
            Required. The core body temperature in Celsius. Must be in
            the range ``[0, 100]``.

            This field is a member of `oneof`_ ``_temperature_celsius``.
        measurement_location (google.devicesandservices.health_v4.types.CoreBodyTemperature.MeasurementLocation):
            Optional. The location of the core body
            temperature measurement.
        id (str):
            Optional. The unique identifier of the core
            body temperature measurement.
    """

    class MeasurementLocation(proto.Enum):
        r"""Measurement location for core body temperature.

        Values:
            MEASUREMENT_LOCATION_UNSPECIFIED (0):
                Measurement location is unspecified.
            OTHER (1):
                Other measurement location.
            ARMPIT (2):
                Armpit measurement location.
            BODY (3):
                Body measurement location.
            EAR (4):
                Ear measurement location.
            FINGER (5):
                Finger measurement location.
            GASTRO_INTESTINAL (6):
                Gastro-intestinal measurement location.
            MOUTH (7):
                Mouth measurement location.
            RECTUM (8):
                Rectum measurement location.
            TOE (9):
                Toe measurement location.
            EAR_DRUM (10):
                Ear drum measurement location.
            TEMPORAL_ARTERY (11):
                Temporal artery measurement location.
            FOREHEAD (12):
                Forehead measurement location.
            URINARY_BLADDER (13):
                Urinary bladder measurement location.
            NASAL (14):
                Nasal measurement location.
            NASOPHARYNGEAL (15):
                Nasopharyngeal measurement location.
            WRIST (16):
                Wrist measurement location.
            VAGINA (17):
                Vagina measurement location.
        """

        MEASUREMENT_LOCATION_UNSPECIFIED = 0
        OTHER = 1
        ARMPIT = 2
        BODY = 3
        EAR = 4
        FINGER = 5
        GASTRO_INTESTINAL = 6
        MOUTH = 7
        RECTUM = 8
        TOE = 9
        EAR_DRUM = 10
        TEMPORAL_ARTERY = 11
        FOREHEAD = 12
        URINARY_BLADDER = 13
        NASAL = 14
        NASOPHARYNGEAL = 15
        WRIST = 16
        VAGINA = 17

    sample_time: data_coordinates.ObservationSampleTime = proto.Field(
        proto.MESSAGE,
        number=2,
        message=data_coordinates.ObservationSampleTime,
    )
    temperature_celsius: float = proto.Field(
        proto.DOUBLE,
        number=3,
        optional=True,
    )
    measurement_location: MeasurementLocation = proto.Field(
        proto.ENUM,
        number=4,
        enum=MeasurementLocation,
    )
    id: str = proto.Field(
        proto.STRING,
        number=5,
    )


class CoreBodyTemperatureRollupValue(proto.Message):
    r"""Represents the result of the rollup of the core body
    temperature data type.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        temperature_celsius_avg (float):
            Average core body temperature in Celsius.

            This field is a member of `oneof`_ ``_temperature_celsius_avg``.
        temperature_celsius_max (float):
            Maximum core body temperature in Celsius.

            This field is a member of `oneof`_ ``_temperature_celsius_max``.
        temperature_celsius_min (float):
            Minimum core body temperature in Celsius.

            This field is a member of `oneof`_ ``_temperature_celsius_min``.
    """

    temperature_celsius_avg: float = proto.Field(
        proto.DOUBLE,
        number=1,
        optional=True,
    )
    temperature_celsius_max: float = proto.Field(
        proto.DOUBLE,
        number=2,
        optional=True,
    )
    temperature_celsius_min: float = proto.Field(
        proto.DOUBLE,
        number=3,
        optional=True,
    )


class CaloriesInHeartRateZoneRollupValue(proto.Message):
    r"""Represents the result of the rollup of the calories in heart
    rate zone data type.

    Attributes:
        calories_in_heart_rate_zones (MutableSequence[google.devicesandservices.health_v4.types.CaloriesInHeartRateZoneRollupValue.CaloriesInHeartRateZoneValue]):
            List of calories burned in each heart rate
            zone.
    """

    class CaloriesInHeartRateZoneValue(proto.Message):
        r"""Represents the amount of kilocalories burned in a specific
        heart rate zone.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            heart_rate_zone (google.devicesandservices.health_v4.types.HeartRateZoneType):
                The heart rate zone.
            kcal (float):
                The amount of kilocalories burned in the
                specified heart rate zone.

                This field is a member of `oneof`_ ``_kcal``.
        """

        heart_rate_zone: "HeartRateZoneType" = proto.Field(
            proto.ENUM,
            number=1,
            enum="HeartRateZoneType",
        )
        kcal: float = proto.Field(
            proto.DOUBLE,
            number=2,
            optional=True,
        )

    calories_in_heart_rate_zones: MutableSequence[CaloriesInHeartRateZoneValue] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=CaloriesInHeartRateZoneValue,
        )
    )


class DailyHeartRateZones(proto.Message):
    r"""User's heart rate zone thresholds based on the Karvonen
    algorithm for a specific day.

    Attributes:
        date (google.type.date_pb2.Date):
            Required. Date (in user's timezone) of the
            heart rate zones record.
        heart_rate_zones (MutableSequence[google.devicesandservices.health_v4.types.DailyHeartRateZones.HeartRateZone]):
            Required. The heart rate zones.
    """

    class HeartRateZone(proto.Message):
        r"""The heart rate zone.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            heart_rate_zone_type (google.devicesandservices.health_v4.types.HeartRateZoneType):
                Required. The heart rate zone type.
            min_beats_per_minute (int):
                Required. Minimum heart rate for this zone in
                beats per minute.

                This field is a member of `oneof`_ ``_min_beats_per_minute``.
            max_beats_per_minute (int):
                Required. Maximum heart rate for this zone in
                beats per minute.

                This field is a member of `oneof`_ ``_max_beats_per_minute``.
        """

        heart_rate_zone_type: "HeartRateZoneType" = proto.Field(
            proto.ENUM,
            number=1,
            enum="HeartRateZoneType",
        )
        min_beats_per_minute: int = proto.Field(
            proto.INT64,
            number=2,
            optional=True,
        )
        max_beats_per_minute: int = proto.Field(
            proto.INT64,
            number=3,
            optional=True,
        )

    date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=1,
        message=date_pb2.Date,
    )
    heart_rate_zones: MutableSequence[HeartRateZone] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=HeartRateZone,
    )


class DailyHeartRateVariability(proto.Message):
    r"""Represents the daily heart rate variability data type.

    At least one of the following fields must be set:

    - ``average_heart_rate_variability_milliseconds``
    - ``non_rem_heart_rate_beats_per_minute``
    - ``entropy``
    - ``deep_sleep_root_mean_square_of_successive_differences_milliseconds``


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        date (google.type.date_pb2.Date):
            Required. Date (in the user's timezone) of
            heart rate variability measurement.
        average_heart_rate_variability_milliseconds (float):
            Optional. A user's average heart rate
            variability calculated using the root mean
            square of successive differences (RMSSD) in
            times between heartbeats.

            This field is a member of `oneof`_ ``_average_heart_rate_variability_milliseconds``.
        non_rem_heart_rate_beats_per_minute (int):
            Optional. Non-REM heart rate

            This field is a member of `oneof`_ ``_non_rem_heart_rate_beats_per_minute``.
        entropy (float):
            Optional. The Shanon entropy of heartbeat
            intervals. Entropy quantifies randomness or
            disorder in a system. High entropy indicates
            high HRV. Entropy is measured from the histogram
            of time interval between successive heart beats
            values measured during sleep.

            This field is a member of `oneof`_ ``_entropy``.
        deep_sleep_root_mean_square_of_successive_differences_milliseconds (float):
            Optional. The root mean square of successive
            differences (RMSSD) value during deep sleep.

            This field is a member of `oneof`_ ``_deep_sleep_root_mean_square_of_successive_differences_milliseconds``.
    """

    date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=2,
        message=date_pb2.Date,
    )
    average_heart_rate_variability_milliseconds: float = proto.Field(
        proto.DOUBLE,
        number=4,
        optional=True,
    )
    non_rem_heart_rate_beats_per_minute: int = proto.Field(
        proto.INT64,
        number=5,
        optional=True,
    )
    entropy: float = proto.Field(
        proto.DOUBLE,
        number=6,
        optional=True,
    )
    deep_sleep_root_mean_square_of_successive_differences_milliseconds: float = (
        proto.Field(
            proto.DOUBLE,
            number=7,
            optional=True,
        )
    )


class DailyRespiratoryRate(proto.Message):
    r"""A daily average respiratory rate (breaths per minute) for a
    day of the year. One data point per day calculated for the main
    sleep.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        date (google.type.date_pb2.Date):
            Required. The date on which the respiratory
            rate was measured.
        breaths_per_minute (float):
            Required. The average number of breaths taken
            per minute.

            This field is a member of `oneof`_ ``_breaths_per_minute``.
    """

    date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=1,
        message=date_pb2.Date,
    )
    breaths_per_minute: float = proto.Field(
        proto.DOUBLE,
        number=2,
        optional=True,
    )


class DailyOxygenSaturation(proto.Message):
    r"""A daily oxygen saturation (SpO2) record.
    Represents the user's daily oxygen saturation summary, typically
    calculated during sleep.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        date (google.type.date_pb2.Date):
            Required. Date (in user's timezone) of the
            daily oxygen saturation record.
        average_percentage (float):
            Required. The average value of the oxygen saturation samples
            during the sleep. Must be in the range ``[0, 100]``.

            This field is a member of `oneof`_ ``_average_percentage``.
        lower_bound_percentage (float):
            Required. The lower bound of the confidence interval of
            oxygen saturation samples during sleep. Must be in the range
            ``[0, 100]``.

            This field is a member of `oneof`_ ``_lower_bound_percentage``.
        upper_bound_percentage (float):
            Required. The upper bound of the confidence interval of
            oxygen saturation samples during sleep. Must be in the range
            ``[0, 100]``.

            This field is a member of `oneof`_ ``_upper_bound_percentage``.
        standard_deviation_percentage (float):
            Optional. Standard deviation of the daily
            oxygen saturation averages from the past 7-30
            days.

            This field is a member of `oneof`_ ``_standard_deviation_percentage``.
    """

    date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=1,
        message=date_pb2.Date,
    )
    average_percentage: float = proto.Field(
        proto.DOUBLE,
        number=2,
        optional=True,
    )
    lower_bound_percentage: float = proto.Field(
        proto.DOUBLE,
        number=3,
        optional=True,
    )
    upper_bound_percentage: float = proto.Field(
        proto.DOUBLE,
        number=4,
        optional=True,
    )
    standard_deviation_percentage: float = proto.Field(
        proto.DOUBLE,
        number=5,
        optional=True,
    )


class DailyRestingHeartRate(proto.Message):
    r"""Measures the daily resting heart rate for a user, calculated
    using the all day heart rate measurements.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        date (google.type.date_pb2.Date):
            Required. Date  (in the user's timezone) of
            the resting heart rate measurement.
        beats_per_minute (int):
            Required. The resting heart rate value in
            beats per minute.

            This field is a member of `oneof`_ ``_beats_per_minute``.
        daily_resting_heart_rate_metadata (google.devicesandservices.health_v4.types.DailyRestingHeartRate.DailyRestingHeartRateMetadata):
            Optional. Metadata for the daily resting
            heart rate.
    """

    class DailyRestingHeartRateMetadata(proto.Message):
        r"""Metadata for the daily resting heart rate.

        Attributes:
            calculation_method (google.devicesandservices.health_v4.types.DailyRestingHeartRate.DailyRestingHeartRateMetadata.CalculationMethod):
                Required. The method used to calculate the
                resting heart rate.
        """

        class CalculationMethod(proto.Enum):
            r"""The method used to calculate the resting heart rate.

            Values:
                CALCULATION_METHOD_UNSPECIFIED (0):
                    The calculation method is unspecified.
                WITH_SLEEP (1):
                    The resting heart rate is calculated using
                    the sleep data.
                ONLY_WITH_AWAKE_DATA (2):
                    The resting heart rate is calculated using
                    only awake data.
            """

            CALCULATION_METHOD_UNSPECIFIED = 0
            WITH_SLEEP = 1
            ONLY_WITH_AWAKE_DATA = 2

        calculation_method: "DailyRestingHeartRate.DailyRestingHeartRateMetadata.CalculationMethod" = proto.Field(
            proto.ENUM,
            number=1,
            enum="DailyRestingHeartRate.DailyRestingHeartRateMetadata.CalculationMethod",
        )

    date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=2,
        message=date_pb2.Date,
    )
    beats_per_minute: int = proto.Field(
        proto.INT64,
        number=4,
        optional=True,
    )
    daily_resting_heart_rate_metadata: DailyRestingHeartRateMetadata = proto.Field(
        proto.MESSAGE,
        number=5,
        message=DailyRestingHeartRateMetadata,
    )


class DailySleepTemperatureDerivations(proto.Message):
    r"""Provides derived sleep temperature values, calculated from
    skin or internal device temperature readings during sleep.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        date (google.type.date_pb2.Date):
            Required. Date for which the sleep
            temperature derivations are calculated.
        nightly_temperature_celsius (float):
            Required. The user's nightly skin
            temperature. It is the mean of skin temperature
            samples taken from the user’s sleep.

            This field is a member of `oneof`_ ``_nightly_temperature_celsius``.
        baseline_temperature_celsius (float):
            Optional. The user's baseline skin
            temperature. It is the median of the user's
            nightly skin temperature over the past 30 days.

            This field is a member of `oneof`_ ``_baseline_temperature_celsius``.
        relative_nightly_stddev_30d_celsius (float):
            Optional. The standard deviation of the
            user’s relative nightly skin temperature
            (temperature - baseline) over the past 30 days.

            This field is a member of `oneof`_ ``_relative_nightly_stddev_30d_celsius``.
    """

    date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=1,
        message=date_pb2.Date,
    )
    nightly_temperature_celsius: float = proto.Field(
        proto.DOUBLE,
        number=2,
        optional=True,
    )
    baseline_temperature_celsius: float = proto.Field(
        proto.DOUBLE,
        number=3,
        optional=True,
    )
    relative_nightly_stddev_30d_celsius: float = proto.Field(
        proto.DOUBLE,
        number=4,
        optional=True,
    )


class DailyVO2Max(proto.Message):
    r"""Contains a daily summary of the user's VO2 max (cardio
    fitness score), which is the maximum rate of oxygen the body can
    use during exercise.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        date (google.type.date_pb2.Date):
            Required. The date for which the Daily VO2
            max was measured.
        vo2_max (float):
            Required. Daily VO2 max value measured as in ml consumed
            oxygen / kg of body weight / min. Must be in the range
            ``[0, 100]``.

            This field is a member of `oneof`_ ``_vo2_max``.
        estimated (bool):
            Optional. An estimated field is added to
            indicate when the confidence has decreased
            sufficiently to consider the value an
            estimation.
        cardio_fitness_level (google.devicesandservices.health_v4.types.DailyVO2Max.CardioFitnessLevel):
            Optional. Represents the user's cardio
            fitness level based on their VO2 max.
        vo2_max_covariance (float):
            Optional. The covariance of the VO2 max
            value.

            This field is a member of `oneof`_ ``_vo2_max_covariance``.
    """

    class CardioFitnessLevel(proto.Enum):
        r"""The cardio fitness level categories.

        Values:
            CARDIO_FITNESS_LEVEL_UNSPECIFIED (0):
                Unspecified cardio fitness level.
            POOR (1):
                Poor cardio fitness level.
            FAIR (2):
                Fair cardio fitness level.
            AVERAGE (3):
                Average cardio fitness level.
            GOOD (4):
                Good cardio fitness level.
            VERY_GOOD (5):
                Very good cardio fitness level.
            EXCELLENT (6):
                Excellent cardio fitness level.
        """

        CARDIO_FITNESS_LEVEL_UNSPECIFIED = 0
        POOR = 1
        FAIR = 2
        AVERAGE = 3
        GOOD = 4
        VERY_GOOD = 5
        EXCELLENT = 6

    date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=1,
        message=date_pb2.Date,
    )
    vo2_max: float = proto.Field(
        proto.DOUBLE,
        number=2,
        optional=True,
    )
    estimated: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    cardio_fitness_level: CardioFitnessLevel = proto.Field(
        proto.ENUM,
        number=4,
        enum=CardioFitnessLevel,
    )
    vo2_max_covariance: float = proto.Field(
        proto.DOUBLE,
        number=5,
        optional=True,
    )


class Distance(proto.Message):
    r"""Distance traveled over an interval of time.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        interval (google.devicesandservices.health_v4.types.ObservationTimeInterval):
            Required. Observed interval.
        millimeters (int):
            Required. Distance in millimeters over the observed
            interval. Must be in the range ``[0, 1000000000]``.

            This field is a member of `oneof`_ ``_millimeters``.
    """

    interval: data_coordinates.ObservationTimeInterval = proto.Field(
        proto.MESSAGE,
        number=2,
        message=data_coordinates.ObservationTimeInterval,
    )
    millimeters: int = proto.Field(
        proto.INT64,
        number=3,
        optional=True,
    )


class DistanceRollupValue(proto.Message):
    r"""Result of the rollup of the user's distance.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        millimeters_sum (int):
            Sum of the distance in millimeters.

            This field is a member of `oneof`_ ``_millimeters_sum``.
    """

    millimeters_sum: int = proto.Field(
        proto.INT64,
        number=1,
        optional=True,
    )


class Electrocardiogram(proto.Message):
    r"""Represents an Electrocardiogram (ECG) measurement session.
    This data type is based on SaMD feature and any changes to it
    may require additional review.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        interval (google.devicesandservices.health_v4.types.SessionTimeInterval):
            Required. Observed interval.

            NOTE: Historical ECG data lacks timezone offsets, so
            ``start_utc_offset`` and ``end_utc_offset`` will be missing
            or default to zero. As a result, the civil time fields
            within this interval will default to UTC. It is recommended
            to use physical time fields instead for accurate time
            referencing.

            NOTE: The ``start_time`` and ``end_time`` of the interval
            are equal, representing the reading time.
        beats_per_minute_avg (int):
            Optional. Average heart rate recorded during
            ECG reading in beats per minute.

            This field is a member of `oneof`_ ``_beats_per_minute_avg``.
        result_classification (google.devicesandservices.health_v4.types.Electrocardiogram.ResultClassification):
            Optional. The result classification of the
            ECG reading.
        waveform_samples (MutableSequence[int]):
            Optional. An array of voltage values
            representing lead I ECG values. Each sample
            represents voltage difference in ECG graph. The
            first value in array corresponds to the start of
            the reading.
        sampling_frequency_hertz (int):
            Optional. The sampling frequency of waveform
            samples in hertz.

            This field is a member of `oneof`_ ``_sampling_frequency_hertz``.
        millivolts_scaling_factor (int):
            Optional. The factor by which to divide waveform samples to
            get voltage in millivolts: millivolts = waveform_sample /
            millivolts_scaling_factor.

            This field is a member of `oneof`_ ``_millivolts_scaling_factor``.
        lead_number (int):
            Optional. The number of leads used for ECG
            reading.

            This field is a member of `oneof`_ ``_lead_number``.
        medical_device_info (google.devicesandservices.health_v4.types.MedicalDeviceInfo):
            Output only. The meta information for the compatible device
            used to conduct the measurement.

            ECG measurements typically populate ``firmware_version``,
            ``feature_version``, and ``device_model``.
    """

    class ResultClassification(proto.Enum):
        r"""The classification of the ECG reading rhythm.

        Values:
            RESULT_CLASSIFICATION_UNSPECIFIED (0):
                Unspecified result classification.
            NORMAL_SINUS_RHYTHM (1):
                Heart rhythm appears normal. Corresponds to
                result "Normal Sinus Rhythm".
            ATRIAL_FIBRILLATION (2):
                Signs of Atrial Fibrillation detected.
                Corresponds to result "Atrial Fibrillation".
            INCONCLUSIVE (3):
                The reading is inconclusive as it could not
                be classified. Corresponds to result
                "Inconclusive".
            INCONCLUSIVE_HIGH_HEART_RATE (4):
                The reading is inconclusive as it could not
                be classified because heart rate is high
                (>120bpm). Corresponds to result "Inconclusive:
                High heart rate".
            INCONCLUSIVE_LOW_HEART_RATE (5):
                The reading is inconclusive as it could not
                be classified because heart rate is low
                (<50bpm). Corresponds to result "Inconclusive:
                Low heart rate".
            UNREADABLE (6):
                The reading is unreadable.
            NOT_ANALYZED (7):
                The reading was not analyzed.
        """

        RESULT_CLASSIFICATION_UNSPECIFIED = 0
        NORMAL_SINUS_RHYTHM = 1
        ATRIAL_FIBRILLATION = 2
        INCONCLUSIVE = 3
        INCONCLUSIVE_HIGH_HEART_RATE = 4
        INCONCLUSIVE_LOW_HEART_RATE = 5
        UNREADABLE = 6
        NOT_ANALYZED = 7

    interval: data_coordinates.SessionTimeInterval = proto.Field(
        proto.MESSAGE,
        number=1,
        message=data_coordinates.SessionTimeInterval,
    )
    beats_per_minute_avg: int = proto.Field(
        proto.INT64,
        number=2,
        optional=True,
    )
    result_classification: ResultClassification = proto.Field(
        proto.ENUM,
        number=3,
        enum=ResultClassification,
    )
    waveform_samples: MutableSequence[int] = proto.RepeatedField(
        proto.SINT32,
        number=4,
    )
    sampling_frequency_hertz: int = proto.Field(
        proto.INT32,
        number=5,
        optional=True,
    )
    millivolts_scaling_factor: int = proto.Field(
        proto.INT32,
        number=6,
        optional=True,
    )
    lead_number: int = proto.Field(
        proto.INT32,
        number=7,
        optional=True,
    )
    medical_device_info: gdh_medical_device_info.MedicalDeviceInfo = proto.Field(
        proto.MESSAGE,
        number=8,
        message=gdh_medical_device_info.MedicalDeviceInfo,
    )


class Exercise(proto.Message):
    r"""An exercise that stores information about a physical
    activity.

    Attributes:
        interval (google.devicesandservices.health_v4.types.SessionTimeInterval):
            Required. Observed exercise interval
        exercise_type (google.devicesandservices.health_v4.types.Exercise.ExerciseType):
            Required. The type of activity performed
            during an exercise.
        splits (MutableSequence[google.devicesandservices.health_v4.types.Exercise.SplitSummary]):
            Optional. The default split is 1 km or 1
            mile.
            -  if the movement distance is less than the
              default,    then there are no splits
            -  if the movement distance is greater than or
              equal to the default,
               then we have splits
        exercise_events (MutableSequence[google.devicesandservices.health_v4.types.Exercise.ExerciseEvent]):
            Optional. Exercise events that happen during
            an exercise, such as pause & restarts.
        split_summaries (MutableSequence[google.devicesandservices.health_v4.types.Exercise.SplitSummary]):
            Optional. Laps or splits recorded within an
            exercise. Laps could be split based on distance
            or other criteria (duration, etc.) Laps should
            not be overlapping with each other.
        metrics_summary (google.devicesandservices.health_v4.types.MetricsSummary):
            Required. Summary metrics for this exercise
            ( )
        exercise_metadata (google.devicesandservices.health_v4.types.Exercise.ExerciseMetadata):
            Optional. Additional exercise metadata.
        display_name (str):
            Required. The localized, human-readable name of the
            exercise. For all exercise types other than ``OTHER``, the
            system ignores client input and overrides this field with a
            generated name based on ``exercise_type`` (e.g., "Walking"
            for ``WALKING``). If ``exercise_type`` is ``OTHER``, this
            field can contain the user's custom, free-form display name.
        active_duration (google.protobuf.duration_pb2.Duration):
            Optional. Duration excluding pauses.
        notes (str):
            Optional. Standard free-form notes captured
            at manual logging.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. This is the timestamp of the
            last update to the exercise.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Represents the timestamp of the
            creation of the exercise.
    """

    class ExerciseType(proto.Enum):
        r"""The type of activity performed during an exercise.
        May receive new values in the future.

        Values:
            EXERCISE_TYPE_UNSPECIFIED (0):
                Exercise type is unspecified.
            AEROBIC_WORKOUT (13):
                Aerobic workout type.
            ARCHERY (47):
                Archery type.
            ASSAULT_BIKE (164):
                Assault bike type.
            BACKPACKING (181):
                Backpacking type.
            BADMINTON (48):
                Badminton type.
            BALLET (103):
                Ballet type.
            BALLROOM_DANCE (156):
                Ballroom dance type.
            BARRE_CLASS (49):
                Barre class type.
            BASEBALL (50):
                Baseball type.
            BASKETBALL (51):
                Basketball type.
            BIKING (3):
                Biking type.
            BILLIARDS (180):
                Billiards type.
            BODY_WEIGHT (149):
                Body weight type.
            BOOTCAMP (14):
                Bootcamp type.
            BOWLING (52):
                Bowling type.
            BOXING (53):
                Boxing type.
            BREAKDANCING (157):
                Breakdancing type.
            CALISTHENICS (54):
                Calisthenics type.
            CANOEING (15):
                Canoeing type.
            CARDIO_SCULPT (129):
                Cardio sculpt type.
            CARDIO_WORKOUT (140):
                Cardio workout type.
            CARPENTRY (108):
                Carpentry type.
            CHEERLEADING (165):
                Cheerleading type.
            CIRCUIT_TRAINING (16):
                Circuit training type.
            CLEANING (105):
                Cleaning type.
            CLIMBING (55):
                Climbing type.
            CORE_TRAINING (17):
                Core training type.
            CRICKET (56):
                Cricket type.
            CROQUET (111):
                Croquet type.
            CROSS_COUNTRY_SKI (18):
                Cross country ski type.
            CROSS_TRAINING (57):
                Cross training type.
            CROSSFIT (19):
                Crossfit type.
            CURLING (58):
                Curling type.
            DANCING (20):
                Dancing type.
            DIVING (59):
                Diving type.
            ELECTRIC_BIKE (152):
                Electric bike type.
            ELECTRIC_SCOOTER (168):
                Electric scooter type.
            ELLIPTICAL (21):
                Elliptical type.
            EQUESTRIAN_SPORTS (60):
                Equestrian sports type.
            EXERCISE_CLASS (61):
                Exercise class type.
            FENCING (62):
                Fencing type.
            FIELD_HOCKEY (113):
                Field hockey type.
            FISHING (63):
                Fishing type.
            FITNESS_GAMING (64):
                Fitness gaming type.
            FOILING (175):
                Foiling type.
            FOOTBALL_AMERICAN (65):
                Football american type.
            FOOTBALL_AUSTRALIAN (66):
                Football australian type.
            FREE_WEIGHTS (148):
                Free weights type.
            FRISBEE_PLAYING_GENERAL (67):
                Frisbee playing general type.
            FUNCTIONAL_STRENGTH_TRAINING (68):
                Functional strength training type.
            GARDENING (107):
                Gardening type.
            GOLF (22):
                Golf type.
            GYMNASTICS (69):
                Gymnastics type.
            HANDBALL (70):
                Handball type.
            HAND_CYCLING (71):
                Hand cycling type.
            HIIT (9):
                Hiit type.
            HIKING (5):
                Hiking type.
            HIP_HOP (158):
                Hip hop type.
            HOCKEY (72):
                Hockey type.
            HOEING (109):
                Hoeing type.
            HOUSEHOLD_CHORES (137):
                Household chores type.
            HUNTING (73):
                Hunting type.
            ICE_SKATING (127):
                Ice skating type.
            INCLINE_RUN (142):
                Incline run type.
            INCLINE_WALK (146):
                Incline walk type.
            INDOOR_CLIMBING (23):
                Indoor climbing type.
            INTERVAL_WORKOUT (24):
                Interval workout type.
            JAZZ_DANCE (154):
                Jazz dance type.
            JIU_JITSU (160):
                Jiu jitsu type.
            JUMPING_ROPE (74):
                Jumping rope type.
            KARATE (159):
                Karate type.
            KAYAKING (25):
                Kayaking type.
            KICKBOXING (26):
                Kickboxing type.
            KITESURFING (172):
                Kitesurfing type.
            LACROSSE (75):
                Lacrosse type.
            MARTIAL_ARTS (27):
                Martial arts type.
            MEDITATE (28):
                Meditate type.
            MODERN_DANCE (153):
                Modern dance type.
            MOTOCROSS (114):
                Motocross type.
            MOTORCYCLE (121):
                Motorcycle type.
            MOUNTAIN_BIKE (128):
                Mountain bike type.
            MOWING_LAWN (106):
                Mowing lawn type.
            MUAY_THAI (162):
                Muay thai type.
            MULTISPORT (76):
                Multisport type.
            MUSICAL_PERFORMANCE (163):
                Musical performance type.
            NORDIC_WALKING (145):
                Nordic walking type.
            ORIENTEERING (115):
                Orienteering type.
            OTHER (12):
                Other type.
            OUTDOOR_BIKE (29):
                Outdoor bike type.
            OUTDOOR_WORKOUT (30):
                Outdoor workout type.
            PADDLEBOARDING (31):
                Paddleboarding type.
            PADEL (176):
                Padel type.
            PAINTING (170):
                Painting type.
            PARAGLIDING (78):
                Paragliding type.
            PARKOUR (166):
                Parkour type.
            PICKELBALL (79):
                Pickelball type.
            PILATES (7):
                Pilates type.
            POLO (116):
                Polo type.
            POWERLIFTING (32):
                Powerlifting type.
            POWER_WALKING (143):
                Power walking type.
            RACKET_SPORTS (169):
                Racket sports type.
            RACQUETBALL (80):
                Racquetball type.
            RESISTANCE_BANDS (151):
                Resistance bands type.
            ROCK_CLIMBING (123):
                Rock climbing type.
            ROLLERBLADING (33):
                Rollerblading type.
            ROLLER_SKATING (118):
                Roller skating type.
            ROWING (81):
                Rowing type.
            ROWING_MACHINE (34):
                Rowing machine type.
            RUCKING (144):
                Rucking type.
            RUGBY (82):
                Rugby type.
            RUNNING (1):
                Running type.
            SAILING (83):
                Sailing type.
            SCOOTERING (167):
                Scootering type.
            SCUBA_DIVING (84):
                Scuba diving type.
            SHOOTING (104):
                Shooting type.
            SHOVELING (171):
                Shoveling type.
            SKATEBOARDING (117):
                Skateboarding type.
            SKATING (35):
                Skating type.
            SKIING (36):
                Skiing type.
            SKYDIVING (182):
                Skydiving type.
            SNORKELING (37):
                Snorkeling type.
            SNOWBOARDING (38):
                Snowboarding type.
            SNOWMOBILING (179):
                Snowmobiling type.
            SNOWSHOEING (85):
                Snowshoeing type.
            SNOW_SPORT (86):
                Snow sport type.
            SOCCER (87):
                Soccer type.
            SOFTBALL (88):
                Softball type.
            SPEED_SKATING (178):
                Speed skating type.
            SPINNING (39):
                Spinning type.
            SPORT (40):
                Sport type.
            SQUASH (89):
                Squash type.
            STAIRCLIMBER (41):
                Stairclimber type.
            STATIONARY_BIKE (139):
                Stationary bike type.
            STEP_TRAINING (90):
                Step training type.
            STRENGTH_TRAINING (11):
                Strength training type.
            STRETCHING (42):
                Stretching type.
            STROLLER_WALK (122):
                Stroller walk type.
            SURFING (43):
                Surfing type.
            SWIMMING (4):
                Swimming type.
            SWIMMING_OPEN_WATER (91):
                Swimming open water type.
            SWIMMING_POOL (101):
                Swimming pool type.
            SYNCHRONIZED_SWIMMING (177):
                Synchronized swimming type.
            TABATA_WORKOUT (130):
                Tabata workout type.
            TABLE_TENNIS (92):
                Table tennis type.
            TAEKWONDO (161):
                Taekwondo type.
            TAI_CHI (93):
                Tai chi type.
            TANGO (155):
                Tango type.
            TENNIS (44):
                Tennis type.
            TRACK_AND_FIELD (94):
                Track and field type.
            TRAIL_RUN (141):
                Trail run type.
            TRAMPOLINE (119):
                Trampoline type.
            TREADMILL (45):
                Treadmill type.
            TREADMILL_WALK (138):
                Treadmill walk type.
            TRX (131):
                Trx type.
            ULTIMATE_FRISBEE (112):
                Ultimate frisbee type.
            UNICYCLING (102):
                Unicycling type.
            VOLLEYBALL (95):
                Volleyball type.
            VOLLEYBALL_BEACH (120):
                Volleyball beach type.
            WAKEBOARDING (173):
                Wakeboarding type.
            WALKING (2):
                Walking type.
            WALK_WITH_WEIGHTS (147):
                Walk with weights type.
            WATER_AEROBICS (96):
                Water aerobics type.
            WATER_JOGGING (126):
                Water jogging type.
            WATER_POLO (97):
                Water polo type.
            WATER_SKIING (124):
                Water skiing type.
            WATER_SPORT (98):
                Water sport type.
            WATER_VOLLEYBALL (125):
                Water volleyball type.
            WEEDING (110):
                Weeding type.
            WEIGHTLIFTING (10):
                Weightlifting type.
            WEIGHT_MACHINES (150):
                Weight machines type.
            WEIGHTS (46):
                Weights type.
            WHEELCHAIR (99):
                Wheelchair type.
            WINDSURFING (174):
                Windsurfing type.
            WORKOUT (8):
                Workout type.
            WRESTLING (100):
                Wrestling type.
            YOGA (6):
                Yoga type.
            YOGA_BIKRAM (132):
                Yoga bikram type.
            YOGA_HATHA (133):
                Yoga hatha type.
            YOGA_POWER (134):
                Yoga power type.
            YOGA_VINYASA (135):
                Yoga vinyasa type.
            ZUMBA (136):
                Zumba type.
        """

        EXERCISE_TYPE_UNSPECIFIED = 0
        AEROBIC_WORKOUT = 13
        ARCHERY = 47
        ASSAULT_BIKE = 164
        BACKPACKING = 181
        BADMINTON = 48
        BALLET = 103
        BALLROOM_DANCE = 156
        BARRE_CLASS = 49
        BASEBALL = 50
        BASKETBALL = 51
        BIKING = 3
        BILLIARDS = 180
        BODY_WEIGHT = 149
        BOOTCAMP = 14
        BOWLING = 52
        BOXING = 53
        BREAKDANCING = 157
        CALISTHENICS = 54
        CANOEING = 15
        CARDIO_SCULPT = 129
        CARDIO_WORKOUT = 140
        CARPENTRY = 108
        CHEERLEADING = 165
        CIRCUIT_TRAINING = 16
        CLEANING = 105
        CLIMBING = 55
        CORE_TRAINING = 17
        CRICKET = 56
        CROQUET = 111
        CROSS_COUNTRY_SKI = 18
        CROSS_TRAINING = 57
        CROSSFIT = 19
        CURLING = 58
        DANCING = 20
        DIVING = 59
        ELECTRIC_BIKE = 152
        ELECTRIC_SCOOTER = 168
        ELLIPTICAL = 21
        EQUESTRIAN_SPORTS = 60
        EXERCISE_CLASS = 61
        FENCING = 62
        FIELD_HOCKEY = 113
        FISHING = 63
        FITNESS_GAMING = 64
        FOILING = 175
        FOOTBALL_AMERICAN = 65
        FOOTBALL_AUSTRALIAN = 66
        FREE_WEIGHTS = 148
        FRISBEE_PLAYING_GENERAL = 67
        FUNCTIONAL_STRENGTH_TRAINING = 68
        GARDENING = 107
        GOLF = 22
        GYMNASTICS = 69
        HANDBALL = 70
        HAND_CYCLING = 71
        HIIT = 9
        HIKING = 5
        HIP_HOP = 158
        HOCKEY = 72
        HOEING = 109
        HOUSEHOLD_CHORES = 137
        HUNTING = 73
        ICE_SKATING = 127
        INCLINE_RUN = 142
        INCLINE_WALK = 146
        INDOOR_CLIMBING = 23
        INTERVAL_WORKOUT = 24
        JAZZ_DANCE = 154
        JIU_JITSU = 160
        JUMPING_ROPE = 74
        KARATE = 159
        KAYAKING = 25
        KICKBOXING = 26
        KITESURFING = 172
        LACROSSE = 75
        MARTIAL_ARTS = 27
        MEDITATE = 28
        MODERN_DANCE = 153
        MOTOCROSS = 114
        MOTORCYCLE = 121
        MOUNTAIN_BIKE = 128
        MOWING_LAWN = 106
        MUAY_THAI = 162
        MULTISPORT = 76
        MUSICAL_PERFORMANCE = 163
        NORDIC_WALKING = 145
        ORIENTEERING = 115
        OTHER = 12
        OUTDOOR_BIKE = 29
        OUTDOOR_WORKOUT = 30
        PADDLEBOARDING = 31
        PADEL = 176
        PAINTING = 170
        PARAGLIDING = 78
        PARKOUR = 166
        PICKELBALL = 79
        PILATES = 7
        POLO = 116
        POWERLIFTING = 32
        POWER_WALKING = 143
        RACKET_SPORTS = 169
        RACQUETBALL = 80
        RESISTANCE_BANDS = 151
        ROCK_CLIMBING = 123
        ROLLERBLADING = 33
        ROLLER_SKATING = 118
        ROWING = 81
        ROWING_MACHINE = 34
        RUCKING = 144
        RUGBY = 82
        RUNNING = 1
        SAILING = 83
        SCOOTERING = 167
        SCUBA_DIVING = 84
        SHOOTING = 104
        SHOVELING = 171
        SKATEBOARDING = 117
        SKATING = 35
        SKIING = 36
        SKYDIVING = 182
        SNORKELING = 37
        SNOWBOARDING = 38
        SNOWMOBILING = 179
        SNOWSHOEING = 85
        SNOW_SPORT = 86
        SOCCER = 87
        SOFTBALL = 88
        SPEED_SKATING = 178
        SPINNING = 39
        SPORT = 40
        SQUASH = 89
        STAIRCLIMBER = 41
        STATIONARY_BIKE = 139
        STEP_TRAINING = 90
        STRENGTH_TRAINING = 11
        STRETCHING = 42
        STROLLER_WALK = 122
        SURFING = 43
        SWIMMING = 4
        SWIMMING_OPEN_WATER = 91
        SWIMMING_POOL = 101
        SYNCHRONIZED_SWIMMING = 177
        TABATA_WORKOUT = 130
        TABLE_TENNIS = 92
        TAEKWONDO = 161
        TAI_CHI = 93
        TANGO = 155
        TENNIS = 44
        TRACK_AND_FIELD = 94
        TRAIL_RUN = 141
        TRAMPOLINE = 119
        TREADMILL = 45
        TREADMILL_WALK = 138
        TRX = 131
        ULTIMATE_FRISBEE = 112
        UNICYCLING = 102
        VOLLEYBALL = 95
        VOLLEYBALL_BEACH = 120
        WAKEBOARDING = 173
        WALKING = 2
        WALK_WITH_WEIGHTS = 147
        WATER_AEROBICS = 96
        WATER_JOGGING = 126
        WATER_POLO = 97
        WATER_SKIING = 124
        WATER_SPORT = 98
        WATER_VOLLEYBALL = 125
        WEEDING = 110
        WEIGHTLIFTING = 10
        WEIGHT_MACHINES = 150
        WEIGHTS = 46
        WHEELCHAIR = 99
        WINDSURFING = 174
        WORKOUT = 8
        WRESTLING = 100
        YOGA = 6
        YOGA_BIKRAM = 132
        YOGA_HATHA = 133
        YOGA_POWER = 134
        YOGA_VINYASA = 135
        ZUMBA = 136

    class SplitSummary(proto.Message):
        r"""Represents splits or laps recorded within an exercise. Lap
        events partition a workout into segments based on criteria like
        distance, time, or calories.

        Attributes:
            start_time (google.protobuf.timestamp_pb2.Timestamp):
                Required. Lap start time
            start_utc_offset (google.protobuf.duration_pb2.Duration):
                Required. Lap start time offset from UTC
            end_time (google.protobuf.timestamp_pb2.Timestamp):
                Required. Lap end time
            end_utc_offset (google.protobuf.duration_pb2.Duration):
                Required. Lap end time offset from UTC
            active_duration (google.protobuf.duration_pb2.Duration):
                Output only. Lap time excluding the pauses.
            metrics_summary (google.devicesandservices.health_v4.types.MetricsSummary):
                Required. Summary metrics for this split.
            split_type (google.devicesandservices.health_v4.types.Exercise.SplitSummary.SplitType):
                Required. Method used to split the exercise
                laps. Users may manually mark the lap as
                complete even if the tracking is automatic.
        """

        class SplitType(proto.Enum):
            r"""The type of the split, such as manual, duration, distance,
            calories.

            Values:
                SPLIT_TYPE_UNSPECIFIED (0):
                    Split type is unspecified.
                MANUAL (1):
                    Manual split.
                DURATION (2):
                    Split by duration.
                DISTANCE (3):
                    Split by distance.
                CALORIES (4):
                    Split by calories.
            """

            SPLIT_TYPE_UNSPECIFIED = 0
            MANUAL = 1
            DURATION = 2
            DISTANCE = 3
            CALORIES = 4

        start_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=1,
            message=timestamp_pb2.Timestamp,
        )
        start_utc_offset: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=2,
            message=duration_pb2.Duration,
        )
        end_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=3,
            message=timestamp_pb2.Timestamp,
        )
        end_utc_offset: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=4,
            message=duration_pb2.Duration,
        )
        active_duration: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=5,
            message=duration_pb2.Duration,
        )
        metrics_summary: "MetricsSummary" = proto.Field(
            proto.MESSAGE,
            number=6,
            message="MetricsSummary",
        )
        split_type: "Exercise.SplitSummary.SplitType" = proto.Field(
            proto.ENUM,
            number=7,
            enum="Exercise.SplitSummary.SplitType",
        )

    class ExerciseEvent(proto.Message):
        r"""Represents instantaneous events that happen during an
        exercise, such as start, stop, pause, split.

        Attributes:
            event_time (google.protobuf.timestamp_pb2.Timestamp):
                Required. Exercise event time
            event_utc_offset (google.protobuf.duration_pb2.Duration):
                Required. Exercise event time offset from UTC
            exercise_event_type (google.devicesandservices.health_v4.types.Exercise.ExerciseEvent.ExerciseEventType):
                Required. The type of the event, such as
                start, stop, pause, resume.
        """

        class ExerciseEventType(proto.Enum):
            r"""The type of the event, such as start, stop, pause, resume.

            Values:
                EXERCISE_EVENT_TYPE_UNSPECIFIED (0):
                    Exercise event type is unspecified.
                START (1):
                    Exercise start event.
                STOP (2):
                    Exercise stop event.
                PAUSE (3):
                    Exercise pause event.
                RESUME (4):
                    Exercise resume event.
                AUTO_PAUSE (5):
                    Exercise auto-pause event.
                AUTO_RESUME (6):
                    Exercise auto-resume event.
            """

            EXERCISE_EVENT_TYPE_UNSPECIFIED = 0
            START = 1
            STOP = 2
            PAUSE = 3
            RESUME = 4
            AUTO_PAUSE = 5
            AUTO_RESUME = 6

        event_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=1,
            message=timestamp_pb2.Timestamp,
        )
        event_utc_offset: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=2,
            message=duration_pb2.Duration,
        )
        exercise_event_type: "Exercise.ExerciseEvent.ExerciseEventType" = proto.Field(
            proto.ENUM,
            number=3,
            enum="Exercise.ExerciseEvent.ExerciseEventType",
        )

    class ExerciseMetadata(proto.Message):
        r"""Additional exercise metadata.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            pool_length_millimeters (int):
                Optional. Pool length in millimeters. Only
                present in the swimming exercises.

                This field is a member of `oneof`_ ``_pool_length_millimeters``.
            has_gps (bool):
                Optional. Whether the exercise had GPS
                tracking.
        """

        pool_length_millimeters: int = proto.Field(
            proto.INT64,
            number=1,
            optional=True,
        )
        has_gps: bool = proto.Field(
            proto.BOOL,
            number=2,
        )

    interval: data_coordinates.SessionTimeInterval = proto.Field(
        proto.MESSAGE,
        number=2,
        message=data_coordinates.SessionTimeInterval,
    )
    exercise_type: ExerciseType = proto.Field(
        proto.ENUM,
        number=6,
        enum=ExerciseType,
    )
    splits: MutableSequence[SplitSummary] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message=SplitSummary,
    )
    exercise_events: MutableSequence[ExerciseEvent] = proto.RepeatedField(
        proto.MESSAGE,
        number=15,
        message=ExerciseEvent,
    )
    split_summaries: MutableSequence[SplitSummary] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message=SplitSummary,
    )
    metrics_summary: "MetricsSummary" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="MetricsSummary",
    )
    exercise_metadata: ExerciseMetadata = proto.Field(
        proto.MESSAGE,
        number=11,
        message=ExerciseMetadata,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=12,
    )
    active_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=13,
        message=duration_pb2.Duration,
    )
    notes: str = proto.Field(
        proto.STRING,
        number=14,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=16,
        message=timestamp_pb2.Timestamp,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=17,
        message=timestamp_pb2.Timestamp,
    )


class Floors(proto.Message):
    r"""Gained elevation measured in floors over the time interval

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        interval (google.devicesandservices.health_v4.types.ObservationTimeInterval):
            Required. Observed interval
        count (int):
            Required. Number of floors in the recorded interval. Must be
            in the range ``[0, 1000000]``.

            This field is a member of `oneof`_ ``_count``.
    """

    interval: data_coordinates.ObservationTimeInterval = proto.Field(
        proto.MESSAGE,
        number=2,
        message=data_coordinates.ObservationTimeInterval,
    )
    count: int = proto.Field(
        proto.INT64,
        number=4,
        optional=True,
    )


class FloorsRollupValue(proto.Message):
    r"""Represents the result of the rollup of the user's floors.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        count_sum (int):
            Sum of the floors count.

            This field is a member of `oneof`_ ``_count_sum``.
    """

    count_sum: int = proto.Field(
        proto.INT64,
        number=1,
        optional=True,
    )


class AltitudeRollupValue(proto.Message):
    r"""Represents the result of the rollup of the user's altitude.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        gain_millimeters_sum (int):
            Sum of the altitude gain in millimeters.

            This field is a member of `oneof`_ ``_gain_millimeters_sum``.
    """

    gain_millimeters_sum: int = proto.Field(
        proto.INT64,
        number=1,
        optional=True,
    )


class HeartRate(proto.Message):
    r"""A heart rate measurement.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        sample_time (google.devicesandservices.health_v4.types.ObservationSampleTime):
            Required. Observation time
        beats_per_minute (int):
            Required. The heart rate value in beats per minute. Must be
            in the range ``[1, 300]``.

            This field is a member of `oneof`_ ``_beats_per_minute``.
        metadata (google.devicesandservices.health_v4.types.HeartRate.HeartRateMetadata):
            Optional. Metadata about the heart rate
            sample.
    """

    class HeartRateMetadata(proto.Message):
        r"""Heart rate metadata.

        Attributes:
            motion_context (google.devicesandservices.health_v4.types.HeartRate.HeartRateMetadata.MotionContext):
                Optional. Indicates the user’s level of
                activity when the heart rate sample was measured
            sensor_location (google.devicesandservices.health_v4.types.HeartRate.HeartRateMetadata.SensorLocation):
                Optional. Indicates the location of the
                sensor that measured the heart rate.
        """

        class MotionContext(proto.Enum):
            r"""The user’s level of activity when the heart rate sample was
            measured.

            Values:
                MOTION_CONTEXT_UNSPECIFIED (0):
                    The default value when no data is available.
                ACTIVE (1):
                    The user is active.
                SEDENTARY (2):
                    The user is inactive.
            """

            MOTION_CONTEXT_UNSPECIFIED = 0
            ACTIVE = 1
            SEDENTARY = 2

        class SensorLocation(proto.Enum):
            r"""The location of the sensor that measured the heart rate.

            Values:
                SENSOR_LOCATION_UNSPECIFIED (0):
                    The default value when no data is available.
                CHEST (1):
                    Chest sensor.
                WRIST (2):
                    Wrist sensor.
                FINGER (3):
                    Finger sensor.
                HAND (4):
                    Hand sensor.
                EAR_LOBE (5):
                    Ear lobe sensor.
                FOOT (6):
                    Foot sensor.
            """

            SENSOR_LOCATION_UNSPECIFIED = 0
            CHEST = 1
            WRIST = 2
            FINGER = 3
            HAND = 4
            EAR_LOBE = 5
            FOOT = 6

        motion_context: "HeartRate.HeartRateMetadata.MotionContext" = proto.Field(
            proto.ENUM,
            number=1,
            enum="HeartRate.HeartRateMetadata.MotionContext",
        )
        sensor_location: "HeartRate.HeartRateMetadata.SensorLocation" = proto.Field(
            proto.ENUM,
            number=2,
            enum="HeartRate.HeartRateMetadata.SensorLocation",
        )

    sample_time: data_coordinates.ObservationSampleTime = proto.Field(
        proto.MESSAGE,
        number=2,
        message=data_coordinates.ObservationSampleTime,
    )
    beats_per_minute: int = proto.Field(
        proto.INT64,
        number=4,
        optional=True,
    )
    metadata: HeartRateMetadata = proto.Field(
        proto.MESSAGE,
        number=6,
        message=HeartRateMetadata,
    )


class HeartRateRollupValue(proto.Message):
    r"""Represents the result of the rollup of the heart rate data
    type.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        beats_per_minute_avg (float):
            The average heart rate value in the interval.

            This field is a member of `oneof`_ ``_beats_per_minute_avg``.
        beats_per_minute_max (float):
            The maximum heart rate value in the interval.

            This field is a member of `oneof`_ ``_beats_per_minute_max``.
        beats_per_minute_min (float):
            The minimum heart rate value in the interval.

            This field is a member of `oneof`_ ``_beats_per_minute_min``.
    """

    beats_per_minute_avg: float = proto.Field(
        proto.DOUBLE,
        number=1,
        optional=True,
    )
    beats_per_minute_max: float = proto.Field(
        proto.DOUBLE,
        number=2,
        optional=True,
    )
    beats_per_minute_min: float = proto.Field(
        proto.DOUBLE,
        number=3,
        optional=True,
    )


class RunVO2MaxRollupValue(proto.Message):
    r"""Represents the result of the rollup of the user's daily heart
    rate variability personal range.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        rate_min (float):
            Minimum value of run VO2 max in the
            interval..

            This field is a member of `oneof`_ ``_rate_min``.
        rate_max (float):
            Maximum value of run VO2 max in the interval.

            This field is a member of `oneof`_ ``_rate_max``.
        rate_avg (float):
            Average value of run VO2 max in the interval.

            This field is a member of `oneof`_ ``_rate_avg``.
    """

    rate_min: float = proto.Field(
        proto.DOUBLE,
        number=1,
        optional=True,
    )
    rate_max: float = proto.Field(
        proto.DOUBLE,
        number=2,
        optional=True,
    )
    rate_avg: float = proto.Field(
        proto.DOUBLE,
        number=3,
        optional=True,
    )


class RunVO2Max(proto.Message):
    r"""VO2 max value calculated based on the user's running
    activity. Value stored in ml/kg/min.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        sample_time (google.devicesandservices.health_v4.types.ObservationSampleTime):
            Required. The time at which the metric was
            measured.
        run_vo2_max (float):
            Required. Run VO2 max value in ml/kg/min. Must be in the
            range ``[0, 100]``.

            This field is a member of `oneof`_ ``_run_vo2_max``.
    """

    sample_time: data_coordinates.ObservationSampleTime = proto.Field(
        proto.MESSAGE,
        number=1,
        message=data_coordinates.ObservationSampleTime,
    )
    run_vo2_max: float = proto.Field(
        proto.DOUBLE,
        number=2,
        optional=True,
    )


class HeartRateVariabilityPersonalRangeRollupValue(proto.Message):
    r"""Represents the result of the rollup of the user's daily heart
    rate variability personal range.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        average_heart_rate_variability_milliseconds_min (float):
            The lower bound of the user's average heart
            rate variability personal range.

            This field is a member of `oneof`_ ``_average_heart_rate_variability_milliseconds_min``.
        average_heart_rate_variability_milliseconds_max (float):
            The upper bound of the user's average heart
            rate variability personal range.

            This field is a member of `oneof`_ ``_average_heart_rate_variability_milliseconds_max``.
    """

    average_heart_rate_variability_milliseconds_min: float = proto.Field(
        proto.DOUBLE,
        number=1,
        optional=True,
    )
    average_heart_rate_variability_milliseconds_max: float = proto.Field(
        proto.DOUBLE,
        number=2,
        optional=True,
    )


class Height(proto.Message):
    r"""Body height measurement.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        sample_time (google.devicesandservices.health_v4.types.ObservationSampleTime):
            Required. The time at which the height was
            recorded.
        height_millimeters (int):
            Required. Height of the user in millimeters. Must be in the
            range ``[0, 3000]``.

            This field is a member of `oneof`_ ``_height_millimeters``.
    """

    sample_time: data_coordinates.ObservationSampleTime = proto.Field(
        proto.MESSAGE,
        number=1,
        message=data_coordinates.ObservationSampleTime,
    )
    height_millimeters: int = proto.Field(
        proto.INT64,
        number=2,
        optional=True,
    )


class HeartRateVariability(proto.Message):
    r"""Captures user's heart rate variability (HRV) as measured by
    the root mean square of successive differences (RMSSD) between
    normal heartbeats or by standard deviation of the inter-beat
    intervals (SDNN).


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        sample_time (google.devicesandservices.health_v4.types.ObservationSampleTime):
            Required. The time of the heart rate
            variability measurement.
        root_mean_square_of_successive_differences_milliseconds (float):
            Optional. The root mean square of successive differences
            between normal heartbeats. This is a measure of heart rate
            variability used by Google Health. Must be in the range
            ``[1, 200]``.

            This field is a member of `oneof`_ ``_root_mean_square_of_successive_differences_milliseconds``.
        standard_deviation_milliseconds (float):
            Optional. The standard deviation of the heart
            rate variability measurement.

            This field is a member of `oneof`_ ``_standard_deviation_milliseconds``.
        metadata (google.devicesandservices.health_v4.types.HeartRateVariability.HeartRateVariabilityMetadata):
            Optional. Additional information about the
            heart rate variability measurement.
    """

    class HeartRateVariabilityMetadata(proto.Message):
        r"""Metadata for HeartRateVariability.

        Attributes:
            high_frequency_power (float):
                Optional. The power in interbeat interval
                fluctuations within the high frequency band
                (0.15 Hz - 0.4 Hz).
            low_frequency_power (float):
                Optional. The power in interbeat interval
                fluctuations within the low frequency band (0.04
                Hz - 0.15 Hz).
        """

        high_frequency_power: float = proto.Field(
            proto.DOUBLE,
            number=2,
        )
        low_frequency_power: float = proto.Field(
            proto.DOUBLE,
            number=3,
        )

    sample_time: data_coordinates.ObservationSampleTime = proto.Field(
        proto.MESSAGE,
        number=1,
        message=data_coordinates.ObservationSampleTime,
    )
    root_mean_square_of_successive_differences_milliseconds: float = proto.Field(
        proto.DOUBLE,
        number=2,
        optional=True,
    )
    standard_deviation_milliseconds: float = proto.Field(
        proto.DOUBLE,
        number=3,
        optional=True,
    )
    metadata: HeartRateVariabilityMetadata = proto.Field(
        proto.MESSAGE,
        number=4,
        message=HeartRateVariabilityMetadata,
    )


class VolumeQuantity(proto.Message):
    r"""Represents the volume quantity.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        milliliters (float):
            Required. Value representing the volume in milliliters. Must
            be in the range ``[0, 100000]``.

            This field is a member of `oneof`_ ``_milliliters``.
        user_provided_unit (google.devicesandservices.health_v4.types.VolumeUnit):
            Optional. Value representing the user
            provided unit, used only for user-facing input
            and display purposes. In the API format, all
            volume quantities are converted to milliliters.
    """

    milliliters: float = proto.Field(
        proto.DOUBLE,
        number=1,
        optional=True,
    )
    user_provided_unit: "VolumeUnit" = proto.Field(
        proto.ENUM,
        number=2,
        enum="VolumeUnit",
    )


class HydrationLog(proto.Message):
    r"""Holds information about a user logged hydration.

    Attributes:
        interval (google.devicesandservices.health_v4.types.SessionTimeInterval):
            Required. Observed interval.
        amount_consumed (google.devicesandservices.health_v4.types.VolumeQuantity):
            Required. Amount of liquid (ex. water)
            consumed.
    """

    interval: data_coordinates.SessionTimeInterval = proto.Field(
        proto.MESSAGE,
        number=1,
        message=data_coordinates.SessionTimeInterval,
    )
    amount_consumed: "VolumeQuantity" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="VolumeQuantity",
    )


class HydrationLogRollupValue(proto.Message):
    r"""Represents the result of the rollup of the hydration log data
    type.

    Attributes:
        amount_consumed (google.devicesandservices.health_v4.types.HydrationLogRollupValue.VolumeQuantityRollup):
            Rollup for amount consumed.
    """

    class VolumeQuantityRollup(proto.Message):
        r"""Rollup for volume quantity.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            milliliters_sum (float):
                Required. The sum of volume in milliliters.

                This field is a member of `oneof`_ ``_milliliters_sum``.
            user_provided_unit_last (google.devicesandservices.health_v4.types.VolumeUnit):
                Optional. The user provided unit on the last
                element.
        """

        milliliters_sum: float = proto.Field(
            proto.DOUBLE,
            number=1,
            optional=True,
        )
        user_provided_unit_last: "VolumeUnit" = proto.Field(
            proto.ENUM,
            number=2,
            enum="VolumeUnit",
        )

    amount_consumed: VolumeQuantityRollup = proto.Field(
        proto.MESSAGE,
        number=1,
        message=VolumeQuantityRollup,
    )


class IrregularRhythmNotification(proto.Message):
    r"""Represents an Irregular Rhythm Notification alert, indicating
    a potential sign of atrial fibrillation (AFib).
    This data type is based on SaMD feature and any changes to it
    may require additional review.

    Attributes:
        interval (google.devicesandservices.health_v4.types.SessionTimeInterval):
            Required. Observed interval.
        alert_windows (MutableSequence[google.devicesandservices.health_v4.types.IrregularRhythmNotification.AlertWindow]):
            Optional. The overlapping analysis windows
            that were used to evaluate rhythm for potential
            AFib, containing specific information about the
            user's heart rhythm.
        medical_device_info (google.devicesandservices.health_v4.types.MedicalDeviceInfo):
            Output only. The meta information for the compatible device
            used to conduct the measurement.

            Irregular Rhythm Notification measurements typically
            populate ``algorithm_version``, ``service_version``, and
            ``device_model``.
    """

    class HeartBeat(proto.Message):
        r"""A single heart beat measurement.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            physical_time (google.protobuf.timestamp_pb2.Timestamp):
                Required. The time of the heart beat
                measurement.
            utc_offset (google.protobuf.duration_pb2.Duration):
                Required. The UTC offset of the user's
                timezone when the heart beat measurement
                occurred.
            civil_time (google.devicesandservices.health_v4.types.CivilDateTime):
                Output only. The civil time in the timezone
                the subject is in at the time of the
                observation.
            beats_per_minute (int):
                Required. The beats-per-minute value
                extrapolated from the time before the following
                heart beat. This is calculated as 60000 / rr,
                where rr is the gap between heart beats in
                milliseconds (IBI - Interbeat Interval).

                This field is a member of `oneof`_ ``_beats_per_minute``.
        """

        physical_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=1,
            message=timestamp_pb2.Timestamp,
        )
        utc_offset: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=2,
            message=duration_pb2.Duration,
        )
        civil_time: data_coordinates.CivilDateTime = proto.Field(
            proto.MESSAGE,
            number=3,
            message=data_coordinates.CivilDateTime,
        )
        beats_per_minute: int = proto.Field(
            proto.INT32,
            number=4,
            optional=True,
        )

    class AlertWindow(proto.Message):
        r"""An analysis window evaluated for AFib.

        Note: The current version of the algorithm will only produce
        alerts if all windows are positive. So anything returned from
        the API will always have the positive bit set to true.
        Internally, windows can be negative, however. We never save
        "inconclusive" windows (they aren't produced by the algorithm).

        Attributes:
            start_time (google.protobuf.timestamp_pb2.Timestamp):
                Required. Observed interval.
                The start time of the analysis window.
            start_utc_offset (google.protobuf.duration_pb2.Duration):
                Required. The UTC offset of the user's
                timezone when the analysis window started.
            end_time (google.protobuf.timestamp_pb2.Timestamp):
                Required. The end time of the analysis
                window.
            end_utc_offset (google.protobuf.duration_pb2.Duration):
                Required. The UTC offset of the user's
                timezone when the analysis window ended.
            civil_start_time (google.devicesandservices.health_v4.types.CivilDateTime):
                Output only. Observed interval start time in
                civil time in the timezone the subject is in at
                the start of the observed interval
            civil_end_time (google.devicesandservices.health_v4.types.CivilDateTime):
                Output only. Observed interval end time in
                civil time in the timezone the subject is in at
                the end of the observed interval
            positive (bool):
                Optional. Flag indicating whether the window was positive
                for AFib or not. A ``true`` value indicates that AFib was
                detected in this window. A ``false`` value means AFib was
                not detected, but does not guarantee the absence of AFib.
            heart_beats (MutableSequence[google.devicesandservices.health_v4.types.IrregularRhythmNotification.HeartBeat]):
                Optional. All heart beats in the interval
                contained in this analysis window.
        """

        start_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=1,
            message=timestamp_pb2.Timestamp,
        )
        start_utc_offset: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=2,
            message=duration_pb2.Duration,
        )
        end_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=3,
            message=timestamp_pb2.Timestamp,
        )
        end_utc_offset: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=4,
            message=duration_pb2.Duration,
        )
        civil_start_time: data_coordinates.CivilDateTime = proto.Field(
            proto.MESSAGE,
            number=5,
            message=data_coordinates.CivilDateTime,
        )
        civil_end_time: data_coordinates.CivilDateTime = proto.Field(
            proto.MESSAGE,
            number=6,
            message=data_coordinates.CivilDateTime,
        )
        positive: bool = proto.Field(
            proto.BOOL,
            number=7,
        )
        heart_beats: MutableSequence["IrregularRhythmNotification.HeartBeat"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=8,
                message="IrregularRhythmNotification.HeartBeat",
            )
        )

    interval: data_coordinates.SessionTimeInterval = proto.Field(
        proto.MESSAGE,
        number=1,
        message=data_coordinates.SessionTimeInterval,
    )
    alert_windows: MutableSequence[AlertWindow] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message=AlertWindow,
    )
    medical_device_info: gdh_medical_device_info.MedicalDeviceInfo = proto.Field(
        proto.MESSAGE,
        number=6,
        message=gdh_medical_device_info.MedicalDeviceInfo,
    )


class MetricsSummary(proto.Message):
    r"""Summary metrics for an exercise.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        calories_kcal (float):
            Optional. Total calories burned by the user
            during the exercise.

            This field is a member of `oneof`_ ``_calories_kcal``.
        distance_millimeters (float):
            Optional. Total distance covered by the user
            during the exercise.

            This field is a member of `oneof`_ ``_distance_millimeters``.
        steps (int):
            Optional. Total steps taken during the
            exercise.

            This field is a member of `oneof`_ ``_steps``.
        average_speed_millimeters_per_second (float):
            Optional. Average speed in millimeters per
            second.

            This field is a member of `oneof`_ ``_average_speed_millimeters_per_second``.
        average_pace_seconds_per_meter (float):
            Optional. Average pace in seconds per meter.

            This field is a member of `oneof`_ ``_average_pace_seconds_per_meter``.
        average_heart_rate_beats_per_minute (int):
            Optional. Average heart rate during the
            exercise.

            This field is a member of `oneof`_ ``_average_heart_rate_beats_per_minute``.
        elevation_gain_millimeters (float):
            Optional. Total elevation gain during the
            exercise.

            This field is a member of `oneof`_ ``_elevation_gain_millimeters``.
        active_zone_minutes (int):
            Optional. Total active zone minutes for the
            exercise.

            This field is a member of `oneof`_ ``_active_zone_minutes``.
        run_vo2_max (float):
            Optional. Run VO2 max value for the exercise.
            Only present in the running exercises at the top
            level as in the summary of the whole exercise.

            This field is a member of `oneof`_ ``_run_vo2_max``.
        total_swim_lengths (float):
            Optional. Number of full pool lengths
            completed during the exercise. Only present in
            the swimming exercises at the top level as in
            the summary of the whole exercise.

            This field is a member of `oneof`_ ``_total_swim_lengths``.
        heart_rate_zone_durations (google.devicesandservices.health_v4.types.MetricsSummary.TimeInHeartRateZones):
            Optional. Time spent in each heart rate zone.
        mobility_metrics (google.devicesandservices.health_v4.types.MetricsSummary.MobilityMetrics):
            Optional. Mobility workouts specific metrics.
            Only present in the advanced running exercises.
    """

    class TimeInHeartRateZones(proto.Message):
        r"""Time spent in each heart rate zone.

        Attributes:
            light_time (google.protobuf.duration_pb2.Duration):
                Optional. Time spent in light heart rate
                zone.
            moderate_time (google.protobuf.duration_pb2.Duration):
                Optional. Time spent in moderate heart rate
                zone.
            vigorous_time (google.protobuf.duration_pb2.Duration):
                Optional. Time spent in vigorous heart rate
                zone.
            peak_time (google.protobuf.duration_pb2.Duration):
                Optional. Time spent in peak heart rate zone.
        """

        light_time: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=1,
            message=duration_pb2.Duration,
        )
        moderate_time: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=2,
            message=duration_pb2.Duration,
        )
        vigorous_time: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=3,
            message=duration_pb2.Duration,
        )
        peak_time: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=4,
            message=duration_pb2.Duration,
        )

    class MobilityMetrics(proto.Message):
        r"""Mobility workouts specific metrics

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            avg_cadence_steps_per_minute (float):
                Optional. Cadence is a measure of the
                frequency of your foot strikes. Steps / min in
                real time during workout.

                This field is a member of `oneof`_ ``_avg_cadence_steps_per_minute``.
            avg_stride_length_millimeters (int):
                Optional. Stride length is a measure of the
                distance covered by a single stride

                This field is a member of `oneof`_ ``_avg_stride_length_millimeters``.
            avg_vertical_oscillation_millimeters (int):
                Optional. Distance off the ground your center
                of mass moves with each stride while running

                This field is a member of `oneof`_ ``_avg_vertical_oscillation_millimeters``.
            avg_vertical_ratio (float):
                Optional. Vertical oscillation/stride length between [5.0,
                11.0].

                This field is a member of `oneof`_ ``_avg_vertical_ratio``.
            avg_ground_contact_time_duration (google.protobuf.duration_pb2.Duration):
                Optional. The ground contact time for a
                particular stride is the amount of time for
                which the foot was in contact with the ground on
                that stride
        """

        avg_cadence_steps_per_minute: float = proto.Field(
            proto.DOUBLE,
            number=1,
            optional=True,
        )
        avg_stride_length_millimeters: int = proto.Field(
            proto.INT64,
            number=2,
            optional=True,
        )
        avg_vertical_oscillation_millimeters: int = proto.Field(
            proto.INT64,
            number=3,
            optional=True,
        )
        avg_vertical_ratio: float = proto.Field(
            proto.DOUBLE,
            number=4,
            optional=True,
        )
        avg_ground_contact_time_duration: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=5,
            message=duration_pb2.Duration,
        )

    calories_kcal: float = proto.Field(
        proto.DOUBLE,
        number=1,
        optional=True,
    )
    distance_millimeters: float = proto.Field(
        proto.DOUBLE,
        number=2,
        optional=True,
    )
    steps: int = proto.Field(
        proto.INT64,
        number=3,
        optional=True,
    )
    average_speed_millimeters_per_second: float = proto.Field(
        proto.DOUBLE,
        number=4,
        optional=True,
    )
    average_pace_seconds_per_meter: float = proto.Field(
        proto.DOUBLE,
        number=5,
        optional=True,
    )
    average_heart_rate_beats_per_minute: int = proto.Field(
        proto.INT64,
        number=6,
        optional=True,
    )
    elevation_gain_millimeters: float = proto.Field(
        proto.DOUBLE,
        number=7,
        optional=True,
    )
    active_zone_minutes: int = proto.Field(
        proto.INT64,
        number=9,
        optional=True,
    )
    run_vo2_max: float = proto.Field(
        proto.DOUBLE,
        number=10,
        optional=True,
    )
    total_swim_lengths: float = proto.Field(
        proto.DOUBLE,
        number=11,
        optional=True,
    )
    heart_rate_zone_durations: TimeInHeartRateZones = proto.Field(
        proto.MESSAGE,
        number=12,
        message=TimeInHeartRateZones,
    )
    mobility_metrics: MobilityMetrics = proto.Field(
        proto.MESSAGE,
        number=13,
        message=MobilityMetrics,
    )


class WeightQuantity(proto.Message):
    r"""Represents the weight quantity.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        grams (float):
            Required. The weight value in grams. Must be in the range
            ``[0, 100000]``.

            This field is a member of `oneof`_ ``_grams``.
        user_provided_unit (google.devicesandservices.health_v4.types.WeightUnit):
            Optional. Value representing the user
            provided unit.
    """

    grams: float = proto.Field(
        proto.DOUBLE,
        number=1,
        optional=True,
    )
    user_provided_unit: "WeightUnit" = proto.Field(
        proto.ENUM,
        number=2,
        enum="WeightUnit",
    )


class EnergyQuantity(proto.Message):
    r"""Represents the energy quantity.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        kcal (float):
            Required. The energy value in kilocalories. Must be in the
            range ``[0, 100000]``.

            This field is a member of `oneof`_ ``_kcal``.
        user_provided_unit (google.devicesandservices.health_v4.types.EnergyUnit):
            Optional. Value representing the user
            provided unit.
    """

    kcal: float = proto.Field(
        proto.DOUBLE,
        number=1,
        optional=True,
    )
    user_provided_unit: "EnergyUnit" = proto.Field(
        proto.ENUM,
        number=2,
        enum="EnergyUnit",
    )


class NutrientQuantity(proto.Message):
    r"""Represents the quantity of a nutrient.

    Attributes:
        quantity (google.devicesandservices.health_v4.types.WeightQuantity):
            Required. The quantity of the nutrient,
            measured in grams.
        nutrient (google.devicesandservices.health_v4.types.Nutrient):
            Required. The nutrient type.
    """

    quantity: "WeightQuantity" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="WeightQuantity",
    )
    nutrient: "Nutrient" = proto.Field(
        proto.ENUM,
        number=2,
        enum="Nutrient",
    )


class NutritionLog(proto.Message):
    r"""Holds information about food logged by a user.

    There are two ways of creating a nutrition log based on the food
    type:

    1. Identified food: Using the food field, which is a reference to a
       Food resource. In this case fields ``nutrients``, ``energy``,
       ``energy_from_fat``, ``total_carbohydrate``, ``total_fat``,
       ``food_display_name`` will be populated based on the referenced
       food.
    2. Anonymous food: Using the ``food_display_name`` field and setting
       the ``nutrients``, ``energy``, ``energy_from_fat``,
       ``total_carbohydrate``, ``total_fat`` fields manually.

    The identified food is preferred over the anonymous food. Nutrition
    logs created from anonymous food are not editable.

    Attributes:
        interval (google.devicesandservices.health_v4.types.SessionTimeInterval):
            Required. The time window when the food was
            logged.
        nutrients (MutableSequence[google.devicesandservices.health_v4.types.NutrientQuantity]):
            Optional. An array of individual nutrient
            values for the nutrition log.
        energy (google.devicesandservices.health_v4.types.EnergyQuantity):
            Optional. The total energy of the food, measured in
            kilocalories (``kcal``).
        energy_from_fat (google.devicesandservices.health_v4.types.EnergyQuantity):
            Optional. The energy from fat, measured in kilocalories
            (``kcal``).
        total_carbohydrate (google.devicesandservices.health_v4.types.WeightQuantity):
            Optional. The total carbohydrate content,
            measured in grams.
        total_fat (google.devicesandservices.health_v4.types.WeightQuantity):
            Optional. The total fat content, measured in
            grams.
        meal_type (google.devicesandservices.health_v4.types.MealType):
            Optional. The meal category. One of ``BREAKFAST``,
            ``LUNCH``, ``DINNER``, or ``SNACK``.
        serving (google.devicesandservices.health_v4.types.NutritionLog.Serving):
            Optional. The serving information for the
            logged food.
        food (str):
            Optional. The resource name of the Food item. Required when
            creating a nutrition log from an identified food. For
            anonymous food logs, use the ``food_display_name`` field
            instead.
        food_display_name (str):
            The display name of the food. For identified
            food logs, this is populated automatically from
            the referenced food.
    """

    class Serving(proto.Message):
        r"""Represents different properties and information about the
        serving of a specific food.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            amount (float):
                Optional. The number of servings.

                This field is a member of `oneof`_ ``_amount``.
            food_measurement_unit (str):
                Required. Food measurement unit
            food_measurement_unit_display_name (str):
                Output only. Legacy measurement unit for
                serving size in singular form (e.g. "piece",
                "gram").
        """

        amount: float = proto.Field(
            proto.DOUBLE,
            number=1,
            optional=True,
        )
        food_measurement_unit: str = proto.Field(
            proto.STRING,
            number=2,
        )
        food_measurement_unit_display_name: str = proto.Field(
            proto.STRING,
            number=3,
        )

    interval: data_coordinates.SessionTimeInterval = proto.Field(
        proto.MESSAGE,
        number=2,
        message=data_coordinates.SessionTimeInterval,
    )
    nutrients: MutableSequence["NutrientQuantity"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="NutrientQuantity",
    )
    energy: "EnergyQuantity" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="EnergyQuantity",
    )
    energy_from_fat: "EnergyQuantity" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="EnergyQuantity",
    )
    total_carbohydrate: "WeightQuantity" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="WeightQuantity",
    )
    total_fat: "WeightQuantity" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="WeightQuantity",
    )
    meal_type: "MealType" = proto.Field(
        proto.ENUM,
        number=13,
        enum="MealType",
    )
    serving: Serving = proto.Field(
        proto.MESSAGE,
        number=14,
        message=Serving,
    )
    food: str = proto.Field(
        proto.STRING,
        number=15,
    )
    food_display_name: str = proto.Field(
        proto.STRING,
        number=16,
    )


class Food(proto.Message):
    r"""Represents a food item.

    Attributes:
        display_name (str):
            Required. The display name of the food.
        brand (str):
            Optional. The brand of the food.
        access_level (google.devicesandservices.health_v4.types.FoodAccessLevel):
            Required. The access level of the food.
        description (str):
            Optional. The description of the food.
        language_code (str):
            Optional. The language code where the food is available in
            format xx-XX. Supported values are defined in
            [Settings.food_language_code][google.devicesandservices.health.v4.Settings.food_language_code].
        meal_type (google.devicesandservices.health_v4.types.MealType):
            Optional. The meal type associated with this
            food.
        nutrients (MutableSequence[google.devicesandservices.health_v4.types.NutrientQuantity]):
            Optional. Value representing the nutrients of
            the food for the default serving.
        energy_from_fat (google.devicesandservices.health_v4.types.EnergyQuantity):
            Optional. Value representing the energy from
            fat of the food for the default serving.
        total_carbohydrate (google.devicesandservices.health_v4.types.WeightQuantity):
            Optional. Value representing the total
            carbohydrate of the food for the default
            serving.
        total_fat (google.devicesandservices.health_v4.types.WeightQuantity):
            Optional. Value representing the total fat of
            the food for the default serving.
        energy_min (google.devicesandservices.health_v4.types.EnergyQuantity):
            Optional. Value representing the minimum
            energy of the food for the default serving.
        energy_avg (google.devicesandservices.health_v4.types.EnergyQuantity):
            Optional. Value representing the average
            energy of the food for the default serving.
        energy_max (google.devicesandservices.health_v4.types.EnergyQuantity):
            Optional. Value representing the maximum
            energy of the food for the default serving.
        default_serving (google.devicesandservices.health_v4.types.Food.FoodServing):
            Required. Value representing the default
            serving of the food.
        servings (MutableSequence[google.devicesandservices.health_v4.types.Food.FoodServing]):
            Optional. The serving of the food.
    """

    class FoodServing(proto.Message):
        r"""Represents different properties and information about the
        serving of a specific food.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            amount (float):
                Optional. Amount of food consumed, fractional
                values are supported.

                This field is a member of `oneof`_ ``_amount``.
            food_measurement_unit (str):
                Required. Food measurement unit
            food_measurement_unit_display_name (str):
                Output only. Legacy measurement unit for
                serving size in singular form (e.g. "piece",
                "gram").
            food_measurement_unit_display_name_plural (str):
                Output only. Legacy measurement unit for
                serving size in plural form (e.g. "pieces",
                "grams").
            multiplier (float):
                Optional. Value representing the multiplier
                used to compute the energy when using this
                serving instead of the default serving.
        """

        amount: float = proto.Field(
            proto.DOUBLE,
            number=1,
            optional=True,
        )
        food_measurement_unit: str = proto.Field(
            proto.STRING,
            number=2,
        )
        food_measurement_unit_display_name: str = proto.Field(
            proto.STRING,
            number=3,
        )
        food_measurement_unit_display_name_plural: str = proto.Field(
            proto.STRING,
            number=4,
        )
        multiplier: float = proto.Field(
            proto.DOUBLE,
            number=5,
        )

    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    brand: str = proto.Field(
        proto.STRING,
        number=3,
    )
    access_level: "FoodAccessLevel" = proto.Field(
        proto.ENUM,
        number=4,
        enum="FoodAccessLevel",
    )
    description: str = proto.Field(
        proto.STRING,
        number=5,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=6,
    )
    meal_type: "MealType" = proto.Field(
        proto.ENUM,
        number=10,
        enum="MealType",
    )
    nutrients: MutableSequence["NutrientQuantity"] = proto.RepeatedField(
        proto.MESSAGE,
        number=12,
        message="NutrientQuantity",
    )
    energy_from_fat: "EnergyQuantity" = proto.Field(
        proto.MESSAGE,
        number=13,
        message="EnergyQuantity",
    )
    total_carbohydrate: "WeightQuantity" = proto.Field(
        proto.MESSAGE,
        number=14,
        message="WeightQuantity",
    )
    total_fat: "WeightQuantity" = proto.Field(
        proto.MESSAGE,
        number=15,
        message="WeightQuantity",
    )
    energy_min: "EnergyQuantity" = proto.Field(
        proto.MESSAGE,
        number=16,
        message="EnergyQuantity",
    )
    energy_avg: "EnergyQuantity" = proto.Field(
        proto.MESSAGE,
        number=17,
        message="EnergyQuantity",
    )
    energy_max: "EnergyQuantity" = proto.Field(
        proto.MESSAGE,
        number=18,
        message="EnergyQuantity",
    )
    default_serving: FoodServing = proto.Field(
        proto.MESSAGE,
        number=19,
        message=FoodServing,
    )
    servings: MutableSequence[FoodServing] = proto.RepeatedField(
        proto.MESSAGE,
        number=20,
        message=FoodServing,
    )


class NutritionLogRollupValue(proto.Message):
    r"""Represents the result of the rollup of the nutrition log data
    type.

    Attributes:
        nutrients (MutableSequence[google.devicesandservices.health_v4.types.NutritionLogRollupValue.NutrientQuantityRollup]):
            List of the nutrient roll-ups by the nutrient
            type.
        energy (google.devicesandservices.health_v4.types.NutritionLogRollupValue.EnergyQuantityRollup):
            Energy rollup.
        energy_from_fat (google.devicesandservices.health_v4.types.NutritionLogRollupValue.EnergyQuantityRollup):
            Value
            Energy from fat rollup.
        total_carbohydrate (google.devicesandservices.health_v4.types.NutritionLogRollupValue.WeightQuantityRollup):
            Total carbohydrate rollup.
        total_fat (google.devicesandservices.health_v4.types.NutritionLogRollupValue.WeightQuantityRollup):
            Total fat rollup.
    """

    class WeightQuantityRollup(proto.Message):
        r"""Rollup for the weight.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            grams_sum (float):
                Required. The sum of the weight in grams.

                This field is a member of `oneof`_ ``_grams_sum``.
            user_provided_unit_last (google.devicesandservices.health_v4.types.WeightUnit):
                Optional. The user provided unit on the last
                element.
        """

        grams_sum: float = proto.Field(
            proto.DOUBLE,
            number=1,
            optional=True,
        )
        user_provided_unit_last: "WeightUnit" = proto.Field(
            proto.ENUM,
            number=2,
            enum="WeightUnit",
        )

    class EnergyQuantityRollup(proto.Message):
        r"""Rollup for the energy quantity.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            kcal_sum (float):
                Required. The sum of the energy in
                kilocalories.

                This field is a member of `oneof`_ ``_kcal_sum``.
            user_provided_unit_last (google.devicesandservices.health_v4.types.EnergyUnit):
                Optional. The user provided unit on the last
                element.
        """

        kcal_sum: float = proto.Field(
            proto.DOUBLE,
            number=1,
            optional=True,
        )
        user_provided_unit_last: "EnergyUnit" = proto.Field(
            proto.ENUM,
            number=2,
            enum="EnergyUnit",
        )

    class NutrientQuantityRollup(proto.Message):
        r"""Nutrient quantity rollup.

        Attributes:
            quantity (google.devicesandservices.health_v4.types.NutritionLogRollupValue.WeightQuantityRollup):
                Required. Aggregated nutrient weight.
            nutrient (google.devicesandservices.health_v4.types.Nutrient):
                Required. Aggregated nutrient.
        """

        quantity: "NutritionLogRollupValue.WeightQuantityRollup" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="NutritionLogRollupValue.WeightQuantityRollup",
        )
        nutrient: "Nutrient" = proto.Field(
            proto.ENUM,
            number=2,
            enum="Nutrient",
        )

    nutrients: MutableSequence[NutrientQuantityRollup] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=NutrientQuantityRollup,
    )
    energy: EnergyQuantityRollup = proto.Field(
        proto.MESSAGE,
        number=2,
        message=EnergyQuantityRollup,
    )
    energy_from_fat: EnergyQuantityRollup = proto.Field(
        proto.MESSAGE,
        number=3,
        message=EnergyQuantityRollup,
    )
    total_carbohydrate: WeightQuantityRollup = proto.Field(
        proto.MESSAGE,
        number=4,
        message=WeightQuantityRollup,
    )
    total_fat: WeightQuantityRollup = proto.Field(
        proto.MESSAGE,
        number=5,
        message=WeightQuantityRollup,
    )


class OxygenSaturation(proto.Message):
    r"""Captures the user's instantaneous oxygen saturation
    percentage (SpO2).


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        sample_time (google.devicesandservices.health_v4.types.ObservationSampleTime):
            Required. The time at which oxygen saturation
            was measured.
        percentage (float):
            Required. The oxygen saturation percentage. Must be in the
            range ``[0, 100]``.

            This field is a member of `oneof`_ ``_percentage``.
    """

    sample_time: data_coordinates.ObservationSampleTime = proto.Field(
        proto.MESSAGE,
        number=1,
        message=data_coordinates.ObservationSampleTime,
    )
    percentage: float = proto.Field(
        proto.DOUBLE,
        number=2,
        optional=True,
    )


class RestingHeartRatePersonalRangeRollupValue(proto.Message):
    r"""Represents the rollup value for the daily resting heart rate
    data type.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        beats_per_minute_min (float):
            The lower bound of the user's daily resting
            heart rate personal range.

            This field is a member of `oneof`_ ``_beats_per_minute_min``.
        beats_per_minute_max (float):
            The upper bound of the user's daily resting
            heart rate personal range.

            This field is a member of `oneof`_ ``_beats_per_minute_max``.
    """

    beats_per_minute_min: float = proto.Field(
        proto.DOUBLE,
        number=1,
        optional=True,
    )
    beats_per_minute_max: float = proto.Field(
        proto.DOUBLE,
        number=2,
        optional=True,
    )


class FoodMeasurementUnit(proto.Message):
    r"""Represents a food measurement unit.

    Attributes:
        display_name (str):
            Required. The display name of the food
            measurement unit (e.g., "gram", "piece").
        plural_display_name (str):
            Optional. The plural display name of the food
            measurement unit (e.g., "grams", "pieces").
    """

    display_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    plural_display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )


class RespiratoryRateSleepSummary(proto.Message):
    r"""Records respiratory rate details during sleep.
    Can have multiple per day if the user sleeps multiple times.

    Attributes:
        sample_time (google.devicesandservices.health_v4.types.ObservationSampleTime):
            Required. The time at which respiratory rate
            was measured.
        deep_sleep_stats (google.devicesandservices.health_v4.types.RespiratoryRateSleepSummary.RespiratoryRateSleepSummaryStatistics):
            Optional. Respiratory rate statistics for
            deep sleep.
        light_sleep_stats (google.devicesandservices.health_v4.types.RespiratoryRateSleepSummary.RespiratoryRateSleepSummaryStatistics):
            Optional. Respiratory rate statistics for
            light sleep.
        rem_sleep_stats (google.devicesandservices.health_v4.types.RespiratoryRateSleepSummary.RespiratoryRateSleepSummaryStatistics):
            Optional. Respiratory rate statistics for REM
            sleep.
        full_sleep_stats (google.devicesandservices.health_v4.types.RespiratoryRateSleepSummary.RespiratoryRateSleepSummaryStatistics):
            Required. Full respiratory rate statistics.
    """

    class RespiratoryRateSleepSummaryStatistics(proto.Message):
        r"""Respiratory rate statistics for a given sleep stage.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            breaths_per_minute (float):
                Required. Average breaths per minute.

                This field is a member of `oneof`_ ``_breaths_per_minute``.
            standard_deviation (float):
                Optional. Standard deviation of the
                respiratory rate during sleep.

                This field is a member of `oneof`_ ``_standard_deviation``.
            signal_to_noise (float):
                Optional. How trustworthy the data is for the
                computation.

                This field is a member of `oneof`_ ``_signal_to_noise``.
        """

        breaths_per_minute: float = proto.Field(
            proto.DOUBLE,
            number=1,
            optional=True,
        )
        standard_deviation: float = proto.Field(
            proto.DOUBLE,
            number=2,
            optional=True,
        )
        signal_to_noise: float = proto.Field(
            proto.DOUBLE,
            number=3,
            optional=True,
        )

    sample_time: data_coordinates.ObservationSampleTime = proto.Field(
        proto.MESSAGE,
        number=1,
        message=data_coordinates.ObservationSampleTime,
    )
    deep_sleep_stats: RespiratoryRateSleepSummaryStatistics = proto.Field(
        proto.MESSAGE,
        number=2,
        message=RespiratoryRateSleepSummaryStatistics,
    )
    light_sleep_stats: RespiratoryRateSleepSummaryStatistics = proto.Field(
        proto.MESSAGE,
        number=3,
        message=RespiratoryRateSleepSummaryStatistics,
    )
    rem_sleep_stats: RespiratoryRateSleepSummaryStatistics = proto.Field(
        proto.MESSAGE,
        number=4,
        message=RespiratoryRateSleepSummaryStatistics,
    )
    full_sleep_stats: RespiratoryRateSleepSummaryStatistics = proto.Field(
        proto.MESSAGE,
        number=5,
        message=RespiratoryRateSleepSummaryStatistics,
    )


class Sleep(proto.Message):
    r"""A sleep session possibly including stages.

    Attributes:
        interval (google.devicesandservices.health_v4.types.SessionTimeInterval):
            Required. Observed sleep interval.
        type_ (google.devicesandservices.health_v4.types.Sleep.SleepType):
            Optional. SleepType: classic or stages.
        stages (MutableSequence[google.devicesandservices.health_v4.types.Sleep.SleepStage]):
            Optional. List of non-overlapping contiguous
            sleep stage segments that cover the sleep
            period.
        out_of_bed_segments (MutableSequence[google.devicesandservices.health_v4.types.Sleep.OutOfBedSegment]):
            Optional.
            “Out of bed” segments that can overlap with
            sleep stages.
        metadata (google.devicesandservices.health_v4.types.Sleep.SleepMetadata):
            Optional. Sleep metadata: ``processed``, ``main_sleep``,
            ``manually_edited``, and ``stages_status``.
        summary (google.devicesandservices.health_v4.types.Sleep.SleepSummary):
            Output only. Sleep summary: metrics and
            stages summary.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Creation time of this sleep
            observation.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Last update time of this sleep
            observation.
        short_awakenings (MutableSequence[google.devicesandservices.health_v4.types.Sleep.SleepStage]):
            Output only. List of short awake segments
            (under a set threshold) that are part of the
            sleep session. These can overlap with sleep
            stages.
    """

    class SleepType(proto.Enum):
        r"""Sleep type: classic or stages.

        Values:
            SLEEP_TYPE_UNSPECIFIED (0):
                Sleep type is unspecified.
            CLASSIC (1):
                Classic sleep is a sleep with 3 stages types:
                AWAKE, RESTLESS and ASLEEP.
            STAGES (2):
                On top of "classic" sleep stages an
                additional processing pass can calculate stages
                more precisely, overwriting the prior stages
                with AWAKE, LIGHT, REM and DEEP.
        """

        SLEEP_TYPE_UNSPECIFIED = 0
        CLASSIC = 1
        STAGES = 2

    class SleepStageType(proto.Enum):
        r"""Sleep stage type: AWAKE, DEEP, REM, LIGHT etc.

        Values:
            SLEEP_STAGE_TYPE_UNSPECIFIED (0):
                The default unset value.
            AWAKE (1):
                Sleep stage AWAKE.
            LIGHT (2):
                Sleep stage LIGHT.
            DEEP (3):
                Sleep stage DEEP.
            REM (4):
                Sleep stage REM.
            ASLEEP (5):
                Sleep stage ASLEEP.
            RESTLESS (6):
                Sleep stage RESTLESS.
        """

        SLEEP_STAGE_TYPE_UNSPECIFIED = 0
        AWAKE = 1
        LIGHT = 2
        DEEP = 3
        REM = 4
        ASLEEP = 5
        RESTLESS = 6

    class SleepStage(proto.Message):
        r"""Sleep stage segment.

        Attributes:
            start_time (google.protobuf.timestamp_pb2.Timestamp):
                Required. Sleep stage start time.
            start_utc_offset (google.protobuf.duration_pb2.Duration):
                Required. The offset of the user's local time
                at the start of the sleep stage relative to the
                Coordinated Universal Time (UTC).
            end_time (google.protobuf.timestamp_pb2.Timestamp):
                Required. Sleep stage end time.
            end_utc_offset (google.protobuf.duration_pb2.Duration):
                Required. The offset of the user's local time
                at the end of the sleep stage relative to the
                Coordinated Universal Time (UTC).
            type_ (google.devicesandservices.health_v4.types.Sleep.SleepStageType):
                Required. Sleep stage type: AWAKE, DEEP, REM,
                LIGHT etc.
            create_time (google.protobuf.timestamp_pb2.Timestamp):
                Output only. Creation time of this sleep
                stages segment.
            update_time (google.protobuf.timestamp_pb2.Timestamp):
                Output only. Last update time of this sleep
                stages segment.
        """

        start_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=3,
            message=timestamp_pb2.Timestamp,
        )
        start_utc_offset: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=4,
            message=duration_pb2.Duration,
        )
        end_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=5,
            message=timestamp_pb2.Timestamp,
        )
        end_utc_offset: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=6,
            message=duration_pb2.Duration,
        )
        type_: "Sleep.SleepStageType" = proto.Field(
            proto.ENUM,
            number=7,
            enum="Sleep.SleepStageType",
        )
        create_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=8,
            message=timestamp_pb2.Timestamp,
        )
        update_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=9,
            message=timestamp_pb2.Timestamp,
        )

    class OutOfBedSegment(proto.Message):
        r"""A time interval to represent an out-of-bed segment.

        Attributes:
            start_time (google.protobuf.timestamp_pb2.Timestamp):
                Required. Segment tart time.
            start_utc_offset (google.protobuf.duration_pb2.Duration):
                Required. The offset of the user's local time
                at the start of the segment relative to the
                Coordinated Universal Time (UTC).
            end_time (google.protobuf.timestamp_pb2.Timestamp):
                Required. Segment end time.
            end_utc_offset (google.protobuf.duration_pb2.Duration):
                Required. The offset of the user's local time
                at the end of the segment relative to the
                Coordinated Universal Time (UTC).
        """

        start_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=1,
            message=timestamp_pb2.Timestamp,
        )
        start_utc_offset: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=2,
            message=duration_pb2.Duration,
        )
        end_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=3,
            message=timestamp_pb2.Timestamp,
        )
        end_utc_offset: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=4,
            message=duration_pb2.Duration,
        )

    class SleepMetadata(proto.Message):
        r"""Additional information about how the sleep was processed.

        Attributes:
            stages_status (google.devicesandservices.health_v4.types.Sleep.SleepMetadata.StagesState):
                Output only. Sleep stages algorithm
                processing status.
            processed (bool):
                Output only. Sleep and sleep stages algorithms finished
                processing. A ``true`` value indicates whether all data
                processing for the session is complete. A ``false`` value
                means sleep period is detected but sleep stages is still
                processing.
            nap (bool):
                Output only. Naps are sleeps without stages
                and relatively short durations.
            manually_edited (bool):
                Output only. Some sleeps autodetected by
                algorithms can be manually edited by users.
            external_id (str):
                Optional. Sleep identifier relevant in the
                context of the data source.
            main_sleep (bool):
                Output only. ``main_sleep``: the longest sleep session with
                stages within one day. If no sleep session has stages, then
                the longest sleep is the ``main_sleep``. If there are
                multiple days of sleep in the response, there is one
                ``main_sleep`` per day.
        """

        class StagesState(proto.Enum):
            r"""Sleep stages algorithm processing status.

            Values:
                STAGES_STATE_UNSPECIFIED (0):
                    Output only. Sleep stages status is
                    unspecified.
                REJECTED_COVERAGE (1):
                    Output only. Sleep stages cannot be computed
                    due to low RR coverage.
                REJECTED_MAX_GAP (2):
                    Output only. Sleep stages cannot be computed
                    due to the large middle gap (2h).
                REJECTED_START_GAP (3):
                    Output only. Sleep stages cannot be computed
                    due to the large start gap (1h).
                REJECTED_END_GAP (4):
                    Output only. Sleep stages cannot be computed
                    due to the large end gap (1h).
                REJECTED_NAP (5):
                    Output only. Sleep stages cannot be computed
                    because the sleep log is a nap (has < 3h
                    duration).
                REJECTED_SERVER (6):
                    Output only. Sleep stages cannot be computed
                    because input data is not available (PPGV2, wake
                    magnitude, etc).
                TIMEOUT (7):
                    Output only. Sleep stages cannot be computed
                    due to server timeout.
                SUCCEEDED (8):
                    Output only. Sleep stages successfully
                    computed.
                PROCESSING_INTERNAL_ERROR (9):
                    Output only. Sleep stages cannot be computed
                    due to server internal error.
            """

            STAGES_STATE_UNSPECIFIED = 0
            REJECTED_COVERAGE = 1
            REJECTED_MAX_GAP = 2
            REJECTED_START_GAP = 3
            REJECTED_END_GAP = 4
            REJECTED_NAP = 5
            REJECTED_SERVER = 6
            TIMEOUT = 7
            SUCCEEDED = 8
            PROCESSING_INTERNAL_ERROR = 9

        stages_status: "Sleep.SleepMetadata.StagesState" = proto.Field(
            proto.ENUM,
            number=1,
            enum="Sleep.SleepMetadata.StagesState",
        )
        processed: bool = proto.Field(
            proto.BOOL,
            number=2,
        )
        nap: bool = proto.Field(
            proto.BOOL,
            number=5,
        )
        manually_edited: bool = proto.Field(
            proto.BOOL,
            number=6,
        )
        external_id: str = proto.Field(
            proto.STRING,
            number=7,
        )
        main_sleep: bool = proto.Field(
            proto.BOOL,
            number=9,
        )

    class SleepSummary(proto.Message):
        r"""Sleep summary: metrics and stages summary.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            minutes_in_sleep_period (int):
                Output only. Delta between wake time and
                bedtime. It is the sum of all stages.

                This field is a member of `oneof`_ ``_minutes_in_sleep_period``.
            minutes_after_wake_up (int):
                Output only. Minutes after wake up calculated
                by restlessness algorithm.

                This field is a member of `oneof`_ ``_minutes_after_wake_up``.
            minutes_to_fall_asleep (int):
                Output only. Minutes to fall asleep
                calculated by restlessness algorithm.

                This field is a member of `oneof`_ ``_minutes_to_fall_asleep``.
            minutes_asleep (int):
                Output only. Total number of minutes asleep.
                For classic sleep it is the sum of ASLEEP stages
                (excluding AWAKE and RESTLESS). For "stages"
                sleep it is the sum of LIGHT, REM and DEEP
                stages (excluding AWAKE).

                This field is a member of `oneof`_ ``_minutes_asleep``.
            minutes_awake (int):
                Output only. Total number of minutes awake.
                It is a sum of all AWAKE stages.

                This field is a member of `oneof`_ ``_minutes_awake``.
            stages_summary (MutableSequence[google.devicesandservices.health_v4.types.Sleep.SleepSummary.StageSummary]):
                Output only. List of summaries (total
                duration and segment count) per each sleep stage
                type.
        """

        class StageSummary(proto.Message):
            r"""Total duration and segment count for a stage.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                type_ (google.devicesandservices.health_v4.types.Sleep.SleepStageType):
                    Output only. Sleep stage type: AWAKE, DEEP,
                    REM, LIGHT etc.
                minutes (int):
                    Output only. Total duration in minutes of a
                    sleep stage.

                    This field is a member of `oneof`_ ``_minutes``.
                count (int):
                    Output only. Number of sleep stages segments.

                    This field is a member of `oneof`_ ``_count``.
            """

            type_: "Sleep.SleepStageType" = proto.Field(
                proto.ENUM,
                number=1,
                enum="Sleep.SleepStageType",
            )
            minutes: int = proto.Field(
                proto.INT64,
                number=2,
                optional=True,
            )
            count: int = proto.Field(
                proto.INT64,
                number=3,
                optional=True,
            )

        minutes_in_sleep_period: int = proto.Field(
            proto.INT64,
            number=1,
            optional=True,
        )
        minutes_after_wake_up: int = proto.Field(
            proto.INT64,
            number=2,
            optional=True,
        )
        minutes_to_fall_asleep: int = proto.Field(
            proto.INT64,
            number=3,
            optional=True,
        )
        minutes_asleep: int = proto.Field(
            proto.INT64,
            number=4,
            optional=True,
        )
        minutes_awake: int = proto.Field(
            proto.INT64,
            number=5,
            optional=True,
        )
        stages_summary: MutableSequence["Sleep.SleepSummary.StageSummary"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=6,
                message="Sleep.SleepSummary.StageSummary",
            )
        )

    interval: data_coordinates.SessionTimeInterval = proto.Field(
        proto.MESSAGE,
        number=3,
        message=data_coordinates.SessionTimeInterval,
    )
    type_: SleepType = proto.Field(
        proto.ENUM,
        number=4,
        enum=SleepType,
    )
    stages: MutableSequence[SleepStage] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message=SleepStage,
    )
    out_of_bed_segments: MutableSequence[OutOfBedSegment] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message=OutOfBedSegment,
    )
    metadata: SleepMetadata = proto.Field(
        proto.MESSAGE,
        number=8,
        message=SleepMetadata,
    )
    summary: SleepSummary = proto.Field(
        proto.MESSAGE,
        number=9,
        message=SleepSummary,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=11,
        message=timestamp_pb2.Timestamp,
    )
    short_awakenings: MutableSequence[SleepStage] = proto.RepeatedField(
        proto.MESSAGE,
        number=12,
        message=SleepStage,
    )


class Steps(proto.Message):
    r"""Step count over the time interval.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        interval (google.devicesandservices.health_v4.types.ObservationTimeInterval):
            Required. Observed interval.
        count (int):
            Required. Number of steps in the recorded interval. Must be
            in the range ``[0, 1000000]``.

            This field is a member of `oneof`_ ``_count``.
    """

    interval: data_coordinates.ObservationTimeInterval = proto.Field(
        proto.MESSAGE,
        number=2,
        message=data_coordinates.ObservationTimeInterval,
    )
    count: int = proto.Field(
        proto.INT64,
        number=4,
        optional=True,
    )


class StepsRollupValue(proto.Message):
    r"""Represents the result of the rollup of the steps data type.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        count_sum (int):
            Total number of steps in the interval.

            This field is a member of `oneof`_ ``_count_sum``.
    """

    count_sum: int = proto.Field(
        proto.INT64,
        number=1,
        optional=True,
    )


class SwimLengthsData(proto.Message):
    r"""Swim lengths data over the time interval.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        interval (google.devicesandservices.health_v4.types.ObservationTimeInterval):
            Required. Observed interval.
        swim_stroke_type (google.devicesandservices.health_v4.types.SwimLengthsData.SwimStrokeType):
            Required. Swim stroke type.
        stroke_count (int):
            Required. Number of strokes in the lap.

            This field is a member of `oneof`_ ``_stroke_count``.
    """

    class SwimStrokeType(proto.Enum):
        r"""Swim stroke type.

        Values:
            SWIM_STROKE_TYPE_UNSPECIFIED (0):
                Swim stroke type is unspecified.
            FREESTYLE (1):
                Freestyle swim stroke type.
            BACKSTROKE (2):
                Backstroke swim stroke type.
            BREASTSTROKE (3):
                Breaststroke swim stroke type.
            BUTTERFLY (4):
                Butterfly swim stroke type.
        """

        SWIM_STROKE_TYPE_UNSPECIFIED = 0
        FREESTYLE = 1
        BACKSTROKE = 2
        BREASTSTROKE = 3
        BUTTERFLY = 4

    interval: data_coordinates.ObservationTimeInterval = proto.Field(
        proto.MESSAGE,
        number=1,
        message=data_coordinates.ObservationTimeInterval,
    )
    swim_stroke_type: SwimStrokeType = proto.Field(
        proto.ENUM,
        number=2,
        enum=SwimStrokeType,
    )
    stroke_count: int = proto.Field(
        proto.INT64,
        number=3,
        optional=True,
    )


class SwimLengthsDataRollupValue(proto.Message):
    r"""Represents the result of the rollup of the swim lengths data
    type.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        stroke_count_sum (int):
            Total number of swim strokes in the interval.

            This field is a member of `oneof`_ ``_stroke_count_sum``.
    """

    stroke_count_sum: int = proto.Field(
        proto.INT64,
        number=1,
        optional=True,
    )


class TimeInHeartRateZone(proto.Message):
    r"""Time in heart rate zone record. It's an interval spent in
    specific heart rate zone.

    Attributes:
        interval (google.devicesandservices.health_v4.types.ObservationTimeInterval):
            Required. Observed interval.
        heart_rate_zone_type (google.devicesandservices.health_v4.types.HeartRateZoneType):
            Required. Heart rate zone type.
    """

    interval: data_coordinates.ObservationTimeInterval = proto.Field(
        proto.MESSAGE,
        number=1,
        message=data_coordinates.ObservationTimeInterval,
    )
    heart_rate_zone_type: "HeartRateZoneType" = proto.Field(
        proto.ENUM,
        number=2,
        enum="HeartRateZoneType",
    )


class TimeInHeartRateZoneRollupValue(proto.Message):
    r"""Represents the result of the rollup of the time in heart rate
    zone data type.

    Attributes:
        time_in_heart_rate_zones (MutableSequence[google.devicesandservices.health_v4.types.TimeInHeartRateZoneRollupValue.TimeInHeartRateZoneValue]):
            List of time spent in each heart rate zone.
    """

    class TimeInHeartRateZoneValue(proto.Message):
        r"""Represents the total time spent in a specific heart rate
        zone.

        Attributes:
            heart_rate_zone (google.devicesandservices.health_v4.types.HeartRateZoneType):
                The heart rate zone.
            duration (google.protobuf.duration_pb2.Duration):
                The total time spent in the specified heart
                rate zone.
        """

        heart_rate_zone: "HeartRateZoneType" = proto.Field(
            proto.ENUM,
            number=1,
            enum="HeartRateZoneType",
        )
        duration: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=2,
            message=duration_pb2.Duration,
        )

    time_in_heart_rate_zones: MutableSequence[TimeInHeartRateZoneValue] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=TimeInHeartRateZoneValue,
        )
    )


class TotalCaloriesRollupValue(proto.Message):
    r"""Represents the result of the rollup of the user's total calories.

    Note: Queries for the ``total-calories`` data type must include a
    time interval filter (such as
    [``total_calories.interval.start_time``][google.devicesandservices.health.v4main.ObservationTimeInterval.start_time]
    or
    [``total_calories.interval.civil_start_time``][google.devicesandservices.health.v4main.ObservationTimeInterval.civil_start_time]).
    The maximum range is 14 days.

    Example filter query:
    ``total_calories.interval.start_time >= "2026-04-20T00:00:00Z" AND total_calories.interval.start_time < "2026-04-21T00:00:00Z"``


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        kcal_sum (float):
            Sum of the total calories in kilocalories.

            This field is a member of `oneof`_ ``_kcal_sum``.
    """

    kcal_sum: float = proto.Field(
        proto.DOUBLE,
        number=1,
        optional=True,
    )


class VO2Max(proto.Message):
    r"""VO2 max measurement.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        sample_time (google.devicesandservices.health_v4.types.ObservationSampleTime):
            Required. The time at which VO2 max was
            measured.
        vo2_max (float):
            Required. VO2 max value measured as in ml consumed oxygen /
            kg of body weight / min. Must be in the range ``[0, 100]``.

            This field is a member of `oneof`_ ``_vo2_max``.
        measurement_method (google.devicesandservices.health_v4.types.VO2Max.MeasurementMethod):
            Optional. The method used to measure the VO2
            max value.
    """

    class MeasurementMethod(proto.Enum):
        r"""Measurement method used to measure the VO2 max value.

        Values:
            MEASUREMENT_METHOD_UNSPECIFIED (0):
                Unspecified measurement method.
            FITBIT_RUN (1):
                Fitbit specific, measures VO2 max rate during
                a run.
            GOOGLE_DEMOGRAPHIC (2):
                Google specific, measures VO2 max rate for a
                user based on their demographic data.
            COOPER_TEST (3):
                Run as far as possible for 12 minutes.
                Distance correlated with age and gender
                translates to a VO2 max value.
            HEART_RATE_RATIO (4):
                Maximum heart rate divided by the resting
                heart rate, with a multiplier applied. Does not
                require any exercise.
            METABOLIC_CART (5):
                Measured by a medical device called metabolic
                cart.
            MULTISTAGE_FITNESS_TEST (6):
                Continuous 20m back-and-forth runs with
                increasing difficulty, until exhaustion.
            ROCKPORT_FITNESS_TEST (7):
                Measured using walking exercise.
            MAX_EXERCISE (8):
                Healthkit specific, measures VO2 max rate by monitoring
                exercise to the user’s physical limit. Similar to
                COOPER_TEST or MULTISTAGE_FITNESS_TEST.
            PREDICTION_SUB_MAX_EXERCISE (9):
                Healthkit specific, estimates VO2 max rate based on
                low-intensity exercise. Similar to ROCKPORT_FITNESS_TEST.
            PREDICTION_NON_EXERCISE (10):
                Healthkit specific, estimates VO2 max rate without any
                exercise. Similar to HEART_RATE_RATIO.
            OTHER (11):
                Use when the method is not covered in this
                enum.
        """

        MEASUREMENT_METHOD_UNSPECIFIED = 0
        FITBIT_RUN = 1
        GOOGLE_DEMOGRAPHIC = 2
        COOPER_TEST = 3
        HEART_RATE_RATIO = 4
        METABOLIC_CART = 5
        MULTISTAGE_FITNESS_TEST = 6
        ROCKPORT_FITNESS_TEST = 7
        MAX_EXERCISE = 8
        PREDICTION_SUB_MAX_EXERCISE = 9
        PREDICTION_NON_EXERCISE = 10
        OTHER = 11

    sample_time: data_coordinates.ObservationSampleTime = proto.Field(
        proto.MESSAGE,
        number=1,
        message=data_coordinates.ObservationSampleTime,
    )
    vo2_max: float = proto.Field(
        proto.DOUBLE,
        number=2,
        optional=True,
    )
    measurement_method: MeasurementMethod = proto.Field(
        proto.ENUM,
        number=4,
        enum=MeasurementMethod,
    )


class Weight(proto.Message):
    r"""Body weight measurement.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        sample_time (google.devicesandservices.health_v4.types.ObservationSampleTime):
            Required. The time at which the weight was
            measured
        weight_grams (float):
            Required. Weight of a user in grams. Must be in the range
            ``[0, 1000000]``.

            This field is a member of `oneof`_ ``_weight_grams``.
        notes (str):
            Optional. Standard free-form notes captured
            at manual logging.
    """

    sample_time: data_coordinates.ObservationSampleTime = proto.Field(
        proto.MESSAGE,
        number=2,
        message=data_coordinates.ObservationSampleTime,
    )
    weight_grams: float = proto.Field(
        proto.DOUBLE,
        number=3,
        optional=True,
    )
    notes: str = proto.Field(
        proto.STRING,
        number=4,
    )


class WeightRollupValue(proto.Message):
    r"""Represents the result of the rollup of the weight data type.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        weight_grams_avg (float):
            Average weight in grams.

            This field is a member of `oneof`_ ``_weight_grams_avg``.
    """

    weight_grams_avg: float = proto.Field(
        proto.DOUBLE,
        number=1,
        optional=True,
    )


class BloodGlucose(proto.Message):
    r"""Represents a blood glucose level measurement. LINT: LEGACY_NAMES

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        sample_time (google.devicesandservices.health_v4.types.ObservationSampleTime):
            Required. The time at which blood glucose was
            measured.
        blood_glucose_milligrams_per_deciliter (float):
            Required. Blood glucose level concentration in mg/dL. Must
            be in the range ``[0, 900]``.

            This field is a member of `oneof`_ ``_blood_glucose_milligrams_per_deciliter``.
        measurement_source (google.devicesandservices.health_v4.types.BloodGlucose.MeasurementSource):
            Optional. Source of the measurement.
        meal_type (google.devicesandservices.health_v4.types.BloodGlucose.MealType):
            Optional. Meal type of the measurement.
        measurement_timing (google.devicesandservices.health_v4.types.BloodGlucose.MeasurementTiming):
            Optional. Timing of the measurement.
        specimen (google.devicesandservices.health_v4.types.BloodGlucose.Specimen):
            Optional. Type of body fluid used to measure
            the blood glucose.
        notes (str):
            Optional. Standard free-form notes captured
            at manual logging.
    """

    class MeasurementSource(proto.Enum):
        r"""The clinical method or tool used to measure the blood glucose
        level.

        Values:
            MEASUREMENT_SOURCE_UNSPECIFIED (0):
                Unspecified measurement source.
            SELF_MONITORING_BLOOD_GLUCOSE (1):
                Self-monitoring of blood glucose (Blood
                glucose meter)
            CONTINUOUS_GLUCOSE_MONITORING (2):
                Continuous glucose monitoring device
            LAB_TEST (3):
                Laboratory test
        """

        MEASUREMENT_SOURCE_UNSPECIFIED = 0
        SELF_MONITORING_BLOOD_GLUCOSE = 1
        CONTINUOUS_GLUCOSE_MONITORING = 2
        LAB_TEST = 3

    class MealType(proto.Enum):
        r"""Meal type associated with the measurement.

        Values:
            MEAL_TYPE_UNSPECIFIED (0):
                Unspecified meal type.
            BREAKFAST (1):
                Breakfast.
            LUNCH (2):
                Lunch.
            DINNER (3):
                Dinner.
            SNACK (4):
                Snack.
        """

        MEAL_TYPE_UNSPECIFIED = 0
        BREAKFAST = 1
        LUNCH = 2
        DINNER = 3
        SNACK = 4

    class MeasurementTiming(proto.Enum):
        r"""Timing of the measurement.

        Values:
            MEASUREMENT_TIMING_UNSPECIFIED (0):
                Unspecified measurement timing.
            AFTER_MEAL (1):
                Measurement taken after meal.
            BEFORE_MEAL (2):
                Measurement taken before meal.
            FASTING (3):
                Measurement taken while fasting.
            GENERAL (4):
                General measurement (not associated with a
                meal or time of day).
            BEFORE_BED (5):
                Measurement taken before bed.
            OVER_NIGHT (6):
                Measurement taken over night.
        """

        MEASUREMENT_TIMING_UNSPECIFIED = 0
        AFTER_MEAL = 1
        BEFORE_MEAL = 2
        FASTING = 3
        GENERAL = 4
        BEFORE_BED = 5
        OVER_NIGHT = 6

    class Specimen(proto.Enum):
        r"""Type of body fluid used to measure the blood glucose.

        Values:
            SPECIMEN_UNSPECIFIED (0):
                Unspecified specimen.
            CAPILLARY_BLOOD (1):
                Capillary blood.
            INTERSTITIAL_FLUID (2):
                Interstitial fluid.
            PLASMA (3):
                Plasma.
            SERUM (4):
                Serum.
            TEARS (5):
                Tears.
            WHOLE_BLOOD (6):
                Whole blood.
        """

        SPECIMEN_UNSPECIFIED = 0
        CAPILLARY_BLOOD = 1
        INTERSTITIAL_FLUID = 2
        PLASMA = 3
        SERUM = 4
        TEARS = 5
        WHOLE_BLOOD = 6

    sample_time: data_coordinates.ObservationSampleTime = proto.Field(
        proto.MESSAGE,
        number=1,
        message=data_coordinates.ObservationSampleTime,
    )
    blood_glucose_milligrams_per_deciliter: float = proto.Field(
        proto.DOUBLE,
        number=2,
        optional=True,
    )
    measurement_source: MeasurementSource = proto.Field(
        proto.ENUM,
        number=3,
        enum=MeasurementSource,
    )
    meal_type: MealType = proto.Field(
        proto.ENUM,
        number=4,
        enum=MealType,
    )
    measurement_timing: MeasurementTiming = proto.Field(
        proto.ENUM,
        number=5,
        enum=MeasurementTiming,
    )
    specimen: Specimen = proto.Field(
        proto.ENUM,
        number=6,
        enum=Specimen,
    )
    notes: str = proto.Field(
        proto.STRING,
        number=8,
    )


class BloodGlucoseRollupValue(proto.Message):
    r"""Represents the result of the rollup of the blood glucose data type.
    LINT: LEGACY_NAMES


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        blood_glucose_milligrams_per_deciliter_avg (float):
            Average blood glucose level in mg/dL.

            This field is a member of `oneof`_ ``_blood_glucose_milligrams_per_deciliter_avg``.
    """

    blood_glucose_milligrams_per_deciliter_avg: float = proto.Field(
        proto.DOUBLE,
        number=1,
        optional=True,
    )


class SedentaryPeriod(proto.Message):
    r"""SedentaryPeriod

    SedentaryPeriod data represents the periods of time that the
    user was sedentary (i.e. not moving while wearing the device).

    Attributes:
        interval (google.devicesandservices.health_v4.types.ObservationTimeInterval):
            Required. Observed interval.
    """

    interval: data_coordinates.ObservationTimeInterval = proto.Field(
        proto.MESSAGE,
        number=1,
        message=data_coordinates.ObservationTimeInterval,
    )


class SedentaryPeriodRollupValue(proto.Message):
    r"""Represents the result of the rollup of the user's sedentary
    periods.

    Attributes:
        duration_sum (google.protobuf.duration_pb2.Duration):
            The total time user spent sedentary during
            the interval.
    """

    duration_sum: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=1,
        message=duration_pb2.Duration,
    )


class ActiveEnergyBurned(proto.Message):
    r"""Energy burned as part of an activity, excluding the basal
    energy burn.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        interval (google.devicesandservices.health_v4.types.ObservationTimeInterval):
            Required. Observed interval
        kcal (float):
            Required. Energy burned during an activity, measured in
            kilocalories. Must be in the range ``[0, 1000000]``.

            This field is a member of `oneof`_ ``_kcal``.
    """

    interval: data_coordinates.ObservationTimeInterval = proto.Field(
        proto.MESSAGE,
        number=1,
        message=data_coordinates.ObservationTimeInterval,
    )
    kcal: float = proto.Field(
        proto.DOUBLE,
        number=2,
        optional=True,
    )


class ActiveEnergyBurnedRollupValue(proto.Message):
    r"""Represents the result of the rollup of active energy burned.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        kcal_sum (float):
            Output only. Sum of the active energy burned
            in kilocalories.

            This field is a member of `oneof`_ ``_kcal_sum``.
    """

    kcal_sum: float = proto.Field(
        proto.DOUBLE,
        number=1,
        optional=True,
    )


class MenstrualPeriod(proto.Message):
    r"""Menstrual period record.

    Attributes:
        interval (google.devicesandservices.health_v4.types.ObservationTimeInterval):
            Required. Observed interval.
        notes (str):
            Optional. Standard free-form notes captured
            at manual logging.
    """

    interval: data_coordinates.ObservationTimeInterval = proto.Field(
        proto.MESSAGE,
        number=2,
        message=data_coordinates.ObservationTimeInterval,
    )
    notes: str = proto.Field(
        proto.STRING,
        number=4,
    )


class OvulationTest(proto.Message):
    r"""Ovulation test record.

    Attributes:
        sample_time (google.devicesandservices.health_v4.types.ObservationSampleTime):
            Required. The time at which ovulation test
            was measured.
        result (google.devicesandservices.health_v4.types.OvulationTestResult):
            Required. The result of the ovulation test.
    """

    sample_time: data_coordinates.ObservationSampleTime = proto.Field(
        proto.MESSAGE,
        number=2,
        message=data_coordinates.ObservationSampleTime,
    )
    result: "OvulationTestResult" = proto.Field(
        proto.ENUM,
        number=3,
        enum="OvulationTestResult",
    )


class Symptoms(proto.Message):
    r"""Symptoms logged by the user.

    Attributes:
        sample_time (google.devicesandservices.health_v4.types.ObservationSampleTime):
            Required. Time when the symptoms were logged.
        symptoms (MutableSequence[google.devicesandservices.health_v4.types.Symptoms.SymptomValue]):
            Required. List of symptoms experienced.
    """

    class SymptomValue(proto.Enum):
        r"""Enum representing possible symptom values.

        Values:
            SYMPTOM_VALUE_UNSPECIFIED (0):
                Unspecified symptom value.
            CRAMPS (1):
                Abdominal cramps.
            HEADACHE (2):
                Headache.
            TENDER_BREASTS (3):
                Tender breasts.
            ACNE (4):
                Acne.
            SICK (5):
                Feeling sick or unwell.
            BLOATED (6):
                Bloating or abdominal swelling.
            HOT_FLASHES (7):
                Hot flashes.
            PMS (8):
                Premenstrual syndrome symptoms.
            COUGH (9):
                Coughing.
            FEVER (10):
                Fever or elevated body temperature.
            DIFFICULTY_BREATHING (11):
                Difficulty breathing or shortness of breath.
            BACK_PAIN (12):
                Back pain.
            SHAKINESS (13):
                Shakiness or tremors.
            HUNGER (14):
                Excessive hunger.
            SWEATING (15):
                Excessive sweating.
            ANXIETY (16):
                Anxiety or nervousness.
            THIRST (17):
                Excessive thirst.
            FREQUENT_URINATION (18):
                Frequent urination.
            BLURRED_VISION (19):
                Blurred vision.
            OTHER (20):
                Other symptoms.
            SEX_DRIVE_HIGH (21):
                High sex drive.
            SEX_DRIVE_MEDIUM (22):
                Medium sex drive.
            SEX_DRIVE_LOW (23):
                Low sex drive.
            HEART_PALPITATIONS (24):
                Heart palpitations or racing heart.
            FAINTING (25):
                Fainting or loss of consciousness.
            CHEST_PAIN (26):
                Chest pain or discomfort.
            FATIGUE (27):
                Fatigue or extreme tiredness.
            CONFUSION (28):
                Confusion or mental fogginess.
            DIZZINESS (29):
                Dizziness or lightheadedness.
            ABDOMINAL_PAIN (30):
                Abdominal pain.
            BLADDER_LEAKS (31):
                Bladder leaks.
            BLEEDING_GUMS (32):
                Bleeding gums.
            BRAIN_FOG (33):
                Brain fog.
            BURNING_MOUTH (34):
                Burning mouth.
            CONSTIPATION (35):
                Constipation.
            CRAVINGS (36):
                Food cravings.
            DECREASED_APPETITE (37):
                Decreased appetite.
            DIARRHEA (38):
                Diarrhea.
            DRAWING_PAIN (39):
                Drawing pain.
            DRY_EYES (40):
                Dry eyes.
            DRY_HAIR (41):
                Dry hair.
            DRY_SKIN (42):
                Dry skin.
            EXHAUSTION (43):
                Exhaustion.
            FEEL_GOOD (44):
                Feeling good or well.
            FOOD_AVERSIONS (45):
                Food aversions.
            HAIR_LOSS (46):
                Hair loss.
            HEARTBURN (47):
                Heartburn.
            HYPERPIGMENTATION (48):
                Hyperpigmentation.
            INCREASED_APPETITE (49):
                Increased appetite.
            INCREASED_APPETITE_V2 (50):
                Increased appetite V2.
            INSOMNIA (51):
                Insomnia or difficulty sleeping.
            JOINT_PAIN (52):
                Joint pain.
            LEG_CRAMPS (53):
                Leg cramps.
            MILKY_NIPPLE_DISCHARGE (54):
                Milky nipple discharge.
            NAUSEA (55):
                Nausea.
            NIGHT_SWEATS (56):
                Night sweats.
            NORMAL_DIGESTION (57):
                Normal digestion.
            NORMAL_STOOL (58):
                Normal stool.
            PERINEUM_PAIN (59):
                Perineum pain.
            SLEEPINESS (60):
                Sleepiness or drowsiness.
            STRETCH_MARKS (61):
                Stretch marks.
            SWELLING (62):
                Swelling.
            VAGINAL_DRYNESS (63):
                Vaginal dryness.
            VAGINAL_ITCHING (64):
                Vaginal itching.
            VOMITING (65):
                Vomiting.
        """

        SYMPTOM_VALUE_UNSPECIFIED = 0
        CRAMPS = 1
        HEADACHE = 2
        TENDER_BREASTS = 3
        ACNE = 4
        SICK = 5
        BLOATED = 6
        HOT_FLASHES = 7
        PMS = 8
        COUGH = 9
        FEVER = 10
        DIFFICULTY_BREATHING = 11
        BACK_PAIN = 12
        SHAKINESS = 13
        HUNGER = 14
        SWEATING = 15
        ANXIETY = 16
        THIRST = 17
        FREQUENT_URINATION = 18
        BLURRED_VISION = 19
        OTHER = 20
        SEX_DRIVE_HIGH = 21
        SEX_DRIVE_MEDIUM = 22
        SEX_DRIVE_LOW = 23
        HEART_PALPITATIONS = 24
        FAINTING = 25
        CHEST_PAIN = 26
        FATIGUE = 27
        CONFUSION = 28
        DIZZINESS = 29
        ABDOMINAL_PAIN = 30
        BLADDER_LEAKS = 31
        BLEEDING_GUMS = 32
        BRAIN_FOG = 33
        BURNING_MOUTH = 34
        CONSTIPATION = 35
        CRAVINGS = 36
        DECREASED_APPETITE = 37
        DIARRHEA = 38
        DRAWING_PAIN = 39
        DRY_EYES = 40
        DRY_HAIR = 41
        DRY_SKIN = 42
        EXHAUSTION = 43
        FEEL_GOOD = 44
        FOOD_AVERSIONS = 45
        HAIR_LOSS = 46
        HEARTBURN = 47
        HYPERPIGMENTATION = 48
        INCREASED_APPETITE = 49
        INCREASED_APPETITE_V2 = 50
        INSOMNIA = 51
        JOINT_PAIN = 52
        LEG_CRAMPS = 53
        MILKY_NIPPLE_DISCHARGE = 54
        NAUSEA = 55
        NIGHT_SWEATS = 56
        NORMAL_DIGESTION = 57
        NORMAL_STOOL = 58
        PERINEUM_PAIN = 59
        SLEEPINESS = 60
        STRETCH_MARKS = 61
        SWELLING = 62
        VAGINAL_DRYNESS = 63
        VAGINAL_ITCHING = 64
        VOMITING = 65

    sample_time: data_coordinates.ObservationSampleTime = proto.Field(
        proto.MESSAGE,
        number=1,
        message=data_coordinates.ObservationSampleTime,
    )
    symptoms: MutableSequence[SymptomValue] = proto.RepeatedField(
        proto.ENUM,
        number=2,
        enum=SymptomValue,
    )


class Moods(proto.Message):
    r"""Moods record.

    Attributes:
        sample_time (google.devicesandservices.health_v4.types.ObservationSampleTime):
            Required. The time at which moods were
            measured.
        moods (MutableSequence[google.devicesandservices.health_v4.types.Moods.Mood]):
            Required. The moods logged.
        valences (MutableSequence[google.devicesandservices.health_v4.types.Moods.Valence]):
            Optional. The valences.
    """

    class Mood(proto.Enum):
        r"""The mood.

        Values:
            MOOD_UNSPECIFIED (0):
                Unspecified mood.
            AMAZED (1):
                Amazed.
            AMUSED (2):
                Amused.
            ANGRY (3):
                Angry.
            ANNOYED (4):
                Annoyed.
            ANXIOUS (5):
                Anxious.
            HAPPY (6):
                Happy.
            CONTENT (7):
                Content.
            SAD (8):
                Sad.
            WORRIED (9):
                Worried.
            FRUSTRATED (10):
                Frustrated.
            EXCITED (11):
                Excited.
            CALM (12):
                Calm.
            STRESSED (13):
                Stressed.
            ASHAMED (14):
                Ashamed.
            BRAVE (15):
                Brave.
            CONFIDENT (16):
                Confident.
            DISAPPOINTED (17):
                Disappointed.
            DISCOURAGED (18):
                Discouraged.
            DISGUSTED (19):
                Disgusted.
            DRAINED (20):
                Drained.
            EMBARRASSED (21):
                Embarrassed.
            GRATEFUL (22):
                Grateful.
            GUILTY (23):
                Guilty.
            HOPEFUL (24):
                Hopeful.
            HOPELESS (25):
                Hopeless.
            INDIFFERENT (26):
                Indifferent.
            IRRITATED (27):
                Irritated.
            JEALOUS (28):
                Jealous.
            JOYFUL (29):
                Joyful.
            LONELY (30):
                Lonely.
            OVERWHELMED (31):
                Overwhelmed.
            PASSIONATE (32):
                Passionate.
            PEACEFUL (33):
                Peaceful.
            PROUD (34):
                Proud.
            RELIEVED (35):
                Relieved.
            SATISFIED (36):
                Satisfied.
            SCARED (37):
                Scared.
            SURPRISED (38):
                Surprised.
            ENERGIZED (39):
                Energized.
            FATIGUED (40):
                Fatigued.
            VERY_CALM (41):
                Very calm.
            VERY_STRESSED (42):
                Very stressed.
            NEUTRAL (43):
                Neutral.
            AFRAID (44):
                Afraid.
            HURTING (45):
                Hurting.
            BORED (46):
                Bored.
            BITTER (47):
                Bitter.
            ENVIOUS (48):
                Envious.
            CONFUSED (49):
                Confused.
            CURIOUS (50):
                Curious.
            AWESTRUCK (51):
                Awestruck.
            INSPIRED (52):
                Inspired.
            LONGING (53):
                Longing.
            ACCOMPLISHED (54):
                Accomplished.
            LOVING (55):
                Loving.
            COMPASSIONATE (56):
                Compassionate.
            DEPRESSED (57):
                Depressed.
            GOOD (58):
                Good.
            LOW_ENERGY (59):
                Low energy.
            OBSESSIVE_THOUGHTS (60):
                Obsessive thoughts.
            PANIC (61):
                Panic.
            PLAYFUL (62):
                Playful.
            PLEASED (63):
                Pleased.
            SENSITIVE (64):
                Sensitive.
            SLEEPY (65):
                Sleepy.
            SWINGS (66):
                Mood swings.
            UNHAPPY (67):
                Unhappy.
            VERY_SELF_CRITICAL (68):
                Very self-critical.
        """

        MOOD_UNSPECIFIED = 0
        AMAZED = 1
        AMUSED = 2
        ANGRY = 3
        ANNOYED = 4
        ANXIOUS = 5
        HAPPY = 6
        CONTENT = 7
        SAD = 8
        WORRIED = 9
        FRUSTRATED = 10
        EXCITED = 11
        CALM = 12
        STRESSED = 13
        ASHAMED = 14
        BRAVE = 15
        CONFIDENT = 16
        DISAPPOINTED = 17
        DISCOURAGED = 18
        DISGUSTED = 19
        DRAINED = 20
        EMBARRASSED = 21
        GRATEFUL = 22
        GUILTY = 23
        HOPEFUL = 24
        HOPELESS = 25
        INDIFFERENT = 26
        IRRITATED = 27
        JEALOUS = 28
        JOYFUL = 29
        LONELY = 30
        OVERWHELMED = 31
        PASSIONATE = 32
        PEACEFUL = 33
        PROUD = 34
        RELIEVED = 35
        SATISFIED = 36
        SCARED = 37
        SURPRISED = 38
        ENERGIZED = 39
        FATIGUED = 40
        VERY_CALM = 41
        VERY_STRESSED = 42
        NEUTRAL = 43
        AFRAID = 44
        HURTING = 45
        BORED = 46
        BITTER = 47
        ENVIOUS = 48
        CONFUSED = 49
        CURIOUS = 50
        AWESTRUCK = 51
        INSPIRED = 52
        LONGING = 53
        ACCOMPLISHED = 54
        LOVING = 55
        COMPASSIONATE = 56
        DEPRESSED = 57
        GOOD = 58
        LOW_ENERGY = 59
        OBSESSIVE_THOUGHTS = 60
        PANIC = 61
        PLAYFUL = 62
        PLEASED = 63
        SENSITIVE = 64
        SLEEPY = 65
        SWINGS = 66
        UNHAPPY = 67
        VERY_SELF_CRITICAL = 68

    class Valence(proto.Enum):
        r"""The valence.

        Values:
            VALENCE_UNSPECIFIED (0):
                Unspecified valence.
            UNPLEASANT (1):
                Unpleasant.
            BASELINE (2):
                Baseline.
            PLEASANT (3):
                Pleasant.
        """

        VALENCE_UNSPECIFIED = 0
        UNPLEASANT = 1
        BASELINE = 2
        PLEASANT = 3

    sample_time: data_coordinates.ObservationSampleTime = proto.Field(
        proto.MESSAGE,
        number=2,
        message=data_coordinates.ObservationSampleTime,
    )
    moods: MutableSequence[Mood] = proto.RepeatedField(
        proto.ENUM,
        number=3,
        enum=Mood,
    )
    valences: MutableSequence[Valence] = proto.RepeatedField(
        proto.ENUM,
        number=5,
        enum=Valence,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
