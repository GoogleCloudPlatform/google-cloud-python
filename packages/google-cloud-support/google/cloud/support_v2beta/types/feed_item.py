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

from google.cloud.support_v2beta.types import attachment as gcs_attachment
from google.cloud.support_v2beta.types import comment as gcs_comment
from google.cloud.support_v2beta.types import email_message as gcs_email_message

__protobuf__ = proto.module(
    package="google.cloud.support.v2beta",
    manifest={
        "FeedItem",
    },
)


class FeedItem(proto.Message):
    r"""A feed item associated with a support case.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        comment (google.cloud.support_v2beta.types.Comment):
            Output only. A comment added to the case.

            This field is a member of `oneof`_ ``event_object``.
        attachment (google.cloud.support_v2beta.types.Attachment):
            Output only. An attachment attached to the
            case.

            This field is a member of `oneof`_ ``event_object``.
        email_message (google.cloud.support_v2beta.types.EmailMessage):
            Output only. An email message received in
            reply to the case.

            This field is a member of `oneof`_ ``event_object``.
        deleted_attachment (google.cloud.support_v2beta.types.Attachment):
            Output only. A deleted attachment that used
            to be associated with the support case.

            This field is a member of `oneof`_ ``event_object``.
        event_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time corresponding to the event
            of this item.
    """

    comment: gcs_comment.Comment = proto.Field(
        proto.MESSAGE,
        number=100,
        oneof="event_object",
        message=gcs_comment.Comment,
    )
    attachment: gcs_attachment.Attachment = proto.Field(
        proto.MESSAGE,
        number=101,
        oneof="event_object",
        message=gcs_attachment.Attachment,
    )
    email_message: gcs_email_message.EmailMessage = proto.Field(
        proto.MESSAGE,
        number=102,
        oneof="event_object",
        message=gcs_email_message.EmailMessage,
    )
    deleted_attachment: gcs_attachment.Attachment = proto.Field(
        proto.MESSAGE,
        number=103,
        oneof="event_object",
        message=gcs_attachment.Attachment,
    )
    event_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
