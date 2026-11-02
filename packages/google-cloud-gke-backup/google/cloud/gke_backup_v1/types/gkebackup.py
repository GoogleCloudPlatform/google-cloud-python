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

from google.cloud.gke_backup_v1.types import backup as gcg_backup
from google.cloud.gke_backup_v1.types import backup_channel as gcg_backup_channel
from google.cloud.gke_backup_v1.types import backup_plan as gcg_backup_plan
from google.cloud.gke_backup_v1.types import (
    backup_plan_binding,
    restore_plan_binding,
    volume,
)
from google.cloud.gke_backup_v1.types import restore as gcg_restore
from google.cloud.gke_backup_v1.types import restore_channel as gcg_restore_channel
from google.cloud.gke_backup_v1.types import restore_plan as gcg_restore_plan

__protobuf__ = proto.module(
    package="google.cloud.gkebackup.v1",
    manifest={
        "OperationMetadata",
        "CreateBackupPlanRequest",
        "ListBackupPlansRequest",
        "ListBackupPlansResponse",
        "GetBackupPlanRequest",
        "UpdateBackupPlanRequest",
        "DeleteBackupPlanRequest",
        "CreateBackupChannelRequest",
        "ListBackupChannelsRequest",
        "ListBackupChannelsResponse",
        "GetBackupChannelRequest",
        "UpdateBackupChannelRequest",
        "DeleteBackupChannelRequest",
        "ListBackupPlanBindingsRequest",
        "ListBackupPlanBindingsResponse",
        "GetBackupPlanBindingRequest",
        "CreateBackupRequest",
        "ListBackupsRequest",
        "ListBackupsResponse",
        "GetBackupRequest",
        "UpdateBackupRequest",
        "DeleteBackupRequest",
        "ListVolumeBackupsRequest",
        "ListVolumeBackupsResponse",
        "GetVolumeBackupRequest",
        "CreateRestorePlanRequest",
        "ListRestorePlansRequest",
        "ListRestorePlansResponse",
        "GetRestorePlanRequest",
        "UpdateRestorePlanRequest",
        "DeleteRestorePlanRequest",
        "CreateRestoreChannelRequest",
        "ListRestoreChannelsRequest",
        "ListRestoreChannelsResponse",
        "GetRestoreChannelRequest",
        "UpdateRestoreChannelRequest",
        "DeleteRestoreChannelRequest",
        "ListRestorePlanBindingsRequest",
        "ListRestorePlanBindingsResponse",
        "GetRestorePlanBindingRequest",
        "CreateRestoreRequest",
        "ListRestoresRequest",
        "ListRestoresResponse",
        "GetRestoreRequest",
        "UpdateRestoreRequest",
        "DeleteRestoreRequest",
        "ListVolumeRestoresRequest",
        "ListVolumeRestoresResponse",
        "GetVolumeRestoreRequest",
        "GetBackupIndexDownloadUrlRequest",
        "GetBackupIndexDownloadUrlResponse",
    },
)


