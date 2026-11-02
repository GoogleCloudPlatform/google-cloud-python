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

from google.cloud.notebooks_v2.types import diagnostic_config as gcn_diagnostic_config
from google.cloud.notebooks_v2.types import instance as gcn_instance

__protobuf__ = proto.module(
    package="google.cloud.notebooks.v2",
    manifest={
        "OperationMetadata",
        "ListInstancesRequest",
        "ListInstancesResponse",
        "GetInstanceRequest",
        "CreateInstanceRequest",
        "UpdateInstanceRequest",
        "DeleteInstanceRequest",
        "StartInstanceRequest",
        "StopInstanceRequest",
        "ResetInstanceRequest",
        "CheckInstanceUpgradabilityRequest",
        "CheckInstanceUpgradabilityResponse",
        "UpgradeInstanceRequest",
        "RollbackInstanceRequest",
        "DiagnoseInstanceRequest",
    },
)


class OperationMetadata(proto.Message):
    r"""Represents the metadata of the long-running operation.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            The time the operation was created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            The time the operation finished running.
        target (str):
            Server-defined resource path for the target
            of the operation.
        verb (str):
            Name of the verb executed by the operation.
        status_message (str):
            Human-readable status of the operation, if
            any.
        requested_cancellation (bool):
            Identifies whether the user has requested cancellation of
            the operation. Operations that have successfully been
            cancelled have [Operation.error][] value with a
            [google.rpc.Status.code][google.rpc.Status.code] of 1,
            corresponding to ``Code.CANCELLED``.
        api_version (str):
            API version used to start the operation.
        endpoint (str):
            API endpoint name of this operation.
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
    endpoint: str = proto.Field(
        proto.STRING,
        number=8,
    )


class ListInstancesRequest(proto.Message):
    r"""Request for listing notebook instances.

    Attributes:
        parent (str):
            Required. Format:
            ``parent=projects/{project_id}/locations/{location}``
        page_size (int):
            Optional. Maximum return size of the list
            call.
        page_token (str):
            Optional. A previous returned page token that
            can be used to continue listing from the last
            result.
        order_by (str):
            Optional. Sort results. Supported values are
            "name", "name desc" or "" (unsorted).
        filter (str):
            Optional. List filter.
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


class ListInstancesResponse(proto.Message):
    r"""Response for listing notebook instances.

    Attributes:
        instances (MutableSequence[google.cloud.notebooks_v2.types.Instance]):
            A list of returned instances.
        next_page_token (str):
            Page token that can be used to continue
            listing from the last result in the next list
            call.
        unreachable (MutableSequence[str]):
            Locations that could not be reached. For example,
            ['us-west1-a', 'us-central1-b']. A ListInstancesResponse
            will only contain either instances or unreachables,
    """

    @property
    def raw_page(self):
        return self

    instances: MutableSequence[gcn_instance.Instance] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcn_instance.Instance,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetInstanceRequest(proto.Message):
    r"""Request for getting a notebook instance.

    Attributes:
        name (str):
            Required. Format:
            ``projects/{project_id}/locations/{location}/instances/{instance_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateInstanceRequest(proto.Message):
    r"""Request for creating a notebook instance.

    Attributes:
        parent (str):
            Required. Format:
            ``parent=projects/{project_id}/locations/{location}``
        instance_id (str):
            Required. User-defined unique ID of this
            instance.
        instance (google.cloud.notebooks_v2.types.Instance):
            Required. The instance to be created.
        request_id (str):
            Optional. Idempotent request UUID.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    instance_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    instance: gcn_instance.Instance = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gcn_instance.Instance,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateInstanceRequest(proto.Message):
    r"""Request for updating a notebook instance.

    Attributes:
        instance (google.cloud.notebooks_v2.types.Instance):
            Required. A representation of an instance.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Mask used to update an instance
        request_id (str):
            Optional. Idempotent request UUID.
    """

    instance: gcn_instance.Instance = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcn_instance.Instance,
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


class DeleteInstanceRequest(proto.Message):
    r"""Request for deleting a notebook instance.

    Attributes:
        name (str):
            Required. Format:
            ``projects/{project_id}/locations/{location}/instances/{instance_id}``
        request_id (str):
            Optional. Idempotent request UUID.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class StartInstanceRequest(proto.Message):
    r"""Request for starting a notebook instance

    Attributes:
        name (str):
            Required. Format:
            ``projects/{project_id}/locations/{location}/instances/{instance_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class StopInstanceRequest(proto.Message):
    r"""Request for stopping a notebook instance

    Attributes:
        name (str):
            Required. Format:
            ``projects/{project_id}/locations/{location}/instances/{instance_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ResetInstanceRequest(proto.Message):
    r"""Request for resetting a notebook instance

    Attributes:
        name (str):
            Required. Format:
            ``projects/{project_id}/locations/{location}/instances/{instance_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CheckInstanceUpgradabilityRequest(proto.Message):
    r"""Request for checking if a notebook instance is upgradeable.

    Attributes:
        notebook_instance (str):
            Required. Format:
            ``projects/{project_id}/locations/{location}/instances/{instance_id}``
    """

    notebook_instance: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CheckInstanceUpgradabilityResponse(proto.Message):
    r"""Response for checking if a notebook instance is upgradeable.

    Attributes:
        upgradeable (bool):
            If an instance is upgradeable.
        upgrade_version (str):
            The version this instance will be upgraded to
            if calling the upgrade endpoint. This field will
            only be populated if field upgradeable is true.
        upgrade_info (str):
            Additional information about upgrade.
        upgrade_image (str):
            The new image self link this instance will be
            upgraded to if calling the upgrade endpoint.
            This field will only be populated if field
            upgradeable is true.
    """

    upgradeable: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    upgrade_version: str = proto.Field(
        proto.STRING,
        number=2,
    )
    upgrade_info: str = proto.Field(
        proto.STRING,
        number=3,
    )
    upgrade_image: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpgradeInstanceRequest(proto.Message):
    r"""Request for upgrading a notebook instance

    Attributes:
        name (str):
            Required. Format:
            ``projects/{project_id}/locations/{location}/instances/{instance_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class RollbackInstanceRequest(proto.Message):
    r"""Request for rollbacking a notebook instance

    Attributes:
        name (str):
            Required. Format:
            ``projects/{project_id}/locations/{location}/instances/{instance_id}``
        target_snapshot (str):
            Required. The snapshot for rollback.
            Example:
            "projects/test-project/global/snapshots/krwlzipynril".
        revision_id (str):
            Required. Output only. Revision Id
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    target_snapshot: str = proto.Field(
        proto.STRING,
        number=2,
    )
    revision_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DiagnoseInstanceRequest(proto.Message):
    r"""Request for creating a notebook instance diagnostic file.

    Attributes:
        name (str):
            Required. Format:
            ``projects/{project_id}/locations/{location}/instances/{instance_id}``
        diagnostic_config (google.cloud.notebooks_v2.types.DiagnosticConfig):
            Required. Defines flags that are used to run
            the diagnostic tool
        timeout_minutes (int):
            Optional. Maxmium amount of time in minutes
            before the operation times out.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    diagnostic_config: gcn_diagnostic_config.DiagnosticConfig = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcn_diagnostic_config.DiagnosticConfig,
    )
    timeout_minutes: int = proto.Field(
        proto.INT32,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
