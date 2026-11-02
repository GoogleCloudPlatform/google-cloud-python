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
        "LineItemDeliveryForecastSourceEnum",
    },
)


class LineItemDeliveryForecastSourceEnum(proto.Message):
    r"""Wrapper message for
    [LineItemDeliveryForecastSource][google.ads.admanager.v1.LineItemDeliveryForecastSourceEnum.LineItemDeliveryForecastSource]

    """

    class LineItemDeliveryForecastSource(proto.Enum):
        r"""Strategies for choosing forecasted traffic shapes to pace
        line items.

        Values:
            LINE_ITEM_DELIVERY_FORECAST_SOURCE_UNSPECIFIED (0):
                Default value. This value is unused.
            CUSTOM_PACING_CURVE (1):
                A user specified custom pacing curve will be
                used to pace line item delivery.
            FORECASTING (2):
                The line item's projected future traffic will
                be used to pace line item delivery.
            HISTORICAL (3):
                The line item's historical traffic shape will
                be used to pace line item delivery.
        """

        LINE_ITEM_DELIVERY_FORECAST_SOURCE_UNSPECIFIED = 0
        CUSTOM_PACING_CURVE = 1
        FORECASTING = 2
        HISTORICAL = 3


__all__ = tuple(sorted(__protobuf__.manifest))
