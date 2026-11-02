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

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.beyondcorp.clientconnectorservices.v1",
    manifest={
        "ClientConnectorService",
        "ListClientConnectorServicesRequest",
        "ListClientConnectorServicesResponse",
        "GetClientConnectorServiceRequest",
        "CreateClientConnectorServiceRequest",
        "UpdateClientConnectorServiceRequest",
        "DeleteClientConnectorServiceRequest",
        "ClientConnectorServiceOperationMetadata",
    },
)


class ClientConnectorService(proto.Message):
    r"""Message describing ClientConnectorService object.

    Attributes:
        name (str):
            Required. Name of resource. The name is
            ignored during creation.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. [Output only] Create time stamp.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. [Output only] Update time stamp.
        display_name (str):
            Optional. User-provided name. The display name should follow
            certain format.

            - Must be 6 to 30 characters in length.
            - Can only contain lowercase letters, numbers, and hyphens.
            - Must start with a letter.
        ingress (google.cloud.beyondcorp_clientconnectorservices_v1.types.ClientConnectorService.Ingress):
            Required. The details of the ingress
            settings.
        egress (google.cloud.beyondcorp_clientconnectorservices_v1.types.ClientConnectorService.Egress):
            Required. The details of the egress settings.
        state (google.cloud.beyondcorp_clientconnectorservices_v1.types.ClientConnectorService.State):
            Output only. The operational state of the
            ClientConnectorService.
    """

    class State(proto.Enum):
        r"""Represents the different states of a ClientConnectorService.

        Values:
            STATE_UNSPECIFIED (0):
                Default value. This value is unused.
            CREATING (1):
                ClientConnectorService is being created.
            UPDATING (2):
                ClientConnectorService is being updated.
            DELETING (3):
                ClientConnectorService is being deleted.
            RUNNING (4):
                ClientConnectorService is running.
            DOWN (5):
                ClientConnectorService is down and may be
                restored in the future. This happens when CCFE
                sends ProjectState = OFF.
            ERROR (6):
                ClientConnectorService encountered an error
                and is in an indeterministic state.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        UPDATING = 2
        DELETING = 3
        RUNNING = 4
        DOWN = 5
        ERROR = 6

    class Ingress(proto.Message):
        r"""Settings of how to connect to the ClientGateway.
        One of the following options should be set.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            config (google.cloud.beyondcorp_clientconnectorservices_v1.types.ClientConnectorService.Ingress.Config):
                The basic ingress config for ClientGateways.

                This field is a member of `oneof`_ ``ingress_config``.
        """

        class Config(proto.Message):
            r"""The basic ingress config for ClientGateways.

            Attributes:
                transport_protocol (google.cloud.beyondcorp_clientconnectorservices_v1.types.ClientConnectorService.Ingress.Config.TransportProtocol):
                    Required. Immutable. The transport protocol
                    used between the client and the server.
                destination_routes (MutableSequence[google.cloud.beyondcorp_clientconnectorservices_v1.types.ClientConnectorService.Ingress.Config.DestinationRoute]):
                    Required. The settings used to configure
                    basic ClientGateways.
            """

            class TransportProtocol(proto.Enum):
                r"""The protocol used to connect to the server.

                Values:
                    TRANSPORT_PROTOCOL_UNSPECIFIED (0):
                        Default value. This value is unused.
                    TCP (1):
                        TCP protocol.
                """

                TRANSPORT_PROTOCOL_UNSPECIFIED = 0
                TCP = 1

            class DestinationRoute(proto.Message):
                r"""The setting used to configure ClientGateways.
                It is adding routes to the client's routing table
                after the connection is established.

                Attributes:
                    address (str):
                        Required. The network address of the subnet
                        for which the packet is routed to the
                        ClientGateway.
                    netmask (str):
                        Required. The network mask of the subnet
                        for which the packet is routed to the
                        ClientGateway.
                """

                address: str = proto.Field(
                    proto.STRING,
                    number=1,
                )
                netmask: str = proto.Field(
                    proto.STRING,
                    number=2,
                )

            transport_protocol: "ClientConnectorService.Ingress.Config.TransportProtocol" = proto.Field(
                proto.ENUM,
                number=1,
                enum="ClientConnectorService.Ingress.Config.TransportProtocol",
            )
            destination_routes: MutableSequence[
                "ClientConnectorService.Ingress.Config.DestinationRoute"
            ] = proto.RepeatedField(
                proto.MESSAGE,
                number=2,
                message="ClientConnectorService.Ingress.Config.DestinationRoute",
            )

        config: "ClientConnectorService.Ingress.Config" = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="ingress_config",
            message="ClientConnectorService.Ingress.Config",
        )

    class Egress(proto.Message):
        r"""The details of the egress info. One of the following options
        should be set.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            peered_vpc (google.cloud.beyondcorp_clientconnectorservices_v1.types.ClientConnectorService.Egress.PeeredVpc):
                A VPC from the consumer project.

                This field is a member of `oneof`_ ``destination_type``.
        """

        class PeeredVpc(proto.Message):
            r"""The peered VPC owned by the consumer project.

            Attributes:
                network_vpc (str):
                    Required. The name of the peered VPC owned by
                    the consumer project.
            """

            network_vpc: str = proto.Field(
                proto.STRING,
                number=1,
            )

        peered_vpc: "ClientConnectorService.Egress.PeeredVpc" = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="destination_type",
            message="ClientConnectorService.Egress.PeeredVpc",
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=4,
    )
    ingress: Ingress = proto.Field(
        proto.MESSAGE,
        number=6,
        message=Ingress,
    )
    egress: Egress = proto.Field(
        proto.MESSAGE,
        number=7,
        message=Egress,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=8,
        enum=State,
    )


class ListClientConnectorServicesRequest(proto.Message):
    r"""Message for requesting list of ClientConnectorServices.

    Attributes:
        parent (str):
            Required. Parent value for
            ListClientConnectorServicesRequest.
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. Filtering results.
        order_by (str):
            Optional. Hint for how to order the results.
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


