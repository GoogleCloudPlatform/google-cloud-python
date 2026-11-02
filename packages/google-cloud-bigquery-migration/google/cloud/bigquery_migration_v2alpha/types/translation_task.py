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
        "TranslationFileMapping",
        "TranslationTaskDetails",
        "Filter",
        "IdentifierSettings",
        "TeradataOptions",
        "BteqOptions",
        "DatasetReference",
    },
)


class TranslationFileMapping(proto.Message):
    r"""Mapping between an input and output file to be translated in
    a subtask.

    Attributes:
        input_path (str):
            The Cloud Storage path for a file to
            translation in a subtask.
        output_path (str):
            The Cloud Storage path to write back the
            corresponding input file to.
    """

    input_path: str = proto.Field(
        proto.STRING,
        number=1,
    )
    output_path: str = proto.Field(
        proto.STRING,
        number=2,
    )


class TranslationTaskDetails(proto.Message):
    r"""The translation task config to capture necessary settings for
    a translation task and subtask.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        teradata_options (google.cloud.bigquery_migration_v2alpha.types.TeradataOptions):
            The Teradata SQL specific settings for the
            translation task.

            This field is a member of `oneof`_ ``language_options``.
        bteq_options (google.cloud.bigquery_migration_v2alpha.types.BteqOptions):
            The BTEQ specific settings for the
            translation task.

            This field is a member of `oneof`_ ``language_options``.
        input_path (str):
            The Cloud Storage path for translation input
            files.
        output_path (str):
            The Cloud Storage path for translation output
            files.
        file_paths (MutableSequence[google.cloud.bigquery_migration_v2alpha.types.TranslationFileMapping]):
            Cloud Storage files to be processed for
            translation.
        schema_path (str):
            The Cloud Storage path to DDL files as table
            schema to assist semantic translation.
        file_encoding (google.cloud.bigquery_migration_v2alpha.types.TranslationTaskDetails.FileEncoding):
            The file encoding type.
        identifier_settings (google.cloud.bigquery_migration_v2alpha.types.IdentifierSettings):
            The settings for SQL identifiers.
        special_token_map (MutableMapping[str, google.cloud.bigquery_migration_v2alpha.types.TranslationTaskDetails.TokenType]):
            The map capturing special tokens to be
            replaced during translation. The key is special
            token in string. The value is the token data
            type. This is used to translate SQL query
            template which contains special token as place
            holder. The special token makes a query invalid
            to parse. This map will be applied to annotate
            those special token with types to let parser
            understand how to parse them into proper
            structure with type information.
        filter (google.cloud.bigquery_migration_v2alpha.types.Filter):
            The filter applied to translation details.
        translation_exception_table (str):
            Specifies the exact name of the bigquery
            table ("dataset.table") to be used for surfacing
            raw translation errors. If the table does not
            exist, we will create it. If it already exists
            and the schema is the same, we will re-use. If
            the table exists and the schema is different, we
            will throw an error.
    """

    class FileEncoding(proto.Enum):
        r"""The file encoding types.

        Values:
            FILE_ENCODING_UNSPECIFIED (0):
                File encoding setting is not specified.
            UTF_8 (1):
                File encoding is UTF_8.
            ISO_8859_1 (2):
                File encoding is ISO_8859_1.
            US_ASCII (3):
                File encoding is US_ASCII.
            UTF_16 (4):
                File encoding is UTF_16.
            UTF_16LE (5):
                File encoding is UTF_16LE.
            UTF_16BE (6):
                File encoding is UTF_16BE.
        """

        FILE_ENCODING_UNSPECIFIED = 0
        UTF_8 = 1
        ISO_8859_1 = 2
        US_ASCII = 3
        UTF_16 = 4
        UTF_16LE = 5
        UTF_16BE = 6

    class TokenType(proto.Enum):
        r"""The special token data type.

        Values:
            TOKEN_TYPE_UNSPECIFIED (0):
                Token type is not specified.
            STRING (1):
                Token type as string.
            INT64 (2):
                Token type as integer.
            NUMERIC (3):
                Token type as numeric.
            BOOL (4):
                Token type as boolean.
            FLOAT64 (5):
                Token type as float.
            DATE (6):
                Token type as date.
            TIMESTAMP (7):
                Token type as timestamp.
        """

        TOKEN_TYPE_UNSPECIFIED = 0
        STRING = 1
        INT64 = 2
        NUMERIC = 3
        BOOL = 4
        FLOAT64 = 5
        DATE = 6
        TIMESTAMP = 7

    teradata_options: "TeradataOptions" = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="language_options",
        message="TeradataOptions",
    )
    bteq_options: "BteqOptions" = proto.Field(
        proto.MESSAGE,
        number=11,
        oneof="language_options",
        message="BteqOptions",
    )
    input_path: str = proto.Field(
        proto.STRING,
        number=1,
    )
    output_path: str = proto.Field(
        proto.STRING,
        number=2,
    )
    file_paths: MutableSequence["TranslationFileMapping"] = proto.RepeatedField(
        proto.MESSAGE,
        number=12,
        message="TranslationFileMapping",
    )
    schema_path: str = proto.Field(
        proto.STRING,
        number=3,
    )
    file_encoding: FileEncoding = proto.Field(
        proto.ENUM,
        number=4,
        enum=FileEncoding,
    )
    identifier_settings: "IdentifierSettings" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="IdentifierSettings",
    )
    special_token_map: MutableMapping[str, TokenType] = proto.MapField(
        proto.STRING,
        proto.ENUM,
        number=6,
        enum=TokenType,
    )
    filter: "Filter" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="Filter",
    )
    translation_exception_table: str = proto.Field(
        proto.STRING,
        number=13,
    )


