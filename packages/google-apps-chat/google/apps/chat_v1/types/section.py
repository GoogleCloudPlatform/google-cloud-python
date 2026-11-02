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
    package="google.chat.v1",
    manifest={
        "Section",
        "SectionItem",
        "CreateSectionRequest",
        "DeleteSectionRequest",
        "UpdateSectionRequest",
        "ListSectionsRequest",
        "ListSectionsResponse",
        "PositionSectionRequest",
        "PositionSectionResponse",
        "ListSectionItemsRequest",
        "ListSectionItemsResponse",
        "MoveSectionItemRequest",
        "MoveSectionItemResponse",
    },
)


class Section(proto.Message):
    r"""Represents a
    `section <https://support.google.com/chat/answer/16059854>`__ in
    Google Chat. Sections help users organize their spaces. There are
    two types of sections:

    1. **System Sections:** These are predefined sections managed by
       Google Chat. Their resource names are fixed, and they cannot be
       created, deleted, or have their ``display_name`` modified.
       Examples include:

       - ``users/{user}/sections/default-direct-messages``
       - ``users/{user}/sections/default-spaces``
       - ``users/{user}/sections/default-apps``

    2. **Custom Sections:** These are sections created and managed by
       the user. Creating a custom section using ``CreateSection``
       **requires** a ``display_name``. Custom sections can be updated
       using ``UpdateSection`` and deleted using ``DeleteSection``.

    Attributes:
        name (str):
            Identifier. Resource name of the section.

            For system sections, the section ID is a constant string:

            - DEFAULT_DIRECT_MESSAGES:
              ``users/{user}/sections/default-direct-messages``
            - DEFAULT_SPACES: ``users/{user}/sections/default-spaces``
            - DEFAULT_APPS: ``users/{user}/sections/default-apps``

            Format: ``users/{user}/sections/{section}``
        display_name (str):
            Optional. The section's display name. Only populated for
            sections of type ``CUSTOM_SECTION``. Supports up to 80
            characters. Required when creating a ``CUSTOM_SECTION``.
        sort_order (int):
            Output only. The order of the section in relation to other
            sections. Sections with a lower ``sort_order`` value appear
            before sections with a higher value.
        type_ (google.apps.chat_v1.types.Section.SectionType):
            Required. The type of the section.
    """

    class SectionType(proto.Enum):
        r"""Section types.

        Values:
            SECTION_TYPE_UNSPECIFIED (0):
                Unspecified section type.
            CUSTOM_SECTION (1):
                Custom section.
            DEFAULT_DIRECT_MESSAGES (2):
                Default section containing
                `DIRECT_MESSAGE <https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces#spacetype>`__
                between two human users or
                `GROUP_CHAT <https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces#spacetype>`__
                spaces that don't belong to any custom section.
            DEFAULT_SPACES (3):
                Default spaces that don't belong to any
                custom section.
            DEFAULT_APPS (6):
                Default section containing a user's installed
                apps.
        """

        SECTION_TYPE_UNSPECIFIED = 0
        CUSTOM_SECTION = 1
        DEFAULT_DIRECT_MESSAGES = 2
        DEFAULT_SPACES = 3
        DEFAULT_APPS = 6

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    sort_order: int = proto.Field(
        proto.INT32,
        number=3,
    )
    type_: SectionType = proto.Field(
        proto.ENUM,
        number=4,
        enum=SectionType,
    )


class SectionItem(proto.Message):
    r"""A user's defined section item. This is used to represent
    section items, such as spaces, grouped under a section.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the section item.

            Format: ``users/{user}/sections/{section}/items/{item}``
        space (str):
            Optional. The space resource name.

            Format: ``spaces/{space}``

            This field is a member of `oneof`_ ``item``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    space: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="item",
    )


class CreateSectionRequest(proto.Message):
    r"""Request message for creating a section.

    Attributes:
        parent (str):
            Required. The parent resource name where the section is
            created.

            Format: ``users/{user}``
        section (google.apps.chat_v1.types.Section):
            Required. The section to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    section: "Section" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Section",
    )


