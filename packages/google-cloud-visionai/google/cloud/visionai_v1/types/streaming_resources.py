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
import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.visionai.v1",
    manifest={
        "GstreamerBufferDescriptor",
        "RawImageDescriptor",
        "PacketType",
        "ServerMetadata",
        "SeriesMetadata",
        "PacketHeader",
        "Packet",
    },
)


class GstreamerBufferDescriptor(proto.Message):
    r"""The descriptor for a gstreamer buffer payload.

    Attributes:
        caps_string (str):
            The caps string of the payload.
        is_key_frame (bool):
            Whether the buffer is a key frame.
        pts_time (google.protobuf.timestamp_pb2.Timestamp):
            PTS of the frame.
        dts_time (google.protobuf.timestamp_pb2.Timestamp):
            DTS of the frame.
        duration (google.protobuf.duration_pb2.Duration):
            Duration of the frame.
    """

    caps_string: str = proto.Field(
        proto.STRING,
        number=1,
    )
    is_key_frame: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    pts_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    dts_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=5,
        message=duration_pb2.Duration,
    )


class RawImageDescriptor(proto.Message):
    r"""The descriptor for a raw image.

    Attributes:
        format_ (str):
            Raw image format. Its possible values are:
            "srgb".
        height (int):
            The height of the image.
        width (int):
            The width of the image.
    """

    format_: str = proto.Field(
        proto.STRING,
        number=1,
    )
    height: int = proto.Field(
        proto.INT32,
        number=2,
    )
    width: int = proto.Field(
        proto.INT32,
        number=3,
    )


class PacketType(proto.Message):
    r"""The message that represents the data type of a packet.

    Attributes:
        type_class (str):
            The type class of the packet. Its possible
            values are: "gst", "protobuf", and "string".
        type_descriptor (google.cloud.visionai_v1.types.PacketType.TypeDescriptor):
            The type descriptor.
    """

    class TypeDescriptor(proto.Message):
        r"""The message that fully specifies the type of the packet.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            gstreamer_buffer_descriptor (google.cloud.visionai_v1.types.GstreamerBufferDescriptor):
                GstreamerBufferDescriptor is the descriptor
                for gstreamer buffer type.

                This field is a member of `oneof`_ ``type_details``.
            raw_image_descriptor (google.cloud.visionai_v1.types.RawImageDescriptor):
                RawImageDescriptor is the descriptor for the
                raw image type.

                This field is a member of `oneof`_ ``type_details``.
            type_ (str):
                The type of the packet. Its possible values is codec
                dependent.

                The fully qualified type name is always the concatenation of
                the value in ``type_class`` together with the value in
                ``type``, separated by a '/'.

                Note that specific codecs can define their own type
                hierarchy, and so the type string here can in fact be
                separated by multiple '/'s of its own.

                Please see the open source SDK for specific codec
                documentation.
        """

        gstreamer_buffer_descriptor: "GstreamerBufferDescriptor" = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="type_details",
            message="GstreamerBufferDescriptor",
        )
        raw_image_descriptor: "RawImageDescriptor" = proto.Field(
            proto.MESSAGE,
            number=3,
            oneof="type_details",
            message="RawImageDescriptor",
        )
        type_: str = proto.Field(
            proto.STRING,
            number=1,
        )

    type_class: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_descriptor: TypeDescriptor = proto.Field(
        proto.MESSAGE,
        number=2,
        message=TypeDescriptor,
    )


class ServerMetadata(proto.Message):
    r"""The message that represents server metadata.

    Attributes:
        offset (int):
            The offset position for the packet in its
            stream.
        ingest_time (google.protobuf.timestamp_pb2.Timestamp):
            The timestamp at which the stream server
            receives this packet. This is based on the local
            clock of on the server side. It is guaranteed to
            be monotonically increasing for the packets
            within each session; however this timestamp is
            not comparable across packets sent to the same
            stream different sessions. Session here refers
            to one individual gRPC streaming request to the
            stream server.
    """

    offset: int = proto.Field(
        proto.INT64,
        number=1,
    )
    ingest_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )


class SeriesMetadata(proto.Message):
    r"""The message that represents series metadata.

    Attributes:
        series (str):
            Series name. It's in the format of
            "projects/{project}/locations/{location}/clusters/{cluster}/series/{stream}".
    """

    series: str = proto.Field(
        proto.STRING,
        number=1,
    )


class PacketHeader(proto.Message):
    r"""The message that represents packet header.

    Attributes:
        capture_time (google.protobuf.timestamp_pb2.Timestamp):
            Input only. The capture time of the packet.
        type_ (google.cloud.visionai_v1.types.PacketType):
            Input only. Immutable. The type of the
            payload.
        metadata (google.protobuf.struct_pb2.Struct):
            Input only. This field is for users to attach
            user managed metadata.
        server_metadata (google.cloud.visionai_v1.types.ServerMetadata):
            Output only. Metadata that the server appends
            to each packet before sending it to receivers.
            You don't need to set a value for this field
            when sending packets.
        series_metadata (google.cloud.visionai_v1.types.SeriesMetadata):
            Input only. Immutable. Metadata that the
            server needs to know where to write the packets
            to. It's only required for the first packet.
        flags (int):
            Immutable. Packet flag set. SDK will set the
            flag automatically.
        trace_context (str):
            Immutable. Header string for tracing across services. It
            should be set when the packet is first arrived in the stream
            server.

            The input format is a lowercase hex string:

            - version_id: 1 byte, currently must be zero - hex encoded
              (2 characters)
            - trace_id: 16 bytes (opaque blob) - hex encoded (32
              characters)
            - span_id: 8 bytes (opaque blob) - hex encoded (16
              characters)
            - trace_options: 1 byte (LSB means tracing enabled) - hex
              encoded (2 characters) Example:
              "00-404142434445464748494a4b4c4d4e4f-6162636465666768-01"
              v trace_id span_id options
    """

    capture_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    type_: "PacketType" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="PacketType",
    )
    metadata: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=3,
        message=struct_pb2.Struct,
    )
    server_metadata: "ServerMetadata" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="ServerMetadata",
    )
    series_metadata: "SeriesMetadata" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="SeriesMetadata",
    )
    flags: int = proto.Field(
        proto.INT32,
        number=6,
    )
    trace_context: str = proto.Field(
        proto.STRING,
        number=7,
    )


class Packet(proto.Message):
    r"""The quanta of datum that the series accepts.

    Attributes:
        header (google.cloud.visionai_v1.types.PacketHeader):
            The packet header.
        payload (bytes):
            The payload of the packet.
    """

    header: "PacketHeader" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="PacketHeader",
    )
    payload: bytes = proto.Field(
        proto.BYTES,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
