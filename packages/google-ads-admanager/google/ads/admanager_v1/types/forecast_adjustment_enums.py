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
        "ForecastAdjustmentVolumeTypeEnum",
        "ForecastAdjustmentStatusEnum",
    },
)


class ForecastAdjustmentVolumeTypeEnum(proto.Message):
    r"""Wrapper message for
    [ForecastAdjustmentVolumeType][google.ads.admanager.v1.ForecastAdjustmentVolumeTypeEnum.ForecastAdjustmentVolumeType]

    """

    class ForecastAdjustmentVolumeType(proto.Enum):
        r"""Options for how the volume settings of a ForecastAdjustment
        are defined.

        Values:
            FORECAST_ADJUSTMENT_VOLUME_TYPE_UNSPECIFIED (0):
                Default value. This value is unused.
            DAILY_VOLUME (1):
                Volume is defined by a series of daily ad
                opportunity counts.
            HISTORICAL_BASIS_VOLUME (2):
                Volume is defined by historical volume data.
            TOTAL_VOLUME (3):
                Volume is defined by a single total ad
                opportunity count.
        """

        FORECAST_ADJUSTMENT_VOLUME_TYPE_UNSPECIFIED = 0
        DAILY_VOLUME = 1
        HISTORICAL_BASIS_VOLUME = 2
        TOTAL_VOLUME = 3


class ForecastAdjustmentStatusEnum(proto.Message):
    r"""Wrapper message for
    [ForecastAdjustmentStatus][google.ads.admanager.v1.ForecastAdjustmentStatusEnum.ForecastAdjustmentStatus]

    """

    class ForecastAdjustmentStatus(proto.Enum):
        r"""The status of a forecast adjustment. Inactive adjustments are
        not applied during forecasting.

        Values:
            FORECAST_ADJUSTMENT_STATUS_UNSPECIFIED (0):
                Default value. This value is unused.
            ACTIVE (1):
                Indicates the current adjustment is active.
            INACTIVE (2):
                Indicates the current adjustment is inactive.
        """

        FORECAST_ADJUSTMENT_STATUS_UNSPECIFIED = 0
        ACTIVE = 1
        INACTIVE = 2


__all__ = tuple(sorted(__protobuf__.manifest))
