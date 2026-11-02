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

from google.cloud.apihub_v1.types import common_fields

__protobuf__ = proto.module(
    package="google.cloud.apihub.v1",
    manifest={
        "CreateApiHubInstanceRequest",
        "DeleteApiHubInstanceRequest",
        "GetApiHubInstanceRequest",
        "LookupApiHubInstanceRequest",
        "LookupApiHubInstanceResponse",
    },
)


class CreateApiHubInstanceRequest(proto.Message):
    r"""The
    [CreateApiHubInstance][google.cloud.apihub.v1.Provisioning.CreateApiHubInstance]
    method's request.

    Attributes:
        parent (str):
            Required. The parent resource for the Api Hub instance
            resource. Format:
            ``projects/{project}/locations/{location}``
        api_hub_instance_id (str):
            Optional. Identifier to assign to the Api Hub instance. Must
            be unique within scope of the parent resource. If the field
            is not provided, system generated id will be used.

            This value should be 4-40 characters, and valid characters
            are ``/[a-z][A-Z][0-9]-_/``.
        api_hub_instance (google.cloud.apihub_v1.types.ApiHubInstance):
            Required. The ApiHub instance.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    api_hub_instance_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    api_hub_instance: common_fields.ApiHubInstance = proto.Field(
        proto.MESSAGE,
        number=3,
        message=common_fields.ApiHubInstance,
    )


class DeleteApiHubInstanceRequest(proto.Message):
    r"""The
    [DeleteApiHubInstance][google.cloud.apihub.v1.Provisioning.DeleteApiHubInstance]
    method's request.

    Attributes:
        name (str):
            Required. The name of the Api Hub instance to delete.
            Format:
            ``projects/{project}/locations/{location}/apiHubInstances/{apiHubInstance}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetApiHubInstanceRequest(proto.Message):
    r"""The
    [GetApiHubInstance][google.cloud.apihub.v1.Provisioning.GetApiHubInstance]
    method's request.

    Attributes:
        name (str):
            Required. The name of the Api Hub instance to retrieve.
            Format:
            ``projects/{project}/locations/{location}/apiHubInstances/{apiHubInstance}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class LookupApiHubInstanceRequest(proto.Message):
    r"""The
    [LookupApiHubInstance][google.cloud.apihub.v1.Provisioning.LookupApiHubInstance]
    method's request.

    Attributes:
        parent (str):
            Required. There will always be only one Api Hub instance for
            a GCP project across all locations. The parent resource for
            the Api Hub instance resource. Format:
            ``projects/{project}/locations/{location}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )


class LookupApiHubInstanceResponse(proto.Message):
    r"""The
    [LookupApiHubInstance][google.cloud.apihub.v1.Provisioning.LookupApiHubInstance]
    method's response.\`

    Attributes:
        api_hub_instance (google.cloud.apihub_v1.types.ApiHubInstance):
            API Hub instance for a project if it exists,
            empty otherwise.
    """

    api_hub_instance: common_fields.ApiHubInstance = proto.Field(
        proto.MESSAGE,
        number=1,
        message=common_fields.ApiHubInstance,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
