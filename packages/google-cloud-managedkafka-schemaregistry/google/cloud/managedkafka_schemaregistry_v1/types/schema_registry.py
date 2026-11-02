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

from google.cloud.managedkafka_schemaregistry_v1.types import schema_registry_resources

__protobuf__ = proto.module(
    package="google.cloud.managedkafka.schemaregistry.v1",
    manifest={
        "GetSchemaRegistryRequest",
        "ListSchemaRegistriesRequest",
        "ListSchemaRegistriesResponse",
        "CreateSchemaRegistryRequest",
        "DeleteSchemaRegistryRequest",
        "GetContextRequest",
        "ListContextsRequest",
        "GetSchemaRequest",
        "ListSchemaTypesRequest",
        "ListSchemaVersionsRequest",
        "ListSubjectsRequest",
        "ListSubjectsBySchemaIdRequest",
        "ListVersionsRequest",
        "DeleteSubjectRequest",
        "GetVersionRequest",
        "CreateVersionRequest",
        "CreateVersionResponse",
        "LookupVersionRequest",
        "DeleteVersionRequest",
        "ListReferencedSchemasRequest",
        "CheckCompatibilityRequest",
        "CheckCompatibilityResponse",
        "GetSchemaConfigRequest",
        "UpdateSchemaConfigRequest",
        "DeleteSchemaConfigRequest",
        "GetSchemaModeRequest",
        "UpdateSchemaModeRequest",
        "DeleteSchemaModeRequest",
    },
)


class GetSchemaRegistryRequest(proto.Message):
    r"""Request for GetSchemaRegistry.

    Attributes:
        name (str):
            Required. The name of the schema registry instance to
            return. Structured like:
            ``projects/{project}/locations/{location}/schemaRegistries/{schema_registry}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListSchemaRegistriesRequest(proto.Message):
    r"""Request for ListSchemaRegistries.

    Attributes:
        parent (str):
            Required. The parent whose schema registry instances are to
            be listed. Structured like:
            ``projects/{project}/locations/{location}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListSchemaRegistriesResponse(proto.Message):
    r"""Request for ListSchemaRegistries.

    Attributes:
        schema_registries (MutableSequence[google.cloud.managedkafka_schemaregistry_v1.types.SchemaRegistry]):
            The schema registry instances.
    """

    schema_registries: MutableSequence[schema_registry_resources.SchemaRegistry] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=schema_registry_resources.SchemaRegistry,
        )
    )


