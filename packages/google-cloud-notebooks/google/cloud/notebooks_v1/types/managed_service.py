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

from google.cloud.notebooks_v1.types import diagnostic_config as gcn_diagnostic_config
from google.cloud.notebooks_v1.types import event as gcn_event
from google.cloud.notebooks_v1.types import runtime as gcn_runtime

__protobuf__ = proto.module(
    package="google.cloud.notebooks.v1",
    manifest={
        "ListRuntimesRequest",
        "ListRuntimesResponse",
        "GetRuntimeRequest",
        "CreateRuntimeRequest",
        "DeleteRuntimeRequest",
        "StartRuntimeRequest",
        "StopRuntimeRequest",
        "SwitchRuntimeRequest",
        "ResetRuntimeRequest",
        "UpgradeRuntimeRequest",
        "ReportRuntimeEventRequest",
        "UpdateRuntimeRequest",
        "RefreshRuntimeTokenInternalRequest",
        "RefreshRuntimeTokenInternalResponse",
        "DiagnoseRuntimeRequest",
    },
)


class ListRuntimesRequest(proto.Message):
    r"""Request for listing Managed Notebook Runtimes.

    Attributes:
        parent (str):
            Required. Format:
            ``parent=projects/{project_id}/locations/{location}``
        page_size (int):
            Maximum return size of the list call.
        page_token (str):
            A previous returned page token that can be
            used to continue listing from the last result.
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


class ListRuntimesResponse(proto.Message):
    r"""Response for listing Managed Notebook Runtimes.

    Attributes:
        runtimes (MutableSequence[google.cloud.notebooks_v1.types.Runtime]):
            A list of returned Runtimes.
        next_page_token (str):
            Page token that can be used to continue
            listing from the last result in the next list
            call.
        unreachable (MutableSequence[str]):
            Locations that could not be reached. For example,
            ``['us-west1', 'us-central1']``. A ListRuntimesResponse will
            only contain either runtimes or unreachables,
    """

    @property
    def raw_page(self):
        return self

    runtimes: MutableSequence[gcn_runtime.Runtime] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcn_runtime.Runtime,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetRuntimeRequest(proto.Message):
    r"""Request for getting a Managed Notebook Runtime.

    Attributes:
        name (str):
            Required. Format:
            ``projects/{project_id}/locations/{location}/runtimes/{runtime_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateRuntimeRequest(proto.Message):
    r"""Request for creating a Managed Notebook Runtime.

    Attributes:
        parent (str):
            Required. Format:
            ``parent=projects/{project_id}/locations/{location}``
        runtime_id (str):
            Required. User-defined unique ID of this
            Runtime.
        runtime (google.cloud.notebooks_v1.types.Runtime):
            Required. The Runtime to be created.
        request_id (str):
            Idempotent request UUID.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    runtime_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    runtime: gcn_runtime.Runtime = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gcn_runtime.Runtime,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class DeleteRuntimeRequest(proto.Message):
    r"""Request for deleting a Managed Notebook Runtime.

    Attributes:
        name (str):
            Required. Format:
            ``projects/{project_id}/locations/{location}/runtimes/{runtime_id}``
        request_id (str):
            Idempotent request UUID.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class StartRuntimeRequest(proto.Message):
    r"""Request for starting a Managed Notebook Runtime.

    Attributes:
        name (str):
            Required. Format:
            ``projects/{project_id}/locations/{location}/runtimes/{runtime_id}``
        request_id (str):
            Idempotent request UUID.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class StopRuntimeRequest(proto.Message):
    r"""Request for stopping a Managed Notebook Runtime.

    Attributes:
        name (str):
            Required. Format:
            ``projects/{project_id}/locations/{location}/runtimes/{runtime_id}``
        request_id (str):
            Idempotent request UUID.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class SwitchRuntimeRequest(proto.Message):
    r"""Request for switching a Managed Notebook Runtime.

    Attributes:
        name (str):
            Required. Format:
            ``projects/{project_id}/locations/{location}/runtimes/{runtime_id}``
        machine_type (str):
            machine type.
        accelerator_config (google.cloud.notebooks_v1.types.RuntimeAcceleratorConfig):
            accelerator config.
        request_id (str):
            Idempotent request UUID.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    machine_type: str = proto.Field(
        proto.STRING,
        number=2,
    )
    accelerator_config: gcn_runtime.RuntimeAcceleratorConfig = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gcn_runtime.RuntimeAcceleratorConfig,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ResetRuntimeRequest(proto.Message):
    r"""Request for resetting a Managed Notebook Runtime.

    Attributes:
        name (str):
            Required. Format:
            ``projects/{project_id}/locations/{location}/runtimes/{runtime_id}``
        request_id (str):
            Idempotent request UUID.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UpgradeRuntimeRequest(proto.Message):
    r"""Request for upgrading a Managed Notebook Runtime to the latest
    version. option (google.api.message_visibility).restriction =
    "TRUSTED_TESTER,SPECIAL_TESTER";

    Attributes:
        name (str):
            Required. Format:
            ``projects/{project_id}/locations/{location}/runtimes/{runtime_id}``
        request_id (str):
            Idempotent request UUID.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ReportRuntimeEventRequest(proto.Message):
    r"""Request for reporting a Managed Notebook Event.

    Attributes:
        name (str):
            Required. Format:
            ``projects/{project_id}/locations/{location}/runtimes/{runtime_id}``
        vm_id (str):
            Required. The VM hardware token for
            authenticating the VM.
            https://cloud.google.com/compute/docs/instances/verifying-instance-identity
        event (google.cloud.notebooks_v1.types.Event):
            Required. The Event to be reported.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    vm_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    event: gcn_event.Event = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gcn_event.Event,
    )


