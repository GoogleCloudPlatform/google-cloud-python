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
import google.rpc.status_pb2 as status_pb2  # type: ignore
import google.type.interval_pb2 as interval_pb2  # type: ignore
import proto  # type: ignore

from google.devicesandservices.health_v4.types import data_coordinates, data_model
from google.devicesandservices.health_v4.types import data_source as gdh_data_source

__protobuf__ = proto.module(
    package="google.devicesandservices.health.v4",
    manifest={
        "DataPoint",
        "ReconciledDataPoint",
        "RollupDataPoint",
        "DailyRollupDataPoint",
        "GetDataPointRequest",
        "ListDataPointsRequest",
        "ListDataPointsResponse",
        "CreateDataPointRequest",
        "CreateDataPointOperationMetadata",
        "UpdateDataPointRequest",
        "UpdateDataPointOperationMetadata",
        "BatchDeleteDataPointsRequest",
        "BatchDeleteDataPointsResponse",
        "BatchDeleteDataPointsOperationMetadata",
        "ReconcileDataPointsRequest",
        "ReconcileDataPointsResponse",
        "RollUpDataPointsRequest",
        "RollUpDataPointsResponse",
        "DailyRollUpDataPointsRequest",
        "DailyRollUpDataPointsResponse",
        "DataType",
        "ExportExerciseTcxRequest",
        "ExportExerciseTcxResponse",
    },
)


