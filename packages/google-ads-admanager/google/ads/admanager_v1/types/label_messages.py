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

from google.ads.admanager_v1.types import label_enums

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "Label",
    },
)


class Label(proto.Message):
    r"""A Label is additional information that can be added to an
    entity.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the ``Label``. Format:
            ``networks/{network_code}/labels/{label_id}``
        display_name (str):
            Required. Display name of the Label. This
            attribute has a maximum length of 127
            characters.

            This field is a member of `oneof`_ ``_display_name``.
        description (str):
            Optional. A description of the label. This
            attribute has a maximum length of 255
            characters.

            This field is a member of `oneof`_ ``_description``.
        active (bool):
            Output only. Specifies whether or not the
            label is active.

            This field is a member of `oneof`_ ``_active``.
        types (MutableSequence[google.ads.admanager_v1.types.LabelTypeEnum.LabelType]):
            Required. Unordered list. The types of the
            Label.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
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
    active: bool = proto.Field(
        proto.BOOL,
        number=5,
        optional=True,
    )
    types: MutableSequence[label_enums.LabelTypeEnum.LabelType] = proto.RepeatedField(
        proto.ENUM,
        number=7,
        enum=label_enums.LabelTypeEnum.LabelType,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
