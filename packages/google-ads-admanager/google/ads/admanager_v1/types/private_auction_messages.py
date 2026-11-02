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
        "PrivateAuction",
    },
)


class PrivateAuction(proto.Message):
    r"""The ``PrivateAuction`` resource.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the ``PrivateAuction``.
            Format:
            ``networks/{network_code}/privateAuctions/{private_auction_id}``
        private_auction_id (int):
            Output only. Deprecated: ``PrivateAuction`` ID.

            This field is a member of `oneof`_ ``_private_auction_id``.
        display_name (str):
            Required. Display name of the ``PrivateAuction``. This
            attribute has a maximum length of 255 bytes.

            This field is a member of `oneof`_ ``_display_name``.
        description (str):
            Optional. Description of the ``PrivateAuction``. This
            attribute has a maximum length of 4096 bytes.

            This field is a member of `oneof`_ ``_description``.
        seller_contact_users (MutableSequence[str]):
            Optional. The resource names of the seller contact users
            associated with this ``PrivateAuction``. Format:
            ``networks/{network_code}/users/{user_id}``
        archived (bool):
            Output only. Whether the ``PrivateAuction`` is archived.

            This field is a member of `oneof`_ ``_archived``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The instant at which the
            PrivateAuction was created.

            This field is a member of `oneof`_ ``_create_time``.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The instant at which the
            PrivateAuction was last updated.

            This field is a member of `oneof`_ ``_update_time``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    private_auction_id: int = proto.Field(
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
    seller_contact_users: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=9,
    )
    archived: bool = proto.Field(
        proto.BOOL,
        number=6,
        optional=True,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        optional=True,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        optional=True,
        message=timestamp_pb2.Timestamp,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
