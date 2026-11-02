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
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

from google.apps.chat_v1.types import group, user

__protobuf__ = proto.module(
    package="google.chat.v1",
    manifest={
        "Membership",
        "CreateMembershipRequest",
        "UpdateMembershipRequest",
        "ListMembershipsRequest",
        "ListMembershipsResponse",
        "GetMembershipRequest",
        "DeleteMembershipRequest",
    },
)


class Membership(proto.Message):
    r"""Represents a membership relation in Google Chat, such as
    whether a user or Chat app is invited to, part of, or absent
    from a space.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. Resource name of the membership, assigned by the
            server.

            Format: ``spaces/{space}/members/{member}``
        state (google.apps.chat_v1.types.Membership.MembershipState):
            Output only. State of the membership.
        role (google.apps.chat_v1.types.Membership.MembershipRole):
            Optional. User's role within a Chat space, which determines
            their permitted actions in the space.

            This field can only be used as input in
            ``UpdateMembership``.
        member (google.apps.chat_v1.types.User):
            Optional. The Google Chat user or app the membership
            corresponds to. If your Chat app `authenticates as a
            user <https://developers.google.com/workspace/chat/authenticate-authorize-chat-user>`__,
            the output only populates the
            `user <https://developers.google.com/workspace/chat/api/reference/rest/v1/User>`__
            ``name`` and ``type`` fields for both internal and external
            users, unless they are members of the space or have a prior
            affinity, like a direct message (DM) conversation, with the
            calling user.

            This field is a member of `oneof`_ ``memberType``.
        group_member (google.apps.chat_v1.types.Group):
            Optional. The Google Group the membership corresponds to.

            Reading or mutating memberships for Google Groups requires
            `user
            authentication <https://developers.google.com/workspace/chat/authenticate-authorize-chat-user>`__.

            This field is a member of `oneof`_ ``memberType``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. Immutable. The creation time of the
            membership, such as when a member joined or was
            invited to join a space. This field is output
            only, except when used to import historical
            memberships in import mode spaces.
        delete_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. Immutable. The deletion time of the
            membership, such as when a member left or was
            removed from a space. This field is output only,
            except when used to import historical
            memberships in import mode spaces.
        affiliation (google.apps.chat_v1.types.Membership.Affiliation):
            Output only. A user's relationship to the Workspace
            organization that owns the space. In spaces owned by
            consumer accounts, the affiliation of all members is
            ``EXTERNAL``.
    """

    class MembershipState(proto.Enum):
        r"""Specifies the member's relationship with a space. Other
        membership states might be supported in the future.

        Values:
            MEMBERSHIP_STATE_UNSPECIFIED (0):
                Default value. Don't use.
            JOINED (1):
                The user is added to the space, and can
                participate in the space.
            INVITED (2):
                The user is invited to join the space, but
                hasn't joined it.
            NOT_A_MEMBER (3):
                The user doesn't belong to the space and
                doesn't have a pending invitation to join the
                space.
        """

        MEMBERSHIP_STATE_UNSPECIFIED = 0
        JOINED = 1
        INVITED = 2
        NOT_A_MEMBER = 3

    class MembershipRole(proto.Enum):
        r"""Represents a user's permitted actions in a Chat space. More
        enum values might be added in the future.

        Values:
            MEMBERSHIP_ROLE_UNSPECIFIED (0):
                Default value. For
                [users][google.chat.v1.Membership.member]: they aren't a
                member of the space, but can be invited. For [Google
                Groups][google.chat.v1.Membership.group_member]: they're
                always assigned this role (other enum values might be used
                in the future).
            ROLE_MEMBER (1):
                A member of the space. In the Chat UI, this role is called
                Member.

                The user has basic permissions, like sending messages to the
                space. Managers and owners can grant members additional
                permissions in a space, including:

                - Add or remove members.
                - Modify space details.
                - Turn history on or off.
                - Mention everyone in the space with ``@all``.
                - Manage Chat apps and webhooks installed in the space.

                In direct messages and unnamed group conversations, everyone
                has this role.
            ROLE_MANAGER (2):
                A space owner. In the Chat UI, this role is called Owner.

                The user has the complete set of space permissions to manage
                the space, including:

                - Change the role of other members in the space to member,
                  manager, or owner.
                - Delete the space.

                Only supported in
                [SpaceType.SPACE][google.chat.v1.Space.SpaceType] (named
                spaces).

                To learn more, see `Learn more about your role as a space
                owner or
                manager <https://support.google.com/chat/answer/11833441>`__.
            ROLE_ASSISTANT_MANAGER (4):
                A space manager. In the Chat UI, this role is called
                Manager.

                The user has all basic permissions of ``ROLE_MEMBER``, and
                can be granted a subset of administrative permissions by an
                owner. By default, managers have all the permissions of an
                owner except for the ability to:

                - Delete the space.
                - Make another space member an owner.
                - Change an owner's role.

                By default, managers permissions include but aren't limited
                to:

                - Make another member a manager.
                - Delete messages in the space.
                - Manage space permissions.
                - Receive notifications for requests to join the space if
                  the manager has the "manage members" permission in the
                  space settings.
                - Make a space discoverable.

                Only supported in
                [SpaceType.SPACE][google.chat.v1.Space.SpaceType] (named
                spaces).

                To learn more, see `Manage space
                settings <https://support.google.com/chat/answer/13340792>`__.
        """

        MEMBERSHIP_ROLE_UNSPECIFIED = 0
        ROLE_MEMBER = 1
        ROLE_MANAGER = 2
        ROLE_ASSISTANT_MANAGER = 4

    class Affiliation(proto.Enum):
        r"""Represents the affiliation of a user to the Google Workspace
        organization that owns the space. This enum may have more values
        added in the future.

        Values:
            AFFILIATION_UNSPECIFIED (0):
                Default value. This value is unused.
            INTERNAL (1):
                An account managed by the same Google
                Workspace organization that owns the space.
            EXTERNAL (2):
                An account external to the Google Workspace
                organization that owns the space (e.g., a
                consumer account, or an account managed by a
                different Workspace organization).
            MANAGED_EXTERNAL (3):
                An account managed by the Workspace
                organization that owns the space, but
                provisioned for a user who is external to the
                organization (e.g., a Guest user). To learn more
                about guests, see
                https://support.google.com/chat/answer/16997417.
        """

        AFFILIATION_UNSPECIFIED = 0
        INTERNAL = 1
        EXTERNAL = 2
        MANAGED_EXTERNAL = 3

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    state: MembershipState = proto.Field(
        proto.ENUM,
        number=2,
        enum=MembershipState,
    )
    role: MembershipRole = proto.Field(
        proto.ENUM,
        number=7,
        enum=MembershipRole,
    )
    member: user.User = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="memberType",
        message=user.User,
    )
    group_member: group.Group = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="memberType",
        message=group.Group,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    delete_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    affiliation: Affiliation = proto.Field(
        proto.ENUM,
        number=9,
        enum=Affiliation,
    )


