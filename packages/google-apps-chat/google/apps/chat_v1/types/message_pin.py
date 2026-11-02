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

__protobuf__ = proto.module(
    package="google.chat.v1",
    manifest={
        "MessagePin",
        "ListMessagePinsRequest",
        "ListMessagePinsResponse",
        "CreateMessagePinRequest",
        "DeleteMessagePinRequest",
    },
)


class MessagePin(proto.Message):
    r"""A pin on a Chat message. For more information see `Pin a
    message <https://support.google.com/chat?p=chat-board-hc>`__.

    Attributes:
        name (str):
            Identifier. The resource name of the message pin. Format:
            ``spaces/{space}/messagePins/{message_pin}`` The resource ID
            component matches the resource ID component of the message.
            For example, a message with ``spaces/AAA/messages/bbb.ccc``
            corresponds to the message pin with the resource name
            ``spaces/AAA/messagePins/bbb.ccc``.
        message (str):
            Required. Immutable. The resource name of the message that
            is pinned. Format: ``spaces/{space}/messages/{message}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    message: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListMessagePinsRequest(proto.Message):
    r"""Request message for listing message pins.

    Attributes:
        parent (str):
            Required. The parent space which owns the collection of
            pinned items Format: ``spaces/{space}``
        page_size (int):
            Optional. The maximum number of message pins returned. The
            service might return fewer messages than this value. The
            maximum value is 100. If you use a value more than 100, it's
            automatically changed to 100. If unspecified, at most 100
            message pins will be returned. Negative values return an
            ``INVALID_ARGUMENT`` error.
        page_token (str):
            Optional. A page token received from a
            previous list message pins call. Provide this
            parameter to retrieve the subsequent page.

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


class ListMessagePinsResponse(proto.Message):
    r"""Response message for listing message pins.

    Attributes:
        message_pins (MutableSequence[google.apps.chat_v1.types.MessagePin]):
            The pinned messages from the specified space.
        next_page_token (str):
            You can send a token as ``pageToken`` to retrieve the next
            page of results. If empty, there are no subsequent pages.
    """

    @property
    def raw_page(self):
        return self

    message_pins: MutableSequence["MessagePin"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="MessagePin",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateMessagePinRequest(proto.Message):
    r"""Request message for creating a message pin.

    Attributes:
        parent (str):
            Required. The parent space in which to create
            the message pin. Format: spaces/{space}
        message_pin (google.apps.chat_v1.types.MessagePin):
            Required. The MessagePin to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    message_pin: "MessagePin" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="MessagePin",
    )


class DeleteMessagePinRequest(proto.Message):
    r"""Request message for deleting a message pin.

    Attributes:
        name (str):
            Required. The resource name of the message pin to remove.
            Format: spaces/{space}/messagePins/{message_pin}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
