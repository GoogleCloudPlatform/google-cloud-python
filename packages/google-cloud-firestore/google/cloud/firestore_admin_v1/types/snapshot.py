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
    package="google.firestore.admin.v1",
    manifest={
        "PitrSnapshot",
    },
)


class PitrSnapshot(proto.Message):
    r"""A consistent snapshot of a database at a specific point in
    time. A PITR (Point-in-time recovery) snapshot with previous
    versions of a database's data is available for every minute up
    to the associated database's data retention period. If the PITR
    feature is enabled, the retention period is 7 days; otherwise,
    it is one hour.

    Attributes:
        database (str):
            Required. The name of the database that this was a snapshot
            of. Format: ``projects/{project}/databases/{database}``.
        database_uid (bytes):
            Output only. Public UUID of the database the
            snapshot was associated with.
        snapshot_time (google.protobuf.timestamp_pb2.Timestamp):
            Required. Snapshot time of the database.
    """

    database: str = proto.Field(
        proto.STRING,
        number=1,
    )
    database_uid: bytes = proto.Field(
        proto.BYTES,
        number=2,
    )
    snapshot_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
