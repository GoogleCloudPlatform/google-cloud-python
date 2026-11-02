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
        "ContactStatusEnum",
    },
)


class ContactStatusEnum(proto.Message):
    r"""Wrapper message for
    [ContactStatus][google.ads.admanager.v1.ContactStatusEnum.ContactStatus]

    """

    class ContactStatus(proto.Enum):
        r"""Describes the contact statuses.

        Values:
            CONTACT_STATUS_UNSPECIFIED (0):
                Default value. This value is unused.
            INVITE_CANCELED (1):
                The contact was invited to see their orders,
                but the invitation was cancelled.
            INVITE_EXPIRED (2):
                The contact has been invited to see their
                orders, but the invitation has already expired.
            INVITE_PENDING (3):
                The contact has been invited to see their
                orders, but has not yet accepted the invitation.
            UNINVITED (4):
                The contact has not been invited to see their
                orders.
            USER_ACTIVE (5):
                The contact has access to login and view
                their orders.
            USER_DISABLED (6):
                The contact accepted an invitation to see
                their orders, but their access was later
                revoked.
        """

        CONTACT_STATUS_UNSPECIFIED = 0
        INVITE_CANCELED = 1
        INVITE_EXPIRED = 2
        INVITE_PENDING = 3
        UNINVITED = 4
        USER_ACTIVE = 5
        USER_DISABLED = 6


__all__ = tuple(sorted(__protobuf__.manifest))
