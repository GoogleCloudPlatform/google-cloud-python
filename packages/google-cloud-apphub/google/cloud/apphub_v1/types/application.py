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

from google.cloud.apphub_v1.types import attributes as gca_attributes
from google.cloud.apphub_v1.types import properties

__protobuf__ = proto.module(
    package="google.cloud.apphub.v1",
    manifest={
        "Application",
        "ApplicationType",
        "Scope",
        "ApplicationProperties",
    },
)


class Application(proto.Message):
    r"""Application defines the governance boundary for App Hub
    entities that perform a logical end-to-end business function.
    App Hub supports application level IAM permission to align with
    governance requirements.

    Attributes:
        name (str):
            Identifier. The resource name of an Application. Format:
            ``"projects/{host-project-id}/locations/{location}/applications/{application-id}"``
        display_name (str):
            Optional. User-defined name for the
            Application. Can have a maximum length of 63
            characters.
        description (str):
            Optional. User-defined description of an
            Application. Can have a maximum length of 2048
            characters.
        attributes (google.cloud.apphub_v1.types.Attributes):
            Optional. Consumer provided attributes.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Create time.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Update time.
        scope (google.cloud.apphub_v1.types.Scope):
            Required. Immutable. Defines what data can be
            included into this Application. Limits which
            Services and Workloads can be registered.
        uid (str):
            Output only. A universally unique identifier (in UUID4
            format) for the ``Application``.
        state (google.cloud.apphub_v1.types.Application.State):
            Output only. Application state.
        application_properties (google.cloud.apphub_v1.types.ApplicationProperties):
            Output only. Properties of an underlying
            cloud resource that can comprise an Application.
        application_type (google.cloud.apphub_v1.types.ApplicationType):
            Output only. Application type.
    """

    class State(proto.Enum):
        r"""Application state.

        Values:
            STATE_UNSPECIFIED (0):
                Unspecified state.
            CREATING (1):
                The Application is being created.
            ACTIVE (2):
                The Application is ready to register Services
                and Workloads.
            DELETING (3):
                The Application is being deleted.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        ACTIVE = 2
        DELETING = 3

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
    attributes: gca_attributes.Attributes = proto.Field(
        proto.MESSAGE,
        number=4,
        message=gca_attributes.Attributes,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    scope: "Scope" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="Scope",
    )
    uid: str = proto.Field(
        proto.STRING,
        number=10,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=11,
        enum=State,
    )
    application_properties: "ApplicationProperties" = proto.Field(
        proto.MESSAGE,
        number=12,
        message="ApplicationProperties",
    )
    application_type: "ApplicationType" = proto.Field(
        proto.MESSAGE,
        number=13,
        message="ApplicationType",
    )


class ApplicationType(proto.Message):
    r"""Application type.

    Attributes:
        type_ (google.cloud.apphub_v1.types.ApplicationType.Type):
            The type of the application.
    """

    class Type(proto.Enum):
        r"""Application type enum.

        Values:
            TYPE_UNSPECIFIED (0):
                Unspecified type.
            AI_APPLICATION (1):
                AI Application type.
        """

        TYPE_UNSPECIFIED = 0
        AI_APPLICATION = 1

    type_: Type = proto.Field(
        proto.ENUM,
        number=1,
        enum=Type,
    )


class Scope(proto.Message):
    r"""Scope of an application.

    Attributes:
        type_ (google.cloud.apphub_v1.types.Scope.Type):
            Required. Scope Type.
    """

    class Type(proto.Enum):
        r"""Scope Type.

        Values:
            TYPE_UNSPECIFIED (0):
                Unspecified type.
            REGIONAL (1):
                Regional type.
            GLOBAL (2):
                Global type.
        """

        TYPE_UNSPECIFIED = 0
        REGIONAL = 1
        GLOBAL = 2

    type_: Type = proto.Field(
        proto.ENUM,
        number=1,
        enum=Type,
    )


class ApplicationProperties(proto.Message):
    r"""Additional system properties of an Application.

    Attributes:
        extended_metadata (MutableMapping[str, google.cloud.apphub_v1.types.ExtendedMetadata]):
            Output only. Additional metadata specific to the App Hub
            application. The key is a string that identifies the type of
            metadata and the value is the metadata contents specific to
            that type. Key format:
            ``apphub.googleapis.com/{metadataType}``
    """

    extended_metadata: MutableMapping[str, properties.ExtendedMetadata] = (
        proto.MapField(
            proto.STRING,
            proto.MESSAGE,
            number=1,
            message=properties.ExtendedMetadata,
        )
    )


__all__ = tuple(sorted(__protobuf__.manifest))
