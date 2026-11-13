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

import google.protobuf.wrappers_pb2 as wrappers_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.geminidataanalytics_v1alpha.types import datasource as gcg_datasource

__protobuf__ = proto.module(
    package="google.cloud.geminidataanalytics.v1alpha",
    manifest={
        "Context",
        "UserFunctions",
        "BigQueryRoutine",
        "BigQueryRoutineReference",
        "ExampleQuery",
        "QueryParameter",
        "MatchedQuery",
        "QueryParameterValues",
        "LookerGoldenQuery",
        "DynamicField",
        "LookerQuery",
        "GlossaryTerm",
        "ConversationOptions",
        "DatasourceOptions",
        "ChartOptions",
        "AnalysisOptions",
        "Citation",
        "CitationSource",
        "CitationAnchor",
    },
)


class Context(proto.Message):
    r"""A collection of context to apply to this conversation

    Attributes:
        system_instruction (str):
            Optional. The basic entry point for data
            owners creating domain knowledge for Agent.

            Why: Business jargon (e.g., YTD revenue is
            calculated as…, Retirement Age is 65 in the USA,
            etc) and system instructions (e.g., answer like
            a Pirate) can help the model understand the
            business context around a user question.

            Must be at most 250,000 bytes (approx. 250,000
            characters for English text).
        datasource_references (google.cloud.geminidataanalytics_v1alpha.types.DatasourceReferences):
            Required. Data sources that are available for
            answering the question.
        options (google.cloud.geminidataanalytics_v1alpha.types.ConversationOptions):
            Optional. Additional options for the
            conversation.
        example_queries (MutableSequence[google.cloud.geminidataanalytics_v1alpha.types.ExampleQuery]):
            Optional. A list of example queries,
            providing examples of relevant and commonly used
            SQL queries and their corresponding natural
            language queries optionally present. Currently
            only used for BigQuery data sources and
            databases (alloydb, cloudsql, spanner) data
            sources.
        looker_golden_queries (MutableSequence[google.cloud.geminidataanalytics_v1alpha.types.LookerGoldenQuery]):
            Optional. A list of golden queries, providing
            examples of relevant and commonly used Looker
            queries and their corresponding natural language
            queries optionally present. Only supported for
            Looker data sources.
        glossary_terms (MutableSequence[google.cloud.geminidataanalytics_v1alpha.types.GlossaryTerm]):
            Optional. Term definitions (currently, only
            user authored) Not supported for databases
            (alloydb, cloudsql, spanner) data sources.
        schema_relationships (MutableSequence[google.cloud.geminidataanalytics_v1alpha.types.Context.SchemaRelationship]):
            Optional. Relationships between table schema,
            including referencing and referenced columns.
        user_functions (google.cloud.geminidataanalytics_v1alpha.types.UserFunctions):
            Optional. A collection of user functions to
            be included in context.
    """

    class SchemaRelationship(proto.Message):
        r"""The relationship between two tables, including referencing
        and referenced columns. This is a derived context retrieved from
        Dataplex Dataset Insights.

        Attributes:
            left_schema_paths (google.cloud.geminidataanalytics_v1alpha.types.Context.SchemaRelationship.SchemaPaths):
                An ordered list of fields for the join from the first table.
                The size of this list must be the same as
                ``right_schema_paths``. Each field at index i in this list
                must correspond to a field at the same index in the
                ``right_schema_paths`` list.
            right_schema_paths (google.cloud.geminidataanalytics_v1alpha.types.Context.SchemaRelationship.SchemaPaths):
                An ordered list of fields for the join from the second
                table. The size of this list must be the same as
                ``left_schema_paths``. Each field at index i in this list
                must correspond to a field at the same index in the
                ``left_schema_paths`` list.
            sources (MutableSequence[google.cloud.geminidataanalytics_v1alpha.types.Context.SchemaRelationship.Source]):
                Optional. Sources which generated the schema
                relation edge.
            confidence_score (float):
                Optional. A confidence score for the
                suggested relationship. Manually added edges
                have the highest confidence score.
        """

        class Source(proto.Enum):
            r"""Source which generated the schema relation edge.

            Values:
                SOURCE_UNSPECIFIED (0):
                    The source of the schema relationship is
                    unspecified.
                BIGQUERY_JOB_HISTORY (1):
                    The source of the schema relationship is
                    BigQuery job history.
                LLM_SUGGESTED (2):
                    The source of the schema relationship is LLM
                    suggested.
                BIGQUERY_TABLE_CONSTRAINTS (3):
                    The source of the schema relationship is
                    BigQuery table constraints.
            """

            SOURCE_UNSPECIFIED = 0
            BIGQUERY_JOB_HISTORY = 1
            LLM_SUGGESTED = 2
            BIGQUERY_TABLE_CONSTRAINTS = 3

        class SchemaPaths(proto.Message):
            r"""Represents an ordered set of paths within the table schema.

            Attributes:
                table_fqn (str):
                    The service-qualified full resource name of the table Ex:
                    bigquery.googleapis.com/projects/PROJECT_ID/datasets/DATASET_ID/tables/TABLE_ID
                paths (MutableSequence[str]):
                    The ordered list of paths within the table
                    schema.
            """

            table_fqn: str = proto.Field(
                proto.STRING,
                number=1,
            )
            paths: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=2,
            )

        left_schema_paths: "Context.SchemaRelationship.SchemaPaths" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="Context.SchemaRelationship.SchemaPaths",
        )
        right_schema_paths: "Context.SchemaRelationship.SchemaPaths" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="Context.SchemaRelationship.SchemaPaths",
        )
        sources: MutableSequence["Context.SchemaRelationship.Source"] = (
            proto.RepeatedField(
                proto.ENUM,
                number=3,
                enum="Context.SchemaRelationship.Source",
            )
        )
        confidence_score: float = proto.Field(
            proto.FLOAT,
            number=4,
        )

    system_instruction: str = proto.Field(
        proto.STRING,
        number=1,
    )
    datasource_references: gcg_datasource.DatasourceReferences = proto.Field(
        proto.MESSAGE,
        number=7,
        message=gcg_datasource.DatasourceReferences,
    )
    options: "ConversationOptions" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="ConversationOptions",
    )
    example_queries: MutableSequence["ExampleQuery"] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message="ExampleQuery",
    )
    looker_golden_queries: MutableSequence["LookerGoldenQuery"] = proto.RepeatedField(
        proto.MESSAGE,
        number=11,
        message="LookerGoldenQuery",
    )
    glossary_terms: MutableSequence["GlossaryTerm"] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message="GlossaryTerm",
    )
    schema_relationships: MutableSequence[SchemaRelationship] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message=SchemaRelationship,
    )
    user_functions: "UserFunctions" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="UserFunctions",
    )


