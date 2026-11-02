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
    package="google.ads.datamanager.v1",
    manifest={
        "UserListLicenseMetrics",
    },
)


class UserListLicenseMetrics(proto.Message):
    r"""Metrics related to a user list license.

    Attributes:
        click_count (int):
            Output only. The number of clicks for the
            user list license.
        impression_count (int):
            Output only. The number of impressions for
            the user list license.
        revenue_usd_micros (int):
            Output only. The revenue for the user list
            license in USD micros.
        start_date (int):
            Output only. The start date (inclusive) of the metrics in
            the format YYYYMMDD. For example, 20260102 represents
            January 2, 2026. If ``end_date`` is used in the filter,
            ``start_date`` is also required. If neither ``start_date``
            nor ``end_date`` are included in the filter, the
            UserListLicenseMetrics fields will not be populated in the
            response.
        end_date (int):
            Output only. The end date (inclusive) of the metrics in the
            format YYYYMMDD. For example, 20260102 represents January 2,
            2026. If ``start_date`` is used in the filter, ``end_date``
            is also required. If neither ``start_date`` nor ``end_date``
            are included in the filter, the UserListLicenseMetrics
            fields will not be populated in the response.
    """

    click_count: int = proto.Field(
        proto.INT64,
        number=1,
    )
    impression_count: int = proto.Field(
        proto.INT64,
        number=2,
    )
    revenue_usd_micros: int = proto.Field(
        proto.INT64,
        number=3,
    )
    start_date: int = proto.Field(
        proto.INT64,
        number=4,
    )
    end_date: int = proto.Field(
        proto.INT64,
        number=5,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
