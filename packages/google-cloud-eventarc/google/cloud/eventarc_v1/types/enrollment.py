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
    package="google.cloud.eventarc.v1",
    manifest={
        "Enrollment",
    },
)


class Enrollment(proto.Message):
    r"""An enrollment represents a subscription for messages on a
    particular message bus. It defines a matching criteria for
    messages on the bus and the subscriber endpoint where matched
    messages should be delivered.

    Attributes:
        name (str):
            Identifier. Resource name of the form
            projects/{project}/locations/{location}/enrollments/{enrollment}
        uid (str):
            Output only. Server assigned unique
            identifier for the channel. The value is a UUID4
            string and guaranteed to remain unchanged until
            the resource is deleted.
        etag (str):
            Output only. This checksum is computed by the
            server based on the value of other fields, and
            might be sent only on update and delete requests
            to ensure that the client has an up-to-date
            value before proceeding.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The creation time.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last-modified time.
        labels (MutableMapping[str, str]):
            Optional. Resource labels.
        annotations (MutableMapping[str, str]):
            Optional. Resource annotations.
        display_name (str):
            Optional. Resource display name.
        cel_match (str):
            Required. A CEL expression identifying which
            messages this enrollment applies to.
        message_bus (str):
            Required. Immutable. Resource name of the
            message bus identifying the source of the
            messages. It matches the form
            projects/{project}/locations/{location}/messageBuses/{messageBus}.
        destination (str):
            Required. Destination is the Pipeline that the Enrollment is
            delivering to. It must point to the full resource name of a
            Pipeline. Format:
            "projects/{PROJECT_ID}/locations/{region}/pipelines/{PIPELINE_ID)".
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=3,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=6,
    )
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=7,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=8,
    )
    cel_match: str = proto.Field(
        proto.STRING,
        number=9,
    )
    message_bus: str = proto.Field(
        proto.STRING,
        number=10,
    )
    destination: str = proto.Field(
        proto.STRING,
        number=11,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
