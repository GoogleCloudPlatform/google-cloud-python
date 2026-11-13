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

from google.apps.chat_v1.types import membership
from google.apps.chat_v1.types import space as gc_space

__protobuf__ = proto.module(
    package="google.chat.v1",
    manifest={
        "SetUpSpaceRequest",
    },
)


class SetUpSpaceRequest(proto.Message):
    r"""Request to create a space and add specified users to it.

    Attributes:
        space (google.apps.chat_v1.types.Space):
            Required. The ``Space.spaceType`` field is required.

            To create a space, set ``Space.spaceType`` to ``SPACE`` and
            set ``Space.displayName``. If you receive the error message
            ``ALREADY_EXISTS`` when setting up a space, try a different
            ``displayName``. An existing space within the Google
            Workspace organization might already use this display name.

            To create a group chat, set ``Space.spaceType`` to
            ``GROUP_CHAT``. Don't set ``Space.displayName``.

            To create a 1:1 conversation between humans, set
            ``Space.spaceType`` to ``DIRECT_MESSAGE`` and set
            ``Space.singleUserBotDm`` to ``false``. Don't set
            ``Space.displayName`` or ``Space.spaceDetails``.

            To create an 1:1 conversation between a human and the
            calling Chat app, set ``Space.spaceType`` to
            ``DIRECT_MESSAGE`` and ``Space.singleUserBotDm`` to
            ``true``. Don't set ``Space.displayName`` or
            ``Space.spaceDetails``.

            If a ``DIRECT_MESSAGE`` space already exists, that space is
            returned instead of creating a new space.
        request_id (str):
            Optional. A unique ID for this request. A random UUID is
            recommended. Specifying a request ID makes the request
            idempotent, which ensures that multiple identical requests
            with the same request ID result in only a single space being
            created. Subsequent requests with the same request ID return
            the existing space and do not update the space, even if the
            requested details differ from the current state.

            To use this field effectively:

            - Ensure that subsequent requests are identical and use the
              same authentication credentials as the original request.
            - If a space was already created with the provided request
              ID, the request returns that space. Note that the returned
              space might not be fully populated; the API echoes the
              space in your request with the system-assigned resource
              name populated. To retrieve the latest metadata for the
              space, call ``GetSpace``.
            - Reusing an existing request ID with a different
              authenticated user results in an error.
        memberships (MutableSequence[google.apps.chat_v1.types.Membership]):
            Optional. The Google Chat users or groups to invite to join
            the space. Omit the calling user, as they are added
            automatically.

            The set currently allows up to 49 memberships (in addition
            to the caller).

            For human membership, the ``Membership.member`` field must
            contain a ``user`` with ``name`` populated (format:
            ``users/{user}``) and ``type`` set to ``User.Type.HUMAN``.
            You can only add human users when setting up a space (adding
            Chat apps is only supported for direct message setup with
            the calling app). You can also add members using the user's
            email as an alias for {user}. For example, the ``user.name``
            can be ``users/example@gmail.com``. To invite Gmail users or
            users from external Google Workspace domains, user's email
            must be used for ``{user}``.

            For Google group membership, the ``Membership.group_member``
            field must contain a ``group`` with ``name`` populated
            (format ``groups/{group}``). You can only add Google groups
            when setting ``Space.spaceType`` to ``SPACE``.

            Optional when setting ``Space.spaceType`` to ``SPACE``.

            Required when setting ``Space.spaceType`` to ``GROUP_CHAT``,
            along with at least two memberships.

            Required when setting ``Space.spaceType`` to
            ``DIRECT_MESSAGE`` with a human user, along with exactly one
            membership.

            Must be empty when creating a 1:1 conversation between a
            human and the calling Chat app (when setting
            ``Space.spaceType`` to ``DIRECT_MESSAGE`` and
            ``Space.singleUserBotDm`` to ``true``).
    """

    space: gc_space.Space = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gc_space.Space,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    memberships: MutableSequence[membership.Membership] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=membership.Membership,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
