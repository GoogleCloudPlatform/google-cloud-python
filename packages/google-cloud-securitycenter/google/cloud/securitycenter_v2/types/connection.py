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

import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.securitycenter.v2",
    manifest={
        "Connection",
    },
)


class Connection(proto.Message):
    r"""Contains information about the IP connection associated with
    the finding.

    Attributes:
        destination_ip (str):
            Destination IP address. Not present for
            sockets that are listening and not connected.
        destination_port (int):
            Destination port. Not present for sockets
            that are listening and not connected.
        source_ip (str):
            Source IP address.
        source_port (int):
            Source port.
        protocol (google.cloud.securitycenter_v2.types.Connection.Protocol):
            IANA Internet Protocol Number such as TCP(6)
            and UDP(17).
    """

    class Protocol(proto.Enum):
        r"""IANA Internet Protocol Number such as TCP(6) and UDP(17).

        Values:
            PROTOCOL_UNSPECIFIED (0):
                Unspecified protocol (not HOPOPT).
            ICMP (1):
                Internet Control Message Protocol.
            TCP (6):
                Transmission Control Protocol.
            UDP (17):
                User Datagram Protocol.
            GRE (47):
                Generic Routing Encapsulation.
            ESP (50):
                Encap Security Payload.
        """

        PROTOCOL_UNSPECIFIED = 0
        ICMP = 1
        TCP = 6
        UDP = 17
        GRE = 47
        ESP = 50

    destination_ip: str = proto.Field(
        proto.STRING,
        number=1,
    )
    destination_port: int = proto.Field(
        proto.INT32,
        number=2,
    )
    source_ip: str = proto.Field(
        proto.STRING,
        number=3,
    )
    source_port: int = proto.Field(
        proto.INT32,
        number=4,
    )
    protocol: Protocol = proto.Field(
        proto.ENUM,
        number=5,
        enum=Protocol,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