class CreateSchemaRegistryRequest(proto.Message):
    r"""Request to create a schema registry instance.

    Attributes:
        parent (str):
            Required. The parent whose schema registry instance is to be
            created. Structured like:
            ``projects/{project}/locations/{location}``
        schema_registry_id (str):
            Required. The schema registry instance ID to
            use for this schema registry. The ID must
            contain only letters (a-z, A-Z), numbers (0-9),
            and underscores (-). The maximum length is 63
            characters.
            The ID must not start with a number.
        schema_registry (google.cloud.managedkafka_schemaregistry_v1.types.SchemaRegistry):
            Required. The schema registry instance to
            create. The name field is ignored.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    schema_registry_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    schema_registry: schema_registry_resources.SchemaRegistry = proto.Field(
        proto.MESSAGE,
        number=3,
        message=schema_registry_resources.SchemaRegistry,
    )


class DeleteSchemaRegistryRequest(proto.Message):
    r"""Request for DeleteSchemaRegistry.

    Attributes:
        name (str):
            Required. The name of the schema registry instance to
            delete. Structured like:
            ``projects/{project}/locations/{location}/schemaRegistries/{schema_registry}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetContextRequest(proto.Message):
    r"""Request for GetContext

    Attributes:
        name (str):
            Required. The name of the context to return. Structured
            like:
            ``projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/contexts/{context}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListContextsRequest(proto.Message):
    r"""Request for ListContexts.

    Attributes:
        parent (str):
            Required. The parent of the contexts. Structured like:
            ``projects/{project}/locations/{location}/schemaRegistries/{schema_registry}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetSchemaRequest(proto.Message):
    r"""Request for GetSchema.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Required. The name of the schema to return. Structured like:
            ``projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/schemas/ids/{schema}``
        subject (str):
            Optional. Used to limit the search for the
            schema ID to a specific subject, otherwise the
            schema ID will be searched for in all subjects
            in the given specified context.

            This field is a member of `oneof`_ ``_subject``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    subject: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )


class ListSchemaTypesRequest(proto.Message):
    r"""Request for ListSchemaTypes.

    Attributes:
        parent (str):
            Required. The parent schema registry whose schema types are
            to be listed. Structured like:
            ``projects/{project}/locations/{location}/schemaRegistries/{schema_registry}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListSchemaVersionsRequest(proto.Message):
    r"""Request for ListSchemaVersions.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        parent (str):
            Required. The schema whose schema versions are to be listed.
            Structured like:
            ``projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/schemas/ids/{schema}``
            or
            ``projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/contexts/{context}/schemas/ids/{schema}``
        subject (str):
            Optional. The subject to filter the subjects
            by.

            This field is a member of `oneof`_ ``_subject``.
        deleted (bool):
            Optional. If true, the response will include
            soft-deleted versions of the schema, even if the
            subject is soft-deleted. The default is false.

            This field is a member of `oneof`_ ``_deleted``.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    subject: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    deleted: bool = proto.Field(
        proto.BOOL,
        number=3,
        optional=True,
    )


class ListSubjectsRequest(proto.Message):
    r"""Request for listing subjects.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        parent (str):
            Required. The parent schema registry/context whose subjects
            are to be listed. Structured like:
            ``projects/{project}/locations/{location}/schemaRegistries/{schema_registry}``
            or
            ``projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/contexts/{context}``
        subject_prefix (str):
            Optional. The context to filter the subjects by, in the
            format of ``:.{context}:``. If unset, all subjects in the
            registry are returned. Set to empty string or add as
            '?subjectPrefix=' at the end of this request to list
            subjects in the default context.

            This field is a member of `oneof`_ ``_subject_prefix``.
        deleted (bool):
            Optional. If true, the response will include
            soft-deleted subjects. The default is false.

            This field is a member of `oneof`_ ``_deleted``.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    subject_prefix: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    deleted: bool = proto.Field(
        proto.BOOL,
        number=3,
        optional=True,
    )


class ListSubjectsBySchemaIdRequest(proto.Message):
    r"""Request for listing subjects.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        parent (str):
            Required. The schema resource whose associated subjects are
            to be listed. Structured like:
            ``projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/schemas/ids/{schema}``
            or
            ``projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/contexts/{context}/schemas/ids/{schema}``
        subject (str):
            Optional. The subject to filter the subjects
            by.

            This field is a member of `oneof`_ ``_subject``.
        deleted (bool):
            Optional. If true, the response will include
            soft-deleted subjects. The default is false.

            This field is a member of `oneof`_ ``_deleted``.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    subject: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    deleted: bool = proto.Field(
        proto.BOOL,
        number=3,
        optional=True,
    )


class ListVersionsRequest(proto.Message):
    r"""Request for GetVersions.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        parent (str):
            Required. The subject whose versions are to be listed.
            Structured like:
            ``projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/subjects/{subject}``
            or
            ``projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/contexts/{context}/subjects/{subject}``
        deleted (bool):
            Optional. If true, the response will include
            soft-deleted versions of an active or
            soft-deleted subject. The default is false.

            This field is a member of `oneof`_ ``_deleted``.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    deleted: bool = proto.Field(
        proto.BOOL,
        number=2,
        optional=True,
    )


