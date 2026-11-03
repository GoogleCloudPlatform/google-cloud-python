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

import google.protobuf.any_pb2 as any_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.beyondcorp.appconnectors.v1",
    manifest={
        "AppConnectorInstanceConfig",
        "NotificationConfig",
        "ImageConfig",
    },
)


class AppConnectorInstanceConfig(proto.Message):
    r"""AppConnectorInstanceConfig defines the instance config of a
    AppConnector.

    Attributes:
        sequence_number (int):
            Required. A monotonically increasing number
            generated and maintained by the API provider.
            Every time a config changes in the backend, the
            sequenceNumber should be bumped up to reflect
            the change.
        instance_config (google.protobuf.any_pb2.Any):
            The SLM instance agent configuration.
        notification_config (google.cloud.beyondcorp_appconnectors_v1.types.NotificationConfig):
            NotificationConfig defines the notification
            mechanism that the remote instance should
            subscribe to in order to receive notification.
        image_config (google.cloud.beyondcorp_appconnectors_v1.types.ImageConfig):
            ImageConfig defines the GCR images to run for
            the remote agent's control plane.
    """

    sequence_number: int = proto.Field(
        proto.INT64,
        number=1,
    )
    instance_config: any_pb2.Any = proto.Field(
        proto.MESSAGE,
        number=2,
        message=any_pb2.Any,
    )
    notification_config: "NotificationConfig" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="NotificationConfig",
    )
    image_config: "ImageConfig" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="ImageConfig",
    )


class NotificationConfig(proto.Message):
    r"""NotificationConfig defines the mechanisms to notify instance
    agent.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        pubsub_notification (google.cloud.beyondcorp_appconnectors_v1.types.NotificationConfig.CloudPubSubNotificationConfig):
            Cloud Pub/Sub Configuration to receive
            notifications.

            This field is a member of `oneof`_ ``config``.
    """

    class CloudPubSubNotificationConfig(proto.Message):
        r"""The configuration for Pub/Sub messaging for the AppConnector.

        Attributes:
            pubsub_subscription (str):
                The Pub/Sub subscription the AppConnector
                uses to receive notifications.
        """

        pubsub_subscription: str = proto.Field(
            proto.STRING,
            number=1,
        )

    pubsub_notification: CloudPubSubNotificationConfig = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="config",
        message=CloudPubSubNotificationConfig,
    )


class ImageConfig(proto.Message):
    r"""ImageConfig defines the control plane images to run.

    Attributes:
        target_image (str):
            The initial image the remote agent will
            attempt to run for the control plane. Format
            would be a gcr image path, e.g.:

            gcr.io/PROJECT-ID/my-image:tag1
        stable_image (str):
            The stable image that the remote agent will
            fallback to if the target image fails. Format
            would be a gcr image path, e.g.:

            gcr.io/PROJECT-ID/my-image:tag1
    """

    target_image: str = proto.Field(
        proto.STRING,
        number=1,
    )
    stable_image: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
