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

import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.backupdr.v1beta",
    manifest={
        "BackupSelectionConfig",
        "PreRestoreConfig",
        "PostRestoreConfig",
        "VerificationConfig",
    },
)


class BackupSelectionConfig(proto.Message):
    r"""Configuration for selecting a backup.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        data_source (str):
            Required. Immutable. The fully qualified URI
            of the backupdr data source.

            This field is a member of `oneof`_ ``source``.
    """

    data_source: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="source",
    )


class PreRestoreConfig(proto.Message):
    r"""Configuration for Pre-Restore.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        cloud_run_job (str):
            Cloud Run job action to execute. Format:
            ``projects/{project}/locations/{location}/jobs/{job}``

            This field is a member of `oneof`_ ``pre_restore_action``.
        timeout (google.protobuf.duration_pb2.Duration):
            Optional. The timeout for this phase.
            If set, the timeout must be positive and less
            than or equal to 24 hours (86400s).
    """

    cloud_run_job: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="pre_restore_action",
    )
    timeout: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=1,
        message=duration_pb2.Duration,
    )


class PostRestoreConfig(proto.Message):
    r"""Configuration for Post-Restore.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        cloud_run_job (str):
            Cloud Run job action to execute. Format:
            ``projects/{project}/locations/{location}/jobs/{job}``

            This field is a member of `oneof`_ ``post_restore_action``.
        timeout (google.protobuf.duration_pb2.Duration):
            Optional. The timeout for this phase.
            If set, the timeout must be positive and less
            than or equal to 24 hours (86400s).
    """

    cloud_run_job: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="post_restore_action",
    )
    timeout: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=1,
        message=duration_pb2.Duration,
    )


class VerificationConfig(proto.Message):
    r"""Configuration for Verification.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        cloud_run_job (str):
            Cloud Run job action to execute. Format:
            ``projects/{project}/locations/{location}/jobs/{job}``

            This field is a member of `oneof`_ ``verification_action``.
        timeout (google.protobuf.duration_pb2.Duration):
            Optional. The timeout for this phase.
            If set, the timeout must be positive and less
            than or equal to 24 hours (86400s).
    """

    cloud_run_job: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="verification_action",
    )
    timeout: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=1,
        message=duration_pb2.Duration,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
