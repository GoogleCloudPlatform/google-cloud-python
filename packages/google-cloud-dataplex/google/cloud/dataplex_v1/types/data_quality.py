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

from google.cloud.dataplex_v1.types import (
    data_quality_rule_template,
    datascans_common,
    processing,
)

__protobuf__ = proto.module(
    package="google.cloud.dataplex.v1",
    manifest={
        "DataQualitySpec",
        "DataQualityResult",
        "DataQualityRuleResult",
        "DataQualityDimensionResult",
        "DataQualityDimension",
        "DataQualityRule",
        "DataQualityColumnResult",
    },
)


class DataQualitySpec(proto.Message):
    r"""DataQualityScan related setting.

    Attributes:
        rules (MutableSequence[google.cloud.dataplex_v1.types.DataQualityRule]):
            Required. The list of rules to evaluate
            against a data source. At least one rule is
            required.
        sampling_percent (float):
            Optional. The percentage of the records to be selected from
            the dataset for DataScan.

            - Value can range between 0.0 and 100.0 with up to 3
              significant decimal digits.
            - Sampling is not applied if ``sampling_percent`` is not
              specified, 0 or

            100.
        row_filter (str):
            Optional. A filter applied to all rows in a single DataScan
            job. The filter needs to be a valid SQL expression for a
            `WHERE clause in GoogleSQL
            syntax <https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax#where_clause>`__.

            Example: col1 >= 0 AND col2 < 10
        post_scan_actions (google.cloud.dataplex_v1.types.DataQualitySpec.PostScanActions):
            Optional. Actions to take upon job
            completion.
        catalog_publishing_enabled (bool):
            Optional. If set, the latest DataScan job
            result will be published as Dataplex Universal
            Catalog metadata.
        enable_catalog_based_rules (bool):
            Optional. If enabled, the data scan will
            retrieve rules defined in the
            dataplex-types.global.data-rules aspect on all
            paths of the catalog entry corresponding to the
            BigQuery table resource and all attached
            glossary terms. The path that data-rules aspect
            is attached on the table entry defines the
            column that the rule will be evaluated against.
            For glossary terms, the path that the terms are
            attached on the table entry defines the column
            that the rule will be evaluated against. At the
            start of scan execution, the rules reflect the
            latest state retrieved from the catalog entry
            and any updates on the rules thereafter are
            ignored for that execution. The updates will be
            reflected from the next execution. Rules defined
            in the datascan must be empty if this field is
            enabled.
        filter (str):
            Optional. Filter for selectively running a subset of rules.
            You can filter the request by the name or attribute
            key-value pairs defined on the rule. If not specified, all
            rules are run. The filter is applicable to both, the rules
            retrieved from catalog and explicitly defined rules in the
            scan. Please see `filter
            syntax <https://docs.cloud.google.com/dataplex/docs/auto-data-quality-overview#rule-filtering>`__
            for more details.
    """

    class PostScanActions(proto.Message):
        r"""The configuration of post scan actions of DataQualityScan.

        Attributes:
            bigquery_export (google.cloud.dataplex_v1.types.DataQualitySpec.PostScanActions.BigQueryExport):
                Optional. If set, results will be exported to
                the provided BigQuery table.
            notification_report (google.cloud.dataplex_v1.types.DataQualitySpec.PostScanActions.NotificationReport):
                Optional. If set, results will be sent to the
                provided notification receipts upon triggers.
        """

        class BigQueryExport(proto.Message):
            r"""The configuration of BigQuery export post scan action.

            Attributes:
                results_table (str):
                    Optional. The BigQuery table to export DataQualityScan
                    results to. Format:
                    //bigquery.googleapis.com/projects/PROJECT_ID/datasets/DATASET_ID/tables/TABLE_ID
                    or projects/PROJECT_ID/datasets/DATASET_ID/tables/TABLE_ID
            """

            results_table: str = proto.Field(
                proto.STRING,
                number=1,
            )

        class Recipients(proto.Message):
            r"""The individuals or groups who are designated to receive
            notifications upon triggers.

            Attributes:
                emails (MutableSequence[str]):
                    Optional. The email recipients who will
                    receive the DataQualityScan results report.
            """

            emails: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=1,
            )

        class ScoreThresholdTrigger(proto.Message):
            r"""This trigger is triggered when the DQ score in the job result
            is less than a specified input score.

            Attributes:
                score_threshold (float):
                    Optional. The score range is in [0,100].
            """

            score_threshold: float = proto.Field(
                proto.FLOAT,
                number=2,
            )

        class JobFailureTrigger(proto.Message):
            r"""This trigger is triggered when the scan job itself fails,
            regardless of the result.

            """

        class JobEndTrigger(proto.Message):
            r"""This trigger is triggered whenever a scan job run ends,
            regardless of the result.

            """

        class NotificationReport(proto.Message):
            r"""The configuration of notification report post scan action.

            Attributes:
                recipients (google.cloud.dataplex_v1.types.DataQualitySpec.PostScanActions.Recipients):
                    Required. The recipients who will receive the
                    notification report.
                score_threshold_trigger (google.cloud.dataplex_v1.types.DataQualitySpec.PostScanActions.ScoreThresholdTrigger):
                    Optional. If set, report will be sent when
                    score threshold is met.
                job_failure_trigger (google.cloud.dataplex_v1.types.DataQualitySpec.PostScanActions.JobFailureTrigger):
                    Optional. If set, report will be sent when a
                    scan job fails.
                job_end_trigger (google.cloud.dataplex_v1.types.DataQualitySpec.PostScanActions.JobEndTrigger):
                    Optional. If set, report will be sent when a
                    scan job ends.
            """

            recipients: "DataQualitySpec.PostScanActions.Recipients" = proto.Field(
                proto.MESSAGE,
                number=1,
                message="DataQualitySpec.PostScanActions.Recipients",
            )
            score_threshold_trigger: "DataQualitySpec.PostScanActions.ScoreThresholdTrigger" = proto.Field(
                proto.MESSAGE,
                number=2,
                message="DataQualitySpec.PostScanActions.ScoreThresholdTrigger",
            )
            job_failure_trigger: "DataQualitySpec.PostScanActions.JobFailureTrigger" = (
                proto.Field(
                    proto.MESSAGE,
                    number=4,
                    message="DataQualitySpec.PostScanActions.JobFailureTrigger",
                )
            )
            job_end_trigger: "DataQualitySpec.PostScanActions.JobEndTrigger" = (
                proto.Field(
                    proto.MESSAGE,
                    number=5,
                    message="DataQualitySpec.PostScanActions.JobEndTrigger",
                )
            )

        bigquery_export: "DataQualitySpec.PostScanActions.BigQueryExport" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="DataQualitySpec.PostScanActions.BigQueryExport",
        )
        notification_report: "DataQualitySpec.PostScanActions.NotificationReport" = (
            proto.Field(
                proto.MESSAGE,
                number=2,
                message="DataQualitySpec.PostScanActions.NotificationReport",
            )
        )

    rules: MutableSequence["DataQualityRule"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="DataQualityRule",
    )
    sampling_percent: float = proto.Field(
        proto.FLOAT,
        number=4,
    )
    row_filter: str = proto.Field(
        proto.STRING,
        number=5,
    )
    post_scan_actions: PostScanActions = proto.Field(
        proto.MESSAGE,
        number=6,
        message=PostScanActions,
    )
    catalog_publishing_enabled: bool = proto.Field(
        proto.BOOL,
        number=8,
    )
    enable_catalog_based_rules: bool = proto.Field(
        proto.BOOL,
        number=10,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=11,
    )


