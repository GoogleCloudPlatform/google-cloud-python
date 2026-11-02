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

from google.cloud.servicedirectory_v1beta1.types import endpoint

__protobuf__ = proto.module(
    package="google.cloud.servicedirectory.v1beta1",
    manifest={
        "Service",
    },
)


class Service(proto.Message):
    r"""An individual service. A service contains a name and optional
    metadata. A service must exist before
    [endpoints][google.cloud.servicedirectory.v1beta1.Endpoint] can be
    added to it.

    Attributes:
        name (str):
            Immutable. The resource name for the service in the format
            ``projects/*/locations/*/namespaces/*/services/*``.
        metadata (MutableMapping[str, str]):
            Optional. Metadata for the service. This data can be
            consumed by service clients.

            Restrictions:

            - The entire metadata dictionary may contain up to 2000
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
        endpoints (MutableSequence[google.cloud.servicedirectory_v1beta1.types.Endpoint]):
            Output only. Endpoints associated with this service.
            Returned on
            [LookupService.ResolveService][google.cloud.servicedirectory.v1beta1.LookupService.ResolveService].
            Control plane clients should use
            [RegistrationService.ListEndpoints][google.cloud.servicedirectory.v1beta1.RegistrationService.ListEndpoints].
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the service
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the service
            was last updated. Note: endpoints being
            created/deleted/updated within the service are
            not considered service updates for the purpose
            of this timestamp.
        uid (str):
            Output only. A globally unique identifier (in
            UUID4 format) for this service.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    metadata: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=2,
    )
    endpoints: MutableSequence[endpoint.Endpoint] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=endpoint.Endpoint,
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
