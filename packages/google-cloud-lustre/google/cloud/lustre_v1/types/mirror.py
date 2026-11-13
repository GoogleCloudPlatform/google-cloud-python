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

from google.cloud.lustre_v1.types import transfer

__protobuf__ = proto.module(
    package="google.cloud.lustre.v1",
    manifest={
        "Mirror",
        "CreateMirrorRequest",
        "UpdateMirrorRequest",
        "DeleteMirrorRequest",
        "GetMirrorRequest",
        "ListMirrorsRequest",
        "ListMirrorsResponse",
        "CreateMirrorMetadata",
    },
)


class Mirror(proto.Message):
    r"""Represents a Cloud Storage mirror.

    Attributes:
        name (str):
            Identifier. Name of the mirror. Format:
            ``projects/{project}/locations/{location}/instances/{instance}/mirrors/{mirror}``
        gcs_path (google.cloud.lustre_v1.types.GcsPath):
            Required. Immutable. The URI to a Cloud Storage bucket, or a
            path within a bucket, using the format
            ``gs://{BUCKET_NAME}/{OPTIONAL_PATH}/``. If a path inside
            the bucket is specified, it must end with a forward slash
            (``/``).
        lustre_path (google.cloud.lustre_v1.types.LustrePath):
            Required. Immutable. The Managed Lustre directory to mirror
            to. Must be an absolute path starting with ``/``, for
            example ``/data`` or ``/data/subdir``. Defaults to the root
            directory, ``/``. If the specified directory doesn't exist,
            it is created.
        direction (google.cloud.lustre_v1.types.Mirror.Direction):
            Required. Immutable. Represents the direction
            of the mirror.
        deleted_files_retained (bool):
            Optional. If ``true``, files are not deleted from Managed
            Lustre when the source files are deleted from Cloud Storage.
            Default is ``false``.
        description (str):
            Optional. Description of the mirror.
        labels (MutableMapping[str, str]):
            Optional. Labels to apply to the mirror.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. [Output only] Create time stamp.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. [Output only] Update time stamp.
        uid (str):
            Output only. Unique ID of the resource.
        state (google.cloud.lustre_v1.types.Mirror.State):
            Output only. [Output only] The current state of the mirror.
    """

    class Direction(proto.Enum):
        r"""Represents the direction of the mirror.
        This enum expects to be extended in future with new mirror
        types.

        Values:
            DIRECTION_UNSPECIFIED (0):
                Invalid value.
            FROM_CLOUD_STORAGE (1):
                Mirror from Cloud Storage to Lustre.
        """

        DIRECTION_UNSPECIFIED = 0
        FROM_CLOUD_STORAGE = 1

    class State(proto.Enum):
        r"""State of the mirror.

        Values:
            STATE_UNSPECIFIED (0):
                State is unspecified.
            CREATING (1):
                The mirror resource is being created.
            INITIAL_SYNC (2):
                The initial sync is copying existing objects
                from Cloud Storage.
            DELETING (3):
                The mirror is being deleted.
            ACTIVE (4):
                The mirror is synchronizing changes as they
                occur.
            SUSPENDED (5):
                Synchronization is paused because the file
                system is close to capacity.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        INITIAL_SYNC = 2
        DELETING = 3
        ACTIVE = 4
        SUSPENDED = 5

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    gcs_path: transfer.GcsPath = proto.Field(
        proto.MESSAGE,
        number=3,
        message=transfer.GcsPath,
    )
    lustre_path: transfer.LustrePath = proto.Field(
        proto.MESSAGE,
        number=4,
        message=transfer.LustrePath,
    )
    direction: Direction = proto.Field(
        proto.ENUM,
        number=5,
        enum=Direction,
    )
    deleted_files_retained: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    description: str = proto.Field(
        proto.STRING,
        number=7,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=8,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=11,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=12,
        enum=State,
    )


class CreateMirrorRequest(proto.Message):
    r"""Request for CreateMirror.

    Attributes:
        parent (str):
            Required. Parent instance resource where the mirror will be
            created, in the format:
            ``projects/{project}/locations/{location}/instances/{instance}``
        mirror_id (str):
            Required. The ID to use for the mirror.

            - Must contain only lowercase letters, numbers, and hyphens.
            - Must start with a letter.
            - Must be between 1-63 characters.
            - Must end with a number or a letter.

            The ID cannot be changed after the mirror is created.
        mirror (google.cloud.lustre_v1.types.Mirror):
            Required. The mirror to create.
        request_id (str):
            Optional. The unique ID to identify requests. Specify a
            unique request ID so that if you must retry your request,
            the server will know to ignore the request if it has already
            been completed. The server guarantees that a request doesn't
            result in creation of duplicate mirrors for at least 60
            minutes.

            For example, consider a situation where you make an initial
            request and the request times out. If you make the request
            again with the same request ID, the server can check if
            original operation with the same request ID was received,
            and if so, will ignore the second request. This prevents
            clients from accidentally creating duplicate mirrors.

            The request ID must be a valid UUID version 4 with the
            exception that zero UUID is not supported
            (``00000000-0000-0000-0000-000000000000``). This request is
            only idempotent if a ``request_id`` is provided.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    mirror_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    mirror: "Mirror" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Mirror",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateMirrorRequest(proto.Message):
    r"""Request for UpdateMirror.

    Attributes:
        mirror (google.cloud.lustre_v1.types.Mirror):
            Required. Mirror to update. The mirror's ``name`` field is
            used to identify the mirror to update, in the format:
            ``projects/{project}/locations/{location}/instances/{instance}/mirrors/{mirror}``
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Fields specified in the update_mask are relative
            to the resource, not the full request. A field will be
            overwritten if it is in the mask. If no mask is provided
            then all fields present in the request are overwritten.
        request_id (str):
            Optional. The unique ID to identify requests. Specify a
            unique request ID so that if you must retry your request,
            the server will know to ignore the request if it has already
            been completed. The server guarantees that a request doesn't
            result in the same update request being executed for at
            least 60 minutes.

            For example, consider a situation where you make an initial
            request and the request times out. If you make the request
            again with the same request ID, the server can check if
            original operation with the same request ID was received,
            and if so, will ignore the second request.

            The request ID must be a valid UUID version 4 with the
            exception that zero UUID is not supported
            (``00000000-0000-0000-0000-000000000000``). This request is
            only idempotent if a ``request_id`` is provided.
    """

    mirror: "Mirror" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Mirror",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteMirrorRequest(proto.Message):
    r"""Request for DeleteMirror.

    Attributes:
        name (str):
            Required. Name of the mirror to delete, in the format:
            ``projects/{project}/locations/{location}/instances/{instance}/mirrors/{mirror}``
        request_id (str):
            Optional. The unique ID to identify requests. Specify a
            unique request ID so that if you must retry your request,
            the server will know to ignore the request if it has already
            been completed. The server guarantees that a request doesn't
            result in the same delete request being executed for at
            least 60 minutes.

            For example, consider a situation where you make an initial
            request and the request times out. If you make the request
            again with the same request ID, the server can check if
            original operation with the same request ID was received,
            and if so, will ignore the second request.

            The request ID must be a valid UUID version 4 with the
            exception that zero UUID is not supported
            (``00000000-0000-0000-0000-000000000000``). This request is
            only idempotent if a ``request_id`` is provided.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetMirrorRequest(proto.Message):
    r"""Request for GetMirror.

    Attributes:
        name (str):
            Required. Name of the mirror to retrieve, in the format:
            ``projects/{project}/locations/{location}/instances/{instance}/mirrors/{mirror}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListMirrorsRequest(proto.Message):
    r"""Request for ListMirrors.

    Attributes:
        parent (str):
            Required. Parent instance resource where the mirrors will be
            listed, in the format:
            ``projects/{project}/locations/{location}/instances/{instance}``
        page_size (int):
            Optional. Requested page size. The server
            might return fewer items than requested. If
            unspecified, the default page size is 10. The
            maximum value is 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListMirrors`` call. Provide this to retrieve the
            subsequent page. When paginating, all other parameters
            provided to ``ListMirrors`` must match the call that
            provided the page token.
        order_by (str):
            Optional. Desired order of results.
        filter (str):
            Optional. Filtering results.
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


class ListMirrorsResponse(proto.Message):
    r"""Response for ListMirrors.

    Attributes:
        mirrors (MutableSequence[google.cloud.lustre_v1.types.Mirror]):
            List of mirrors on the instance.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Unordered list. Locations that could not be
            reached.
    """

    @property
    def raw_page(self):
        return self

    mirrors: MutableSequence["Mirror"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Mirror",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class CreateMirrorMetadata(proto.Message):
    r"""Metadata of the create mirror operation.

    Attributes:
        operation_metadata (google.cloud.lustre_v1.types.TransferOperationMetadata):
            Data transfer operation metadata.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation was
            created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation finished
            running.
        target (str):
            Output only. Server-defined resource path for
            the target of the operation.
        verb (str):
            Output only. Name of the verb executed by the
            operation.
        status_message (str):
            Output only. Human-readable status of the
            operation, if any.
        requested_cancellation (bool):
            Output only. Identifies whether the user has requested
            cancellation of the operation. Operations that have
            successfully been cancelled have
            [google.longrunning.Operation.error][google.longrunning.Operation.error]
            value with a
            [google.rpc.Status.code][google.rpc.Status.code] of 1,
            corresponding to ``Code.CANCELLED``.
        api_version (str):
            Output only. API version used to start the
            operation.
    """

    operation_metadata: transfer.TransferOperationMetadata = proto.Field(
        proto.MESSAGE,
        number=1,
        message=transfer.TransferOperationMetadata,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    target: str = proto.Field(
        proto.STRING,
        number=4,
    )
    verb: str = proto.Field(
        proto.STRING,
        number=5,
    )
    status_message: str = proto.Field(
        proto.STRING,
        number=6,
    )
    requested_cancellation: bool = proto.Field(
        proto.BOOL,
        number=7,
    )
    api_version: str = proto.Field(
        proto.STRING,
        number=8,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