class CreateMembershipRequest(proto.Message):
    r"""Request message for creating a membership.

    Attributes:
        parent (str):
            Required. The resource name of the space for
            which to create the membership.

            Format: spaces/{space}
        membership (google.apps.chat_v1.types.Membership):
            Required. The membership relation to create.

            The ``memberType`` field must contain a user with the
            ``user.name`` and ``user.type`` fields populated. The server
            will assign a resource name and overwrite anything
            specified.

            When a Chat app creates a membership relation for a human
            user, it must use certain authorization scopes and set
            specific values for certain fields:

            - When `authenticating as a
              user <https://developers.google.com/workspace/chat/authenticate-authorize-chat-user>`__,
              the ``chat.memberships`` authorization scope is required.

            - When `authenticating as an
              app <https://developers.google.com/workspace/chat/authenticate-authorize-chat-app>`__,
              the ``chat.app.memberships`` authorization scope is
              required.

            - Set ``user.type`` to ``HUMAN``, and set ``user.name`` with
              format ``users/{user}``, where ``{user}`` can be the email
              address for the user. For users in the same Workspace
              organization ``{user}`` can also be the ``id`` of the
              `person <https://developers.google.com/people/api/rest/v1/people>`__
              from the People API, or the ``id`` for the user in the
              Directory API. For example, if the People API Person
              profile ID for ``user@example.com`` is ``123456789``, you
              can add the user to the space by setting the
              ``membership.member.name`` to ``users/user@example.com``
              or ``users/123456789``.

            Inviting users external to the Workspace organization that
            owns the space requires `user
            authentication <https://developers.google.com/workspace/chat/authenticate-authorize-chat-user>`__.

            When a Chat app creates a membership relation for itself, it
            must `authenticate as a
            user <https://developers.google.com/workspace/chat/authenticate-authorize-chat-user>`__
            and use the ``chat.memberships.app`` scope, set
            ``user.type`` to ``BOT``, and set ``user.name`` to
            ``users/app``.
        use_admin_access (bool):
            Optional. When ``true``, the method runs using the user's
            Google Workspace administrator privileges.

            The calling user must be a Google Workspace administrator
            with the `manage chat and spaces conversations
            privilege <https://support.google.com/a/answer/13369245>`__.

            Requires the ``chat.admin.memberships`` `OAuth 2.0
            scope <https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes>`__.

            Creating app memberships or creating memberships for users
            outside the administrator's Google Workspace organization
            isn't supported using admin access.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    membership: "Membership" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Membership",
    )
    use_admin_access: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class UpdateMembershipRequest(proto.Message):
    r"""Request message for updating a membership.

    Attributes:
        membership (google.apps.chat_v1.types.Membership):
            Required. The membership to update. Only fields specified by
            ``update_mask`` are updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The field paths to update. Separate multiple
            values with commas or use ``*`` to update all field paths.

            Currently supported field paths:

            - ``role``
        use_admin_access (bool):
            Optional. When ``true``, the method runs using the user's
            Google Workspace administrator privileges.

            The calling user must be a Google Workspace administrator
            with the `manage chat and spaces conversations
            privilege <https://support.google.com/a/answer/13369245>`__.

            Requires the ``chat.admin.memberships`` `OAuth 2.0
            scope <https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes>`__.
    """

    membership: "Membership" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Membership",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )
    use_admin_access: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class ListMembershipsRequest(proto.Message):
    r"""Request message for listing memberships.

    Attributes:
        parent (str):
            Required. The resource name of the space for
            which to fetch a membership list.

            Format: spaces/{space}
        page_size (int):
            Optional. The maximum number of memberships to return. The
            service might return fewer than this value.

            If unspecified, at most 100 memberships are returned.

            The maximum value is 1000. If you use a value more than
            1000, it's automatically changed to 1000.

            Negative values return an ``INVALID_ARGUMENT`` error.
        page_token (str):
            Optional. A page token, received from a
            previous call to list memberships. Provide this
            parameter to retrieve the subsequent page.

            When paginating, all other parameters provided
            should match the call that provided the page
            token. Passing different values to the other
            parameters might lead to unexpected results.
        filter (str):
            Optional. A query filter.

            You can filter memberships by a member's role
            (```role`` <https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces.members#membershiprole>`__)
            and type
            (```member.type`` <https://developers.google.com/workspace/chat/api/reference/rest/v1/User#type>`__).

            To filter by role, set ``role`` to ``ROLE_MEMBER`` or
            ``ROLE_MANAGER``.

            To filter by type, set ``member.type`` to ``HUMAN`` or
            ``BOT``. You can also filter for ``member.type`` using the
            ``!=`` operator.

            To filter by both role and type, use the ``AND`` operator.
            To filter by either role or type, use the ``OR`` operator.

            Either ``member.type = "HUMAN"`` or ``member.type != "BOT"``
            is required when ``use_admin_access`` is set to true. Other
            member type filters will be rejected.

            For example, the following queries are valid:

            ::

               role = "ROLE_MANAGER" OR role = "ROLE_MEMBER"
               member.type = "HUMAN" AND role = "ROLE_MANAGER"

               member.type != "BOT"

            The following queries are invalid:

            ::

               member.type = "HUMAN" AND member.type = "BOT"
               role = "ROLE_MANAGER" AND role = "ROLE_MEMBER"

            Invalid queries are rejected by the server with an
            ``INVALID_ARGUMENT`` error.
        show_groups (bool):
            Optional. When ``true``, also returns memberships associated
            with a [Google
            Group][google.chat.v1.Membership.group_member], in addition
            to other types of memberships. If a
            [filter][google.chat.v1.ListMembershipsRequest.filter] is
            set, [Google Group][google.chat.v1.Membership.group_member]
            memberships that don't match the filter criteria aren't
            returned.
        show_invited (bool):
            Optional. When ``true``, also returns memberships associated
            with
            [invited][google.chat.v1.Membership.MembershipState.INVITED]
            members, in addition to other types of memberships. If a
            filter is set,
            [invited][google.chat.v1.Membership.MembershipState.INVITED]
            memberships that don't match the filter criteria aren't
            returned.

            Currently requires `user
            authentication <https://developers.google.com/workspace/chat/authenticate-authorize-chat-user>`__.
        use_admin_access (bool):
            Optional. When ``true``, the method runs using the user's
            Google Workspace administrator privileges.

            The calling user must be a Google Workspace administrator
            with the `manage chat and spaces conversations
            privilege <https://support.google.com/a/answer/13369245>`__.

            Requires either the ``chat.admin.memberships.readonly`` or
            ``chat.admin.memberships`` `OAuth 2.0
            scope <https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes>`__.

            Listing app memberships in a space isn't supported when
            using admin access.
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
        number=5,
    )
    show_groups: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    show_invited: bool = proto.Field(
        proto.BOOL,
        number=7,
    )
    use_admin_access: bool = proto.Field(
        proto.BOOL,
        number=8,
    )


