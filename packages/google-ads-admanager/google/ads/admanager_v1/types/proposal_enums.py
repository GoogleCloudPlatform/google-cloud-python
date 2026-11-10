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
        "BuyerRfpTypeEnum",
        "ProposalCompanyAssociationTypeEnum",
    },
)


class BuyerRfpTypeEnum(proto.Message):
    r"""Wrapper message for
    [BuyerRfpType][google.ads.admanager.v1.BuyerRfpTypeEnum.BuyerRfpType]

    """

    class BuyerRfpType(proto.Enum):
        r"""Decribes the type of BuyerRfp.

        Values:
            BUYER_RFP_TYPE_UNSPECIFIED (0):
                Default value. This value is unused.
            PREFERRED_DEAL (1):
                Indicates the BuyerRfp is a Preferred Deal
                RFP.
            PROGRAMMATIC_GUARANTEED (2):
                Indicates the BuyerRfp is a Programmatic
                Guaranteed RFP.
        """

        BUYER_RFP_TYPE_UNSPECIFIED = 0
        PREFERRED_DEAL = 1
        PROGRAMMATIC_GUARANTEED = 2


class ProposalCompanyAssociationTypeEnum(proto.Message):
    r"""Wrapper message for
    [ProposalCompanyAssociationType][google.ads.admanager.v1.ProposalCompanyAssociationTypeEnum.ProposalCompanyAssociationType]

    """

    class ProposalCompanyAssociationType(proto.Enum):
        r"""Describes the type of a Company associated with a Proposal.

        Values:
            PROPOSAL_COMPANY_ASSOCIATION_TYPE_UNSPECIFIED (0):
                Default value. This value is unused.
            BILLING_AGENCY (2):
                The company is a billing agency.
            BRANDING_AGENCY (3):
                The company is a branding agency.
            OTHER_AGENCY (4):
                The company is other type of agency.
            PRIMARY_AGENCY (5):
                The company is a primary agency.
        """

        PROPOSAL_COMPANY_ASSOCIATION_TYPE_UNSPECIFIED = 0
        BILLING_AGENCY = 2
        BRANDING_AGENCY = 3
        OTHER_AGENCY = 4
        PRIMARY_AGENCY = 5


__all__ = tuple(sorted(__protobuf__.manifest))