class OperationMetadata(proto.Message):
    r"""Represents the metadata of the long-running operation.

    Attributes:
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

    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    target: str = proto.Field(
        proto.STRING,
        number=3,
    )
    verb: str = proto.Field(
        proto.STRING,
        number=4,
    )
    status_message: str = proto.Field(
        proto.STRING,
        number=5,
    )
    requested_cancellation: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    api_version: str = proto.Field(
        proto.STRING,
        number=7,
    )


class CreateBackupPlanRequest(proto.Message):
    r"""Request message for CreateBackupPlan.

    Attributes:
        parent (str):
            Required. The location within which to create the
            BackupPlan. Format: ``projects/*/locations/*``
        backup_plan (google.cloud.gke_backup_v1.types.BackupPlan):
            Required. The BackupPlan resource object to
            create.
        backup_plan_id (str):
            Required. The client-provided short name for
            the BackupPlan resource. This name must:

            - be between 1 and 63 characters long
              (inclusive)
            - consist of only lower-case ASCII letters,
              numbers, and dashes
            - start with a lower-case letter
            - end with a lower-case letter or number
            - be unique within the set of BackupPlans in
              this location
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    backup_plan: gcg_backup_plan.BackupPlan = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcg_backup_plan.BackupPlan,
    )
    backup_plan_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListBackupPlansRequest(proto.Message):
    r"""Request message for ListBackupPlans.

    Attributes:
        parent (str):
            Required. The location that contains the BackupPlans to
            list. Format: ``projects/*/locations/*``
        page_size (int):
            Optional. The target number of results to return in a single
            response. If not specified, a default value will be chosen
            by the service. Note that the response may include a partial
            list and a caller should only rely on the response's
            [next_page_token][google.cloud.gkebackup.v1.ListBackupPlansResponse.next_page_token]
            to determine if there are more instances left to be queried.
        page_token (str):
            Optional. The value of
            [next_page_token][google.cloud.gkebackup.v1.ListBackupPlansResponse.next_page_token]
            received from a previous ``ListBackupPlans`` call. Provide
            this to retrieve the subsequent page in a multi-page list of
            results. When paginating, all other parameters provided to
            ``ListBackupPlans`` must match the call that provided the
            page token.
        filter (str):
            Optional. Field match expression used to
            filter the results.
        order_by (str):
            Optional. Field by which to sort the results.
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


class ListBackupPlansResponse(proto.Message):
    r"""Response message for ListBackupPlans.

    Attributes:
        backup_plans (MutableSequence[google.cloud.gke_backup_v1.types.BackupPlan]):
            The list of BackupPlans matching the given
            criteria.
        next_page_token (str):
            A token which may be sent as
            [page_token][google.cloud.gkebackup.v1.ListBackupPlansRequest.page_token]
            in a subsequent ``ListBackupPlans`` call to retrieve the
            next page of results. If this field is omitted or empty,
            then there are no more results to return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    backup_plans: MutableSequence[gcg_backup_plan.BackupPlan] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcg_backup_plan.BackupPlan,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetBackupPlanRequest(proto.Message):
    r"""Request message for GetBackupPlan.

    Attributes:
        name (str):
            Required. Fully qualified BackupPlan name. Format:
            ``projects/*/locations/*/backupPlans/*``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateBackupPlanRequest(proto.Message):
    r"""Request message for UpdateBackupPlan.

    Attributes:
        backup_plan (google.cloud.gke_backup_v1.types.BackupPlan):
            Required. A new version of the BackupPlan resource that
            contains updated fields. This may be sparsely populated if
            an ``update_mask`` is provided.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. This is used to specify the fields to be
            overwritten in the BackupPlan targeted for update. The
            values for each of these updated fields will be taken from
            the ``backup_plan`` provided with this request. Field names
            are relative to the root of the resource (e.g.,
            ``description``, ``backup_config.include_volume_data``,
            etc.) If no ``update_mask`` is provided, all fields in
            ``backup_plan`` will be written to the target BackupPlan
            resource. Note that OUTPUT_ONLY and IMMUTABLE fields in
            ``backup_plan`` are ignored and are not used to update the
            target BackupPlan.
    """

    backup_plan: gcg_backup_plan.BackupPlan = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcg_backup_plan.BackupPlan,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteBackupPlanRequest(proto.Message):
    r"""Request message for DeleteBackupPlan.

    Attributes:
        name (str):
            Required. Fully qualified BackupPlan name. Format:
            ``projects/*/locations/*/backupPlans/*``
        etag (str):
            Optional. If provided, this value must match the current
            value of the target BackupPlan's
            [etag][google.cloud.gkebackup.v1.BackupPlan.etag] field or
            the request is rejected.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateBackupChannelRequest(proto.Message):
    r"""Request message for CreateBackupChannel.

    Attributes:
        parent (str):
            Required. The location within which to create the
            BackupChannel. Format: ``projects/*/locations/*``
        backup_channel (google.cloud.gke_backup_v1.types.BackupChannel):
            Required. The BackupChannel resource object
            to create.
        backup_channel_id (str):
            Optional. The client-provided short name for
            the BackupChannel resource. This name must:

            - be between 1 and 63 characters long
              (inclusive)
            - consist of only lower-case ASCII letters,
              numbers, and dashes
            - start with a lower-case letter
            - end with a lower-case letter or number
            - be unique within the set of BackupChannels in
              this location If the user does not provide a
              name, a uuid will be used as the name.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    backup_channel: gcg_backup_channel.BackupChannel = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcg_backup_channel.BackupChannel,
    )
    backup_channel_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListBackupChannelsRequest(proto.Message):
    r"""Request message for ListBackupChannels.

    Attributes:
        parent (str):
            Required. The location that contains the BackupChannels to
            list. Format: ``projects/*/locations/*``
        page_size (int):
            Optional. The target number of results to return in a single
            response. If not specified, a default value will be chosen
            by the service. Note that the response may include a partial
            list and a caller should only rely on the response's
            [next_page_token][google.cloud.gkebackup.v1.ListBackupChannelsResponse.next_page_token]
            to determine if there are more instances left to be queried.
        page_token (str):
            Optional. The value of
            [next_page_token][google.cloud.gkebackup.v1.ListBackupChannelsResponse.next_page_token]
            received from a previous ``ListBackupChannels`` call.
            Provide this to retrieve the subsequent page in a multi-page
            list of results. When paginating, all other parameters
            provided to ``ListBackupChannels`` must match the call that
            provided the page token.
        filter (str):
            Optional. Field match expression used to
            filter the results.
        order_by (str):
            Optional. Field by which to sort the results.
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


class ListBackupChannelsResponse(proto.Message):
    r"""Response message for ListBackupChannels.

    Attributes:
        backup_channels (MutableSequence[google.cloud.gke_backup_v1.types.BackupChannel]):
            The list of BackupChannels matching the given
            criteria.
        next_page_token (str):
            A token which may be sent as
            [page_token][google.cloud.gkebackup.v1.ListBackupChannelsRequest.page_token]
            in a subsequent ``ListBackupChannels`` call to retrieve the
            next page of results. If this field is omitted or empty,
            then there are no more results to return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    backup_channels: MutableSequence[gcg_backup_channel.BackupChannel] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=gcg_backup_channel.BackupChannel,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetBackupChannelRequest(proto.Message):
    r"""Request message for GetBackupChannel.

    Attributes:
        name (str):
            Required. Fully qualified BackupChannel name. Format:
            ``projects/*/locations/*/backupChannels/*``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateBackupChannelRequest(proto.Message):
    r"""Request message for UpdateBackupChannel.

    Attributes:
        backup_channel (google.cloud.gke_backup_v1.types.BackupChannel):
            Required. A new version of the BackupChannel resource that
            contains updated fields. This may be sparsely populated if
            an ``update_mask`` is provided.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. This is used to specify the fields to be
            overwritten in the BackupChannel targeted for update. The
            values for each of these updated fields will be taken from
            the ``backup_channel`` provided with this request. Field
            names are relative to the root of the resource (e.g.,
            ``description``, ``labels``, etc.) If no ``update_mask`` is
            provided, all fields in ``backup_channel`` will be written
            to the target BackupChannel resource. Note that OUTPUT_ONLY
            and IMMUTABLE fields in ``backup_channel`` are ignored and
            are not used to update the target BackupChannel.
    """

    backup_channel: gcg_backup_channel.BackupChannel = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcg_backup_channel.BackupChannel,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteBackupChannelRequest(proto.Message):
    r"""Request message for DeleteBackupChannel.

    Attributes:
        name (str):
            Required. Fully qualified BackupChannel name. Format:
            ``projects/*/locations/*/backupChannels/*``
        etag (str):
            Optional. If provided, this value must match the current
            value of the target BackupChannel's
            [etag][google.cloud.gkebackup.v1.BackupChannel.etag] field
            or the request is rejected.
        force (bool):
            Optional. If set to true, any
            BackupPlanAssociations below this BackupChannel
            will also be deleted. Otherwise, the request
            will only succeed if the BackupChannel has no
            BackupPlanAssociations.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=2,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class ListBackupPlanBindingsRequest(proto.Message):
    r"""Request message for ListBackupPlanBindings.

    Attributes:
        parent (str):
            Required. The BackupChannel that contains the
            BackupPlanBindings to list. Format:
            ``projects/*/locations/*/backupChannels/*``
        page_size (int):
            Optional. The target number of results to return in a single
            response. If not specified, a default value will be chosen
            by the service. Note that the response may include a partial
            list and a caller should only rely on the response's
            [next_page_token][google.cloud.gkebackup.v1.ListBackupPlanBindingsResponse.next_page_token]
            to determine if there are more instances left to be queried.
        page_token (str):
            Optional. The value of
            [next_page_token][google.cloud.gkebackup.v1.ListBackupPlanBindingsResponse.next_page_token]
            received from a previous ``ListBackupPlanBindings`` call.
            Provide this to retrieve the subsequent page in a multi-page
            list of results. When paginating, all other parameters
            provided to ``ListBackupPlanBindings`` must match the call
            that provided the page token.
        filter (str):
            Optional. Field match expression used to
            filter the results.
        order_by (str):
            Optional. Field by which to sort the results.
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


class ListBackupPlanBindingsResponse(proto.Message):
    r"""Response message for ListBackupPlanBindings.

    Attributes:
        backup_plan_bindings (MutableSequence[google.cloud.gke_backup_v1.types.BackupPlanBinding]):
            The list of BackupPlanBindings matching the
            given criteria.
        next_page_token (str):
            A token which may be sent as
            [page_token][google.cloud.gkebackup.v1.ListBackupPlanBindingsRequest.page_token]
            in a subsequent ``ListBackupPlanBindingss`` call to retrieve
            the next page of results. If this field is omitted or empty,
            then there are no more results to return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    backup_plan_bindings: MutableSequence[backup_plan_binding.BackupPlanBinding] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=backup_plan_binding.BackupPlanBinding,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetBackupPlanBindingRequest(proto.Message):
    r"""Request message for GetBackupPlanBinding.

    Attributes:
        name (str):
            Required. Fully qualified BackupPlanBinding name. Format:
            ``projects/*/locations/*/backupChannels/*/backupPlanBindings/*``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateBackupRequest(proto.Message):
    r"""Request message for CreateBackup.

    Attributes:
        parent (str):
            Required. The BackupPlan within which to create the Backup.
            Format: ``projects/*/locations/*/backupPlans/*``
        backup (google.cloud.gke_backup_v1.types.Backup):
            Optional. The Backup resource to create.
        backup_id (str):
            Optional. The client-provided short name for
            the Backup resource. This name must:

            - be between 1 and 63 characters long
              (inclusive)
            - consist of only lower-case ASCII letters,
              numbers, and dashes
            - start with a lower-case letter
            - end with a lower-case letter or number
            - be unique within the set of Backups in this
              BackupPlan
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    backup: gcg_backup.Backup = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcg_backup.Backup,
    )
    backup_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListBackupsRequest(proto.Message):
    r"""Request message for ListBackups.

    Attributes:
        parent (str):
            Required. The BackupPlan that contains the Backups to list.
            Format: ``projects/*/locations/*/backupPlans/*``
        page_size (int):
            Optional. The target number of results to return in a single
            response. If not specified, a default value will be chosen
            by the service. Note that the response may include a partial
            list and a caller should only rely on the response's
            [next_page_token][google.cloud.gkebackup.v1.ListBackupsResponse.next_page_token]
            to determine if there are more instances left to be queried.
        page_token (str):
            Optional. The value of
            [next_page_token][google.cloud.gkebackup.v1.ListBackupsResponse.next_page_token]
            received from a previous ``ListBackups`` call. Provide this
            to retrieve the subsequent page in a multi-page list of
            results. When paginating, all other parameters provided to
            ``ListBackups`` must match the call that provided the page
            token.
        filter (str):
            Optional. Field match expression used to
            filter the results.
        order_by (str):
            Optional. Field by which to sort the results.
        return_partial_success (bool):
            Optional. If set to true, the response will
            return partial results when some regions are
            unreachable and the unreachable field will be
            populated.
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
    return_partial_success: bool = proto.Field(
        proto.BOOL,
        number=6,
    )


class ListBackupsResponse(proto.Message):
    r"""Response message for ListBackups.

    Attributes:
        backups (MutableSequence[google.cloud.gke_backup_v1.types.Backup]):
            The list of Backups matching the given
            criteria.
        next_page_token (str):
            A token which may be sent as
            [page_token][google.cloud.gkebackup.v1.ListBackupsRequest.page_token]
            in a subsequent ``ListBackups`` call to retrieve the next
            page of results. If this field is omitted or empty, then
            there are no more results to return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    backups: MutableSequence[gcg_backup.Backup] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcg_backup.Backup,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetBackupRequest(proto.Message):
    r"""Request message for GetBackup.

    Attributes:
        name (str):
            Required. Full name of the Backup resource. Format:
            ``projects/*/locations/*/backupPlans/*/backups/*``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateBackupRequest(proto.Message):
    r"""Request message for UpdateBackup.

    Attributes:
        backup (google.cloud.gke_backup_v1.types.Backup):
            Required. A new version of the Backup resource that contains
            updated fields. This may be sparsely populated if an
            ``update_mask`` is provided.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. This is used to specify the fields to be
            overwritten in the Backup targeted for update. The values
            for each of these updated fields will be taken from the
            ``backup_plan`` provided with this request. Field names are
            relative to the root of the resource. If no ``update_mask``
            is provided, all fields in ``backup`` will be written to the
            target Backup resource. Note that OUTPUT_ONLY and IMMUTABLE
            fields in ``backup`` are ignored and are not used to update
            the target Backup.
    """

    backup: gcg_backup.Backup = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcg_backup.Backup,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteBackupRequest(proto.Message):
    r"""Request message for DeleteBackup.

    Attributes:
        name (str):
            Required. Name of the Backup resource. Format:
            ``projects/*/locations/*/backupPlans/*/backups/*``
        etag (str):
            Optional. If provided, this value must match the current
            value of the target Backup's
            [etag][google.cloud.gkebackup.v1.Backup.etag] field or the
            request is rejected.
        force (bool):
            Optional. If set to true, any VolumeBackups
            below this Backup will also be deleted.
            Otherwise, the request will only succeed if the
            Backup has no VolumeBackups.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=2,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class ListVolumeBackupsRequest(proto.Message):
    r"""Request message for ListVolumeBackups.

    Attributes:
        parent (str):
            Required. The Backup that contains the VolumeBackups to
            list. Format:
            ``projects/*/locations/*/backupPlans/*/backups/*``
        page_size (int):
            Optional. The target number of results to return in a single
            response. If not specified, a default value will be chosen
            by the service. Note that the response may include a partial
            list and a caller should only rely on the response's
            [next_page_token][google.cloud.gkebackup.v1.ListVolumeBackupsResponse.next_page_token]
            to determine if there are more instances left to be queried.
        page_token (str):
            Optional. The value of
            [next_page_token][google.cloud.gkebackup.v1.ListVolumeBackupsResponse.next_page_token]
            received from a previous ``ListVolumeBackups`` call. Provide
            this to retrieve the subsequent page in a multi-page list of
            results. When paginating, all other parameters provided to
            ``ListVolumeBackups`` must match the call that provided the
            page token.
        filter (str):
            Optional. Field match expression used to
            filter the results.
        order_by (str):
            Optional. Field by which to sort the results.
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


class ListVolumeBackupsResponse(proto.Message):
    r"""Response message for ListVolumeBackups.

    Attributes:
        volume_backups (MutableSequence[google.cloud.gke_backup_v1.types.VolumeBackup]):
            The list of VolumeBackups matching the given
            criteria.
        next_page_token (str):
            A token which may be sent as
            [page_token][google.cloud.gkebackup.v1.ListVolumeBackupsRequest.page_token]
            in a subsequent ``ListVolumeBackups`` call to retrieve the
            next page of results. If this field is omitted or empty,
            then there are no more results to return.
    """

    @property
    def raw_page(self):
        return self

    volume_backups: MutableSequence[volume.VolumeBackup] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=volume.VolumeBackup,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetVolumeBackupRequest(proto.Message):
    r"""Request message for GetVolumeBackup.

    Attributes:
        name (str):
            Required. Full name of the VolumeBackup resource. Format:
            ``projects/*/locations/*/backupPlans/*/backups/*/volumeBackups/*``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateRestorePlanRequest(proto.Message):
    r"""Request message for CreateRestorePlan.

    Attributes:
        parent (str):
            Required. The location within which to create the
            RestorePlan. Format: ``projects/*/locations/*``
        restore_plan (google.cloud.gke_backup_v1.types.RestorePlan):
            Required. The RestorePlan resource object to
            create.
        restore_plan_id (str):
            Required. The client-provided short name for
            the RestorePlan resource. This name must:

            - be between 1 and 63 characters long
              (inclusive)
            - consist of only lower-case ASCII letters,
              numbers, and dashes
            - start with a lower-case letter
            - end with a lower-case letter or number
            - be unique within the set of RestorePlans in
              this location
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    restore_plan: gcg_restore_plan.RestorePlan = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcg_restore_plan.RestorePlan,
    )
    restore_plan_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListRestorePlansRequest(proto.Message):
    r"""Request message for ListRestorePlans.

    Attributes:
        parent (str):
            Required. The location that contains the RestorePlans to
            list. Format: ``projects/*/locations/*``
        page_size (int):
            Optional. The target number of results to return in a single
            response. If not specified, a default value will be chosen
            by the service. Note that the response may include a partial
            list and a caller should only rely on the response's
            [next_page_token][google.cloud.gkebackup.v1.ListRestorePlansResponse.next_page_token]
            to determine if there are more instances left to be queried.
        page_token (str):
            Optional. The value of
            [next_page_token][google.cloud.gkebackup.v1.ListRestorePlansResponse.next_page_token]
            received from a previous ``ListRestorePlans`` call. Provide
            this to retrieve the subsequent page in a multi-page list of
            results. When paginating, all other parameters provided to
            ``ListRestorePlans`` must match the call that provided the
            page token.
        filter (str):
            Optional. Field match expression used to
            filter the results.
        order_by (str):
            Optional. Field by which to sort the results.
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


class ListRestorePlansResponse(proto.Message):
    r"""Response message for ListRestorePlans.

    Attributes:
        restore_plans (MutableSequence[google.cloud.gke_backup_v1.types.RestorePlan]):
            The list of RestorePlans matching the given
            criteria.
        next_page_token (str):
            A token which may be sent as
            [page_token][google.cloud.gkebackup.v1.ListRestorePlansRequest.page_token]
            in a subsequent ``ListRestorePlans`` call to retrieve the
            next page of results. If this field is omitted or empty,
            then there are no more results to return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    restore_plans: MutableSequence[gcg_restore_plan.RestorePlan] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcg_restore_plan.RestorePlan,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetRestorePlanRequest(proto.Message):
    r"""Request message for GetRestorePlan.

    Attributes:
        name (str):
            Required. Fully qualified RestorePlan name. Format:
            ``projects/*/locations/*/restorePlans/*``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateRestorePlanRequest(proto.Message):
    r"""Request message for UpdateRestorePlan.

    Attributes:
        restore_plan (google.cloud.gke_backup_v1.types.RestorePlan):
            Required. A new version of the RestorePlan resource that
            contains updated fields. This may be sparsely populated if
            an ``update_mask`` is provided.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. This is used to specify the fields to be
            overwritten in the RestorePlan targeted for update. The
            values for each of these updated fields will be taken from
            the ``restore_plan`` provided with this request. Field names
            are relative to the root of the resource. If no
            ``update_mask`` is provided, all fields in ``restore_plan``
            will be written to the target RestorePlan resource. Note
            that OUTPUT_ONLY and IMMUTABLE fields in ``restore_plan``
            are ignored and are not used to update the target
            RestorePlan.
    """

    restore_plan: gcg_restore_plan.RestorePlan = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcg_restore_plan.RestorePlan,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteRestorePlanRequest(proto.Message):
    r"""Request message for DeleteRestorePlan.

    Attributes:
        name (str):
            Required. Fully qualified RestorePlan name. Format:
            ``projects/*/locations/*/restorePlans/*``
        etag (str):
            Optional. If provided, this value must match the current
            value of the target RestorePlan's
            [etag][google.cloud.gkebackup.v1.RestorePlan.etag] field or
            the request is rejected.
        force (bool):
            Optional. If set to true, any Restores below
            this RestorePlan will also be deleted.
            Otherwise, the request will only succeed if the
            RestorePlan has no Restores.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=2,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class CreateRestoreChannelRequest(proto.Message):
    r"""Request message for CreateRestoreChannel.

    Attributes:
        parent (str):
            Required. The location within which to create the
            RestoreChannel. Format: ``projects/*/locations/*``
        restore_channel (google.cloud.gke_backup_v1.types.RestoreChannel):
            Required. The RestoreChannel resource object
            to create.
        restore_channel_id (str):
            Optional. The client-provided short name for
            the RestoreChannel resource. This name must:

            - be between 1 and 63 characters long
              (inclusive)
            - consist of only lower-case ASCII letters,
              numbers, and dashes
            - start with a lower-case letter
            - end with a lower-case letter or number
            - be unique within the set of RestoreChannels in
              this location If the user does not provide a
              name, a uuid will be used as the name.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    restore_channel: gcg_restore_channel.RestoreChannel = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcg_restore_channel.RestoreChannel,
    )
    restore_channel_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListRestoreChannelsRequest(proto.Message):
    r"""Request message for ListRestoreChannels.

    Attributes:
        parent (str):
            Required. The location that contains the RestoreChannels to
            list. Format: ``projects/*/locations/*``
        page_size (int):
            Optional. The target number of results to return in a single
            response. If not specified, a default value will be chosen
            by the service. Note that the response may include a partial
            list and a caller should only rely on the response's
            [next_page_token][google.cloud.gkebackup.v1.ListRestoreChannelsResponse.next_page_token]
            to determine if there are more instances left to be queried.
        page_token (str):
            Optional. The value of
            [next_page_token][google.cloud.gkebackup.v1.ListRestoreChannelsResponse.next_page_token]
            received from a previous ``ListRestoreChannels`` call.
            Provide this to retrieve the subsequent page in a multi-page
            list of results. When paginating, all other parameters
            provided to ``ListRestoreChannels`` must match the call that
            provided the page token.
        filter (str):
            Optional. Field match expression used to
            filter the results.
        order_by (str):
            Optional. Field by which to sort the results.
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


class ListRestoreChannelsResponse(proto.Message):
    r"""Response message for ListRestoreChannels.

    Attributes:
        restore_channels (MutableSequence[google.cloud.gke_backup_v1.types.RestoreChannel]):
            The list of RestoreChannels matching the
            given criteria.
        next_page_token (str):
            A token which may be sent as
            [page_token][google.cloud.gkebackup.v1.ListRestoreChannelsRequest.page_token]
            in a subsequent ``ListRestoreChannels`` call to retrieve the
            next page of results. If this field is omitted or empty,
            then there are no more results to return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    restore_channels: MutableSequence[gcg_restore_channel.RestoreChannel] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=gcg_restore_channel.RestoreChannel,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetRestoreChannelRequest(proto.Message):
    r"""Request message for GetRestoreChannel.

    Attributes:
        name (str):
            Required. Fully qualified RestoreChannel name. Format:
            ``projects/*/locations/*/restoreChannels/*``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateRestoreChannelRequest(proto.Message):
    r"""Request message for UpdateRestoreChannel.

    Attributes:
        restore_channel (google.cloud.gke_backup_v1.types.RestoreChannel):
            Required. A new version of the RestoreChannel resource that
            contains updated fields. This may be sparsely populated if
            an ``update_mask`` is provided.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. This is used to specify the fields to be
            overwritten in the RestoreChannel targeted for update. The
            values for each of these updated fields will be taken from
            the ``restore_channel`` provided with this request. Field
            names are relative to the root of the resource (e.g.,
            ``description``, ``destination_project_id``, etc.) If no
            ``update_mask`` is provided, all fields in
            ``restore_channel`` will be written to the target
            RestoreChannel resource. Note that OUTPUT_ONLY and IMMUTABLE
            fields in ``restore_channel`` are ignored and are not used
            to update the target RestoreChannel.
    """

    restore_channel: gcg_restore_channel.RestoreChannel = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcg_restore_channel.RestoreChannel,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteRestoreChannelRequest(proto.Message):
    r"""Request message for DeleteRestoreChannel.

    Attributes:
        name (str):
            Required. Fully qualified RestoreChannel name. Format:
            ``projects/*/locations/*/restoreChannels/*``
        etag (str):
            Optional. If provided, this value must match the current
            value of the target RestoreChannel's
            [etag][google.cloud.gkebackup.v1.RestoreChannel.etag] field
            or the request is rejected.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListRestorePlanBindingsRequest(proto.Message):
    r"""Request message for ListRestorePlanBindings.

    Attributes:
        parent (str):
            Required. The RestoreChannel that contains the
            ListRestorePlanBindings to list. Format:
            ``projects/*/locations/*/restoreChannels/*``
        page_size (int):
            Optional. The target number of results to return in a single
            response. If not specified, a default value will be chosen
            by the service. Note that the response may include a partial
            list and a caller should only rely on the response's
            [next_page_token][google.cloud.gkebackup.v1.ListRestorePlanBindingsResponse.next_page_token]
            to determine if there are more instances left to be queried.
        page_token (str):
            Optional. The value of
            [next_page_token][google.cloud.gkebackup.v1.ListRestorePlanBindingsResponse.next_page_token]
            received from a previous ``ListRestorePlanBindings`` call.
            Provide this to retrieve the subsequent page in a multi-page
            list of results. When paginating, all other parameters
            provided to ``ListRestorePlanBindings`` must match the call
            that provided the page token.
        filter (str):
            Optional. Field match expression used to
            filter the results.
        order_by (str):
            Optional. Field by which to sort the results.
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


class ListRestorePlanBindingsResponse(proto.Message):
    r"""Response message for ListRestorePlanBindings.

    Attributes:
        restore_plan_bindings (MutableSequence[google.cloud.gke_backup_v1.types.RestorePlanBinding]):
            The list of RestorePlanBindings matching the
            given criteria.
        next_page_token (str):
            A token which may be sent as
            [page_token][google.cloud.gkebackup.v1.ListRestorePlanBindingsRequest.page_token]
            in a subsequent ``ListRestorePlanBindings`` call to retrieve
            the next page of results. If this field is omitted or empty,
            then there are no more results to return.
        unreachable (MutableSequence[str]):
            Unordered list. Locations that could not be
            reached.
    """

    @property
    def raw_page(self):
        return self

    restore_plan_bindings: MutableSequence[restore_plan_binding.RestorePlanBinding] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=restore_plan_binding.RestorePlanBinding,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetRestorePlanBindingRequest(proto.Message):
    r"""Request message for GetRestorePlanBinding.

    Attributes:
        name (str):
            Required. Fully qualified RestorePlanBinding name. Format:
            ``projects/*/locations/*/restoreChannels/*/restorePlanBindings/*``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateRestoreRequest(proto.Message):
    r"""Request message for CreateRestore.

    Attributes:
        parent (str):
            Required. The RestorePlan within which to create the
            Restore. Format: ``projects/*/locations/*/restorePlans/*``
        restore (google.cloud.gke_backup_v1.types.Restore):
            Required. The restore resource to create.
        restore_id (str):
            Required. The client-provided short name for
            the Restore resource. This name must:

            - be between 1 and 63 characters long
              (inclusive)
            - consist of only lower-case ASCII letters,
              numbers, and dashes
            - start with a lower-case letter
            - end with a lower-case letter or number
            - be unique within the set of Restores in this
              RestorePlan.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    restore: gcg_restore.Restore = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcg_restore.Restore,
    )
    restore_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListRestoresRequest(proto.Message):
    r"""Request message for ListRestores.

    Attributes:
        parent (str):
            Required. The RestorePlan that contains the Restores to
            list. Format: ``projects/*/locations/*/restorePlans/*``
        page_size (int):
            Optional. The target number of results to return in a single
            response. If not specified, a default value will be chosen
            by the service. Note that the response may include a partial
            list and a caller should only rely on the response's
            [next_page_token][google.cloud.gkebackup.v1.ListRestoresResponse.next_page_token]
            to determine if there are more instances left to be queried.
        page_token (str):
            Optional. The value of
            [next_page_token][google.cloud.gkebackup.v1.ListRestoresResponse.next_page_token]
            received from a previous ``ListRestores`` call. Provide this
            to retrieve the subsequent page in a multi-page list of
            results. When paginating, all other parameters provided to
            ``ListRestores`` must match the call that provided the page
            token.
        filter (str):
            Optional. Field match expression used to
            filter the results.
        order_by (str):
            Optional. Field by which to sort the results.
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


class ListRestoresResponse(proto.Message):
    r"""Response message for ListRestores.

    Attributes:
        restores (MutableSequence[google.cloud.gke_backup_v1.types.Restore]):
            The list of Restores matching the given
            criteria.
        next_page_token (str):
            A token which may be sent as
            [page_token][google.cloud.gkebackup.v1.ListRestoresRequest.page_token]
            in a subsequent ``ListRestores`` call to retrieve the next
            page of results. If this field is omitted or empty, then
            there are no more results to return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    restores: MutableSequence[gcg_restore.Restore] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcg_restore.Restore,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetRestoreRequest(proto.Message):
    r"""Request message for GetRestore.

    Attributes:
        name (str):
            Required. Name of the restore resource. Format:
            ``projects/*/locations/*/restorePlans/*/restores/*``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateRestoreRequest(proto.Message):
    r"""Request message for UpdateRestore.

    Attributes:
        restore (google.cloud.gke_backup_v1.types.Restore):
            Required. A new version of the Restore resource that
            contains updated fields. This may be sparsely populated if
            an ``update_mask`` is provided.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. This is used to specify the fields to be
            overwritten in the Restore targeted for update. The values
            for each of these updated fields will be taken from the
            ``restore`` provided with this request. Field names are
            relative to the root of the resource. If no ``update_mask``
            is provided, all fields in ``restore`` will be written to
            the target Restore resource. Note that OUTPUT_ONLY and
            IMMUTABLE fields in ``restore`` are ignored and are not used
            to update the target Restore.
    """

    restore: gcg_restore.Restore = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcg_restore.Restore,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteRestoreRequest(proto.Message):
    r"""Request message for DeleteRestore.

    Attributes:
        name (str):
            Required. Full name of the Restore Format:
            ``projects/*/locations/*/restorePlans/*/restores/*``
        etag (str):
            Optional. If provided, this value must match the current
            value of the target Restore's
            [etag][google.cloud.gkebackup.v1.Restore.etag] field or the
            request is rejected.
        force (bool):
            Optional. If set to true, any VolumeRestores
            below this restore will also be deleted.
            Otherwise, the request will only succeed if the
            restore has no VolumeRestores.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=2,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class ListVolumeRestoresRequest(proto.Message):
    r"""Request message for ListVolumeRestores.

    Attributes:
        parent (str):
            Required. The Restore that contains the VolumeRestores to
            list. Format:
            ``projects/*/locations/*/restorePlans/*/restores/*``
        page_size (int):
            Optional. The target number of results to return in a single
            response. If not specified, a default value will be chosen
            by the service. Note that the response may include a partial
            list and a caller should only rely on the response's
            [next_page_token][google.cloud.gkebackup.v1.ListVolumeRestoresResponse.next_page_token]
            to determine if there are more instances left to be queried.
        page_token (str):
            Optional. The value of
            [next_page_token][google.cloud.gkebackup.v1.ListVolumeRestoresResponse.next_page_token]
            received from a previous ``ListVolumeRestores`` call.
            Provide this to retrieve the subsequent page in a multi-page
            list of results. When paginating, all other parameters
            provided to ``ListVolumeRestores`` must match the call that
            provided the page token.
        filter (str):
            Optional. Field match expression used to
            filter the results.
        order_by (str):
            Optional. Field by which to sort the results.
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


class ListVolumeRestoresResponse(proto.Message):
    r"""Response message for ListVolumeRestores.

    Attributes:
        volume_restores (MutableSequence[google.cloud.gke_backup_v1.types.VolumeRestore]):
            The list of VolumeRestores matching the given
            criteria.
        next_page_token (str):
            A token which may be sent as
            [page_token][google.cloud.gkebackup.v1.ListVolumeRestoresRequest.page_token]
            in a subsequent ``ListVolumeRestores`` call to retrieve the
            next page of results. If this field is omitted or empty,
            then there are no more results to return.
    """

    @property
    def raw_page(self):
        return self

    volume_restores: MutableSequence[volume.VolumeRestore] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=volume.VolumeRestore,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetVolumeRestoreRequest(proto.Message):
    r"""Request message for GetVolumeRestore.

    Attributes:
        name (str):
            Required. Full name of the VolumeRestore resource. Format:
            ``projects/*/locations/*/restorePlans/*/restores/*/volumeRestores/*``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetBackupIndexDownloadUrlRequest(proto.Message):
    r"""Request message for GetBackupIndexDownloadUrl.

    Attributes:
        backup (str):
            Required. Full name of Backup resource. Format:
            projects/{project}/locations/{location}/backupPlans/{backup_plan}/backups/{backup}
    """

    backup: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetBackupIndexDownloadUrlResponse(proto.Message):
    r"""Response message for GetBackupIndexDownloadUrl.

    Attributes:
        signed_url (str):
            Required. The signed URL for downloading the
            backup index.
    """

    signed_url: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
