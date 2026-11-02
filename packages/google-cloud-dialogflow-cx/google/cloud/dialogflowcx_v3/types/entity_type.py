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

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.dialogflowcx_v3.types import inline

__protobuf__ = proto.module(
    package="google.cloud.dialogflow.cx.v3",
    manifest={
        "EntityType",
        "ExportEntityTypesRequest",
        "ExportEntityTypesResponse",
        "ExportEntityTypesMetadata",
        "ImportEntityTypesRequest",
        "ImportEntityTypesResponse",
        "ImportEntityTypesMetadata",
        "ListEntityTypesRequest",
        "ListEntityTypesResponse",
        "GetEntityTypeRequest",
        "CreateEntityTypeRequest",
        "UpdateEntityTypeRequest",
        "DeleteEntityTypeRequest",
    },
)


class EntityType(proto.Message):
    r"""Entities are extracted from user input and represent parameters that
    are meaningful to your application. For example, a date range, a
    proper name such as a geographic location or landmark, and so on.
    Entities represent actionable data for your application.

    When you define an entity, you can also include synonyms that all
    map to that entity. For example, "soft drink", "soda", "pop", and so
    on.

    There are three types of entities:

    - **System** - entities that are defined by the Dialogflow API for
      common data types such as date, time, currency, and so on. A
      system entity is represented by the ``EntityType`` type.

    - **Custom** - entities that are defined by you that represent
      actionable data that is meaningful to your application. For
      example, you could define a ``pizza.sauce`` entity for red or
      white pizza sauce, a ``pizza.cheese`` entity for the different
      types of cheese on a pizza, a ``pizza.topping`` entity for
      different toppings, and so on. A custom entity is represented by
      the ``EntityType`` type.

    - **User** - entities that are built for an individual user such as
      favorites, preferences, playlists, and so on. A user entity is
      represented by the
      [SessionEntityType][google.cloud.dialogflow.cx.v3.SessionEntityType]
      type.

    For more information about entity types, see the `Dialogflow
    documentation <https://cloud.google.com/dialogflow/docs/entities-overview>`__.

    Attributes:
        name (str):
            The unique identifier of the entity type. Required for
            [EntityTypes.UpdateEntityType][google.cloud.dialogflow.cx.v3.EntityTypes.UpdateEntityType].
            Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/entityTypes/<EntityTypeID>``.
        display_name (str):
            Required. The human-readable name of the
            entity type, unique within the agent.
        kind (google.cloud.dialogflowcx_v3.types.EntityType.Kind):
            Required. Indicates the kind of entity type.
        auto_expansion_mode (google.cloud.dialogflowcx_v3.types.EntityType.AutoExpansionMode):
            Indicates whether the entity type can be
            automatically expanded.
        entities (MutableSequence[google.cloud.dialogflowcx_v3.types.EntityType.Entity]):
            The collection of entity entries associated
            with the entity type.
        excluded_phrases (MutableSequence[google.cloud.dialogflowcx_v3.types.EntityType.ExcludedPhrase]):
            Collection of exceptional words and phrases that shouldn't
            be matched. For example, if you have a size entity type with
            entry ``giant``\ (an adjective), you might consider adding
            ``giants``\ (a noun) as an exclusion. If the kind of entity
            type is ``KIND_MAP``, then the phrases specified by entities
            and excluded phrases should be mutually exclusive.
        enable_fuzzy_extraction (bool):
            Enables fuzzy entity extraction during
            classification.
        redact (bool):
            Indicates whether parameters of the entity
            type should be redacted in log. If redaction is
            enabled, page parameters and intent parameters
            referring to the entity type will be replaced by
            parameter name when logging.
    """

    class Kind(proto.Enum):
        r"""Represents kinds of entities.

        Values:
            KIND_UNSPECIFIED (0):
                Not specified. This value should be never
                used.
            KIND_MAP (1):
                Map entity types allow mapping of a group of
                synonyms to a canonical value.
            KIND_LIST (2):
                List entity types contain a set of entries
                that do not map to canonical values. However,
                list entity types can contain references to
                other entity types (with or without aliases).
            KIND_REGEXP (3):
                Regexp entity types allow to specify regular
                expressions in entries values.
        """

        KIND_UNSPECIFIED = 0
        KIND_MAP = 1
        KIND_LIST = 2
        KIND_REGEXP = 3

    class AutoExpansionMode(proto.Enum):
        r"""Represents different entity type expansion modes. Automated
        expansion allows an agent to recognize values that have not been
        explicitly listed in the entity (for example, new kinds of
        shopping list items).

        Values:
            AUTO_EXPANSION_MODE_UNSPECIFIED (0):
                Auto expansion disabled for the entity.
            AUTO_EXPANSION_MODE_DEFAULT (1):
                Allows an agent to recognize values that have
                not been explicitly listed in the entity.
        """

        AUTO_EXPANSION_MODE_UNSPECIFIED = 0
        AUTO_EXPANSION_MODE_DEFAULT = 1

    class Entity(proto.Message):
        r"""An **entity entry** for an associated entity type.

        Attributes:
            value (str):
                Required. The primary value associated with this entity
                entry. For example, if the entity type is *vegetable*, the
                value could be *scallions*.

                For ``KIND_MAP`` entity types:

                - A canonical value to be used in place of synonyms.

                For ``KIND_LIST`` entity types:

                - A string that can contain references to other entity types
                  (with or without aliases).
            synonyms (MutableSequence[str]):
                Required. A collection of value synonyms. For example, if
                the entity type is *vegetable*, and ``value`` is
                *scallions*, a synonym could be *green onions*.

                For ``KIND_LIST`` entity types:

                - This collection must contain exactly one synonym equal to
                  ``value``.
        """

        value: str = proto.Field(
            proto.STRING,
            number=1,
        )
        synonyms: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )

    class ExcludedPhrase(proto.Message):
        r"""An excluded entity phrase that should not be matched.

        Attributes:
            value (str):
                Required. The word or phrase to be excluded.
        """

        value: str = proto.Field(
            proto.STRING,
            number=1,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    kind: Kind = proto.Field(
        proto.ENUM,
        number=3,
        enum=Kind,
    )
    auto_expansion_mode: AutoExpansionMode = proto.Field(
        proto.ENUM,
        number=4,
        enum=AutoExpansionMode,
    )
    entities: MutableSequence[Entity] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message=Entity,
    )
    excluded_phrases: MutableSequence[ExcludedPhrase] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message=ExcludedPhrase,
    )
    enable_fuzzy_extraction: bool = proto.Field(
        proto.BOOL,
        number=7,
    )
    redact: bool = proto.Field(
        proto.BOOL,
        number=9,
    )


