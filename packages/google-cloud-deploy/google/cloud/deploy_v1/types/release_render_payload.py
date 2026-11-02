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

from google.cloud.deploy_v1.types import cloud_deploy, log_enums

__protobuf__ = proto.module(
    package="google.cloud.deploy.v1",
    manifest={
        "ReleaseRenderEvent",
    },
)


class ReleaseRenderEvent(proto.Message):
    r"""Payload proto for "clouddeploy.googleapis.com/release_render"
    Platform Log event that describes the render status change.

    Attributes:
        message (str):
            Debug message for when a render transition
            occurs. Provides further details as rendering
            progresses through render states.
        pipeline_uid (str):
            Unique identifier of the ``DeliveryPipeline``.
        release (str):
            The name of the release. release_uid is not in this log
            message because we write some of these log messages at
            release creation time, before we've generated the uid.
        type_ (google.cloud.deploy_v1.types.Type):
            Type of this notification, e.g. for a release
            render state change event.
        release_render_state (google.cloud.deploy_v1.types.Release.RenderState):
            The state of the release render.
    """

    message: str = proto.Field(
        proto.STRING,
        number=1,
    )
    pipeline_uid: str = proto.Field(
        proto.STRING,
        number=4,
    )
    release: str = proto.Field(
        proto.STRING,
        number=2,
    )
    type_: log_enums.Type = proto.Field(
        proto.ENUM,
        number=5,
        enum=log_enums.Type,
    )
    release_render_state: cloud_deploy.Release.RenderState = proto.Field(
        proto.ENUM,
        number=3,
        enum=cloud_deploy.Release.RenderState,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