class DataPoint(proto.Message):
    r"""A computed or recorded metric.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        steps (google.devicesandservices.health_v4.types.Steps):
            Optional. Data for points in the ``steps`` interval data
            type collection.

            This field is a member of `oneof`_ ``data``.
        floors (google.devicesandservices.health_v4.types.Floors):
            Optional. Data for points in the ``floors`` interval data
            type collection.

            This field is a member of `oneof`_ ``data``.
        heart_rate (google.devicesandservices.health_v4.types.HeartRate):
            Optional. Data for points in the ``heart-rate`` sample data
            type collection.

            This field is a member of `oneof`_ ``data``.
        sleep (google.devicesandservices.health_v4.types.Sleep):
            Optional. Data for points in the ``sleep`` session data type
            collection.

            This field is a member of `oneof`_ ``data``.
        daily_resting_heart_rate (google.devicesandservices.health_v4.types.DailyRestingHeartRate):
            Optional. Data for points in the
            ``daily-resting-heart-rate`` daily data type collection.

            This field is a member of `oneof`_ ``data``.
        daily_heart_rate_variability (google.devicesandservices.health_v4.types.DailyHeartRateVariability):
            Optional. Data for points in the
            ``daily-heart-rate-variability`` daily data type collection.

            This field is a member of `oneof`_ ``data``.
        exercise (google.devicesandservices.health_v4.types.Exercise):
            Optional. Data for points in the ``exercise`` session data
            type collection.

            This field is a member of `oneof`_ ``data``.
        weight (google.devicesandservices.health_v4.types.Weight):
            Optional. Data for points in the ``weight`` sample data type
            collection.

            This field is a member of `oneof`_ ``data``.
        altitude (google.devicesandservices.health_v4.types.Altitude):
            Optional. Data for points in the ``altitude`` interval data
            type collection.

            This field is a member of `oneof`_ ``data``.
        distance (google.devicesandservices.health_v4.types.Distance):
            Optional. Data for points in the ``distance`` interval data
            type collection.

            This field is a member of `oneof`_ ``data``.
        body_fat (google.devicesandservices.health_v4.types.BodyFat):
            Optional. Data for points in the ``body-fat`` sample data
            type collection.

            This field is a member of `oneof`_ ``data``.
        active_zone_minutes (google.devicesandservices.health_v4.types.ActiveZoneMinutes):
            Optional. Data for points in the ``active-zone-minutes``
            interval data type collection, measured in minutes.

            This field is a member of `oneof`_ ``data``.
        heart_rate_variability (google.devicesandservices.health_v4.types.HeartRateVariability):
            Optional. Data for points in the ``heart-rate-variability``
            sample data type collection.

            This field is a member of `oneof`_ ``data``.
        daily_sleep_temperature_derivations (google.devicesandservices.health_v4.types.DailySleepTemperatureDerivations):
            Optional. Data for points in the
            ``daily-sleep-temperature-derivations`` daily data type
            collection.

            This field is a member of `oneof`_ ``data``.
        sedentary_period (google.devicesandservices.health_v4.types.SedentaryPeriod):
            Optional. Data for points in the ``sedentary-period``
            interval data type collection.

            This field is a member of `oneof`_ ``data``.
        run_vo2_max (google.devicesandservices.health_v4.types.RunVO2Max):
            Optional. Data for points in the ``run-vo2-max`` sample data
            type collection.

            This field is a member of `oneof`_ ``data``.
        oxygen_saturation (google.devicesandservices.health_v4.types.OxygenSaturation):
            Optional. Data for points in the ``oxygen-saturation``
            sample data type collection.

            This field is a member of `oneof`_ ``data``.
        daily_oxygen_saturation (google.devicesandservices.health_v4.types.DailyOxygenSaturation):
            Optional. Data for points in the ``daily-oxygen-saturation``
            daily data type collection.

            This field is a member of `oneof`_ ``data``.
        activity_level (google.devicesandservices.health_v4.types.ActivityLevel):
            Optional. Data for points in the ``activity-level`` daily
            data type collection.

            This field is a member of `oneof`_ ``data``.
        vo2_max (google.devicesandservices.health_v4.types.VO2Max):
            Optional. Data for points in the ``vo2-max`` sample data
            type collection.

            This field is a member of `oneof`_ ``data``.
        daily_vo2_max (google.devicesandservices.health_v4.types.DailyVO2Max):
            Optional. Data for points in the ``daily-vo2-max`` daily
            data type collection.

            This field is a member of `oneof`_ ``data``.
        nutrition_log (google.devicesandservices.health_v4.types.NutritionLog):
            Optional. Data for points in the ``nutrition-log`` session
            data type collection.

            This field is a member of `oneof`_ ``data``.
        irregular_rhythm_notification (google.devicesandservices.health_v4.types.IrregularRhythmNotification):
            Optional. Data for points in the
            ``irregular-rhythm-notification`` session data type
            collection.

            This field is a member of `oneof`_ ``data``.
        electrocardiogram (google.devicesandservices.health_v4.types.Electrocardiogram):
            Optional. Data for points in the ``electrocardiogram``
            session data type collection.

            This field is a member of `oneof`_ ``data``.
        daily_heart_rate_zones (google.devicesandservices.health_v4.types.DailyHeartRateZones):
            Optional. Data for points in the ``daily-heart-rate-zones``
            daily data type collection.

            This field is a member of `oneof`_ ``data``.
        hydration_log (google.devicesandservices.health_v4.types.HydrationLog):
            Optional. Data for points in the ``hydration-log`` session
            data type collection.

            This field is a member of `oneof`_ ``data``.
        food (google.devicesandservices.health_v4.types.Food):
            Optional. The food details.

            This field is a member of `oneof`_ ``data``.
        time_in_heart_rate_zone (google.devicesandservices.health_v4.types.TimeInHeartRateZone):
            Optional. Data for points in the ``time-in-heart-rate-zone``
            interval data type collection.

            This field is a member of `oneof`_ ``data``.
        active_minutes (google.devicesandservices.health_v4.types.ActiveMinutes):
            Optional. Data for points in the ``active-minutes`` interval
            data type collection.

            This field is a member of `oneof`_ ``data``.
        respiratory_rate_sleep_summary (google.devicesandservices.health_v4.types.RespiratoryRateSleepSummary):
            Optional. Data for points in the
            ``respiratory-rate-sleep-summary`` sample data type
            collection.

            This field is a member of `oneof`_ ``data``.
        daily_respiratory_rate (google.devicesandservices.health_v4.types.DailyRespiratoryRate):
            Optional. Data for points in the ``daily-respiratory-rate``
            daily data type collection.

            This field is a member of `oneof`_ ``data``.
        swim_lengths_data (google.devicesandservices.health_v4.types.SwimLengthsData):
            Optional. Data for points in the ``swim-lengths-data``
            interval data type collection.

            This field is a member of `oneof`_ ``data``.
        height (google.devicesandservices.health_v4.types.Height):
            Optional. Data for points in the ``height`` sample data type
            collection.

            This field is a member of `oneof`_ ``data``.
        basal_energy_burned (google.devicesandservices.health_v4.types.BasalEnergyBurned):
            Optional. Data for points in the ``basal-energy-burned``
            interval data type collection.

            This field is a member of `oneof`_ ``data``.
        core_body_temperature (google.devicesandservices.health_v4.types.CoreBodyTemperature):
            Optional. Data for points in the ``core-body-temperature``
            sample data type collection.

            This field is a member of `oneof`_ ``data``.
        active_energy_burned (google.devicesandservices.health_v4.types.ActiveEnergyBurned):
            Optional. Data for points in the ``active-energy-burned``
            interval data type collection.

            This field is a member of `oneof`_ ``data``.
        food_measurement_unit (google.devicesandservices.health_v4.types.FoodMeasurementUnit):
            Optional. The food measurement unit details.

            This field is a member of `oneof`_ ``data``.
        blood_glucose (google.devicesandservices.health_v4.types.BloodGlucose):
            Optional. Data for points in the ``blood-glucose`` sample
            data type collection.

            This field is a member of `oneof`_ ``data``.
        menstrual_period (google.devicesandservices.health_v4.types.MenstrualPeriod):
            Optional. Data for points in the ``menstrual-period``
            interval data type collection.

            This field is a member of `oneof`_ ``data``.
        ovulation_test (google.devicesandservices.health_v4.types.OvulationTest):
            Optional. Data for points in the ``ovulation-test`` sample
            data type collection.

            This field is a member of `oneof`_ ``data``.
        symptoms (google.devicesandservices.health_v4.types.Symptoms):
            Optional. Data for points in the ``symptoms`` sample data
            type collection.

            This field is a member of `oneof`_ ``data``.
        moods (google.devicesandservices.health_v4.types.Moods):
            Optional. Data for points in the ``moods`` sample data type
            collection.

            This field is a member of `oneof`_ ``data``.
        name (str):
            Identifier. Data point name, only supported for the subset
            of identifiable data types. For the majority of the data
            types, individual data points do not need to be identified
            and this field would be empty.

            Format:
            ``users/{user}/dataTypes/{data_type}/dataPoints/{data_point}``

            Example:
            ``users/abcd1234/dataTypes/sleep/dataPoints/a1b2c3d4-e5f6-7890-1234-567890abcdef``

            The ``{user}`` ID is a system-generated identifier, as
            described in
            [Identity.health_user_id][google.devicesandservices.health.v4.Identity.health_user_id].

            The ``{data_type}`` ID corresponds to the kebab-case version
            of the field names in the [DataPoint
            data][google.devicesandservices.health.v4.DataPoint] union
            field, e.g. ``heart-rate`` for the ``heart_rate`` field.

            The ``{data_point}`` ID can be client-provided or
            system-generated. If client-provided, it must be a string of
            4-63 characters, containing only lowercase letters, numbers,
            and hyphens.
        data_source (google.devicesandservices.health_v4.types.DataSource):
            Optional. Data source information for the
            metric
    """

    steps: data_model.Steps = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="data",
        message=data_model.Steps,
    )
    floors: data_model.Floors = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="data",
        message=data_model.Floors,
    )
    heart_rate: data_model.HeartRate = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="data",
        message=data_model.HeartRate,
    )
    sleep: data_model.Sleep = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="data",
        message=data_model.Sleep,
    )
    daily_resting_heart_rate: data_model.DailyRestingHeartRate = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="data",
        message=data_model.DailyRestingHeartRate,
    )
    daily_heart_rate_variability: data_model.DailyHeartRateVariability = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="data",
        message=data_model.DailyHeartRateVariability,
    )
    exercise: data_model.Exercise = proto.Field(
        proto.MESSAGE,
        number=11,
        oneof="data",
        message=data_model.Exercise,
    )
    weight: data_model.Weight = proto.Field(
        proto.MESSAGE,
        number=12,
        oneof="data",
        message=data_model.Weight,
    )
    altitude: data_model.Altitude = proto.Field(
        proto.MESSAGE,
        number=13,
        oneof="data",
        message=data_model.Altitude,
    )
    distance: data_model.Distance = proto.Field(
        proto.MESSAGE,
        number=14,
        oneof="data",
        message=data_model.Distance,
    )
    body_fat: data_model.BodyFat = proto.Field(
        proto.MESSAGE,
        number=15,
        oneof="data",
        message=data_model.BodyFat,
    )
    active_zone_minutes: data_model.ActiveZoneMinutes = proto.Field(
        proto.MESSAGE,
        number=17,
        oneof="data",
        message=data_model.ActiveZoneMinutes,
    )
    heart_rate_variability: data_model.HeartRateVariability = proto.Field(
        proto.MESSAGE,
        number=19,
        oneof="data",
        message=data_model.HeartRateVariability,
    )
    daily_sleep_temperature_derivations: data_model.DailySleepTemperatureDerivations = (
        proto.Field(
            proto.MESSAGE,
            number=20,
            oneof="data",
            message=data_model.DailySleepTemperatureDerivations,
        )
    )
    sedentary_period: data_model.SedentaryPeriod = proto.Field(
        proto.MESSAGE,
        number=21,
        oneof="data",
        message=data_model.SedentaryPeriod,
    )
    run_vo2_max: data_model.RunVO2Max = proto.Field(
        proto.MESSAGE,
        number=22,
        oneof="data",
        message=data_model.RunVO2Max,
    )
    oxygen_saturation: data_model.OxygenSaturation = proto.Field(
        proto.MESSAGE,
        number=24,
        oneof="data",
        message=data_model.OxygenSaturation,
    )
    daily_oxygen_saturation: data_model.DailyOxygenSaturation = proto.Field(
        proto.MESSAGE,
        number=25,
        oneof="data",
        message=data_model.DailyOxygenSaturation,
    )
    activity_level: data_model.ActivityLevel = proto.Field(
        proto.MESSAGE,
        number=26,
        oneof="data",
        message=data_model.ActivityLevel,
    )
    vo2_max: data_model.VO2Max = proto.Field(
        proto.MESSAGE,
        number=27,
        oneof="data",
        message=data_model.VO2Max,
    )
    daily_vo2_max: data_model.DailyVO2Max = proto.Field(
        proto.MESSAGE,
        number=28,
        oneof="data",
        message=data_model.DailyVO2Max,
    )
    nutrition_log: data_model.NutritionLog = proto.Field(
        proto.MESSAGE,
        number=29,
        oneof="data",
        message=data_model.NutritionLog,
    )
    irregular_rhythm_notification: data_model.IrregularRhythmNotification = proto.Field(
        proto.MESSAGE,
        number=30,
        oneof="data",
        message=data_model.IrregularRhythmNotification,
    )
    electrocardiogram: data_model.Electrocardiogram = proto.Field(
        proto.MESSAGE,
        number=31,
        oneof="data",
        message=data_model.Electrocardiogram,
    )
    daily_heart_rate_zones: data_model.DailyHeartRateZones = proto.Field(
        proto.MESSAGE,
        number=32,
        oneof="data",
        message=data_model.DailyHeartRateZones,
    )
    hydration_log: data_model.HydrationLog = proto.Field(
        proto.MESSAGE,
        number=33,
        oneof="data",
        message=data_model.HydrationLog,
    )
    food: data_model.Food = proto.Field(
        proto.MESSAGE,
        number=34,
        oneof="data",
        message=data_model.Food,
    )
    time_in_heart_rate_zone: data_model.TimeInHeartRateZone = proto.Field(
        proto.MESSAGE,
        number=35,
        oneof="data",
        message=data_model.TimeInHeartRateZone,
    )
    active_minutes: data_model.ActiveMinutes = proto.Field(
        proto.MESSAGE,
        number=36,
        oneof="data",
        message=data_model.ActiveMinutes,
    )
    respiratory_rate_sleep_summary: data_model.RespiratoryRateSleepSummary = (
        proto.Field(
            proto.MESSAGE,
            number=37,
            oneof="data",
            message=data_model.RespiratoryRateSleepSummary,
        )
    )
    daily_respiratory_rate: data_model.DailyRespiratoryRate = proto.Field(
        proto.MESSAGE,
        number=38,
        oneof="data",
        message=data_model.DailyRespiratoryRate,
    )
    swim_lengths_data: data_model.SwimLengthsData = proto.Field(
        proto.MESSAGE,
        number=39,
        oneof="data",
        message=data_model.SwimLengthsData,
    )
    height: data_model.Height = proto.Field(
        proto.MESSAGE,
        number=40,
        oneof="data",
        message=data_model.Height,
    )
    basal_energy_burned: data_model.BasalEnergyBurned = proto.Field(
        proto.MESSAGE,
        number=41,
        oneof="data",
        message=data_model.BasalEnergyBurned,
    )
    core_body_temperature: data_model.CoreBodyTemperature = proto.Field(
        proto.MESSAGE,
        number=42,
        oneof="data",
        message=data_model.CoreBodyTemperature,
    )
    active_energy_burned: data_model.ActiveEnergyBurned = proto.Field(
        proto.MESSAGE,
        number=44,
        oneof="data",
        message=data_model.ActiveEnergyBurned,
    )
    food_measurement_unit: data_model.FoodMeasurementUnit = proto.Field(
        proto.MESSAGE,
        number=45,
        oneof="data",
        message=data_model.FoodMeasurementUnit,
    )
    blood_glucose: data_model.BloodGlucose = proto.Field(
        proto.MESSAGE,
        number=46,
        oneof="data",
        message=data_model.BloodGlucose,
    )
    menstrual_period: data_model.MenstrualPeriod = proto.Field(
        proto.MESSAGE,
        number=49,
        oneof="data",
        message=data_model.MenstrualPeriod,
    )
    ovulation_test: data_model.OvulationTest = proto.Field(
        proto.MESSAGE,
        number=50,
        oneof="data",
        message=data_model.OvulationTest,
    )
    symptoms: data_model.Symptoms = proto.Field(
        proto.MESSAGE,
        number=52,
        oneof="data",
        message=data_model.Symptoms,
    )
    moods: data_model.Moods = proto.Field(
        proto.MESSAGE,
        number=53,
        oneof="data",
        message=data_model.Moods,
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    data_source: gdh_data_source.DataSource = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gdh_data_source.DataSource,
    )


