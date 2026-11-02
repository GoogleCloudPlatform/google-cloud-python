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
    package="google.cloud.managedkafka.schemaregistry.v1",
    manifest={
        "SchemaRegistry",
        "Context",
        "Schema",
        "SchemaSubject",
        "SchemaVersion",
        "SchemaConfig",
        "SchemaMode",
    },
)


class SchemaRegistry(proto.Message):
    r"""SchemaRegistry is a schema registry instance.

    Attributes:
        name (str):
            Identifier. The name of the schema registry instance.
            Structured like:
            ``projects/{project}/locations/{location}/schemaRegistries/{schema_registry}``
            The instance name {schema_registry} can contain the
            following:

            - Up to 255 characters.
            - Letters (uppercase or lowercase), numbers, and
              underscores.
        contexts (MutableSequence[str]):
            Output only. The contexts of the schema
            registry instance.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    contexts: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class Context(proto.Message):
    r"""Context represents an independent schema grouping in a schema
    registry instance.

    Attributes:
        name (str):
            Identifier. The name of the context. Structured like:
            ``projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/contexts/{context}``
            The context name {context} can contain the following:

            - Up to 255 characters.
            - Allowed characters: letters (uppercase or lowercase),
              numbers, and the following special characters: ``.``,
              ``-``, ``_``, ``+``, ``%``, and ``~``.
        subjects (MutableSequence[str]):
            Optional. The subjects of the context.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    subjects: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class Schema(proto.Message):
    r"""Schema for a Kafka message.

    Attributes:
        schema_type (google.cloud.managedkafka_schemaregistry_v1.types.Schema.SchemaType):
            Optional. The schema type of the schema.
        schema_payload (str):
            The schema payload.
        references (MutableSequence[google.cloud.managedkafka_schemaregistry_v1.types.Schema.SchemaReference]):
            Optional. The schema references used by the
            schema.
    """

    class SchemaType(proto.Enum):
        r"""Schema types.

        Values:
            SCHEMA_TYPE_UNSPECIFIED (0):
                No schema type. The default will be AVRO.
            AVRO (1):
                Avro schema type.
            JSON (2):
                JSON schema type.
            PROTOBUF (3):
                Protobuf schema type.
        """

        SCHEMA_TYPE_UNSPECIFIED = 0
        AVRO = 1
        JSON = 2
        PROTOBUF = 3

    class SchemaReference(proto.Message):
        r"""SchemaReference is a reference to a schema.

        Attributes:
            name (str):
                Required. The name of the reference.
            subject (str):
                Required. The subject of the reference.
            version (int):
                Required. The version of the reference.
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        subject: str = proto.Field(
            proto.STRING,
            number=2,
        )
        version: int = proto.Field(
            proto.INT32,
            number=3,
        )

    schema_type: SchemaType = proto.Field(
        proto.ENUM,
        number=1,
        enum=SchemaType,
    )
    schema_payload: str = proto.Field(
        proto.STRING,
        number=2,
    )
    references: MutableSequence[SchemaReference] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=SchemaReference,
    )


class SchemaSubject(proto.Message):
    r"""Subject defines the evolution scope of schemas as a holder of
    schema versions.

    Attributes:
        name (str):
            The name of the subject. Structured like:
            ``projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/subjects/{subject}``
            or
            ``projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/contexts/{context}/subjects/{subject}``

            Subject name {subject} can contain the following:

            - Up to 255 UTF-8 bytes.
            - Allowed characters: letters (uppercase or lowercase),
              numbers, and the following special characters: ``.``,
              ``-``, ``_``, ``+``, ``%``, and ``~``.
        versions (MutableSequence[str]):
            The versions of the subject.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    versions: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class SchemaVersion(proto.Message):
    r"""Version of a schema.

    Attributes:
        subject (str):
            Required. The subject of the version.
        version_id (int):
            Required. The version ID
        schema_id (int):
            Required. The schema ID.
        schema_type (google.cloud.managedkafka_schemaregistry_v1.types.Schema.SchemaType):
            Optional. The schema type of the schema.
        schema_payload (str):
            Required. The schema payload.
        references (MutableSequence[google.cloud.managedkafka_schemaregistry_v1.types.Schema.SchemaReference]):
            Optional. The schema references used by the
            schema.
    """

    subject: str = proto.Field(
        proto.STRING,
        number=1,
    )
    version_id: int = proto.Field(
        proto.INT32,
        number=2,
    )
    schema_id: int = proto.Field(
        proto.INT32,
        number=3,
    )
    schema_type: "Schema.SchemaType" = proto.Field(
        proto.ENUM,
        number=4,
        enum="Schema.SchemaType",
    )
    schema_payload: str = proto.Field(
        proto.STRING,
        number=5,
    )
    references: MutableSequence["Schema.SchemaReference"] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message="Schema.SchemaReference",
    )


