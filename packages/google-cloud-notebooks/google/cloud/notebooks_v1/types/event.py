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
    package="google.cloud.notebooks.v1",
    manifest={
        "Event",
    },
)


class Event(proto.Message):
    r"""The definition of an Event for a managed / semi-managed
    notebook instance.

    Attributes:
        report_time (google.protobuf.timestamp_pb2.Timestamp):
            Event report time.
        type_ (google.cloud.notebooks_v1.types.Event.EventType):
            Event type.
        details (MutableMapping[str, str]):
            Optional. Event details. This field is used
            to pass event information.
    """

    class EventType(proto.Enum):
        r"""The definition of the event types.

        Values:
            EVENT_TYPE_UNSPECIFIED (0):
                Event is not specified.
            IDLE (1):
                The instance / runtime is idle
            HEARTBEAT (2):
                The instance / runtime is available.
                This event indicates that instance / runtime
                underlying compute is operational.
            HEALTH (3):
                The instance / runtime health is available.
                This event indicates that instance / runtime
                health information.
            MAINTENANCE (4):
                The instance / runtime is available.
                This event allows instance / runtime to send
                Host maintenance information to Control Plane.
                https://cloud.google.com/compute/docs/gpus/gpu-host-maintenance
        """

        EVENT_TYPE_UNSPECIFIED = 0
        IDLE = 1
        HEARTBEAT = 2
        HEALTH = 3
        MAINTENANCE = 4

    report_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    type_: EventType = proto.Field(
        proto.ENUM,
        number=2,
        enum=EventType,
    )
    details: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
