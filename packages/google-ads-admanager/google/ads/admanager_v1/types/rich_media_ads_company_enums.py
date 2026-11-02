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
        "RichMediaAdsCompanyGdprStatusEnum",
    },
)


class RichMediaAdsCompanyGdprStatusEnum(proto.Message):
    r"""Wrapper message for
    [RichMediaAdsCompanyGdprStatus][google.ads.admanager.v1.RichMediaAdsCompanyGdprStatusEnum.RichMediaAdsCompanyGdprStatus]

    """

    class RichMediaAdsCompanyGdprStatus(proto.Enum):
        r"""The status of a RichMediaAdsCompany for use in a
        GdprProtection.

        Values:
            RICH_MEDIA_ADS_COMPANY_GDPR_STATUS_UNSPECIFIED (0):
                Default value. This value is unused.
            COMPLIANCE_UNKNOWN (1):
                The company has not been contacted or
                responded about GDPR compliance, or otherwise
                the GDPR compliance is undetermined.
            COMPLIANT (2):
                The company has been determined as compliant
                for GDPR.
            COMPLIANT_AND_DEFAULT (3):
                The company has been determined as compliant,
                and is part of the default set of companies
                eligible as a vendor.
            COMPLIANT_LIGHTWEIGHT_VERIFIED (4):
                The company has been determined to be
                compliant through certification process.
            NOT_COMPLIANT (5):
                The company has been determined as
                non-compliant for GDPR.
        """

        RICH_MEDIA_ADS_COMPANY_GDPR_STATUS_UNSPECIFIED = 0
        COMPLIANCE_UNKNOWN = 1
        COMPLIANT = 2
        COMPLIANT_AND_DEFAULT = 3
        COMPLIANT_LIGHTWEIGHT_VERIFIED = 4
        NOT_COMPLIANT = 5


__all__ = tuple(sorted(__protobuf__.manifest))
