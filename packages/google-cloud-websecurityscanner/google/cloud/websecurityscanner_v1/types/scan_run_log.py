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

from google.cloud.websecurityscanner_v1.types import scan_run, scan_run_error_trace

__protobuf__ = proto.module(
    package="google.cloud.websecurityscanner.v1",
    manifest={
        "ScanRunLog",
    },
)


class ScanRunLog(proto.Message):
    r"""A ScanRunLog is an output-only proto used for Stackdriver
    customer logging. It is used for logs covering the start and end
    of scan pipelines. Other than an added summary, this is a subset
    of the ScanRun. Representation in logs is either a proto Struct,
    or converted to JSON. Next id: 9

    Attributes:
        summary (str):
            Human friendly message about the event.
        name (str):
            The resource name of the ScanRun being
            logged.
        execution_state (google.cloud.websecurityscanner_v1.types.ScanRun.ExecutionState):
            The execution state of the ScanRun.
        result_state (google.cloud.websecurityscanner_v1.types.ScanRun.ResultState):
            The result state of the ScanRun.
        urls_crawled_count (int):

        urls_tested_count (int):

        has_findings (bool):

        error_trace (google.cloud.websecurityscanner_v1.types.ScanRunErrorTrace):

    """

    summary: str = proto.Field(
        proto.STRING,
        number=1,
    )
    name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    execution_state: scan_run.ScanRun.ExecutionState = proto.Field(
        proto.ENUM,
        number=3,
        enum=scan_run.ScanRun.ExecutionState,
    )
    result_state: scan_run.ScanRun.ResultState = proto.Field(
        proto.ENUM,
        number=4,
        enum=scan_run.ScanRun.ResultState,
    )
    urls_crawled_count: int = proto.Field(
        proto.INT64,
        number=5,
    )
    urls_tested_count: int = proto.Field(
        proto.INT64,
        number=6,
    )
    has_findings: bool = proto.Field(
        proto.BOOL,
        number=7,
    )
    error_trace: scan_run_error_trace.ScanRunErrorTrace = proto.Field(
        proto.MESSAGE,
        number=8,
        message=scan_run_error_trace.ScanRunErrorTrace,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
