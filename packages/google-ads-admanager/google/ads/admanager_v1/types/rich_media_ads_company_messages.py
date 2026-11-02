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

from google.ads.admanager_v1.types import rich_media_ads_company_enums

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "RichMediaAdsCompany",
    },
)


class RichMediaAdsCompany(proto.Message):
    r"""Represents a Rich Media Ads Company, typically used for
    vendor compliance.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the
            ``RichMediaAdsCompany``. Format:
            ``networks/{network_code}/richMediaAdsCompanies/{rich_media_ads_company_id}``
        display_name (str):
            Output only. The name of the Rich Media Ads
            Company.

            This field is a member of `oneof`_ ``_display_name``.
        policy_url (str):
            Output only. The policy URL of the Rich Media
            Ads Company.

            This field is a member of `oneof`_ ``_policy_url``.
        gdpr_status (google.ads.admanager_v1.types.RichMediaAdsCompanyGdprStatusEnum.RichMediaAdsCompanyGdprStatus):
            Output only. The GDPR status of the Rich
            Media Ads Company.

            This field is a member of `oneof`_ ``_gdpr_status``.
        company_gvl_id (int):
            Output only. The GVL ID of the Rich Media Ads
            Company.

            This field is a member of `oneof`_ ``_company_gvl_id``.
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
    policy_url: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    gdpr_status: rich_media_ads_company_enums.RichMediaAdsCompanyGdprStatusEnum.RichMediaAdsCompanyGdprStatus = proto.Field(
        proto.ENUM,
        number=4,
        optional=True,
        enum=rich_media_ads_company_enums.RichMediaAdsCompanyGdprStatusEnum.RichMediaAdsCompanyGdprStatus,
    )
    company_gvl_id: int = proto.Field(
        proto.INT64,
        number=6,
        optional=True,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
