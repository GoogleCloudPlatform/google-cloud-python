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

from google.cloud.support_v2beta.types import actor as gcs_actor
from google.cloud.support_v2beta.types import content

__protobuf__ = proto.module(
    package="google.cloud.support.v2beta",
    manifest={
        "EmailMessage",
    },
)


class EmailMessage(proto.Message):
    r"""An email associated with a support case.

    Attributes:
        name (str):
            Identifier. Resource name for the email
            message.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when this email message
            object was created.
        actor (google.cloud.support_v2beta.types.Actor):
            Output only. The user or Google Support agent
            that created this email message. This is
            inferred from the headers on the email message.
        subject (str):
            Output only. Subject of the email.
        recipient_email_addresses (MutableSequence[str]):
            Output only. Email addresses the email was
            sent to.
        cc_email_addresses (MutableSequence[str]):
            Output only. Email addresses CCed on the
            email.
        body_content (google.cloud.support_v2beta.types.TextContent):
            Output only. The full email message body. A
            best-effort attempt is made to remove extraneous
            reply threads.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    actor: gcs_actor.Actor = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gcs_actor.Actor,
    )
    subject: str = proto.Field(
        proto.STRING,
        number=4,
    )
    recipient_email_addresses: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    cc_email_addresses: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    body_content: content.TextContent = proto.Field(
        proto.MESSAGE,
        number=8,
        message=content.TextContent,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
