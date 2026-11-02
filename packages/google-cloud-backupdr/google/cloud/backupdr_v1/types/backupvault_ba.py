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
    package="google.cloud.backupdr.v1",
    manifest={
        "BackupApplianceBackupProperties",
    },
)


class BackupApplianceBackupProperties(proto.Message):
    r"""BackupApplianceBackupProperties represents BackupDR backup
    appliance's properties.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        generation_id (int):
            Output only. The numeric generation ID of the
            backup (monotonically increasing).

            This field is a member of `oneof`_ ``_generation_id``.
        finalize_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when this backup object
            was finalized (if none, backup is not
            finalized).

            This field is a member of `oneof`_ ``_finalize_time``.
        recovery_range_start_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. The earliest timestamp of data
            available in this Backup.

            This field is a member of `oneof`_ ``_recovery_range_start_time``.
        recovery_range_end_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. The latest timestamp of data
            available in this Backup.

            This field is a member of `oneof`_ ``_recovery_range_end_time``.
    """

    generation_id: int = proto.Field(
        proto.INT32,
        number=1,
        optional=True,
    )
    finalize_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        optional=True,
        message=timestamp_pb2.Timestamp,
    )
    recovery_range_start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        optional=True,
        message=timestamp_pb2.Timestamp,
    )
    recovery_range_end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        optional=True,
        message=timestamp_pb2.Timestamp,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