class ReconciledDataPoint(proto.Message):
    r"""A reconciled computed or recorded metric.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        steps (google.devicesandservices.health_v4.types.Steps):
            Data for points in the ``steps`` interval data type
            collection.

            This field is a member of `oneof`_ ``data``.
        floors (google.devicesandservices.health_v4.types.Floors):
            Data for points in the ``floors`` interval data type
            collection.

            This field is a member of `oneof`_ ``data``.
        heart_rate (google.devicesandservices.health_v4.types.HeartRate):
            Data for points in the ``heart-rate`` sample data type
            collection.

            This field is a member of `oneof`_ ``data``.
        sleep (google.devicesandservices.health_v4.types.Sleep):
            Data for points in the ``sleep`` session data type
            collection.

            This field is a member of `oneof`_ ``data``.
        daily_resting_heart_rate (google.devicesandservices.health_v4.types.DailyRestingHeartRate):
            Data for points in the ``daily-resting-heart-rate`` daily
            data type collection.

            This field is a member of `oneof`_ ``data``.
        daily_heart_rate_variability (google.devicesandservices.health_v4.types.DailyHeartRateVariability):
            Data for points in the ``daily-heart-rate-variability``
            daily data type collection.

            This field is a member of `oneof`_ ``data``.
        exercise (google.devicesandservices.health_v4.types.Exercise):
            Data for points in the ``exercise`` session data type
            collection.

            This field is a member of `oneof`_ ``data``.
        weight (google.devicesandservices.health_v4.types.Weight):
            Data for points in the ``weight`` sample data type
            collection.

            This field is a member of `oneof`_ ``data``.
        altitude (google.devicesandservices.health_v4.types.Altitude):
            Data for points in the ``altitude`` interval data type
            collection.

            This field is a member of `oneof`_ ``data``.
        distance (google.devicesandservices.health_v4.types.Distance):
            Data for points in the ``distance`` interval data type
            collection.

            This field is a member of `oneof`_ ``data``.
        body_fat (google.devicesandservices.health_v4.types.BodyFat):
            Data for points in the ``body-fat`` sample data type
            collection.

            This field is a member of `oneof`_ ``data``.
        active_zone_minutes (google.devicesandservices.health_v4.types.ActiveZoneMinutes):
            Data for points in the ``active-zone-minutes`` interval data
            type collection, measured in minutes.

            This field is a member of `oneof`_ ``data``.
        heart_rate_variability (google.devicesandservices.health_v4.types.HeartRateVariability):
            Data for points in the ``heart-rate-variability`` sample
            data type collection.

            This field is a member of `oneof`_ ``data``.
        daily_sleep_temperature_derivations (google.devicesandservices.health_v4.types.DailySleepTemperatureDerivations):
            Data for points in the
            ``daily-sleep-temperature-derivations`` daily data type
            collection.

            This field is a member of `oneof`_ ``data``.
        sedentary_period (google.devicesandservices.health_v4.types.SedentaryPeriod):
            Data for points in the ``sedentary-period`` interval data
            type collection.

            This field is a member of `oneof`_ ``data``.
        run_vo2_max (google.devicesandservices.health_v4.types.RunVO2Max):
            Data for points in the ``run-vo2-max`` sample data type
            collection.

            This field is a member of `oneof`_ ``data``.
        oxygen_saturation (google.devicesandservices.health_v4.types.OxygenSaturation):
            Data for points in the ``oxygen-saturation`` sample data
            type collection.

            This field is a member of `oneof`_ ``data``.
        daily_oxygen_saturation (google.devicesandservices.health_v4.types.DailyOxygenSaturation):
            Data for points in the ``daily-oxygen-saturation`` daily
            data type collection.

            This field is a member of `oneof`_ ``data``.
        activity_level (google.devicesandservices.health_v4.types.ActivityLevel):
            Data for points in the ``activity-level`` daily data type
            collection.

            This field is a member of `oneof`_ ``data``.
        vo2_max (google.devicesandservices.health_v4.types.VO2Max):
            Data for points in the ``vo2-max`` sample data type
            collection.

            This field is a member of `oneof`_ ``data``.
        daily_vo2_max (google.devicesandservices.health_v4.types.DailyVO2Max):
            Data for points in the ``daily-vo2-max`` daily data type
            collection.

            This field is a member of `oneof`_ ``data``.
        nutrition_log (google.devicesandservices.health_v4.types.NutritionLog):
            Data for points in the ``nutrition-log`` session data type
            collection.

            This field is a member of `oneof`_ ``data``.
        daily_heart_rate_zones (google.devicesandservices.health_v4.types.DailyHeartRateZones):
            Data for points in the ``daily-heart-rate-zones`` daily data
            type collection.

            This field is a member of `oneof`_ ``data``.
        hydration_log (google.devicesandservices.health_v4.types.HydrationLog):
            Data for points in the ``hydration-log`` session data type
            collection.

            This field is a member of `oneof`_ ``data``.
        time_in_heart_rate_zone (google.devicesandservices.health_v4.types.TimeInHeartRateZone):
            Data for points in the ``time-in-heart-rate-zone`` interval
            data type collection.

            This field is a member of `oneof`_ ``data``.
        active_minutes (google.devicesandservices.health_v4.types.ActiveMinutes):
            Data for points in the ``active-minutes`` interval data type
            collection.

            This field is a member of `oneof`_ ``data``.
        respiratory_rate_sleep_summary (google.devicesandservices.health_v4.types.RespiratoryRateSleepSummary):
            Data for points in the ``respiratory-rate-sleep-summary``
            sample data type collection.

            This field is a member of `oneof`_ ``data``.
        daily_respiratory_rate (google.devicesandservices.health_v4.types.DailyRespiratoryRate):
            Data for points in the ``daily-respiratory-rate`` daily data
            type collection.

            This field is a member of `oneof`_ ``data``.
        swim_lengths_data (google.devicesandservices.health_v4.types.SwimLengthsData):
            Data for points in the ``swim-lengths-data`` interval data
            type collection.

            This field is a member of `oneof`_ ``data``.
        height (google.devicesandservices.health_v4.types.Height):
            Data for points in the ``height`` sample data type
            collection.

            This field is a member of `oneof`_ ``data``.
        basal_energy_burned (google.devicesandservices.health_v4.types.BasalEnergyBurned):
            Data for points in the ``basal-energy-burned`` interval data
            type collection.

            This field is a member of `oneof`_ ``data``.
        core_body_temperature (google.devicesandservices.health_v4.types.CoreBodyTemperature):
            Data for points in the ``core-body-temperature`` sample data
            type collection.

            This field is a member of `oneof`_ ``data``.
        active_energy_burned (google.devicesandservices.health_v4.types.ActiveEnergyBurned):
            Data for points in the ``active-energy-burned`` interval
            data type collection.

            This field is a member of `oneof`_ ``data``.
        blood_glucose (google.devicesandservices.health_v4.types.BloodGlucose):
            Data for points in the ``blood-glucose`` sample data type
            collection.

            This field is a member of `oneof`_ ``data``.
        data_point_name (str):
            Identifier. Data point name, only supported for the subset
            of identifiable data types. For the majority of the data
            types, individual data points do not need to be identified
            and this field would be empty.

            Format:
            ``users/{user}/dataTypes/{data_type}/dataPoints/{data_point}``

            Example:
            ``users/abcd1234/dataTypes/sleep/dataPoints/a1b2c3d4-e5f6-7890-1234-567890abcdef``

            The ``{user}`` ID is a system-generated identifier, as
            described in
            [Identity.health_user_id][google.devicesandservices.health.v4.Identity.health_user_id].

            The ``{data_type}`` ID corresponds to the kebab-case version
            of the field names in the [DataPoint
            data][google.devicesandservices.health.v4.DataPoint] union
            field, e.g. ``heart-rate`` for the ``heart_rate`` field.

            The ``{data_point}`` ID can be client-provided or
            system-generated. If client-provided, it must be a string of
            4-63 characters, containing only lowercase letters, numbers,
            and hyphens.
    """

    steps: data_model.Steps = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="data",
        message=data_model.Steps,
    )
    floors: data_model.Floors = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="data",
        message=data_model.Floors,
    )
    heart_rate: data_model.HeartRate = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="data",
        message=data_model.HeartRate,
    )
    sleep: data_model.Sleep = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="data",
        message=data_model.Sleep,
    )
    daily_resting_heart_rate: data_model.DailyRestingHeartRate = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="data",
        message=data_model.DailyRestingHeartRate,
    )
    daily_heart_rate_variability: data_model.DailyHeartRateVariability = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="data",
        message=data_model.DailyHeartRateVariability,
    )
    exercise: data_model.Exercise = proto.Field(
        proto.MESSAGE,
        number=11,
        oneof="data",
        message=data_model.Exercise,
    )
    weight: data_model.Weight = proto.Field(
        proto.MESSAGE,
        number=12,
        oneof="data",
        message=data_model.Weight,
    )
    altitude: data_model.Altitude = proto.Field(
        proto.MESSAGE,
        number=13,
        oneof="data",
        message=data_model.Altitude,
    )
    distance: data_model.Distance = proto.Field(
        proto.MESSAGE,
        number=14,
        oneof="data",
        message=data_model.Distance,
    )
    body_fat: data_model.BodyFat = proto.Field(
        proto.MESSAGE,
        number=15,
        oneof="data",
        message=data_model.BodyFat,
    )
    active_zone_minutes: data_model.ActiveZoneMinutes = proto.Field(
        proto.MESSAGE,
        number=17,
        oneof="data",
        message=data_model.ActiveZoneMinutes,
    )
    heart_rate_variability: data_model.HeartRateVariability = proto.Field(
        proto.MESSAGE,
        number=19,
        oneof="data",
        message=data_model.HeartRateVariability,
    )
    daily_sleep_temperature_derivations: data_model.DailySleepTemperatureDerivations = (
        proto.Field(
            proto.MESSAGE,
            number=20,
            oneof="data",
            message=data_model.DailySleepTemperatureDerivations,
        )
    )
    sedentary_period: data_model.SedentaryPeriod = proto.Field(
        proto.MESSAGE,
        number=21,
        oneof="data",
        message=data_model.SedentaryPeriod,
    )
    run_vo2_max: data_model.RunVO2Max = proto.Field(
        proto.MESSAGE,
        number=22,
        oneof="data",
        message=data_model.RunVO2Max,
    )
    oxygen_saturation: data_model.OxygenSaturation = proto.Field(
        proto.MESSAGE,
        number=24,
        oneof="data",
        message=data_model.OxygenSaturation,
    )
    daily_oxygen_saturation: data_model.DailyOxygenSaturation = proto.Field(
        proto.MESSAGE,
        number=25,
        oneof="data",
        message=data_model.DailyOxygenSaturation,
    )
    activity_level: data_model.ActivityLevel = proto.Field(
        proto.MESSAGE,
        number=26,
        oneof="data",
        message=data_model.ActivityLevel,
    )
    vo2_max: data_model.VO2Max = proto.Field(
        proto.MESSAGE,
        number=27,
        oneof="data",
        message=data_model.VO2Max,
    )
    daily_vo2_max: data_model.DailyVO2Max = proto.Field(
        proto.MESSAGE,
        number=28,
        oneof="data",
        message=data_model.DailyVO2Max,
    )
    nutrition_log: data_model.NutritionLog = proto.Field(
        proto.MESSAGE,
        number=29,
        oneof="data",
        message=data_model.NutritionLog,
    )
    daily_heart_rate_zones: data_model.DailyHeartRateZones = proto.Field(
        proto.MESSAGE,
        number=32,
        oneof="data",
        message=data_model.DailyHeartRateZones,
    )
    hydration_log: data_model.HydrationLog = proto.Field(
        proto.MESSAGE,
        number=33,
        oneof="data",
        message=data_model.HydrationLog,
    )
    time_in_heart_rate_zone: data_model.TimeInHeartRateZone = proto.Field(
        proto.MESSAGE,
        number=35,
        oneof="data",
        message=data_model.TimeInHeartRateZone,
    )
    active_minutes: data_model.ActiveMinutes = proto.Field(
        proto.MESSAGE,
        number=36,
        oneof="data",
        message=data_model.ActiveMinutes,
    )
    respiratory_rate_sleep_summary: data_model.RespiratoryRateSleepSummary = (
        proto.Field(
            proto.MESSAGE,
            number=37,
            oneof="data",
            message=data_model.RespiratoryRateSleepSummary,
        )
    )
    daily_respiratory_rate: data_model.DailyRespiratoryRate = proto.Field(
        proto.MESSAGE,
        number=38,
        oneof="data",
        message=data_model.DailyRespiratoryRate,
    )
    swim_lengths_data: data_model.SwimLengthsData = proto.Field(
        proto.MESSAGE,
        number=39,
        oneof="data",
        message=data_model.SwimLengthsData,
    )
    height: data_model.Height = proto.Field(
        proto.MESSAGE,
        number=40,
        oneof="data",
        message=data_model.Height,
    )
    basal_energy_burned: data_model.BasalEnergyBurned = proto.Field(
        proto.MESSAGE,
        number=41,
        oneof="data",
        message=data_model.BasalEnergyBurned,
    )
    core_body_temperature: data_model.CoreBodyTemperature = proto.Field(
        proto.MESSAGE,
        number=42,
        oneof="data",
        message=data_model.CoreBodyTemperature,
    )
    active_energy_burned: data_model.ActiveEnergyBurned = proto.Field(
        proto.MESSAGE,
        number=44,
        oneof="data",
        message=data_model.ActiveEnergyBurned,
    )
    blood_glucose: data_model.BloodGlucose = proto.Field(
        proto.MESSAGE,
        number=46,
        oneof="data",
        message=data_model.BloodGlucose,
    )
    data_point_name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class RollupDataPoint(proto.Message):
    r"""Value of a rollup for a single physical time interval
    (aggregation window) of reconciled data points from all data
    sources, excluding those data points that are identified as
    recorded by wearables in intervals when they were not actually
    worn.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        steps (google.devicesandservices.health_v4.types.StepsRollupValue):
            Returned by default when rolling up data points from the
            ``steps`` data type, or when requested explicitly using the
            ``steps`` rollup type identifier.

            This field is a member of `oneof`_ ``value``.
        floors (google.devicesandservices.health_v4.types.FloorsRollupValue):
            Returned by default when rolling up data points from the
            ``floors`` data type, or when requested explicitly using the
            ``floors`` rollup type identifier.

            This field is a member of `oneof`_ ``value``.
        heart_rate (google.devicesandservices.health_v4.types.HeartRateRollupValue):
            Returned by default when rolling up data points from the
            ``heart-rate`` data type, or when requested explicitly using
            the ``heart-rate`` rollup type identifier.

            This field is a member of `oneof`_ ``value``.
        weight (google.devicesandservices.health_v4.types.WeightRollupValue):
            Returned by default when rolling up data points from the
            ``weight`` data type, or when requested explicitly using the
            ``weight`` rollup type identifier.

            This field is a member of `oneof`_ ``value``.
        altitude (google.devicesandservices.health_v4.types.AltitudeRollupValue):
            Returned by default when rolling up data points from the
            ``altitude`` data type, or when requested explicitly using
            the ``altitude`` rollup type identifier.

            This field is a member of `oneof`_ ``value``.
        distance (google.devicesandservices.health_v4.types.DistanceRollupValue):
            Returned by default when rolling up data points from the
            ``distance`` data type, or when requested explicitly using
            the ``distance`` rollup type identifier.

            This field is a member of `oneof`_ ``value``.
        body_fat (google.devicesandservices.health_v4.types.BodyFatRollupValue):
            Returned by default when rolling up data points from the
            ``body-fat`` data type, or when requested explicitly using
            the ``body-fat`` rollup type identifier.

            This field is a member of `oneof`_ ``value``.
        total_calories (google.devicesandservices.health_v4.types.TotalCaloriesRollupValue):
            Returned by default when rolling up data points from the
            ``total-calories`` data type, or when requested explicitly
            using the ``total-calories`` rollup type identifier.

            This field is a member of `oneof`_ ``value``.
        active_zone_minutes (google.devicesandservices.health_v4.types.ActiveZoneMinutesRollupValue):
            Returned by default when rolling up data points from the
            ``active-zone-minutes`` data type, or when requested
            explicitly using the ``active-zone-minutes`` rollup type
            identifier.

            This field is a member of `oneof`_ ``value``.
        sedentary_period (google.devicesandservices.health_v4.types.SedentaryPeriodRollupValue):
            Returned by default when rolling up data points from the
            ``sedentary-period`` data type, or when requested explicitly
            using the ``sedentary-period`` rollup type identifier.

            This field is a member of `oneof`_ ``value``.
        run_vo2_max (google.devicesandservices.health_v4.types.RunVO2MaxRollupValue):
            Returned by default when rolling up data points from the
            ``run-vo2-max`` data type, or when requested explicitly
            using the ``run-vo2-max`` rollup type identifier.

            This field is a member of `oneof`_ ``value``.
        calories_in_heart_rate_zone (google.devicesandservices.health_v4.types.CaloriesInHeartRateZoneRollupValue):
            Returned by default when rolling up data points from the
            ``calories-in-heart-rate-zone`` data type, or when requested
            explicitly using the ``calories-in-heart-rate-zone`` rollup
            type identifier.

            This field is a member of `oneof`_ ``value``.
        activity_level (google.devicesandservices.health_v4.types.ActivityLevelRollupValue):
            Returned by default when rolling up data points from the
            ``activity-level`` data type, or when requested explicitly
            using the ``activity-level`` rollup type identifier.

            This field is a member of `oneof`_ ``value``.
        nutrition_log (google.devicesandservices.health_v4.types.NutritionLogRollupValue):
            Returned by default when rolling up data points from the
            ``nutrition-log`` data type, or when requested explicitly
            using the ``nutrition-log`` rollup type identifier.

            This field is a member of `oneof`_ ``value``.
        hydration_log (google.devicesandservices.health_v4.types.HydrationLogRollupValue):
            Returned by default when rolling up data points from the
            ``hydration-log`` data type, or when requested explicitly
            using the ``hydration-log`` rollup type identifier.

            This field is a member of `oneof`_ ``value``.
        time_in_heart_rate_zone (google.devicesandservices.health_v4.types.TimeInHeartRateZoneRollupValue):
            Returned by default when rolling up data points from the
            ``time-in-heart-rate-zone`` data type, or when requested
            explicitly using the ``time-in-heart-rate-zone`` rollup type
            identifier.

            This field is a member of `oneof`_ ``value``.
        active_minutes (google.devicesandservices.health_v4.types.ActiveMinutesRollupValue):
            Returned by default when rolling up data points from the
            ``active-minutes`` data type, or when requested explicitly
            using the ``active-minutes`` rollup type identifier.

            This field is a member of `oneof`_ ``value``.
        swim_lengths_data (google.devicesandservices.health_v4.types.SwimLengthsDataRollupValue):
            Returned by default when rolling up data points from the
            ``swim-lengths-data`` data type, or when requested
            explicitly using the ``swim-lengths-data`` rollup type
            identifier.

            This field is a member of `oneof`_ ``value``.
        core_body_temperature (google.devicesandservices.health_v4.types.CoreBodyTemperatureRollupValue):
            Returned by default when rolling up data points from the
            ``core-body-temperature`` data type, or when requested
            explicitly using the ``core-body-temperature`` rollup type
            identifier.

            This field is a member of `oneof`_ ``value``.
        active_energy_burned (google.devicesandservices.health_v4.types.ActiveEnergyBurnedRollupValue):
            Returned by default when rolling up data points from the
            ``active-energy-burned`` data type.

            This field is a member of `oneof`_ ``value``.
        blood_glucose (google.devicesandservices.health_v4.types.BloodGlucoseRollupValue):
            Returned by default when rolling up data points from the
            ``blood-glucose`` data type.

            This field is a member of `oneof`_ ``value``.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Start time of the window this value
            aggregates over
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            End time of the window this value aggregates
            over
    """

    steps: data_model.StepsRollupValue = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="value",
        message=data_model.StepsRollupValue,
    )
    floors: data_model.FloorsRollupValue = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="value",
        message=data_model.FloorsRollupValue,
    )
    heart_rate: data_model.HeartRateRollupValue = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="value",
        message=data_model.HeartRateRollupValue,
    )
    weight: data_model.WeightRollupValue = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="value",
        message=data_model.WeightRollupValue,
    )
    altitude: data_model.AltitudeRollupValue = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="value",
        message=data_model.AltitudeRollupValue,
    )
    distance: data_model.DistanceRollupValue = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="value",
        message=data_model.DistanceRollupValue,
    )
    body_fat: data_model.BodyFatRollupValue = proto.Field(
        proto.MESSAGE,
        number=11,
        oneof="value",
        message=data_model.BodyFatRollupValue,
    )
    total_calories: data_model.TotalCaloriesRollupValue = proto.Field(
        proto.MESSAGE,
        number=12,
        oneof="value",
        message=data_model.TotalCaloriesRollupValue,
    )
    active_zone_minutes: data_model.ActiveZoneMinutesRollupValue = proto.Field(
        proto.MESSAGE,
        number=13,
        oneof="value",
        message=data_model.ActiveZoneMinutesRollupValue,
    )
    sedentary_period: data_model.SedentaryPeriodRollupValue = proto.Field(
        proto.MESSAGE,
        number=15,
        oneof="value",
        message=data_model.SedentaryPeriodRollupValue,
    )
    run_vo2_max: data_model.RunVO2MaxRollupValue = proto.Field(
        proto.MESSAGE,
        number=16,
        oneof="value",
        message=data_model.RunVO2MaxRollupValue,
    )
    calories_in_heart_rate_zone: data_model.CaloriesInHeartRateZoneRollupValue = (
        proto.Field(
            proto.MESSAGE,
            number=17,
            oneof="value",
            message=data_model.CaloriesInHeartRateZoneRollupValue,
        )
    )
    activity_level: data_model.ActivityLevelRollupValue = proto.Field(
        proto.MESSAGE,
        number=18,
        oneof="value",
        message=data_model.ActivityLevelRollupValue,
    )
    nutrition_log: data_model.NutritionLogRollupValue = proto.Field(
        proto.MESSAGE,
        number=19,
        oneof="value",
        message=data_model.NutritionLogRollupValue,
    )
    hydration_log: data_model.HydrationLogRollupValue = proto.Field(
        proto.MESSAGE,
        number=20,
        oneof="value",
        message=data_model.HydrationLogRollupValue,
    )
    time_in_heart_rate_zone: data_model.TimeInHeartRateZoneRollupValue = proto.Field(
        proto.MESSAGE,
        number=21,
        oneof="value",
        message=data_model.TimeInHeartRateZoneRollupValue,
    )
    active_minutes: data_model.ActiveMinutesRollupValue = proto.Field(
        proto.MESSAGE,
        number=22,
        oneof="value",
        message=data_model.ActiveMinutesRollupValue,
    )
    swim_lengths_data: data_model.SwimLengthsDataRollupValue = proto.Field(
        proto.MESSAGE,
        number=23,
        oneof="value",
        message=data_model.SwimLengthsDataRollupValue,
    )
    core_body_temperature: data_model.CoreBodyTemperatureRollupValue = proto.Field(
        proto.MESSAGE,
        number=24,
        oneof="value",
        message=data_model.CoreBodyTemperatureRollupValue,
    )
    active_energy_burned: data_model.ActiveEnergyBurnedRollupValue = proto.Field(
        proto.MESSAGE,
        number=25,
        oneof="value",
        message=data_model.ActiveEnergyBurnedRollupValue,
    )
    blood_glucose: data_model.BloodGlucoseRollupValue = proto.Field(
        proto.MESSAGE,
        number=26,
        oneof="value",
        message=data_model.BloodGlucoseRollupValue,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )


