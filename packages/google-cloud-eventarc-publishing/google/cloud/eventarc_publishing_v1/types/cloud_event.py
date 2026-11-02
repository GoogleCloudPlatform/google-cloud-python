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

import google.protobuf.any_pb2 as any_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.eventarc.publishing.v1",
    manifest={
        "CloudEvent",
    },
)


class CloudEvent(proto.Message):
    r"""CloudEvent represents a vendor-neutral specification for
    defining the format of event data.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        id (str):
            Required. Identifies the event. Producers
            MUST ensure that source + id is unique for each
            distinct event.
        source (str):
            Required. Identifies the context in which an
            event happened. URI-reference
        spec_version (str):
            Required. The version of the CloudEvents
            specification which the event uses.
        type_ (str):
            Required. This attribute contains a value
            describing the type of event related to the
            originating occurrence.
        attributes (MutableMapping[str, google.cloud.eventarc_publishing_v1.types.CloudEvent.CloudEventAttributeValue]):
            Optional. Used for Optional & Extension
            Attributes
        binary_data (bytes):
            Optional. Binary data.

            This field is a member of `oneof`_ ``data``.
        text_data (str):
            Optional. Text data.

            This field is a member of `oneof`_ ``data``.
        proto_data (google.protobuf.any_pb2.Any):
            Optional. Proto data.

            NOTE: The ``protoData`` field only functions as expected
            when the payload is specifically a ``CloudEvent`` message
            type, and can't be used for arbitrary protocol buffer
            messages. For any other protocol buffer type, you must
            serialize your proto message into bytes, and use the
            ``binaryData`` field instead.

            This field is a member of `oneof`_ ``data``.
    """

    class CloudEventAttributeValue(proto.Message):
        r"""The following abstract data types are available for use in
        attributes.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            ce_boolean (bool):
                Boolean value.

                This field is a member of `oneof`_ ``attr``.
            ce_integer (int):
                Integer value.

                This field is a member of `oneof`_ ``attr``.
            ce_string (str):
                String value.

                This field is a member of `oneof`_ ``attr``.
            ce_bytes (bytes):
                Bytes value.

                This field is a member of `oneof`_ ``attr``.
            ce_uri (str):
                URI value.

                This field is a member of `oneof`_ ``attr``.
            ce_uri_ref (str):
                URI-reference value.

                This field is a member of `oneof`_ ``attr``.
            ce_timestamp (google.protobuf.timestamp_pb2.Timestamp):
                Timestamp value.

                This field is a member of `oneof`_ ``attr``.
        """

        ce_boolean: bool = proto.Field(
            proto.BOOL,
            number=1,
            oneof="attr",
        )
        ce_integer: int = proto.Field(
            proto.INT32,
            number=2,
            oneof="attr",
        )
        ce_string: str = proto.Field(
            proto.STRING,
            number=3,
            oneof="attr",
        )
        ce_bytes: bytes = proto.Field(
            proto.BYTES,
            number=4,
            oneof="attr",
        )
        ce_uri: str = proto.Field(
            proto.STRING,
            number=5,
            oneof="attr",
        )
        ce_uri_ref: str = proto.Field(
            proto.STRING,
            number=6,
            oneof="attr",
        )
        ce_timestamp: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=7,
            oneof="attr",
            message=timestamp_pb2.Timestamp,
        )

    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    source: str = proto.Field(
        proto.STRING,
        number=2,
    )
    spec_version: str = proto.Field(
        proto.STRING,
        number=3,
    )
    type_: str = proto.Field(
        proto.STRING,
        number=4,
    )
    attributes: MutableMapping[str, CloudEventAttributeValue] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=5,
        message=CloudEventAttributeValue,
    )
    binary_data: bytes = proto.Field(
        proto.BYTES,
        number=6,
        oneof="data",
    )
    text_data: str = proto.Field(
        proto.STRING,
        number=7,
        oneof="data",
    )
    proto_data: any_pb2.Any = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="data",
        message=any_pb2.Any,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
