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
        "RolloutUpdateEvent",
    },
)


class RolloutUpdateEvent(proto.Message):
    r"""Payload proto for "clouddeploy.googleapis.com/rollout_update"
    Platform Log event that describes the rollout update event.

    Attributes:
        message (str):
            Debug message for when a rollout update event
            occurs.
        pipeline_uid (str):
            Unique identifier of the pipeline.
        release_uid (str):
            Unique identifier of the release.
        release (str):
            The name of the ``Release``.
        rollout (str):
            The name of the rollout. rollout_uid is not in this log
            message because we write some of these log messages at
            rollout creation time, before we've generated the uid.
        target_id (str):
            ID of the target.
        type_ (google.cloud.deploy_v1.types.Type):
            Type of this notification, e.g. for a rollout
            update event.
        rollout_update_type (google.cloud.deploy_v1.types.RolloutUpdateEvent.RolloutUpdateType):
            The type of the rollout update.
    """

    class RolloutUpdateType(proto.Enum):
        r"""RolloutUpdateType indicates the type of the rollout update.

        Values:
            ROLLOUT_UPDATE_TYPE_UNSPECIFIED (0):
                Rollout update type unspecified.
            PENDING (1):
                rollout state updated to pending.
            PENDING_RELEASE (2):
                Rollout state updated to pending release.
            IN_PROGRESS (3):
                Rollout state updated to in progress.
            CANCELLING (4):
                Rollout state updated to cancelling.
            CANCELLED (5):
                Rollout state updated to cancelled.
            HALTED (6):
                Rollout state updated to halted.
            SUCCEEDED (7):
                Rollout state updated to succeeded.
            FAILED (8):
                Rollout state updated to failed.
            APPROVAL_REQUIRED (9):
                Rollout requires approval.
            APPROVED (10):
                Rollout has been approved.
            REJECTED (11):
                Rollout has been rejected.
            ADVANCE_REQUIRED (12):
                Rollout requires advance to the next phase.
            ADVANCED (13):
                Rollout has been advanced.
        """

        ROLLOUT_UPDATE_TYPE_UNSPECIFIED = 0
        PENDING = 1
        PENDING_RELEASE = 2
        IN_PROGRESS = 3
        CANCELLING = 4
        CANCELLED = 5
        HALTED = 6
        SUCCEEDED = 7
        FAILED = 8
        APPROVAL_REQUIRED = 9
        APPROVED = 10
        REJECTED = 11
        ADVANCE_REQUIRED = 12
        ADVANCED = 13

    message: str = proto.Field(
        proto.STRING,
        number=6,
    )
    pipeline_uid: str = proto.Field(
        proto.STRING,
        number=1,
    )
    release_uid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    release: str = proto.Field(
        proto.STRING,
        number=8,
    )
    rollout: str = proto.Field(
        proto.STRING,
        number=3,
    )
    target_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    type_: log_enums.Type = proto.Field(
        proto.ENUM,
        number=7,
        enum=log_enums.Type,
    )
    rollout_update_type: RolloutUpdateType = proto.Field(
        proto.ENUM,
        number=5,
        enum=RolloutUpdateType,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