class UserFunctions(proto.Message):
    r"""A collection of user functions to be included in context.

    Attributes:
        bq_routines (MutableSequence[google.cloud.geminidataanalytics_v1alpha.types.BigQueryRoutine]):
            A list of BigQuery routines to include in the
            context.
    """

    bq_routines: MutableSequence["BigQueryRoutine"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="BigQueryRoutine",
    )


class BigQueryRoutine(proto.Message):
    r"""A reference to a BigQuery routine.

    Attributes:
        routine_reference (google.cloud.geminidataanalytics_v1alpha.types.BigQueryRoutineReference):
            The reference to the BigQuery routine.
        description (str):
            User override or addition to description, to
            tell the agent when to use the UDF.
    """

    routine_reference: "BigQueryRoutineReference" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="BigQueryRoutineReference",
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )


class BigQueryRoutineReference(proto.Message):
    r"""A reference to a BigQuery routine.

    Attributes:
        project_id (str):
            The project ID of the routine.
        dataset_id (str):
            The dataset ID of the routine.
        routine_id (str):
            The routine ID of the routine.
    """

    project_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    dataset_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    routine_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ExampleQuery(proto.Message):
    r"""Example of relevant and commonly used SQL query and its
    corresponding natural language queries optionally present.
    Currently only used for BigQuery data sources.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        sql_query (str):
            Optional. The SQL query that should be generated to answer
            the natural language question. For example: "SELECT
            COUNT(\*) FROM orders WHERE order_date BETWEEN '2024-01-01'
            AND '2024-01-31'"

            Must be at most 50,000 bytes (approx. 50,000 characters).

            This field is a member of `oneof`_ ``query``.
        natural_language_question (str):
            Optional. A natural language question that a
            user might ask. For example: "How many orders
            were placed last month?"

            Must be at most 2,000 bytes (approx. 2,000
            characters).
        parameters (MutableSequence[google.cloud.geminidataanalytics_v1alpha.types.QueryParameter]):
            Optional. The list of query parameters. Example: The
            parameterized SQL query "SELECT \* FROM my_table WHERE id =
            @id" can be matched with any value of id.
    """

    sql_query: str = proto.Field(
        proto.STRING,
        number=101,
        oneof="query",
    )
    natural_language_question: str = proto.Field(
        proto.STRING,
        number=1,
    )
    parameters: MutableSequence["QueryParameter"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="QueryParameter",
    )


