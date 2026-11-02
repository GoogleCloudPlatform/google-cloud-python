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
    package="google.cloud.dataplex.v1",
    manifest={
        "DataDocumentationSpec",
        "DataDocumentationResult",
    },
)


class DataDocumentationSpec(proto.Message):
    r"""DataDocumentation scan related spec.

    Attributes:
        catalog_publishing_enabled (bool):
            Optional. Whether to publish result to
            Dataplex Catalog.
        generation_scopes (MutableSequence[google.cloud.dataplex_v1.types.DataDocumentationSpec.GenerationScope]):
            Optional. Specifies which components of the
            data documentation to generate. Any component
            that is required to generate the specified
            components will also be generated. If no
            generation scope is specified, all available
            documentation components will be generated.
    """

    class GenerationScope(proto.Enum):
        r"""The data documentation generation scope. This field contains
        the possible components of a data documentation scan which can
        be selectively generated.

        Values:
            GENERATION_SCOPE_UNSPECIFIED (0):
                Unspecified generation scope. If no
                generation scope is specified, all available
                documentation components will be generated.
            ALL (1):
                All the possible results will be generated.
            TABLE_AND_COLUMN_DESCRIPTIONS (2):
                Table and column descriptions will be
                generated.
            SQL_QUERIES (3):
                SQL queries will be generated.
        """

        GENERATION_SCOPE_UNSPECIFIED = 0
        ALL = 1
        TABLE_AND_COLUMN_DESCRIPTIONS = 2
        SQL_QUERIES = 3

    catalog_publishing_enabled: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    generation_scopes: MutableSequence[GenerationScope] = proto.RepeatedField(
        proto.ENUM,
        number=3,
        enum=GenerationScope,
    )


