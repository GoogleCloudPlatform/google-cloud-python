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

from google.cloud.dataplex_v1.types import datascans_common, processing

__protobuf__ = proto.module(
    package="google.cloud.dataplex.v1",
    manifest={
        "DataProfileSpec",
        "DataProfileResult",
    },
)


class DataProfileSpec(proto.Message):
    r"""DataProfileScan related setting.

    Attributes:
        sampling_percent (float):
            Optional. The percentage of the records to be selected from
            the dataset for DataScan.

            - Value can range between 0.0 and 100.0 with up to 3
              significant decimal digits.
            - Sampling is not applied if ``sampling_percent`` is not
              specified, 0 or

            100.
        row_filter (str):
            Optional. A filter applied to all rows in a
            single DataScan job. The filter needs to be a
            valid SQL expression for a WHERE clause in
            BigQuery standard SQL syntax.
            Example: col1 >= 0 AND col2 < 10
        post_scan_actions (google.cloud.dataplex_v1.types.DataProfileSpec.PostScanActions):
            Optional. Actions to take upon job
            completion..
        include_fields (google.cloud.dataplex_v1.types.DataProfileSpec.SelectedFields):
            Optional. The fields to include in data profile.

            If not specified, all fields at the time of profile scan job
            execution are included, except for ones listed in
            ``exclude_fields``.
        exclude_fields (google.cloud.dataplex_v1.types.DataProfileSpec.SelectedFields):
            Optional. The fields to exclude from data profile.

            If specified, the fields will be excluded from data profile,
            regardless of ``include_fields`` value.
        catalog_publishing_enabled (bool):
            Optional. If set, the latest DataScan job
            result will be published as Dataplex Universal
            Catalog metadata.
        mode (google.cloud.dataplex_v1.types.DataProfileSpec.Mode):
            Optional. The execution mode for the profile
            scan.
    """

    class Mode(proto.Enum):
        r"""Defines the execution mode for the profile scan.

        Values:
            MODE_UNSPECIFIED (0):
                Default value. This value is unused.
            STANDARD (1):
                Performs standard profiling. The behavior is controlled by
                other fields such as ``sampling_percent``, ``row_filter``,
                and column filters. This mode allows for full scans or
                custom sampling.
            LIGHTWEIGHT (2):
                Specifies lightweight profiling mode. This mode is optimized
                for low-latency, low-fidelity profiling.

                When this mode is selected, the following fields must not be
                set: ``sampling_percent``, ``row_filter``,
                ``include_fields``, and ``exclude_fields``.
        """

        MODE_UNSPECIFIED = 0
        STANDARD = 1
        LIGHTWEIGHT = 2

    class PostScanActions(proto.Message):
        r"""The configuration of post scan actions of DataProfileScan
        job.

        Attributes:
            bigquery_export (google.cloud.dataplex_v1.types.DataProfileSpec.PostScanActions.BigQueryExport):
                Optional. If set, results will be exported to
                the provided BigQuery table.
        """

        class BigQueryExport(proto.Message):
            r"""The configuration of BigQuery export post scan action.

            Attributes:
                results_table (str):
                    Optional. The BigQuery table to export DataProfileScan
                    results to. Format:
                    //bigquery.googleapis.com/projects/PROJECT_ID/datasets/DATASET_ID/tables/TABLE_ID
            """

            results_table: str = proto.Field(
                proto.STRING,
                number=1,
            )

        bigquery_export: "DataProfileSpec.PostScanActions.BigQueryExport" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="DataProfileSpec.PostScanActions.BigQueryExport",
        )

    class SelectedFields(proto.Message):
        r"""The specification for fields to include or exclude in data
        profile scan.

        Attributes:
            field_names (MutableSequence[str]):
                Optional. Expected input is a list of fully
                qualified names of fields as in the schema.

                Only top-level field names for nested fields are
                supported. For instance, if 'x' is of nested
                field type, listing 'x' is supported but 'x.y.z'
                is not supported. Here 'y' and 'y.z' are nested
                fields of 'x'.
        """

        field_names: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )

    sampling_percent: float = proto.Field(
        proto.FLOAT,
        number=2,
    )
    row_filter: str = proto.Field(
        proto.STRING,
        number=3,
    )
    post_scan_actions: PostScanActions = proto.Field(
        proto.MESSAGE,
        number=4,
        message=PostScanActions,
    )
    include_fields: SelectedFields = proto.Field(
        proto.MESSAGE,
        number=5,
        message=SelectedFields,
    )
    exclude_fields: SelectedFields = proto.Field(
        proto.MESSAGE,
        number=6,
        message=SelectedFields,
    )
    catalog_publishing_enabled: bool = proto.Field(
        proto.BOOL,
        number=8,
    )
    mode: Mode = proto.Field(
        proto.ENUM,
        number=9,
        enum=Mode,
    )


