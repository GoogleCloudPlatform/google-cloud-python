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
        "TranslationReportRecord",
    },
)


class TranslationReportRecord(proto.Message):
    r"""Details about a record.

    Attributes:
        severity (google.cloud.bigquery_migration_v2.types.TranslationReportRecord.Severity):
            Severity of the translation record.
        script_line (int):
            Specifies the row from the source text where
            the error occurred (0 based). Example: 2
        script_column (int):
            Specifies the column from the source texts
            where the error occurred. (0 based) example: 6
        category (str):
            Category of the error/warning. Example:
            SyntaxError
        message (str):
            Detailed message of the record.
    """

    class Severity(proto.Enum):
        r"""The severity type of the record.

        Values:
            SEVERITY_UNSPECIFIED (0):
                SeverityType not specified.
            INFO (1):
                INFO type.
            WARNING (2):
                WARNING type. The translated query may still
                provide useful information if all the report
                records are WARNING.
            ERROR (3):
                ERROR type. Translation failed.
        """

        SEVERITY_UNSPECIFIED = 0
        INFO = 1
        WARNING = 2
        ERROR = 3

    severity: Severity = proto.Field(
        proto.ENUM,
        number=1,
        enum=Severity,
    )
    script_line: int = proto.Field(
        proto.INT32,
        number=2,
    )
    script_column: int = proto.Field(
        proto.INT32,
        number=3,
    )
    category: str = proto.Field(
        proto.STRING,
        number=4,
    )
    message: str = proto.Field(
        proto.STRING,
        number=5,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
