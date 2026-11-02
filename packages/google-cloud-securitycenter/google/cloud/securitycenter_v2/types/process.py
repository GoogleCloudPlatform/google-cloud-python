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

from google.cloud.securitycenter_v2.types import file

__protobuf__ = proto.module(
    package="google.cloud.securitycenter.v2",
    manifest={
        "Process",
        "EnvironmentVariable",
    },
)


class Process(proto.Message):
    r"""Represents an operating system process.

    Attributes:
        name (str):
            The process name, as displayed in utilities like ``top`` and
            ``ps``. This name can be accessed through
            ``/proc/[pid]/comm`` and changed with
            ``prctl(PR_SET_NAME)``.
        binary (google.cloud.securitycenter_v2.types.File):
            File information for the process executable.
        libraries (MutableSequence[google.cloud.securitycenter_v2.types.File]):
            File information for libraries loaded by the
            process.
        script (google.cloud.securitycenter_v2.types.File):
            When the process represents the invocation of a script,
            ``binary`` provides information about the interpreter, while
            ``script`` provides information about the script file
            provided to the interpreter.
        args (MutableSequence[str]):
            Process arguments as JSON encoded strings.
        arguments_truncated (bool):
            True if ``args`` is incomplete.
        env_variables (MutableSequence[google.cloud.securitycenter_v2.types.EnvironmentVariable]):
            Process environment variables.
        env_variables_truncated (bool):
            True if ``env_variables`` is incomplete.
        pid (int):
            The process ID.
        parent_pid (int):
            The parent process ID.
        user_id (int):
            The ID of the user that executed the process.
            E.g. If this is the root user this will always
            be 0.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    binary: file.File = proto.Field(
        proto.MESSAGE,
        number=2,
        message=file.File,
    )
    libraries: MutableSequence[file.File] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=file.File,
    )
    script: file.File = proto.Field(
        proto.MESSAGE,
        number=4,
        message=file.File,
    )
    args: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    arguments_truncated: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    env_variables: MutableSequence["EnvironmentVariable"] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message="EnvironmentVariable",
    )
    env_variables_truncated: bool = proto.Field(
        proto.BOOL,
        number=8,
    )
    pid: int = proto.Field(
        proto.INT64,
        number=9,
    )
    parent_pid: int = proto.Field(
        proto.INT64,
        number=10,
    )
    user_id: int = proto.Field(
        proto.INT64,
        number=11,
    )


class EnvironmentVariable(proto.Message):
    r"""A name-value pair representing an environment variable used
    in an operating system process.

    Attributes:
        name (str):
            Environment variable name as a JSON encoded
            string.
        val (str):
            Environment variable value as a JSON encoded
            string.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    val: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