class QueryParameter(proto.Message):
    r"""A query parameter message represents a parameter that can be
    used to parameterize a SQL query.

    Attributes:
        name (str):
            Required. The name of the parameter reference
            in the SQL query.
        description (str):
            Optional. The description of the parameter
            that can be used by LLM to extract the parameter
            value from the user question.
        data_type (str):
            Required. The data type of the parameter, e.g. "STRING",
            "INT64", "DATE", etc. For valid values, see the `BigQuery
            documentation <https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types>`__.
            This will be used to populate
            google.cloud.bigquery.v2.QueryParameterType.type.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    data_type: str = proto.Field(
        proto.STRING,
        number=3,
    )


class MatchedQuery(proto.Message):
    r"""A matched query message represents the agent having matched
    one of the example queries supplied in context as being
    applicable to the current question. It will also contain
    additional info during the matching process.

    Attributes:
        example_query (google.cloud.geminidataanalytics_v1alpha.types.ExampleQuery):
            The query that was matched based on an
            example query.
        query_parameter_values (MutableSequence[google.cloud.geminidataanalytics_v1alpha.types.QueryParameterValues]):
            The extracted values for the query
            parameters.
    """

    example_query: "ExampleQuery" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="ExampleQuery",
    )
    query_parameter_values: MutableSequence["QueryParameterValues"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="QueryParameterValues",
        )
    )


class QueryParameterValues(proto.Message):
    r"""A query parameter values message represents the values for
    the query parameters that were extracted from the user question
    by LLM, based on the example query.

    Attributes:
        name (str):
            Required. The name of the parameter.
        value (str):
            Required. The value of the parameter.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    value: str = proto.Field(
        proto.STRING,
        number=2,
    )


class LookerGoldenQuery(proto.Message):
    r"""A golden query for Looker, including natural language
    questions and a corresponding Looker Query. Analogous to
    ExampleQuery.

    Attributes:
        natural_language_questions (MutableSequence[str]):
            Optional. Natural language questions that a
            user might ask. For example: "How many orders
            were placed last month?"

            Must be at most 2,000 bytes per question
            (approx. 2,000 characters).
        looker_query (google.cloud.geminidataanalytics_v1alpha.types.LookerQuery):
            Optional. The Looker Query corresponding to
            the natural language questions.
    """

    natural_language_questions: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    looker_query: "LookerQuery" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="LookerQuery",
    )