class ExportEntityTypesRequest(proto.Message):
    r"""The request message for
    [EntityTypes.ExportEntityTypes][google.cloud.dialogflow.cx.v3.EntityTypes.ExportEntityTypes].

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        parent (str):
            Required. The name of the parent agent to export entity
            types. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>``.
        entity_types (MutableSequence[str]):
            Required. The name of the entity types to export. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/entityTypes/<EntityTypeID>``.
        entity_types_uri (str):
            Optional. The `Google Cloud
            Storage <https://cloud.google.com/storage/docs/>`__ URI to
            export the entity types to. The format of this URI must be
            ``gs://<bucket-name>/<object-name>``.

            Dialogflow performs a write operation for the Cloud Storage
            object on the caller's behalf, so your request
            authentication must have write permissions for the object.
            For more information, see `Dialogflow access
            control <https://cloud.google.com/dialogflow/cx/docs/concept/access-control#storage>`__.

            This field is a member of `oneof`_ ``destination``.
        entity_types_content_inline (bool):
            Optional. The option to return the serialized
            entity types inline.

            This field is a member of `oneof`_ ``destination``.
        data_format (google.cloud.dialogflowcx_v3.types.ExportEntityTypesRequest.DataFormat):
            Optional. The data format of the exported entity types. If
            not specified, ``BLOB`` is assumed.
        language_code (str):
            Optional. The language to retrieve the entity type for. The
            following fields are language dependent:

            - ``EntityType.entities.value``
            - ``EntityType.entities.synonyms``
            - ``EntityType.excluded_phrases.value``

            If not specified, all language dependent fields will be
            retrieved. `Many
            languages <https://cloud.google.com/dialogflow/docs/reference/language>`__
            are supported. Note: languages must be enabled in the agent
            before they can be used.
    """

    class DataFormat(proto.Enum):
        r"""Data format of the exported entity types.

        Values:
            DATA_FORMAT_UNSPECIFIED (0):
                Unspecified format. Treated as ``BLOB``.
            BLOB (1):
                EntityTypes will be exported as raw bytes.
            JSON_PACKAGE (5):
                EntityTypes will be exported in JSON Package
                format.
        """

        DATA_FORMAT_UNSPECIFIED = 0
        BLOB = 1
        JSON_PACKAGE = 5

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    entity_types: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    entity_types_uri: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="destination",
    )
    entity_types_content_inline: bool = proto.Field(
        proto.BOOL,
        number=4,
        oneof="destination",
    )
    data_format: DataFormat = proto.Field(
        proto.ENUM,
        number=5,
        enum=DataFormat,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=6,
    )


