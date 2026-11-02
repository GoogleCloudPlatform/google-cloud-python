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

from google.ads.admanager_v1.types import third_party_company_enums

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "ThirdPartyCompany",
    },
)


class ThirdPartyCompany(proto.Message):
    r"""Represents a third-party company recognized by Google Ad
    Manager, which can be an ad network, ad server, or video
    technology partner.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the ``ThirdPartyCompany``.
            Format:
            ``networks/{network_code}/thirdPartyCompanies/{third_party_company_id}``
        display_name (str):
            Output only. The display name of the
            ThirdPartyCompany. This field must be unique
            among all ThirdPartyCompanies for this network.

            This field is a member of `oneof`_ ``_display_name``.
        status (google.ads.admanager_v1.types.ThirdPartyCompanyStatusEnum.ThirdPartyCompanyStatus):
            Output only. The status of the
            ThirdPartyCompany. ThirdPartyCompanies are set
            to inactive rather than deleting them.

            This field is a member of `oneof`_ ``_status``.
        type_ (google.ads.admanager_v1.types.ThirdPartyCompanyTypeEnum.ThirdPartyCompanyType):
            Output only. The type of the
            ThirdPartyCompany.

            This field is a member of `oneof`_ ``_type``.
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
    status: third_party_company_enums.ThirdPartyCompanyStatusEnum.ThirdPartyCompanyStatus = proto.Field(
        proto.ENUM,
        number=3,
        optional=True,
        enum=third_party_company_enums.ThirdPartyCompanyStatusEnum.ThirdPartyCompanyStatus,
    )
    type_: third_party_company_enums.ThirdPartyCompanyTypeEnum.ThirdPartyCompanyType = proto.Field(
        proto.ENUM,
        number=4,
        optional=True,
        enum=third_party_company_enums.ThirdPartyCompanyTypeEnum.ThirdPartyCompanyType,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
