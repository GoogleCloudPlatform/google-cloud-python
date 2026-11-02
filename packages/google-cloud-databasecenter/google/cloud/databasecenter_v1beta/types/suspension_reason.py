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
    package="google.cloud.databasecenter.v1beta",
    manifest={
        "SuspensionReason",
    },
)


class SuspensionReason(proto.Enum):
    r"""The reason for suspension of the database resource.

    Values:
        SUSPENSION_REASON_UNSPECIFIED (0):
            Suspension reason is unspecified.
        WIPEOUT_HIDE_EVENT (1):
            Wipeout hide event.
        WIPEOUT_PURGE_EVENT (2):
            Wipeout purge event.
        BILLING_DISABLED (3):
            Billing disabled for project
        ABUSER_DETECTED (4):
            Abuse detected for resource
        ENCRYPTION_KEY_INACCESSIBLE (5):
            Encryption key inaccessible.
        REPLICATED_CLUSTER_ENCRYPTION_KEY_INACCESSIBLE (6):
            Replicated cluster encryption key
            inaccessible.
    """

    SUSPENSION_REASON_UNSPECIFIED = 0
    WIPEOUT_HIDE_EVENT = 1
    WIPEOUT_PURGE_EVENT = 2
    BILLING_DISABLED = 3
    ABUSER_DETECTED = 4
    ENCRYPTION_KEY_INACCESSIBLE = 5
    REPLICATED_CLUSTER_ENCRYPTION_KEY_INACCESSIBLE = 6


__all__ = tuple(sorted(__protobuf__.manifest))