class DynamicField(proto.Message):
    r"""A dynamic field in Looker (Custom Dimension, Custom Measure,
    or Table Calculation).


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        category (str):
            Optional. The type of dynamic field: dimension, measure,
            table_calculation. Looker can use the category type to
            specify the name of the dynamic field. However, Looker
            Conversational Analytics keeps the category separate from
            the name of the dynamic field. For more details, see
            https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard-table-chart#dynamic_fields.

            This field is a member of `oneof`_ ``_category``.
        name (str):
            Optional. The name of the dynamic field in
            LookML.

            This field is a member of `oneof`_ ``_name``.
        label (str):
            Optional. The label defines the display name
            of the dynamic field.

            This field is a member of `oneof`_ ``_label``.
        based_on (str):
            Optional. For custom measures, this
            identifies the measure the field is based on.

            This field is a member of `oneof`_ ``_based_on``.
        type_ (str):
            Optional. For custom measures, this
            identifies the type of aggregation (e.g. sum).

            This field is a member of `oneof`_ ``_type``.
        description (str):
            Optional. Description of the dynamic field.

            This field is a member of `oneof`_ ``_description``.
        expression (str):
            Optional. Looker expression to create a table
            calculation.

            This field is a member of `oneof`_ ``_expression``.
        filter_expression (str):
            Optional. Looker expression to filter a base
            measure.

            This field is a member of `oneof`_ ``_filter_expression``.
        value_format (str):
            Optional. Value format for the dynamic field.

            This field is a member of `oneof`_ ``_value_format``.
        value_format_name (str):
            Optional. Value format name for the dynamic
            field if using a default named format.

            This field is a member of `oneof`_ ``_value_format_name``.
        calculation_type (str):
            Optional. Calculation type for table calculations. Refer to
            https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard-table-chart#calculation_type
            for all possible values depending on the ``category`` of
            dynamic field.

            This field is a member of `oneof`_ ``_calculation_type``.
        args (MutableSequence[str]):
            Optional. Arguments for custom groups, custom bins, or
            shortcut calculations. For more details, refer to
            https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard-table-chart#args_for_custom_groups
        kind_hint (str):
            Optional. Identifies whether the dynamic
            field returns a dimension or measure.

            This field is a member of `oneof`_ ``_kind_hint``.
        type_hint (str):
            Optional. Identifies the data type the
            dynamic field's expression should produce.

            This field is a member of `oneof`_ ``_type_hint``.
        is_disabled (bool):
            Optional. Whether the dynamic field is
            disabled.

            This field is a member of `oneof`_ ``_is_disabled``.
    """

    category: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    name: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    label: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    based_on: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )
    type_: str = proto.Field(
        proto.STRING,
        number=5,
        optional=True,
    )
    description: str = proto.Field(
        proto.STRING,
        number=6,
        optional=True,
    )
    expression: str = proto.Field(
        proto.STRING,
        number=7,
        optional=True,
    )
    filter_expression: str = proto.Field(
        proto.STRING,
        number=8,
        optional=True,
    )
    value_format: str = proto.Field(
        proto.STRING,
        number=9,
        optional=True,
    )
    value_format_name: str = proto.Field(
        proto.STRING,
        number=10,
        optional=True,
    )
    calculation_type: str = proto.Field(
        proto.STRING,
        number=11,
        optional=True,
    )
    args: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=12,
    )
    kind_hint: str = proto.Field(
        proto.STRING,
        number=13,
        optional=True,
    )
    type_hint: str = proto.Field(
        proto.STRING,
        number=14,
        optional=True,
    )
    is_disabled: bool = proto.Field(
        proto.BOOL,
        number=15,
        optional=True,
    )


class LookerQuery(proto.Message):
    r"""Looker Query Object `Looker API
    documentation <https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/Query/run_inline_query>`__.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        model (str):
            Required. The LookML model used to generate
            the query.
        explore (str):
            Required. The LookML explore used to generate
            the query.
        fields (MutableSequence[str]):
            Optional. The fields to retrieve from the
            explore.
        filters (MutableSequence[google.cloud.geminidataanalytics_v1alpha.types.LookerQuery.Filter]):
            Optional. The filters to apply to the
            explore.
        sorts (MutableSequence[str]):
            Optional. The sorts to apply to the explore.
        limit (str):
            Optional. Limit in the query.

            This field is a member of `oneof`_ ``_limit``.
        dynamic_fields (MutableSequence[google.cloud.geminidataanalytics_v1alpha.types.DynamicField]):
            Optional. The dynamic fields used in the
            query.
        query_id (str):
            Optional. The primary identifier for the query resource in
            Looker, used for API operations. Maps to ``id`` (or
            ``slug``) in the Looker API ``Query`` resource.

            This field is a member of `oneof`_ ``_query_id``.
        client_id (str):
            Optional. The short alphanumeric identifier for the query,
            used for share links and Explore URLs (e.g., in the ``qid``
            parameter). Maps to ``client_id`` in the Looker API
            ``Query`` resource.

            This field is a member of `oneof`_ ``_client_id``.
    """

    class Filter(proto.Message):
        r"""A Looker query filter.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            field (str):
                Required. The field to filter on.
            value (str):
                Optional. The value for the field to filter
                on. Optional so we can preserve the default
                value as an empty string, important to get a
                valid and working Looker Explore url.

                This field is a member of `oneof`_ ``_value``.
        """

        field: str = proto.Field(
            proto.STRING,
            number=1,
        )
        value: str = proto.Field(
            proto.STRING,
            number=2,
            optional=True,
        )

    model: str = proto.Field(
        proto.STRING,
        number=1,
    )
    explore: str = proto.Field(
        proto.STRING,
        number=2,
    )
    fields: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    filters: MutableSequence[Filter] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=Filter,
    )
    sorts: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    limit: str = proto.Field(
        proto.STRING,
        number=6,
        optional=True,
    )
    dynamic_fields: MutableSequence["DynamicField"] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message="DynamicField",
    )
    query_id: str = proto.Field(
        proto.STRING,
        number=10,
        optional=True,
    )
    client_id: str = proto.Field(
        proto.STRING,
        number=11,
        optional=True,
    )


