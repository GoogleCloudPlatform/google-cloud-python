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

from google.cloud.gke_backup_v1.types import restore

__protobuf__ = proto.module(
    package="google.cloud.gkebackup.v1",
    manifest={
        "RestorePlan",
    },
)


class RestorePlan(proto.Message):
    r"""The configuration of a potential series of Restore operations
    to be performed against Backups belong to a particular
    BackupPlan.

    Attributes:
        name (str):
            Output only. The full name of the RestorePlan resource.
            Format: ``projects/*/locations/*/restorePlans/*``.
        uid (str):
            Output only. Server generated global unique identifier of
            `UUID <https://en.wikipedia.org/wiki/Universally_unique_identifier>`__
            format.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when this
            RestorePlan resource was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when this
            RestorePlan resource was last updated.
        description (str):
            Optional. User specified descriptive string
            for this RestorePlan.
        backup_plan (str):
            Required. Immutable. A reference to the
            [BackupPlan][google.cloud.gkebackup.v1.BackupPlan] from
            which Backups may be used as the source for Restores created
            via this RestorePlan. Format:
            ``projects/*/locations/*/backupPlans/*``.
        cluster (str):
            Required. Immutable. The target cluster into which Restores
            created via this RestorePlan will restore data. NOTE: the
            cluster's region must be the same as the RestorePlan. Valid
            formats:

            - ``projects/*/locations/*/clusters/*``
            - ``projects/*/zones/*/clusters/*``
        restore_config (google.cloud.gke_backup_v1.types.RestoreConfig):
            Required. Configuration of Restores created
            via this RestorePlan.
        labels (MutableMapping[str, str]):
            Optional. A set of custom labels supplied by
            user.
        etag (str):
            Output only. ``etag`` is used for optimistic concurrency
            control as a way to help prevent simultaneous updates of a
            restore from overwriting each other. It is strongly
            suggested that systems make use of the ``etag`` in the
            read-modify-write cycle to perform restore updates in order
            to avoid race conditions: An ``etag`` is returned in the
            response to ``GetRestorePlan``, and systems are expected to
            put that etag in the request to ``UpdateRestorePlan`` or
            ``DeleteRestorePlan`` to ensure that their change will be
            applied to the same version of the resource.
        state (google.cloud.gke_backup_v1.types.RestorePlan.State):
            Output only. State of the RestorePlan. This
            State field reflects the various stages a
            RestorePlan can be in during the Create
            operation.
        state_reason (str):
            Output only. Human-readable description of why RestorePlan
            is in the current ``state``. This field is only meant for
            human readability and should not be used programmatically as
            this field is not guaranteed to be consistent.
        restore_channel (str):
            Output only. The fully qualified name of the RestoreChannel
            to be used to create a RestorePlan. This field is set only
            if the ``backup_plan`` is in a different project than the
            RestorePlan. Format:
            ``projects/*/locations/*/restoreChannels/*``
    """

    class State(proto.Enum):
        r"""State

        Values:
            STATE_UNSPECIFIED (0):
                Default first value for Enums.
            CLUSTER_PENDING (1):
                Waiting for cluster state to be RUNNING.
            READY (2):
                The RestorePlan has successfully been created
                and is ready for Restores.
            FAILED (3):
                RestorePlan creation has failed.
            DELETING (4):
                The RestorePlan is in the process of being
                deleted.
        """

        STATE_UNSPECIFIED = 0
        CLUSTER_PENDING = 1
        READY = 2
        FAILED = 3
        DELETING = 4

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    description: str = proto.Field(
        proto.STRING,
        number=5,
    )
    backup_plan: str = proto.Field(
        proto.STRING,
        number=6,
    )
    cluster: str = proto.Field(
        proto.STRING,
        number=7,
    )
    restore_config: restore.RestoreConfig = proto.Field(
        proto.MESSAGE,
        number=8,
        message=restore.RestoreConfig,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=9,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=10,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=11,
        enum=State,
    )
    state_reason: str = proto.Field(
        proto.STRING,
        number=12,
    )
    restore_channel: str = proto.Field(
        proto.STRING,
        number=13,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
