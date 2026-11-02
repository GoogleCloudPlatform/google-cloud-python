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

import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.clouddms_v1.types import clouddms_resources

__protobuf__ = proto.module(
    package="google.cloud.clouddms.v1",
    manifest={
        "ValuePresentInList",
        "DatabaseEntityType",
        "EntityNameTransformation",
        "BackgroundJobType",
        "ImportRulesFileFormat",
        "ValueComparison",
        "NumericFilterOption",
        "DatabaseEngineInfo",
        "ConversionWorkspace",
        "BackgroundJobLogEntry",
        "MappingRuleFilter",
        "MappingRule",
        "SingleEntityRename",
        "MultiEntityRename",
        "EntityMove",
        "SingleColumnChange",
        "MultiColumnDatatypeChange",
        "SourceTextFilter",
        "SourceNumericFilter",
        "ConditionalColumnSetValue",
        "ValueTransformation",
        "ConvertRowIdToColumn",
        "SetTablePrimaryKey",
        "SinglePackageChange",
        "SourceSqlChange",
        "FilterTableColumns",
        "ValueListFilter",
        "IntComparisonFilter",
        "DoubleComparisonFilter",
        "AssignSpecificValue",
        "ApplyHash",
        "RoundToScale",
        "DatabaseEntity",
        "DatabaseInstanceEntity",
        "SchemaEntity",
        "TableEntity",
        "ColumnEntity",
        "ConstraintEntity",
        "IndexEntity",
        "TriggerEntity",
        "ViewEntity",
        "SequenceEntity",
        "StoredProcedureEntity",
        "FunctionEntity",
        "MaterializedViewEntity",
        "SynonymEntity",
        "PackageEntity",
        "UDTEntity",
        "EntityMapping",
        "EntityMappingLogEntry",
        "EntityDdl",
        "EntityIssue",
    },
)


class ValuePresentInList(proto.Enum):
    r"""Enum used by ValueListFilter to indicate whether the source
    value is in the supplied list

    Values:
        VALUE_PRESENT_IN_LIST_UNSPECIFIED (0):
            Value present in list unspecified
        VALUE_PRESENT_IN_LIST_IF_VALUE_LIST (1):
            If the source value is in the supplied list at value_list
        VALUE_PRESENT_IN_LIST_IF_VALUE_NOT_LIST (2):
            If the source value is not in the supplied list at
            value_list
    """

    VALUE_PRESENT_IN_LIST_UNSPECIFIED = 0
    VALUE_PRESENT_IN_LIST_IF_VALUE_LIST = 1
    VALUE_PRESENT_IN_LIST_IF_VALUE_NOT_LIST = 2


class DatabaseEntityType(proto.Enum):
    r"""The type of database entities supported,

    Values:
        DATABASE_ENTITY_TYPE_UNSPECIFIED (0):
            Unspecified database entity type.
        DATABASE_ENTITY_TYPE_SCHEMA (1):
            Schema.
        DATABASE_ENTITY_TYPE_TABLE (2):
            Table.
        DATABASE_ENTITY_TYPE_COLUMN (3):
            Column.
        DATABASE_ENTITY_TYPE_CONSTRAINT (4):
            Constraint.
        DATABASE_ENTITY_TYPE_INDEX (5):
            Index.
        DATABASE_ENTITY_TYPE_TRIGGER (6):
            Trigger.
        DATABASE_ENTITY_TYPE_VIEW (7):
            View.
        DATABASE_ENTITY_TYPE_SEQUENCE (8):
            Sequence.
        DATABASE_ENTITY_TYPE_STORED_PROCEDURE (9):
            Stored Procedure.
        DATABASE_ENTITY_TYPE_FUNCTION (10):
            Function.
        DATABASE_ENTITY_TYPE_SYNONYM (11):
            Synonym.
        DATABASE_ENTITY_TYPE_DATABASE_PACKAGE (12):
            Package.
        DATABASE_ENTITY_TYPE_UDT (13):
            UDT.
        DATABASE_ENTITY_TYPE_MATERIALIZED_VIEW (14):
            Materialized View.
        DATABASE_ENTITY_TYPE_DATABASE (15):
            Database.
    """

    DATABASE_ENTITY_TYPE_UNSPECIFIED = 0
    DATABASE_ENTITY_TYPE_SCHEMA = 1
    DATABASE_ENTITY_TYPE_TABLE = 2
    DATABASE_ENTITY_TYPE_COLUMN = 3
    DATABASE_ENTITY_TYPE_CONSTRAINT = 4
    DATABASE_ENTITY_TYPE_INDEX = 5
    DATABASE_ENTITY_TYPE_TRIGGER = 6
    DATABASE_ENTITY_TYPE_VIEW = 7
    DATABASE_ENTITY_TYPE_SEQUENCE = 8
    DATABASE_ENTITY_TYPE_STORED_PROCEDURE = 9
    DATABASE_ENTITY_TYPE_FUNCTION = 10
    DATABASE_ENTITY_TYPE_SYNONYM = 11
    DATABASE_ENTITY_TYPE_DATABASE_PACKAGE = 12
    DATABASE_ENTITY_TYPE_UDT = 13
    DATABASE_ENTITY_TYPE_MATERIALIZED_VIEW = 14
    DATABASE_ENTITY_TYPE_DATABASE = 15


class EntityNameTransformation(proto.Enum):
    r"""Entity Name Transformation Types

    Values:
        ENTITY_NAME_TRANSFORMATION_UNSPECIFIED (0):
            Entity name transformation unspecified.
        ENTITY_NAME_TRANSFORMATION_NO_TRANSFORMATION (1):
            No transformation.
        ENTITY_NAME_TRANSFORMATION_LOWER_CASE (2):
            Transform to lower case.
        ENTITY_NAME_TRANSFORMATION_UPPER_CASE (3):
            Transform to upper case.
        ENTITY_NAME_TRANSFORMATION_CAPITALIZED_CASE (4):
            Transform to capitalized case.
    """

    ENTITY_NAME_TRANSFORMATION_UNSPECIFIED = 0
    ENTITY_NAME_TRANSFORMATION_NO_TRANSFORMATION = 1
    ENTITY_NAME_TRANSFORMATION_LOWER_CASE = 2
    ENTITY_NAME_TRANSFORMATION_UPPER_CASE = 3
    ENTITY_NAME_TRANSFORMATION_CAPITALIZED_CASE = 4


class BackgroundJobType(proto.Enum):
    r"""The types of jobs that can be executed in the background.

    Values:
        BACKGROUND_JOB_TYPE_UNSPECIFIED (0):
            Unspecified background job type.
        BACKGROUND_JOB_TYPE_SOURCE_SEED (1):
            Job to seed from the source database.
        BACKGROUND_JOB_TYPE_CONVERT (2):
            Job to convert the source database into a
            draft of the destination database.
        BACKGROUND_JOB_TYPE_APPLY_DESTINATION (3):
            Job to apply the draft tree onto the
            destination.
        BACKGROUND_JOB_TYPE_IMPORT_RULES_FILE (5):
            Job to import and convert mapping rules from
            an external source such as an ora2pg config
            file.
    """

    BACKGROUND_JOB_TYPE_UNSPECIFIED = 0
    BACKGROUND_JOB_TYPE_SOURCE_SEED = 1
    BACKGROUND_JOB_TYPE_CONVERT = 2
    BACKGROUND_JOB_TYPE_APPLY_DESTINATION = 3
    BACKGROUND_JOB_TYPE_IMPORT_RULES_FILE = 5


class ImportRulesFileFormat(proto.Enum):
    r"""The format for the import rules file.

    Values:
        IMPORT_RULES_FILE_FORMAT_UNSPECIFIED (0):
            Unspecified rules format.
        IMPORT_RULES_FILE_FORMAT_HARBOUR_BRIDGE_SESSION_FILE (1):
            HarbourBridge session file.
        IMPORT_RULES_FILE_FORMAT_ORATOPG_CONFIG_FILE (2):
            Ora2Pg configuration file.
    """

    IMPORT_RULES_FILE_FORMAT_UNSPECIFIED = 0
    IMPORT_RULES_FILE_FORMAT_HARBOUR_BRIDGE_SESSION_FILE = 1
    IMPORT_RULES_FILE_FORMAT_ORATOPG_CONFIG_FILE = 2


