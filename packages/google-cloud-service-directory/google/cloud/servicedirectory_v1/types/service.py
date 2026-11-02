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

import proto  # type: ignore

from google.cloud.servicedirectory_v1.types import endpoint

__protobuf__ = proto.module(
    package="google.cloud.servicedirectory.v1",
    manifest={
        "Service",
    },
)


class Service(proto.Message):
    r"""An individual service. A service contains a name and optional
    metadata. A service must exist before
    [endpoints][google.cloud.servicedirectory.v1.Endpoint] can be added
    to it.

    Attributes:
        name (str):
            Immutable. The resource name for the service in the format
            ``projects/*/locations/*/namespaces/*/services/*``.
        annotations (MutableMapping[str, str]):
            Optional. Annotations for the service. This data can be
            consumed by service clients.

            Restrictions:

            - The entire annotations dictionary may contain up to 2000
              characters, spread accoss all key-value pairs. Annotations
              that go beyond this limit are rejected
            - Valid annotation keys have two segments: an optional
              prefix and name, separated by a slash (/). The name
              segment is required and must be 63 characters or less,
              beginning and ending with an alphanumeric character
              ([a-z0-9A-Z]) with dashes (-), underscores (\_), dots (.),
              and alphanumerics between. The prefix is optional. If
              specified, the prefix must be a DNS subdomain: a series of
              DNS labels separated by dots (.), not longer than 253
              characters in total, followed by a slash (/). Annotations
              that fails to meet these requirements are rejected

            Note: This field is equivalent to the ``metadata`` field in
            the v1beta1 API. They have the same syntax and read/write to
            the same location in Service Directory.
        endpoints (MutableSequence[google.cloud.servicedirectory_v1.types.Endpoint]):
            Output only. Endpoints associated with this service.
            Returned on
            [LookupService.ResolveService][google.cloud.servicedirectory.v1.LookupService.ResolveService].
            Control plane clients should use
            [RegistrationService.ListEndpoints][google.cloud.servicedirectory.v1.RegistrationService.ListEndpoints].
        uid (str):
            Output only. The globally unique identifier
            of the service in the UUID4 format.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    endpoints: MutableSequence[endpoint.Endpoint] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=endpoint.Endpoint,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=7,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
