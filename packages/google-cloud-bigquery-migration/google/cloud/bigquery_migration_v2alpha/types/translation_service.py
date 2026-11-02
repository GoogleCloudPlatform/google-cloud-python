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
    package="google.cloud.bigquery.migration.v2alpha",
    manifest={
        "TranslateQueryRequest",
        "TranslateQueryResponse",
        "SqlTranslationErrorDetail",
        "SqlTranslationError",
        "SqlTranslationWarning",
    },
)


class TranslateQueryRequest(proto.Message):
    r"""The request of translating a SQL query to Standard SQL.

    Attributes:
        parent (str):
            Required. The name of the project to which this translation
            request belongs. Example: ``projects/foo/locations/bar``
        source_dialect (google.cloud.bigquery_migration_v2alpha.types.TranslateQueryRequest.SqlTranslationSourceDialect):
            Required. The source SQL dialect of ``queries``.
        query (str):
            Required. The query to be translated.
    """

    class SqlTranslationSourceDialect(proto.Enum):
        r"""Supported SQL translation source dialects.

        Values:
            SQL_TRANSLATION_SOURCE_DIALECT_UNSPECIFIED (0):
                SqlTranslationSourceDialect not specified.
            TERADATA (1):
                Teradata SQL.
        """

        SQL_TRANSLATION_SOURCE_DIALECT_UNSPECIFIED = 0
        TERADATA = 1

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    source_dialect: SqlTranslationSourceDialect = proto.Field(
        proto.ENUM,
        number=2,
        enum=SqlTranslationSourceDialect,
    )
    query: str = proto.Field(
        proto.STRING,
        number=3,
    )


class TranslateQueryResponse(proto.Message):
    r"""The response of translating a SQL query to Standard SQL.

    Attributes:
        translation_job (str):
            Output only. Immutable. The unique identifier for the SQL
            translation job. Example:
            ``projects/123/locations/us/translation/1234``
        translated_query (str):
            The translated result. This will be empty if
            the translation fails.
        errors (MutableSequence[google.cloud.bigquery_migration_v2alpha.types.SqlTranslationError]):
            The list of errors encountered during the
            translation, if present.
        warnings (MutableSequence[google.cloud.bigquery_migration_v2alpha.types.SqlTranslationWarning]):
            The list of warnings encountered during the
            translation, if present, indicates
            non-semantically correct translation.
    """

    translation_job: str = proto.Field(
        proto.STRING,
        number=4,
    )
    translated_query: str = proto.Field(
        proto.STRING,
        number=1,
    )
    errors: MutableSequence["SqlTranslationError"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="SqlTranslationError",
    )
    warnings: MutableSequence["SqlTranslationWarning"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="SqlTranslationWarning",
    )


class SqlTranslationErrorDetail(proto.Message):
    r"""Structured error object capturing the error message and the
    location in the source text where the error occurs.

    Attributes:
        row (int):
            Specifies the row from the source text where
            the error occurred.
        column (int):
            Specifie the column from the source texts
            where the error occurred.
        message (str):
            A human-readable description of the error.
    """

    row: int = proto.Field(
        proto.INT64,
        number=1,
    )
    column: int = proto.Field(
        proto.INT64,
        number=2,
    )
    message: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SqlTranslationError(proto.Message):
    r"""The detailed error object if the SQL translation job fails.

    Attributes:
        error_type (google.cloud.bigquery_migration_v2alpha.types.SqlTranslationError.SqlTranslationErrorType):
            The type of SQL translation error.
        error_detail (google.cloud.bigquery_migration_v2alpha.types.SqlTranslationErrorDetail):
            Specifies the details of the error, including
            the error message and location from the source
            text.
    """

    class SqlTranslationErrorType(proto.Enum):
        r"""The error type of the SQL translation job.

        Values:
            SQL_TRANSLATION_ERROR_TYPE_UNSPECIFIED (0):
                SqlTranslationErrorType not specified.
            SQL_PARSE_ERROR (1):
                Failed to parse the input text as a SQL
                query.
            UNSUPPORTED_SQL_FUNCTION (2):
                Found unsupported functions in the input SQL
                query that are not able to translate.
        """

        SQL_TRANSLATION_ERROR_TYPE_UNSPECIFIED = 0
        SQL_PARSE_ERROR = 1
        UNSUPPORTED_SQL_FUNCTION = 2

    error_type: SqlTranslationErrorType = proto.Field(
        proto.ENUM,
        number=1,
        enum=SqlTranslationErrorType,
    )
    error_detail: "SqlTranslationErrorDetail" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="SqlTranslationErrorDetail",
    )


class SqlTranslationWarning(proto.Message):
    r"""The detailed warning object if the SQL translation job is
    completed but not semantically correct.

    Attributes:
        warning_detail (google.cloud.bigquery_migration_v2alpha.types.SqlTranslationErrorDetail):
            Specifies the details of the warning,
            including the warning message and location from
            the source text.
    """

    warning_detail: "SqlTranslationErrorDetail" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="SqlTranslationErrorDetail",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