class DeleteSubjectRequest(proto.Message):
    r"""Request for DeleteSubject.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Required. The name of the subject to delete. Structured
            like:
            ``projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/subjects/{subject}``
            or
            ``projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/contexts/{context}/subjects/{subject}``
        permanent (bool):
            Optional. If true, the subject and all
            associated metadata including the schema ID will
            be deleted permanently. Otherwise, only the
            subject is soft-deleted. The default is false.
            Soft-deleted subjects can still be searched in
            ListSubjects API call with deleted=true query
            parameter. A soft-delete of a subject must be
            performed before a hard-delete.

            This field is a member of `oneof`_ ``_permanent``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    permanent: bool = proto.Field(
        proto.BOOL,
        number=2,
        optional=True,
    )


class GetVersionRequest(proto.Message):
    r"""Request for GetVersion.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Required. The name of the subject to return versions.
            Structured like:
            ``projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/subjects/{subject}/versions/{version}``
            or
            ``projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/contexts/{context}/subjects/{subject}/versions/{version}``
        deleted (bool):
            Optional. If true, no matter if the subject/version is
            soft-deleted or not, it returns the version details. If
            false, it returns NOT_FOUND error if the subject/version is
            soft-deleted. The default is false.

            This field is a member of `oneof`_ ``_deleted``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    deleted: bool = proto.Field(
        proto.BOOL,
        number=2,
        optional=True,
    )


class CreateVersionRequest(proto.Message):
    r"""Request for CreateVersion.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        parent (str):
            Required. The subject to create the version for. Structured
            like:
            ``projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/subjects/{subject}``
            or
            ``projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/contexts/{context}/subjects/{subject}``
        version (int):
            Optional. The version to create. It is
            optional. If not specified, the version will be
            created with the max version ID of the subject
            increased by 1. If the version ID is specified,
            it will be used as the new version ID and must
            not be used by an existing version of the
            subject.

            This field is a member of `oneof`_ ``_version``.
        id (int):
            Optional. The schema ID of the schema. If not
            specified, the schema ID will be generated by
            the server. If the schema ID is specified, it
            must not be used by an existing schema that is
            different from the schema to be created.

            This field is a member of `oneof`_ ``_id``.
        schema_type (google.cloud.managedkafka_schemaregistry_v1.types.Schema.SchemaType):
            Optional. The type of the schema. It is
            optional. If not specified, the schema type will
            be AVRO.

            This field is a member of `oneof`_ ``_schema_type``.
        schema (str):
            Required. The schema payload
        references (MutableSequence[google.cloud.managedkafka_schemaregistry_v1.types.Schema.SchemaReference]):
            Optional. The schema references used by the
            schema.
        normalize (bool):
            Optional. If true, the schema will be
            normalized before being stored. The default is
            false.

            This field is a member of `oneof`_ ``_normalize``.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    version: int = proto.Field(
        proto.INT32,
        number=2,
        optional=True,
    )
    id: int = proto.Field(
        proto.INT32,
        number=3,
        optional=True,
    )
    schema_type: schema_registry_resources.Schema.SchemaType = proto.Field(
        proto.ENUM,
        number=4,
        optional=True,
        enum=schema_registry_resources.Schema.SchemaType,
    )
    schema: str = proto.Field(
        proto.STRING,
        number=5,
    )
    references: MutableSequence[schema_registry_resources.Schema.SchemaReference] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=6,
            message=schema_registry_resources.Schema.SchemaReference,
        )
    )
    normalize: bool = proto.Field(
        proto.BOOL,
        number=7,
        optional=True,
    )


class CreateVersionResponse(proto.Message):
    r"""Response for CreateVersion.

    Attributes:
        id (int):
            The unique identifier of the schema created.
    """

    id: int = proto.Field(
        proto.INT32,
        number=1,
    )


class LookupVersionRequest(proto.Message):
    r"""Request for LookupVersion.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        parent (str):
            Required. The subject to lookup the schema in. Structured
            like:
            ``projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/subjects/{subject}``
            or
            ``projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/contexts/{context}/subjects/{subject}``
        schema_type (google.cloud.managedkafka_schemaregistry_v1.types.Schema.SchemaType):
            Optional. The schema type of the schema.

            This field is a member of `oneof`_ ``_schema_type``.
        schema (str):
            Required. The schema payload
        references (MutableSequence[google.cloud.managedkafka_schemaregistry_v1.types.Schema.SchemaReference]):
            Optional. The schema references used by the
            schema.
        normalize (bool):
            Optional. If true, the schema will be
            normalized before being looked up. The default
            is false.

            This field is a member of `oneof`_ ``_normalize``.
        deleted (bool):
            Optional. If true, soft-deleted versions will
            be included in lookup, no matter if the subject
            is active or soft-deleted. If false,
            soft-deleted versions will be excluded. The
            default is false.

            This field is a member of `oneof`_ ``_deleted``.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    schema_type: schema_registry_resources.Schema.SchemaType = proto.Field(
        proto.ENUM,
        number=2,
        optional=True,
        enum=schema_registry_resources.Schema.SchemaType,
    )
    schema: str = proto.Field(
        proto.STRING,
        number=3,
    )
    references: MutableSequence[schema_registry_resources.Schema.SchemaReference] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=4,
            message=schema_registry_resources.Schema.SchemaReference,
        )
    )
    normalize: bool = proto.Field(
        proto.BOOL,
        number=5,
        optional=True,
    )
    deleted: bool = proto.Field(
        proto.BOOL,
        number=6,
        optional=True,
    )


