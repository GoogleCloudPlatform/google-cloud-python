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
    package="google.cloud.securitycenter.v1",
    manifest={
        "KernelRootkit",
    },
)


class KernelRootkit(proto.Message):
    r"""Kernel mode rootkit signatures.

    Attributes:
        name (str):
            Rootkit name, when available.
        unexpected_code_modification (bool):
            True if unexpected modifications of kernel
            code memory are present.
        unexpected_read_only_data_modification (bool):
            True if unexpected modifications of kernel
            read-only data memory are present.
        unexpected_ftrace_handler (bool):
            True if ``ftrace`` points are present with callbacks
            pointing to regions that are not in the expected kernel or
            module code range.
        unexpected_kprobe_handler (bool):
            True if ``kprobe`` points are present with callbacks
            pointing to regions that are not in the expected kernel or
            module code range.
        unexpected_kernel_code_pages (bool):
            True if kernel code pages that are not in the
            expected kernel or module code regions are
            present.
        unexpected_system_call_handler (bool):
            True if system call handlers that are are not
            in the expected kernel or module code regions
            are present.
        unexpected_interrupt_handler (bool):
            True if interrupt handlers that are are not
            in the expected kernel or module code regions
            are present.
        unexpected_processes_in_runqueue (bool):
            True if unexpected processes in the scheduler
            run queue are present. Such processes are in the
            run queue, but not in the process task list.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    unexpected_code_modification: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    unexpected_read_only_data_modification: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    unexpected_ftrace_handler: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    unexpected_kprobe_handler: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    unexpected_kernel_code_pages: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    unexpected_system_call_handler: bool = proto.Field(
        proto.BOOL,
        number=7,
    )
    unexpected_interrupt_handler: bool = proto.Field(
        proto.BOOL,
        number=8,
    )
    unexpected_processes_in_runqueue: bool = proto.Field(
        proto.BOOL,
        number=9,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
