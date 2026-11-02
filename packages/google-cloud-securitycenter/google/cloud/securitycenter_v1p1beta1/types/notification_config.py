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
    package="google.cloud.securitycenter.v1p1beta1",
    manifest={
        "NotificationConfig",
    },
)


class NotificationConfig(proto.Message):
    r"""Security Command Center notification configs.

    A notification config is a Security Command Center resource that
    contains the configuration to send notifications for
    create/update events of findings, assets and etc.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            The relative resource name of this notification config. See:
            https://cloud.google.com/apis/design/resource_names#relative_resource_name
            Example:
            "organizations/{organization_id}/notificationConfigs/notify_public_bucket".
        description (str):
            The description of the notification config
            (max of 1024 characters).
        event_type (google.cloud.securitycenter_v1p1beta1.types.NotificationConfig.EventType):
            The type of events the config is for, e.g.
            FINDING.
        pubsub_topic (str):
            The Pub/Sub topic to send notifications to. Its format is
            "projects/[project_id]/topics/[topic]".
        service_account (str):
            Output only. The service account that needs
            "pubsub.topics.publish" permission to publish to
            the Pub/Sub topic.
        streaming_config (google.cloud.securitycenter_v1p1beta1.types.NotificationConfig.StreamingConfig):
            The config for triggering streaming-based
            notifications.

            This field is a member of `oneof`_ ``notify_config``.
    """

    class EventType(proto.Enum):
        r"""The type of events.

        Values:
            EVENT_TYPE_UNSPECIFIED (0):
                Unspecified event type.
            FINDING (1):
                Events for findings.
        """

        EVENT_TYPE_UNSPECIFIED = 0
        FINDING = 1

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
    event_type: EventType = proto.Field(
        proto.ENUM,
        number=3,
        enum=EventType,
    )
    pubsub_topic: str = proto.Field(
        proto.STRING,
        number=4,
    )
    service_account: str = proto.Field(
        proto.STRING,
        number=5,
    )
    streaming_config: StreamingConfig = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="notify_config",
        message=StreamingConfig,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
