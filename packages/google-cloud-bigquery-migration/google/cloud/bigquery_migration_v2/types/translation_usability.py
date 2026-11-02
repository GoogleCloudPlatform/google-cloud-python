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
    package="google.cloud.bigquery.migration.v2",
    manifest={
        "GcsReportLogMessage",
    },
)


class GcsReportLogMessage(proto.Message):
    r"""A record in the aggregate CSV report for a migration workflow

    Attributes:
        severity (str):
            Severity of the translation record.
        category (str):
            Category of the error/warning. Example:
            SyntaxError
        file_path (str):
            The file path in which the error occurred
        filename (str):
            The file name in which the error occurred
        source_script_line (int):
            Specifies the row from the source text where
            the error occurred (0 based, -1 for messages
            without line location). Example: 2
        source_script_column (int):
            Specifies the column from the source texts
            where the error occurred. (0 based, -1 for
            messages without column location) example: 6
        message (str):
            Detailed message of the record.
        script_context (str):
            The script context (obfuscated) in which the
            error occurred
        action (str):
            Category of the error/warning. Example:
            SyntaxError
        effect (str):
            Effect of the error/warning. Example:
            COMPATIBILITY
        object_name (str):
            Name of the affected object in the log
            message.
    """

    severity: str = proto.Field(
        proto.STRING,
        number=1,
    )
    category: str = proto.Field(
        proto.STRING,
        number=2,
    )
    file_path: str = proto.Field(
        proto.STRING,
        number=3,
    )
    filename: str = proto.Field(
        proto.STRING,
        number=4,
    )
    source_script_line: int = proto.Field(
        proto.INT32,
        number=5,
    )
    source_script_column: int = proto.Field(
        proto.INT32,
        number=6,
    )
    message: str = proto.Field(
        proto.STRING,
        number=7,
    )
    script_context: str = proto.Field(
        proto.STRING,
        number=8,
    )
    action: str = proto.Field(
        proto.STRING,
        number=9,
    )
    effect: str = proto.Field(
        proto.STRING,
        number=10,
    )
    object_name: str = proto.Field(
        proto.STRING,
        number=11,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