class DataQualityResult(proto.Message):
    r"""The output of a DataQualityScan.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        passed (bool):
            Output only. Overall data quality result -- ``true`` if all
            rules passed.
        score (float):
            Output only. The overall data quality score.

            The score ranges between [0, 100] (up to two decimal
            points).

            This field is a member of `oneof`_ ``_score``.
        dimensions (MutableSequence[google.cloud.dataplex_v1.types.DataQualityDimensionResult]):
            Output only. A list of results at the dimension level.

            A dimension will have a corresponding
            ``DataQualityDimensionResult`` if and only if there is at
            least one rule with the 'dimension' field set to it.
        columns (MutableSequence[google.cloud.dataplex_v1.types.DataQualityColumnResult]):
            Output only. A list of results at the column level.

            A column will have a corresponding
            ``DataQualityColumnResult`` if and only if there is at least
            one rule with the 'column' field set to it.
        rules (MutableSequence[google.cloud.dataplex_v1.types.DataQualityRuleResult]):
            Output only. A list of all the rules in a
            job, and their results.
        row_count (int):
            Output only. The count of rows processed.
        scanned_data (google.cloud.dataplex_v1.types.ScannedData):
            Output only. The data scanned for this
            result.
        post_scan_actions_result (google.cloud.dataplex_v1.types.DataQualityResult.PostScanActionsResult):
            Output only. The result of post scan actions.
        catalog_publishing_status (google.cloud.dataplex_v1.types.DataScanCatalogPublishingStatus):
            Output only. The status of publishing the
            data scan as Dataplex Universal Catalog
            metadata.
        anomaly_detection_generated_assets (google.cloud.dataplex_v1.types.DataQualityResult.AnomalyDetectionGeneratedAssets):
            Output only. The generated assets for anomaly
            detection.
    """

    class PostScanActionsResult(proto.Message):
        r"""The result of post scan actions of DataQualityScan job.

        Attributes:
            bigquery_export_result (google.cloud.dataplex_v1.types.DataQualityResult.PostScanActionsResult.BigQueryExportResult):
                Output only. The result of BigQuery export
                post scan action.
        """

        class BigQueryExportResult(proto.Message):
            r"""The result of BigQuery export post scan action.

            Attributes:
                state (google.cloud.dataplex_v1.types.DataQualityResult.PostScanActionsResult.BigQueryExportResult.State):
                    Output only. Execution state for the BigQuery
                    exporting.
                message (str):
                    Output only. Additional information about the
                    BigQuery exporting.
            """

            class State(proto.Enum):
                r"""Execution state for the exporting.

                Values:
                    STATE_UNSPECIFIED (0):
                        The exporting state is unspecified.
                    SUCCEEDED (1):
                        The exporting completed successfully.
                    FAILED (2):
                        The exporting is no longer running due to an
                        error.
                    SKIPPED (3):
                        The exporting is skipped due to no valid scan
                        result to export (usually caused by scan
                        failed).
                """

                STATE_UNSPECIFIED = 0
                SUCCEEDED = 1
                FAILED = 2
                SKIPPED = 3

            state: "DataQualityResult.PostScanActionsResult.BigQueryExportResult.State" = proto.Field(
                proto.ENUM,
                number=1,
                enum="DataQualityResult.PostScanActionsResult.BigQueryExportResult.State",
            )
            message: str = proto.Field(
                proto.STRING,
                number=2,
            )

        bigquery_export_result: "DataQualityResult.PostScanActionsResult.BigQueryExportResult" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="DataQualityResult.PostScanActionsResult.BigQueryExportResult",
        )

    class AnomalyDetectionGeneratedAssets(proto.Message):
        r"""The assets generated by Anomaly Detection Data Scan.

        Attributes:
            result_table (str):
                Output only. The result table for anomaly detection. Format:
                PROJECT_ID.DATASET_ID.TABLE_ID If the result table is set at
                AnomalyDetectionAssets, the result table here would be the
                same as the one set in the
                AnomalyDetectionAssets.result_table.
            data_intermediate_table (str):
                Output only. The intermediate table for data anomaly
                detection. Format: PROJECT_ID.DATASET_ID.TABLE_ID
            freshness_intermediate_table (str):
                Output only. The intermediate table for freshness anomaly
                detection. Format: PROJECT_ID.DATASET_ID.TABLE_ID
            volume_intermediate_table (str):
                Output only. The intermediate table for volume anomaly
                detection. Format: PROJECT_ID.DATASET_ID.TABLE_ID
        """

        result_table: str = proto.Field(
            proto.STRING,
            number=1,
        )
        data_intermediate_table: str = proto.Field(
            proto.STRING,
            number=2,
        )
        freshness_intermediate_table: str = proto.Field(
            proto.STRING,
            number=3,
        )
        volume_intermediate_table: str = proto.Field(
            proto.STRING,
            number=4,
        )

    passed: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    score: float = proto.Field(
        proto.FLOAT,
        number=9,
        optional=True,
    )
    dimensions: MutableSequence["DataQualityDimensionResult"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="DataQualityDimensionResult",
    )
    columns: MutableSequence["DataQualityColumnResult"] = proto.RepeatedField(
        proto.MESSAGE,
        number=10,
        message="DataQualityColumnResult",
    )
    rules: MutableSequence["DataQualityRuleResult"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="DataQualityRuleResult",
    )
    row_count: int = proto.Field(
        proto.INT64,
        number=4,
    )
    scanned_data: processing.ScannedData = proto.Field(
        proto.MESSAGE,
        number=7,
        message=processing.ScannedData,
    )
    post_scan_actions_result: PostScanActionsResult = proto.Field(
        proto.MESSAGE,
        number=8,
        message=PostScanActionsResult,
    )
    catalog_publishing_status: datascans_common.DataScanCatalogPublishingStatus = (
        proto.Field(
            proto.MESSAGE,
            number=11,
            message=datascans_common.DataScanCatalogPublishingStatus,
        )
    )
    anomaly_detection_generated_assets: AnomalyDetectionGeneratedAssets = proto.Field(
        proto.MESSAGE,
        number=12,
        message=AnomalyDetectionGeneratedAssets,
    )


