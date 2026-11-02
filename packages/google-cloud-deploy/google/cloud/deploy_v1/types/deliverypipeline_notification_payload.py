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

from google.cloud.deploy_v1.types import log_enums

__protobuf__ = proto.module(
    package="google.cloud.deploy.v1",
    manifest={
        "DeliveryPipelineNotificationEvent",
    },
)


class DeliveryPipelineNotificationEvent(proto.Message):
    r"""Payload proto for
    "clouddeploy.googleapis.com/deliverypipeline_notification" Platform
    Log event that describes the failure to send delivery pipeline
    status change Pub/Sub notification.

    Attributes:
        message (str):
            Debug message for when a notification fails
            to send.
        pipeline_uid (str):
            Unique identifier of the ``DeliveryPipeline``.
        delivery_pipeline (str):
            The name of the ``Delivery Pipeline``.
        type_ (google.cloud.deploy_v1.types.Type):
            Type of this notification, e.g. for a Pub/Sub
            failure.
    """

    message: str = proto.Field(
        proto.STRING,
        number=1,
    )
    pipeline_uid: str = proto.Field(
        proto.STRING,
        number=4,
    )
    delivery_pipeline: str = proto.Field(
        proto.STRING,
        number=2,
    )
    type_: log_enums.Type = proto.Field(
        proto.ENUM,
        number=3,
        enum=log_enums.Type,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
