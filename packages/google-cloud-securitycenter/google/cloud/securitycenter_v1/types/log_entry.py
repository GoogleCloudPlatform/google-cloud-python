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
    package="google.cloud.securitycenter.v1",
    manifest={
        "LogEntry",
        "CloudLoggingEntry",
    },
)


class LogEntry(proto.Message):
    r"""An individual entry in a log.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        cloud_logging_entry (google.cloud.securitycenter_v1.types.CloudLoggingEntry):
            An individual entry in a log stored in Cloud
            Logging.

            This field is a member of `oneof`_ ``log_entry``.
    """

    cloud_logging_entry: "CloudLoggingEntry" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="log_entry",
        message="CloudLoggingEntry",
    )


class CloudLoggingEntry(proto.Message):
    r"""Metadata taken from a `Cloud Logging
    LogEntry <https://cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry>`__

    Attributes:
        insert_id (str):
            A unique identifier for the log entry.
        log_id (str):
            The type of the log (part of ``log_name``. ``log_name`` is
            the resource name of the log to which this log entry
            belongs). For example:
            ``cloudresourcemanager.googleapis.com/activity``. Note that
            this field is not URL-encoded, unlike the ``LOG_ID`` field
            in ``LogEntry``.
        resource_container (str):
            The organization, folder, or project of the
            monitored resource that produced this log entry.
        timestamp (google.protobuf.timestamp_pb2.Timestamp):
            The time the event described by the log entry
            occurred.
    """

    insert_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    log_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    resource_container: str = proto.Field(
        proto.STRING,
        number=3,
    )
    timestamp: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