class ValueComparison(proto.Enum):
    r"""Enum used by IntComparisonFilter and DoubleComparisonFilter
    to indicate the relation between source value and compare value.

    Values:
        VALUE_COMPARISON_UNSPECIFIED (0):
            Value comparison unspecified.
        VALUE_COMPARISON_IF_VALUE_SMALLER_THAN (1):
            Value is smaller than the Compare value.
        VALUE_COMPARISON_IF_VALUE_SMALLER_EQUAL_THAN (2):
            Value is smaller or equal than the Compare
            value.
        VALUE_COMPARISON_IF_VALUE_LARGER_THAN (3):
            Value is larger than the Compare value.
        VALUE_COMPARISON_IF_VALUE_LARGER_EQUAL_THAN (4):
            Value is larger or equal than the Compare
            value.
    """

    VALUE_COMPARISON_UNSPECIFIED = 0
    VALUE_COMPARISON_IF_VALUE_SMALLER_THAN = 1
    VALUE_COMPARISON_IF_VALUE_SMALLER_EQUAL_THAN = 2
    VALUE_COMPARISON_IF_VALUE_LARGER_THAN = 3
    VALUE_COMPARISON_IF_VALUE_LARGER_EQUAL_THAN = 4


class NumericFilterOption(proto.Enum):
    r"""Specifies the columns on which numeric filter needs to be
    applied.

    Values:
        NUMERIC_FILTER_OPTION_UNSPECIFIED (0):
            Numeric filter option unspecified
        NUMERIC_FILTER_OPTION_ALL (1):
            Numeric filter option that matches all
            numeric columns.
        NUMERIC_FILTER_OPTION_LIMIT (2):
            Numeric filter option that matches columns
            having numeric datatypes with specified
            precision and scale within the limited range of
            filter.
        NUMERIC_FILTER_OPTION_LIMITLESS (3):
            Numeric filter option that matches only the
            numeric columns with no precision and scale
            specified.
    """

    NUMERIC_FILTER_OPTION_UNSPECIFIED = 0
    NUMERIC_FILTER_OPTION_ALL = 1
    NUMERIC_FILTER_OPTION_LIMIT = 2
    NUMERIC_FILTER_OPTION_LIMITLESS = 3