class DataProfileResult(proto.Message):
    r"""DataProfileResult defines the output of DataProfileScan. Each
    field of the table will have field type specific profile result.

    Attributes:
        row_count (int):
            Output only. The count of rows scanned.
        profile (google.cloud.dataplex_v1.types.DataProfileResult.Profile):
            Output only. The profile information per
            field.
        scanned_data (google.cloud.dataplex_v1.types.ScannedData):
            Output only. The data scanned for this
            result.
        post_scan_actions_result (google.cloud.dataplex_v1.types.DataProfileResult.PostScanActionsResult):
            Output only. The result of post scan actions.
        catalog_publishing_status (google.cloud.dataplex_v1.types.DataScanCatalogPublishingStatus):
            Output only. The status of publishing the
            data scan as Dataplex Universal Catalog
            metadata.
    """

    class Profile(proto.Message):
        r"""Contains name, type, mode and field type specific profile
        information.

        Attributes:
            fields (MutableSequence[google.cloud.dataplex_v1.types.DataProfileResult.Profile.Field]):
                Output only. List of fields with structural
                and profile information for each field.
        """

        class Field(proto.Message):
            r"""A field within a table.

            Attributes:
                name (str):
                    Output only. The name of the field.
                type_ (str):
                    Output only. The data type retrieved from the schema of the
                    data source. For instance, for a BigQuery native table, it
                    is the `BigQuery Table
                    Schema <https://cloud.google.com/bigquery/docs/reference/rest/v2/tables#tablefieldschema>`__.
                    For a Dataplex Universal Catalog Entity, it is the `Entity
                    Schema <https://cloud.google.com/dataplex/docs/reference/rpc/google.cloud.dataplex.v1#type_3>`__.
                mode (str):
                    Output only. The mode of the field. Possible values include:

                    - REQUIRED, if it is a required field.
                    - NULLABLE, if it is an optional field.
                    - REPEATED, if it is a repeated field.
                profile (google.cloud.dataplex_v1.types.DataProfileResult.Profile.Field.ProfileInfo):
                    Output only. Profile information for the
                    corresponding field.
            """

            class ProfileInfo(proto.Message):
                r"""The profile information for each field type.

                This message has `oneof`_ fields (mutually exclusive fields).
                For each oneof, at most one member field can be set at the same time.
                Setting any member of the oneof automatically clears all other
                members.

                .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

                Attributes:
                    null_ratio (float):
                        Output only. Ratio of rows with null value
                        against total scanned rows.
                    distinct_ratio (float):
                        Output only. Ratio of rows with distinct
                        values against total scanned rows. Not available
                        for complex non-groupable field type, including
                        RECORD, ARRAY, GEOGRAPHY, and JSON, as well as
                        fields with REPEATABLE mode.
                    top_n_values (MutableSequence[google.cloud.dataplex_v1.types.DataProfileResult.Profile.Field.ProfileInfo.TopNValue]):
                        Output only. The list of top N non-null
                        values, frequency and ratio with which they
                        occur in the scanned data. N is 10 or equal to
                        the number of distinct values in the field,
                        whichever is smaller. Not available for complex
                        non-groupable field type, including RECORD,
                        ARRAY, GEOGRAPHY, and JSON, as well as fields
                        with REPEATABLE mode.
                    string_profile (google.cloud.dataplex_v1.types.DataProfileResult.Profile.Field.ProfileInfo.StringFieldInfo):
                        String type field information.

                        This field is a member of `oneof`_ ``field_info``.
                    integer_profile (google.cloud.dataplex_v1.types.DataProfileResult.Profile.Field.ProfileInfo.IntegerFieldInfo):
                        Integer type field information.

                        This field is a member of `oneof`_ ``field_info``.
                    double_profile (google.cloud.dataplex_v1.types.DataProfileResult.Profile.Field.ProfileInfo.DoubleFieldInfo):
                        Double type field information.

                        This field is a member of `oneof`_ ``field_info``.
                """

                class StringFieldInfo(proto.Message):
                    r"""The profile information for a string type field.

                    Attributes:
                        min_length (int):
                            Output only. Minimum length of non-null
                            values in the scanned data.
                        max_length (int):
                            Output only. Maximum length of non-null
                            values in the scanned data.
                        average_length (float):
                            Output only. Average length of non-null
                            values in the scanned data.
                    """

                    min_length: int = proto.Field(
                        proto.INT64,
                        number=1,
                    )
                    max_length: int = proto.Field(
                        proto.INT64,
                        number=2,
                    )
                    average_length: float = proto.Field(
                        proto.DOUBLE,
                        number=3,
                    )

                class IntegerFieldInfo(proto.Message):
                    r"""The profile information for an integer type field.

                    Attributes:
                        average (float):
                            Output only. Average of non-null values in
                            the scanned data. NaN, if the field has a NaN.
                        standard_deviation (float):
                            Output only. Standard deviation of non-null
                            values in the scanned data. NaN, if the field
                            has a NaN.
                        min_ (int):
                            Output only. Minimum of non-null values in
                            the scanned data. NaN, if the field has a NaN.
                        quartiles (MutableSequence[int]):
                            Output only. A quartile divides the number of
                            data points into four parts, or quarters, of
                            more-or-less equal size. Three main quartiles
                            used are: The first quartile (Q1) splits off the
                            lowest 25% of data from the highest 75%. It is
                            also known as the lower or 25th empirical
                            quartile, as 25% of the data is below this
                            point. The second quartile (Q2) is the median of
                            a data set. So, 50% of the data lies below this
                            point. The third quartile (Q3) splits off the
                            highest 25% of data from the lowest 75%. It is
                            known as the upper or 75th empirical quartile,
                            as 75% of the data lies below this point. Here,
                            the quartiles is provided as an ordered list of
                            approximate quartile values for the scanned
                            data, occurring in order Q1, median, Q3.
                        max_ (int):
                            Output only. Maximum of non-null values in
                            the scanned data. NaN, if the field has a NaN.
                    """

                    average: float = proto.Field(
                        proto.DOUBLE,
                        number=1,
                    )
                    standard_deviation: float = proto.Field(
                        proto.DOUBLE,
                        number=3,
                    )
                    min_: int = proto.Field(
                        proto.INT64,
                        number=4,
                    )
                    quartiles: MutableSequence[int] = proto.RepeatedField(
                        proto.INT64,
                        number=6,
                    )
                    max_: int = proto.Field(
                        proto.INT64,
                        number=5,
                    )

                class DoubleFieldInfo(proto.Message):
                    r"""The profile information for a double type field.

                    Attributes:
                        average (float):
                            Output only. Average of non-null values in
                            the scanned data. NaN, if the field has a NaN.
                        standard_deviation (float):
                            Output only. Standard deviation of non-null
                            values in the scanned data. NaN, if the field
                            has a NaN.
                        min_ (float):
                            Output only. Minimum of non-null values in
                            the scanned data. NaN, if the field has a NaN.
                        quartiles (MutableSequence[float]):
                            Output only. A quartile divides the number of
                            data points into four parts, or quarters, of
                            more-or-less equal size. Three main quartiles
                            used are: The first quartile (Q1) splits off the
                            lowest 25% of data from the highest 75%. It is
                            also known as the lower or 25th empirical
                            quartile, as 25% of the data is below this
                            point. The second quartile (Q2) is the median of
                            a data set. So, 50% of the data lies below this
                            point. The third quartile (Q3) splits off the
                            highest 25% of data from the lowest 75%. It is
                            known as the upper or 75th empirical quartile,
                            as 75% of the data lies below this point. Here,
                            the quartiles is provided as an ordered list of
                            quartile values for the scanned data, occurring
                            in order Q1, median, Q3.
                        max_ (float):
                            Output only. Maximum of non-null values in
                            the scanned data. NaN, if the field has a NaN.
                    """

                    average: float = proto.Field(
                        proto.DOUBLE,
                        number=1,
                    )
                    standard_deviation: float = proto.Field(
                        proto.DOUBLE,
                        number=3,
                    )
                    min_: float = proto.Field(
                        proto.DOUBLE,
                        number=4,
                    )
                    quartiles: MutableSequence[float] = proto.RepeatedField(
                        proto.DOUBLE,
                        number=6,
                    )
                    max_: float = proto.Field(
                        proto.DOUBLE,
                        number=5,
                    )

                class TopNValue(proto.Message):
                    r"""Top N non-null values in the scanned data.

                    Attributes:
                        value (str):
                            Output only. String value of a top N non-null
                            value.
                        count (int):
                            Output only. Count of the corresponding value
                            in the scanned data.
                        ratio (float):
                            Output only. Ratio of the corresponding value
                            in the field against the total number of rows in
                            the scanned data.
                    """

                    value: str = proto.Field(
                        proto.STRING,
                        number=1,
                    )
                    count: int = proto.Field(
                        proto.INT64,
                        number=2,
                    )
                    ratio: float = proto.Field(
                        proto.DOUBLE,
                        number=3,
                    )

                null_ratio: float = proto.Field(
                    proto.DOUBLE,
                    number=2,
                )
                distinct_ratio: float = proto.Field(
                    proto.DOUBLE,
                    number=3,
                )
                top_n_values: MutableSequence[
                    "DataProfileResult.Profile.Field.ProfileInfo.TopNValue"
                ] = proto.RepeatedField(
                    proto.MESSAGE,
                    number=4,
                    message="DataProfileResult.Profile.Field.ProfileInfo.TopNValue",
                )
                string_profile: "DataProfileResult.Profile.Field.ProfileInfo.StringFieldInfo" = proto.Field(
                    proto.MESSAGE,
                    number=101,
                    oneof="field_info",
                    message="DataProfileResult.Profile.Field.ProfileInfo.StringFieldInfo",
                )
                integer_profile: "DataProfileResult.Profile.Field.ProfileInfo.IntegerFieldInfo" = proto.Field(
                    proto.MESSAGE,
                    number=102,
                    oneof="field_info",
                    message="DataProfileResult.Profile.Field.ProfileInfo.IntegerFieldInfo",
                )
                double_profile: "DataProfileResult.Profile.Field.ProfileInfo.DoubleFieldInfo" = proto.Field(
                    proto.MESSAGE,
                    number=103,
                    oneof="field_info",
                    message="DataProfileResult.Profile.Field.ProfileInfo.DoubleFieldInfo",
                )

            name: str = proto.Field(
                proto.STRING,
                number=1,
            )
            type_: str = proto.Field(
                proto.STRING,
                number=2,
            )
            mode: str = proto.Field(
                proto.STRING,
                number=3,
            )
            profile: "DataProfileResult.Profile.Field.ProfileInfo" = proto.Field(
                proto.MESSAGE,
                number=4,
                message="DataProfileResult.Profile.Field.ProfileInfo",
            )

        fields: MutableSequence["DataProfileResult.Profile.Field"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=2,
                message="DataProfileResult.Profile.Field",
            )
        )

    class PostScanActionsResult(proto.Message):
        r"""The result of post scan actions of DataProfileScan job.

        Attributes:
            bigquery_export_result (google.cloud.dataplex_v1.types.DataProfileResult.PostScanActionsResult.BigQueryExportResult):
                Output only. The result of BigQuery export
                post scan action.
        """

        class BigQueryExportResult(proto.Message):
            r"""The result of BigQuery export post scan action.

            Attributes:
                state (google.cloud.dataplex_v1.types.DataProfileResult.PostScanActionsResult.BigQueryExportResult.State):
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

            state: "DataProfileResult.PostScanActionsResult.BigQueryExportResult.State" = proto.Field(
                proto.ENUM,
                number=1,
                enum="DataProfileResult.PostScanActionsResult.BigQueryExportResult.State",
            )
            message: str = proto.Field(
                proto.STRING,
                number=2,
            )

        bigquery_export_result: "DataProfileResult.PostScanActionsResult.BigQueryExportResult" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="DataProfileResult.PostScanActionsResult.BigQueryExportResult",
        )

    row_count: int = proto.Field(
        proto.INT64,
        number=3,
    )
    profile: Profile = proto.Field(
        proto.MESSAGE,
        number=4,
        message=Profile,
    )
    scanned_data: processing.ScannedData = proto.Field(
        proto.MESSAGE,
        number=5,
        message=processing.ScannedData,
    )
    post_scan_actions_result: PostScanActionsResult = proto.Field(
        proto.MESSAGE,
        number=6,
        message=PostScanActionsResult,
    )
    catalog_publishing_status: datascans_common.DataScanCatalogPublishingStatus = (
        proto.Field(
            proto.MESSAGE,
            number=7,
            message=datascans_common.DataScanCatalogPublishingStatus,
        )
    )


__all__ = tuple(sorted(__protobuf__.manifest))
