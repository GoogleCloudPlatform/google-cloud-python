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
        "AudienceSegmentTypeEnum",
        "AudienceSegmentStatusEnum",
        "AudienceSegmentLicenseTypeEnum",
        "AudienceSegmentApprovalStatusEnum",
    },
)


class AudienceSegmentTypeEnum(proto.Message):
    r"""Wraps the
    [AudienceSegmentType][google.ads.admanager.v1.AudienceSegmentTypeEnum.AudienceSegmentType]
    enum.

    """

    class AudienceSegmentType(proto.Enum):
        r"""Specifies the type of an AudienceSegment.

        Values:
            AUDIENCE_SEGMENT_TYPE_UNSPECIFIED (0):
                Default value. This value is unused.
            FIRST_PARTY (1):
                Indicates that the segment is a first party
                segment created and owned by the publisher.
            SHARED (2):
                Indicates that the segment is a first party
                segment shared by other clients.
            THIRD_PARTY (3):
                Indicates that the segment is a third party
                segment licensed by the publisher from data
                providers. This does not include Google-provided
                licensed segments.
        """

        AUDIENCE_SEGMENT_TYPE_UNSPECIFIED = 0
        FIRST_PARTY = 1
        SHARED = 2
        THIRD_PARTY = 3


class AudienceSegmentStatusEnum(proto.Message):
    r"""Wraps the
    [AudienceSegmentStatus][google.ads.admanager.v1.AudienceSegmentStatusEnum.AudienceSegmentStatus]
    enum.

    """

    class AudienceSegmentStatus(proto.Enum):
        r"""Specifies the status of an AudienceSegment.

        Values:
            AUDIENCE_SEGMENT_STATUS_UNSPECIFIED (0):
                Default value. This value is unused.
            ACTIVE (1):
                Indicates that this audience segment is
                available for targeting.
            INACTIVE (2):
                Indicates that this audience segment is not
                available for targeting.
            UNUSED (3):
                Indicates that this audience segment was
                deactivated by Google because it is unused.
        """

        AUDIENCE_SEGMENT_STATUS_UNSPECIFIED = 0
        ACTIVE = 1
        INACTIVE = 2
        UNUSED = 3


class AudienceSegmentLicenseTypeEnum(proto.Message):
    r"""Wraps the
    [AudienceSegmentLicenseType][google.ads.admanager.v1.AudienceSegmentLicenseTypeEnum.AudienceSegmentLicenseType]
    enum.

    """

    class AudienceSegmentLicenseType(proto.Enum):
        r"""Specifies the license type of a ThirdPartyAudienceSegment.

        Values:
            AUDIENCE_SEGMENT_LICENSE_TYPE_UNSPECIFIED (0):
                Default value. This value is unused.
            DIRECT (1):
                Indicates that the license is the result of a
                direct contract between the data provider and
                the publisher.
            GLOBAL (2):
                Indicates that the license is the result of
                an agreement between Google and the data
                provider, which agrees to license their audience
                segments to all the publishers and/or
                advertisers of the Google ecosystem.
        """

        AUDIENCE_SEGMENT_LICENSE_TYPE_UNSPECIFIED = 0
        DIRECT = 1
        GLOBAL = 2


class AudienceSegmentApprovalStatusEnum(proto.Message):
    r"""Wraps the
    [AudienceSegmentApprovalStatus][google.ads.admanager.v1.AudienceSegmentApprovalStatusEnum.AudienceSegmentApprovalStatus]
    enum.

    """

    class AudienceSegmentApprovalStatus(proto.Enum):
        r"""Specifies the approval status of a ThirdPartyAudienceSegment.

        Values:
            AUDIENCE_SEGMENT_APPROVAL_STATUS_UNSPECIFIED (0):
                Default value. This value is unused.
            APPROVED (1):
                Indicates that this segment is approved and
                can be targeted.
            REJECTED (2):
                Indicates that this segment is rejected and
                cannot be targeted.
            UNAPPROVED (3):
                Indicates that this segment is waiting to be
                approved or rejected. It cannot be targeted.
        """

        AUDIENCE_SEGMENT_APPROVAL_STATUS_UNSPECIFIED = 0
        APPROVED = 1
        REJECTED = 2
        UNAPPROVED = 3


__all__ = tuple(sorted(__protobuf__.manifest))
