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
        "ThirdPartyCompanyStatusEnum",
        "ThirdPartyCompanyTypeEnum",
    },
)


class ThirdPartyCompanyStatusEnum(proto.Message):
    r"""Wrapper message for
    [ThirdPartyCompanyStatus][google.ads.admanager.v1.ThirdPartyCompanyStatusEnum.ThirdPartyCompanyStatus]

    """

    class ThirdPartyCompanyStatus(proto.Enum):
        r"""Status of a third party company.

        Values:
            THIRD_PARTY_COMPANY_STATUS_UNSPECIFIED (0):
                No value specified
            ACTIVE (1):
                The third party company is active.
            INACTIVE (2):
                The third party company is inactive.
        """

        THIRD_PARTY_COMPANY_STATUS_UNSPECIFIED = 0
        ACTIVE = 1
        INACTIVE = 2


class ThirdPartyCompanyTypeEnum(proto.Message):
    r"""Wrapper message for
    [ThirdPartyCompanyType][google.ads.admanager.v1.ThirdPartyCompanyTypeEnum.ThirdPartyCompanyType]

    """

    class ThirdPartyCompanyType(proto.Enum):
        r"""The type of a third party company.

        Values:
            THIRD_PARTY_COMPANY_TYPE_UNSPECIFIED (0):
                No value specified
            AD_NETWORK (1):
                A company representing multiple advertisers
                and agencies.
            AD_SERVER (2):
                An organization that provides ad serving
                technology.
            VIDEO_TECHNOLOGY_PARTNER (3):
                A company that provides video technology.
        """

        THIRD_PARTY_COMPANY_TYPE_UNSPECIFIED = 0
        AD_NETWORK = 1
        AD_SERVER = 2
        VIDEO_TECHNOLOGY_PARTNER = 3


__all__ = tuple(sorted(__protobuf__.manifest))