class DatabaseEngineInfo(proto.Message):
    r"""The type and version of a source or destination database.

    Attributes:
        engine (google.cloud.clouddms_v1.types.DatabaseEngine):
            Required. Engine type.
        version (str):
            Required. Engine named version, for example
            12.c.1.
    """

    engine: clouddms_resources.DatabaseEngine = proto.Field(
        proto.ENUM,
        number=1,
        enum=clouddms_resources.DatabaseEngine,
    )
    version: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ConversionWorkspace(proto.Message):
    r"""The main conversion workspace resource entity.

    Attributes:
        name (str):
            Full name of the workspace resource, in the form of:
            projects/{project}/locations/{location}/conversionWorkspaces/{conversion_workspace}.
        source (google.cloud.clouddms_v1.types.DatabaseEngineInfo):
            Required. The source engine details.
        destination (google.cloud.clouddms_v1.types.DatabaseEngineInfo):
            Required. The destination engine details.
        global_settings (MutableMapping[str, str]):
            Optional. A generic list of settings for the workspace. The
            settings are database pair dependant and can indicate
            default behavior for the mapping rules engine or turn on or
            off specific features. Such examples can be:
            convert_foreign_key_to_interleave=true, skip_triggers=false,
            ignore_non_table_synonyms=true
        has_uncommitted_changes (bool):
            Output only. Whether the workspace has
            uncommitted changes (changes which were made
            after the workspace was committed).
        latest_commit_id (str):
            Output only. The latest commit ID.
        latest_commit_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the workspace
            was committed.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the workspace
            resource was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the workspace
            resource was last updated.
        display_name (str):
            Optional. The display name for the workspace.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    source: "DatabaseEngineInfo" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="DatabaseEngineInfo",
    )
    destination: "DatabaseEngineInfo" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="DatabaseEngineInfo",
    )
    global_settings: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    has_uncommitted_changes: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    latest_commit_id: str = proto.Field(
        proto.STRING,
        number=6,
    )
    latest_commit_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=11,
    )


class BackgroundJobLogEntry(proto.Message):
    r"""Execution log of a background job.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        id (str):
            The background job log entry ID.
        job_type (google.cloud.clouddms_v1.types.BackgroundJobType):
            The type of job that was executed.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            The timestamp when the background job was
            started.
        finish_time (google.protobuf.timestamp_pb2.Timestamp):
            The timestamp when the background job was
            finished.
        completion_state (google.cloud.clouddms_v1.types.BackgroundJobLogEntry.JobCompletionState):
            Output only. Job completion state, i.e. the
            final state after the job completed.
        completion_comment (str):
            Output only. Job completion comment, such as
            how many entities were seeded, how many warnings
            were found during conversion, and similar
            information.
        request_autocommit (bool):
            Output only. Whether the client requested the
            conversion workspace to be committed after a
            successful completion of the job.
        seed_job_details (google.cloud.clouddms_v1.types.BackgroundJobLogEntry.SeedJobDetails):
            Output only. Seed job details.

            This field is a member of `oneof`_ ``job_details``.
        import_rules_job_details (google.cloud.clouddms_v1.types.BackgroundJobLogEntry.ImportRulesJobDetails):
            Output only. Import rules job details.

            This field is a member of `oneof`_ ``job_details``.
        convert_job_details (google.cloud.clouddms_v1.types.BackgroundJobLogEntry.ConvertJobDetails):
            Output only. Convert job details.

            This field is a member of `oneof`_ ``job_details``.
        apply_job_details (google.cloud.clouddms_v1.types.BackgroundJobLogEntry.ApplyJobDetails):
            Output only. Apply job details.

            This field is a member of `oneof`_ ``job_details``.
    """

    class JobCompletionState(proto.Enum):
        r"""Final state after a job completes.

        Values:
            JOB_COMPLETION_STATE_UNSPECIFIED (0):
                The status is not specified. This state is
                used when job is not yet finished.
            SUCCEEDED (1):
                Success.
            FAILED (2):
                Error.
        """

        JOB_COMPLETION_STATE_UNSPECIFIED = 0
        SUCCEEDED = 1
        FAILED = 2

    class SeedJobDetails(proto.Message):
        r"""Details regarding a Seed background job.

        Attributes:
            connection_profile (str):
                Output only. The connection profile which was
                used for the seed job.
        """

        connection_profile: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class ImportRulesJobDetails(proto.Message):
        r"""Details regarding an Import Rules background job.

        Attributes:
            files (MutableSequence[str]):
                Output only. File names used for the import
                rules job.
            file_format (google.cloud.clouddms_v1.types.ImportRulesFileFormat):
                Output only. The requested file format.
        """

        files: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )
        file_format: "ImportRulesFileFormat" = proto.Field(
            proto.ENUM,
            number=2,
            enum="ImportRulesFileFormat",
        )

    class ConvertJobDetails(proto.Message):
        r"""Details regarding a Convert background job.

        Attributes:
            filter (str):
                Output only. AIP-160 based filter used to
                specify the entities to convert
        """

        filter: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class ApplyJobDetails(proto.Message):
        r"""Details regarding an Apply background job.

        Attributes:
            connection_profile (str):
                Output only. The connection profile which was
                used for the apply job.
            filter (str):
                Output only. AIP-160 based filter used to
                specify the entities to apply
        """

        connection_profile: str = proto.Field(
            proto.STRING,
            number=1,
        )
        filter: str = proto.Field(
            proto.STRING,
            number=2,
        )

    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    job_type: "BackgroundJobType" = proto.Field(
        proto.ENUM,
        number=2,
        enum="BackgroundJobType",
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    finish_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    completion_state: JobCompletionState = proto.Field(
        proto.ENUM,
        number=5,
        enum=JobCompletionState,
    )
    completion_comment: str = proto.Field(
        proto.STRING,
        number=6,
    )
    request_autocommit: bool = proto.Field(
        proto.BOOL,
        number=7,
    )
    seed_job_details: SeedJobDetails = proto.Field(
        proto.MESSAGE,
        number=100,
        oneof="job_details",
        message=SeedJobDetails,
    )
    import_rules_job_details: ImportRulesJobDetails = proto.Field(
        proto.MESSAGE,
        number=101,
        oneof="job_details",
        message=ImportRulesJobDetails,
    )
    convert_job_details: ConvertJobDetails = proto.Field(
        proto.MESSAGE,
        number=102,
        oneof="job_details",
        message=ConvertJobDetails,
    )
    apply_job_details: ApplyJobDetails = proto.Field(
        proto.MESSAGE,
        number=103,
        oneof="job_details",
        message=ApplyJobDetails,
    )


class MappingRuleFilter(proto.Message):
    r"""A filter defining the entities that a mapping rule should be
    applied to. When more than one field is specified, the rule is
    applied only to entities which match all the fields.

    Attributes:
        parent_entity (str):
            Optional. The rule should be applied to
            entities whose parent entity (fully qualified
            name) matches the given value. For example, if
            the rule applies to a table entity, the expected
            value should be a schema (schema). If the rule
            applies to a column or index entity, the
            expected value can be either a schema (schema)
            or a table (schema.table)
        entity_name_prefix (str):
            Optional. The rule should be applied to
            entities whose non-qualified name starts with
            the given prefix.
        entity_name_suffix (str):
            Optional. The rule should be applied to
            entities whose non-qualified name ends with the
            given suffix.
        entity_name_contains (str):
            Optional. The rule should be applied to
            entities whose non-qualified name contains the
            given string.
        entities (MutableSequence[str]):
            Optional. The rule should be applied to
            specific entities defined by their fully
            qualified names.
    """

    parent_entity: str = proto.Field(
        proto.STRING,
        number=1,
    )
    entity_name_prefix: str = proto.Field(
        proto.STRING,
        number=2,
    )
    entity_name_suffix: str = proto.Field(
        proto.STRING,
        number=3,
    )
    entity_name_contains: str = proto.Field(
        proto.STRING,
        number=4,
    )
    entities: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )


class MappingRule(proto.Message):
    r"""Definition of a transformation that is to be applied to a
    group of entities in the source schema. Several such
    transformations can be applied to an entity sequentially to
    define the corresponding entity in the target schema.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Full name of the mapping rule resource, in
            the form of:
            projects/{project}/locations/{location}/conversionWorkspaces/{set}/mappingRule/{rule}.
        display_name (str):
            Optional. A human readable name
        state (google.cloud.clouddms_v1.types.MappingRule.State):
            Optional. The mapping rule state
        rule_scope (google.cloud.clouddms_v1.types.DatabaseEntityType):
            Required. The rule scope
        filter (google.cloud.clouddms_v1.types.MappingRuleFilter):
            Required. The rule filter
        rule_order (int):
            Required. The order in which the rule is
            applied. Lower order rules are applied before
            higher value rules so they may end up being
            overridden.
        revision_id (str):
            Output only. The revision ID of the mapping
            rule. A new revision is committed whenever the
            mapping rule is changed in any way. The format
            is an 8-character hexadecimal string.
        revision_create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp that the revision
            was created.
        single_entity_rename (google.cloud.clouddms_v1.types.SingleEntityRename):
            Optional. Rule to specify how a single entity
            should be renamed.

            This field is a member of `oneof`_ ``details``.
        multi_entity_rename (google.cloud.clouddms_v1.types.MultiEntityRename):
            Optional. Rule to specify how multiple
            entities should be renamed.

            This field is a member of `oneof`_ ``details``.
        entity_move (google.cloud.clouddms_v1.types.EntityMove):
            Optional. Rule to specify how multiple
            entities should be relocated into a different
            schema.

            This field is a member of `oneof`_ ``details``.
        single_column_change (google.cloud.clouddms_v1.types.SingleColumnChange):
            Optional. Rule to specify how a single column
            is converted.

            This field is a member of `oneof`_ ``details``.
        multi_column_data_type_change (google.cloud.clouddms_v1.types.MultiColumnDatatypeChange):
            Optional. Rule to specify how multiple
            columns should be converted to a different data
            type.

            This field is a member of `oneof`_ ``details``.
        conditional_column_set_value (google.cloud.clouddms_v1.types.ConditionalColumnSetValue):
            Optional. Rule to specify how the data
            contained in a column should be transformed
            (such as trimmed, rounded, etc) provided that
            the data meets certain criteria.

            This field is a member of `oneof`_ ``details``.
        convert_rowid_column (google.cloud.clouddms_v1.types.ConvertRowIdToColumn):
            Optional. Rule to specify how multiple tables
            should be converted with an additional rowid
            column.

            This field is a member of `oneof`_ ``details``.
        set_table_primary_key (google.cloud.clouddms_v1.types.SetTablePrimaryKey):
            Optional. Rule to specify the primary key for
            a table

            This field is a member of `oneof`_ ``details``.
        single_package_change (google.cloud.clouddms_v1.types.SinglePackageChange):
            Optional. Rule to specify how a single
            package is converted.

            This field is a member of `oneof`_ ``details``.
        source_sql_change (google.cloud.clouddms_v1.types.SourceSqlChange):
            Optional. Rule to change the sql code for an
            entity, for example, function, procedure.

            This field is a member of `oneof`_ ``details``.
        filter_table_columns (google.cloud.clouddms_v1.types.FilterTableColumns):
            Optional. Rule to specify the list of columns
            to include or exclude from a table.

            This field is a member of `oneof`_ ``details``.
    """

    class State(proto.Enum):
        r"""The current mapping rule state such as enabled, disabled or
        deleted.

        Values:
            STATE_UNSPECIFIED (0):
                The state of the mapping rule is unknown.
            ENABLED (1):
                The rule is enabled.
            DISABLED (2):
                The rule is disabled.
            DELETED (3):
                The rule is logically deleted.
        """

        STATE_UNSPECIFIED = 0
        ENABLED = 1
        DISABLED = 2
        DELETED = 3

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=3,
        enum=State,
    )
    rule_scope: "DatabaseEntityType" = proto.Field(
        proto.ENUM,
        number=4,
        enum="DatabaseEntityType",
    )
    filter: "MappingRuleFilter" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="MappingRuleFilter",
    )
    rule_order: int = proto.Field(
        proto.INT64,
        number=6,
    )
    revision_id: str = proto.Field(
        proto.STRING,
        number=7,
    )
    revision_create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    single_entity_rename: "SingleEntityRename" = proto.Field(
        proto.MESSAGE,
        number=102,
        oneof="details",
        message="SingleEntityRename",
    )
    multi_entity_rename: "MultiEntityRename" = proto.Field(
        proto.MESSAGE,
        number=103,
        oneof="details",
        message="MultiEntityRename",
    )
    entity_move: "EntityMove" = proto.Field(
        proto.MESSAGE,
        number=105,
        oneof="details",
        message="EntityMove",
    )
    single_column_change: "SingleColumnChange" = proto.Field(
        proto.MESSAGE,
        number=106,
        oneof="details",
        message="SingleColumnChange",
    )
    multi_column_data_type_change: "MultiColumnDatatypeChange" = proto.Field(
        proto.MESSAGE,
        number=107,
        oneof="details",
        message="MultiColumnDatatypeChange",
    )
    conditional_column_set_value: "ConditionalColumnSetValue" = proto.Field(
        proto.MESSAGE,
        number=108,
        oneof="details",
        message="ConditionalColumnSetValue",
    )
    convert_rowid_column: "ConvertRowIdToColumn" = proto.Field(
        proto.MESSAGE,
        number=114,
        oneof="details",
        message="ConvertRowIdToColumn",
    )
    set_table_primary_key: "SetTablePrimaryKey" = proto.Field(
        proto.MESSAGE,
        number=115,
        oneof="details",
        message="SetTablePrimaryKey",
    )
    single_package_change: "SinglePackageChange" = proto.Field(
        proto.MESSAGE,
        number=116,
        oneof="details",
        message="SinglePackageChange",
    )
    source_sql_change: "SourceSqlChange" = proto.Field(
        proto.MESSAGE,
        number=117,
        oneof="details",
        message="SourceSqlChange",
    )
    filter_table_columns: "FilterTableColumns" = proto.Field(
        proto.MESSAGE,
        number=118,
        oneof="details",
        message="FilterTableColumns",
    )


class SingleEntityRename(proto.Message):
    r"""Options to configure rule type SingleEntityRename.
    The rule is used to rename an entity.

    The rule filter field can refer to only one entity.

    The rule scope can be one of: Database, Schema, Table, Column,
    Constraint, Index, View, Function, Stored Procedure,
    Materialized View, Sequence, UDT, Synonym

    Attributes:
        new_name (str):
            Required. The new name of the destination
            entity
    """

    new_name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class MultiEntityRename(proto.Message):
    r"""Options to configure rule type MultiEntityRename.
    The rule is used to rename multiple entities.

    The rule filter field can refer to one or more entities.

    The rule scope can be one of: Database, Schema, Table, Column,
    Constraint, Index, View, Function, Stored Procedure,
    Materialized View, Sequence, UDT

    Attributes:
        new_name_pattern (str):
            Optional. The pattern used to generate the new entity's
            name. This pattern must include the characters '{name}',
            which will be replaced with the name of the original entity.
            For example, the pattern 't\_{name}' for an entity name jobs
            would be converted to 't_jobs'.

            If unspecified, the default value for this field is '{name}'
        source_name_transformation (google.cloud.clouddms_v1.types.EntityNameTransformation):
            Optional. Additional transformation that can be done on the
            source entity name before it is being used by the
            new_name_pattern, for example lower case. If no
            transformation is desired, use NO_TRANSFORMATION
    """

    new_name_pattern: str = proto.Field(
        proto.STRING,
        number=1,
    )
    source_name_transformation: "EntityNameTransformation" = proto.Field(
        proto.ENUM,
        number=2,
        enum="EntityNameTransformation",
    )


class EntityMove(proto.Message):
    r"""Options to configure rule type EntityMove.
    The rule is used to move an entity to a new schema.

    The rule filter field can refer to one or more entities.

    The rule scope can be one of: Table, Column, Constraint, Index,
    View, Function, Stored Procedure, Materialized View, Sequence,
    UDT

    Attributes:
        new_schema (str):
            Required. The new schema
    """

    new_schema: str = proto.Field(
        proto.STRING,
        number=1,
    )


class SingleColumnChange(proto.Message):
    r"""Options to configure rule type SingleColumnChange.
    The rule is used to change the properties of a column.

    The rule filter field can refer to one entity.

    The rule scope can be one of: Column.

    When using this rule, if a field is not specified than the
    destination column's configuration will be the same as the one
    in the source column..

    Attributes:
        data_type (str):
            Optional. Column data type name.
        charset (str):
            Optional. Charset override - instead of table
            level charset.
        collation (str):
            Optional. Collation override - instead of
            table level collation.
        length (int):
            Optional. Column length - e.g. 50 as in
            varchar (50) - when relevant.
        precision (int):
            Optional. Column precision - e.g. 8 as in
            double (8,2) - when relevant.
        scale (int):
            Optional. Column scale - e.g. 2 as in double
            (8,2) - when relevant.
        fractional_seconds_precision (int):
            Optional. Column fractional seconds precision
            - e.g. 2 as in timestamp (2)
            - when relevant.
        array (bool):
            Optional. Is the column of array type.
        array_length (int):
            Optional. The length of the array, only
            relevant if the column type is an array.
        nullable (bool):
            Optional. Is the column nullable.
        auto_generated (bool):
            Optional. Is the column
            auto-generated/identity.
        udt (bool):
            Optional. Is the column a UDT (User-defined
            Type).
        custom_features (google.protobuf.struct_pb2.Struct):
            Optional. Custom engine specific features.
        set_values (MutableSequence[str]):
            Optional. Specifies the list of values
            allowed in the column.
        comment (str):
            Optional. Comment associated with the column.
    """

    data_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    charset: str = proto.Field(
        proto.STRING,
        number=2,
    )
    collation: str = proto.Field(
        proto.STRING,
        number=3,
    )
    length: int = proto.Field(
        proto.INT64,
        number=4,
    )
    precision: int = proto.Field(
        proto.INT32,
        number=5,
    )
    scale: int = proto.Field(
        proto.INT32,
        number=6,
    )
    fractional_seconds_precision: int = proto.Field(
        proto.INT32,
        number=7,
    )
    array: bool = proto.Field(
        proto.BOOL,
        number=8,
    )
    array_length: int = proto.Field(
        proto.INT32,
        number=9,
    )
    nullable: bool = proto.Field(
        proto.BOOL,
        number=10,
    )
    auto_generated: bool = proto.Field(
        proto.BOOL,
        number=11,
    )
    udt: bool = proto.Field(
        proto.BOOL,
        number=12,
    )
    custom_features: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=13,
        message=struct_pb2.Struct,
    )
    set_values: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=14,
    )
    comment: str = proto.Field(
        proto.STRING,
        number=15,
    )


class MultiColumnDatatypeChange(proto.Message):
    r"""Options to configure rule type MultiColumnDatatypeChange.
    The rule is used to change the data type and associated
    properties of multiple columns at once.

    The rule filter field can refer to one or more entities.

    The rule scope can be one of:Column.

    This rule requires additional filters to be specified beyond the
    basic rule filter field, which is the source data type, but the
    rule supports additional filtering capabilities such as the
    minimum and maximum field length. All additional filters which
    are specified are required to be met in order for the rule to be
    applied (logical AND between the fields).

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        source_data_type_filter (str):
            Required. Filter on source data type.
        source_text_filter (google.cloud.clouddms_v1.types.SourceTextFilter):
            Optional. Filter for text-based data types
            like varchar.

            This field is a member of `oneof`_ ``source_filter``.
        source_numeric_filter (google.cloud.clouddms_v1.types.SourceNumericFilter):
            Optional. Filter for fixed point number data
            types such as NUMERIC/NUMBER.

            This field is a member of `oneof`_ ``source_filter``.
        new_data_type (str):
            Required. New data type.
        override_length (int):
            Optional. Column length - e.g. varchar (50) -
            if not specified and relevant uses the source
            column length.
        override_scale (int):
            Optional. Column scale - when relevant - if
            not specified and relevant uses the source
            column scale.
        override_precision (int):
            Optional. Column precision - when relevant -
            if not specified and relevant uses the source
            column precision.
        override_fractional_seconds_precision (int):
            Optional. Column fractional seconds precision
            - used only for timestamp based datatypes - if
              not specified and relevant uses the source
              column fractional seconds precision.
        custom_features (google.protobuf.struct_pb2.Struct):
            Optional. Custom engine specific features.
    """

    source_data_type_filter: str = proto.Field(
        proto.STRING,
        number=1,
    )
    source_text_filter: "SourceTextFilter" = proto.Field(
        proto.MESSAGE,
        number=100,
        oneof="source_filter",
        message="SourceTextFilter",
    )
    source_numeric_filter: "SourceNumericFilter" = proto.Field(
        proto.MESSAGE,
        number=101,
        oneof="source_filter",
        message="SourceNumericFilter",
    )
    new_data_type: str = proto.Field(
        proto.STRING,
        number=2,
    )
    override_length: int = proto.Field(
        proto.INT64,
        number=3,
    )
    override_scale: int = proto.Field(
        proto.INT32,
        number=4,
    )
    override_precision: int = proto.Field(
        proto.INT32,
        number=5,
    )
    override_fractional_seconds_precision: int = proto.Field(
        proto.INT32,
        number=6,
    )
    custom_features: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=7,
        message=struct_pb2.Struct,
    )


class SourceTextFilter(proto.Message):
    r"""Filter for text-based data types like varchar.

    Attributes:
        source_min_length_filter (int):
            Optional. The filter will match columns with
            length greater than or equal to this number.
        source_max_length_filter (int):
            Optional. The filter will match columns with
            length smaller than or equal to this number.
    """

    source_min_length_filter: int = proto.Field(
        proto.INT64,
        number=1,
    )
    source_max_length_filter: int = proto.Field(
        proto.INT64,
        number=2,
    )


class SourceNumericFilter(proto.Message):
    r"""Filter for fixed point number data types such as
    NUMERIC/NUMBER

    Attributes:
        source_min_scale_filter (int):
            Optional. The filter will match columns with
            scale greater than or equal to this number.
        source_max_scale_filter (int):
            Optional. The filter will match columns with
            scale smaller than or equal to this number.
        source_min_precision_filter (int):
            Optional. The filter will match columns with
            precision greater than or equal to this number.
        source_max_precision_filter (int):
            Optional. The filter will match columns with
            precision smaller than or equal to this number.
        numeric_filter_option (google.cloud.clouddms_v1.types.NumericFilterOption):
            Required. Enum to set the option defining the
            datatypes numeric filter has to be applied to
    """

    source_min_scale_filter: int = proto.Field(
        proto.INT32,
        number=1,
    )
    source_max_scale_filter: int = proto.Field(
        proto.INT32,
        number=2,
    )
    source_min_precision_filter: int = proto.Field(
        proto.INT32,
        number=3,
    )
    source_max_precision_filter: int = proto.Field(
        proto.INT32,
        number=4,
    )
    numeric_filter_option: "NumericFilterOption" = proto.Field(
        proto.ENUM,
        number=5,
        enum="NumericFilterOption",
    )


class ConditionalColumnSetValue(proto.Message):
    r"""Options to configure rule type ConditionalColumnSetValue.
    The rule is used to transform the data which is being
    replicated/migrated.

    The rule filter field can refer to one or more entities.

    The rule scope can be one of: Column.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        source_text_filter (google.cloud.clouddms_v1.types.SourceTextFilter):
            Optional. Optional filter on source column
            length. Used for text based data types like
            varchar.

            This field is a member of `oneof`_ ``source_filter``.
        source_numeric_filter (google.cloud.clouddms_v1.types.SourceNumericFilter):
            Optional. Optional filter on source column
            precision and scale. Used for fixed point
            numbers such as NUMERIC/NUMBER data types.

            This field is a member of `oneof`_ ``source_filter``.
        value_transformation (google.cloud.clouddms_v1.types.ValueTransformation):
            Required. Description of data transformation
            during migration.
        custom_features (google.protobuf.struct_pb2.Struct):
            Optional. Custom engine specific features.
    """

    source_text_filter: "SourceTextFilter" = proto.Field(
        proto.MESSAGE,
        number=100,
        oneof="source_filter",
        message="SourceTextFilter",
    )
    source_numeric_filter: "SourceNumericFilter" = proto.Field(
        proto.MESSAGE,
        number=101,
        oneof="source_filter",
        message="SourceNumericFilter",
    )
    value_transformation: "ValueTransformation" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="ValueTransformation",
    )
    custom_features: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=2,
        message=struct_pb2.Struct,
    )


class ValueTransformation(proto.Message):
    r"""Description of data transformation during migration as part
    of the ConditionalColumnSetValue.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        is_null (google.protobuf.empty_pb2.Empty):
            Optional. Value is null

            This field is a member of `oneof`_ ``filter``.
        value_list (google.cloud.clouddms_v1.types.ValueListFilter):
            Optional. Value is found in the specified
            list.

            This field is a member of `oneof`_ ``filter``.
        int_comparison (google.cloud.clouddms_v1.types.IntComparisonFilter):
            Optional. Filter on relation between source
            value and compare value of type integer.

            This field is a member of `oneof`_ ``filter``.
        double_comparison (google.cloud.clouddms_v1.types.DoubleComparisonFilter):
            Optional. Filter on relation between source
            value and compare value of type double.

            This field is a member of `oneof`_ ``filter``.
        assign_null (google.protobuf.empty_pb2.Empty):
            Optional. Set to null

            This field is a member of `oneof`_ ``action``.
        assign_specific_value (google.cloud.clouddms_v1.types.AssignSpecificValue):
            Optional. Set to a specific value (value is
            converted to fit the target data type)

            This field is a member of `oneof`_ ``action``.
        assign_min_value (google.protobuf.empty_pb2.Empty):
            Optional. Set to min_value - if integer or numeric, will use
            int.minvalue, etc

            This field is a member of `oneof`_ ``action``.
        assign_max_value (google.protobuf.empty_pb2.Empty):
            Optional. Set to max_value - if integer or numeric, will use
            int.maxvalue, etc

            This field is a member of `oneof`_ ``action``.
        round_scale (google.cloud.clouddms_v1.types.RoundToScale):
            Optional. Allows the data to change scale

            This field is a member of `oneof`_ ``action``.
        apply_hash (google.cloud.clouddms_v1.types.ApplyHash):
            Optional. Applies a hash function on the data

            This field is a member of `oneof`_ ``action``.
    """

    is_null: empty_pb2.Empty = proto.Field(
        proto.MESSAGE,
        number=100,
        oneof="filter",
        message=empty_pb2.Empty,
    )
    value_list: "ValueListFilter" = proto.Field(
        proto.MESSAGE,
        number=101,
        oneof="filter",
        message="ValueListFilter",
    )
    int_comparison: "IntComparisonFilter" = proto.Field(
        proto.MESSAGE,
        number=102,
        oneof="filter",
        message="IntComparisonFilter",
    )
    double_comparison: "DoubleComparisonFilter" = proto.Field(
        proto.MESSAGE,
        number=103,
        oneof="filter",
        message="DoubleComparisonFilter",
    )
    assign_null: empty_pb2.Empty = proto.Field(
        proto.MESSAGE,
        number=200,
        oneof="action",
        message=empty_pb2.Empty,
    )
    assign_specific_value: "AssignSpecificValue" = proto.Field(
        proto.MESSAGE,
        number=201,
        oneof="action",
        message="AssignSpecificValue",
    )
    assign_min_value: empty_pb2.Empty = proto.Field(
        proto.MESSAGE,
        number=202,
        oneof="action",
        message=empty_pb2.Empty,
    )
    assign_max_value: empty_pb2.Empty = proto.Field(
        proto.MESSAGE,
        number=203,
        oneof="action",
        message=empty_pb2.Empty,
    )
    round_scale: "RoundToScale" = proto.Field(
        proto.MESSAGE,
        number=204,
        oneof="action",
        message="RoundToScale",
    )
    apply_hash: "ApplyHash" = proto.Field(
        proto.MESSAGE,
        number=205,
        oneof="action",
        message="ApplyHash",
    )


class ConvertRowIdToColumn(proto.Message):
    r"""Options to configure rule type ConvertROWIDToColumn.
    The rule is used to add column rowid to destination tables based
    on an Oracle rowid function/property.

    The rule filter field can refer to one or more entities.

    The rule scope can be one of: Table.

    This rule requires additional filter to be specified beyond the
    basic rule filter field, which is whether or not to work on
    tables which already have a primary key defined.

    Attributes:
        only_if_no_primary_key (bool):
            Required. Only work on tables without primary
            key defined
    """

    only_if_no_primary_key: bool = proto.Field(
        proto.BOOL,
        number=1,
    )


class SetTablePrimaryKey(proto.Message):
    r"""Options to configure rule type SetTablePrimaryKey.
    The rule is used to specify the columns and name to
    configure/alter the primary key of a table.

    The rule filter field can refer to one entity.

    The rule scope can be one of: Table.

    Attributes:
        primary_key_columns (MutableSequence[str]):
            Required. List of column names for the
            primary key
        primary_key (str):
            Optional. Name for the primary key
    """

    primary_key_columns: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    primary_key: str = proto.Field(
        proto.STRING,
        number=2,
    )


class SinglePackageChange(proto.Message):
    r"""Options to configure rule type SinglePackageChange.
    The rule is used to alter the sql code for a package entities.

    The rule filter field can refer to one entity.

    The rule scope can be: Package

    Attributes:
        package_description (str):
            Optional. Sql code for package description
        package_body (str):
            Optional. Sql code for package body
    """

    package_description: str = proto.Field(
        proto.STRING,
        number=1,
    )
    package_body: str = proto.Field(
        proto.STRING,
        number=2,
    )


class SourceSqlChange(proto.Message):
    r"""Options to configure rule type SourceSqlChange.
    The rule is used to alter the sql code for database entities.

    The rule filter field can refer to one entity.

    The rule scope can be: StoredProcedure, Function, Trigger, View

    Attributes:
        sql_code (str):
            Required. Sql code for source (stored
            procedure, function, trigger or view)
    """

    sql_code: str = proto.Field(
        proto.STRING,
        number=1,
    )


class FilterTableColumns(proto.Message):
    r"""Options to configure rule type FilterTableColumns.
    The rule is used to filter the list of columns to include or
    exclude from a table.

    The rule filter field can refer to one entity.

    The rule scope can be: Table

    Only one of the two lists can be specified for the rule.

    Attributes:
        include_columns (MutableSequence[str]):
            Optional. List of columns to be included for
            a particular table.
        exclude_columns (MutableSequence[str]):
            Optional. List of columns to be excluded for
            a particular table.
    """

    include_columns: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    exclude_columns: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class ValueListFilter(proto.Message):
    r"""A list of values to filter by in ConditionalColumnSetValue

    Attributes:
        value_present_list (google.cloud.clouddms_v1.types.ValuePresentInList):
            Required. Indicates whether the filter
            matches rows with values that are present in the
            list or those with values not present in it.
        values (MutableSequence[str]):
            Required. The list to be used to filter by
        ignore_case (bool):
            Required. Whether to ignore case when
            filtering by values. Defaults to false
    """

    value_present_list: "ValuePresentInList" = proto.Field(
        proto.ENUM,
        number=1,
        enum="ValuePresentInList",
    )
    values: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    ignore_case: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class IntComparisonFilter(proto.Message):
    r"""Filter based on relation between source value and compare
    value of type integer in ConditionalColumnSetValue

    Attributes:
        value_comparison (google.cloud.clouddms_v1.types.ValueComparison):
            Required. Relation between source value and
            compare value
        value (int):
            Required. Integer compare value to be used
    """

    value_comparison: "ValueComparison" = proto.Field(
        proto.ENUM,
        number=1,
        enum="ValueComparison",
    )
    value: int = proto.Field(
        proto.INT64,
        number=2,
    )


class DoubleComparisonFilter(proto.Message):
    r"""Filter based on relation between source
    value and compare value of type double in
    ConditionalColumnSetValue

    Attributes:
        value_comparison (google.cloud.clouddms_v1.types.ValueComparison):
            Required. Relation between source value and
            compare value
        value (float):
            Required. Double compare value to be used
    """

    value_comparison: "ValueComparison" = proto.Field(
        proto.ENUM,
        number=1,
        enum="ValueComparison",
    )
    value: float = proto.Field(
        proto.DOUBLE,
        number=2,
    )


class AssignSpecificValue(proto.Message):
    r"""Set to a specific value (value is converted to fit the target
    data type)

    Attributes:
        value (str):
            Required. Specific value to be assigned
    """

    value: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ApplyHash(proto.Message):
    r"""Apply a hash function on the value.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        uuid_from_bytes (google.protobuf.empty_pb2.Empty):
            Optional. Generate UUID from the data's byte
            array

            This field is a member of `oneof`_ ``hash_function``.
    """

    uuid_from_bytes: empty_pb2.Empty = proto.Field(
        proto.MESSAGE,
        number=100,
        oneof="hash_function",
        message=empty_pb2.Empty,
    )


class RoundToScale(proto.Message):
    r"""This allows the data to change scale, for example if the
    source is 2 digits after the decimal point, specify round to
    scale value = 2. If for example the value needs to be converted
    to an integer, use round to scale value = 0.

    Attributes:
        scale (int):
            Required. Scale value to be used
    """

    scale: int = proto.Field(
        proto.INT32,
        number=1,
    )


class DatabaseEntity(proto.Message):
    r"""The base entity type for all the database related entities.
    The message contains the entity name, the name of its parent,
    the entity type, and the specific details per entity type.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        short_name (str):
            The short name (e.g. table name) of the
            entity.
        parent_entity (str):
            The full name of the parent entity (e.g.
            schema name).
        tree (google.cloud.clouddms_v1.types.DatabaseEntity.TreeType):
            The type of tree the entity belongs to.
        entity_type (google.cloud.clouddms_v1.types.DatabaseEntityType):
            The type of the database entity (table, view,
            index, ...).
        mappings (MutableSequence[google.cloud.clouddms_v1.types.EntityMapping]):
            Details about entity mappings.
            For source tree entities, this holds the draft
            entities which were generated by the mapping
            rules.
            For draft tree entities, this holds the source
            entities which were converted to form the draft
            entity.
            Destination entities will have no mapping
            details.
        entity_ddl (MutableSequence[google.cloud.clouddms_v1.types.EntityDdl]):
            Details about the entity DDL script. Multiple
            DDL scripts are provided for child entities such
            as a table entity will have one DDL for the
            table with additional DDLs for each index,
            constraint and such.
        issues (MutableSequence[google.cloud.clouddms_v1.types.EntityIssue]):
            Details about the various issues found for
            the entity.
        database (google.cloud.clouddms_v1.types.DatabaseInstanceEntity):
            Database.

            This field is a member of `oneof`_ ``entity_body``.
        schema (google.cloud.clouddms_v1.types.SchemaEntity):
            Schema.

            This field is a member of `oneof`_ ``entity_body``.
        table (google.cloud.clouddms_v1.types.TableEntity):
            Table.

            This field is a member of `oneof`_ ``entity_body``.
        view (google.cloud.clouddms_v1.types.ViewEntity):
            View.

            This field is a member of `oneof`_ ``entity_body``.
        sequence (google.cloud.clouddms_v1.types.SequenceEntity):
            Sequence.

            This field is a member of `oneof`_ ``entity_body``.
        stored_procedure (google.cloud.clouddms_v1.types.StoredProcedureEntity):
            Stored procedure.

            This field is a member of `oneof`_ ``entity_body``.
        database_function (google.cloud.clouddms_v1.types.FunctionEntity):
            Function.

            This field is a member of `oneof`_ ``entity_body``.
        synonym (google.cloud.clouddms_v1.types.SynonymEntity):
            Synonym.

            This field is a member of `oneof`_ ``entity_body``.
        database_package (google.cloud.clouddms_v1.types.PackageEntity):
            Package.

            This field is a member of `oneof`_ ``entity_body``.
        udt (google.cloud.clouddms_v1.types.UDTEntity):
            UDT.

            This field is a member of `oneof`_ ``entity_body``.
        materialized_view (google.cloud.clouddms_v1.types.MaterializedViewEntity):
            Materialized view.

            This field is a member of `oneof`_ ``entity_body``.
    """

    class TreeType(proto.Enum):
        r"""The type of database entities tree.

        Values:
            TREE_TYPE_UNSPECIFIED (0):
                Tree type unspecified.
            SOURCE (1):
                Tree of entities loaded from a source
                database.
            DRAFT (2):
                Tree of entities converted from the source
                tree using the mapping rules.
            DESTINATION (3):
                Tree of entities observed on the destination
                database.
        """

        TREE_TYPE_UNSPECIFIED = 0
        SOURCE = 1
        DRAFT = 2
        DESTINATION = 3

    short_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    parent_entity: str = proto.Field(
        proto.STRING,
        number=2,
    )
    tree: TreeType = proto.Field(
        proto.ENUM,
        number=3,
        enum=TreeType,
    )
    entity_type: "DatabaseEntityType" = proto.Field(
        proto.ENUM,
        number=4,
        enum="DatabaseEntityType",
    )
    mappings: MutableSequence["EntityMapping"] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message="EntityMapping",
    )
    entity_ddl: MutableSequence["EntityDdl"] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message="EntityDdl",
    )
    issues: MutableSequence["EntityIssue"] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message="EntityIssue",
    )
    database: "DatabaseInstanceEntity" = proto.Field(
        proto.MESSAGE,
        number=101,
        oneof="entity_body",
        message="DatabaseInstanceEntity",
    )
    schema: "SchemaEntity" = proto.Field(
        proto.MESSAGE,
        number=102,
        oneof="entity_body",
        message="SchemaEntity",
    )
    table: "TableEntity" = proto.Field(
        proto.MESSAGE,
        number=103,
        oneof="entity_body",
        message="TableEntity",
    )
    view: "ViewEntity" = proto.Field(
        proto.MESSAGE,
        number=104,
        oneof="entity_body",
        message="ViewEntity",
    )
    sequence: "SequenceEntity" = proto.Field(
        proto.MESSAGE,
        number=105,
        oneof="entity_body",
        message="SequenceEntity",
    )
    stored_procedure: "StoredProcedureEntity" = proto.Field(
        proto.MESSAGE,
        number=106,
        oneof="entity_body",
        message="StoredProcedureEntity",
    )
    database_function: "FunctionEntity" = proto.Field(
        proto.MESSAGE,
        number=107,
        oneof="entity_body",
        message="FunctionEntity",
    )
    synonym: "SynonymEntity" = proto.Field(
        proto.MESSAGE,
        number=108,
        oneof="entity_body",
        message="SynonymEntity",
    )
    database_package: "PackageEntity" = proto.Field(
        proto.MESSAGE,
        number=109,
        oneof="entity_body",
        message="PackageEntity",
    )
    udt: "UDTEntity" = proto.Field(
        proto.MESSAGE,
        number=110,
        oneof="entity_body",
        message="UDTEntity",
    )
    materialized_view: "MaterializedViewEntity" = proto.Field(
        proto.MESSAGE,
        number=111,
        oneof="entity_body",
        message="MaterializedViewEntity",
    )


class DatabaseInstanceEntity(proto.Message):
    r"""DatabaseInstance acts as a parent entity to other database
    entities.

    Attributes:
        custom_features (google.protobuf.struct_pb2.Struct):
            Custom engine specific features.
    """

    custom_features: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=1,
        message=struct_pb2.Struct,
    )


class SchemaEntity(proto.Message):
    r"""Schema typically has no parent entity, but can have a parent
    entity DatabaseInstance (for database engines which support it).
    For some database engines, the terms  schema and user can be
    used interchangeably when they refer to a namespace or a
    collection of other database entities. Can store additional
    information which is schema specific.

    Attributes:
        custom_features (google.protobuf.struct_pb2.Struct):
            Custom engine specific features.
    """

    custom_features: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=1,
        message=struct_pb2.Struct,
    )


class TableEntity(proto.Message):
    r"""Table's parent is a schema.

    Attributes:
        columns (MutableSequence[google.cloud.clouddms_v1.types.ColumnEntity]):
            Table columns.
        constraints (MutableSequence[google.cloud.clouddms_v1.types.ConstraintEntity]):
            Table constraints.
        indices (MutableSequence[google.cloud.clouddms_v1.types.IndexEntity]):
            Table indices.
        triggers (MutableSequence[google.cloud.clouddms_v1.types.TriggerEntity]):
            Table triggers.
        custom_features (google.protobuf.struct_pb2.Struct):
            Custom engine specific features.
        comment (str):
            Comment associated with the table.
    """

    columns: MutableSequence["ColumnEntity"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ColumnEntity",
    )
    constraints: MutableSequence["ConstraintEntity"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="ConstraintEntity",
    )
    indices: MutableSequence["IndexEntity"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="IndexEntity",
    )
    triggers: MutableSequence["TriggerEntity"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="TriggerEntity",
    )
    custom_features: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=5,
        message=struct_pb2.Struct,
    )
    comment: str = proto.Field(
        proto.STRING,
        number=6,
    )


class ColumnEntity(proto.Message):
    r"""Column is not used as an independent entity, it is retrieved
    as part of a Table entity.

    Attributes:
        name (str):
            Column name.
        data_type (str):
            Column data type.
        charset (str):
            Charset override - instead of table level
            charset.
        collation (str):
            Collation override - instead of table level
            collation.
        length (int):
            Column length - e.g. varchar (50).
        precision (int):
            Column precision - when relevant.
        scale (int):
            Column scale - when relevant.
        fractional_seconds_precision (int):
            Column fractional second precision - used for
            timestamp based datatypes.
        array (bool):
            Is the column of array type.
        array_length (int):
            If the column is array, of which length.
        nullable (bool):
            Is the column nullable.
        auto_generated (bool):
            Is the column auto-generated/identity.
        udt (bool):
            Is the column a UDT.
        custom_features (google.protobuf.struct_pb2.Struct):
            Custom engine specific features.
        set_values (MutableSequence[str]):
            Specifies the list of values allowed in the
            column. Only used for set data type.
        comment (str):
            Comment associated with the column.
        ordinal_position (int):
            Column order in the table.
        default_value (str):
            Default value of the column.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    data_type: str = proto.Field(
        proto.STRING,
        number=2,
    )
    charset: str = proto.Field(
        proto.STRING,
        number=3,
    )
    collation: str = proto.Field(
        proto.STRING,
        number=4,
    )
    length: int = proto.Field(
        proto.INT64,
        number=5,
    )
    precision: int = proto.Field(
        proto.INT32,
        number=6,
    )
    scale: int = proto.Field(
        proto.INT32,
        number=7,
    )
    fractional_seconds_precision: int = proto.Field(
        proto.INT32,
        number=8,
    )
    array: bool = proto.Field(
        proto.BOOL,
        number=9,
    )
    array_length: int = proto.Field(
        proto.INT32,
        number=10,
    )
    nullable: bool = proto.Field(
        proto.BOOL,
        number=11,
    )
    auto_generated: bool = proto.Field(
        proto.BOOL,
        number=12,
    )
    udt: bool = proto.Field(
        proto.BOOL,
        number=13,
    )
    custom_features: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=14,
        message=struct_pb2.Struct,
    )
    set_values: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=15,
    )
    comment: str = proto.Field(
        proto.STRING,
        number=16,
    )
    ordinal_position: int = proto.Field(
        proto.INT32,
        number=17,
    )
    default_value: str = proto.Field(
        proto.STRING,
        number=18,
    )