class UpdateRuntimeRequest(proto.Message):
    r"""Request for updating a Managed Notebook configuration.

    Attributes:
        runtime (google.cloud.notebooks_v1.types.Runtime):
            Required. The Runtime to be updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Specifies the path, relative to ``Runtime``, of
            the field to update. For example, to change the software
            configuration kernels, the ``update_mask`` parameter would
            be specified as ``software_config.kernels``, and the
            ``PATCH`` request body would specify the new value, as
            follows:

            ::

                {
                  "software_config":{
                    "kernels": [{
                       'repository':
                       'gcr.io/deeplearning-platform-release/pytorch-gpu', 'tag':
                       'latest' }],
                    }
                }

            Currently, only the following fields can be updated:

            - ``software_config.kernels``
            - ``software_config.post_startup_script``
            - ``software_config.custom_gpu_driver_path``
            - ``software_config.idle_shutdown``
            - ``software_config.idle_shutdown_timeout``
            - ``software_config.disable_terminal``
        request_id (str):
            Idempotent request UUID.
    """

    runtime: gcn_runtime.Runtime = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcn_runtime.Runtime,
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


class RefreshRuntimeTokenInternalRequest(proto.Message):
    r"""Request for getting a new access token.

    Attributes:
        name (str):
            Required. Format:
            ``projects/{project_id}/locations/{location}/runtimes/{runtime_id}``
        vm_id (str):
            Required. The VM hardware token for
            authenticating the VM.
            https://cloud.google.com/compute/docs/instances/verifying-instance-identity
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    vm_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class RefreshRuntimeTokenInternalResponse(proto.Message):
    r"""Response with a new access token.

    Attributes:
        access_token (str):
            The OAuth 2.0 access token.
        expire_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Token expiration time.
    """

    access_token: str = proto.Field(
        proto.STRING,
        number=1,
    )
    expire_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )


class DiagnoseRuntimeRequest(proto.Message):
    r"""Request for creating a notebook instance diagnostic file.

    Attributes:
        name (str):
            Required. Format:
            ``projects/{project_id}/locations/{location}/runtimes/{runtimes_id}``
        diagnostic_config (google.cloud.notebooks_v1.types.DiagnosticConfig):
            Required. Defines flags that are used to run
            the diagnostic tool
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


__all__ = tuple(sorted(__protobuf__.manifest))