class DataDocumentationResult(proto.Message):
    r"""The output of a DataDocumentation scan.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        dataset_result (google.cloud.dataplex_v1.types.DataDocumentationResult.DatasetResult):
            Output only. Insights for a Dataset resource.

            This field is a member of `oneof`_ ``result``.
        table_result (google.cloud.dataplex_v1.types.DataDocumentationResult.TableResult):
            Output only. Insights for a Table resource.

            This field is a member of `oneof`_ ``result``.
    """

    class DatasetResult(proto.Message):
        r"""Insights for a dataset resource.

        Attributes:
            overview (str):
                Output only. Generated Dataset description.
            schema_relationships (MutableSequence[google.cloud.dataplex_v1.types.DataDocumentationResult.SchemaRelationship]):
                Output only. Relationships suggesting how
                tables in the dataset are related to each other,
                based on their schema.
            queries (MutableSequence[google.cloud.dataplex_v1.types.DataDocumentationResult.Query]):
                Output only. Sample SQL queries for the
                dataset.
        """

        overview: str = proto.Field(
            proto.STRING,
            number=1,
        )
        schema_relationships: MutableSequence[
            "DataDocumentationResult.SchemaRelationship"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message="DataDocumentationResult.SchemaRelationship",
        )
        queries: MutableSequence["DataDocumentationResult.Query"] = proto.RepeatedField(
            proto.MESSAGE,
            number=4,
            message="DataDocumentationResult.Query",
        )

    class TableResult(proto.Message):
        r"""Insights for a table resource.

        Attributes:
            name (str):
                Output only. The service-qualified full resource name of the
                cloud resource. Ex:
                //bigquery.googleapis.com/projects/PROJECT_ID/datasets/DATASET_ID/tables/TABLE_ID
            overview (str):
                Output only. Generated description of the
                table.
            schema (google.cloud.dataplex_v1.types.DataDocumentationResult.Schema):
                Output only. Schema of the table with
                generated metadata of the columns in the schema.
            queries (MutableSequence[google.cloud.dataplex_v1.types.DataDocumentationResult.Query]):
                Output only. Sample SQL queries for the
                table.
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        overview: str = proto.Field(
            proto.STRING,
            number=2,
        )
        schema: "DataDocumentationResult.Schema" = proto.Field(
            proto.MESSAGE,
            number=3,
            message="DataDocumentationResult.Schema",
        )
        queries: MutableSequence["DataDocumentationResult.Query"] = proto.RepeatedField(
            proto.MESSAGE,
            number=4,
            message="DataDocumentationResult.Query",
        )

    class SchemaRelationship(proto.Message):
        r"""Details of the relationship between the schema of two
        resources.

        Attributes:
            left_schema_paths (google.cloud.dataplex_v1.types.DataDocumentationResult.SchemaRelationship.SchemaPaths):
                Output only. An ordered list of fields for the join from the
                first table. The size of this list must be the same as
                ``right_schema_paths``. Each field at index i in this list
                must correspond to a field at the same index in the
                ``right_schema_paths`` list.
            right_schema_paths (google.cloud.dataplex_v1.types.DataDocumentationResult.SchemaRelationship.SchemaPaths):
                Output only. An ordered list of fields for the join from the
                second table. The size of this list must be the same as
                ``left_schema_paths``. Each field at index i in this list
                must correspond to a field at the same index in the
                ``left_schema_paths`` list.
            sources (MutableSequence[google.cloud.dataplex_v1.types.DataDocumentationResult.SchemaRelationship.Source]):
                Output only. Sources which generated the
                schema relation edge.
            type_ (google.cloud.dataplex_v1.types.DataDocumentationResult.SchemaRelationship.Type):
                Output only. The type of relationship between
                the schema paths.
        """

        class Source(proto.Enum):
            r"""Source which generated the schema relation edge.

            Values:
                SOURCE_UNSPECIFIED (0):
                    The source of the schema relationship is
                    unspecified.
                AGENT (4):
                    The source of the schema relationship is
                    agent.
                QUERY_HISTORY (5):
                    The source of the schema relationship is
                    query history from the source system.
                TABLE_CONSTRAINTS (6):
                    The source of the schema relationship is
                    table constraints added in the source system.
            """

            SOURCE_UNSPECIFIED = 0
            AGENT = 4
            QUERY_HISTORY = 5
            TABLE_CONSTRAINTS = 6

        class Type(proto.Enum):
            r"""The type of relationship.

            Values:
                TYPE_UNSPECIFIED (0):
                    The type of the schema relationship is
                    unspecified.
                SCHEMA_JOIN (1):
                    Indicates a join relationship between the
                    schema fields.
            """

            TYPE_UNSPECIFIED = 0
            SCHEMA_JOIN = 1

        class SchemaPaths(proto.Message):
            r"""Represents an ordered set of paths within a table's schema.

            Attributes:
                table_fqn (str):
                    Output only. The service-qualified full resource name of the
                    table Ex:
                    //bigquery.googleapis.com/projects/PROJECT_ID/datasets/DATASET_ID/tables/TABLE_ID
                paths (MutableSequence[str]):
                    Output only. An ordered set of Paths to fields within the
                    schema of the table. For fields nested within a top level
                    field of type record, use '.' to separate field names.
                    Examples: Top level field - ``top_level`` Nested field -
                    ``top_level.child.sub_field``
            """

            table_fqn: str = proto.Field(
                proto.STRING,
                number=1,
            )
            paths: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=2,
            )

        left_schema_paths: "DataDocumentationResult.SchemaRelationship.SchemaPaths" = (
            proto.Field(
                proto.MESSAGE,
                number=1,
                message="DataDocumentationResult.SchemaRelationship.SchemaPaths",
            )
        )
        right_schema_paths: "DataDocumentationResult.SchemaRelationship.SchemaPaths" = (
            proto.Field(
                proto.MESSAGE,
                number=2,
                message="DataDocumentationResult.SchemaRelationship.SchemaPaths",
            )
        )
        sources: MutableSequence[
            "DataDocumentationResult.SchemaRelationship.Source"
        ] = proto.RepeatedField(
            proto.ENUM,
            number=4,
            enum="DataDocumentationResult.SchemaRelationship.Source",
        )
        type_: "DataDocumentationResult.SchemaRelationship.Type" = proto.Field(
            proto.ENUM,
            number=6,
            enum="DataDocumentationResult.SchemaRelationship.Type",
        )

    class Query(proto.Message):
        r"""A sample SQL query in data documentation.

        Attributes:
            sql (str):
                Output only. The SQL query string which can
                be executed.
            description (str):
                Output only. The description for the query.
        """

        sql: str = proto.Field(
            proto.STRING,
            number=1,
        )
        description: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class Schema(proto.Message):
        r"""Schema of the table with generated metadata of columns.

        Attributes:
            fields (MutableSequence[google.cloud.dataplex_v1.types.DataDocumentationResult.Field]):
                Output only. The list of columns.
        """

        fields: MutableSequence["DataDocumentationResult.Field"] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="DataDocumentationResult.Field",
        )

    class Field(proto.Message):
        r"""Column of a table with generated metadata and nested fields.

        Attributes:
            name (str):
                Output only. The name of the column.
            description (str):
                Output only. Generated description for
                columns and fields.
            fields (MutableSequence[google.cloud.dataplex_v1.types.DataDocumentationResult.Field]):
                Output only. Nested fields.
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        description: str = proto.Field(
            proto.STRING,
            number=2,
        )
        fields: MutableSequence["DataDocumentationResult.Field"] = proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message="DataDocumentationResult.Field",
        )

    dataset_result: DatasetResult = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="result",
        message=DatasetResult,
    )
    table_result: TableResult = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="result",
        message=TableResult,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
