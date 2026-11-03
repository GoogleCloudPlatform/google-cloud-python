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

import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.securitycenter.v2",
    manifest={
        "NotificationConfig",
    },
)


class NotificationConfig(proto.Message):
    r"""Cloud Security Command Center (Cloud SCC) notification
    configs.
    A notification config is a Cloud SCC resource that contains the
    configuration to send notifications for create/update events of
    findings, assets and etc.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The relative resource name of this notification
            config. See:
            https://cloud.google.com/apis/design/resource_names#relative_resource_name
            The following list shows some examples: +
            ``organizations/{organization_id}/locations/{location_id}/notificationConfigs/notify_public_bucket``
            +
            ``folders/{folder_id}/locations/{location_id}/notificationConfigs/notify_public_bucket``
            +
            ``projects/{project_id}/locations/{location_id}/notificationConfigs/notify_public_bucket``
        description (str):
            The description of the notification config
            (max of 1024 characters).
        pubsub_topic (str):
            The Pub/Sub topic to send notifications to. Its format is
            "projects/[project_id]/topics/[topic]".
        service_account (str):
            Output only. The service account that needs
            "pubsub.topics.publish" permission to publish to
            the Pub/Sub topic.
        streaming_config (google.cloud.securitycenter_v2.types.NotificationConfig.StreamingConfig):
            The config for triggering streaming-based
            notifications.

            This field is a member of `oneof`_ ``notify_config``.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp of when the
            notification config was last updated.
        deletion_notifications_enabled (bool):
            Optional. Indicates whether the notifications
            will be sent for deleted findings. When enabled,
            the filter defined in the streaming config is
            still respected when sending deletion
            notifications.
    """

    class StreamingConfig(proto.Message):
        r"""The config for streaming-based notifications, which send each
        event as soon as it is detected.

        Attributes:
            filter (str):
                Expression that defines the filter to apply across
                create/update events of assets or findings as specified by
                the event type. The expression is a list of zero or more
                restrictions combined via logical operators ``AND`` and
                ``OR``. Parentheses are supported, and ``OR`` has higher
                precedence than ``AND``.

                Restrictions have the form ``<field> <operator> <value>``
                and may have a ``-`` character in front of them to indicate
                negation. The fields map to those defined in the
                corresponding resource.

                The supported operators are:

                - ``=`` for all value types.
                - ``>``, ``<``, ``>=``, ``<=`` for integer values.
                - ``:``, meaning substring matching, for strings.

                The supported value types are:

                - string literals in quotes.
                - integer literals without quotes.
                - boolean literals ``true`` and ``false`` without quotes.
        """

        filter: str = proto.Field(
            proto.STRING,
            number=1,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    pubsub_topic: str = proto.Field(
        proto.STRING,
        number=3,
    )
    service_account: str = proto.Field(
        proto.STRING,
        number=4,
    )
    streaming_config: StreamingConfig = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="notify_config",
        message=StreamingConfig,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    deletion_notifications_enabled: bool = proto.Field(
        proto.BOOL,
        number=9,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
