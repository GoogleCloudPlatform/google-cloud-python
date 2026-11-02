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
        "CompanyTypeEnum",
        "CompanyCreditStatusEnum",
    },
)


class CompanyTypeEnum(proto.Message):
    r"""Wrapper message for
    [CompanyType][google.ads.admanager.v1.CompanyTypeEnum.CompanyType]

    """

    class CompanyType(proto.Enum):
        r"""The type of a company.

        Values:
            COMPANY_TYPE_UNSPECIFIED (0):
                No value specified
            ADVERTISER (1):
                A business entity that purchases ad
                inventory.
            HOUSE_ADVERTISER (2):
                A company representing the publisher's own
                advertiser for house ads.
            AGENCY (3):
                An organization that manages ad accounts and
                offers services, such as ad creation, placement,
                and management to advertisers.
            HOUSE_AGENCY (4):
                A company representing the publisher's own
                agency.
            AD_NETWORK (5):
                A company representing multiple advertisers
                and agencies.
        """

        COMPANY_TYPE_UNSPECIFIED = 0
        ADVERTISER = 1
        HOUSE_ADVERTISER = 2
        AGENCY = 3
        HOUSE_AGENCY = 4
        AD_NETWORK = 5


class CompanyCreditStatusEnum(proto.Message):
    r"""Wrapper message for
    [CompanyCreditStatus][google.ads.admanager.v1.CompanyCreditStatusEnum.CompanyCreditStatus]

    """

    class CompanyCreditStatus(proto.Enum):
        r"""The credit status of a company.

        Credit statuses specify the credit-worthiness of a company and
        affect the ad serving of campaigns belonging to the company.

        In basic settings, only the
        [ACTIVE][google.ads.admanager.v1.CompanyCreditStatusEnum.CompanyCreditStatus.ACTIVE]
        and
        [INACTIVE][google.ads.admanager.v1.CompanyCreditStatusEnum.CompanyCreditStatus.INACTIVE]
        credit statuses are applicable. In advance settings, all credit
        statuses are applicable.

        Values:
            COMPANY_CREDIT_STATUS_UNSPECIFIED (0):
                No value specified
            ACTIVE (1):
                The company's credit status is active.

                Line items belonging to the company can serve.

                This credit status is the default for basic
                settings and is available in both basic and
                advance settings.
            INACTIVE (2):
                The company's credit status is inactive.

                Line items belonging to the company cannot be
                activated. However, line items that were
                activated before the credit status changed will
                remain active. New orders or line items
                belonging to the company cannot be created.

                Companies with this credit status will be hidden
                by default in company search results.

                This credit status is available in both basic
                and advance settings.
            ON_HOLD (3):
                The company's credit status is on hold.

                Line items belonging to the company cannot be
                activated. However, line items that were
                activated before the credit status changed will
                remain active. New orders or line items
                belonging to the company can be created.

                This credit status is the default in advance
                settings and is only available in advance
                settings.
            STOP (4):
                The company's credit status is stopped.

                Line items belonging to the company cannot be
                activated. However, line items that were
                activated before the credit status changed will
                remain active. New orders or line items
                belonging to the company cannot be created.

                This credit status is only available in advance
                settings.
            BLOCKED (5):
                The company's credit status is blocked.

                All active line items belonging to the company
                will stop serving with immediate effect. Line
                items belonging to the company cannot be
                activated, and new orders or line items
                belonging to the company cannot be created.

                This credit status is only available in advance
                settings.
        """

        COMPANY_CREDIT_STATUS_UNSPECIFIED = 0
        ACTIVE = 1
        INACTIVE = 2
        ON_HOLD = 3
        STOP = 4
        BLOCKED = 5


__all__ = tuple(sorted(__protobuf__.manifest))
