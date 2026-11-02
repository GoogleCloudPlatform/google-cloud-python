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
    package="google.cloud.notebooks.v2",
    manifest={
        "DiagnosticConfig",
    },
)


class DiagnosticConfig(proto.Message):
    r"""Defines flags that are used to run the diagnostic tool

    Attributes:
        gcs_bucket (str):
            Required. User Cloud Storage bucket location (REQUIRED).
            Must be formatted with path prefix (``gs://$GCS_BUCKET``).

            Permissions: User Managed Notebooks:

            - storage.buckets.writer: Must be given to the project's
              service account attached to VM. Google Managed Notebooks:
            - storage.buckets.writer: Must be given to the project's
              service account or user credentials attached to VM
              depending on authentication mode.

            Cloud Storage bucket Log file will be written to
            ``gs://$GCS_BUCKET/$RELATIVE_PATH/$VM_DATE_$TIME.tar.gz``
        relative_path (str):
            Optional. Defines the relative storage path in the Cloud
            Storage bucket where the diagnostic logs will be written:
            Default path will be the root directory of the Cloud Storage
            bucket (``gs://$GCS_BUCKET/$DATE_$TIME.tar.gz``) Example of
            full path where Log file will be written:
            ``gs://$GCS_BUCKET/$RELATIVE_PATH/``
        enable_repair_flag (bool):
            Optional. Enables flag to repair service for
            instance
        enable_packet_capture_flag (bool):
            Optional. Enables flag to capture packets
            from the instance for 30 seconds
        enable_copy_home_files_flag (bool):
            Optional. Enables flag to copy all ``/home/jupyter`` folder
            contents
    """

    gcs_bucket: str = proto.Field(
        proto.STRING,
        number=1,
    )
    relative_path: str = proto.Field(
        proto.STRING,
        number=2,
    )
    enable_repair_flag: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    enable_packet_capture_flag: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    enable_copy_home_files_flag: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
