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
import google.rpc.status_pb2 as status_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.apigeeconnect.v1",
    manifest={
        "Action",
        "TetherEndpoint",
        "Scheme",
        "EgressRequest",
        "Payload",
        "StreamInfo",
        "EgressResponse",
        "HttpRequest",
        "Url",
        "Header",
        "HttpResponse",
    },
)


class Action(proto.Enum):
    r"""The action taken by agent.

    Values:
        ACTION_UNSPECIFIED (0):
            Unspecified Action.
        OPEN_NEW_STREAM (1):
            Indicates that agent should open a new
            stream.
    """

    ACTION_UNSPECIFIED = 0
    OPEN_NEW_STREAM = 1


class TetherEndpoint(proto.Enum):
    r"""Endpoint indicates where the messages will be delivered.

    Values:
        TETHER_ENDPOINT_UNSPECIFIED (0):
            Unspecified tether endpoint.
        APIGEE_MART (1):
            Apigee MART endpoint.
        APIGEE_RUNTIME (2):
            Apigee Runtime endpoint.
        APIGEE_MINT_RATING (3):
            Apigee Mint Rating endpoint.
    """

    TETHER_ENDPOINT_UNSPECIFIED = 0
    APIGEE_MART = 1
    APIGEE_RUNTIME = 2
    APIGEE_MINT_RATING = 3


class Scheme(proto.Enum):
    r"""HTTP Scheme.

    Values:
        SCHEME_UNSPECIFIED (0):
            Unspecified scheme.
        HTTPS (1):
            HTTPS protocol.
    """

    SCHEME_UNSPECIFIED = 0
    HTTPS = 1


class EgressRequest(proto.Message):
    r"""gRPC request payload for tether.

    Attributes:
        id (str):
            Unique identifier for the request.
        payload (google.cloud.apigeeconnect_v1.types.Payload):
            Actual payload to send to agent.
        endpoint (google.cloud.apigeeconnect_v1.types.TetherEndpoint):
            Tether Endpoint.
        project (str):
            GCP Project. Format: ``projects/{project_number}``.
        trace_id (str):
            Unique identifier for clients to trace their
            request/response.
        timeout (google.protobuf.duration_pb2.Duration):
            Timeout for the HTTP request.
    """

    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    payload: "Payload" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Payload",
    )
    endpoint: "TetherEndpoint" = proto.Field(
        proto.ENUM,
        number=3,
        enum="TetherEndpoint",
    )
    project: str = proto.Field(
        proto.STRING,
        number=4,
    )
    trace_id: str = proto.Field(
        proto.STRING,
        number=5,
    )
    timeout: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=6,
        message=duration_pb2.Duration,
    )


class Payload(proto.Message):
    r"""Payload for EgressRequest.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        http_request (google.cloud.apigeeconnect_v1.types.HttpRequest):
            The HttpRequest proto.

            This field is a member of `oneof`_ ``kind``.
        stream_info (google.cloud.apigeeconnect_v1.types.StreamInfo):
            The information of stream.

            This field is a member of `oneof`_ ``kind``.
        action (google.cloud.apigeeconnect_v1.types.Action):
            The action taken by agent.

            This field is a member of `oneof`_ ``kind``.
    """

    http_request: "HttpRequest" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="kind",
        message="HttpRequest",
    )
    stream_info: "StreamInfo" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="kind",
        message="StreamInfo",
    )
    action: "Action" = proto.Field(
        proto.ENUM,
        number=3,
        oneof="kind",
        enum="Action",
    )


class StreamInfo(proto.Message):
    r"""The Information of bi-directional stream.

    Attributes:
        id (str):
            Unique identifier for the stream.
    """

    id: str = proto.Field(
        proto.STRING,
        number=1,
    )