class ConstraintEntity(proto.Message):
    r"""Constraint is not used as an independent entity, it is
    retrieved as part of another entity such as Table or View.

    Attributes:
        name (str):
            The name of the table constraint.
        type_ (str):
            Type of constraint, for example unique,
            primary key, foreign key (currently only primary
            key is supported).
        table_columns (MutableSequence[str]):
            Table columns used as part of the Constraint,
            for example primary key constraint should list
            the columns which constitutes the key.
        custom_features (google.protobuf.struct_pb2.Struct):
            Custom engine specific features.
        reference_columns (MutableSequence[str]):
            Reference columns which may be associated with the
            constraint. For example, if the constraint is a FOREIGN_KEY,
            this represents the list of full names of referenced columns
            by the foreign key.
        reference_table (str):
            Reference table which may be associated with the constraint.
            For example, if the constraint is a FOREIGN_KEY, this
            represents the list of full name of the referenced table by
            the foreign key.
        table_name (str):
            Table which is associated with the constraint. In case the
            constraint is defined on a table, this field is left empty
            as this information is stored in parent_name. However, if
            constraint is defined on a view, this field stores the table
            name on which the view is defined.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_: str = proto.Field(
        proto.STRING,
        number=2,
    )
    table_columns: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    custom_features: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=4,
        message=struct_pb2.Struct,
    )
    reference_columns: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    reference_table: str = proto.Field(
        proto.STRING,
        number=6,
    )
    table_name: str = proto.Field(
        proto.STRING,
        number=7,
    )


class IndexEntity(proto.Message):
    r"""Index is not used as an independent entity, it is retrieved
    as part of a Table entity.

    Attributes:
        name (str):
            The name of the index.
        type_ (str):
            Type of index, for example B-TREE.
        table_columns (MutableSequence[str]):
            Table columns used as part of the Index, for
            example B-TREE index should list the columns
            which constitutes the index.
        unique (bool):
            Boolean value indicating whether the index is
            unique.
        custom_features (google.protobuf.struct_pb2.Struct):
            Custom engine specific features.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_: str = proto.Field(
        proto.STRING,
        number=2,
    )
    table_columns: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    unique: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    custom_features: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=5,
        message=struct_pb2.Struct,
    )


