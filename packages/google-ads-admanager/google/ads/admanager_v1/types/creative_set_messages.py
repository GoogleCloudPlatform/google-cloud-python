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

import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "CreativeSet",
    },
)


class CreativeSet(proto.Message):
    r"""A ``CreativeSet`` is comprised of a master ``Creative`` and its
    companion ``Creative``\ s.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the ``CreativeSet``.
            Format:
            ``networks/{network_code}/creativeSets/{creative_set_id}``
        display_name (str):
            Required. The name of the ``CreativeSet``. This attribute
            has a maximum length of 255 characters.

            This field is a member of `oneof`_ ``_display_name``.
        master_creative (str):
            Required. Immutable. The master
            [Creative][google.ads.admanager.v1.Creative] to which the
            ``CreativeSet`` is associated.

            This field is a member of `oneof`_ ``_master_creative``.
        companion_creatives (MutableSequence[str]):
            Required. The resource names of the companion
            ``Creative``\ s associated with this ``CreativeSet``.
            Format: ``networks/{network_code}/creatives/{creative}``
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time this ``CreativeSet`` was last
            modified.

            This field is a member of `oneof`_ ``_update_time``.
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
    master_creative: str = proto.Field(
        proto.STRING,
        number=5,
        optional=True,
    )
    companion_creatives: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        optional=True,
        message=timestamp_pb2.Timestamp,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
