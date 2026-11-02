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
    package="google.cloud.servicedirectory.v1beta1",
    manifest={
        "Endpoint",
    },
)


class Endpoint(proto.Message):
    r"""An individual endpoint that provides a
    [service][google.cloud.servicedirectory.v1beta1.Service]. The
    service must already exist to create an endpoint.

    Attributes:
        name (str):
            Immutable. The resource name for the endpoint in the format
            ``projects/*/locations/*/namespaces/*/services/*/endpoints/*``.
        address (str):
            Optional. An IPv4 or IPv6 address. Service Directory rejects
            bad addresses like:

            - ``8.8.8``
            - ``8.8.8.8:53``
            - ``test:bad:address``
            - ``[::1]``
            - ``[::1]:8080``

            Limited to 45 characters.
        port (int):
            Optional. Service Directory rejects values outside of
            ``[0, 65535]``.
        metadata (MutableMapping[str, str]):
            Optional. Metadata for the endpoint. This data can be
            consumed by service clients.

            Restrictions:

            - The entire metadata dictionary may contain up to 512
              characters, spread accoss all key-value pairs. Metadata
              that goes beyond this limit are rejected
            - Valid metadata keys have two segments: an optional prefix
              and name, separated by a slash (/). The name segment is
              required and must be 63 characters or less, beginning and
              ending with an alphanumeric character ([a-z0-9A-Z]) with
              dashes (-), underscores (\_), dots (.), and alphanumerics
              between. The prefix is optional. If specified, the prefix
              must be a DNS subdomain: a series of DNS labels separated
              by dots (.), not longer than 253 characters in total,
              followed by a slash (/). Metadata that fails to meet these
              requirements are rejected

            Note: This field is equivalent to the ``annotations`` field
            in the v1 API. They have the same syntax and read/write to
            the same location in Service Directory.
        network (str):
            Immutable. The Google Compute Engine network (VPC) of the
            endpoint in the format
            ``projects/<project number>/locations/global/networks/*``.

            The project must be specified by project number (project id
            is rejected). Incorrectly formatted networks are rejected,
            but no other validation is performed on this field (ex.
            network or project existence, reachability, or permissions).
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the endpoint
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the endpoint
            was last updated.
        uid (str):
            Output only. A globally unique identifier (in
            UUID4 format) for this endpoint.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    address: str = proto.Field(
        proto.STRING,
        number=2,
    )
    port: int = proto.Field(
        proto.INT32,
        number=3,
    )
    metadata: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    network: str = proto.Field(
        proto.STRING,
        number=5,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=8,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
