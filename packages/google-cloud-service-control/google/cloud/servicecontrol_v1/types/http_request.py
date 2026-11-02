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
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.api.servicecontrol.v1",
    manifest={
        "HttpRequest",
    },
)


class HttpRequest(proto.Message):
    r"""A common proto for logging HTTP requests. Only contains
    semantics defined by the HTTP specification. Product-specific
    logging information MUST be defined in a separate message.

    Attributes:
        request_method (str):
            The request method. Examples: ``"GET"``, ``"HEAD"``,
            ``"PUT"``, ``"POST"``.
        request_url (str):
            The scheme (http, https), the host name, the path, and the
            query portion of the URL that was requested. Example:
            ``"http://example.com/some/info?color=red"``.
        request_size (int):
            The size of the HTTP request message in
            bytes, including the request headers and the
            request body.
        status (int):
            The response code indicating the status of
            the response. Examples: 200, 404.
        response_size (int):
            The size of the HTTP response message sent
            back to the client, in bytes, including the
            response headers and the response body.
        user_agent (str):
            The user agent sent by the client. Example:
            ``"Mozilla/4.0 (compatible; MSIE 6.0; Windows 98; Q312461; .NET CLR 1.0.3705)"``.
        remote_ip (str):
            The IP address (IPv4 or IPv6) of the client that issued the
            HTTP request. Examples: ``"192.168.1.1"``,
            ``"FE80::0202:B3FF:FE1E:8329"``.
        server_ip (str):
            The IP address (IPv4 or IPv6) of the origin
            server that the request was sent to.
        referer (str):
            The referer URL of the request, as defined in `HTTP/1.1
            Header Field
            Definitions <https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html>`__.
        latency (google.protobuf.duration_pb2.Duration):
            The request processing latency on the server,
            from the time the request was received until the
            response was sent.
        cache_lookup (bool):
            Whether or not a cache lookup was attempted.
        cache_hit (bool):
            Whether or not an entity was served from
            cache (with or without validation).
        cache_validated_with_origin_server (bool):
            Whether or not the response was validated with the origin
            server before being served from cache. This field is only
            meaningful if ``cache_hit`` is True.
        cache_fill_bytes (int):
            The number of HTTP response bytes inserted
            into cache. Set only when a cache fill was
            attempted.
        protocol (str):
            Protocol used for the request. Examples:
            "HTTP/1.1", "HTTP/2", "websocket".
    """

    request_method: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_url: str = proto.Field(
        proto.STRING,
        number=2,
    )
    request_size: int = proto.Field(
        proto.INT64,
        number=3,
    )
    status: int = proto.Field(
        proto.INT32,
        number=4,
    )
    response_size: int = proto.Field(
        proto.INT64,
        number=5,
    )
    user_agent: str = proto.Field(
        proto.STRING,
        number=6,
    )
    remote_ip: str = proto.Field(
        proto.STRING,
        number=7,
    )
    server_ip: str = proto.Field(
        proto.STRING,
        number=13,
    )
    referer: str = proto.Field(
        proto.STRING,
        number=8,
    )
    latency: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=14,
        message=duration_pb2.Duration,
    )
    cache_lookup: bool = proto.Field(
        proto.BOOL,
        number=11,
    )
    cache_hit: bool = proto.Field(
        proto.BOOL,
        number=9,
    )
    cache_validated_with_origin_server: bool = proto.Field(
        proto.BOOL,
        number=10,
    )
    cache_fill_bytes: int = proto.Field(
        proto.INT64,
        number=12,
    )
    protocol: str = proto.Field(
        proto.STRING,
        number=15,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
