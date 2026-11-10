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

import google.type.money_pb2 as money_pb2  # type: ignore
import proto  # type: ignore

from google.ads.admanager_v1.types import targeting as gaa_targeting
from google.ads.admanager_v1.types import yield_enums

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "YieldGroup",
        "YieldAdSource",
    },
)


class YieldGroup(proto.Message):
    r"""Represents a segment of inventory and a set of yield partners
    that can monetize that inventory.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the ``YieldGroup``. Format:
            ``networks/{network_code}/yieldGroups/{yield_group_id}``
        display_name (str):
            Required. The display name of the ``YieldGroup``. This value
            has a maximum length of 255 characters.

            This field is a member of `oneof`_ ``_display_name``.
        status (google.ads.admanager_v1.types.YieldEntityStatusEnum.YieldEntityStatus):
            Output only. Status of the ``YieldGroup``.

            This field is a member of `oneof`_ ``_status``.
        targeting (google.ads.admanager_v1.types.Targeting):
            Optional. The targeting of the ``YieldGroup``.

            This field is a member of `oneof`_ ``_targeting``.
        ad_sources (MutableSequence[google.ads.admanager_v1.types.YieldAdSource]):
            Optional. The ad sources that belong to the ``YieldGroup``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    status: yield_enums.YieldEntityStatusEnum.YieldEntityStatus = proto.Field(
        proto.ENUM,
        number=3,
        optional=True,
        enum=yield_enums.YieldEntityStatusEnum.YieldEntityStatus,
    )
    targeting: gaa_targeting.Targeting = proto.Field(
        proto.MESSAGE,
        number=6,
        optional=True,
        message=gaa_targeting.Targeting,
    )
    ad_sources: MutableSequence["YieldAdSource"] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message="YieldAdSource",
    )


class YieldAdSource(proto.Message):
    r"""Represents an opportunity for a third party network to be mediated
    on a segment of inventory described in a ``YieldGroup``.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        open_bidding_settings (google.ads.admanager_v1.types.YieldAdSource.OpenBiddingSettings):
            Settings for Open Bidding.

            This field is a member of `oneof`_ ``display_settings``.
        sdk_mediation_settings (google.ads.admanager_v1.types.YieldAdSource.SdkMediationSettings):
            Settings for mobile app display.

            This field is a member of `oneof`_ ``display_settings``.
        ad_source_id (int):
            Optional. Non-empty default. The ID of the ad
            source. This field is assigned by Google when
            the ad source is created. Provide this ID when
            updating an existing ad source; omit it when
            adding a new ad source.

            This field is a member of `oneof`_ ``_ad_source_id``.
        company (str):
            Required. Immutable. The resource name of the ``Company``.
            Format: ``networks/{network_code}/companies/{company_id}``

            This field is a member of `oneof`_ ``_company``.
        status (google.ads.admanager_v1.types.YieldEntityStatusEnum.YieldEntityStatus):
            Optional. User-assigned status of the ad
            source.

            This field is a member of `oneof`_ ``_status``.
        manual_cpm (google.type.money_pb2.Money):
            Optional. CPM manually assigned to this
            source.

            This field is a member of `oneof`_ ``_manual_cpm``.
        override_dynamic_cpm (bool):
            Optional. If true, then the automatically collected CPM is
            ignored in favor of ``manualCpm``.

            This field is a member of `oneof`_ ``_override_dynamic_cpm``.
    """

    class OpenBiddingSettings(proto.Message):
        r"""Configuration for Open Bidding in a ``YieldAdSource``.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            integration_type (google.ads.admanager_v1.types.YieldIntegrationTypeEnum.YieldIntegrationType):
                Required. The integration type of the yield
                partner.

                This field is a member of `oneof`_ ``_integration_type``.
        """

        integration_type: yield_enums.YieldIntegrationTypeEnum.YieldIntegrationType = (
            proto.Field(
                proto.ENUM,
                number=1,
                optional=True,
                enum=yield_enums.YieldIntegrationTypeEnum.YieldIntegrationType,
            )
        )

    class SdkMediationSettings(proto.Message):
        r"""Display settings for mobile SDK adapters.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            integration_type (google.ads.admanager_v1.types.YieldIntegrationTypeEnum.YieldIntegrationType):
                Required. The integration type of the yield
                partner.

                This field is a member of `oneof`_ ``_integration_type``.
            parameters (MutableMapping[str, str]):
                Optional. The parameters for the mobile SDK
                adapter.
            platform (google.ads.admanager_v1.types.YieldPlatformEnum.YieldPlatform):
                Required. The platform of the adapter.

                This field is a member of `oneof`_ ``_platform``.
        """

        integration_type: yield_enums.YieldIntegrationTypeEnum.YieldIntegrationType = (
            proto.Field(
                proto.ENUM,
                number=1,
                optional=True,
                enum=yield_enums.YieldIntegrationTypeEnum.YieldIntegrationType,
            )
        )
        parameters: MutableMapping[str, str] = proto.MapField(
            proto.STRING,
            proto.STRING,
            number=2,
        )
        platform: yield_enums.YieldPlatformEnum.YieldPlatform = proto.Field(
            proto.ENUM,
            number=3,
            optional=True,
            enum=yield_enums.YieldPlatformEnum.YieldPlatform,
        )

    open_bidding_settings: OpenBiddingSettings = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="display_settings",
        message=OpenBiddingSettings,
    )
    sdk_mediation_settings: SdkMediationSettings = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="display_settings",
        message=SdkMediationSettings,
    )
    ad_source_id: int = proto.Field(
        proto.INT64,
        number=1,
        optional=True,
    )
    company: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    status: yield_enums.YieldEntityStatusEnum.YieldEntityStatus = proto.Field(
        proto.ENUM,
        number=3,
        optional=True,
        enum=yield_enums.YieldEntityStatusEnum.YieldEntityStatus,
    )
    manual_cpm: money_pb2.Money = proto.Field(
        proto.MESSAGE,
        number=4,
        optional=True,
        message=money_pb2.Money,
    )
    override_dynamic_cpm: bool = proto.Field(
        proto.BOOL,
        number=5,
        optional=True,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
