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
    package="google.cloud.beyondcorp.appgateways.v1",
    manifest={
        "ListAppGatewaysRequest",
        "ListAppGatewaysResponse",
        "GetAppGatewayRequest",
        "CreateAppGatewayRequest",
        "DeleteAppGatewayRequest",
        "AppGateway",
        "AppGatewayOperationMetadata",
    },
)


class ListAppGatewaysRequest(proto.Message):
    r"""Request message for BeyondCorp.ListAppGateways.

    Attributes:
        parent (str):
            Required. The resource name of the AppGateway location using
            the form: ``projects/{project_id}/locations/{location_id}``
        page_size (int):
            Optional. The maximum number of items to return. If not
            specified, a default value of 50 will be used by the
            service. Regardless of the page_size value, the response may
            include a partial list and a caller should only rely on
            response's
            [next_page_token][google.cloud.beyondcorp.appgateways.v1.ListAppGatewaysResponse.next_page_token]
            to determine if there are more instances left to be queried.
        page_token (str):
            Optional. The next_page_token value returned from a previous
            ListAppGatewaysRequest, if any.
        filter (str):
            Optional. A filter specifying constraints of
            a list operation.
        order_by (str):
            Optional. Specifies the ordering of results. See `Sorting
            order <https://cloud.google.com/apis/design/design_patterns#sorting_order>`__
            for more information.
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


class ListAppGatewaysResponse(proto.Message):
    r"""Response message for BeyondCorp.ListAppGateways.

    Attributes:
        app_gateways (MutableSequence[google.cloud.beyondcorp_appgateways_v1.types.AppGateway]):
            A list of BeyondCorp AppGateways in the
            project.
        next_page_token (str):
            A token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
        unreachable (MutableSequence[str]):
            A list of locations that could not be
            reached.
    """

    @property
    def raw_page(self):
        return self

    app_gateways: MutableSequence["AppGateway"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="AppGateway",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetAppGatewayRequest(proto.Message):
    r"""Request message for BeyondCorp.GetAppGateway.

    Attributes:
        name (str):
            Required. BeyondCorp AppGateway name using the form:
            ``projects/{project_id}/locations/{location_id}/appGateways/{app_gateway_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateAppGatewayRequest(proto.Message):
    r"""Request message for BeyondCorp.CreateAppGateway.

    Attributes:
        parent (str):
            Required. The resource project name of the AppGateway
            location using the form:
            ``projects/{project_id}/locations/{location_id}``
        app_gateway_id (str):
            Optional. User-settable AppGateway resource ID.

            - Must start with a letter.
            - Must contain between 4-63 characters from
              ``/[a-z][0-9]-/``.
            - Must end with a number or a letter.
        app_gateway (google.cloud.beyondcorp_appgateways_v1.types.AppGateway):
            Required. A BeyondCorp AppGateway resource.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
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
    app_gateway_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    app_gateway: "AppGateway" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="AppGateway",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class DeleteAppGatewayRequest(proto.Message):
    r"""Request message for BeyondCorp.DeleteAppGateway.

    Attributes:
        name (str):
            Required. BeyondCorp AppGateway name using the form:
            ``projects/{project_id}/locations/{location_id}/appGateways/{app_gateway_id}``
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes after the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
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


class AppGateway(proto.Message):
    r"""A BeyondCorp AppGateway resource represents a BeyondCorp
    protected AppGateway to a remote application. It creates all the
    necessary GCP components needed for creating a BeyondCorp
    protected AppGateway. Multiple connectors can be authorised for
    a single AppGateway.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Required. Unique resource name of the
            AppGateway. The name is ignored when creating an
            AppGateway.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the resource was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the resource was
            last modified.
        labels (MutableMapping[str, str]):
            Optional. Resource labels to represent user
            provided metadata.
        display_name (str):
            Optional. An arbitrary user-provided name for
            the AppGateway. Cannot exceed 64 characters.
        uid (str):
            Output only. A unique identifier for the
            instance generated by the system.
        type_ (google.cloud.beyondcorp_appgateways_v1.types.AppGateway.Type):
            Required. The type of network connectivity
            used by the AppGateway.
        state (google.cloud.beyondcorp_appgateways_v1.types.AppGateway.State):
            Output only. The current state of the
            AppGateway.
        uri (str):
            Output only. Server-defined URI for this
            resource.
        allocated_connections (MutableSequence[google.cloud.beyondcorp_appgateways_v1.types.AppGateway.AllocatedConnection]):
            Output only. A list of connections allocated
            for the Gateway
        host_type (google.cloud.beyondcorp_appgateways_v1.types.AppGateway.HostType):
            Required. The type of hosting used by the
            AppGateway.
        satisfies_pzs (bool):
            Output only. Reserved for future use.

            This field is a member of `oneof`_ ``_satisfies_pzs``.
        satisfies_pzi (bool):
            Output only. Reserved for future use.

            This field is a member of `oneof`_ ``_satisfies_pzi``.
    """

    class Type(proto.Enum):
        r"""Enum containing list of all possible network connectivity
        options supported by BeyondCorp AppGateway.

        Values:
            TYPE_UNSPECIFIED (0):
                Default value. This value is unused.
            TCP_PROXY (1):
                TCP Proxy based BeyondCorp Connection. API
                will default to this if unset.
        """

        TYPE_UNSPECIFIED = 0
        TCP_PROXY = 1

    class State(proto.Enum):
        r"""Represents the different states of an AppGateway.

        Values:
            STATE_UNSPECIFIED (0):
                Default value. This value is unused.
            CREATING (1):
                AppGateway is being created.
            CREATED (2):
                AppGateway has been created.
            UPDATING (3):
                AppGateway's configuration is being updated.
            DELETING (4):
                AppGateway is being deleted.
            DOWN (5):
                AppGateway is down and may be restored in the
                future. This happens when CCFE sends
                ProjectState = OFF.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        CREATED = 2
        UPDATING = 3
        DELETING = 4
        DOWN = 5

    class HostType(proto.Enum):
        r"""Enum containing list of all possible host types supported by
        BeyondCorp Connection.

        Values:
            HOST_TYPE_UNSPECIFIED (0):
                Default value. This value is unused.
            GCP_REGIONAL_MIG (1):
                AppGateway hosted in a GCP regional managed
                instance group.
        """

        HOST_TYPE_UNSPECIFIED = 0
        GCP_REGIONAL_MIG = 1

    class AllocatedConnection(proto.Message):
        r"""Allocated connection of the AppGateway.

        Attributes:
            psc_uri (str):
                Required. The PSC uri of an allocated
                connection
            ingress_port (int):
                Required. The ingress port of an allocated
                connection
        """

        psc_uri: str = proto.Field(
            proto.STRING,
            number=1,
        )
        ingress_port: int = proto.Field(
            proto.INT32,
            number=2,
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
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=5,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=6,
    )
    type_: Type = proto.Field(
        proto.ENUM,
        number=7,
        enum=Type,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=8,
        enum=State,
    )
    uri: str = proto.Field(
        proto.STRING,
        number=9,
    )
    allocated_connections: MutableSequence[AllocatedConnection] = proto.RepeatedField(
        proto.MESSAGE,
        number=10,
        message=AllocatedConnection,
    )
    host_type: HostType = proto.Field(
        proto.ENUM,
        number=11,
        enum=HostType,
    )
    satisfies_pzs: bool = proto.Field(
        proto.BOOL,
        number=12,
        optional=True,
    )
    satisfies_pzi: bool = proto.Field(
        proto.BOOL,
        number=13,
        optional=True,
    )


class AppGatewayOperationMetadata(proto.Message):
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
            successfully been cancelled have
            [google.longrunning.Operation.error][google.longrunning.Operation.error]
            value with a
            [google.rpc.Status.code][google.rpc.Status.code] of ``1``,
            corresponding to ``Code.CANCELLED``.
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