class SchemaConfig(proto.Message):
    r"""SchemaConfig represents configuration for a schema registry
    or a specific subject.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        compatibility (google.cloud.managedkafka_schemaregistry_v1.types.SchemaConfig.CompatibilityType):
            Required. The compatibility type of the
            schema. The default value is BACKWARD.
            If unset in a SchemaSubject-level SchemaConfig,
            defaults to the global value. If unset in a
            SchemaRegistry-level SchemaConfig, reverts to
            the default value.

            This field is a member of `oneof`_ ``_compatibility``.
        normalize (bool):
            Optional. If true, the schema will be
            normalized before being stored or looked up. The
            default is false. If unset in a
            SchemaSubject-level SchemaConfig, the global
            value will be used. If unset in a
            SchemaRegistry-level SchemaConfig, reverts to
            the default value.

            This field is a member of `oneof`_ ``_normalize``.
        alias (str):
            Optional. The subject to which this subject
            is an alias of. Only applicable for subject
            config.
    """

    class CompatibilityType(proto.Enum):
        r"""Compatibility type of the schemas.

        Values:
            NONE (0):
                No compatibility check.
            BACKWARD (1):
                Backwards compatible with the most recent
                version.
            BACKWARD_TRANSITIVE (2):
                Backwards compatible with all previous
                versions.
            FORWARD (3):
                Forwards compatible with the most recent
                version.
            FORWARD_TRANSITIVE (4):
                Forwards compatible with all previous
                versions.
            FULL (5):
                Backwards and forwards compatible with the
                most recent version.
            FULL_TRANSITIVE (6):
                Backwards and forwards compatible with all
                previous versions.
        """

        NONE = 0
        BACKWARD = 1
        BACKWARD_TRANSITIVE = 2
        FORWARD = 3
        FORWARD_TRANSITIVE = 4
        FULL = 5
        FULL_TRANSITIVE = 6

    compatibility: CompatibilityType = proto.Field(
        proto.ENUM,
        number=1,
        optional=True,
        enum=CompatibilityType,
    )
    normalize: bool = proto.Field(
        proto.BOOL,
        number=2,
        optional=True,
    )
    alias: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SchemaMode(proto.Message):
    r"""SchemaMode represents the mode of a schema registry or a specific
    subject. Four modes are supported:

    - NONE: deprecated. This was the default mode for a subject, but now
      the default is unset (which means use the global schema registry
      setting)
    - READONLY: The schema registry is in read-only mode.
    - READWRITE: The schema registry is in read-write mode, which allows
      limited write operations on the schema.
    - IMPORT: The schema registry is in import mode, which allows more
      editing operations on the schema for data importing purposes.

    Attributes:
        mode (google.cloud.managedkafka_schemaregistry_v1.types.SchemaMode.ModeType):
            Required. The mode type of a schema registry
            (READWRITE by default) or of a subject (unset by
            default, which means use the global schema
            registry setting).
    """

    class ModeType(proto.Enum):
        r"""Mode type of the schemas or subjects.

        Values:
            NONE (0):
                The default / unset value.
                The subject mode is NONE/unset by default, which
                means use the global schema registry mode. This
                should not be used for setting the mode.
            READONLY (1):
                READONLY mode.
            READWRITE (2):
                READWRITE mode.
            IMPORT (3):
                IMPORT mode.
        """

        NONE = 0
        READONLY = 1
        READWRITE = 2
        IMPORT = 3

    mode: ModeType = proto.Field(
        proto.ENUM,
        number=1,
        enum=ModeType,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
