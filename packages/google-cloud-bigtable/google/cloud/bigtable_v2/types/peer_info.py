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
    package="google.bigtable.v2",
    manifest={
        "PeerInfo",
    },
)


class PeerInfo(proto.Message):
    r"""PeerInfo contains information about the peer that the client
    is connecting to.

    Attributes:
        google_frontend_id (int):
            An opaque identifier for the Google Frontend
            which serviced this request. Only set when not
            using DirectAccess.
        application_frontend_id (int):
            An opaque identifier for the application
            frontend which serviced this request.
        application_frontend_region (str):
            The Cloud region of the application frontend
            that served this request.
        application_frontend_zone (str):
            The Cloud zone of the application frontend
            that served this request.
        application_frontend_subzone (str):
            The subzone of the application frontend that
            served this request, e.g. an identifier for
            where within a zone (within the reported region)
            the application frontend is.
        transport_type (google.cloud.bigtable_v2.types.PeerInfo.TransportType):

    """

    class TransportType(proto.Enum):
        r"""The transport type that the client used to connect to this
        peer.

        Values:
            TRANSPORT_TYPE_UNKNOWN (0):
                The transport type is unknown.
            TRANSPORT_TYPE_EXTERNAL (1):
                The client connected to this peer via an
                external network (e.g. outside Google Cloud).
            TRANSPORT_TYPE_CLOUD_PATH (2):
                The client connected to this peer via
                CloudPath.
            TRANSPORT_TYPE_DIRECT_ACCESS (3):
                The client connected to this peer via
                DirectAccess.
            TRANSPORT_TYPE_SESSION_UNKNOWN (4):
                The client connected to this peer via
                Bigtable Sessions using an unknown transport
                type.
            TRANSPORT_TYPE_SESSION_EXTERNAL (5):
                The client connected to this peer via
                Bigtable Sessions on an external network (e.g.
                outside Google Cloud).
            TRANSPORT_TYPE_SESSION_CLOUD_PATH (6):
                The client connected to this peer via
                Bigtable Sessions using CloudPath.
            TRANSPORT_TYPE_SESSION_DIRECT_ACCESS (7):
                The client connected to this peer via
                Bigtable Sessions using DirectAccess.
        """

        TRANSPORT_TYPE_UNKNOWN = 0
        TRANSPORT_TYPE_EXTERNAL = 1
        TRANSPORT_TYPE_CLOUD_PATH = 2
        TRANSPORT_TYPE_DIRECT_ACCESS = 3
        TRANSPORT_TYPE_SESSION_UNKNOWN = 4
        TRANSPORT_TYPE_SESSION_EXTERNAL = 5
        TRANSPORT_TYPE_SESSION_CLOUD_PATH = 6
        TRANSPORT_TYPE_SESSION_DIRECT_ACCESS = 7

    google_frontend_id: int = proto.Field(
        proto.INT64,
        number=1,
    )
    application_frontend_id: int = proto.Field(
        proto.INT64,
        number=2,
    )
    application_frontend_region: str = proto.Field(
        proto.STRING,
        number=6,
    )
    application_frontend_zone: str = proto.Field(
        proto.STRING,
        number=3,
    )
    application_frontend_subzone: str = proto.Field(
        proto.STRING,
        number=4,
    )
    transport_type: TransportType = proto.Field(
        proto.ENUM,
        number=5,
        enum=TransportType,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