class DailyRollupDataPoint(proto.Message):
    r"""Value of a daily rollup for a single civil time interval
    (aggregation window) of reconciled data points from all data
    sources, excluding those data points that are identified as
    recorded by wearables in intervals when they were not actually
    worn.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        steps (google.devicesandservices.health_v4.types.StepsRollupValue):
            Returned by default when rolling up data points from the
            ``steps`` data type, or when requested explicitly using the
            ``steps`` rollup type identifier.

            This field is a member of `oneof`_ ``value``.
        floors (google.devicesandservices.health_v4.types.FloorsRollupValue):
            Returned by default when rolling up data points from the
            ``floors`` data type, or when requested explicitly using the
            ``floors`` rollup type identifier.

            This field is a member of `oneof`_ ``value``.
        heart_rate (google.devicesandservices.health_v4.types.HeartRateRollupValue):
            Returned by default when rolling up data points from the
            ``heart-rate`` data type, or when requested explicitly using
            the ``heart-rate`` rollup type identifier.

            This field is a member of `oneof`_ ``value``.
        resting_heart_rate_personal_range (google.devicesandservices.health_v4.types.RestingHeartRatePersonalRangeRollupValue):
            Returned by default when rolling up data points from the
            ``daily-resting-heart-rate`` data type, or when requested
            explicitly using the ``resting-heart-rate-personal-range``
            rollup type identifier.

            This field is a member of `oneof`_ ``value``.
        heart_rate_variability_personal_range (google.devicesandservices.health_v4.types.HeartRateVariabilityPersonalRangeRollupValue):
            Returned by default when rolling up data points from the
            ``daily-heart-rate-variability`` data type, or when
            requested explicitly using the
            ``heart-rate-variability-personal-range`` rollup type
            identifier.

            This field is a member of `oneof`_ ``value``.
        weight (google.devicesandservices.health_v4.types.WeightRollupValue):
            Returned by default when rolling up data points from the
            ``weight`` data type, or when requested explicitly using the
            ``weight`` rollup type identifier.

            This field is a member of `oneof`_ ``value``.
        altitude (google.devicesandservices.health_v4.types.AltitudeRollupValue):
            Returned by default when rolling up data points from the
            ``altitude`` data type, or when requested explicitly using
            the ``altitude`` rollup type identifier.

            This field is a member of `oneof`_ ``value``.
        distance (google.devicesandservices.health_v4.types.DistanceRollupValue):
            Returned by default when rolling up data points from the
            ``distance`` data type, or when requested explicitly using
            the ``distance`` rollup type identifier.

            This field is a member of `oneof`_ ``value``.
        body_fat (google.devicesandservices.health_v4.types.BodyFatRollupValue):
            Returned by default when rolling up data points from the
            ``body-fat`` data type, or when requested explicitly using
            the ``body-fat`` rollup type identifier.

            This field is a member of `oneof`_ ``value``.
        total_calories (google.devicesandservices.health_v4.types.TotalCaloriesRollupValue):
            Returned by default when rolling up data points from the
            ``total-calories`` data type, or when requested explicitly
            using the ``total-calories`` rollup type identifier.

            This field is a member of `oneof`_ ``value``.
        active_zone_minutes (google.devicesandservices.health_v4.types.ActiveZoneMinutesRollupValue):
            Returned by default when rolling up data points from the
            ``active-zone-minutes`` data type, or when requested
            explicitly using the ``active-zone-minutes`` rollup type
            identifier.

            This field is a member of `oneof`_ ``value``.
        sedentary_period (google.devicesandservices.health_v4.types.SedentaryPeriodRollupValue):
            Returned by default when rolling up data points from the
            ``sedentary-period`` data type, or when requested explicitly
            using the ``sedentary-period`` rollup type identifier.

            This field is a member of `oneof`_ ``value``.
        run_vo2_max (google.devicesandservices.health_v4.types.RunVO2MaxRollupValue):
            Returned by default when rolling up data points from the
            ``run-vo2-max`` data type, or when requested explicitly
            using the ``run-vo2-max`` rollup type identifier.

            This field is a member of `oneof`_ ``value``.
        calories_in_heart_rate_zone (google.devicesandservices.health_v4.types.CaloriesInHeartRateZoneRollupValue):
            Returned by default when rolling up data points from the
            ``calories-in-heart-rate-zone`` data type, or when requested
            explicitly using the ``calories-in-heart-rate-zone`` rollup
            type identifier.

            This field is a member of `oneof`_ ``value``.
        activity_level (google.devicesandservices.health_v4.types.ActivityLevelRollupValue):
            Returned by default when rolling up data points from the
            ``activity-level`` data type, or when requested explicitly
            using the ``activity-level`` rollup type identifier.

            This field is a member of `oneof`_ ``value``.
        nutrition_log (google.devicesandservices.health_v4.types.NutritionLogRollupValue):
            Returned by default when rolling up data points from the
            ``nutrition-log`` data type, or when requested explicitly
            using the ``nutrition-log`` rollup type identifier.

            This field is a member of `oneof`_ ``value``.
        hydration_log (google.devicesandservices.health_v4.types.HydrationLogRollupValue):
            Returned by default when rolling up data points from the
            ``hydration-log`` data type, or when requested explicitly
            using the ``hydration-log`` rollup type identifier.

            This field is a member of `oneof`_ ``value``.
        time_in_heart_rate_zone (google.devicesandservices.health_v4.types.TimeInHeartRateZoneRollupValue):
            Returned by default when rolling up data points from the
            ``time-in-heart-rate-zone`` data type, or when requested
            explicitly using the ``time-in-heart-rate-zone`` rollup type
            identifier.

            This field is a member of `oneof`_ ``value``.
        active_minutes (google.devicesandservices.health_v4.types.ActiveMinutesRollupValue):
            Returned by default when rolling up data points from the
            ``active-minutes`` data type, or when requested explicitly
            using the ``active-minutes`` rollup type identifier.

            This field is a member of `oneof`_ ``value``.
        swim_lengths_data (google.devicesandservices.health_v4.types.SwimLengthsDataRollupValue):
            Returned by default when rolling up data points from the
            ``swim-lengths-data`` data type, or when requested
            explicitly using the ``swim-lengths-data`` rollup type
            identifier.

            This field is a member of `oneof`_ ``value``.
        core_body_temperature (google.devicesandservices.health_v4.types.CoreBodyTemperatureRollupValue):
            Returned by default when rolling up data points from the
            ``core-body-temperature`` data type, or when requested
            explicitly using the ``core-body-temperature`` rollup type
            identifier.

            This field is a member of `oneof`_ ``value``.
        active_energy_burned (google.devicesandservices.health_v4.types.ActiveEnergyBurnedRollupValue):
            Returned by default when rolling up data points from the
            ``active-energy-burned`` data type.

            This field is a member of `oneof`_ ``value``.
        blood_glucose (google.devicesandservices.health_v4.types.BloodGlucoseRollupValue):
            Returned by default when rolling up data points from the
            ``blood-glucose`` data type.

            This field is a member of `oneof`_ ``value``.
        civil_start_time (google.devicesandservices.health_v4.types.CivilDateTime):
            Start time of the window this value
            aggregates over
        civil_end_time (google.devicesandservices.health_v4.types.CivilDateTime):
            End time of the window this value aggregates
            over
    """

    steps: data_model.StepsRollupValue = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="value",
        message=data_model.StepsRollupValue,
    )
    floors: data_model.FloorsRollupValue = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="value",
        message=data_model.FloorsRollupValue,
    )
    heart_rate: data_model.HeartRateRollupValue = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="value",
        message=data_model.HeartRateRollupValue,
    )
    resting_heart_rate_personal_range: data_model.RestingHeartRatePersonalRangeRollupValue = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="value",
        message=data_model.RestingHeartRatePersonalRangeRollupValue,
    )
    heart_rate_variability_personal_range: data_model.HeartRateVariabilityPersonalRangeRollupValue = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="value",
        message=data_model.HeartRateVariabilityPersonalRangeRollupValue,
    )
    weight: data_model.WeightRollupValue = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="value",
        message=data_model.WeightRollupValue,
    )
    altitude: data_model.AltitudeRollupValue = proto.Field(
        proto.MESSAGE,
        number=11,
        oneof="value",
        message=data_model.AltitudeRollupValue,
    )
    distance: data_model.DistanceRollupValue = proto.Field(
        proto.MESSAGE,
        number=12,
        oneof="value",
        message=data_model.DistanceRollupValue,
    )
    body_fat: data_model.BodyFatRollupValue = proto.Field(
        proto.MESSAGE,
        number=13,
        oneof="value",
        message=data_model.BodyFatRollupValue,
    )
    total_calories: data_model.TotalCaloriesRollupValue = proto.Field(
        proto.MESSAGE,
        number=14,
        oneof="value",
        message=data_model.TotalCaloriesRollupValue,
    )
    active_zone_minutes: data_model.ActiveZoneMinutesRollupValue = proto.Field(
        proto.MESSAGE,
        number=15,
        oneof="value",
        message=data_model.ActiveZoneMinutesRollupValue,
    )
    sedentary_period: data_model.SedentaryPeriodRollupValue = proto.Field(
        proto.MESSAGE,
        number=17,
        oneof="value",
        message=data_model.SedentaryPeriodRollupValue,
    )
    run_vo2_max: data_model.RunVO2MaxRollupValue = proto.Field(
        proto.MESSAGE,
        number=18,
        oneof="value",
        message=data_model.RunVO2MaxRollupValue,
    )
    calories_in_heart_rate_zone: data_model.CaloriesInHeartRateZoneRollupValue = (
        proto.Field(
            proto.MESSAGE,
            number=19,
            oneof="value",
            message=data_model.CaloriesInHeartRateZoneRollupValue,
        )
    )
    activity_level: data_model.ActivityLevelRollupValue = proto.Field(
        proto.MESSAGE,
        number=20,
        oneof="value",
        message=data_model.ActivityLevelRollupValue,
    )
    nutrition_log: data_model.NutritionLogRollupValue = proto.Field(
        proto.MESSAGE,
        number=21,
        oneof="value",
        message=data_model.NutritionLogRollupValue,
    )
    hydration_log: data_model.HydrationLogRollupValue = proto.Field(
        proto.MESSAGE,
        number=22,
        oneof="value",
        message=data_model.HydrationLogRollupValue,
    )
    time_in_heart_rate_zone: data_model.TimeInHeartRateZoneRollupValue = proto.Field(
        proto.MESSAGE,
        number=23,
        oneof="value",
        message=data_model.TimeInHeartRateZoneRollupValue,
    )
    active_minutes: data_model.ActiveMinutesRollupValue = proto.Field(
        proto.MESSAGE,
        number=24,
        oneof="value",
        message=data_model.ActiveMinutesRollupValue,
    )
    swim_lengths_data: data_model.SwimLengthsDataRollupValue = proto.Field(
        proto.MESSAGE,
        number=25,
        oneof="value",
        message=data_model.SwimLengthsDataRollupValue,
    )
    core_body_temperature: data_model.CoreBodyTemperatureRollupValue = proto.Field(
        proto.MESSAGE,
        number=26,
        oneof="value",
        message=data_model.CoreBodyTemperatureRollupValue,
    )
    active_energy_burned: data_model.ActiveEnergyBurnedRollupValue = proto.Field(
        proto.MESSAGE,
        number=27,
        oneof="value",
        message=data_model.ActiveEnergyBurnedRollupValue,
    )
    blood_glucose: data_model.BloodGlucoseRollupValue = proto.Field(
        proto.MESSAGE,
        number=28,
        oneof="value",
        message=data_model.BloodGlucoseRollupValue,
    )
    civil_start_time: data_coordinates.CivilDateTime = proto.Field(
        proto.MESSAGE,
        number=1,
        message=data_coordinates.CivilDateTime,
    )
    civil_end_time: data_coordinates.CivilDateTime = proto.Field(
        proto.MESSAGE,
        number=2,
        message=data_coordinates.CivilDateTime,
    )