class GlossaryTerm(proto.Message):
    r"""Definition of a term within a specific domain.

    Attributes:
        display_name (str):
            Required. User friendly display name of the
            glossary term being defined. For example: "CTR",
            "conversion rate", "pending"

            Must be at most 256 bytes.
        description (str):
            Required. The description or meaning of the
            term. For example: "Click-through rate", "The
            percentage of users who complete a desired
            action", "An order that is waiting to be
            processed."

            Must be at most 5,000 bytes (approx. 5,000
            characters).
        labels (MutableSequence[str]):
            Optional. A list of general purpose labels associated to
            this term. For example: ["click rate", "clickthrough",
            "waiting"]
    """

    display_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    labels: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class ConversationOptions(proto.Message):
    r"""Options for the conversation.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        chart (google.cloud.geminidataanalytics_v1alpha.types.ChartOptions):
            Optional. Options for chart generation.
        analysis (google.cloud.geminidataanalytics_v1alpha.types.AnalysisOptions):
            Optional. Options for analysis.
        datasource (google.cloud.geminidataanalytics_v1alpha.types.DatasourceOptions):
            Optional. Options for datasources.
        model (google.cloud.geminidataanalytics_v1alpha.types.ConversationOptions.Model):
            Optional. The model to use for the agent
            loop.

            This field is a member of `oneof`_ ``_model``.
    """

    class Model(proto.Enum):
        r"""Allowed models for the agent/conversation.

        Values:
            MODEL_UNSPECIFIED (0):
                No model specified. The model may be set on
                the chat request, or the default model will be
                used.
            LATEST_GA_MODEL (1):
                Use the most up-to-date non-preview model.
                This may constrain certain request level
                settings.
        """

        MODEL_UNSPECIFIED = 0
        LATEST_GA_MODEL = 1

    chart: "ChartOptions" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="ChartOptions",
    )
    analysis: "AnalysisOptions" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="AnalysisOptions",
    )
    datasource: "DatasourceOptions" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="DatasourceOptions",
    )
    model: Model = proto.Field(
        proto.ENUM,
        number=6,
        optional=True,
        enum=Model,
    )


class DatasourceOptions(proto.Message):
    r"""Options for datasources configurations.

    Attributes:
        big_query_max_billed_bytes (google.protobuf.wrappers_pb2.Int64Value):
            Optional. This option applies to datasources
            that require BigQuery queries only. Limits the
            bytes billed for each BQ query job. Queries that
            will have bytes billed beyond this limit will
            fail (without incurring a charge). If
            unspecified, no limit will be applied.
    """

    big_query_max_billed_bytes: wrappers_pb2.Int64Value = proto.Field(
        proto.MESSAGE,
        number=1,
        message=wrappers_pb2.Int64Value,
    )


class ChartOptions(proto.Message):
    r"""Options for chart generation.

    Attributes:
        image (google.cloud.geminidataanalytics_v1alpha.types.ChartOptions.ImageOptions):
            Optional. When specified, the agent will
            render generated charts using the provided
            format. Defaults to no image.
    """

    class ImageOptions(proto.Message):
        r"""Options for rendering images of generated charts.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            no_image (google.cloud.geminidataanalytics_v1alpha.types.ChartOptions.ImageOptions.NoImage):
                No image.

                This field is a member of `oneof`_ ``kind``.
            svg (google.cloud.geminidataanalytics_v1alpha.types.ChartOptions.ImageOptions.SvgOptions):
                SVG format.

                This field is a member of `oneof`_ ``kind``.
        """

        class NoImage(proto.Message):
            r"""No image."""

        class SvgOptions(proto.Message):
            r"""SVG options."""

        no_image: "ChartOptions.ImageOptions.NoImage" = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="kind",
            message="ChartOptions.ImageOptions.NoImage",
        )
        svg: "ChartOptions.ImageOptions.SvgOptions" = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="kind",
            message="ChartOptions.ImageOptions.SvgOptions",
        )

    image: ImageOptions = proto.Field(
        proto.MESSAGE,
        number=1,
        message=ImageOptions,
    )


