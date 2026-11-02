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

__protobuf__ = proto.module(
    package="google.cloud.dialogflow.v2",
    manifest={
        "EntityType",
        "ListEntityTypesRequest",
        "ListEntityTypesResponse",
        "GetEntityTypeRequest",
        "CreateEntityTypeRequest",
        "UpdateEntityTypeRequest",
        "DeleteEntityTypeRequest",
        "BatchUpdateEntityTypesRequest",
        "BatchUpdateEntityTypesResponse",
        "BatchDeleteEntityTypesRequest",
        "BatchCreateEntitiesRequest",
        "BatchUpdateEntitiesRequest",
        "BatchDeleteEntitiesRequest",
        "EntityTypeBatch",
    },
)


class EntityType(proto.Message):
    r"""Each intent parameter has a type, called the entity type, which
    dictates exactly how data from an end-user expression is extracted.

    Dialogflow provides predefined system entities that can match many
    common types of data. For example, there are system entities for
    matching dates, times, colors, email addresses, and so on. You can
    also create your own custom entities for matching custom data. For
    example, you could define a vegetable entity that can match the
    types of vegetables available for purchase with a grocery store
    agent.

    For more information, see the `Entity
    guide <https://cloud.google.com/dialogflow/docs/entities-overview>`__.

    Attributes:
        name (str):
            The unique identifier of the entity type. Required for
            [EntityTypes.UpdateEntityType][google.cloud.dialogflow.v2.EntityTypes.UpdateEntityType]
            and
            [EntityTypes.BatchUpdateEntityTypes][google.cloud.dialogflow.v2.EntityTypes.BatchUpdateEntityTypes]
            methods. Format:
            ``projects/<Project ID>/agent/entityTypes/<Entity Type ID>``.
        display_name (str):
            Required. The name of the entity type.
        kind (google.cloud.dialogflow_v2.types.EntityType.Kind):
            Required. Indicates the kind of entity type.
        auto_expansion_mode (google.cloud.dialogflow_v2.types.EntityType.AutoExpansionMode):
            Optional. Indicates whether the entity type
            can be automatically expanded.
        entities (MutableSequence[google.cloud.dialogflow_v2.types.EntityType.Entity]):
            Optional. The collection of entity entries
            associated with the entity type.
        enable_fuzzy_extraction (bool):
            Optional. Enables fuzzy entity extraction
            during classification.
    """

    class Kind(proto.Enum):
        r"""Represents kinds of entities.

        Values:
            KIND_UNSPECIFIED (0):
                Not specified. This value should be never
                used.
            KIND_MAP (1):
                Map entity types allow mapping of a group of
                synonyms to a reference value.
            KIND_LIST (2):
                List entity types contain a set of entries
                that do not map to reference values. However,
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

                - A reference value to be used in place of synonyms.

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
        number=6,
        message=Entity,
    )
    enable_fuzzy_extraction: bool = proto.Field(
        proto.BOOL,
        number=7,
    )


class ListEntityTypesRequest(proto.Message):
    r"""The request message for
    [EntityTypes.ListEntityTypes][google.cloud.dialogflow.v2.EntityTypes.ListEntityTypes].

    Attributes:
        parent (str):
            Required. The agent to list all entity types from. Format:
            ``projects/<Project ID>/agent``.
        language_code (str):
            Optional. The language used to access language-specific
            data. If not specified, the agent's default language is
            used. For more information, see `Multilingual intent and
            entity
            data <https://cloud.google.com/dialogflow/docs/agents-multilingual#intent-entity>`__.
        page_size (int):
            Optional. The maximum number of items to
            return in a single page. By default 100 and at
            most 1000.
        page_token (str):
            Optional. The next_page_token value returned from a previous
            list request.
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
    [EntityTypes.ListEntityTypes][google.cloud.dialogflow.v2.EntityTypes.ListEntityTypes].

    Attributes:
        entity_types (MutableSequence[google.cloud.dialogflow_v2.types.EntityType]):
            The list of agent entity types. There will be a maximum
            number of items returned based on the page_size field in the
            request.
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
    [EntityTypes.GetEntityType][google.cloud.dialogflow.v2.EntityTypes.GetEntityType].

    Attributes:
        name (str):
            Required. The name of the entity type. Format:
            ``projects/<Project ID>/agent/entityTypes/<EntityType ID>``.
        language_code (str):
            Optional. The language used to access language-specific
            data. If not specified, the agent's default language is
            used. For more information, see `Multilingual intent and
            entity
            data <https://cloud.google.com/dialogflow/docs/agents-multilingual#intent-entity>`__.
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
    [EntityTypes.CreateEntityType][google.cloud.dialogflow.v2.EntityTypes.CreateEntityType].

    Attributes:
        parent (str):
            Required. The agent to create a entity type for. Format:
            ``projects/<Project ID>/agent``.
        entity_type (google.cloud.dialogflow_v2.types.EntityType):
            Required. The entity type to create.
        language_code (str):
            Optional. The language used to access language-specific
            data. If not specified, the agent's default language is
            used. For more information, see `Multilingual intent and
            entity
            data <https://cloud.google.com/dialogflow/docs/agents-multilingual#intent-entity>`__.
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
    [EntityTypes.UpdateEntityType][google.cloud.dialogflow.v2.EntityTypes.UpdateEntityType].

    Attributes:
        entity_type (google.cloud.dialogflow_v2.types.EntityType):
            Required. The entity type to update.
        language_code (str):
            Optional. The language used to access language-specific
            data. If not specified, the agent's default language is
            used. For more information, see `Multilingual intent and
            entity
            data <https://cloud.google.com/dialogflow/docs/agents-multilingual#intent-entity>`__.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The mask to control which fields
            get updated.
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
    [EntityTypes.DeleteEntityType][google.cloud.dialogflow.v2.EntityTypes.DeleteEntityType].

    Attributes:
        name (str):
            Required. The name of the entity type to delete. Format:
            ``projects/<Project ID>/agent/entityTypes/<EntityType ID>``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class BatchUpdateEntityTypesRequest(proto.Message):
    r"""The request message for
    [EntityTypes.BatchUpdateEntityTypes][google.cloud.dialogflow.v2.EntityTypes.BatchUpdateEntityTypes].

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        parent (str):
            Required. The name of the agent to update or create entity
            types in. Format: ``projects/<Project ID>/agent``.
        entity_type_batch_uri (str):
            The URI to a Google Cloud Storage file
            containing entity types to update or create. The
            file format can either be a serialized proto (of
            EntityBatch type) or a JSON object. Note: The
            URI must start with "gs://".

            This field is a member of `oneof`_ ``entity_type_batch``.
        entity_type_batch_inline (google.cloud.dialogflow_v2.types.EntityTypeBatch):
            The collection of entity types to update or
            create.

            This field is a member of `oneof`_ ``entity_type_batch``.
        language_code (str):
            Optional. The language used to access language-specific
            data. If not specified, the agent's default language is
            used. For more information, see `Multilingual intent and
            entity
            data <https://cloud.google.com/dialogflow/docs/agents-multilingual#intent-entity>`__.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The mask to control which fields
            get updated.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    entity_type_batch_uri: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="entity_type_batch",
    )
    entity_type_batch_inline: "EntityTypeBatch" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="entity_type_batch",
        message="EntityTypeBatch",
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=4,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=5,
        message=field_mask_pb2.FieldMask,
    )


class BatchUpdateEntityTypesResponse(proto.Message):
    r"""The response message for
    [EntityTypes.BatchUpdateEntityTypes][google.cloud.dialogflow.v2.EntityTypes.BatchUpdateEntityTypes].

    Attributes:
        entity_types (MutableSequence[google.cloud.dialogflow_v2.types.EntityType]):
            The collection of updated or created entity
            types.
    """

    entity_types: MutableSequence["EntityType"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="EntityType",
    )


class BatchDeleteEntityTypesRequest(proto.Message):
    r"""The request message for
    [EntityTypes.BatchDeleteEntityTypes][google.cloud.dialogflow.v2.EntityTypes.BatchDeleteEntityTypes].

    Attributes:
        parent (str):
            Required. The name of the agent to delete all entities types
            for. Format: ``projects/<Project ID>/agent``.
        entity_type_names (MutableSequence[str]):
            Required. The names entity types to delete. All names must
            point to the same agent as ``parent``.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    entity_type_names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchCreateEntitiesRequest(proto.Message):
    r"""The request message for
    [EntityTypes.BatchCreateEntities][google.cloud.dialogflow.v2.EntityTypes.BatchCreateEntities].

    Attributes:
        parent (str):
            Required. The name of the entity type to create entities in.
            Format:
            ``projects/<Project ID>/agent/entityTypes/<Entity Type ID>``.
        entities (MutableSequence[google.cloud.dialogflow_v2.types.EntityType.Entity]):
            Required. The entities to create.
        language_code (str):
            Optional. The language used to access language-specific
            data. If not specified, the agent's default language is
            used. For more information, see `Multilingual intent and
            entity
            data <https://cloud.google.com/dialogflow/docs/agents-multilingual#intent-entity>`__.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    entities: MutableSequence["EntityType.Entity"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="EntityType.Entity",
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=3,
    )


class BatchUpdateEntitiesRequest(proto.Message):
    r"""The request message for
    [EntityTypes.BatchUpdateEntities][google.cloud.dialogflow.v2.EntityTypes.BatchUpdateEntities].

    Attributes:
        parent (str):
            Required. The name of the entity type to update or create
            entities in. Format:
            ``projects/<Project ID>/agent/entityTypes/<Entity Type ID>``.
        entities (MutableSequence[google.cloud.dialogflow_v2.types.EntityType.Entity]):
            Required. The entities to update or create.
        language_code (str):
            Optional. The language used to access language-specific
            data. If not specified, the agent's default language is
            used. For more information, see `Multilingual intent and
            entity
            data <https://cloud.google.com/dialogflow/docs/agents-multilingual#intent-entity>`__.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The mask to control which fields
            get updated.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    entities: MutableSequence["EntityType.Entity"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="EntityType.Entity",
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=3,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=4,
        message=field_mask_pb2.FieldMask,
    )


class BatchDeleteEntitiesRequest(proto.Message):
    r"""The request message for
    [EntityTypes.BatchDeleteEntities][google.cloud.dialogflow.v2.EntityTypes.BatchDeleteEntities].

    Attributes:
        parent (str):
            Required. The name of the entity type to delete entries for.
            Format:
            ``projects/<Project ID>/agent/entityTypes/<Entity Type ID>``.
        entity_values (MutableSequence[str]):
            Required. The reference ``values`` of the entities to
            delete. Note that these are not fully-qualified names, i.e.
            they don't start with ``projects/<Project ID>``.
        language_code (str):
            Optional. The language used to access language-specific
            data. If not specified, the agent's default language is
            used. For more information, see `Multilingual intent and
            entity
            data <https://cloud.google.com/dialogflow/docs/agents-multilingual#intent-entity>`__.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    entity_values: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=3,
    )


class EntityTypeBatch(proto.Message):
    r"""This message is a wrapper around a collection of entity
    types.

    Attributes:
        entity_types (MutableSequence[google.cloud.dialogflow_v2.types.EntityType]):
            A collection of entity types.
    """

    entity_types: MutableSequence["EntityType"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="EntityType",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
