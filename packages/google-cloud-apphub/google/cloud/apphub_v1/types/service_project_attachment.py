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
    package="google.cloud.apphub.v1",
    manifest={
        "ServiceProjectAttachment",
    },
)


class ServiceProjectAttachment(proto.Message):
    r"""ServiceProjectAttachment represents an attachment from a
    service project to a host project. Service projects contain the
    underlying cloud infrastructure resources, and expose these
    resources to the host project through a
    ServiceProjectAttachment. With the attachments, the host project
    can provide an aggregated view of resources across all service
    projects.

    Attributes:
        name (str):
            Identifier. The resource name of a ServiceProjectAttachment.
            Format:
            ``"projects/{host-project-id}/locations/global/serviceProjectAttachments/{service-project-id}."``
        service_project (str):
            Required. Immutable. Service project name in the format:
            ``"projects/abc"`` or ``"projects/123"``. As input, project
            name with either project id or number are accepted. As
            output, this field will contain project number.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Create time.
        uid (str):
            Output only. A globally unique identifier (in UUID4 format)
            for the ``ServiceProjectAttachment``.
        state (google.cloud.apphub_v1.types.ServiceProjectAttachment.State):
            Output only. ServiceProjectAttachment state.
    """

    class State(proto.Enum):
        r"""ServiceProjectAttachment state.

        Values:
            STATE_UNSPECIFIED (0):
                Unspecified state.
            CREATING (1):
                The ServiceProjectAttachment is being
                created.
            ACTIVE (2):
                The ServiceProjectAttachment is ready.
                This means Services and Workloads under the
                corresponding ServiceProjectAttachment is ready
                for registration.
            DELETING (3):
                The ServiceProjectAttachment is being
                deleted.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        ACTIVE = 2
        DELETING = 3

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    service_project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=4,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=5,
        enum=State,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