class Filter(proto.Message):
    r"""The filter applied to fields of translation details.

    Attributes:
        input_file_exclusion_prefixes (MutableSequence[str]):
            The list of prefixes used to exclude
            processing for input files.
    """

    input_file_exclusion_prefixes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class IdentifierSettings(proto.Message):
    r"""Settings related to SQL identifiers.

    Attributes:
        output_identifier_case (google.cloud.bigquery_migration_v2alpha.types.IdentifierSettings.IdentifierCase):
            The setting to control output queries'
            identifier case.
        identifier_rewrite_mode (google.cloud.bigquery_migration_v2alpha.types.IdentifierSettings.IdentifierRewriteMode):
            Specifies the rewrite mode for SQL
            identifiers.
    """

    class IdentifierCase(proto.Enum):
        r"""The identifier case type.

        Values:
            IDENTIFIER_CASE_UNSPECIFIED (0):
                The identifier case is not specified.
            ORIGINAL (1):
                Identifiers' cases will be kept as the
                original cases.
            UPPER (2):
                Identifiers will be in upper cases.
            LOWER (3):
                Identifiers will be in lower cases.
        """

        IDENTIFIER_CASE_UNSPECIFIED = 0
        ORIGINAL = 1
        UPPER = 2
        LOWER = 3

    class IdentifierRewriteMode(proto.Enum):
        r"""The SQL identifier rewrite mode.

        Values:
            IDENTIFIER_REWRITE_MODE_UNSPECIFIED (0):
                SQL Identifier rewrite mode is unspecified.
            NONE (1):
                SQL identifiers won't be rewrite.
            REWRITE_ALL (2):
                All SQL identifiers will be rewrite.
        """

        IDENTIFIER_REWRITE_MODE_UNSPECIFIED = 0
        NONE = 1
        REWRITE_ALL = 2

    output_identifier_case: IdentifierCase = proto.Field(
        proto.ENUM,
        number=1,
        enum=IdentifierCase,
    )
    identifier_rewrite_mode: IdentifierRewriteMode = proto.Field(
        proto.ENUM,
        number=2,
        enum=IdentifierRewriteMode,
    )


class TeradataOptions(proto.Message):
    r"""Teradata SQL specific translation task related settings."""


class BteqOptions(proto.Message):
    r"""BTEQ translation task related settings.

    Attributes:
        project_dataset (google.cloud.bigquery_migration_v2alpha.types.DatasetReference):
            Specifies the project and dataset in BigQuery
            that will be used for external table creation
            during the translation.
        default_path_uri (str):
            The Cloud Storage location to be used as the
            default path for files that are not otherwise
            specified in the file replacement map.
        file_replacement_map (MutableMapping[str, str]):
            Maps the local paths that are used in BTEQ
            scripts (the keys) to the paths in Cloud Storage
            that should be used in their stead in the
            translation (the value).
    """

    project_dataset: "DatasetReference" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="DatasetReference",
    )
    default_path_uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    file_replacement_map: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=3,
    )


class DatasetReference(proto.Message):
    r"""Reference to a BigQuery dataset.

    Attributes:
        dataset_id (str):
            A unique ID for this dataset, without the project name. The
            ID must contain only letters (a-z, A-Z), numbers (0-9), or
            underscores (\_). The maximum length is 1,024 characters.
        project_id (str):
            The ID of the project containing this
            dataset.
    """

    dataset_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