class EgressResponse(proto.Message):
    r"""gRPC response payload for tether.

    Attributes:
        id (str):
            Unique identifier for the response. Matches
            the EgressRequest's id.
        http_response (google.cloud.apigeeconnect_v1.types.HttpResponse):
            HttpResponse.
        status (google.rpc.status_pb2.Status):
            Errors from application when handling the
            http request.
        project (str):
            GCP Project. Format: ``projects/{project_number}``.
        trace_id (str):
            Unique identifier for clients to trace their
            request/response. Matches the EgressRequest's
            trace id
        endpoint (google.cloud.apigeeconnect_v1.types.TetherEndpoint):
            Tether Endpoint.
        name (str):
            Name is the full resource path of endpoint. Format:
            ``projects/{project_number or project_id}/endpoints/{endpoint}``
    """

    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    http_response: "HttpResponse" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="HttpResponse",
    )
    status: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=3,
        message=status_pb2.Status,
    )
    project: str = proto.Field(
        proto.STRING,
        number=4,
    )
    trace_id: str = proto.Field(
        proto.STRING,
        number=5,
    )
    endpoint: "TetherEndpoint" = proto.Field(
        proto.ENUM,
        number=6,
        enum="TetherEndpoint",
    )
    name: str = proto.Field(
        proto.STRING,
        number=7,
    )


class HttpRequest(proto.Message):
    r"""The proto definition of http request.

    Attributes:
        id (str):
            A unique identifier for the request.
        method (str):
            The HTTP request method.
            Valid methods: "GET", "HEAD", "POST", "PUT",
            "PATCH","DELETE".
        url (google.cloud.apigeeconnect_v1.types.Url):
            The HTTP request URL.
        headers (MutableSequence[google.cloud.apigeeconnect_v1.types.Header]):
            The HTTP request headers.
        body (bytes):
            HTTP request body.
    """

    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    method: str = proto.Field(
        proto.STRING,
        number=2,
    )
    url: "Url" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Url",
    )
    headers: MutableSequence["Header"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="Header",
    )
    body: bytes = proto.Field(
        proto.BYTES,
        number=5,
    )


class Url(proto.Message):
    r"""The proto definition of url. A url represents a URL and the general
    form represented is:

    ``[scheme://][google.cloud.apigeeconnect.v1.Url.host][path]``

    Attributes:
        scheme (google.cloud.apigeeconnect_v1.types.Scheme):
            Scheme.
        host (str):
            Host or Host:Port.
        path (str):
            Path starts with ``/``.
    """

    scheme: "Scheme" = proto.Field(
        proto.ENUM,
        number=1,
        enum="Scheme",
    )
    host: str = proto.Field(
        proto.STRING,
        number=2,
    )
    path: str = proto.Field(
        proto.STRING,
        number=3,
    )


class Header(proto.Message):
    r"""The http headers.

    Attributes:
        key (str):

        values (MutableSequence[str]):

    """

    key: str = proto.Field(
        proto.STRING,
        number=1,
    )
    values: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class HttpResponse(proto.Message):
    r"""The proto definition of http response.

    Attributes:
        id (str):
            A unique identifier that matches the request
            ID.
        status (str):
            Status of http response, e.g. "200 OK".
        status_code (int):
            Status code of http response, e.g. 200.
        body (bytes):
            The HTTP 1.1 response body.
        headers (MutableSequence[google.cloud.apigeeconnect_v1.types.Header]):
            The HTTP response headers.
        content_length (int):
            Content length records the length of the
            associated content. The value -1 indicates that
            the length is unknown. Unless http method is
            "HEAD", values >= 0 indicate that the given
            number of bytes may be read from Body.
    """

    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    status: str = proto.Field(
        proto.STRING,
        number=2,
    )
    status_code: int = proto.Field(
        proto.INT32,
        number=3,
    )
    body: bytes = proto.Field(
        proto.BYTES,
        number=4,
    )
    headers: MutableSequence["Header"] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message="Header",
    )
    content_length: int = proto.Field(
        proto.INT64,
        number=6,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
