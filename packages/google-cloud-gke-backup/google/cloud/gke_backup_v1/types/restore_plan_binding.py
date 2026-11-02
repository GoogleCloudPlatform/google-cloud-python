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
    package="google.cloud.gkebackup.v1",
    manifest={
        "RestorePlanBinding",
    },
)


class RestorePlanBinding(proto.Message):
    r"""A RestorePlanBinding binds a RestorePlan with a
    RestoreChannel. This resource is created automatically when a
    RestorePlan is created using a RestoreChannel. This also serves
    as a holder for cross-project fields that need to be displayed
    in the current project.

    Attributes:
        name (str):
            Identifier. The fully qualified name of the
            RestorePlanBinding.
            ``projects/*/locations/*/restoreChannels/*/restorePlanBindings/*``
        uid (str):
            Output only. Server generated global unique identifier of
            `UUID4 <https://en.wikipedia.org/wiki/Universally_unique_identifier>`__
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when this binding
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when this binding
            was created.
        restore_plan (str):
            Output only. The fully qualified name of the RestorePlan
            bound to this RestoreChannel.
            ``projects/*/locations/*/restorePlans/{restore_plan}``
        etag (str):
            Output only. ``etag`` is used for optimistic concurrency
            control as a way to help prevent simultaneous updates of a
            RestorePlanBinding from overwriting each other. It is
            strongly suggested that systems make use of the 'etag' in
            the read-modify-write cycle to perform RestorePlanBinding
            updates in order to avoid race conditions: An ``etag`` is
            returned in the response to ``GetRestorePlanBinding``, and
            systems are expected to put that etag in the request to
            ``UpdateRestorePlanBinding`` or ``DeleteRestorePlanBinding``
            to ensure that their change will be applied to the same
            version of the resource.
        backup_plan (str):
            Output only. The fully qualified name of the BackupPlan
            bound to the specified RestorePlan.
            ``projects/*/locations/*/backukpPlans/{backup_plan}``
    """

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
    restore_plan: str = proto.Field(
        proto.STRING,
        number=5,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=6,
    )
    backup_plan: str = proto.Field(
        proto.STRING,
        number=7,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
