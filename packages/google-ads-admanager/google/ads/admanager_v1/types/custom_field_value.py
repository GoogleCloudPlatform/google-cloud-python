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
        "CustomFieldValue",
    },
)


class CustomFieldValue(proto.Message):
    r"""A value for a CustomField on a resource.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        custom_field (str):
            Required. The custom field for which this is a value.
            Format:
            "networks/{network_code}/customFields/{custom_field_id}".
        value (google.ads.admanager_v1.types.CustomFieldValue.Value):
            Required. A typed value representation of the
            value.

            This field is a member of `oneof`_ ``_value``.
    """

    class Value(proto.Message):
        r"""Represent custom field value type.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            dropdown_value (int):
                The custom_field_option_id, if the
                [CustomFieldDataType][google.ads.admanager.v1.CustomFieldDataTypeEnum.CustomFieldDataType]
                is
                [DROPDOWN][CustomFieldDataTypeEnum.CustomFieldDataType.DROPDOWN].

                This field is a member of `oneof`_ ``value``.
            string_value (str):
                The value, if the
                [CustomFieldDataType][google.ads.admanager.v1.CustomFieldDataTypeEnum.CustomFieldDataType]
                is
                [STRING][google.ads.admanager.v1.CustomFieldDataTypeEnum.CustomFieldDataType.STRING].

                This field is a member of `oneof`_ ``value``.
            number_value (float):
                The value, if the
                [CustomFieldDataType][google.ads.admanager.v1.CustomFieldDataTypeEnum.CustomFieldDataType]
                is
                [NUMBER][google.ads.admanager.v1.CustomFieldDataTypeEnum.CustomFieldDataType.NUMBER].

                This field is a member of `oneof`_ ``value``.
            toggle_value (bool):
                The value, if the
                [CustomFieldDataType][google.ads.admanager.v1.CustomFieldDataTypeEnum.CustomFieldDataType]
                is
                [TOGGLE][google.ads.admanager.v1.CustomFieldDataTypeEnum.CustomFieldDataType.TOGGLE].

                This field is a member of `oneof`_ ``value``.
        """

        dropdown_value: int = proto.Field(
            proto.INT64,
            number=1,
            oneof="value",
        )
        string_value: str = proto.Field(
            proto.STRING,
            number=2,
            oneof="value",
        )
        number_value: float = proto.Field(
            proto.DOUBLE,
            number=3,
            oneof="value",
        )
        toggle_value: bool = proto.Field(
            proto.BOOL,
            number=4,
            oneof="value",
        )

    custom_field: str = proto.Field(
        proto.STRING,
        number=1,
    )
    value: Value = proto.Field(
        proto.MESSAGE,
        number=2,
        optional=True,
        message=Value,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