class DeleteVersionRequest(proto.Message):
    r"""Request for DeleteVersion.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Required. The name of the subject version to delete.
            Structured like:
            ``projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/subjects/{subject}/versions/{version}``
            or
            ``projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/contexts/{context}/subjects/{subject}/versions/{version}``
        permanent (bool):
            Optional. If true, both the version and the
            referenced schema ID will be permanently
            deleted. The default is false. If false, the
            version will be deleted but the schema ID will
            be retained. Soft-deleted versions can still be
            searched in ListVersions API call with
            deleted=true query parameter. A soft-delete of a
            version must be performed before a hard-delete.

            This field is a member of `oneof`_ ``_permanent``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    permanent: bool = proto.Field(
        proto.BOOL,
        number=2,
        optional=True,
    )


class ListReferencedSchemasRequest(proto.Message):
    r"""Request for ListReferencedSchemas.

    Attributes:
        parent (str):
            Required. The version to list referenced by. Structured
            like:
            ``projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/subjects/{subject}/versions/{version}``
            or
            ``projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/contexts/{context}/subjects/{subject}/versions/{version}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CheckCompatibilityRequest(proto.Message):
    r"""Request for CheckCompatibility.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Required. The name of the resource to check compatibility
            for. The format is either of following:

            - projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/compatibility/subjects/\*/versions:
              Check compatibility with one or more versions of the
              specified subject.
            - projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/compatibility/subjects/{subject}/versions/{version}:
              Check compatibility with a specific version of the
              subject.
        schema_type (google.cloud.managedkafka_schemaregistry_v1.types.Schema.SchemaType):
            Optional. The schema type of the schema.

            This field is a member of `oneof`_ ``_schema_type``.
        schema (str):
            Required. The schema payload
        references (MutableSequence[google.cloud.managedkafka_schemaregistry_v1.types.Schema.SchemaReference]):
            Optional. The schema references used by the
            schema.
        verbose (bool):
            Optional. If true, the response will contain
            the compatibility check result with reasons for
            failed checks. The default is false.

            This field is a member of `oneof`_ ``_verbose``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    schema_type: schema_registry_resources.Schema.SchemaType = proto.Field(
        proto.ENUM,
        number=2,
        optional=True,
        enum=schema_registry_resources.Schema.SchemaType,
    )
    schema: str = proto.Field(
        proto.STRING,
        number=3,
    )
    references: MutableSequence[schema_registry_resources.Schema.SchemaReference] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=4,
            message=schema_registry_resources.Schema.SchemaReference,
        )
    )
    verbose: bool = proto.Field(
        proto.BOOL,
        number=5,
        optional=True,
    )


class CheckCompatibilityResponse(proto.Message):
    r"""Response for CheckCompatibility.

    Attributes:
        is_compatible (bool):
            The compatibility check result. If true, the
            schema is compatible with the resource.
        messages (MutableSequence[str]):
            Failure reasons if verbose = true.
    """

    is_compatible: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    messages: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class GetSchemaConfigRequest(proto.Message):
    r"""Request for getting config.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Required. The resource name to get the config for. It can be
            either of following:

            - projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/config:
              Get config at global level.
            - projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/config/{subject}:
              Get config for a specific subject.
        default_to_global (bool):
            Optional. If true, the config will fall back
            to the config at the global level if no subject
            level config is found.

            This field is a member of `oneof`_ ``_default_to_global``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    default_to_global: bool = proto.Field(
        proto.BOOL,
        number=2,
        optional=True,
    )