class DataQualityRuleResult(proto.Message):
    r"""DataQualityRuleResult provides a more detailed, per-rule view
    of the results.

    Attributes:
        rule (google.cloud.dataplex_v1.types.DataQualityRule):
            Output only. The rule specified in the
            DataQualitySpec, as is.
        passed (bool):
            Output only. Whether the rule passed or
            failed.
        evaluated_count (int):
            Output only. The number of rows a rule was evaluated
            against.

            This field is only valid for row-level type rules.

            Evaluated count can be configured to either

            - include all rows (default) - with ``null`` rows
              automatically failing rule evaluation, or
            - exclude ``null`` rows from the ``evaluated_count``, by
              setting ``ignore_nulls = true``.

            This field is not set for rule SqlAssertion.
        passed_count (int):
            Output only. The number of rows which passed
            a rule evaluation.
            This field is only valid for row-level type
            rules.

            This field is not set for rule SqlAssertion.
        null_count (int):
            Output only. The number of rows with null
            values in the specified column.
        pass_ratio (float):
            Output only. The ratio of **passed_count /
            evaluated_count**.

            This field is only valid for row-level type rules.
        failing_rows_query (str):
            Output only. The query to find rows that did
            not pass this rule.
            This field is only valid for row-level type
            rules.
        assertion_row_count (int):
            Output only. The number of rows returned by
            the SQL statement in a SQL assertion rule.

            This field is only valid for SQL assertion
            rules.
        debug_queries_result_sets (MutableSequence[google.cloud.dataplex_v1.types.DataQualityRuleResult.DebugQueryResultSet]):
            Output only. Contains the results of all debug queries for
            this rule. The number of result sets will correspond to the
            number of
            [debug_queries][google.cloud.dataplex.v1.DataQualityRule.debug_queries].
    """

    class DebugQueryResult(proto.Message):
        r"""Contains a single result from the debug query.

        Attributes:
            name (str):
                Specifies the name of the result. Available if provided with
                an explicit alias using ``[AS] alias``.
            type_ (str):
                Indicates the data type of the result. For more information,
                see `BigQuery data
                types <https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types>`__.
            value (str):
                Represents the value of the result as a
                string.
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        type_: str = proto.Field(
            proto.STRING,
            number=2,
        )
        value: str = proto.Field(
            proto.STRING,
            number=3,
        )

    class DebugQueryResultSet(proto.Message):
        r"""Contains all results from a debug query.

        Attributes:
            results (MutableSequence[google.cloud.dataplex_v1.types.DataQualityRuleResult.DebugQueryResult]):
                Output only. Contains all results. Up to 10
                results can be returned.
        """

        results: MutableSequence["DataQualityRuleResult.DebugQueryResult"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=1,
                message="DataQualityRuleResult.DebugQueryResult",
            )
        )

    rule: "DataQualityRule" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="DataQualityRule",
    )
    passed: bool = proto.Field(
        proto.BOOL,
        number=7,
    )
    evaluated_count: int = proto.Field(
        proto.INT64,
        number=9,
    )
    passed_count: int = proto.Field(
        proto.INT64,
        number=8,
    )
    null_count: int = proto.Field(
        proto.INT64,
        number=5,
    )
    pass_ratio: float = proto.Field(
        proto.DOUBLE,
        number=6,
    )
    failing_rows_query: str = proto.Field(
        proto.STRING,
        number=10,
    )
    assertion_row_count: int = proto.Field(
        proto.INT64,
        number=11,
    )
    debug_queries_result_sets: MutableSequence[DebugQueryResultSet] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=13,
            message=DebugQueryResultSet,
        )
    )


class DataQualityDimensionResult(proto.Message):
    r"""DataQualityDimensionResult provides a more detailed,
    per-dimension view of the results.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        dimension (google.cloud.dataplex_v1.types.DataQualityDimension):
            Output only. The dimension config specified
            in the DataQualitySpec, as is.
        passed (bool):
            Output only. Whether the dimension passed or
            failed.
        score (float):
            Output only. The dimension-level data quality score for this
            data scan job if and only if the 'dimension' field is set.

            The score ranges between [0, 100] (up to two decimal
            points).

            This field is a member of `oneof`_ ``_score``.
    """

    dimension: "DataQualityDimension" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="DataQualityDimension",
    )
    passed: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    score: float = proto.Field(
        proto.FLOAT,
        number=4,
        optional=True,
    )


class DataQualityDimension(proto.Message):
    r"""A dimension captures data quality intent about a defined
    subset of the rules specified.

    Attributes:
        name (str):
            Output only. The dimension name a rule
            belongs to. Custom dimension name is supported
            with all uppercase letters and maximum length of
            30 characters.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DataQualityRule(proto.Message):
    r"""A rule captures data quality intent about a data source.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        range_expectation (google.cloud.dataplex_v1.types.DataQualityRule.RangeExpectation):
            Row-level rule which evaluates whether each
            column value lies between a specified range.

            This field is a member of `oneof`_ ``rule_type``.
        non_null_expectation (google.cloud.dataplex_v1.types.DataQualityRule.NonNullExpectation):
            Row-level rule which evaluates whether each
            column value is null.

            This field is a member of `oneof`_ ``rule_type``.
        set_expectation (google.cloud.dataplex_v1.types.DataQualityRule.SetExpectation):
            Row-level rule which evaluates whether each
            column value is contained by a specified set.

            This field is a member of `oneof`_ ``rule_type``.
        regex_expectation (google.cloud.dataplex_v1.types.DataQualityRule.RegexExpectation):
            Row-level rule which evaluates whether each
            column value matches a specified regex.

            This field is a member of `oneof`_ ``rule_type``.
        uniqueness_expectation (google.cloud.dataplex_v1.types.DataQualityRule.UniquenessExpectation):
            Row-level rule which evaluates whether each
            column value is unique.

            This field is a member of `oneof`_ ``rule_type``.
        statistic_range_expectation (google.cloud.dataplex_v1.types.DataQualityRule.StatisticRangeExpectation):
            Aggregate rule which evaluates whether the
            column aggregate statistic lies between a
            specified range.

            This field is a member of `oneof`_ ``rule_type``.
        row_condition_expectation (google.cloud.dataplex_v1.types.DataQualityRule.RowConditionExpectation):
            Row-level rule which evaluates whether each
            row in a table passes the specified condition.

            This field is a member of `oneof`_ ``rule_type``.
        table_condition_expectation (google.cloud.dataplex_v1.types.DataQualityRule.TableConditionExpectation):
            Aggregate rule which evaluates whether the
            provided expression is true for a table.

            This field is a member of `oneof`_ ``rule_type``.
        sql_assertion (google.cloud.dataplex_v1.types.DataQualityRule.SqlAssertion):
            Aggregate rule which evaluates the number of
            rows returned for the provided statement. If any
            rows are returned, this rule fails.

            This field is a member of `oneof`_ ``rule_type``.
        template_reference (google.cloud.dataplex_v1.types.DataQualityRule.TemplateReference):
            Aggregate rule which references a rule
            template and provides the parameters to be
            substituted in the template. If any rows are
            returned, this rule fails.

            This field is a member of `oneof`_ ``rule_type``.
        column (str):
            Optional. The unnested column which this rule
            is evaluated against.
        ignore_null (bool):
            Optional. Rows with ``null`` values will automatically fail
            a rule, unless ``ignore_null`` is ``true``. In that case,
            such ``null`` rows are trivially considered passing.

            This field is only valid for the following type of rules:

            - RangeExpectation
            - RegexExpectation
            - SetExpectation
            - UniquenessExpectation
        dimension (str):
            Optional. The dimension a rule belongs to.
            Results are also aggregated at the dimension
            level. Custom dimension name is supported with
            all uppercase letters and maximum length of 30
            characters.
        threshold (float):
            Optional. The minimum ratio of **passing_rows / total_rows**
            required to pass this rule, with a range of [0.0, 1.0].

            0 indicates default value (i.e. 1.0).

            This field is only valid for row-level type rules.
        name (str):
            Optional. A mutable name for the rule.

            - The name must contain only letters (a-z, A-Z), numbers
              (0-9), or hyphens (-).
            - The maximum length is 63 characters.
            - Must start with a letter.
            - Must end with a number or a letter.
        description (str):
            Optional. Description of the rule.

            - The maximum length is 1,024 characters.
        suspended (bool):
            Optional. Whether the Rule is active or
            suspended. Default is false.
        attributes (MutableMapping[str, str]):
            Optional. Map of attribute name and value
            linked to the rule. The rules to evaluate can be
            filtered based on attributes provided here and a
            filter expression provided in the
            DataQualitySpec.filter field.
        rule_source (google.cloud.dataplex_v1.types.DataQualityRule.RuleSource):
            Output only. Contains information about the
            source of the rule and its relationship with the
            BigQuery table, where applicable.
        debug_queries (MutableSequence[google.cloud.dataplex_v1.types.DataQualityRule.DebugQuery]):
            Optional. Specifies the debug queries for
            this rule. Currently, only one query is
            supported, but this may be expanded in the
            future.
    """

    class RangeExpectation(proto.Message):
        r"""Evaluates whether each column value lies between a specified
        range.

        Attributes:
            min_value (str):
                Optional. The minimum column value allowed for a row to pass
                this validation. At least one of ``min_value`` and
                ``max_value`` need to be provided.
            max_value (str):
                Optional. The maximum column value allowed for a row to pass
                this validation. At least one of ``min_value`` and
                ``max_value`` need to be provided.
            strict_min_enabled (bool):
                Optional. Whether each value needs to be strictly greater
                than ('>') the minimum, or if equality is allowed.

                Only relevant if a ``min_value`` has been defined. Default =
                false.
            strict_max_enabled (bool):
                Optional. Whether each value needs to be strictly lesser
                than ('<') the maximum, or if equality is allowed.

                Only relevant if a ``max_value`` has been defined. Default =
                false.
        """

        min_value: str = proto.Field(
            proto.STRING,
            number=1,
        )
        max_value: str = proto.Field(
            proto.STRING,
            number=2,
        )
        strict_min_enabled: bool = proto.Field(
            proto.BOOL,
            number=3,
        )
        strict_max_enabled: bool = proto.Field(
            proto.BOOL,
            number=4,
        )

    class NonNullExpectation(proto.Message):
        r"""Evaluates whether each column value is null."""

    class SetExpectation(proto.Message):
        r"""Evaluates whether each column value is contained by a
        specified set.

        Attributes:
            values (MutableSequence[str]):
                Optional. Expected values for the column
                value.
        """

        values: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )

    class RegexExpectation(proto.Message):
        r"""Evaluates whether each column value matches a specified
        regex.

        Attributes:
            regex (str):
                Optional. A regular expression the column
                value is expected to match.
        """

        regex: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class UniquenessExpectation(proto.Message):
        r"""Evaluates whether the column has duplicates."""

    class StatisticRangeExpectation(proto.Message):
        r"""Evaluates whether the column aggregate statistic lies between
        a specified range.

        Attributes:
            statistic (google.cloud.dataplex_v1.types.DataQualityRule.StatisticRangeExpectation.ColumnStatistic):
                Optional. The aggregate metric to evaluate.
            min_value (str):
                Optional. The minimum column statistic value allowed for a
                row to pass this validation.

                At least one of ``min_value`` and ``max_value`` need to be
                provided.
            max_value (str):
                Optional. The maximum column statistic value allowed for a
                row to pass this validation.

                At least one of ``min_value`` and ``max_value`` need to be
                provided.
            strict_min_enabled (bool):
                Optional. Whether column statistic needs to be strictly
                greater than ('>') the minimum, or if equality is allowed.

                Only relevant if a ``min_value`` has been defined. Default =
                false.
            strict_max_enabled (bool):
                Optional. Whether column statistic needs to be strictly
                lesser than ('<') the maximum, or if equality is allowed.

                Only relevant if a ``max_value`` has been defined. Default =
                false.
        """

        class ColumnStatistic(proto.Enum):
            r"""The list of aggregate metrics a rule can be evaluated
            against.

            Values:
                STATISTIC_UNDEFINED (0):
                    Unspecified statistic type
                MEAN (1):
                    Evaluate the column mean
                MIN (2):
                    Evaluate the column min
                MAX (3):
                    Evaluate the column max
            """

            STATISTIC_UNDEFINED = 0
            MEAN = 1
            MIN = 2
            MAX = 3

        statistic: "DataQualityRule.StatisticRangeExpectation.ColumnStatistic" = (
            proto.Field(
                proto.ENUM,
                number=1,
                enum="DataQualityRule.StatisticRangeExpectation.ColumnStatistic",
            )
        )
        min_value: str = proto.Field(
            proto.STRING,
            number=2,
        )
        max_value: str = proto.Field(
            proto.STRING,
            number=3,
        )
        strict_min_enabled: bool = proto.Field(
            proto.BOOL,
            number=4,
        )
        strict_max_enabled: bool = proto.Field(
            proto.BOOL,
            number=5,
        )

    class RowConditionExpectation(proto.Message):
        r"""Evaluates whether each row passes the specified condition.

        The SQL expression needs to use `GoogleSQL
        syntax <https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax>`__
        and should produce a boolean value per row as the result.

        Example: col1 >= 0 AND col2 < 10

        Attributes:
            sql_expression (str):
                Optional. The SQL expression.
        """

        sql_expression: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class TableConditionExpectation(proto.Message):
        r"""Evaluates whether the provided expression is true.

        The SQL expression needs to use `GoogleSQL
        syntax <https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax>`__
        and should produce a scalar boolean result.

        Example: MIN(col1) >= 0

        Attributes:
            sql_expression (str):
                Optional. The SQL expression.
        """

        sql_expression: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class SqlAssertion(proto.Message):
        r"""A SQL statement that is evaluated to return rows that match an
        invalid state. If any rows are are returned, this rule fails.

        The SQL statement must use `GoogleSQL
        syntax <https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax>`__,
        and must not contain any semicolons.

        You can use the data reference parameter ``${data()}`` to reference
        the source table with all of its precondition filters applied.
        Examples of precondition filters include row filters, incremental
        data filters, and sampling. For more information, see `Data
        reference
        parameter <https://cloud.google.com/dataplex/docs/auto-data-quality-overview#data-reference-parameter>`__.

        Example: ``SELECT * FROM ${data()} WHERE price < 0``

        Attributes:
            sql_statement (str):
                Optional. The SQL statement.
        """

        sql_statement: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class TemplateReference(proto.Message):
        r"""A rule that constructs a SQL statement to evaluate using a
        rule template and parameter values. If the constructed statement
        returns any rows, this rule fails

        Attributes:
            name (str):
                Required. The template entry name. Entry must be of
                EntryType
                ``projects/dataplex-types/locations/global/entryTypes/data-quality-rule-template``
                and contains top-level aspect of AspectType
                ``projects/dataplex-types/locations/global/aspectTypes/data-quality-rule-template``.
                The format is:
                ``projects/{project_id_or_number}/locations/{location_id}/entryGroups/{entry_group_id}/entries/{entry_id}``
            values (MutableMapping[str, google.cloud.dataplex_v1.types.DataQualityRule.TemplateReference.ParameterValue]):
                Optional. Provides the map of parameter name
                and value. The maximum size of the field is
                120KB (encoded as UTF-8).
            resolved_sql (str):
                Output only. The resolved SQL statement
                generated from the template with parameters
                substituted. It is only populated in the result.
            rule_template (google.cloud.dataplex_v1.types.DataQualityRuleTemplate):
                Output only. The rule template used to
                resolve the rule. It is only populated in the
                result.
        """

        class ParameterValue(proto.Message):
            r"""Represents a parameter value.

            Attributes:
                value (str):
                    Required. Represents the string value of the
                    parameter.
            """

            value: str = proto.Field(
                proto.STRING,
                number=1,
            )

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        values: MutableMapping[
            str, "DataQualityRule.TemplateReference.ParameterValue"
        ] = proto.MapField(
            proto.STRING,
            proto.MESSAGE,
            number=5,
            message="DataQualityRule.TemplateReference.ParameterValue",
        )
        resolved_sql: str = proto.Field(
            proto.STRING,
            number=3,
        )
        rule_template: data_quality_rule_template.DataQualityRuleTemplate = proto.Field(
            proto.MESSAGE,
            number=4,
            message=data_quality_rule_template.DataQualityRuleTemplate,
        )

    class RuleSource(proto.Message):
        r"""Represents the rule source information from Catalog.

        Attributes:
            rule_path_elements (MutableSequence[google.cloud.dataplex_v1.types.DataQualityRule.RuleSource.RulePathElement]):
                Output only. Rule path elements represent
                information about the individual items in the
                relationship path between the scan resource and
                rule origin in that order.
        """

        class RulePathElement(proto.Message):
            r"""Path Element represents the direct relationship between the
            rule origin (aspects) to the BigQuery Entry. Ordering of the
            rule relationship will be maintained such that the first entry
            in the list is the closest ancestor (BigQuery table itself). A
            blank source denotes that the rule is derived directly from the
            DataScan itself.

            This message has `oneof`_ fields (mutually exclusive fields).
            For each oneof, at most one member field can be set at the same time.
            Setting any member of the oneof automatically clears all other
            members.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                entry_source (google.cloud.dataplex_v1.types.DataQualityRule.RuleSource.RulePathElement.EntrySource):
                    Output only. Entry source represents
                    information about the related source entry.

                    This field is a member of `oneof`_ ``source_type``.
                entry_link_source (google.cloud.dataplex_v1.types.DataQualityRule.RuleSource.RulePathElement.EntryLinkSource):
                    Output only. Entry link source represents
                    information about the entry link.

                    This field is a member of `oneof`_ ``source_type``.
            """

            class EntrySource(proto.Message):
                r"""Entry source represents information about the related source
                entry.

                Attributes:
                    entry_type (str):
                        Output only. The entry type to represent the current
                        characteristics of the entry in the form of:
                        ``projects/{project_id_or_number}/locations/{location_id}/entryTypes/{entry-type-id}``.
                    entry (str):
                        Output only. The entry name in the form of:
                        ``projects/{project_id_or_number}/locations/{location_id}/entryGroups/{entry_group_id}/entries/{entry_id}``
                    display_name (str):
                        Output only. The display name of the entry.
                """

                entry_type: str = proto.Field(
                    proto.STRING,
                    number=1,
                )
                entry: str = proto.Field(
                    proto.STRING,
                    number=2,
                )
                display_name: str = proto.Field(
                    proto.STRING,
                    number=3,
                )

            class EntryLinkSource(proto.Message):
                r"""Entry link source represents information about the entry
                link.

                Attributes:
                    entry_link_type (str):
                        Output only. The entry link type to represent the current
                        relationship between the entry and the next entry in the
                        path. In the form of:
                        ``projects/{project_id_or_number}/locations/{location_id}/entryLinkTypes/{entry_link_type_id}``
                    entry_link (str):
                        Output only. The entry link name in the form of:
                        ``projects/{project_id_or_number}/locations/{location_id}/entryGroups/{entry_group_id}/entryLinks/{entry_link_id}``
                """

                entry_link_type: str = proto.Field(
                    proto.STRING,
                    number=1,
                )
                entry_link: str = proto.Field(
                    proto.STRING,
                    number=2,
                )

            entry_source: "DataQualityRule.RuleSource.RulePathElement.EntrySource" = (
                proto.Field(
                    proto.MESSAGE,
                    number=1,
                    oneof="source_type",
                    message="DataQualityRule.RuleSource.RulePathElement.EntrySource",
                )
            )
            entry_link_source: "DataQualityRule.RuleSource.RulePathElement.EntryLinkSource" = proto.Field(
                proto.MESSAGE,
                number=2,
                oneof="source_type",
                message="DataQualityRule.RuleSource.RulePathElement.EntryLinkSource",
            )

        rule_path_elements: MutableSequence[
            "DataQualityRule.RuleSource.RulePathElement"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="DataQualityRule.RuleSource.RulePathElement",
        )

    class DebugQuery(proto.Message):
        r"""Specifies a SQL statement that is evaluated to return up to 10
        scalar values that are used to debug rules. If the rule fails, the
        values can help diagnose the cause of the failure.

        The SQL statement must use `GoogleSQL
        syntax <https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax>`__,
        and must not contain any semicolons.

        You can use the data reference parameter ``${data()}`` to reference
        the source table with all of its precondition filters applied.
        Examples of precondition filters include row filters, incremental
        data filters, and sampling. For more information, see `Data
        reference
        parameter <https://cloud.google.com/dataplex/docs/auto-data-quality-overview#data-reference-parameter>`__.

        You can also name results with an explicit alias using
        ``[AS] alias``. For more information, see `BigQuery explicit
        aliases <https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax#explicit_alias_syntax>`__.

        Example:
        ``SELECT MIN(col1) AS min_col1, MAX(col1) AS max_col1 FROM ${data()}``

        Attributes:
            description (str):
                Optional. Specifies the description of the debug query.

                - The maximum length is 1,024 characters.
            sql_statement (str):
                Required. Specifies the SQL statement to be
                executed.
        """

        description: str = proto.Field(
            proto.STRING,
            number=1,
        )
        sql_statement: str = proto.Field(
            proto.STRING,
            number=2,
        )

    range_expectation: RangeExpectation = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="rule_type",
        message=RangeExpectation,
    )
    non_null_expectation: NonNullExpectation = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="rule_type",
        message=NonNullExpectation,
    )
    set_expectation: SetExpectation = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="rule_type",
        message=SetExpectation,
    )
    regex_expectation: RegexExpectation = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="rule_type",
        message=RegexExpectation,
    )
    uniqueness_expectation: UniquenessExpectation = proto.Field(
        proto.MESSAGE,
        number=100,
        oneof="rule_type",
        message=UniquenessExpectation,
    )
    statistic_range_expectation: StatisticRangeExpectation = proto.Field(
        proto.MESSAGE,
        number=101,
        oneof="rule_type",
        message=StatisticRangeExpectation,
    )
    row_condition_expectation: RowConditionExpectation = proto.Field(
        proto.MESSAGE,
        number=200,
        oneof="rule_type",
        message=RowConditionExpectation,
    )
    table_condition_expectation: TableConditionExpectation = proto.Field(
        proto.MESSAGE,
        number=201,
        oneof="rule_type",
        message=TableConditionExpectation,
    )
    sql_assertion: SqlAssertion = proto.Field(
        proto.MESSAGE,
        number=202,
        oneof="rule_type",
        message=SqlAssertion,
    )
    template_reference: TemplateReference = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="rule_type",
        message=TemplateReference,
    )
    column: str = proto.Field(
        proto.STRING,
        number=500,
    )
    ignore_null: bool = proto.Field(
        proto.BOOL,
        number=501,
    )
    dimension: str = proto.Field(
        proto.STRING,
        number=502,
    )
    threshold: float = proto.Field(
        proto.DOUBLE,
        number=503,
    )
    name: str = proto.Field(
        proto.STRING,
        number=504,
    )
    description: str = proto.Field(
        proto.STRING,
        number=505,
    )
    suspended: bool = proto.Field(
        proto.BOOL,
        number=506,
    )
    attributes: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=507,
    )
    rule_source: RuleSource = proto.Field(
        proto.MESSAGE,
        number=508,
        message=RuleSource,
    )
    debug_queries: MutableSequence[DebugQuery] = proto.RepeatedField(
        proto.MESSAGE,
        number=510,
        message=DebugQuery,
    )


class DataQualityColumnResult(proto.Message):
    r"""DataQualityColumnResult provides a more detailed, per-column
    view of the results.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        column (str):
            Output only. The column specified in the
            DataQualityRule.
        score (float):
            Output only. The column-level data quality score for this
            data scan job if and only if the 'column' field is set.

            The score ranges between between [0, 100] (up to two decimal
            points).

            This field is a member of `oneof`_ ``_score``.
        passed (bool):
            Output only. Whether the column passed or
            failed.
        dimensions (MutableSequence[google.cloud.dataplex_v1.types.DataQualityDimensionResult]):
            Output only. The dimension-level results for
            this column.
    """

    column: str = proto.Field(
        proto.STRING,
        number=1,
    )
    score: float = proto.Field(
        proto.FLOAT,
        number=2,
        optional=True,
    )
    passed: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    dimensions: MutableSequence["DataQualityDimensionResult"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="DataQualityDimensionResult",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
