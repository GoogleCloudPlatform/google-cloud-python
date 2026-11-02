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

from google.ads.admanager_v1.types import (
    brand_lift_partner_enum,
    reach_partner_enum,
    viewability_partner_enum,
)

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "ThirdPartyMeasurementSettings",
    },
)


class ThirdPartyMeasurementSettings(proto.Message):
    r"""Contains third party auto-pixeling settings for cross-sell
    Partners.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        viewability_partner (google.ads.admanager_v1.types.ViewabilityPartnerEnum.ViewabilityPartner):
            Optional. A field to determine the type of
            [ViewabilityPartner][google.ads.admanager.v1.ViewabilityPartnerEnum.ViewabilityPartner].
            This field default is
            [NONE][google.ads.admanager.v1.ViewabilityPartnerEnum.ViewabilityPartner.NONE].

            This field is a member of `oneof`_ ``_viewability_partner``.
        viewability_client_id (str):
            Optional. The third party partner ID for
            YouTube viewability verification.

            This field is a member of `oneof`_ ``_viewability_client_id``.
        viewability_reporting_id (str):
            Optional. The reporting ID that maps
            viewability partner data with a campaign (or a
            group of related campaigns) specific data.

            This field is a member of `oneof`_ ``_viewability_reporting_id``.
        publisher_viewability_partner (google.ads.admanager_v1.types.ViewabilityPartnerEnum.ViewabilityPartner):
            Optional. A field to determine the type of publisher's
            [ViewabilityPartner][google.ads.admanager.v1.ViewabilityPartnerEnum.ViewabilityPartner].
            This field default is
            [NONE][google.ads.admanager.v1.ViewabilityPartnerEnum.ViewabilityPartner.NONE].

            This field is a member of `oneof`_ ``_publisher_viewability_partner``.
        publisher_viewability_client_id (str):
            Optional. The third party partner ID for
            YouTube viewability verification for publisher.

            This field is a member of `oneof`_ ``_publisher_viewability_client_id``.
        publisher_viewability_reporting_id (str):
            Optional. The reporting ID that maps
            viewability partner data with a campaign (or a
            group of related campaigns) specific data for
            publisher.

            This field is a member of `oneof`_ ``_publisher_viewability_reporting_id``.
        brand_lift_partner (google.ads.admanager_v1.types.BrandLiftPartnerEnum.BrandLiftPartner):
            Optional. A field to determine the type of
            [BrandLiftPartner][google.ads.admanager.v1.BrandLiftPartnerEnum.BrandLiftPartner].
            This field default is
            [NONE][google.ads.admanager.v1.BrandLiftPartnerEnum.BrandLiftPartner.NONE].

            This field is a member of `oneof`_ ``_brand_lift_partner``.
        brand_lift_client_id (str):
            Optional. The third party partner ID for
            YouTube brand lift verification.

            This field is a member of `oneof`_ ``_brand_lift_client_id``.
        brand_lift_reporting_id (str):
            Optional. The reporting ID that maps brand
            lift partner data with a campaign (or a group of
            related campaigns) specific data.

            This field is a member of `oneof`_ ``_brand_lift_reporting_id``.
        reach_partner (google.ads.admanager_v1.types.ReachPartnerEnum.ReachPartner):
            Optional. A field to determine the type of advertiser's
            [ReachPartner][google.ads.admanager.v1.ReachPartnerEnum.ReachPartner].
            This field default is
            [UNKNOWN][ReachPartnerEnum.ReachPartner.UNKNOWN].

            This field is a member of `oneof`_ ``_reach_partner``.
        reach_client_id (str):
            Optional. The third party partner ID for
            YouTube reach verification for advertiser.

            This field is a member of `oneof`_ ``_reach_client_id``.
        reach_reporting_id (str):
            Optional. The reporting ID that maps reach
            partner data with a campaign (or a group of
            related campaigns) specific data for advertiser.

            This field is a member of `oneof`_ ``_reach_reporting_id``.
        publisher_reach_partner (google.ads.admanager_v1.types.ReachPartnerEnum.ReachPartner):
            Optional. A field to determine the type of publisher's
            [ReachPartner][google.ads.admanager.v1.ReachPartnerEnum.ReachPartner].
            This field default is
            [UNKNOWN][ReachPartnerEnum.ReachPartner.UNKNOWN].

            This field is a member of `oneof`_ ``_publisher_reach_partner``.
        publisher_reach_client_id (str):
            Optional. The third party partner ID for
            YouTube reach verification for publisher.

            This field is a member of `oneof`_ ``_publisher_reach_client_id``.
        publisher_reach_reporting_id (str):
            Optional. The reporting ID that maps reach
            partner data with a campaign (or a group of
            related campaigns) specific data for publisher.

            This field is a member of `oneof`_ ``_publisher_reach_reporting_id``.
    """

    viewability_partner: viewability_partner_enum.ViewabilityPartnerEnum.ViewabilityPartner = proto.Field(
        proto.ENUM,
        number=1,
        optional=True,
        enum=viewability_partner_enum.ViewabilityPartnerEnum.ViewabilityPartner,
    )
    viewability_client_id: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    viewability_reporting_id: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    publisher_viewability_partner: viewability_partner_enum.ViewabilityPartnerEnum.ViewabilityPartner = proto.Field(
        proto.ENUM,
        number=4,
        optional=True,
        enum=viewability_partner_enum.ViewabilityPartnerEnum.ViewabilityPartner,
    )
    publisher_viewability_client_id: str = proto.Field(
        proto.STRING,
        number=5,
        optional=True,
    )
    publisher_viewability_reporting_id: str = proto.Field(
        proto.STRING,
        number=6,
        optional=True,
    )
    brand_lift_partner: brand_lift_partner_enum.BrandLiftPartnerEnum.BrandLiftPartner = proto.Field(
        proto.ENUM,
        number=10,
        optional=True,
        enum=brand_lift_partner_enum.BrandLiftPartnerEnum.BrandLiftPartner,
    )
    brand_lift_client_id: str = proto.Field(
        proto.STRING,
        number=11,
        optional=True,
    )
    brand_lift_reporting_id: str = proto.Field(
        proto.STRING,
        number=12,
        optional=True,
    )
    reach_partner: reach_partner_enum.ReachPartnerEnum.ReachPartner = proto.Field(
        proto.ENUM,
        number=13,
        optional=True,
        enum=reach_partner_enum.ReachPartnerEnum.ReachPartner,
    )
    reach_client_id: str = proto.Field(
        proto.STRING,
        number=14,
        optional=True,
    )
    reach_reporting_id: str = proto.Field(
        proto.STRING,
        number=15,
        optional=True,
    )
    publisher_reach_partner: reach_partner_enum.ReachPartnerEnum.ReachPartner = (
        proto.Field(
            proto.ENUM,
            number=16,
            optional=True,
            enum=reach_partner_enum.ReachPartnerEnum.ReachPartner,
        )
    )
    publisher_reach_client_id: str = proto.Field(
        proto.STRING,
        number=17,
        optional=True,
    )
    publisher_reach_reporting_id: str = proto.Field(
        proto.STRING,
        number=18,
        optional=True,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