class UpdateSchemaConfigRequest(proto.Message):
    r"""Request for updating schema config.
    On a SchemaSubject-level SchemaConfig, an unset field will be
    removed from the SchemaConfig.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Required. The resource name to update the config for. It can
            be either of following:

            - projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/config:
              Update config at global level.
            - projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/config/{subject}:
              Update config for a specific subject.
        compatibility (google.cloud.managedkafka_schemaregistry_v1.types.SchemaConfig.CompatibilityType):
            Required. The compatibility type of the
            schemas. Cannot be unset for a
            SchemaRegistry-level SchemaConfig. If unset on a
            SchemaSubject-level SchemaConfig, removes the
            compatibility field for the SchemaConfig.

            This field is a member of `oneof`_ ``_compatibility``.
        normalize (bool):
            Optional. If true, the schema will be
            normalized before being stored or looked up. The
            default is false. Cannot be unset for a
            SchemaRegistry-level SchemaConfig. If unset on a
            SchemaSubject-level SchemaConfig, removes the
            normalize field for the SchemaConfig.

            This field is a member of `oneof`_ ``_normalize``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    compatibility: schema_registry_resources.SchemaConfig.CompatibilityType = (
        proto.Field(
            proto.ENUM,
            number=2,
            optional=True,
            enum=schema_registry_resources.SchemaConfig.CompatibilityType,
        )
    )
    normalize: bool = proto.Field(
        proto.BOOL,
        number=3,
        optional=True,
    )


class DeleteSchemaConfigRequest(proto.Message):
    r"""Request for deleting schema config.

    Attributes:
        name (str):
            Required. The resource name of subject to delete the config
            for. The format is

            - projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/config/{subject}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetSchemaModeRequest(proto.Message):
    r"""Request for getting schema registry or subject mode.

    Attributes:
        name (str):
            Required. The resource name of the mode. The format is

            - projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/mode/{subject}:
              mode for a schema registry, or
            - projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/contexts/{context}/mode/{subject}:
              mode for a specific subject in a specific context
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateSchemaModeRequest(proto.Message):
    r"""Request for updating schema registry or subject mode.

    Attributes:
        name (str):
            Required. The resource name of the mode. The format is

            - projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/mode/{subject}:
              mode for a schema registry, or
            - projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/contexts/{context}/mode/{subject}:
              mode for a specific subject in a specific context
        mode (google.cloud.managedkafka_schemaregistry_v1.types.SchemaMode.ModeType):
            Required. The mode type.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    mode: schema_registry_resources.SchemaMode.ModeType = proto.Field(
        proto.ENUM,
        number=2,
        enum=schema_registry_resources.SchemaMode.ModeType,
    )


class DeleteSchemaModeRequest(proto.Message):
    r"""Request for deleting schema mode.

    Attributes:
        name (str):
            Required. The resource name of subject to delete the mode
            for. The format is

            - projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/mode/{subject}
            - projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/contexts/{context}/mode/{subject}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
