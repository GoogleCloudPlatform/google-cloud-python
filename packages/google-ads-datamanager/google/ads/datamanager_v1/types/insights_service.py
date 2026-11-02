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

from google.ads.datamanager_v1.types import age_range as gad_age_range
from google.ads.datamanager_v1.types import gender as gad_gender

__protobuf__ = proto.module(
    package="google.ads.datamanager.v1",
    manifest={
        "RetrieveInsightsRequest",
        "Baseline",
        "RetrieveInsightsResponse",
    },
)


class RetrieveInsightsRequest(proto.Message):
    r"""Request message for DM API
    MarketingDataInsightsService.RetrieveInsights

    Attributes:
        parent (str):
            Required. The parent account that owns the user list.
            Format: ``accountTypes/{account_type}/accounts/{account}``
        baseline (google.ads.datamanager_v1.types.Baseline):
            Required. Baseline for the insights
            requested.
        user_list_id (str):
            Required. The user list ID for which insights
            are requested.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    baseline: "Baseline" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Baseline",
    )
    user_list_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class Baseline(proto.Message):
    r"""Baseline criteria against which insights are compared.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        baseline_location (google.ads.datamanager_v1.types.Baseline.Location):
            The baseline location of the request.
            Baseline location is an OR-list of the requested
            regions.

            This field is a member of `oneof`_ ``baseline``.
        location_auto_detection_enabled (bool):
            If set to true, the service will try to
            automatically detect the baseline location for
            insights.

            This field is a member of `oneof`_ ``baseline``.
    """

    class Location(proto.Message):
        r"""The baseline location of the request. Baseline location is on
        OR-list of ISO 3166-1 alpha-2 region codes of the requested
        regions.

        Attributes:
            region_codes (MutableSequence[str]):
                List of ISO 3166-1 alpha-2 region codes.
        """

        region_codes: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )

    baseline_location: Location = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="baseline",
        message=Location,
    )
    location_auto_detection_enabled: bool = proto.Field(
        proto.BOOL,
        number=2,
        oneof="baseline",
    )


class RetrieveInsightsResponse(proto.Message):
    r"""Response message for DM API
    MarketingDataInsightsService.RetrieveInsights

    Attributes:
        marketing_data_insights (MutableSequence[google.ads.datamanager_v1.types.RetrieveInsightsResponse.MarketingDataInsight]):
            Contains the insights for the marketing data.
    """

    class MarketingDataInsight(proto.Message):
        r"""Insights for marketing data.

        This feature is only available to data partners.

        Attributes:
            dimension (google.ads.datamanager_v1.types.RetrieveInsightsResponse.MarketingDataInsight.AudienceInsightsDimension):
                The dimension to which the insight belongs.
            attributes (MutableSequence[google.ads.datamanager_v1.types.RetrieveInsightsResponse.MarketingDataInsight.MarketingDataInsightsAttribute]):
                Insights for values of a given dimension.
        """

        class AudienceInsightsDimension(proto.Enum):
            r"""Possible dimensions for use in generating insights.

            Values:
                AUDIENCE_INSIGHTS_DIMENSION_UNSPECIFIED (0):
                    Not specified.
                AUDIENCE_INSIGHTS_DIMENSION_UNKNOWN (1):
                    The value is unknown in this version.
                AFFINITY_USER_INTEREST (2):
                    An Affinity UserInterest.
                IN_MARKET_USER_INTEREST (3):
                    An In-Market UserInterest.
                AGE_RANGE (4):
                    An age range.
                GENDER (5):
                    A gender.
            """

            AUDIENCE_INSIGHTS_DIMENSION_UNSPECIFIED = 0
            AUDIENCE_INSIGHTS_DIMENSION_UNKNOWN = 1
            AFFINITY_USER_INTEREST = 2
            IN_MARKET_USER_INTEREST = 3
            AGE_RANGE = 4
            GENDER = 5

        class MarketingDataInsightsAttribute(proto.Message):
            r"""Insights for a collection of related attributes of the same
            dimension.


            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                user_interest_id (int):
                    The user interest ID.

                    This field is a member of `oneof`_ ``_user_interest_id``.
                lift (float):
                    Measure of lift that the audience has for the attribute
                    value as compared to the baseline. Range [0-1].

                    This field is a member of `oneof`_ ``_lift``.
                age_range (google.ads.datamanager_v1.types.AgeRange):
                    Age range of the audience for which the lift
                    is provided.

                    This field is a member of `oneof`_ ``_age_range``.
                gender (google.ads.datamanager_v1.types.Gender):
                    Gender of the audience for which the lift is
                    provided.

                    This field is a member of `oneof`_ ``_gender``.
            """

            user_interest_id: int = proto.Field(
                proto.INT64,
                number=1,
                optional=True,
            )
            lift: float = proto.Field(
                proto.FLOAT,
                number=2,
                optional=True,
            )
            age_range: gad_age_range.AgeRange = proto.Field(
                proto.ENUM,
                number=3,
                optional=True,
                enum=gad_age_range.AgeRange,
            )
            gender: gad_gender.Gender = proto.Field(
                proto.ENUM,
                number=4,
                optional=True,
                enum=gad_gender.Gender,
            )

        dimension: "RetrieveInsightsResponse.MarketingDataInsight.AudienceInsightsDimension" = proto.Field(
            proto.ENUM,
            number=1,
            enum="RetrieveInsightsResponse.MarketingDataInsight.AudienceInsightsDimension",
        )
        attributes: MutableSequence[
            "RetrieveInsightsResponse.MarketingDataInsight.MarketingDataInsightsAttribute"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="RetrieveInsightsResponse.MarketingDataInsight.MarketingDataInsightsAttribute",
        )

    marketing_data_insights: MutableSequence[MarketingDataInsight] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=MarketingDataInsight,
        )
    )


__all__ = tuple(sorted(__protobuf__.manifest))
