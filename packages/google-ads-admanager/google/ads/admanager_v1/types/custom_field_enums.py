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
        "CustomFieldDataTypeEnum",
        "CustomFieldEntityTypeEnum",
        "CustomFieldStatusEnum",
        "CustomFieldVisibilityEnum",
    },
)


class CustomFieldDataTypeEnum(proto.Message):
    r"""Wrapper message for
    [CustomFieldDataType][google.ads.admanager.v1.CustomFieldDataTypeEnum.CustomFieldDataType]

    """

    class CustomFieldDataType(proto.Enum):
        r"""The data type for a CustomField.

        Values:
            CUSTOM_FIELD_DATA_TYPE_UNSPECIFIED (0):
                No value specified
            STRING (1):
                A string field

                The max length is 255 characters.
            NUMBER (2):
                A number field.
            TOGGLE (3):
                A "Yes" or "No" toggle field.
            DROP_DOWN (4):
                A drop-down field.
        """

        CUSTOM_FIELD_DATA_TYPE_UNSPECIFIED = 0
        STRING = 1
        NUMBER = 2
        TOGGLE = 3
        DROP_DOWN = 4


class CustomFieldEntityTypeEnum(proto.Message):
    r"""Wrapper message for
    [CustomFieldEntityType][google.ads.admanager.v1.CustomFieldEntityTypeEnum.CustomFieldEntityType]

    """

    class CustomFieldEntityType(proto.Enum):
        r"""The types of entities that a CustomField can be applied to.

        Values:
            CUSTOM_FIELD_ENTITY_TYPE_UNSPECIFIED (0):
                No value specified
            LINE_ITEM (1):
                The CustomField is applied to LineItems.
            ORDER (2):
                The CustomField is applied to Orders.
            CREATIVE (3):
                The CustomField is applied to Creatives.
            PROPOSAL (4):
                The CustomField is applied to Proposals.
            PROPOSAL_LINE_ITEM (5):
                The CustomField is applied to
                ProposalLineItems.
        """

        CUSTOM_FIELD_ENTITY_TYPE_UNSPECIFIED = 0
        LINE_ITEM = 1
        ORDER = 2
        CREATIVE = 3
        PROPOSAL = 4
        PROPOSAL_LINE_ITEM = 5


class CustomFieldStatusEnum(proto.Message):
    r"""Wrapper message for
    [CustomFieldStatus][google.ads.admanager.v1.CustomFieldStatusEnum.CustomFieldStatus]

    """

    class CustomFieldStatus(proto.Enum):
        r"""The status of the CustomField.

        Values:
            CUSTOM_FIELD_STATUS_UNSPECIFIED (0):
                No value specified
            ACTIVE (1):
                The CustomField is active.
            INACTIVE (2):
                The CustomField is inactive.
        """

        CUSTOM_FIELD_STATUS_UNSPECIFIED = 0
        ACTIVE = 1
        INACTIVE = 2


class CustomFieldVisibilityEnum(proto.Message):
    r"""Wrapper message for
    [CustomFieldVisibility][google.ads.admanager.v1.CustomFieldVisibilityEnum.CustomFieldVisibility]

    """

    class CustomFieldVisibility(proto.Enum):
        r"""The visibility level of a CustomField.

        Values:
            CUSTOM_FIELD_VISIBILITY_UNSPECIFIED (0):
                No value specified
            HIDDEN (1):
                The CustomField is not visible in the UI and
                only visible through the API.
            READ_ONLY (2):
                The CustomField is visible in the UI and only
                editable through the API.
            EDITABLE (3):
                The CustomField is visible and editable in
                both the API and UI.
        """

        CUSTOM_FIELD_VISIBILITY_UNSPECIFIED = 0
        HIDDEN = 1
        READ_ONLY = 2
        EDITABLE = 3


__all__ = tuple(sorted(__protobuf__.manifest))
