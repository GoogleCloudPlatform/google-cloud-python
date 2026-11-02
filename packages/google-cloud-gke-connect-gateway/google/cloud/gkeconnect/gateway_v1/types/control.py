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

__protobuf__ = proto.module(
    package="google.cloud.gkeconnect.gateway.v1",
    manifest={
        "GenerateCredentialsRequest",
        "GenerateCredentialsResponse",
    },
)


class GenerateCredentialsRequest(proto.Message):
    r"""A request for connection information for a particular
    membership.

    Attributes:
        name (str):
            Required. The Fleet membership resource.
        force_use_agent (bool):
            Optional. Whether to force the use of Connect
            Agent-based transport.
            This will return a configuration that uses
            Connect Agent as the underlying transport
            mechanism for cluster types that would otherwise
            have used a different transport. Requires that
            Connect Agent be installed on the cluster.
            Setting this field to false is equivalent to not
            setting it.
        version (str):
            Optional. The Connect Gateway version to be
            used in the resulting configuration.

            Leave this field blank to let the server choose
            the version (recommended).
        kubernetes_namespace (str):
            Optional. The namespace to use in the kubeconfig context.

            If this field is specified, the server will set the
            ``namespace`` field in kubeconfig context. If not specified,
            the ``namespace`` field is omitted.
        operating_system (google.cloud.gkeconnect.gateway_v1.types.GenerateCredentialsRequest.OperatingSystem):
            Optional. The operating system where the
            kubeconfig will be used.
    """

    class OperatingSystem(proto.Enum):
        r"""Operating systems requiring specialized kubeconfigs.

        Values:
            OPERATING_SYSTEM_UNSPECIFIED (0):
                Generates a kubeconfig that works for all
                operating systems not defined below.
            OPERATING_SYSTEM_WINDOWS (1):
                Generates a kubeconfig that is specifically
                designed to work with Windows.
        """

        OPERATING_SYSTEM_UNSPECIFIED = 0
        OPERATING_SYSTEM_WINDOWS = 1

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    force_use_agent: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    version: str = proto.Field(
        proto.STRING,
        number=3,
    )
    kubernetes_namespace: str = proto.Field(
        proto.STRING,
        number=4,
    )
    operating_system: OperatingSystem = proto.Field(
        proto.ENUM,
        number=5,
        enum=OperatingSystem,
    )


class GenerateCredentialsResponse(proto.Message):
    r"""Connection information for a particular membership.

    Attributes:
        kubeconfig (bytes):
            A full YAML kubeconfig in serialized format.
        endpoint (str):
            The generated URI of the cluster as accessed
            through the Connect Gateway API.
    """

    kubeconfig: bytes = proto.Field(
        proto.BYTES,
        number=1,
    )
    endpoint: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
