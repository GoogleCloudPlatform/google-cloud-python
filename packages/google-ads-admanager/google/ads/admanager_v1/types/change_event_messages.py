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

from google.ads.admanager_v1.types import change_event_enums

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "ChangeEvent",
    },
)


class ChangeEvent(proto.Message):
    r"""Represents a single entity change.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the ``ChangeEvent``.
            Format:
            ``networks/{network_code}/changeEvents/{change_event}``
        change_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when the change happened.
        resource_type (google.ads.admanager_v1.types.ChangeEventResourceTypeEnum.ChangeEventResourceType):
            Output only. The type of the resource that
            was changed.

            This field is a member of `oneof`_ ``_resource_type``.
        entity_id (int):
            Output only. The id of the resource that was
            changed. Typically, this is a part of the
            resource name for that entity. It is represented
            here as a long for legacy reasons.

            This field is a member of `oneof`_ ``_entity_id``.
        user (str):
            Output only. The user that made the change. Format:
            ``networks/{network_code}/users/{user}``

            This field is a member of `oneof`_ ``_user``.
        operation_type (google.ads.admanager_v1.types.OperationTypeEnum.OperationType):
            Output only. The type of operation associated with the
            ``ChangeEvent``.

            This field is a member of `oneof`_ ``_operation_type``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    change_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    resource_type: change_event_enums.ChangeEventResourceTypeEnum.ChangeEventResourceType = proto.Field(
        proto.ENUM,
        number=3,
        optional=True,
        enum=change_event_enums.ChangeEventResourceTypeEnum.ChangeEventResourceType,
    )
    entity_id: int = proto.Field(
        proto.INT64,
        number=4,
        optional=True,
    )
    user: str = proto.Field(
        proto.STRING,
        number=6,
        optional=True,
    )
    operation_type: change_event_enums.OperationTypeEnum.OperationType = proto.Field(
        proto.ENUM,
        number=7,
        optional=True,
        enum=change_event_enums.OperationTypeEnum.OperationType,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