class ExportEntityTypesResponse(proto.Message):
    r"""The response message for
    [EntityTypes.ExportEntityTypes][google.cloud.dialogflow.cx.v3.EntityTypes.ExportEntityTypes].

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        entity_types_uri (str):
            The URI to a file containing the exported entity types. This
            field is populated only if ``entity_types_uri`` is specified
            in
            [ExportEntityTypesRequest][google.cloud.dialogflow.cx.v3.ExportEntityTypesRequest].

            This field is a member of `oneof`_ ``exported_entity_types``.
        entity_types_content (google.cloud.dialogflowcx_v3.types.InlineDestination):
            Uncompressed byte content for entity types. This field is
            populated only if ``entity_types_content_inline`` is set to
            true in
            [ExportEntityTypesRequest][google.cloud.dialogflow.cx.v3.ExportEntityTypesRequest].

            This field is a member of `oneof`_ ``exported_entity_types``.
    """

    entity_types_uri: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="exported_entity_types",
    )
    entity_types_content: inline.InlineDestination = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="exported_entity_types",
        message=inline.InlineDestination,
    )


class ExportEntityTypesMetadata(proto.Message):
    r"""Metadata returned for the
    [EntityTypes.ExportEntityTypes][google.cloud.dialogflow.cx.v3.EntityTypes.ExportEntityTypes]
    long running operation.

    """


