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
    package="google.cloud.ids.v1",
    manifest={
        "Endpoint",
        "ListEndpointsRequest",
        "ListEndpointsResponse",
        "GetEndpointRequest",
        "CreateEndpointRequest",
        "DeleteEndpointRequest",
        "OperationMetadata",
    },
)


class Endpoint(proto.Message):
    r"""Endpoint describes a single IDS endpoint. It defines a
    forwarding rule to which packets can be sent for IDS inspection.

    Attributes:
        name (str):
            Output only. The name of the endpoint.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The create time timestamp.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The update time timestamp.
        labels (MutableMapping[str, str]):
            The labels of the endpoint.
        network (str):
            Required. The fully qualified URL of the
            network to which the IDS Endpoint is attached.
        endpoint_forwarding_rule (str):
            Output only. The fully qualified URL of the
            endpoint's ILB Forwarding Rule.
        endpoint_ip (str):
            Output only. The IP address of the IDS
            Endpoint's ILB.
        description (str):
            User-provided description of the endpoint
        severity (google.cloud.ids_v1.types.Endpoint.Severity):
            Required. Lowest threat severity that this
            endpoint will alert on.
        state (google.cloud.ids_v1.types.Endpoint.State):
            Output only. Current state of the endpoint.
        traffic_logs (bool):
            Whether the endpoint should report traffic
            logs in addition to threat logs.
    """

    class Severity(proto.Enum):
        r"""Threat severity levels.

        Values:
            SEVERITY_UNSPECIFIED (0):
                Not set.
            INFORMATIONAL (1):
                Informational alerts.
            LOW (2):
                Low severity alerts.
            MEDIUM (3):
                Medium severity alerts.
            HIGH (4):
                High severity alerts.
            CRITICAL (5):
                Critical severity alerts.
        """

        SEVERITY_UNSPECIFIED = 0
        INFORMATIONAL = 1
        LOW = 2
        MEDIUM = 3
        HIGH = 4
        CRITICAL = 5

    class State(proto.Enum):
        r"""Endpoint state

        Values:
            STATE_UNSPECIFIED (0):
                Not set.
            CREATING (1):
                Being created.
            READY (2):
                Active and ready for traffic.
            DELETING (3):
                Being deleted.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        READY = 2
        DELETING = 3

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
    network: str = proto.Field(
        proto.STRING,
        number=5,
    )
    endpoint_forwarding_rule: str = proto.Field(
        proto.STRING,
        number=6,
    )
    endpoint_ip: str = proto.Field(
        proto.STRING,
        number=7,
    )
    description: str = proto.Field(
        proto.STRING,
        number=8,
    )
    severity: Severity = proto.Field(
        proto.ENUM,
        number=9,
        enum=Severity,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=12,
        enum=State,
    )
    traffic_logs: bool = proto.Field(
        proto.BOOL,
        number=13,
    )


class ListEndpointsRequest(proto.Message):
    r"""

    Attributes:
        parent (str):
            Required. The parent, which owns this
            collection of endpoints.
        page_size (int):
            Optional. The maximum number of endpoints to
            return. The service may return fewer than this
            value.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListEndpoints`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListEndpoints`` must match the call that provided the page
            token.
        filter (str):
            Optional. The filter expression, following
            the syntax outlined in
            https://google.aip.dev/160.
        order_by (str):
            Optional. One or more fields to compare and
            use to sort the output. See
            https://google.aip.dev/132#ordering.
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


class ListEndpointsResponse(proto.Message):
    r"""

    Attributes:
        endpoints (MutableSequence[google.cloud.ids_v1.types.Endpoint]):
            The list of endpoints response.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    endpoints: MutableSequence["Endpoint"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Endpoint",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetEndpointRequest(proto.Message):
    r"""

    Attributes:
        name (str):
            Required. The name of the endpoint to retrieve. Format:
            ``projects/{project}/locations/{location}/endpoints/{endpoint}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateEndpointRequest(proto.Message):
    r"""

    Attributes:
        parent (str):
            Required. The endpoint's parent.
        endpoint_id (str):
            Required. The endpoint identifier. This will be part of the
            endpoint's resource name. This value must start with a
            lowercase letter followed by up to 62 lowercase letters,
            numbers, or hyphens, and cannot end with a hyphen. Values
            that do not match this pattern will trigger an
            INVALID_ARGUMENT error.
        endpoint (google.cloud.ids_v1.types.Endpoint):
            Required. The endpoint to create.
        request_id (str):
            An optional request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server will guarantee that for at
            least 60 minutes since the first request.

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
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    endpoint_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    endpoint: "Endpoint" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Endpoint",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class DeleteEndpointRequest(proto.Message):
    r"""

    Attributes:
        name (str):
            Required. The name of the endpoint to delete.
        request_id (str):
            An optional request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server will guarantee that for at
            least 60 minutes after the first request.

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
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class OperationMetadata(proto.Message):
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
