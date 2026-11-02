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
        "SiteDisapprovalReasonEnum",
        "SiteApprovalStatusEnum",
    },
)


class SiteDisapprovalReasonEnum(proto.Message):
    r"""Wrapper message for
    [SiteDisapprovalReason][google.ads.admanager.v1.SiteDisapprovalReasonEnum.SiteDisapprovalReason]

    """

    class SiteDisapprovalReason(proto.Enum):
        r"""The list of possible policy violation types for a Site.

        Values:
            SITE_DISAPPROVAL_REASON_UNSPECIFIED (0):
                Default value. This value is unused.
            CONTENT (1):
                The site has content that violates policy.
            OTHER (2):
                Generic error type.
            OWNERSHIP (3):
                The parent must be an authorized seller of
                the child network's inventory.
        """

        SITE_DISAPPROVAL_REASON_UNSPECIFIED = 0
        CONTENT = 1
        OTHER = 2
        OWNERSHIP = 3


class SiteApprovalStatusEnum(proto.Message):
    r"""Wrapper message for
    [SiteApprovalStatus][google.ads.admanager.v1.SiteApprovalStatusEnum.SiteApprovalStatus]

    """

    class SiteApprovalStatus(proto.Enum):
        r"""Represents the approval status of a site.

        Values:
            SITE_APPROVAL_STATUS_UNSPECIFIED (0):
                Default value. This value is unused.
            APPROVED (1):
                The site has been approved to serve ads.
            DISAPPROVED (2):
                The site has been disapproved from serving
                ads.
            DRAFT (3):
                The default status with which a site is
                created.
            REQUIRES_REVIEW (4):
                The site has been deactivated and is not
                serving ads due to dormancy. It must be
                resubmitted for approval.
            UNCHECKED (5):
                Once the site is submitted for approval, its
                status changes from draft to unchecked. It will
                be reviwed with an estimated turn-around time of
                24h. Such a site cannot serve ads.
        """

        SITE_APPROVAL_STATUS_UNSPECIFIED = 0
        APPROVED = 1
        DISAPPROVED = 2
        DRAFT = 3
        REQUIRES_REVIEW = 4
        UNCHECKED = 5


__all__ = tuple(sorted(__protobuf__.manifest))
