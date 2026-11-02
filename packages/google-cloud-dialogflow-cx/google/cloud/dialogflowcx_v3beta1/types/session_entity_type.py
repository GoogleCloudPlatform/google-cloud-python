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

from google.cloud.dialogflowcx_v3beta1.types import entity_type

__protobuf__ = proto.module(
    package="google.cloud.dialogflow.cx.v3beta1",
    manifest={
        "SessionEntityType",
        "ListSessionEntityTypesRequest",
        "ListSessionEntityTypesResponse",
        "GetSessionEntityTypeRequest",
        "CreateSessionEntityTypeRequest",
        "UpdateSessionEntityTypeRequest",
        "DeleteSessionEntityTypeRequest",
    },
)


class SessionEntityType(proto.Message):
    r"""Session entity types are referred to as **User** entity types and
    are entities that are built for an individual user such as
    favorites, preferences, playlists, and so on.

    You can redefine a session entity type at the session level to
    extend or replace a [custom entity
    type][google.cloud.dialogflow.cx.v3beta1.EntityType] at the user
    session level (we refer to the entity types defined at the agent
    level as "custom entity types").

    Note: session entity types apply to all queries, regardless of the
    language.

    For more information about entity types, see the `Dialogflow
    documentation <https://cloud.google.com/dialogflow/docs/entities-overview>`__.

    Attributes:
        name (str):
            Required. The unique identifier of the session entity type.
            Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/sessions/<SessionID>/entityTypes/<EntityTypeID>``
            or
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/environments/<EnvironmentID>/sessions/<SessionID>/entityTypes/<EntityTypeID>``.
            If ``Environment ID`` is not specified, we assume default
            'draft' environment.
        entity_override_mode (google.cloud.dialogflowcx_v3beta1.types.SessionEntityType.EntityOverrideMode):
            Required. Indicates whether the additional
            data should override or supplement the custom
            entity type definition.
        entities (MutableSequence[google.cloud.dialogflowcx_v3beta1.types.EntityType.Entity]):
            Required. The collection of entities to
            override or supplement the custom entity type.
    """

    class EntityOverrideMode(proto.Enum):
        r"""The types of modifications for the session entity type.

        Values:
            ENTITY_OVERRIDE_MODE_UNSPECIFIED (0):
                Not specified. This value should be never
                used.
            ENTITY_OVERRIDE_MODE_OVERRIDE (1):
                The collection of session entities overrides
                the collection of entities in the corresponding
                custom entity type.
            ENTITY_OVERRIDE_MODE_SUPPLEMENT (2):
                The collection of session entities extends the collection of
                entities in the corresponding custom entity type.

                Note: Even in this override mode calls to
                ``ListSessionEntityTypes``, ``GetSessionEntityType``,
                ``CreateSessionEntityType`` and ``UpdateSessionEntityType``
                only return the additional entities added in this session
                entity type. If you want to get the supplemented list,
                please call
                [EntityTypes.GetEntityType][google.cloud.dialogflow.cx.v3beta1.EntityTypes.GetEntityType]
                on the custom entity type and merge.
        """

        ENTITY_OVERRIDE_MODE_UNSPECIFIED = 0
        ENTITY_OVERRIDE_MODE_OVERRIDE = 1
        ENTITY_OVERRIDE_MODE_SUPPLEMENT = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    entity_override_mode: EntityOverrideMode = proto.Field(
        proto.ENUM,
        number=3,
        enum=EntityOverrideMode,
    )
    entities: MutableSequence[entity_type.EntityType.Entity] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=entity_type.EntityType.Entity,
    )


class ListSessionEntityTypesRequest(proto.Message):
    r"""The request message for
    [SessionEntityTypes.ListSessionEntityTypes][google.cloud.dialogflow.cx.v3beta1.SessionEntityTypes.ListSessionEntityTypes].

    Attributes:
        parent (str):
            Required. The session to list all session entity types from.
            Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/sessions/<SessionID>``
            or
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/environments/<EnvironmentID>/sessions/<SessionID>``.
            If ``Environment ID`` is not specified, we assume default
            'draft' environment.
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
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListSessionEntityTypesResponse(proto.Message):
    r"""The response message for
    [SessionEntityTypes.ListSessionEntityTypes][google.cloud.dialogflow.cx.v3beta1.SessionEntityTypes.ListSessionEntityTypes].

    Attributes:
        session_entity_types (MutableSequence[google.cloud.dialogflowcx_v3beta1.types.SessionEntityType]):
            The list of session entity types. There will be a maximum
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

    session_entity_types: MutableSequence["SessionEntityType"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="SessionEntityType",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetSessionEntityTypeRequest(proto.Message):
    r"""The request message for
    [SessionEntityTypes.GetSessionEntityType][google.cloud.dialogflow.cx.v3beta1.SessionEntityTypes.GetSessionEntityType].

    Attributes:
        name (str):
            Required. The name of the session entity type. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/sessions/<SessionID>/entityTypes/<EntityTypeID>``
            or
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/environments/<EnvironmentID>/sessions/<SessionID>/entityTypes/<EntityTypeID>``.
            If ``Environment ID`` is not specified, we assume default
            'draft' environment.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateSessionEntityTypeRequest(proto.Message):
    r"""The request message for
    [SessionEntityTypes.CreateSessionEntityType][google.cloud.dialogflow.cx.v3beta1.SessionEntityTypes.CreateSessionEntityType].

    Attributes:
        parent (str):
            Required. The session to create a session entity type for.
            Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/sessions/<SessionID>``
            or
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/environments/<EnvironmentID>/sessions/<SessionID>``.
            If ``Environment ID`` is not specified, we assume default
            'draft' environment.
        session_entity_type (google.cloud.dialogflowcx_v3beta1.types.SessionEntityType):
            Required. The session entity type to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    session_entity_type: "SessionEntityType" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="SessionEntityType",
    )


class UpdateSessionEntityTypeRequest(proto.Message):
    r"""The request message for
    [SessionEntityTypes.UpdateSessionEntityType][google.cloud.dialogflow.cx.v3beta1.SessionEntityTypes.UpdateSessionEntityType].

    Attributes:
        session_entity_type (google.cloud.dialogflowcx_v3beta1.types.SessionEntityType):
            Required. The session entity type to update. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/sessions/<SessionID>/entityTypes/<EntityTypeID>``
            or
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/environments/<EnvironmentID>/sessions/<SessionID>/entityTypes/<EntityTypeID>``.
            If ``Environment ID`` is not specified, we assume default
            'draft' environment.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The mask to control which fields get updated.
    """

    session_entity_type: "SessionEntityType" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="SessionEntityType",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteSessionEntityTypeRequest(proto.Message):
    r"""The request message for
    [SessionEntityTypes.DeleteSessionEntityType][google.cloud.dialogflow.cx.v3beta1.SessionEntityTypes.DeleteSessionEntityType].

    Attributes:
        name (str):
            Required. The name of the session entity type to delete.
            Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/sessions/<SessionID>/entityTypes/<EntityTypeID>``
            or
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/environments/<EnvironmentID>/sessions/<SessionID>/entityTypes/<EntityTypeID>``.
            If ``Environment ID`` is not specified, we assume default
            'draft' environment.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
