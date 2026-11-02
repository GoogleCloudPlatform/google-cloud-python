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

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.netapp.v1",
    manifest={
        "ListSnapshotsRequest",
        "ListSnapshotsResponse",
        "GetSnapshotRequest",
        "CreateSnapshotRequest",
        "DeleteSnapshotRequest",
        "UpdateSnapshotRequest",
        "Snapshot",
    },
)


class ListSnapshotsRequest(proto.Message):
    r"""ListSnapshotsRequest lists snapshots.

    Attributes:
        parent (str):
            Required. The volume for which to retrieve snapshot
            information, in the format
            ``projects/{project_id}/locations/{location}/volumes/{volume_id}``.
        page_size (int):
            The maximum number of items to return.
        page_token (str):
            The next_page_token value to use if there are additional
            results to retrieve for this list request.
        order_by (str):
            Sort results. Supported values are "name",
            "name desc" or "" (unsorted).
        filter (str):
            List filter.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=4,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListSnapshotsResponse(proto.Message):
    r"""ListSnapshotsResponse is the result of ListSnapshotsRequest.

    Attributes:
        snapshots (MutableSequence[google.cloud.netapp_v1.types.Snapshot]):
            A list of snapshots in the project for the
            specified volume.
        next_page_token (str):
            The token you can use to retrieve the next
            page of results. Not returned if there are no
            more results in the list.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    snapshots: MutableSequence["Snapshot"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Snapshot",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetSnapshotRequest(proto.Message):
    r"""GetSnapshotRequest gets the state of a snapshot.

    Attributes:
        name (str):
            Required. The snapshot resource name, in the format
            ``projects/{project_id}/locations/{location}/volumes/{volume_id}/snapshots/{snapshot_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateSnapshotRequest(proto.Message):
    r"""CreateSnapshotRequest creates a snapshot.

    Attributes:
        parent (str):
            Required. The NetApp volume to create the snapshots of, in
            the format
            ``projects/{project_id}/locations/{location}/volumes/{volume_id}``
        snapshot (google.cloud.netapp_v1.types.Snapshot):
            Required. A snapshot resource
        snapshot_id (str):
            Required. ID of the snapshot to create. Must
            be unique within the parent resource. Must
            contain only letters, numbers and hyphen, with
            the first character a letter, the last a letter
            or a
            number, and a 63 character maximum.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    snapshot: "Snapshot" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Snapshot",
    )
    snapshot_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteSnapshotRequest(proto.Message):
    r"""DeleteSnapshotRequest deletes a snapshot.

    Attributes:
        name (str):
            Required. The snapshot resource name, in the format
            ``projects/*/locations/*/volumes/*/snapshots/{snapshot_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateSnapshotRequest(proto.Message):
    r"""UpdateSnapshotRequest updates description and/or labels for a
    snapshot.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Mask of fields to update.  At least
            one path must be supplied in this field.
        snapshot (google.cloud.netapp_v1.types.Snapshot):
            Required. A snapshot resource
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    snapshot: "Snapshot" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Snapshot",
    )


class Snapshot(proto.Message):
    r"""Snapshot is a point-in-time version of a Volume's content.

    Attributes:
        name (str):
            Identifier. The resource name of the snapshot. Format:
            ``projects/{project_id}/locations/{location}/volumes/{volume_id}/snapshots/{snapshot_id}``.
        state (google.cloud.netapp_v1.types.Snapshot.State):
            Output only. The snapshot state.
        state_details (str):
            Output only. State details of the storage
            pool
        description (str):
            A description of the snapshot with 2048
            characters or less. Requests with longer
            descriptions will be rejected.
        used_bytes (float):
            Output only. Current storage usage for the
            snapshot in bytes.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the snapshot was
            created.
        labels (MutableMapping[str, str]):
            Resource labels to represent user provided
            metadata.
    """

    class State(proto.Enum):
        r"""The Snapshot States

        Values:
            STATE_UNSPECIFIED (0):
                Unspecified Snapshot State
            READY (1):
                Snapshot State is Ready
            CREATING (2):
                Snapshot State is Creating
            DELETING (3):
                Snapshot State is Deleting
            UPDATING (4):
                Snapshot State is Updating
            DISABLED (5):
                Snapshot State is Disabled
            ERROR (6):
                Snapshot State is Error
        """

        STATE_UNSPECIFIED = 0
        READY = 1
        CREATING = 2
        DELETING = 3
        UPDATING = 4
        DISABLED = 5
        ERROR = 6

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=2,
        enum=State,
    )
    state_details: str = proto.Field(
        proto.STRING,
        number=3,
    )
    description: str = proto.Field(
        proto.STRING,
        number=4,
    )
    used_bytes: float = proto.Field(
        proto.DOUBLE,
        number=5,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=7,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