class AnalysisOptions(proto.Message):
    r"""Options for analysis.

    Attributes:
        python (google.cloud.geminidataanalytics_v1alpha.types.AnalysisOptions.Python):
            Optional. Options for Python analysis.
    """

    class Python(proto.Message):
        r"""Options for Python analysis.

        Attributes:
            enabled (bool):
                Optional. Whether to enable Python analysis.
                Defaults to false.
        """

        enabled: bool = proto.Field(
            proto.BOOL,
            number=1,
        )

    python: Python = proto.Field(
        proto.MESSAGE,
        number=1,
        message=Python,
    )


class Citation(proto.Message):
    r"""Source attributions for content.

    Attributes:
        sources (MutableSequence[google.cloud.geminidataanalytics_v1alpha.types.CitationSource]):
            Output only. List of the sources being cited.
        anchors (MutableSequence[google.cloud.geminidataanalytics_v1alpha.types.CitationAnchor]):
            Output only. List of the anchors of the
            citations.
    """

    sources: MutableSequence["CitationSource"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="CitationSource",
    )
    anchors: MutableSequence["CitationAnchor"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="CitationAnchor",
    )


class CitationSource(proto.Message):
    r"""The source of the citation.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        uri (str):
            Output only. The uri used as the source, such
            as a web grounding URL.

            This field is a member of `oneof`_ ``source_type``.
        example_query (google.cloud.geminidataanalytics_v1alpha.types.ExampleQuery):
            Output only. The example query used as the
            source.

            This field is a member of `oneof`_ ``source_type``.
        glossary_term (google.cloud.geminidataanalytics_v1alpha.types.GlossaryTerm):
            Output only. The glossary term used as the
            source.

            This field is a member of `oneof`_ ``source_type``.
        id (str):
            Output only. Unique identifier of the source. This ID is
            service-generated and is unique within the scope of a single
            ``Citation`` message.
        title (str):
            Output only. The title of the source.
    """

    uri: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="source_type",
    )
    example_query: "ExampleQuery" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="source_type",
        message="ExampleQuery",
    )
    glossary_term: "GlossaryTerm" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="source_type",
        message="GlossaryTerm",
    )
    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    title: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CitationAnchor(proto.Message):
    r"""The anchor of the citation.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        text_message_anchor (google.cloud.geminidataanalytics_v1alpha.types.CitationAnchor.TextMessageCitationAnchor):
            Output only. Only set if the citation is for
            a TextMessage.

            This field is a member of `oneof`_ ``anchor_type``.
    """

    class TextMessageCitationAnchor(proto.Message):
        r"""Citation anchor within a TextMessage.

        Attributes:
            part_index (int):
                Output only. The 0-based index of the part
                within the TextMessage.parts field.
            start_offset_bytes (int):
                Output only. The offset, measured in UTF-8
                bytes, within the part string where the citation
                begins (inclusive). Example: For the text
                "Hello, world" where "world" is cited, the start
                offset bytes (inclusive) is 7 and the end offset
                bytes (exclusive) is 12.
            end_offset_bytes (int):
                Output only. The offset, measured in UTF-8
                bytes, within the part string where the citation
                ends (exclusive). Example: For the text "Hello,
                world" where "world" is cited, the start offset
                bytes (inclusive) is 7 and the end offset bytes
                (exclusive) is 12.
            source_ids (MutableSequence[str]):
                Output only. The ids of the sources that are
                cited.
        """

        part_index: int = proto.Field(
            proto.INT32,
            number=1,
        )
        start_offset_bytes: int = proto.Field(
            proto.INT32,
            number=2,
        )
        end_offset_bytes: int = proto.Field(
            proto.INT32,
            number=3,
        )
        source_ids: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=4,
        )

    text_message_anchor: TextMessageCitationAnchor = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="anchor_type",
        message=TextMessageCitationAnchor,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
