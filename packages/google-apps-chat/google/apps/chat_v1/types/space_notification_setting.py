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
        "SpaceNotificationSetting",
        "GetSpaceNotificationSettingRequest",
        "UpdateSpaceNotificationSettingRequest",
    },
)


class SpaceNotificationSetting(proto.Message):
    r"""The notification setting of a user in a space.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the space notification
            setting. Format:
            ``users/{user}/spaces/{space}/spaceNotificationSetting``.
        notification_setting (google.apps.chat_v1.types.SpaceNotificationSetting.NotificationSetting):
            The notification setting.

            This field is a member of `oneof`_ ``_notification_setting``.
        mute_setting (google.apps.chat_v1.types.SpaceNotificationSetting.MuteSetting):
            The space notification mute setting.

            This field is a member of `oneof`_ ``_mute_setting``.
    """

    class NotificationSetting(proto.Enum):
        r"""The notification setting types. Other types might be
        supported in the future.

        Values:
            NOTIFICATION_SETTING_UNSPECIFIED (0):
                Reserved.
            ALL (1):
                Notifications are triggered by @mentions,
                followed threads, first message of new threads.
                All new threads are automatically followed,
                unless manually unfollowed by the user.
            MAIN_CONVERSATIONS (2):
                The notification is triggered by @mentions,
                followed threads, first message of new threads.
                Not available for 1:1 direct messages.
            FOR_YOU (3):
                The notification is triggered by @mentions,
                followed threads. Not available for 1:1 direct
                messages.
            OFF (4):
                Notification is off.
        """

        NOTIFICATION_SETTING_UNSPECIFIED = 0
        ALL = 1
        MAIN_CONVERSATIONS = 2
        FOR_YOU = 3
        OFF = 4

    class MuteSetting(proto.Enum):
        r"""The space notification mute setting types.

        Values:
            MUTE_SETTING_UNSPECIFIED (0):
                Reserved.
            UNMUTED (1):
                The user will receive notifications for the
                space based on the notification setting.
            MUTED (2):
                The user will not receive any notifications
                for the space, regardless of the notification
                setting.
        """

        MUTE_SETTING_UNSPECIFIED = 0
        UNMUTED = 1
        MUTED = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    notification_setting: NotificationSetting = proto.Field(
        proto.ENUM,
        number=2,
        optional=True,
        enum=NotificationSetting,
    )
    mute_setting: MuteSetting = proto.Field(
        proto.ENUM,
        number=3,
        optional=True,
        enum=MuteSetting,
    )


class GetSpaceNotificationSettingRequest(proto.Message):
    r"""Request message to get space notification setting.
    Only supports getting notification setting for the calling user.

    Attributes:
        name (str):
            Required. Format:
            users/{user}/spaces/{space}/spaceNotificationSetting

            - ``users/me/spaces/{space}/spaceNotificationSetting``, OR
            - ``users/user@example.com/spaces/{space}/spaceNotificationSetting``,
              OR
            - ``users/123456789/spaces/{space}/spaceNotificationSetting``.
              Note: Only the caller's user id or email is allowed in the
              path.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateSpaceNotificationSettingRequest(proto.Message):
    r"""Request to update the space notification settings.
    Only supports updating notification setting for the calling
    user.

    Attributes:
        space_notification_setting (google.apps.chat_v1.types.SpaceNotificationSetting):
            Required. The resource name for the space notification
            settings must be populated in the form of
            ``users/{user}/spaces/{space}/spaceNotificationSetting``.
            Only fields specified by ``update_mask`` are updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Supported field paths:

            - ``notification_setting``

            - ``mute_setting``
    """

    space_notification_setting: "SpaceNotificationSetting" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="SpaceNotificationSetting",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
