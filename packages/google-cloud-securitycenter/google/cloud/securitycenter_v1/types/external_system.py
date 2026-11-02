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
        "ExternalSystem",
    },
)


class ExternalSystem(proto.Message):
    r"""Representation of third party SIEM/SOAR fields within SCC.

    Attributes:
        name (str):
            Full resource name of the external system,
            for example:
            "organizations/1234/sources/5678/findings/123456/externalSystems/jira",
            "folders/1234/sources/5678/findings/123456/externalSystems/jira",
            "projects/1234/sources/5678/findings/123456/externalSystems/jira".
        assignees (MutableSequence[str]):
            References primary/secondary etc assignees in
            the external system.
        external_uid (str):
            The identifier that's used to track the
            finding's corresponding case in the external
            system.
        status (str):
            The most recent status of the finding's
            corresponding case, as reported by the external
            system.
        external_system_update_time (google.protobuf.timestamp_pb2.Timestamp):
            The time when the case was last updated, as
            reported by the external system.
        case_uri (str):
            The link to the finding's corresponding case
            in the external system.
        case_priority (str):
            The priority of the finding's corresponding
            case in the external system.
        case_sla (google.protobuf.timestamp_pb2.Timestamp):
            The SLA of the finding's corresponding case
            in the external system.
        case_create_time (google.protobuf.timestamp_pb2.Timestamp):
            The time when the case was created, as
            reported by the external system.
        case_close_time (google.protobuf.timestamp_pb2.Timestamp):
            The time when the case was closed, as
            reported by the external system.
        ticket_info (google.cloud.securitycenter_v1.types.ExternalSystem.TicketInfo):
            Information about the ticket, if any, that is
            being used to track the resolution of the issue
            that is identified by this finding.
    """

    class TicketInfo(proto.Message):
        r"""Information about the ticket, if any, that is being used to
        track the resolution of the issue that is identified by this
        finding.

        Attributes:
            id (str):
                The identifier of the ticket in the ticket
                system.
            assignee (str):
                The assignee of the ticket in the ticket
                system.
            description (str):
                The description of the ticket in the ticket
                system.
            uri (str):
                The link to the ticket in the ticket system.
            status (str):
                The latest status of the ticket, as reported
                by the ticket system.
            update_time (google.protobuf.timestamp_pb2.Timestamp):
                The time when the ticket was last updated, as
                reported by the ticket system.
        """

        id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        assignee: str = proto.Field(
            proto.STRING,
            number=2,
        )
        description: str = proto.Field(
            proto.STRING,
            number=3,
        )
        uri: str = proto.Field(
            proto.STRING,
            number=4,
        )
        status: str = proto.Field(
            proto.STRING,
            number=5,
        )
        update_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=6,
            message=timestamp_pb2.Timestamp,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    assignees: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    external_uid: str = proto.Field(
        proto.STRING,
        number=3,
    )
    status: str = proto.Field(
        proto.STRING,
        number=4,
    )
    external_system_update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    case_uri: str = proto.Field(
        proto.STRING,
        number=6,
    )
    case_priority: str = proto.Field(
        proto.STRING,
        number=7,
    )
    case_sla: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    case_create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )
    case_close_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=11,
        message=timestamp_pb2.Timestamp,
    )
    ticket_info: TicketInfo = proto.Field(
        proto.MESSAGE,
        number=8,
        message=TicketInfo,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
