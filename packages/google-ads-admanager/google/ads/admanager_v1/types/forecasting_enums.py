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

import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "ForecastingGrpUnitEnum",
        "ForecastingTargetingDimensionEnum",
        "ForecastingGrpGenderEnum",
        "ForecastingGrpAgeEnum",
    },
)


class ForecastingGrpUnitEnum(proto.Message):
    r"""Wrapper message for
    [ForecastingGrpUnit][google.ads.admanager.v1.ForecastingGrpUnitEnum.ForecastingGrpUnit]

    """

    class ForecastingGrpUnit(proto.Enum):
        r"""Type of unit represented in a GRP demographic breakdown.

        Values:
            FORECASTING_GRP_UNIT_UNSPECIFIED (0):
                Default value. This value is unused.
            IMPRESSIONS (1):
                The type of unit represented in the GRP
                demographic breakdown is impressions.
        """

        FORECASTING_GRP_UNIT_UNSPECIFIED = 0
        IMPRESSIONS = 1


class ForecastingTargetingDimensionEnum(proto.Message):
    r"""Wrapper message for
    [ForecastingTargetingDimension][google.ads.admanager.v1.ForecastingTargetingDimensionEnum.ForecastingTargetingDimension]

    """

    class ForecastingTargetingDimension(proto.Enum):
        r"""Targeting dimension of targeting breakdowns.

        Values:
            FORECASTING_TARGETING_DIMENSION_UNSPECIFIED (0):
                Default value. This value is unused.
            AD_SIZE (1):
                The targeting dimension is ad size.
            AD_UNIT (2):
                The targeting dimension is ad unit.
            BANDWIDTH_GROUP (3):
                The targeting dimension is bandwidth group.
            BROWSER (4):
                The targeting dimension is browser.
            BROWSER_LANGUAGE (5):
                The targeting dimension is browser language.
            CONTENT (6):
                The targeting dimension is content.
            CONTENT_LABEL (7):
                The targeting dimension is content label.
            CUSTOM_CRITERIA (8):
                The targeting dimension is custom criteria.
            DEVICE_CAPABILITY (9):
                The targeting dimension is device capability.
            DEVICE_CATEGORY (10):
                The targeting dimension is device category.
            DEVICE_MANUFACTURER (11):
                The targeting dimension is device
                manufacturer.
            FORECASTED_CREATIVE_RESTRICTION (12):
                The targeting dimension is forecasted
                creative restriction.
            GEOGRAPHY (13):
                The targeting dimension is geography.
            MOBILE_APPLICATION (14):
                The targeting dimension is mobile
                application.
            MOBILE_CARRIER (15):
                The targeting dimension is mobile carrier.
            OPERATING_SYSTEM (16):
                The targeting dimension is operating system.
            PLACEMENT (17):
                The targeting dimension is placement.
            USER_DOMAIN (18):
                The targeting dimension is user domain.
            VERTICAL (19):
                The targeting dimension is vertical.
            VIDEO_POSITION (20):
                The targeting dimension is video position.
        """

        FORECASTING_TARGETING_DIMENSION_UNSPECIFIED = 0
        AD_SIZE = 1
        AD_UNIT = 2
        BANDWIDTH_GROUP = 3
        BROWSER = 4
        BROWSER_LANGUAGE = 5
        CONTENT = 6
        CONTENT_LABEL = 7
        CUSTOM_CRITERIA = 8
        DEVICE_CAPABILITY = 9
        DEVICE_CATEGORY = 10
        DEVICE_MANUFACTURER = 11
        FORECASTED_CREATIVE_RESTRICTION = 12
        GEOGRAPHY = 13
        MOBILE_APPLICATION = 14
        MOBILE_CARRIER = 15
        OPERATING_SYSTEM = 16
        PLACEMENT = 17
        USER_DOMAIN = 18
        VERTICAL = 19
        VIDEO_POSITION = 20


class ForecastingGrpGenderEnum(proto.Message):
    r"""Wrapper message for
    [ForecastingGrpGender][google.ads.admanager.v1.ForecastingGrpGenderEnum.ForecastingGrpGender]

    """

    class ForecastingGrpGender(proto.Enum):
        r"""The demographic gender associated with a GRP demographic
        forecast.

        Values:
            FORECASTING_GRP_GENDER_UNSPECIFIED (0):
                Default value. This value is unused.
            GENDER_FEMALE (1):
                The demographic gender is female.
            GENDER_MALE (2):
                The demographic gender is male.
            GENDER_UNKNOWN (3):
                When gender is not available due to low
                impression levels, GRP privacy thresholds are
                activated and prevent us from specifying gender.
        """

        FORECASTING_GRP_GENDER_UNSPECIFIED = 0
        GENDER_FEMALE = 1
        GENDER_MALE = 2
        GENDER_UNKNOWN = 3


class ForecastingGrpAgeEnum(proto.Message):
    r"""Wrapper message for
    [ForecastingGrpAge][google.ads.admanager.v1.ForecastingGrpAgeEnum.ForecastingGrpAge]

    """

    class ForecastingGrpAge(proto.Enum):
        r"""The age range associated with a GRP demographic forecast.

        Values:
            FORECASTING_GRP_AGE_UNSPECIFIED (0):
                Default value. This value is unused.
            AGE_0_TO_17 (1):
                GRP age range from 0 to 17 years old.
            AGE_18_TO_24 (2):
                GRP age range from 18 to 24 years old.
            AGE_18_TO_49 (3):
                GRP age range from 18 to 49 years old.
            AGE_21_PLUS (4):
                GRP age range from 21 years old and up.
            AGE_21_TO_34 (5):
                GRP age range from 21 to 34 years old.
            AGE_21_TO_44 (6):
                GRP age range from 21 to 44 years old.
            AGE_21_TO_49 (7):
                GRP age range from 21 to 49 years old.
            AGE_21_TO_54 (8):
                GRP age range from 21 to 54 years old.
            AGE_21_TO_64 (9):
                GRP age range from 21 to 64 years old.
            AGE_25_TO_34 (10):
                GRP age range from 25 to 34 years old.
            AGE_25_TO_49 (11):
                GRP age range from 25 to 49 years old.
            AGE_35_TO_44 (12):
                GRP age range from 35 to 44 years old.
            AGE_35_TO_49 (13):
                GRP age range from 35 to 49 years old.
            AGE_45_TO_54 (14):
                GRP age range from 45 to 54 years old.
            AGE_55_TO_64 (15):
                GRP age range from 55 to 64 years old.
            AGE_65_PLUS (16):
                GRP age range from 65 years old and up.
            AGE_UNKNOWN (17):
                When the age range is not available due to
                low impression levels, GRP privacy thresholds
                are activated and prevent us from specifying
                age.
        """

        FORECASTING_GRP_AGE_UNSPECIFIED = 0
        AGE_0_TO_17 = 1
        AGE_18_TO_24 = 2
        AGE_18_TO_49 = 3
        AGE_21_PLUS = 4
        AGE_21_TO_34 = 5
        AGE_21_TO_44 = 6
        AGE_21_TO_49 = 7
        AGE_21_TO_54 = 8
        AGE_21_TO_64 = 9
        AGE_25_TO_34 = 10
        AGE_25_TO_49 = 11
        AGE_35_TO_44 = 12
        AGE_35_TO_49 = 13
        AGE_45_TO_54 = 14
        AGE_55_TO_64 = 15
        AGE_65_PLUS = 16
        AGE_UNKNOWN = 17


__all__ = tuple(sorted(__protobuf__.manifest))
