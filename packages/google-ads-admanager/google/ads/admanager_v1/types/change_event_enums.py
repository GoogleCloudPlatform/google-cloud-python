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
        "OperationTypeEnum",
        "ChangeEventResourceTypeEnum",
    },
)


class OperationTypeEnum(proto.Message):
    r"""Wrapper message for
    [OperationTypeEnum.OperationType][google.ads.admanager.v1.OperationTypeEnum.OperationType]

    """

    class OperationType(proto.Enum):
        r"""The kind of operation associated with the ChangeEvent.

        Values:
            OPERATION_TYPE_UNSPECIFIED (0):
                No value specified
            CREATE (1):
                The resource was created.
            UPDATE (2):
                The resource was updated.
            DELETE (3):
                The resource was deleted.
        """

        OPERATION_TYPE_UNSPECIFIED = 0
        CREATE = 1
        UPDATE = 2
        DELETE = 3


class ChangeEventResourceTypeEnum(proto.Message):
    r"""Wrapper message for
    [ChangeEventResourceTypeEnum.ChangeEventResourceType][google.ads.admanager.v1.ChangeEventResourceTypeEnum.ChangeEventResourceType]

    """

    class ChangeEventResourceType(proto.Enum):
        r"""The type of resource a change occurred on.

        Values:
            CHANGE_EVENT_RESOURCE_TYPE_UNSPECIFIED (0):
                No value specified
            BASE_RATE (8):
                The Base Rate entity type
            COMPANY (10):
                The Company entity type, which might be either a
                ``Company``, ``ChildPublisher``, ``Partner``, or
                ``ViewabilityProvider`` resource.
            CONTACT (11):
                The Contact entity type
            CREATIVE (15):
                The Creative entity type
            CREATIVE_SET (16):
                The Creative Set entity type
            CUSTOM_FIELD (19):
                The Custom Field entity type
            CUSTOM_KEY (20):
                The Custom Key entity type
            CUSTOM_VALUE (21):
                The Custom Value entity type
            PLACEMENT (35):
                The Placement entity type
            AD_UNIT (36):
                The Ad Unit entity type
            LABEL (37):
                The Label entity type
            LINE_ITEM (38):
                The Line Item entity type
            NETWORK (44):
                The Network entity type
            ORDER (45):
                The Order entity type
            PROPOSAL (56):
                The Proposal entity type
            PROPOSAL_LINK (57):
                The Proposal Link entity type
            PROPOSAL_LINE_ITEM (58):
                The Proposal Line Item entity type
            PACKAGE (59):
                The Package entity type
            ROLE (66):
                The Role entity type
            TEAM (69):
                The Team entity type
            USER (72):
                The User entity type
        """

        CHANGE_EVENT_RESOURCE_TYPE_UNSPECIFIED = 0
        BASE_RATE = 8
        COMPANY = 10
        CONTACT = 11
        CREATIVE = 15
        CREATIVE_SET = 16
        CUSTOM_FIELD = 19
        CUSTOM_KEY = 20
        CUSTOM_VALUE = 21
        PLACEMENT = 35
        AD_UNIT = 36
        LABEL = 37
        LINE_ITEM = 38
        NETWORK = 44
        ORDER = 45
        PROPOSAL = 56
        PROPOSAL_LINK = 57
        PROPOSAL_LINE_ITEM = 58
        PACKAGE = 59
        ROLE = 66
        TEAM = 69
        USER = 72


__all__ = tuple(sorted(__protobuf__.manifest))