class DeleteSectionRequest(proto.Message):
    r"""Request message for deleting a section. `Developer
    Preview <https://developers.google.com/workspace/preview>`__.

    Attributes:
        name (str):
            Required. The name of the section to delete.

            Format: ``users/{user}/sections/{section}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateSectionRequest(proto.Message):
    r"""Request message for updating a section.

    Attributes:
        section (google.apps.chat_v1.types.Section):
            Required. The section to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The mask to specify which fields to update.

            Currently supported field paths:

            - ``display_name``
    """

    section: "Section" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Section",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class ListSectionsRequest(proto.Message):
    r"""Request message for listing sections.

    Attributes:
        parent (str):
            Required. The parent, which is the user resource name that
            owns this collection of sections. Only supports listing
            sections for the calling user. To refer to the calling user,
            set one of the following:

            - The ``me`` alias. For example, ``users/me``.

            - Their Workspace email address. For example,
              ``users/user@example.com``.

            - Their user id. For example, ``users/123456789``.

            Format: ``users/{user}``
        page_size (int):
            Optional. The maximum number of sections to return. The
            service may return fewer than this value.

            If unspecified, at most 10 sections will be returned.

            The maximum value is 100. If you use a value more than 100,
            it's automatically changed to 100.

            Negative values return an ``INVALID_ARGUMENT`` error.
        page_token (str):
            Optional. A page token, received from a
            previous list sections call. Provide this to
            retrieve the subsequent page.

            When paginating, all other parameters provided
            should match the call that provided the page
            token. Passing different values to the other
            parameters might lead to unexpected results.
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


class ListSectionsResponse(proto.Message):
    r"""Response message for listing sections.

    Attributes:
        sections (MutableSequence[google.apps.chat_v1.types.Section]):
            The sections from the specified user.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    sections: MutableSequence["Section"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Section",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class PositionSectionRequest(proto.Message):
    r"""Request message for positioning a section.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Required. The resource name of the section to position.

            Format: ``users/{user}/sections/{section}``
        sort_order (int):
            Optional. The absolute position of the
            section in the list of sections. The position
            must be greater than 0. If the position is
            greater than the number of sections, the section
            will be appended to the end of the list. This
            operation inserts the section at the given
            position and shifts the original section at that
            position, and those below it, to the next
            position.

            This field is a member of `oneof`_ ``position``.
        relative_position (google.apps.chat_v1.types.PositionSectionRequest.Position):
            Optional. The relative position of the
            section in the list of sections.

            This field is a member of `oneof`_ ``position``.
    """

    class Position(proto.Enum):
        r"""The position of the section.

        Values:
            POSITION_UNSPECIFIED (0):
                Unspecified position.
            START (1):
                Start of the list of sections.
            END (2):
                End of the list of sections.
        """

        POSITION_UNSPECIFIED = 0
        START = 1
        END = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    sort_order: int = proto.Field(
        proto.INT32,
        number=2,
        oneof="position",
    )
    relative_position: Position = proto.Field(
        proto.ENUM,
        number=3,
        oneof="position",
        enum=Position,
    )


class PositionSectionResponse(proto.Message):
    r"""Response message for positioning a section.

    Attributes:
        section (google.apps.chat_v1.types.Section):
            The updated section.
    """

    section: "Section" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Section",
    )


class ListSectionItemsRequest(proto.Message):
    r"""Request message for listing section items.

    Attributes:
        parent (str):
            Required. The parent, which is the section resource name
            that owns this collection of section items. Only supports
            listing section items for the calling user.

            When you're filtering by space, use the wildcard ``-`` to
            search across all sections. For example,
            ``users/{user}/sections/-``.

            Format: ``users/{user}/sections/{section}``
        page_size (int):
            Optional. The maximum number of section items to return. The
            service may return fewer than this value.

            If unspecified, at most 10 section items will be returned.

            The maximum value is 100. If you use a value more than 100,
            it's automatically changed to 100.

            Negative values return an ``INVALID_ARGUMENT`` error.
        page_token (str):
            Optional. A page token, received from a
            previous list section items call. Provide this
            to retrieve the subsequent page.

            When paginating, all other parameters provided
            should match the call that provided the page
            token. Passing different values to the other
            parameters might lead to unexpected results.
        filter (str):
            Optional. A query filter.

            Currently only supports filtering by space.

            For example, ``space = spaces/{space}``.

            Invalid queries are rejected with an ``INVALID_ARGUMENT``
            error.
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
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListSectionItemsResponse(proto.Message):
    r"""Response message for listing section items.

    Attributes:
        section_items (MutableSequence[google.apps.chat_v1.types.SectionItem]):
            The section items from the specified section.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    section_items: MutableSequence["SectionItem"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="SectionItem",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class MoveSectionItemRequest(proto.Message):
    r"""Request message for moving a section item across sections.

    Attributes:
        name (str):
            Required. The resource name of the section item to move.

            Format: ``users/{user}/sections/{section}/items/{item}``
        target_section (str):
            Required. The resource name of the section to move the
            section item to.

            Format: ``users/{user}/sections/{section}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    target_section: str = proto.Field(
        proto.STRING,
        number=2,
    )


class MoveSectionItemResponse(proto.Message):
    r"""Response message for moving a section item.

    Attributes:
        section_item (google.apps.chat_v1.types.SectionItem):
            The updated section item.
    """

    section_item: "SectionItem" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="SectionItem",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
