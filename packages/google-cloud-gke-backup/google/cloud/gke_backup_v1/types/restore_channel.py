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
        "RestoreChannel",
    },
)


class RestoreChannel(proto.Message):
    r"""A RestoreChannel imposes constraints on where backups can be
    restored. The RestoreChannel should be in the same project and
    region as the backups. The backups can only be restored in the
    ``destination_project``.

    Attributes:
        name (str):
            Identifier. The fully qualified name of the RestoreChannel.
            ``projects/*/locations/*/restoreChannels/*``
        destination_project (str):
            Required. Immutable. The project into which the backups will
            be restored. The format is ``projects/{projectId}`` or
            ``projects/{projectNumber}``.
        uid (str):
            Output only. Server generated global unique identifier of
            `UUID <https://en.wikipedia.org/wiki/Universally_unique_identifier>`__
            format.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when this
            RestoreChannel was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when this
            RestoreChannel was last updated.
        labels (MutableMapping[str, str]):
            Optional. A set of custom labels supplied by
            user.
        description (str):
            Optional. User specified descriptive string
            for this RestoreChannel.
        etag (str):
            Output only. ``etag`` is used for optimistic concurrency
            control as a way to help prevent simultaneous updates of a
            RestoreChannel from overwriting each other. It is strongly
            suggested that systems make use of the 'etag' in the
            read-modify-write cycle to perform RestoreChannel updates in
            order to avoid race conditions: An ``etag`` is returned in
            the response to ``GetRestoreChannel``, and systems are
            expected to put that etag in the request to
            ``UpdateRestoreChannel`` or ``DeleteRestoreChannel`` to
            ensure that their change will be applied to the same version
            of the resource.
        destination_project_id (str):
            Output only. The project_id where backups will be restored.
            Example Project ID: "my-project-id". This will be an
            OUTPUT_ONLY field to return the project_id of the
            destination project.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    destination_project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=3,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=6,
    )
    description: str = proto.Field(
        proto.STRING,
        number=7,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=8,
    )
    destination_project_id: str = proto.Field(
        proto.STRING,
        number=9,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