class TriggerEntity(proto.Message):
    r"""Trigger is not used as an independent entity, it is retrieved
    as part of a Table entity.

    Attributes:
        name (str):
            The name of the trigger.
        triggering_events (MutableSequence[str]):
            The DML, DDL, or database events that fire
            the trigger, for example INSERT, UPDATE.
        trigger_type (str):
            Indicates when the trigger fires, for example
            BEFORE STATEMENT, AFTER EACH ROW.
        sql_code (str):
            The SQL code which creates the trigger.
        custom_features (google.protobuf.struct_pb2.Struct):
            Custom engine specific features.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    triggering_events: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    trigger_type: str = proto.Field(
        proto.STRING,
        number=3,
    )
    sql_code: str = proto.Field(
        proto.STRING,
        number=4,
    )
    custom_features: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=5,
        message=struct_pb2.Struct,
    )


class ViewEntity(proto.Message):
    r"""View's parent is a schema.

    Attributes:
        sql_code (str):
            The SQL code which creates the view.
        custom_features (google.protobuf.struct_pb2.Struct):
            Custom engine specific features.
        constraints (MutableSequence[google.cloud.clouddms_v1.types.ConstraintEntity]):
            View constraints.
    """

    sql_code: str = proto.Field(
        proto.STRING,
        number=1,
    )
    custom_features: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=2,
        message=struct_pb2.Struct,
    )
    constraints: MutableSequence["ConstraintEntity"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="ConstraintEntity",
    )


class SequenceEntity(proto.Message):
    r"""Sequence's parent is a schema.

    Attributes:
        increment (int):
            Increment value for the sequence.
        start_value (bytes):
            Start number for the sequence represented as
            bytes to accommodate large. numbers
        max_value (bytes):
            Maximum number for the sequence represented
            as bytes to accommodate large. numbers
        min_value (bytes):
            Minimum number for the sequence represented
            as bytes to accommodate large. numbers
        cycle (bool):
            Indicates whether the sequence value should
            cycle through.
        cache (int):
            Indicates number of entries to cache /
            precreate.
        custom_features (google.protobuf.struct_pb2.Struct):
            Custom engine specific features.
    """

    increment: int = proto.Field(
        proto.INT64,
        number=1,
    )
    start_value: bytes = proto.Field(
        proto.BYTES,
        number=2,
    )
    max_value: bytes = proto.Field(
        proto.BYTES,
        number=3,
    )
    min_value: bytes = proto.Field(
        proto.BYTES,
        number=4,
    )
    cycle: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    cache: int = proto.Field(
        proto.INT64,
        number=6,
    )
    custom_features: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=7,
        message=struct_pb2.Struct,
    )


class StoredProcedureEntity(proto.Message):
    r"""Stored procedure's parent is a schema.

    Attributes:
        sql_code (str):
            The SQL code which creates the stored
            procedure.
        custom_features (google.protobuf.struct_pb2.Struct):
            Custom engine specific features.
    """

    sql_code: str = proto.Field(
        proto.STRING,
        number=1,
    )
    custom_features: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=2,
        message=struct_pb2.Struct,
    )


class FunctionEntity(proto.Message):
    r"""Function's parent is a schema.

    Attributes:
        sql_code (str):
            The SQL code which creates the function.
        custom_features (google.protobuf.struct_pb2.Struct):
            Custom engine specific features.
    """

    sql_code: str = proto.Field(
        proto.STRING,
        number=1,
    )
    custom_features: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=2,
        message=struct_pb2.Struct,
    )


class MaterializedViewEntity(proto.Message):
    r"""MaterializedView's parent is a schema.

    Attributes:
        sql_code (str):
            The SQL code which creates the view.
        custom_features (google.protobuf.struct_pb2.Struct):
            Custom engine specific features.
    """

    sql_code: str = proto.Field(
        proto.STRING,
        number=1,
    )
    custom_features: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=2,
        message=struct_pb2.Struct,
    )


class SynonymEntity(proto.Message):
    r"""Synonym's parent is a schema.

    Attributes:
        source_entity (str):
            The name of the entity for which the synonym
            is being created (the source).
        source_type (google.cloud.clouddms_v1.types.DatabaseEntityType):
            The type of the entity for which the synonym
            is being created (usually a table or a
            sequence).
        custom_features (google.protobuf.struct_pb2.Struct):
            Custom engine specific features.
    """

    source_entity: str = proto.Field(
        proto.STRING,
        number=1,
    )
    source_type: "DatabaseEntityType" = proto.Field(
        proto.ENUM,
        number=2,
        enum="DatabaseEntityType",
    )
    custom_features: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=3,
        message=struct_pb2.Struct,
    )


class PackageEntity(proto.Message):
    r"""Package's parent is a schema.

    Attributes:
        package_sql_code (str):
            The SQL code which creates the package.
        package_body (str):
            The SQL code which creates the package body.
            If the package specification has cursors or
            subprograms, then the package body is mandatory.
        custom_features (google.protobuf.struct_pb2.Struct):
            Custom engine specific features.
    """

    package_sql_code: str = proto.Field(
        proto.STRING,
        number=1,
    )
    package_body: str = proto.Field(
        proto.STRING,
        number=2,
    )
    custom_features: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=3,
        message=struct_pb2.Struct,
    )


class UDTEntity(proto.Message):
    r"""UDT's parent is a schema.

    Attributes:
        udt_sql_code (str):
            The SQL code which creates the udt.
        udt_body (str):
            The SQL code which creates the udt body.
        custom_features (google.protobuf.struct_pb2.Struct):
            Custom engine specific features.
    """

    udt_sql_code: str = proto.Field(
        proto.STRING,
        number=1,
    )
    udt_body: str = proto.Field(
        proto.STRING,
        number=2,
    )
    custom_features: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=3,
        message=struct_pb2.Struct,
    )


class EntityMapping(proto.Message):
    r"""Details of the mappings of a database entity.

    Attributes:
        source_entity (str):
            Source entity full name.
            The source entity can also be a column, index or
            constraint using the same naming notation
            schema.table.column.
        draft_entity (str):
            Target entity full name.
            The draft entity can also include a column,
            index or constraint using the same naming
            notation schema.table.column.
        source_type (google.cloud.clouddms_v1.types.DatabaseEntityType):
            Type of source entity.
        draft_type (google.cloud.clouddms_v1.types.DatabaseEntityType):
            Type of draft entity.
        mapping_log (MutableSequence[google.cloud.clouddms_v1.types.EntityMappingLogEntry]):
            Entity mapping log entries.
            Multiple rules can be effective and contribute
            changes to a converted entity, such as a rule
            can handle the entity name, another rule can
            handle an entity type. In addition, rules which
            did not change the entity are also logged along
            with the reason preventing them to do so.
    """

    source_entity: str = proto.Field(
        proto.STRING,
        number=1,
    )
    draft_entity: str = proto.Field(
        proto.STRING,
        number=2,
    )
    source_type: "DatabaseEntityType" = proto.Field(
        proto.ENUM,
        number=4,
        enum="DatabaseEntityType",
    )
    draft_type: "DatabaseEntityType" = proto.Field(
        proto.ENUM,
        number=5,
        enum="DatabaseEntityType",
    )
    mapping_log: MutableSequence["EntityMappingLogEntry"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="EntityMappingLogEntry",
    )


class EntityMappingLogEntry(proto.Message):
    r"""A single record of a rule which was used for a mapping.

    Attributes:
        rule_id (str):
            Which rule caused this log entry.
        rule_revision_id (str):
            Rule revision ID.
        mapping_comment (str):
            Comment.
    """

    rule_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    rule_revision_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    mapping_comment: str = proto.Field(
        proto.STRING,
        number=3,
    )


class EntityDdl(proto.Message):
    r"""A single DDL statement for a specific entity

    Attributes:
        ddl_type (str):
            Type of DDL (Create, Alter).
        entity (str):
            The name of the database entity the ddl
            refers to.
        ddl (str):
            The actual ddl code.
        entity_type (google.cloud.clouddms_v1.types.DatabaseEntityType):
            The entity type (if the DDL is for a sub
            entity).
        issue_id (MutableSequence[str]):
            EntityIssues found for this ddl.
    """

    ddl_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    entity: str = proto.Field(
        proto.STRING,
        number=2,
    )
    ddl: str = proto.Field(
        proto.STRING,
        number=3,
    )
    entity_type: "DatabaseEntityType" = proto.Field(
        proto.ENUM,
        number=4,
        enum="DatabaseEntityType",
    )
    issue_id: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=100,
    )


class EntityIssue(proto.Message):
    r"""Issue related to the entity.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        id (str):
            Unique Issue ID.
        type_ (google.cloud.clouddms_v1.types.EntityIssue.IssueType):
            The type of the issue.
        severity (google.cloud.clouddms_v1.types.EntityIssue.IssueSeverity):
            Severity of the issue
        message (str):
            Issue detailed message
        code (str):
            Error/Warning code
        ddl (str):
            The ddl which caused the issue, if relevant.

            This field is a member of `oneof`_ ``_ddl``.
        position (google.cloud.clouddms_v1.types.EntityIssue.Position):
            The position of the issue found, if relevant.

            This field is a member of `oneof`_ ``_position``.
        entity_type (google.cloud.clouddms_v1.types.DatabaseEntityType):
            The entity type (if the DDL is for a sub
            entity).
    """

    class IssueType(proto.Enum):
        r"""Type of issue.

        Values:
            ISSUE_TYPE_UNSPECIFIED (0):
                Unspecified issue type.
            ISSUE_TYPE_DDL (1):
                Issue originated from the DDL
            ISSUE_TYPE_APPLY (2):
                Issue originated during the apply process
            ISSUE_TYPE_CONVERT (3):
                Issue originated during the convert process
        """

        ISSUE_TYPE_UNSPECIFIED = 0
        ISSUE_TYPE_DDL = 1
        ISSUE_TYPE_APPLY = 2
        ISSUE_TYPE_CONVERT = 3

    class IssueSeverity(proto.Enum):
        r"""Severity of issue.

        Values:
            ISSUE_SEVERITY_UNSPECIFIED (0):
                Unspecified issue severity
            ISSUE_SEVERITY_INFO (1):
                Info
            ISSUE_SEVERITY_WARNING (2):
                Warning
            ISSUE_SEVERITY_ERROR (3):
                Error
        """

        ISSUE_SEVERITY_UNSPECIFIED = 0
        ISSUE_SEVERITY_INFO = 1
        ISSUE_SEVERITY_WARNING = 2
        ISSUE_SEVERITY_ERROR = 3

    class Position(proto.Message):
        r"""Issue position.

        Attributes:
            line (int):
                Issue line number
            column (int):
                Issue column number
            offset (int):
                Issue offset
            length (int):
                Issue length
        """

        line: int = proto.Field(
            proto.INT32,
            number=1,
        )
        column: int = proto.Field(
            proto.INT32,
            number=2,
        )
        offset: int = proto.Field(
            proto.INT32,
            number=3,
        )
        length: int = proto.Field(
            proto.INT32,
            number=4,
        )

    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_: IssueType = proto.Field(
        proto.ENUM,
        number=2,
        enum=IssueType,
    )
    severity: IssueSeverity = proto.Field(
        proto.ENUM,
        number=3,
        enum=IssueSeverity,
    )
    message: str = proto.Field(
        proto.STRING,
        number=4,
    )
    code: str = proto.Field(
        proto.STRING,
        number=5,
    )
    ddl: str = proto.Field(
        proto.STRING,
        number=6,
        optional=True,
    )
    position: Position = proto.Field(
        proto.MESSAGE,
        number=7,
        optional=True,
        message=Position,
    )
    entity_type: "DatabaseEntityType" = proto.Field(
        proto.ENUM,
        number=8,
        enum="DatabaseEntityType",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
