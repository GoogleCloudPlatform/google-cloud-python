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
    package="google.cloud.vpcaccess.v1",
    manifest={
        "Connector",
        "CreateConnectorRequest",
        "GetConnectorRequest",
        "ListConnectorsRequest",
        "ListConnectorsResponse",
        "DeleteConnectorRequest",
        "OperationMetadata",
    },
)


class Connector(proto.Message):
    r"""Definition of a Serverless VPC Access connector.

    Attributes:
        name (str):
            The resource name in the format
            ``projects/*/locations/*/connectors/*``.
        network (str):
            Name of a VPC network.
        ip_cidr_range (str):
            The range of internal addresses that follows RFC 4632
            notation. Example: ``10.132.0.0/28``.
        state (google.cloud.vpcaccess_v1.types.Connector.State):
            Output only. State of the VPC access
            connector.
        min_throughput (int):
            Minimum throughput of the connector in Mbps.
            Default and min is 200.
        max_throughput (int):
            Maximum throughput of the connector in Mbps.
            Default is 300, max is 1000.
        connected_projects (MutableSequence[str]):
            Output only. List of projects using the
            connector.
        subnet (google.cloud.vpcaccess_v1.types.Connector.Subnet):
            The subnet in which to house the VPC Access
            Connector.
        machine_type (str):
            Machine type of VM Instance underlying
            connector. Default is e2-micro
        min_instances (int):
            Minimum value of instances in autoscaling
            group underlying the connector.
        max_instances (int):
            Maximum value of instances in autoscaling
            group underlying the connector.
    """

    class State(proto.Enum):
        r"""State of a connector.

        Values:
            STATE_UNSPECIFIED (0):
                Invalid state.
            READY (1):
                Connector is deployed and ready to receive
                traffic.
            CREATING (2):
                An Insert operation is in progress. Transient
                condition.
            DELETING (3):
                A Delete operation is in progress. Transient
                condition.
            ERROR (4):
                Connector is in a bad state, manual deletion
                recommended.
            UPDATING (5):
                The connector is being updated.
        """

        STATE_UNSPECIFIED = 0
        READY = 1
        CREATING = 2
        DELETING = 3
        ERROR = 4
        UPDATING = 5

    class Subnet(proto.Message):
        r"""The subnet in which to house the connector

        Attributes:
            name (str):
                Subnet name (relative, not fully qualified).
                E.g. if the full subnet selfLink is
                https://compute.googleapis.com/compute/v1/projects/{project}/regions/{region}/subnetworks/{subnetName}
                the correct input for this field would be
                {subnetName}
            project_id (str):
                Project in which the subnet exists.
                If not set, this project is assumed to be the
                project for which the connector create request
                was issued.
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        project_id: str = proto.Field(
            proto.STRING,
            number=2,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    network: str = proto.Field(
        proto.STRING,
        number=2,
    )
    ip_cidr_range: str = proto.Field(
        proto.STRING,
        number=3,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=4,
        enum=State,
    )
    min_throughput: int = proto.Field(
        proto.INT32,
        number=5,
    )
    max_throughput: int = proto.Field(
        proto.INT32,
        number=6,
    )
    connected_projects: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )
    subnet: Subnet = proto.Field(
        proto.MESSAGE,
        number=8,
        message=Subnet,
    )
    machine_type: str = proto.Field(
        proto.STRING,
        number=10,
    )
    min_instances: int = proto.Field(
        proto.INT32,
        number=11,
    )
    max_instances: int = proto.Field(
        proto.INT32,
        number=12,
    )


class CreateConnectorRequest(proto.Message):
    r"""Request for creating a Serverless VPC Access connector.

    Attributes:
        parent (str):
            Required. The project and location in which the
            configuration should be created, specified in the format
            ``projects/*/locations/*``.
        connector_id (str):
            Required. The ID to use for this connector.
        connector (google.cloud.vpcaccess_v1.types.Connector):
            Required. Resource to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    connector_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    connector: "Connector" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Connector",
    )


class GetConnectorRequest(proto.Message):
    r"""Request for getting a Serverless VPC Access connector.

    Attributes:
        name (str):
            Required. Name of a Serverless VPC Access
            connector to get.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListConnectorsRequest(proto.Message):
    r"""Request for listing Serverless VPC Access connectors in a
    location.

    Attributes:
        parent (str):
            Required. The project and location from which
            the routes should be listed.
        page_size (int):
            Maximum number of functions to return per
            call.
        page_token (str):
            Continuation token.
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


class ListConnectorsResponse(proto.Message):
    r"""Response for listing Serverless VPC Access connectors.

    Attributes:
        connectors (MutableSequence[google.cloud.vpcaccess_v1.types.Connector]):
            List of Serverless VPC Access connectors.
        next_page_token (str):
            Continuation token.
    """

    @property
    def raw_page(self):
        return self

    connectors: MutableSequence["Connector"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Connector",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteConnectorRequest(proto.Message):
    r"""Request for deleting a Serverless VPC Access connector.

    Attributes:
        name (str):
            Required. Name of a Serverless VPC Access
            connector to delete.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class OperationMetadata(proto.Message):
    r"""Metadata for google.longrunning.Operation.

    Attributes:
        method (str):
            Output only. Method that initiated the
            operation e.g.
            google.cloud.vpcaccess.v1.Connectors.CreateConnector.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when the operation was
            created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when the operation
            completed.
        target (str):
            Output only. Name of the resource that this
            operation is acting on e.g.
            projects/my-project/locations/us-central1/connectors/v1.
    """

    method: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    target: str = proto.Field(
        proto.STRING,
        number=5,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
