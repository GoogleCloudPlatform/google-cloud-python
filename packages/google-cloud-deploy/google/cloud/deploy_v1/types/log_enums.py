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
    package="google.cloud.deploy.v1",
    manifest={
        "Type",
    },
)


class Type(proto.Enum):
    r"""Type indicates the type of the log entry and can be used as a
    filter.

    Values:
        TYPE_UNSPECIFIED (0):
            Type is unspecified.
        TYPE_PUBSUB_NOTIFICATION_FAILURE (1):
            A Pub/Sub notification failed to be sent.
        TYPE_RESOURCE_STATE_CHANGE (3):
            Resource state changed.
        TYPE_PROCESS_ABORTED (4):
            A process aborted.
        TYPE_RESTRICTION_VIOLATED (5):
            Restriction check failed.
        TYPE_RESOURCE_DELETED (6):
            Resource deleted.
        TYPE_ROLLOUT_UPDATE (7):
            Rollout updated.
        TYPE_DEPLOY_POLICY_EVALUATION (8):
            Deploy Policy evaluation.
        TYPE_RENDER_STATUES_CHANGE (2):
            Deprecated: This field is never used. Use release_render log
            type instead.
    """

    TYPE_UNSPECIFIED = 0
    TYPE_PUBSUB_NOTIFICATION_FAILURE = 1
    TYPE_RESOURCE_STATE_CHANGE = 3
    TYPE_PROCESS_ABORTED = 4
    TYPE_RESTRICTION_VIOLATED = 5
    TYPE_RESOURCE_DELETED = 6
    TYPE_ROLLOUT_UPDATE = 7
    TYPE_DEPLOY_POLICY_EVALUATION = 8
    TYPE_RENDER_STATUES_CHANGE = 2


__all__ = tuple(sorted(__protobuf__.manifest))