class ListMembershipsResponse(proto.Message):
    r"""Response to list memberships of the space.

    Attributes:
        memberships (MutableSequence[google.apps.chat_v1.types.Membership]):
            Unordered list. List of memberships in the
            requested (or first) page.
        next_page_token (str):
            A token that you can send as ``pageToken`` to retrieve the
            next page of results. If empty, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    memberships: MutableSequence["Membership"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Membership",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetMembershipRequest(proto.Message):
    r"""Request to get a membership of a space.

    Attributes:
        name (str):
            Required. Resource name of the membership to retrieve.

            To get the app's own membership `by using user
            authentication <https://developers.google.com/workspace/chat/authenticate-authorize-chat-user>`__,
            you can optionally use ``spaces/{space}/members/app``.

            Format: ``spaces/{space}/members/{member}`` or
            ``spaces/{space}/members/app``

            You can use the user's email as an alias for ``{member}``.
            For example, ``spaces/{space}/members/example@gmail.com``
            where ``example@gmail.com`` is the email of the Google Chat
            user.
        use_admin_access (bool):
            Optional. When ``true``, the method runs using the user's
            Google Workspace administrator privileges.

            The calling user must be a Google Workspace administrator
            with the `manage chat and spaces conversations
            privilege <https://support.google.com/a/answer/13369245>`__.

            Requires the ``chat.admin.memberships`` or
            ``chat.admin.memberships.readonly`` `OAuth 2.0
            scopes <https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes>`__.

            Getting app memberships in a space isn't supported when
            using admin access.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    use_admin_access: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class DeleteMembershipRequest(proto.Message):
    r"""Request to delete a membership in a space.

    Attributes:
        name (str):
            Required. Resource name of the membership to delete. Chat
            apps can delete human users' or their own memberships. Chat
            apps can't delete other apps' memberships.

            When deleting a human membership, requires the
            ``chat.memberships`` scope with `user
            authentication <https://developers.google.com/workspace/chat/authenticate-authorize-chat-user>`__
            or the ``chat.memberships.app`` scope with `app
            authentication <https://developers.google.com/workspace/chat/authenticate-authorize-chat-app>`__
            and the ``spaces/{space}/members/{member}`` format. You can
            use the email as an alias for ``{member}``. For example,
            ``spaces/{space}/members/example@gmail.com`` where
            ``example@gmail.com`` is the email of the Google Chat user.

            When deleting an app membership, requires the
            ``chat.memberships.app`` scope and
            ``spaces/{space}/members/app`` format.

            Format: ``spaces/{space}/members/{member}`` or
            ``spaces/{space}/members/app``.
        use_admin_access (bool):
            Optional. When ``true``, the method runs using the user's
            Google Workspace administrator privileges.

            The calling user must be a Google Workspace administrator
            with the `manage chat and spaces conversations
            privilege <https://support.google.com/a/answer/13369245>`__.

            Requires the ``chat.admin.memberships`` `OAuth 2.0
            scope <https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes>`__.

            Deleting app memberships in a space isn't supported using
            admin access.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    use_admin_access: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