class ListClientConnectorServicesResponse(proto.Message):
    r"""Message for response to listing ClientConnectorServices.

    Attributes:
        client_connector_services (MutableSequence[google.cloud.beyondcorp_clientconnectorservices_v1.types.ClientConnectorService]):
            The list of ClientConnectorService.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    client_connector_services: MutableSequence["ClientConnectorService"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="ClientConnectorService",
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetClientConnectorServiceRequest(proto.Message):
    r"""Message for getting a ClientConnectorService.

    Attributes:
        name (str):
            Required. Name of the resource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateClientConnectorServiceRequest(proto.Message):
    r"""Message for creating a ClientConnectorService.

    Attributes:
        parent (str):
            Required. Value for parent.
        client_connector_service_id (str):
            Optional. User-settable client connector service resource
            ID.

            - Must start with a letter.
            - Must contain between 4-63 characters from
              ``/[a-z][0-9]-/``.
            - Must end with a number or a letter.

            A random system generated name will be assigned if not
            specified by the user.
        client_connector_service (google.cloud.beyondcorp_clientconnectorservices_v1.types.ClientConnectorService):
            Required. The resource being created.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and t he request times out.
            If you make the request again with the same
            request ID, the server can check if original
            operation with the same request ID was received,
            and if so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        validate_only (bool):
            Optional. If set, validates request by
            executing a dry-run which would not alter the
            resource in any way.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    client_connector_service_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    client_connector_service: "ClientConnectorService" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="ClientConnectorService",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class UpdateClientConnectorServiceRequest(proto.Message):
    r"""Message for updating a ClientConnectorService

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten in the ClientConnectorService resource by the
            update. The fields specified in the update_mask are relative
            to the resource, not the full request. A field will be
            overwritten if it is in the mask. If the user does not
            provide a mask then all fields will be overwritten.

            Mutable fields: display_name.
        client_connector_service (google.cloud.beyondcorp_clientconnectorservices_v1.types.ClientConnectorService):
            Required. The resource being updated.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and t he request times out.
            If you make the request again with the same
            request ID, the server can check if original
            operation with the same request ID was received,
            and if so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        validate_only (bool):
            Optional. If set, validates request by
            executing a dry-run which would not alter the
            resource in any way.
        allow_missing (bool):
            Optional. If set as true, will create the
            resource if it is not found.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    client_connector_service: "ClientConnectorService" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ClientConnectorService",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    allow_missing: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class DeleteClientConnectorServiceRequest(proto.Message):
    r"""Message for deleting a ClientConnectorService.

    Attributes:
        name (str):
            Required. Name of the resource.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes after the first request.

            For example, consider a situation where you make
            an initial request and t he request times out.
            If you make the request again with the same
            request ID, the server can check if original
            operation with the same request ID was received,
            and if so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        validate_only (bool):
            Optional. If set, validates request by
            executing a dry-run which would not alter the
            resource in any way.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class ClientConnectorServiceOperationMetadata(proto.Message):
    r"""Represents the metadata of the long-running operation.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation was
            created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation finished
            running.
        target (str):
            Output only. Server-defined resource path for
            the target of the operation.
        verb (str):
            Output only. Name of the verb executed by the
            operation.
        status_message (str):
            Output only. Human-readable status of the
            operation, if any.
        requested_cancellation (bool):
            Output only. Identifies whether the user has requested
            cancellation of the operation. Operations that have
            successfully been cancelled have [Operation.error][] value
            with a [google.rpc.Status.code][google.rpc.Status.code] of
            1, corresponding to ``Code.CANCELLED``.
        api_version (str):
            Output only. API version used to start the
            operation.
    """

    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    target: str = proto.Field(
        proto.STRING,
        number=3,
    )
    verb: str = proto.Field(
        proto.STRING,
        number=4,
    )
    status_message: str = proto.Field(
        proto.STRING,
        number=5,
    )
    requested_cancellation: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    api_version: str = proto.Field(
        proto.STRING,
        number=7,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
