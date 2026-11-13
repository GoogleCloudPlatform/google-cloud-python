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

import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.apphub.v1",
    manifest={
        "FunctionalType",
        "RegistrationType",
        "ExtendedMetadata",
        "Identity",
    },
)


class FunctionalType(proto.Message):
    r"""The functional type of a service or workload.

    Attributes:
        type_ (google.cloud.apphub_v1.types.FunctionalType.Type):
            Output only. The functional type of a service
            or workload.
    """

    class Type(proto.Enum):
        r"""The functional type of a service or workload.

        Values:
            TYPE_UNSPECIFIED (0):
                Unspecified type.
            AGENT (1):
                Agent type.
            MCP_SERVER (2):
                MCP Server type.
            ENDPOINT (3):
                Endpoint type.
        """

        TYPE_UNSPECIFIED = 0
        AGENT = 1
        MCP_SERVER = 2
        ENDPOINT = 3

    type_: Type = proto.Field(
        proto.ENUM,
        number=1,
        enum=Type,
    )


class RegistrationType(proto.Message):
    r"""The registration type of a service.

    Attributes:
        type_ (google.cloud.apphub_v1.types.RegistrationType.Type):
            Output only. The registration type of a
            service.
    """

    class Type(proto.Enum):
        r"""The registration type of a service.

        Values:
            TYPE_UNSPECIFIED (0):
                Unspecified registration type. Defaults to
                EXCLUSIVE.
            EXCLUSIVE (1):
                The service can only be registered to one
                application.
            SHARED (2):
                The service can be registered to multiple
                applications.
        """

        TYPE_UNSPECIFIED = 0
        EXCLUSIVE = 1
        SHARED = 2

    type_: Type = proto.Field(
        proto.ENUM,
        number=1,
        enum=Type,
    )


class ExtendedMetadata(proto.Message):
    r"""Additional metadata for a Service or Workload.

    Attributes:
        metadata_struct (google.protobuf.struct_pb2.Struct):
            Output only. The metadata contents.
    """

    metadata_struct: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=1,
        message=struct_pb2.Struct,
    )


class Identity(proto.Message):
    r"""The identity associated with a service or workload.

    Attributes:
        principal (str):
            Output only. The principal of the identity.

            Supported formats:

            - ``sa://my-sa@PROJECT_ID.iam.gserviceaccount.com`` for GCP
              Service Account
            - ``principal://POOL_ID.global.PROJECT_NUMBER.workload.id.goog/ns/NAMESPACE_ID/sa/MANAGED_IDENTITY_ID``
              for Managed Workload Identity
    """

    principal: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
