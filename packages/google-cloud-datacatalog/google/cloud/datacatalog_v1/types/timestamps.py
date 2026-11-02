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
    package="google.cloud.datacatalog.v1",
    manifest={
        "SystemTimestamps",
    },
)


class SystemTimestamps(proto.Message):
    r"""Timestamps associated with this resource in a particular
    system.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Creation timestamp of the resource within the
            given system.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Timestamp of the last modification of the
            resource or its metadata within a given system.

            Note: Depending on the source system, not every
            modification updates this timestamp.
            For example, BigQuery timestamps every metadata
            modification but not data or permission changes.
        expire_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Expiration timestamp of the
            resource within the given system.
            Currently only applicable to BigQuery resources.
    """

    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    expire_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
