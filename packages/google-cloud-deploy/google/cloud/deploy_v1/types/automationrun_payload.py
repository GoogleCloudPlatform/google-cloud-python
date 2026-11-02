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
        "AutomationRunEvent",
    },
)


class AutomationRunEvent(proto.Message):
    r"""Payload proto for "clouddeploy.googleapis.com/automation_run"
    Platform Log event that describes the AutomationRun related events.

    Attributes:
        message (str):
            Debug message for when there is an update on
            the AutomationRun. Provides further details
            about the resource creation or state change.
        automation_run (str):
            The name of the ``AutomationRun``.
        pipeline_uid (str):
            Unique identifier of the ``DeliveryPipeline``.
        automation_id (str):
            Identifier of the ``Automation``.
        rule_id (str):
            Identifier of the ``Automation`` rule.
        destination_target_id (str):
            ID of the ``Target`` to which the ``AutomationRun`` is
            created.
        type_ (google.cloud.deploy_v1.types.Type):
            Type of this notification, e.g. for a Pub/Sub
            failure.
    """

    message: str = proto.Field(
        proto.STRING,
        number=1,
    )
    automation_run: str = proto.Field(
        proto.STRING,
        number=2,
    )
    pipeline_uid: str = proto.Field(
        proto.STRING,
        number=3,
    )
    automation_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    rule_id: str = proto.Field(
        proto.STRING,
        number=5,
    )
    destination_target_id: str = proto.Field(
        proto.STRING,
        number=6,
    )
    type_: log_enums.Type = proto.Field(
        proto.ENUM,
        number=7,
        enum=log_enums.Type,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
