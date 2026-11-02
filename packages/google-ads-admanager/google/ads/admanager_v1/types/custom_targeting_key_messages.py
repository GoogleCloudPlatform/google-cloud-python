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

from google.ads.admanager_v1.types import custom_targeting_key_enums

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "CustomTargetingKey",
    },
)


class CustomTargetingKey(proto.Message):
    r"""The ``CustomTargetingKey`` resource.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the ``CustomTargetingKey``.
            Format:
            ``networks/{network_code}/customTargetingKeys/{custom_targeting_key_id}``
        custom_targeting_key_id (int):
            Output only. Deprecated: ``CustomTargetingKey`` ID.

            This field is a member of `oneof`_ ``_custom_targeting_key_id``.
        ad_tag_name (str):
            Immutable. Name of the key. Keys can contain up to 10
            characters each. You can use alphanumeric characters and
            symbols other than the following: ", ', =, !, +, #, \*, ~,
            ;, ^, (, ), <, >, [, ], the white space character.

            This field is a member of `oneof`_ ``_ad_tag_name``.
        display_name (str):
            Optional. Descriptive name for the ``CustomTargetingKey``.

            This field is a member of `oneof`_ ``_display_name``.
        type_ (google.ads.admanager_v1.types.CustomTargetingKeyTypeEnum.CustomTargetingKeyType):
            Required. Indicates whether users will select
            from predefined values or create new targeting
            values, while specifying targeting criteria for
            a line item.

            This field is a member of `oneof`_ ``_type``.
        status (google.ads.admanager_v1.types.CustomTargetingKeyStatusEnum.CustomTargetingKeyStatus):
            Output only. Status of the ``CustomTargetingKey``.

            This field is a member of `oneof`_ ``_status``.
        reportable_type (google.ads.admanager_v1.types.CustomTargetingKeyReportableTypeEnum.CustomTargetingKeyReportableType):
            Required. Reportable state of the ``CustomTargetingKey``.

            This field is a member of `oneof`_ ``_reportable_type``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    custom_targeting_key_id: int = proto.Field(
        proto.INT64,
        number=2,
        optional=True,
    )
    ad_tag_name: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )
    type_: custom_targeting_key_enums.CustomTargetingKeyTypeEnum.CustomTargetingKeyType = proto.Field(
        proto.ENUM,
        number=5,
        optional=True,
        enum=custom_targeting_key_enums.CustomTargetingKeyTypeEnum.CustomTargetingKeyType,
    )
    status: custom_targeting_key_enums.CustomTargetingKeyStatusEnum.CustomTargetingKeyStatus = proto.Field(
        proto.ENUM,
        number=6,
        optional=True,
        enum=custom_targeting_key_enums.CustomTargetingKeyStatusEnum.CustomTargetingKeyStatus,
    )
    reportable_type: custom_targeting_key_enums.CustomTargetingKeyReportableTypeEnum.CustomTargetingKeyReportableType = proto.Field(
        proto.ENUM,
        number=7,
        optional=True,
        enum=custom_targeting_key_enums.CustomTargetingKeyReportableTypeEnum.CustomTargetingKeyReportableType,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
