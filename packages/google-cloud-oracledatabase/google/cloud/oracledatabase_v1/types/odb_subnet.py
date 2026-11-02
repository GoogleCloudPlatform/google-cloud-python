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
        "OdbSubnet",
        "CreateOdbSubnetRequest",
        "DeleteOdbSubnetRequest",
        "ListOdbSubnetsRequest",
        "ListOdbSubnetsResponse",
        "GetOdbSubnetRequest",
    },
)


class OdbSubnet(proto.Message):
    r"""Represents OdbSubnet resource.

    Attributes:
        name (str):
            Identifier. The name of the OdbSubnet resource in the
            following format:
            projects/{project}/locations/{location}/odbNetworks/{odb_network}/odbSubnets/{odb_subnet}
        cidr_range (str):
            Required. The CIDR range of the subnet.
        purpose (google.cloud.oracledatabase_v1.types.OdbSubnet.Purpose):
            Required. Purpose of the subnet.
        labels (MutableMapping[str, str]):
            Optional. Labels or tags associated with the
            resource.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The date and time that the
            OdbNetwork was created.
        state (google.cloud.oracledatabase_v1.types.OdbSubnet.State):
            Output only. State of the ODB Subnet.
    """

    class Purpose(proto.Enum):
        r"""Purpose available for the subnet.

        Values:
            PURPOSE_UNSPECIFIED (0):
                Default unspecified value.
            CLIENT_SUBNET (1):
                Subnet to be used for client connections.
            BACKUP_SUBNET (2):
                Subnet to be used for backup.
        """

        PURPOSE_UNSPECIFIED = 0
        CLIENT_SUBNET = 1
        BACKUP_SUBNET = 2

    class State(proto.Enum):
        r"""The various lifecycle states of the ODB Subnet.

        Values:
            STATE_UNSPECIFIED (0):
                Default unspecified value.
            PROVISIONING (1):
                Indicates that the resource is in
                provisioning state.
            AVAILABLE (2):
                Indicates that the resource is in available
                state.
            TERMINATING (3):
                Indicates that the resource is in terminating
                state.
            FAILED (4):
                Indicates that the resource is in failed
                state.
        """

        STATE_UNSPECIFIED = 0
        PROVISIONING = 1
        AVAILABLE = 2
        TERMINATING = 3
        FAILED = 4

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    cidr_range: str = proto.Field(
        proto.STRING,
        number=2,
    )
    purpose: Purpose = proto.Field(
        proto.ENUM,
        number=3,
        enum=Purpose,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=6,
        enum=State,
    )


class CreateOdbSubnetRequest(proto.Message):
    r"""The request for ``OdbSubnet.Create``.

    Attributes:
        parent (str):
            Required. The parent value for the OdbSubnet in the
            following format:
            projects/{project}/locations/{location}/odbNetworks/{odb_network}.
        odb_subnet_id (str):
            Required. The ID of the OdbSubnet to create. This value is
            restricted to (^\ `a-z <[a-z0-9-]{0,61}[a-z0-9]>`__?$) and
            must be a maximum of 63 characters in length. The value must
            start with a letter and end with a letter or a number.
        odb_subnet (google.cloud.oracledatabase_v1.types.OdbSubnet):
            Required. Details of the OdbSubnet instance
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
    odb_subnet_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    odb_subnet: "OdbSubnet" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="OdbSubnet",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class DeleteOdbSubnetRequest(proto.Message):
    r"""The request for ``OdbSubnet.Delete``.

    Attributes:
        name (str):
            Required. The name of the resource in the following format:
            projects/{project}/locations/{region}/odbNetworks/{odb_network}/odbSubnets/{odb_subnet}.
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


class ListOdbSubnetsRequest(proto.Message):
    r"""The request for ``OdbSubnet.List``.

    Attributes:
        parent (str):
            Required. The parent value for the OdbSubnet in the
            following format:
            projects/{project}/locations/{location}/odbNetworks/{odb_network}.
        page_size (int):
            Optional. The maximum number of items to
            return. If unspecified, at most 50 ODB Networks
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


class ListOdbSubnetsResponse(proto.Message):
    r"""The response for ``OdbSubnet.List``.

    Attributes:
        odb_subnets (MutableSequence[google.cloud.oracledatabase_v1.types.OdbSubnet]):
            The list of ODB Subnets.
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

    odb_subnets: MutableSequence["OdbSubnet"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="OdbSubnet",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetOdbSubnetRequest(proto.Message):
    r"""The request for ``OdbSubnet.Get``.

    Attributes:
        name (str):
            Required. The name of the OdbSubnet in the following format:
            projects/{project}/locations/{location}/odbNetworks/{odb_network}/odbSubnets/{odb_subnet}.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
