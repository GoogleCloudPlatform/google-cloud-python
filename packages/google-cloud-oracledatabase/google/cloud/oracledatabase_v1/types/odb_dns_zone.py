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
    package="google.cloud.oracledatabase.v1",
    manifest={
        "OdbDnsZone",
        "CreateOdbDnsZoneRequest",
        "DeleteOdbDnsZoneRequest",
        "ListOdbDnsZonesRequest",
        "ListOdbDnsZonesResponse",
        "GetOdbDnsZoneRequest",
    },
)


class OdbDnsZone(proto.Message):
    r"""Represents OdbDnsZone resource.

    Attributes:
        name (str):
            Identifier. The name of the OdbDnsZone resource in the
            following format:
            projects/{project}/locations/{location}/odbNetworks/{odb_network}/odbDnsZones/{odb_dns_zone}
        domain (str):
            Required. Immutable. The DNS suffix for the
            zone. Ex: abc.example.com.
        labels (MutableMapping[str, str]):
            Optional. Labels or tags associated with the
            resource.
        state (google.cloud.oracledatabase_v1.types.OdbDnsZone.State):
            Output only. State of the OdbDnsZone.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The date and time that the
            OdbDnsZone was created.
    """

    class State(proto.Enum):
        r"""The various lifecycle states of the OdbDnsZone.

        Values:
            STATE_UNSPECIFIED (0):
                Default unspecified value.
            PROVISIONING (1):
                Indicates that the resource is in a
                provisioning state.
            AVAILABLE (2):
                Indicates that the resource is in an
                available state.
            INACTIVE (3):
                Indicates that the resource is available but
                inactive.
            TERMINATING (4):
                Indicates that the resource is in a
                terminating state.
            FAILED (5):
                Indicates that the resource is in a failed
                state.
        """

        STATE_UNSPECIFIED = 0
        PROVISIONING = 1
        AVAILABLE = 2
        INACTIVE = 3
        TERMINATING = 4
        FAILED = 5

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    domain: str = proto.Field(
        proto.STRING,
        number=2,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=3,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=4,
        enum=State,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )


class CreateOdbDnsZoneRequest(proto.Message):
    r"""The request for ``OdbDnsZone.Create``.

    Attributes:
        parent (str):
            Required. The parent value for the OdbDnsZone in the
            following format:
            projects/{project}/locations/{location}/odbNetworks/{odb_network}.
        odb_dns_zone_id (str):
            Required. The ID of the OdbDnsZone to create. This value is
            restricted to (^\ `a-z <[a-z0-9-]{0,61}[a-z0-9]>`__?$) and
            must be a maximum of 63 characters in length. The value must
            start with a letter and end with a letter or a number.
        odb_dns_zone (google.cloud.oracledatabase_v1.types.OdbDnsZone):
            Required. Details of the OdbDnsZone instance
            to create.
        request_id (str):
            Optional. An optional ID to identify the
            request. This value is used to identify
            duplicate requests. If you make a request with
            the same request ID and the original request is
            still in progress or completed, the server
            ignores the second request. This prevents
            clients from accidentally creating duplicate
            commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    odb_dns_zone_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    odb_dns_zone: "OdbDnsZone" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="OdbDnsZone",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class DeleteOdbDnsZoneRequest(proto.Message):
    r"""The request for ``OdbDnsZone.Delete``.

    Attributes:
        name (str):
            Required. The name of the resource in the following format:
            projects/{project}/locations/{location}/odbNetworks/{odb_network}/odbDnsZones/{odb_dns_zone}.
        request_id (str):
            Optional. An optional ID to identify the
            request. This value is used to identify
            duplicate requests. If you make a request with
            the same request ID and the original request is
            still in progress or completed, the server
            ignores the second request. This prevents
            clients from accidentally creating duplicate
            commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListOdbDnsZonesRequest(proto.Message):
    r"""The request for ``OdbDnsZone.List``.

    Attributes:
        parent (str):
            Required. The parent value for the OdbDnsZone in the
            following format:
            projects/{project}/locations/{location}/odbNetworks/{odb_network}.
        page_size (int):
            Optional. The maximum number of items to
            return. If unspecified, at most 50 OdbDnsZones
            will be returned. The maximum value is 1000;
            values above 1000 will be coerced to 1000.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. An expression for filtering the
            results of the request.
        order_by (str):
            Optional. An expression for ordering the
            results of the request.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListOdbDnsZonesResponse(proto.Message):
    r"""The response for ``OdbDnsZone.List``.

    Attributes:
        odb_dns_zones (MutableSequence[google.cloud.oracledatabase_v1.types.OdbDnsZone]):
            The list of OdbDnsZones.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Unreachable locations when listing resources
            across all locations using wildcard location
            '-'.
    """

    @property
    def raw_page(self):
        return self

    odb_dns_zones: MutableSequence["OdbDnsZone"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="OdbDnsZone",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetOdbDnsZoneRequest(proto.Message):
    r"""The request for ``OdbDnsZone.Get``.

    Attributes:
        name (str):
            Required. The name of the OdbDnsZone in the following
            format:
            projects/{project}/locations/{location}/odbNetworks/{odb_network}/odbDnsZones/{odb_dns_zone}.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
