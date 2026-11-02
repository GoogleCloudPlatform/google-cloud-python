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

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore


__protobuf__ = proto.module(
    package='google.showcase.v1beta1',
    manifest={
        'User',
        'CreateUserRequest',
        'GetUserRequest',
        'UpdateUserRequest',
        'DeleteUserRequest',
        'ListUsersRequest',
        'ListUsersResponse',
    },
)


class User(proto.Message):
    r"""A user.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            The resource name of the user.
        display_name (str):
            The display_name of the user.
        email (str):
            The email address of the user.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            The timestamp at which the user was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            The latest timestamp at which the user was
            updated.
        age (int):
            The age of the user in years.

            This field is a member of `oneof`_ ``_age``.
        height_feet (float):
            The height of the user in feet.

            This field is a member of `oneof`_ ``_height_feet``.
        nickname (str):
            The nickname of the user.

            (-- aip.dev/not-precedent: An empty string is a valid
            nickname. Ordinarily, proto3_optional should not be used on
            a ``string`` field. --)

            This field is a member of `oneof`_ ``_nickname``.
        enable_notifications (bool):
            Enables the receiving of notifications. The default is true
            if unset.

            (-- aip.dev/not-precedent: The default for the feature is
            true. Ordinarily, the default for a ``bool`` field should be
            false. --)

            This field is a member of `oneof`_ ``_enable_notifications``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    email: str = proto.Field(
        proto.STRING,
        number=3,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    age: int = proto.Field(
        proto.INT32,
        number=6,
        optional=True,
    )
    height_feet: float = proto.Field(
        proto.DOUBLE,
        number=7,
        optional=True,
    )
    nickname: str = proto.Field(
        proto.STRING,
        number=8,
        optional=True,
    )
    enable_notifications: bool = proto.Field(
        proto.BOOL,
        number=9,
        optional=True,
    )


class CreateUserRequest(proto.Message):
    r"""The request message for the
    google.showcase.v1beta1.Identity\CreateUser method.

    Attributes:
        user (google.showcase_v1beta1.types.User):
            The user to create.
    """

    user: 'User' = proto.Field(
        proto.MESSAGE,
        number=1,
        message='User',
    )


class GetUserRequest(proto.Message):
    r"""The request message for the
    google.showcase.v1beta1.Identity\GetUser method.

    Attributes:
        name (str):
            The resource name of the requested user.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateUserRequest(proto.Message):
    r"""The request message for the
    google.showcase.v1beta1.Identity\UpdateUser method.

    Attributes:
        user (google.showcase_v1beta1.types.User):
            The user to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The field mask to determine which fields are
            to be updated. If empty, the server will assume
            all fields are to be updated.
    """

    user: 'User' = proto.Field(
        proto.MESSAGE,
        number=1,
        message='User',
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteUserRequest(proto.Message):
    r"""The request message for the
    google.showcase.v1beta1.Identity\DeleteUser method.

    Attributes:
        name (str):
            The resource name of the user to delete.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListUsersRequest(proto.Message):
    r"""The request message for the
    google.showcase.v1beta1.Identity\ListUsers method.

    Attributes:
        page_size (int):
            The maximum number of users to return. Server
            may return fewer users than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            The value of
            google.showcase.v1beta1.ListUsersResponse.next_page_token
            returned from the previous call to
            ``google.showcase.v1beta1.Identity\ListUsers`` method.
    """

    page_size: int = proto.Field(
        proto.INT32,
        number=1,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListUsersResponse(proto.Message):
    r"""The response message for the
    google.showcase.v1beta1.Identity\ListUsers method.

    Attributes:
        users (MutableSequence[google.showcase_v1beta1.types.User]):
            The list of users.
        next_page_token (str):
            A token to retrieve next page of results. Pass this value in
            ListUsersRequest.page_token field in the subsequent call to
            ``google.showcase.v1beta1.Message\ListUsers`` method to
            retrieve the next page of results.
    """

    @property
    def raw_page(self):
        return self

    users: MutableSequence['User'] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message='User',
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