class GetDataPointRequest(proto.Message):
    r"""Request for getting a single data point

    Attributes:
        name (str):
            Required. The name of the data point to retrieve.

            Format:
            ``users/{user}/dataTypes/{data_type}/dataPoints/{data_point}``

            See
            [DataPoint.name][google.devicesandservices.health.v4.DataPoint.name]
            for examples and possible values.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListDataPointsRequest(proto.Message):
    r"""Request for listing raw data points

    Attributes:
        parent (str):
            Required. Parent data type of the Data Point collection.

            Format: ``users/me/dataTypes/{data_type}``, e.g.:

            - ``users/me/dataTypes/steps``
            - ``users/me/dataTypes/weight``

            For a list of the supported data types see the [DataPoint
            data][google.devicesandservices.health.v4.DataPoint] union
            field.
        page_size (int):
            Optional. The maximum number of data points to return. If
            unspecified, at most 1440 data points will be returned. The
            maximum page size is 10000; values above that will be
            truncated accordingly. For ``exercise`` and ``sleep`` the
            default page size is 25. The maximum page size for
            ``exercise`` and ``sleep`` is 25.
        page_token (str):
            Optional. The ``next_page_token`` from a previous request,
            if any.
        filter (str):
            Optional. Filter expression following
            https://google.aip.dev/160.

            A time range (either physical or civil) can be specified.

            The supported filter fields are:

            - Interval start time:

              - Pattern: ``{interval_data_type}.interval.start_time``
              - Supported comparison operators: ``>=``, ``<``
              - Timestamp literal expected in RFC-3339 format
              - Supported logical operators: ``AND``
              - Example:

                - ``steps.interval.start_time >= "2023-11-24T00:00:00Z" AND steps.interval.start_time < "2023-11-25T00:00:00Z"``
                - ``distance.interval.start_time >= "2024-08-14T12:34:56Z"``

            - Interval civil start time:

              - Pattern:
                ``{interval_data_type}.interval.civil_start_time``
              - Supported comparison operators: ``>=``, ``<``
              - Date with optional time literal expected in ISO 8601
                ``YYYY-MM-DD[THH:mm:ss]`` format
              - Supported logical operators: ``AND``
              - Example:

                - ``steps.interval.civil_start_time >= "2023-11-24" AND steps.interval.civil_start_time < "2023-11-25"``
                - ``distance.interval.civil_start_time >= "2024-08-14T12:34:56"``

            - Sample observation physical time:

              - Pattern:
                ``{sample_data_type}.sample_time.physical_time``
              - Supported comparison operators: ``>=``, ``<``
              - Timestamp literal expected in RFC-3339 format
              - Supported logical operators: ``AND``
              - Example:

                - ``weight.sample_time.physical_time >= "2023-11-24T00:00:00Z" AND weight.sample_time.physical_time < "2023-11-25T00:00:00Z"``
                - ``weight.sample_time.physical_time >= "2024-08-14T12:34:56Z"``

            - Sample observation civil time:

              - Pattern: ``{sample_data_type}.sample_time.civil_time``
              - Supported comparison operators: ``>=``, ``<``
              - Date with optional time literal expected in ISO 8601
                ``YYYY-MM-DD[THH:mm:ss]`` format
              - Supported logical operators: ``AND``
              - Example:

                - ``weight.sample_time.civil_time >= "2023-11-24" AND weight.sample_time.civil_time < "2023-11-25"``
                - ``weight.sample_time.civil_time >= "2024-08-14T12:34:56"``

            - Daily summary date:

              - Pattern: ``{daily_summary_data_type}.date``
              - Supported comparison operators: ``>=``, ``<``
              - Date literal expected in ISO 8601 ``YYYY-MM-DD`` format
              - Supported logical operators: ``AND``
              - Example:

                - ``daily_heart_rate_variability.date < "2024-08-15"``

            - Session civil start time (**Excluding Sleep and ECG**):

              - Pattern:
                ``{session_data_type}.interval.civil_start_time``
              - Supported comparison operators: ``>=``, ``<``
              - Date with optional time literal expected in ISO 8601
                ``YYYY-MM-DD[THH:mm:ss]`` format
              - Supported logical operators: ``AND``
              - Example:

                - ``exercise.interval.civil_start_time >= "2023-11-24" AND exercise.interval.civil_start_time < "2023-11-25"``
                - ``exercise.interval.civil_start_time >= "2024-08-14T12:34:56"``

            - Session start time (**ECG specific**):

              - Pattern: ``electrocardiogram.interval.start_time``
              - Supported comparison operators: ``>=``
              - Timestamp literal expected in RFC-3339 format
              - Example:

                - ``electrocardiogram.interval.start_time >= "2024-08-14T12:34:56Z"``

              - Note: Only filtering by start time is supported for ECG.
                Filtering by end time (e.g.,
                ``electrocardiogram.interval.end_time``) is not
                supported.

            - Session end time (**Sleep specific**):

              - Pattern: ``sleep.interval.end_time``
              - Supported comparison operators: ``>=``, ``<``
              - Timestamp literal expected in RFC-3339 format
              - Supported logical operators: ``AND``, ``OR``
              - Example:

                - ``sleep.interval.end_time >= "2023-11-24T00:00:00Z" AND sleep.interval.end_time < "2023-11-25T00:00:00Z"``

            - Session civil end time (**Sleep specific**):

              - Pattern: ``sleep.interval.civil_end_time``
              - Supported comparison operators: ``>=``, ``<``
              - Date with optional time literal expected in ISO 8601
                ``YYYY-MM-DD[THH:mm:ss]`` format
              - Supported logical operators: ``AND``, ``OR``
              - Example:

                - ``sleep.interval.civil_end_time >= "2023-11-24" AND sleep.interval.civil_end_time < "2023-11-25"``

            Data points in the response will be ordered by the interval
            start time in descending order.
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
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListDataPointsResponse(proto.Message):
    r"""Response containing raw data points matching the query

    Attributes:
        data_points (MutableSequence[google.devicesandservices.health_v4.types.DataPoint]):
            Data points matching the query
        next_page_token (str):
            Next page token, empty if the response is
            complete
    """

    @property
    def raw_page(self):
        return self

    data_points: MutableSequence["DataPoint"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="DataPoint",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateDataPointRequest(proto.Message):
    r"""Request to create an identifiable data point.

    Attributes:
        parent (str):
            Required. The parent resource name where the data point will
            be created. Format: ``users/{user}/dataTypes/{data_type}``
        data_point (google.devicesandservices.health_v4.types.DataPoint):
            Required. The data point to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    data_point: "DataPoint" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="DataPoint",
    )


class CreateDataPointOperationMetadata(proto.Message):
    r"""Metadata for a create data point operation."""


class UpdateDataPointRequest(proto.Message):
    r"""Request to update an identifiable data point.

    Attributes:
        data_point (google.devicesandservices.health_v4.types.DataPoint):
            Required. The data point to update

            The data point's ``name`` field is used to identify the data
            point to update.

            Format:
            ``users/{user}/dataTypes/{data_type}/dataPoints/{data_point}``
    """

    data_point: "DataPoint" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="DataPoint",
    )


class UpdateDataPointOperationMetadata(proto.Message):
    r"""Metadata for an update data point operation."""


class BatchDeleteDataPointsRequest(proto.Message):
    r"""Request to delete a batch of identifiable data points.

    Attributes:
        parent (str):
            Optional. Parent (data type) for the Data Point collection
            Format: ``users/me/dataTypes/{data_type}``, e.g.:

            - ``users/me/dataTypes/steps``
            - ``users/me/dataTypes/-``

            For a list of the supported data types see the [DataPoint
            data][google.devicesandservices.health.v4.DataPoint] union
            field.

            Deleting data points across multiple data type collections
            is supported following https://aip.dev/159.

            If this is set, the parent of all of the data points
            specified in ``names`` must match this field.
        names (MutableSequence[str]):
            Required. The names of the DataPoints to
            delete. A maximum of 10000 data points can be
            deleted in a single request.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchDeleteDataPointsResponse(proto.Message):
    r"""Response containing the list of possibly soft-deleted
    DataPoints.

    Attributes:
        data_points (MutableSequence[google.devicesandservices.health_v4.types.DataPoint]):
            The list of soft-deleted DataPoints, if the
            data type supports only soft deletion.
    """

    data_points: MutableSequence["DataPoint"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="DataPoint",
    )


class BatchDeleteDataPointsOperationMetadata(proto.Message):
    r"""Metadata for a batch delete data points operation.

    Attributes:
        failed_requests (MutableMapping[int, google.rpc.status_pb2.Status]):
            The key in this map is the index of the request in the
            ``requests`` field in the batch request.
    """

    failed_requests: MutableMapping[int, status_pb2.Status] = proto.MapField(
        proto.INT32,
        proto.MESSAGE,
        number=1,
        message=status_pb2.Status,
    )


class ReconcileDataPointsRequest(proto.Message):
    r"""Request to reconcile data points from multiple data sources.

    Attributes:
        parent (str):
            Required. Parent data type of the Data Point collection.

            Format: ``users/me/dataTypes/{data_type}``, e.g.:

            - ``users/me/dataTypes/steps``
            - ``users/me/dataTypes/heart-rate``

            For a list of the supported data types see the [DataPoint
            data][google.devicesandservices.health.v4.DataPoint] union
            field.
        page_size (int):
            Optional. The maximum number of data points to return. If
            unspecified, at most 1440 data points will be returned. The
            maximum page size is 10000; values above that will be
            truncated accordingly. For ``exercise`` and ``sleep`` the
            default page size is 25. The maximum page size for
            ``exercise`` and ``sleep`` is 25.
        page_token (str):
            Optional. The ``next_page_token`` from a previous request,
            if any.
        filter (str):
            Optional. Filter expression based on https://aip.dev/160.

            A time range, either physical or civil, can be specified.
            See the
            [ListDataPointsRequest.filter][google.devicesandservices.health.v4.ListDataPointsRequest.filter]
            for the supported fields and syntax.
        data_source_family (str):
            Optional. The data source family name to reconcile.

            If empty, data points from all data sources will be
            reconciled.

            Format: ``users/me/dataSourceFamilies/{data_source_family}``

            - ``users/me/dataSourceFamilies/all-sources`` - Default
              value. Includes data from all available data sources.
            - ``users/me/dataSourceFamilies/google-wearables`` -
              Includes data from Google and Fitbit tracker devices (such
              as Fitbit trackers and Pixel Watch). Excludes manually
              logged data.
            - ``users/me/dataSourceFamilies/google-sources`` - Includes
              first-party Google data, such as data from tracker
              devices, manually logged data, and Health Connect.
            - ``users/me/dataSourceFamilies/self-sources`` - Includes
              only the data the calling client wrote through this API,
              that is, data points whose data source was registered
              through this API with the same OAuth client ID as the
              caller.

            Callers that were only granted write scopes for the
            requested data type may only read the data they wrote
            themselves: their requests are implicitly restricted to
            ``self-sources``, and requesting any other data source
            family fails with ``PERMISSION_DENIED``.

            If no data point matches the requested data source family,
            the response is an empty list rather than an error.
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
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )
    data_source_family: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ReconcileDataPointsResponse(proto.Message):
    r"""Response containing the list of reconciled DataPoints.

    Attributes:
        data_points (MutableSequence[google.devicesandservices.health_v4.types.ReconciledDataPoint]):
            Data points matching the query
        next_page_token (str):
            Next page token, empty if the response is
            complete
    """

    @property
    def raw_page(self):
        return self

    data_points: MutableSequence["ReconciledDataPoint"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ReconciledDataPoint",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class RollUpDataPointsRequest(proto.Message):
    r"""Request to roll up data points by physical time intervals.

    Attributes:
        parent (str):
            Required. Parent data type of the Data Point collection.

            Format: ``users/{user}/dataTypes/{data_type}``, e.g.:

            - ``users/me/dataTypes/steps``
            - ``users/me/dataTypes/distance``

            For a list of the supported data types see the
            [RollupDataPoint
            value][google.devicesandservices.health.v4.RollupDataPoint]
            union field.
        range_ (google.type.interval_pb2.Interval):
            Required. Closed-open range of data points that will be
            rolled up. The maximum range for
            ``calories-in-heart-rate-zone``, ``heart-rate``,
            ``active-minutes`` and ``total-calories`` is 14 days. The
            maximum range for all other data types is 90 days.
        window_size (google.protobuf.duration_pb2.Duration):
            Required. The size of the time window to group data points
            into before applying the aggregation functions. Must be at
            least 1 second.

            If the requested range is not an exact multiple of
            ``window_size``, the final bucket chronologically will be
            truncated at the upper endpoint of the range and will cover
            a duration shorter than ``window_size``.
        page_size (int):
            Optional. The maximum number of data points
            to return. If unspecified, at most 1440 data
            points will be returned. The maximum page size
            is 10000; values above that will be truncated
            accordingly.
        page_token (str):
            Optional. The next_page_token from a previous request, if
            any. All other request fields need to be the same as in the
            initial request when the page token is specified.
        data_source_family (str):
            Optional. The data source family name to roll up.

            If empty, data points from all available data sources will
            be rolled up.

            Format: ``users/me/dataSourceFamilies/{data_source_family}``

            The supported values are:

            - ``users/me/dataSourceFamilies/all-sources`` - Default
              value. Includes data from all available data sources.
            - ``users/me/dataSourceFamilies/google-wearables`` -
              Includes data from Google and Fitbit tracker devices (such
              as Fitbit trackers and Pixel Watch). Excludes manually
              logged data.
            - ``users/me/dataSourceFamilies/google-sources`` - Includes
              first-party Google data, such as data from tracker
              devices, manually logged data, and Health Connect.
            - ``users/me/dataSourceFamilies/self-sources`` - Includes
              only the data the calling client wrote through this API,
              that is, data points whose data source was registered
              through this API with the same OAuth client ID as the
              caller.

            Callers that were only granted write scopes for the
            requested data type may only read the data they wrote
            themselves: their requests are implicitly restricted to
            ``self-sources``, and requesting any other data source
            family fails with ``PERMISSION_DENIED``.

            If no data point matches the requested data source family,
            the response is an empty list rather than an error.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    range_: interval_pb2.Interval = proto.Field(
        proto.MESSAGE,
        number=2,
        message=interval_pb2.Interval,
    )
    window_size: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=3,
        message=duration_pb2.Duration,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=4,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=5,
    )
    data_source_family: str = proto.Field(
        proto.STRING,
        number=7,
    )


