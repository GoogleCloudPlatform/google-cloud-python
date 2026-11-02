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
        "BackupPolicy",
        "CreateBackupPolicyRequest",
        "GetBackupPolicyRequest",
        "ListBackupPoliciesRequest",
        "ListBackupPoliciesResponse",
        "UpdateBackupPolicyRequest",
        "DeleteBackupPolicyRequest",
    },
)


class BackupPolicy(proto.Message):
    r"""Backup Policy.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the backup policy. Format:
            ``projects/{project_id}/locations/{location}/backupPolicies/{backup_policy_id}``.
        daily_backup_limit (int):
            Number of daily backups to keep. Note that
            the minimum daily backup limit is 2.

            This field is a member of `oneof`_ ``_daily_backup_limit``.
        weekly_backup_limit (int):
            Number of weekly backups to keep. Note that
            the sum of daily, weekly and monthly backups
            should be greater than 1.

            This field is a member of `oneof`_ ``_weekly_backup_limit``.
        monthly_backup_limit (int):
            Number of monthly backups to keep. Note that
            the sum of daily, weekly and monthly backups
            should be greater than 1.

            This field is a member of `oneof`_ ``_monthly_backup_limit``.
        description (str):
            Description of the backup policy.

            This field is a member of `oneof`_ ``_description``.
        enabled (bool):
            If enabled, make backups automatically
            according to the schedules. This will be applied
            to all volumes that have this policy attached
            and enforced on volume level. If not specified,
            default is true.

            This field is a member of `oneof`_ ``_enabled``.
        assigned_volume_count (int):
            Output only. The total number of volumes
            assigned by this backup policy.

            This field is a member of `oneof`_ ``_assigned_volume_count``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the backup policy
            was created.
        labels (MutableMapping[str, str]):
            Resource labels to represent user provided
            metadata.
        state (google.cloud.netapp_v1.types.BackupPolicy.State):
            Output only. The backup policy state.
    """

    class State(proto.Enum):
        r"""

        Values:
            STATE_UNSPECIFIED (0):
                State not set.
            CREATING (1):
                BackupPolicy is being created.
            READY (2):
                BackupPolicy is available for use.
            DELETING (3):
                BackupPolicy is being deleted.
            ERROR (4):
                BackupPolicy is not valid and cannot be used.
            UPDATING (5):
                BackupPolicy is being updated.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        READY = 2
        DELETING = 3
        ERROR = 4
        UPDATING = 5

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    daily_backup_limit: int = proto.Field(
        proto.INT32,
        number=2,
        optional=True,
    )
    weekly_backup_limit: int = proto.Field(
        proto.INT32,
        number=3,
        optional=True,
    )
    monthly_backup_limit: int = proto.Field(
        proto.INT32,
        number=4,
        optional=True,
    )
    description: str = proto.Field(
        proto.STRING,
        number=5,
        optional=True,
    )
    enabled: bool = proto.Field(
        proto.BOOL,
        number=6,
        optional=True,
    )
    assigned_volume_count: int = proto.Field(
        proto.INT32,
        number=7,
        optional=True,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=9,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=10,
        enum=State,
    )


class CreateBackupPolicyRequest(proto.Message):
    r"""CreateBackupPolicyRequest creates a backupPolicy.

    Attributes:
        parent (str):
            Required. The location to create the backup policies of, in
            the format ``projects/{project_id}/locations/{location}``
        backup_policy (google.cloud.netapp_v1.types.BackupPolicy):
            Required. A backupPolicy resource
        backup_policy_id (str):
            Required. The ID to use for the backup
            policy. The ID must be unique within the
            specified location. Must contain only letters,
            numbers and hyphen, with the first character a
            letter, the last a letter or a
            number, and a 63 character maximum.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    backup_policy: "BackupPolicy" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="BackupPolicy",
    )
    backup_policy_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class GetBackupPolicyRequest(proto.Message):
    r"""GetBackupPolicyRequest gets the state of a backupPolicy.

    Attributes:
        name (str):
            Required. The backupPolicy resource name, in the format
            ``projects/{project_id}/locations/{location}/backupPolicies/{backup_policy_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListBackupPoliciesRequest(proto.Message):
    r"""ListBackupPoliciesRequest for requesting multiple backup
    policies.

    Attributes:
        parent (str):
            Required. Parent value for
            ListBackupPoliciesRequest
        page_size (int):
            Requested page size. Server may return fewer
            items than requested. If unspecified, the server
            will pick an appropriate default.
        page_token (str):
            A token identifying a page of results the
            server should return.
        filter (str):
            Filtering results
        order_by (str):
            Hint for how to order the results
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
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListBackupPoliciesResponse(proto.Message):
    r"""ListBackupPoliciesResponse contains all the backup policies
    requested.

    Attributes:
        backup_policies (MutableSequence[google.cloud.netapp_v1.types.BackupPolicy]):
            The list of backup policies.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    backup_policies: MutableSequence["BackupPolicy"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="BackupPolicy",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class UpdateBackupPolicyRequest(proto.Message):
    r"""UpdateBackupPolicyRequest for updating a backup policy.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten in the Backup Policy resource by the update. The
            fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. If the user does not provide a mask
            then all fields will be overwritten.
        backup_policy (google.cloud.netapp_v1.types.BackupPolicy):
            Required. The backup policy being updated
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    backup_policy: "BackupPolicy" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="BackupPolicy",
    )


class DeleteBackupPolicyRequest(proto.Message):
    r"""DeleteBackupPolicyRequest deletes a backup policy.

    Attributes:
        name (str):
            Required. The backup policy resource name, in the format
            ``projects/{project_id}/locations/{location}/backupPolicies/{backup_policy_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