class ImportEntityTypesRequest(proto.Message):
    r"""The request message for
    [EntityTypes.ImportEntityTypes][google.cloud.dialogflow.cx.v3.EntityTypes.ImportEntityTypes].

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        parent (str):
            Required. The agent to import the entity types into. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>``.
        entity_types_uri (str):
            The `Google Cloud
            Storage <https://cloud.google.com/storage/docs/>`__ URI to
            import entity types from. The format of this URI must be
            ``gs://<bucket-name>/<object-name>``.

            Dialogflow performs a read operation for the Cloud Storage
            object on the caller's behalf, so your request
            authentication must have read permissions for the object.
            For more information, see `Dialogflow access
            control <https://cloud.google.com/dialogflow/cx/docs/concept/access-control#storage>`__.

            This field is a member of `oneof`_ ``entity_types``.
        entity_types_content (google.cloud.dialogflowcx_v3.types.InlineSource):
            Uncompressed byte content of entity types.

            This field is a member of `oneof`_ ``entity_types``.
        merge_option (google.cloud.dialogflowcx_v3.types.ImportEntityTypesRequest.MergeOption):
            Required. Merge option for importing entity
            types.
        target_entity_type (str):
            Optional. The target entity type to import into. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/entity_types/<EntityTypeID>``.
            If set, there should be only one entity type included in
            [entity_types][google.cloud.dialogflow.cx.v3.ImportEntityTypesRequest.entity_types],
            of which the type should match the type of the target entity
            type. All
            [entities][google.cloud.dialogflow.cx.v3.EntityType.entities]
            in the imported entity type will be added to the target
            entity type.
    """

    class MergeOption(proto.Enum):
        r"""Merge option when display name conflicts exist during import.

        Values:
            MERGE_OPTION_UNSPECIFIED (0):
                Unspecified. If used, system uses REPORT_CONFLICT as
                default.
            REPLACE (1):
                Replace the original entity type in the agent
                with the new entity type when display name
                conflicts exist.
            MERGE (2):
                Merge the original entity type with the new
                entity type when display name conflicts exist.
            RENAME (3):
                Create new entity types with new display
                names to differentiate them from the existing
                entity types when display name conflicts exist.
            REPORT_CONFLICT (4):
                Report conflict information if display names
                conflict is detected. Otherwise, import entity
                types.
            KEEP (5):
                Keep the original entity type and discard the
                conflicting new entity type when display name
                conflicts exist.
        """

        MERGE_OPTION_UNSPECIFIED = 0
        REPLACE = 1
        MERGE = 2
        RENAME = 3
        REPORT_CONFLICT = 4
        KEEP = 5

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    entity_types_uri: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="entity_types",
    )
    entity_types_content: inline.InlineSource = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="entity_types",
        message=inline.InlineSource,
    )
    merge_option: MergeOption = proto.Field(
        proto.ENUM,
        number=4,
        enum=MergeOption,
    )
    target_entity_type: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ImportEntityTypesResponse(proto.Message):
    r"""The response message for
    [EntityTypes.ImportEntityTypes][google.cloud.dialogflow.cx.v3.EntityTypes.ImportEntityTypes].

    Attributes:
        entity_types (MutableSequence[str]):
            The unique identifier of the imported entity types. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/entity_types/<EntityTypeID>``.
        conflicting_resources (google.cloud.dialogflowcx_v3.types.ImportEntityTypesResponse.ConflictingResources):
            Info which resources have conflicts when
            [REPORT_CONFLICT][ImportEntityTypesResponse.REPORT_CONFLICT]
            merge_option is set in ImportEntityTypesRequest.
    """

    class ConflictingResources(proto.Message):
        r"""Conflicting resources detected during the import process. Only
        filled when
        [REPORT_CONFLICT][ImportEntityTypesResponse.REPORT_CONFLICT] is set
        in the request and there are conflicts in the display names.

        Attributes:
            entity_type_display_names (MutableSequence[str]):
                Display names of conflicting entity types.
            entity_display_names (MutableSequence[str]):
                Display names of conflicting entities.
        """

        entity_type_display_names: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )
        entity_display_names: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )

    entity_types: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    conflicting_resources: ConflictingResources = proto.Field(
        proto.MESSAGE,
        number=2,
        message=ConflictingResources,
    )


class ImportEntityTypesMetadata(proto.Message):
    r"""Metadata returned for the
    [EntityTypes.ImportEntityTypes][google.cloud.dialogflow.cx.v3.EntityTypes.ImportEntityTypes]
    long running operation.

    """


