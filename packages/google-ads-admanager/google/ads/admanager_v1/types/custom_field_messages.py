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

from google.ads.admanager_v1.types import custom_field_enums

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "CustomField",
        "CustomFieldOption",
    },
)


class CustomField(proto.Message):
    r"""An additional, user-created field on an entity.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the ``CustomField``.
            Format:
            ``networks/{network_code}/customFields/{custom_field}``
        custom_field_id (int):
            Output only. Deprecated: Unique ID of the
            CustomField.

            This field is a member of `oneof`_ ``_custom_field_id``.
        display_name (str):
            Required. Name of the CustomField. The max
            length is 127 characters.

            This field is a member of `oneof`_ ``_display_name``.
        description (str):
            Optional. A description of the custom field.
            The maximum length is 511 characters.

            This field is a member of `oneof`_ ``_description``.
        status (google.ads.admanager_v1.types.CustomFieldStatusEnum.CustomFieldStatus):
            Output only. The status of the ``CustomField``.

            This field is a member of `oneof`_ ``_status``.
        entity_type (google.ads.admanager_v1.types.CustomFieldEntityTypeEnum.CustomFieldEntityType):
            Required. The type of entity the ``CustomField`` can be
            applied to.

            This field is a member of `oneof`_ ``_entity_type``.
        data_type (google.ads.admanager_v1.types.CustomFieldDataTypeEnum.CustomFieldDataType):
            Required. The data type of the ``CustomField``.

            This field is a member of `oneof`_ ``_data_type``.
        visibility (google.ads.admanager_v1.types.CustomFieldVisibilityEnum.CustomFieldVisibility):
            Required. The visibility of the ``CustomField``.

            This field is a member of `oneof`_ ``_visibility``.
        options (MutableSequence[google.ads.admanager_v1.types.CustomFieldOption]):
            Optional. The drop-down options for the ``CustomField``.

            Only applicable for ``CustomField`` with the drop-down data
            type.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    custom_field_id: int = proto.Field(
        proto.INT64,
        number=2,
        optional=True,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    description: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )
    status: custom_field_enums.CustomFieldStatusEnum.CustomFieldStatus = proto.Field(
        proto.ENUM,
        number=5,
        optional=True,
        enum=custom_field_enums.CustomFieldStatusEnum.CustomFieldStatus,
    )
    entity_type: custom_field_enums.CustomFieldEntityTypeEnum.CustomFieldEntityType = (
        proto.Field(
            proto.ENUM,
            number=7,
            optional=True,
            enum=custom_field_enums.CustomFieldEntityTypeEnum.CustomFieldEntityType,
        )
    )
    data_type: custom_field_enums.CustomFieldDataTypeEnum.CustomFieldDataType = (
        proto.Field(
            proto.ENUM,
            number=8,
            optional=True,
            enum=custom_field_enums.CustomFieldDataTypeEnum.CustomFieldDataType,
        )
    )
    visibility: custom_field_enums.CustomFieldVisibilityEnum.CustomFieldVisibility = (
        proto.Field(
            proto.ENUM,
            number=9,
            optional=True,
            enum=custom_field_enums.CustomFieldVisibilityEnum.CustomFieldVisibility,
        )
    )
    options: MutableSequence["CustomFieldOption"] = proto.RepeatedField(
        proto.MESSAGE,
        number=10,
        message="CustomFieldOption",
    )


class CustomFieldOption(proto.Message):
    r"""An option for a drop-down ``CustomField``.

    Attributes:
        custom_field_option_id (int):
            Optional. Non-empty default. ``CustomFieldOption`` ID.
        display_name (str):
            Required. The display name of the ``CustomFieldOption``.

            This value has a maximum length of 127 characters.
    """

    custom_field_option_id: int = proto.Field(
        proto.INT64,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