class RollUpDataPointsResponse(proto.Message):
    r"""Response containing the list of rolled up data points.

    Attributes:
        rollup_data_points (MutableSequence[google.devicesandservices.health_v4.types.RollupDataPoint]):
            Values for each aggregation time window.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    rollup_data_points: MutableSequence["RollupDataPoint"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="RollupDataPoint",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DailyRollUpDataPointsRequest(proto.Message):
    r"""Request to roll up data points by civil time intervals.

    Attributes:
        parent (str):
            Required. Parent data type of the Data Point collection.

            Format: ``users/{user}/dataTypes/{data_type}``, e.g.:

            - ``users/me/dataTypes/steps``
            - ``users/me/dataTypes/distance``

            For a list of the supported data types see the
            [DailyRollupDataPoint
            value][google.devicesandservices.health.v4.DailyRollupDataPoint]
            union field.
        range_ (google.devicesandservices.health_v4.types.CivilTimeInterval):
            Required. Closed-open range of data points that will be
            rolled up. The start time must be aligned with the
            aggregation window. The maximum range for
            ``calories-in-heart-rate-zone``, ``heart-rate``,
            ``active-minutes`` and ``total-calories`` is 14 days. The
            maximum range for all other data types is 90 days.
        window_size_days (int):
            Optional. Aggregation window size, in number of days.
            Defaults to 1 if not specified.

            If the requested range is not an exact multiple of
            ``window_size_days``, the final bucket chronologically will
            be truncated at the upper endpoint of the range and will
            cover a duration shorter than ``window_size_days``.
        page_size (int):
            Optional. The maximum number of data points
            to return. If unspecified, at most 1440 data
            points will be returned. The maximum page size
            is 10000; values above that will be truncated
            accordingly.
        page_token (str):
            Optional. The ``next_page_token`` from a previous request,
            if any. All other request fields need to be the same as in
            the initial request when the page token is specified.
        data_source_family (str):
            Optional. The data source family name to roll up. If empty,
            data points from all available data sources will be rolled
            up.

            Format: ``users/me/dataSourceFamilies/{data_source_family}``

            The supported values are:

            - ``users/me/dataSourceFamilies/all-sources`` - Default
              value. Includes data from all available data sources.
            - ``users/me/dataSourceFamilies/google-wearables`` -
              Includes data from Google and Fitbit tracker devices (such
              as Fitbit trackers and Pixel Watch). Excludes manually
              logged data.
            - ``users/me/dataSourceFamilies/google-sources`` - Includes
              first-party Google data, such as data from tracker
              devices, manually logged data, and Health Connect.
            - ``users/me/dataSourceFamilies/self-sources`` - Includes
              only the data the calling client wrote through this API,
              that is, data points whose data source was registered
              through this API with the same OAuth client ID as the
              caller.

            Callers that were only granted write scopes for the
            requested data type may only read the data they wrote
            themselves: their requests are implicitly restricted to
            ``self-sources``, and requesting any other data source
            family fails with ``PERMISSION_DENIED``.

            If no data point matches the requested data source family,
            the response is an empty list rather than an error.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    range_: data_coordinates.CivilTimeInterval = proto.Field(
        proto.MESSAGE,
        number=2,
        message=data_coordinates.CivilTimeInterval,
    )
    window_size_days: int = proto.Field(
        proto.INT32,
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
    data_source_family: str = proto.Field(
        proto.STRING,
        number=7,
    )


class DailyRollUpDataPointsResponse(proto.Message):
    r"""Response containing the list of rolled up data points.

    Attributes:
        rollup_data_points (MutableSequence[google.devicesandservices.health_v4.types.DailyRollupDataPoint]):
            Values for each aggregation time window.
    """

    rollup_data_points: MutableSequence["DailyRollupDataPoint"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="DailyRollupDataPoint",
    )


class DataType(proto.Message):
    r"""Represents a type of health data a user can have data points
    recorded for. It matches the parent resource of collection
    containing data points of the given type.

    Clients currently do not need to interact with this resource
    directly.

    Attributes:
        name (str):
            Identifier. The resource name of the data type.

            Format: ``users/{user}/dataTypes/{data_type}``

            See
            [DataPoint.name][google.devicesandservices.health.v4.DataPoint.name]
            for examples and possible values.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ExportExerciseTcxRequest(proto.Message):
    r"""Represents a request to export exercise data in TCX format.

    Attributes:
        name (str):
            Required. The resource name of the exercise data point to
            export.

            Format:
            ``users/{user}/dataTypes/exercise/dataPoints/{data_point}``
            Example:
            ``users/me/dataTypes/exercise/dataPoints/2026443605080188808``

            The ``{user}`` is the alias ``"me"`` currently. Future
            versions may support user IDs. The ``{data_point}`` ID maps
            to the exercise ID, which is a long integer.
        partial_data (bool):
            Optional. Indicates whether to include the TCX data points
            when the GPS data is not available. If not specified,
            defaults to ``false`` and partial data will not be included.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    partial_data: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class ExportExerciseTcxResponse(proto.Message):
    r"""Represents a Response for exporting exercise data in TCX
    format.

    Attributes:
        tcx_data (str):
            Contains the exported TCX data.

            This field is intended for gRPC clients, as media download
            integration is not supported for gRPC. HTTP clients should
            instead use the ``alt=media`` query parameter to download
            the raw binary TCX file.
    """

    tcx_data: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