class ListEntityTypesRequest(proto.Message):
    r"""The request message for
    [EntityTypes.ListEntityTypes][google.cloud.dialogflow.cx.v3.EntityTypes.ListEntityTypes].

    Attributes:
        parent (str):
            Required. The agent to list all entity types for. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>``.
        language_code (str):
            The language to list entity types for. The following fields
            are language dependent:

            - ``EntityType.entities.value``
            - ``EntityType.entities.synonyms``
            - ``EntityType.excluded_phrases.value``

            If not specified, the agent's default language is used.
            `Many
            languages <https://cloud.google.com/dialogflow/cx/docs/reference/language>`__
            are supported. Note: languages must be enabled in the agent
            before they can be used.
        page_size (int):
            The maximum number of items to return in a
            single page. By default 100 and at most 1000.
        page_token (str):
            The next_page_token value returned from a previous list
            request.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListEntityTypesResponse(proto.Message):
    r"""The response message for
    [EntityTypes.ListEntityTypes][google.cloud.dialogflow.cx.v3.EntityTypes.ListEntityTypes].

    Attributes:
        entity_types (MutableSequence[google.cloud.dialogflowcx_v3.types.EntityType]):
            The list of entity types. There will be a maximum number of
            items returned based on the page_size field in the request.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    entity_types: MutableSequence["EntityType"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="EntityType",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetEntityTypeRequest(proto.Message):
    r"""The request message for
    [EntityTypes.GetEntityType][google.cloud.dialogflow.cx.v3.EntityTypes.GetEntityType].

    Attributes:
        name (str):
            Required. The name of the entity type. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/entityTypes/<EntityTypeID>``.
        language_code (str):
            The language to retrieve the entity type for. The following
            fields are language dependent:

            - ``EntityType.entities.value``
            - ``EntityType.entities.synonyms``
            - ``EntityType.excluded_phrases.value``

            If not specified, the agent's default language is used.
            `Many
            languages <https://cloud.google.com/dialogflow/cx/docs/reference/language>`__
            are supported. Note: languages must be enabled in the agent
            before they can be used.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateEntityTypeRequest(proto.Message):
    r"""The request message for
    [EntityTypes.CreateEntityType][google.cloud.dialogflow.cx.v3.EntityTypes.CreateEntityType].

    Attributes:
        parent (str):
            Required. The agent to create a entity type for. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>``.
        entity_type (google.cloud.dialogflowcx_v3.types.EntityType):
            Required. The entity type to create.
        language_code (str):
            The language of the following fields in ``entity_type``:

            - ``EntityType.entities.value``
            - ``EntityType.entities.synonyms``
            - ``EntityType.excluded_phrases.value``

            If not specified, the agent's default language is used.
            `Many
            languages <https://cloud.google.com/dialogflow/cx/docs/reference/language>`__
            are supported. Note: languages must be enabled in the agent
            before they can be used.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    entity_type: "EntityType" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="EntityType",
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=3,
    )


class UpdateEntityTypeRequest(proto.Message):
    r"""The request message for
    [EntityTypes.UpdateEntityType][google.cloud.dialogflow.cx.v3.EntityTypes.UpdateEntityType].

    Attributes:
        entity_type (google.cloud.dialogflowcx_v3.types.EntityType):
            Required. The entity type to update.
        language_code (str):
            The language of the following fields in ``entity_type``:

            - ``EntityType.entities.value``
            - ``EntityType.entities.synonyms``
            - ``EntityType.excluded_phrases.value``

            If not specified, the agent's default language is used.
            `Many
            languages <https://cloud.google.com/dialogflow/cx/docs/reference/language>`__
            are supported. Note: languages must be enabled in the agent
            before they can be used.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The mask to control which fields get updated.
    """

    entity_type: "EntityType" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="EntityType",
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=2,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=3,
        message=field_mask_pb2.FieldMask,
    )


class DeleteEntityTypeRequest(proto.Message):
    r"""The request message for
    [EntityTypes.DeleteEntityType][google.cloud.dialogflow.cx.v3.EntityTypes.DeleteEntityType].

    Attributes:
        name (str):
            Required. The name of the entity type to delete. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/entityTypes/<EntityTypeID>``.
        force (bool):
            This field has no effect for entity type not being used. For
            entity types that are used by intents or pages:

            - If ``force`` is set to false, an error will be returned
              with message indicating the referencing resources.
            - If ``force`` is set to true, Dialogflow will remove the
              entity type, as well as any references to the entity type
              (i.e. Page
              [parameter][google.cloud.dialogflow.cx.v3.Form.Parameter]
              of the entity type will be changed to '@sys.any' and
              intent
              [parameter][google.cloud.dialogflow.cx.v3.Intent.Parameter]
              of the entity type will be removed).
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
