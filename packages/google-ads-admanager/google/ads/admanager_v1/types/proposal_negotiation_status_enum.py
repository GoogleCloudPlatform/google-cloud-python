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
        "ProposalNegotiationStatusEnum",
    },
)


class ProposalNegotiationStatusEnum(proto.Message):
    r"""Wrapper message for
    [ProposalNegotiationStatus][google.ads.admanager.v1.ProposalNegotiationStatusEnum.ProposalNegotiationStatus]

    """

    class ProposalNegotiationStatus(proto.Enum):
        r"""Represents the Proposal's negotiation status for Marketplace.

        Values:
            PROPOSAL_NEGOTIATION_STATUS_UNSPECIFIED (0):
                Default value. This value is unused.
            AWAITING_BUYER_REVIEW (1):
                Indicates that a Proposal has been updated by
                the seller and is awaiting buyer approval.
            AWAITING_SELLER_REVIEW (2):
                Indicates that a Proposal has been updated by
                the buyer and is awaiting seller approval.
            BUYER_INITIATED (3):
                Indicates that a new Proposal has been
                created by the buyer and is awaiting seller
                action.
            CANCELLED (4):
                Indicates that negotiations for the Proposal
                have been cancelled.
            FINALIZED (5):
                Indicates that the Proposal has been accepted
                by both the buyer and the seller.
            SELLER_ACCEPTANCE_REQUESTED (6):
                Indicates that the buyer has accepted the
                Proposal and is awaiting the seller's
                acceptance.
            BUYER_ACCEPTANCE_REQUESTED (7):
                Indicates that the seller has accepted the
                Proposal and is awaiting the buyer's acceptance.
            SELLER_INITIATED (8):
                Indicates that a new Proposal has been
                created by the seller and has not been sent to
                Marketplace yet.
        """

        PROPOSAL_NEGOTIATION_STATUS_UNSPECIFIED = 0
        AWAITING_BUYER_REVIEW = 1
        AWAITING_SELLER_REVIEW = 2
        BUYER_INITIATED = 3
        CANCELLED = 4
        FINALIZED = 5
        SELLER_ACCEPTANCE_REQUESTED = 6
        BUYER_ACCEPTANCE_REQUESTED = 7
        SELLER_INITIATED = 8


__all__ = tuple(sorted(__protobuf__.manifest))
