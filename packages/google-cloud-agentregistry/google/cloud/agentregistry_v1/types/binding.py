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
    package="google.cloud.agentregistry.v1",
    manifest={
        "Binding",
    },
)


class Binding(proto.Message):
    r"""Represents a user-defined Binding.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        auth_provider_binding (google.cloud.agentregistry_v1.types.Binding.AuthProviderBinding):
            The binding for AuthProvider.

            This field is a member of `oneof`_ ``binding``.
        name (str):
            Required. Identifier. The resource name of the Binding.
            Format:
            ``projects/{project}/locations/{location}/bindings/{binding}``.
        display_name (str):
            Optional. User-defined display name for the Binding. Can
            have a maximum length of ``63`` characters.
        description (str):
            Optional. User-defined description of a Binding. Can have a
            maximum length of ``2048`` characters.
        source (google.cloud.agentregistry_v1.types.Binding.Source):
            Optional. The source Agent of the Binding.
        target (google.cloud.agentregistry_v1.types.Binding.Target):
            Required. The target Agent Registry Resource
            of the Binding.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when this binding was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when this binding was
            last updated.
    """

    class Source(proto.Message):
        r"""The source of the Binding.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            identifier (str):
                The identifier of the source Agent. Format:

                - ``urn:agent:{publisher}:{namespace}:{name}``

                This field is a member of `oneof`_ ``source_type``.
        """

        identifier: str = proto.Field(
            proto.STRING,
            number=1,
            oneof="source_type",
        )

    class Target(proto.Message):
        r"""The target of the Binding.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            identifier (str):
                The identifier of the target Agent, MCP Server, or Endpoint.
                Format:

                - ``urn:agent:{publisher}:{namespace}:{name}``
                - ``urn:mcp:{publisher}:{namespace}:{name}``
                - ``urn:endpoint:{publisher}:{namespace}:{name}``

                This field is a member of `oneof`_ ``target_type``.
        """

        identifier: str = proto.Field(
            proto.STRING,
            number=1,
            oneof="target_type",
        )

    class AuthProviderBinding(proto.Message):
        r"""The AuthProvider of the Binding.

        Attributes:
            auth_provider (str):
                Required. The resource name of the target AuthProvider.
                Format:

                - ``projects/{project}/locations/{location}/authProviders/{auth_provider}``
            scopes (MutableSequence[str]):
                Optional. The list of OAuth2 scopes of the
                AuthProvider.
            continue_uri (str):
                Optional. The continue URI of the
                AuthProvider. The URI is used to reauthenticate
                the user and finalize the managed OAuth flow.
        """

        auth_provider: str = proto.Field(
            proto.STRING,
            number=1,
        )
        scopes: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )
        continue_uri: str = proto.Field(
            proto.STRING,
            number=3,
        )

    auth_provider_binding: AuthProviderBinding = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="binding",
        message=AuthProviderBinding,
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    source: Source = proto.Field(
        proto.MESSAGE,
        number=4,
        message=Source,
    )
    target: Target = proto.Field(
        proto.MESSAGE,
        number=5,
        message=Target,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
