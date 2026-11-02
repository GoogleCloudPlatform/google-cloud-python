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

from google.shopping.merchant_accounts_v1.types import accessright

__protobuf__ = proto.module(
    package="google.shopping.merchant.accounts.v1",
    manifest={
        "User",
        "GetUserRequest",
        "CreateUserRequest",
        "DeleteUserRequest",
        "UpdateUserRequest",
        "ListUsersRequest",
        "ListUsersResponse",
        "VerifySelfRequest",
    },
)


class User(proto.Message):
    r"""The ``User`` resource represents a user associated with a Merchant
    Center account. It is used to manage user permissions and access
    rights within the account. For more information, see `Frequently
    asked questions about people and access
    levels <//support.google.com/merchants/answer/12160472>`__.

    Attributes:
        name (str):
            Identifier. The resource name of the user. Format:
            ``accounts/{account}/user/{email}``

            Use ``me`` to refer to your own email address, for example
            ``accounts/{account}/users/me``.
        state (google.shopping.merchant_accounts_v1.types.User.State):
            Output only. The state of the user.
        access_rights (MutableSequence[google.shopping.merchant_accounts_v1.types.AccessRight]):
            Required. The `access
            rights <https://support.google.com/merchants/answer/12160472?sjid=6789834943175119429-EU#accesstypes>`__
            the user has.
    """

    class State(proto.Enum):
        r"""The state represents the possible statuses of a user. It is an
        output-only field that is set to ``PENDING`` when a user is invited
        to an account and changes to ``VERIFIED`` once the user accepts the
        invitation.

        Values:
            STATE_UNSPECIFIED (0):
                Default value. This value is unused.
            PENDING (1):
                The user is pending confirmation. In this
                state, the user first needs to accept the
                invitation before performing other actions.
            VERIFIED (2):
                The user is verified.
        """

        STATE_UNSPECIFIED = 0
        PENDING = 1
        VERIFIED = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=2,
        enum=State,
    )
    access_rights: MutableSequence[accessright.AccessRight] = proto.RepeatedField(
        proto.ENUM,
        number=4,
        enum=accessright.AccessRight,
    )


class GetUserRequest(proto.Message):
    r"""Request message for the ``GetUser`` method.

    Attributes:
        name (str):
            Required. The name of the user to retrieve. Format:
            ``accounts/{account}/users/{email}``

            It is also possible to retrieve the user corresponding to
            the caller by using ``me`` rather than an email address as
            in ``accounts/{account}/users/me``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateUserRequest(proto.Message):
    r"""Request message for the ``CreateUser`` method.

    Attributes:
        parent (str):
            Required. The resource name of the account for which a user
            will be created. Format: ``accounts/{account}``
        user_id (str):
            Required. The email address of the user (for example,
            ``john.doe@gmail.com``).
        user (google.shopping.merchant_accounts_v1.types.User):
            Optional. The user to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    user_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    user: "User" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="User",
    )


class DeleteUserRequest(proto.Message):
    r"""Request message for the ``DeleteUser`` method.

    Attributes:
        name (str):
            Required. The name of the user to delete. Format:
            ``accounts/{account}/users/{email}``

            It is also possible to delete the user corresponding to the
            caller by using ``me`` rather than an email address as in
            ``accounts/{account}/users/me``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateUserRequest(proto.Message):
    r"""Request message for the ``UpdateUser`` method.

    Attributes:
        user (google.shopping.merchant_accounts_v1.types.User):
            Required. The new version of the user.

            Use ``me`` to refer to your own email address, for example
            ``accounts/{account}/users/me``.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. List of fields being updated.

            The following fields are supported (in both ``snake_case``
            and ``lowerCamelCase``):

            - ``access_rights``
    """

    user: "User" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="User",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class ListUsersRequest(proto.Message):
    r"""Request message for the ``ListUsers`` method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of users.
            Format: ``accounts/{account}``
        page_size (int):
            Optional. The maximum number of users to
            return. The service may return fewer than this
            value. If unspecified, at most 50 users will be
            returned. The maximum value is 100; values above
            100 will be coerced to 100
        page_token (str):
            Optional. A page token, received from a previous
            ``ListUsers`` call. Provide this to retrieve the subsequent
            page.

            When paginating, all other parameters provided to
            ``ListUsers`` must match the call that provided the page
            token.
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


class ListUsersResponse(proto.Message):
    r"""Response message for the ``ListUsers`` method.

    Attributes:
        users (MutableSequence[google.shopping.merchant_accounts_v1.types.User]):
            The users from the specified account.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    users: MutableSequence["User"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="User",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class VerifySelfRequest(proto.Message):
    r"""Request message for the ``VerifySelf`` method.

    Attributes:
        account (str):
            Required. The name of the account under which the caller is
            a user. Format: ``accounts/{account}``
    """

    account: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
