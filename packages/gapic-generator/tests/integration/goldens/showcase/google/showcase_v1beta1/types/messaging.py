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
import google.rpc.error_details_pb2 as error_details_pb2  # type: ignore


__protobuf__ = proto.module(
    package='google.showcase.v1beta1',
    manifest={
        'Room',
        'CreateRoomRequest',
        'GetRoomRequest',
        'UpdateRoomRequest',
        'DeleteRoomRequest',
        'ListRoomsRequest',
        'ListRoomsResponse',
        'Blurb',
        'CreateBlurbRequest',
        'GetBlurbRequest',
        'UpdateBlurbRequest',
        'DeleteBlurbRequest',
        'ListBlurbsRequest',
        'ListBlurbsResponse',
        'SearchBlurbsRequest',
        'SearchBlurbsMetadata',
        'SearchBlurbsResponse',
        'StreamBlurbsRequest',
        'StreamBlurbsResponse',
        'SendBlurbsResponse',
        'ConnectRequest',
    },
)


class Room(proto.Message):
    r"""A chat room.

    Attributes:
        name (str):
            The resource name of the chat room.
        display_name (str):
            The human readable name of the chat room.
        description (str):
            The description of the chat room.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            The timestamp at which the room was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            The latest timestamp at which the room was
            updated.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
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


class CreateRoomRequest(proto.Message):
    r"""The request message for the
    google.showcase.v1beta1.Messaging\CreateRoom method.

    Attributes:
        room (google.showcase_v1beta1.types.Room):
            The room to create.
    """

    room: 'Room' = proto.Field(
        proto.MESSAGE,
        number=1,
        message='Room',
    )


class GetRoomRequest(proto.Message):
    r"""The request message for the
    google.showcase.v1beta1.Messaging\GetRoom method.

    Attributes:
        name (str):
            The resource name of the requested room.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateRoomRequest(proto.Message):
    r"""The request message for the
    google.showcase.v1beta1.Messaging\UpdateRoom method.

    Attributes:
        room (google.showcase_v1beta1.types.Room):
            The room to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The field mask to determine which fields are
            to be updated. If empty, the server will assume
            all fields are to be updated.
    """

    room: 'Room' = proto.Field(
        proto.MESSAGE,
        number=1,
        message='Room',
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteRoomRequest(proto.Message):
    r"""The request message for the
    google.showcase.v1beta1.Messaging\DeleteRoom method.

    Attributes:
        name (str):
            The resource name of the requested room.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListRoomsRequest(proto.Message):
    r"""The request message for the
    google.showcase.v1beta1.Messaging\ListRooms method.

    Attributes:
        page_size (int):
            The maximum number of rooms return. Server
            may return fewer rooms than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            The value of
            google.showcase.v1beta1.ListRoomsResponse.next_page_token
            returned from the previous call to
            ``google.showcase.v1beta1.Messaging\ListRooms`` method.
    """

    page_size: int = proto.Field(
        proto.INT32,
        number=1,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListRoomsResponse(proto.Message):
    r"""The response message for the
    google.showcase.v1beta1.Messaging\ListRooms method.

    Attributes:
        rooms (MutableSequence[google.showcase_v1beta1.types.Room]):
            The list of rooms.
        next_page_token (str):
            A token to retrieve next page of results. Pass this value in
            ListRoomsRequest.page_token field in the subsequent call to
            ``google.showcase.v1beta1.Messaging\ListRooms`` method to
            retrieve the next page of results.
    """

    @property
    def raw_page(self):
        return self

    rooms: MutableSequence['Room'] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message='Room',
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class Blurb(proto.Message):
    r"""This protocol buffer message represents a blurb sent to a
    chat room or posted on a user profile.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            The resource name of the chat room.
        user (str):
            The resource name of the blurb's author.
        text (str):
            The textual content of this blurb.

            This field is a member of `oneof`_ ``content``.
        image (bytes):
            The image content of this blurb.

            This field is a member of `oneof`_ ``content``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            The timestamp at which the blurb was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            The latest timestamp at which the blurb was
            updated.
        legacy_room_id (str):
            The legacy id of the room. This field is used to signal the
            use of the compound resource pattern
            ``rooms/{room}/blurbs/legacy/{legacy_room}.{blurb}``

            This field is a member of `oneof`_ ``legacy_id``.
        legacy_user_id (str):
            The legacy id of the user. This field is used to signal the
            use of the compound resource pattern
            ``users/{user}/profile/blurbs/legacy/{legacy_user}~{blurb}``

            This field is a member of `oneof`_ ``legacy_id``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    user: str = proto.Field(
        proto.STRING,
        number=2,
    )
    text: str = proto.Field(
        proto.STRING,
        number=3,
        oneof='content',
    )
    image: bytes = proto.Field(
        proto.BYTES,
        number=4,
        oneof='content',
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    legacy_room_id: str = proto.Field(
        proto.STRING,
        number=7,
        oneof='legacy_id',
    )
    legacy_user_id: str = proto.Field(
        proto.STRING,
        number=8,
        oneof='legacy_id',
    )


class CreateBlurbRequest(proto.Message):
    r"""The request message for the
    google.showcase.v1beta1.Messaging\CreateBlurb method.

    Attributes:
        parent (str):
            The resource name of the chat room or user
            profile that this blurb will be tied to.
        blurb (google.showcase_v1beta1.types.Blurb):
            The blurb to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    blurb: 'Blurb' = proto.Field(
        proto.MESSAGE,
        number=2,
        message='Blurb',
    )


class GetBlurbRequest(proto.Message):
    r"""The request message for the
    google.showcase.v1beta1.Messaging\GetBlurb method.

    Attributes:
        name (str):
            The resource name of the requested blurb.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateBlurbRequest(proto.Message):
    r"""The request message for the
    google.showcase.v1beta1.Messaging\UpdateBlurb method.

    Attributes:
        blurb (google.showcase_v1beta1.types.Blurb):
            The blurb to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The field mask to determine which fields are
            to be updated. If empty, the server will assume
            all fields are to be updated.
    """

    blurb: 'Blurb' = proto.Field(
        proto.MESSAGE,
        number=1,
        message='Blurb',
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteBlurbRequest(proto.Message):
    r"""The request message for the
    google.showcase.v1beta1.Messaging\DeleteBlurb method.

    Attributes:
        name (str):
            The resource name of the requested blurb.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListBlurbsRequest(proto.Message):
    r"""The request message for the
    google.showcase.v1beta1.Messaging\ListBlurbs method.

    Attributes:
        parent (str):
            The resource name of the requested room or
            profile who blurbs to list.
        page_size (int):
            The maximum number of blurbs to return.
            Server may return fewer blurbs than requested.
            If unspecified, server will pick an appropriate
            default.
        page_token (str):
            The value of
            google.showcase.v1beta1.ListBlurbsResponse.next_page_token
            returned from the previous call to
            ``google.showcase.v1beta1.Messaging\ListBlurbs`` method.
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


class ListBlurbsResponse(proto.Message):
    r"""The response message for the
    google.showcase.v1beta1.Messaging\ListBlurbs method.

    Attributes:
        blurbs (MutableSequence[google.showcase_v1beta1.types.Blurb]):
            The list of blurbs.
        next_page_token (str):
            A token to retrieve next page of results. Pass this value in
            ListBlurbsRequest.page_token field in the subsequent call to
            ``google.showcase.v1beta1.Blurb\ListBlurbs`` method to
            retrieve the next page of results.
    """

    @property
    def raw_page(self):
        return self

    blurbs: MutableSequence['Blurb'] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message='Blurb',
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class SearchBlurbsRequest(proto.Message):
    r"""The request message for the
    google.showcase.v1beta1.Messaging\SearchBlurbs method.

    Attributes:
        query (str):
            The query used to search for blurbs
            containing to words of this string. Only posts
            that contain an exact match of a queried word
            will be returned.
        parent (str):
            The rooms or profiles to search. If unset, ``SearchBlurbs``
            will search all rooms and all profiles.
        page_size (int):
            The maximum number of blurbs return. Server
            may return fewer blurbs than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            The value of
            google.showcase.v1beta1.SearchBlurbsResponse.next_page_token
            returned from the previous call to
            ``google.showcase.v1beta1.Messaging\SearchBlurbs`` method.
    """

    query: str = proto.Field(
        proto.STRING,
        number=1,
    )
    parent: str = proto.Field(
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


class SearchBlurbsMetadata(proto.Message):
    r"""The operation metadata message for the
    google.showcase.v1beta1.Messaging\SearchBlurbs method.

    Attributes:
        retry_info (google.rpc.error_details_pb2.RetryInfo):
            This signals to the client when to next poll
            for response.
    """

    retry_info: error_details_pb2.RetryInfo = proto.Field(
        proto.MESSAGE,
        number=1,
        message=error_details_pb2.RetryInfo,
    )


class SearchBlurbsResponse(proto.Message):
    r"""The operation response message for the
    google.showcase.v1beta1.Messaging\SearchBlurbs method.

    Attributes:
        blurbs (MutableSequence[google.showcase_v1beta1.types.Blurb]):
            Blurbs that matched the search query.
        next_page_token (str):
            A token to retrieve next page of results. Pass this value in
            SearchBlurbsRequest.page_token field in the subsequent call
            to ``google.showcase.v1beta1.Blurb\SearchBlurbs`` method to
            retrieve the next page of results.
    """

    @property
    def raw_page(self):
        return self

    blurbs: MutableSequence['Blurb'] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message='Blurb',
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class StreamBlurbsRequest(proto.Message):
    r"""The request message for the
    google.showcase.v1beta1.Messaging\StreamBlurbs method.

    Attributes:
        name (str):
            The resource name of a chat room or user
            profile whose blurbs to stream.
        expire_time (google.protobuf.timestamp_pb2.Timestamp):
            The time at which this stream will close.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    expire_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )


class StreamBlurbsResponse(proto.Message):
    r"""The response message for the
    google.showcase.v1beta1.Messaging\StreamBlurbs method.

    Attributes:
        blurb (google.showcase_v1beta1.types.Blurb):
            The blurb that was either created, updated,
            or deleted.
        action (google.showcase_v1beta1.types.StreamBlurbsResponse.Action):
            The action that triggered the blurb to be
            returned.
    """
    class Action(proto.Enum):
        r"""The action that triggered the blurb to be returned.

        Values:
            ACTION_UNSPECIFIED (0):
                No description available.
            CREATE (1):
                Specifies that the blurb was created.
            UPDATE (2):
                Specifies that the blurb was updated.
            DELETE (3):
                Specifies that the blurb was deleted.
        """
        ACTION_UNSPECIFIED = 0
        CREATE = 1
        UPDATE = 2
        DELETE = 3

    blurb: 'Blurb' = proto.Field(
        proto.MESSAGE,
        number=1,
        message='Blurb',
    )
    action: Action = proto.Field(
        proto.ENUM,
        number=2,
        enum=Action,
    )


class SendBlurbsResponse(proto.Message):
    r"""The response message for the
    google.showcase.v1beta1.Messaging\SendBlurbs method.

    Attributes:
        names (MutableSequence[str]):
            The names of successful blurb creations.
    """

    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class ConnectRequest(proto.Message):
    r"""The request message for the
    google.showcase.v1beta1.Messaging\Connect method.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        config (google.showcase_v1beta1.types.ConnectRequest.ConnectConfig):
            Provides information that specifies how to process
            subsequent requests. The first ``ConnectRequest`` message
            must contain a ``config`` message.

            This field is a member of `oneof`_ ``request``.
        blurb (google.showcase_v1beta1.types.Blurb):
            The blurb to be created.

            This field is a member of `oneof`_ ``request``.
    """

    class ConnectConfig(proto.Message):
        r"""

        Attributes:
            parent (str):
                The room or profile to follow and create
                messages for.
        """

        parent: str = proto.Field(
            proto.STRING,
            number=1,
        )

    config: ConnectConfig = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof='request',
        message=ConnectConfig,
    )
    blurb: 'Blurb' = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof='request',
        message='Blurb',
    )


__all__ = tuple(sorted(__protobuf__.manifest))
