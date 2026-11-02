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

from google.cloud.ces_v1beta.types import auth, common

__protobuf__ = proto.module(
    package="google.cloud.ces.v1beta",
    manifest={
        "OpenApiToolset",
    },
)


class OpenApiToolset(proto.Message):
    r"""A toolset that contains a list of tools that are defined by
    an OpenAPI schema.

    Attributes:
        open_api_schema (str):
            Required. The OpenAPI schema of the toolset.
        api_authentication (google.cloud.ces_v1beta.types.ApiAuthentication):
            Optional. Authentication information required
            by the API.
        tls_config (google.cloud.ces_v1beta.types.TlsConfig):
            Optional. The TLS configuration. Includes the
            custom server certificates
        service_directory_config (google.cloud.ces_v1beta.types.ServiceDirectoryConfig):
            Optional. Service Directory configuration.
        ignore_unknown_fields_ (bool):
            Optional. If true, the agent will ignore
            unknown fields in the API response for all
            operations defined in the OpenAPI schema.
        url (str):
            Optional. The server URL of the Open API schema. This field
            is only set in toolsets in the environment dependencies
            during the export process if the schema contains a server
            url. During the import process, if this url is present in
            the environment dependencies and the schema has the $env_var
            placeholder, it will replace the placeholder in the schema.
    """

    open_api_schema: str = proto.Field(
        proto.STRING,
        number=1,
    )
    api_authentication: auth.ApiAuthentication = proto.Field(
        proto.MESSAGE,
        number=2,
        message=auth.ApiAuthentication,
    )
    tls_config: common.TlsConfig = proto.Field(
        proto.MESSAGE,
        number=3,
        message=common.TlsConfig,
    )
    service_directory_config: common.ServiceDirectoryConfig = proto.Field(
        proto.MESSAGE,
        number=4,
        message=common.ServiceDirectoryConfig,
    )
    ignore_unknown_fields_: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    url: str = proto.Field(
        proto.STRING,
        number=6,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
