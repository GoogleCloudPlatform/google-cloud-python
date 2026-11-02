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

import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.securitycenter.v2",
    manifest={
        "DataRetentionDeletionEvent",
    },
)


class DataRetentionDeletionEvent(proto.Message):
    r"""Details about data retention deletion violations, in which
    the data is non-compliant based on their retention or deletion
    time, as defined in the applicable data security policy. The
    Data Retention Deletion (DRD) control is a control of the DSPM
    (Data Security Posture Management) suite that enables
    organizations to manage data retention and deletion policies in
    compliance with regulations, such as GDPR and CRPA. DRD supports
    two primary policy types: maximum storage length (max TTL) and
    minimum storage length (min TTL). Both are aimed at helping
    organizations meet regulatory and data management commitments.

    Attributes:
        event_detection_time (google.protobuf.timestamp_pb2.Timestamp):
            Timestamp indicating when the event was
            detected.
        data_object_count (int):
            Number of objects that violated the policy
            for this resource. If the number is less than
            1,000, then the value of this field is the exact
            number. If the number of objects that violated
            the policy is greater than or equal to 1,000,
            then the value of this field is 1000.
        max_retention_allowed (google.protobuf.duration_pb2.Duration):
            Maximum duration of retention allowed from the DRD control.
            This comes from the DRD control where users set a max TTL
            for their data. For example, suppose that a user sets the
            max TTL for a Cloud Storage bucket to 90 days. However, an
            object in that bucket is 100 days old. In this case, a
            DataRetentionDeletionEvent will be generated for that Cloud
            Storage bucket, and the max_retention_allowed is 90 days.
        event_type (google.cloud.securitycenter_v2.types.DataRetentionDeletionEvent.EventType):
            Type of the DRD event.
    """

    class EventType(proto.Enum):
        r"""Type of the DRD event.

        Values:
            EVENT_TYPE_UNSPECIFIED (0):
                Unspecified event type.
            EVENT_TYPE_MAX_TTL_EXCEEDED (1):
                The maximum retention time has been exceeded.
        """

        EVENT_TYPE_UNSPECIFIED = 0
        EVENT_TYPE_MAX_TTL_EXCEEDED = 1

    event_detection_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    data_object_count: int = proto.Field(
        proto.INT64,
        number=3,
    )
    max_retention_allowed: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=4,
        message=duration_pb2.Duration,
    )
    event_type: EventType = proto.Field(
        proto.ENUM,
        number=5,
        enum=EventType,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
