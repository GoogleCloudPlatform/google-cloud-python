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

import google.protobuf.any_pb2 as any_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.type.date_pb2 as date_pb2  # type: ignore
import google.type.interval_pb2 as interval_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.chronicle.v1",
    manifest={
        "LanguageFeature",
        "FilterOperator",
        "DataSource",
        "TimeUnit",
        "DashboardQuery",
        "GetDashboardQueryRequest",
        "ExecuteDashboardQueryRequest",
        "QueryRuntimeError",
        "ExecuteDashboardQueryResponse",
        "DashboardFilter",
        "FilterOperatorAndValues",
        "AdvancedFilterConfig",
        "InAppLink",
        "ColumnMetadata",
        "TimestampMetadata",
    },
)


class LanguageFeature(proto.Enum):
    r"""A language feature describes a specific capability or syntax of the
    query language used in a dashboard query, such as ``JOINS``,
    ``STAGES``, or ``DATA_TABLES``.

    Values:
        LANGUAGE_FEATURE_UNSPECIFIED (0):
            Language feature is unknown.
        JOINS (1):
            Language feature is joins.
        STAGES (2):
            Language feature is stages.
        DATA_TABLES (3):
            Language feature is data table.
    """

    LANGUAGE_FEATURE_UNSPECIFIED = 0
    JOINS = 1
    STAGES = 2
    DATA_TABLES = 3


class FilterOperator(proto.Enum):
    r"""

    Values:
        FILTER_OPERATOR_UNSPECIFIED (0):
            Default unspecified.
        EQUAL (1):
            No description available.
        NOT_EQUAL (2):
            No description available.
        IN (3):
            No description available.
        GREATER_THAN (4):
            No description available.
        GREATER_THAN_OR_EQUAL_TO (5):
            No description available.
        LESS_THAN (6):
            No description available.
        LESS_THAN_OR_EQUAL_TO (7):
            No description available.
        BETWEEN (8):
            No description available.
        PAST (9):
            No description available.
        IS_NULL (10):
            No description available.
        IS_NOT_NULL (11):
            No description available.
        STARTS_WITH (12):
            No description available.
        ENDS_WITH (13):
            No description available.
        DOES_NOT_STARTS_WITH (14):
            No description available.
        DOES_NOT_ENDS_WITH (15):
            No description available.
        NOT_IN (16):
            No description available.
        CONTAINS (17):
            CONTAINS is used for substring match.
        DOES_NOT_CONTAIN (18):
            Used if we want to check if the field does
            not contain the substring.
    """

    FILTER_OPERATOR_UNSPECIFIED = 0
    EQUAL = 1
    NOT_EQUAL = 2
    IN = 3
    GREATER_THAN = 4
    GREATER_THAN_OR_EQUAL_TO = 5
    LESS_THAN = 6
    LESS_THAN_OR_EQUAL_TO = 7
    BETWEEN = 8
    PAST = 9
    IS_NULL = 10
    IS_NOT_NULL = 11
    STARTS_WITH = 12
    ENDS_WITH = 13
    DOES_NOT_STARTS_WITH = 14
    DOES_NOT_ENDS_WITH = 15
    NOT_IN = 16
    CONTAINS = 17
    DOES_NOT_CONTAIN = 18


class DataSource(proto.Enum):
    r"""LINT.IfChange(data_sources)

    Values:
        DATA_SOURCE_UNSPECIFIED (0):
            No description available.
        UDM (1):
            No description available.
        ENTITY (2):
            No description available.
        INGESTION_METRICS (3):
            No description available.
        RULE_DETECTIONS (4):
            RULE_DETECTIONS is used for detections datasource.
        RULESETS (5):
            RULESETS is used for ruleset with detections
            datasource.
        GLOBAL (6):
            GLOBAL is used for standard time range
            filter.
        IOC_MATCHES (7):
            IOC_MATCHES is used for ioc_matches datasource.
        RULES (8):
            RULES is used for rules datasource.
        SOAR_CASES (9):
            SOAR Cases - identified as ``case``.
        SOAR_PLAYBOOKS (10):
            SOAR Playbooks - identified as ``playbook``.
        SOAR_CASE_HISTORY (11):
            SOAR Case History - identified as ``case_history``.
        DATA_TABLE (12):
            DATA_TABLE is used for data tables source.
        INVESTIGATION (13):
            INVESTIGATION is used as the data source for triage agent
            investigations. Identified as ``gemini_investigation``.
        INVESTIGATION_FEEDBACK (14):
            INVESTIGATION_FEEDBACK is used as the data source for user
            feedback on triage agent investigations. Identified as
            ``gemini_investigation_feedback``.
    """

    DATA_SOURCE_UNSPECIFIED = 0
    UDM = 1
    ENTITY = 2
    INGESTION_METRICS = 3
    RULE_DETECTIONS = 4
    RULESETS = 5
    GLOBAL = 6
    IOC_MATCHES = 7
    RULES = 8
    SOAR_CASES = 9
    SOAR_PLAYBOOKS = 10
    SOAR_CASE_HISTORY = 11
    DATA_TABLE = 12
    INVESTIGATION = 13
    INVESTIGATION_FEEDBACK = 14


class TimeUnit(proto.Enum):
    r"""TimeUnit supported for PAST filter operator.

    Values:
        TIME_UNIT_UNSPECIFIED (0):
            Default unspecified.
        SECOND (1):
            No description available.
        MINUTE (2):
            No description available.
        HOUR (3):
            No description available.
        DAY (4):
            No description available.
        WEEK (5):
            No description available.
        MONTH (6):
            No description available.
        YEAR (7):
            No description available.
    """

    TIME_UNIT_UNSPECIFIED = 0
    SECOND = 1
    MINUTE = 2
    HOUR = 3
    DAY = 4
    WEEK = 5
    MONTH = 6
    YEAR = 7


class DashboardQuery(proto.Message):
    r"""DashboardQuery resource.

    Attributes:
        name (str):
            Output only. Name of the dashboardQuery.
        query (str):
            Required. Search query string.
        input (google.cloud.chronicle_v1.types.DashboardQuery.Input):
            Required. Inputs to the query.
        dashboard_chart (str):
            Output only. DashboardChart this query
            belongs to.
        etag (str):
            Optional. This checksum is computed by the
            server based on the value of other fields, and
            may be sent on update and delete requests to
            ensure the client has an up-to-date value before
            proceeding.
    """

    class Input(proto.Message):
        r"""Input to the query like time window.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            time_window (google.type.interval_pb2.Interval):
                time range to fetch the data for.

                This field is a member of `oneof`_ ``time_input``.
            relative_time (google.cloud.chronicle_v1.types.DashboardQuery.Input.RelativeTime):
                time range for last x units.

                This field is a member of `oneof`_ ``time_input``.
        """

        class RelativeTime(proto.Message):
            r"""time representation for last x units.

            Attributes:
                time_unit (google.cloud.chronicle_v1.types.TimeUnit):

                start_time_val (int):

            """

            time_unit: "TimeUnit" = proto.Field(
                proto.ENUM,
                number=1,
                enum="TimeUnit",
            )
            start_time_val: int = proto.Field(
                proto.INT64,
                number=2,
            )

        time_window: interval_pb2.Interval = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="time_input",
            message=interval_pb2.Interval,
        )
        relative_time: "DashboardQuery.Input.RelativeTime" = proto.Field(
            proto.MESSAGE,
            number=3,
            oneof="time_input",
            message="DashboardQuery.Input.RelativeTime",
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    query: str = proto.Field(
        proto.STRING,
        number=2,
    )
    input: Input = proto.Field(
        proto.MESSAGE,
        number=3,
        message=Input,
    )
    dashboard_chart: str = proto.Field(
        proto.STRING,
        number=4,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=5,
    )


class GetDashboardQueryRequest(proto.Message):
    r"""Request message to get a dashboard query.

    Attributes:
        name (str):
            Required. The name of the dashboardQuery to
            retrieve. Format:

            projects/{project}/locations/{location}/instances/{instance}/dashboardQueries/{query}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ExecuteDashboardQueryRequest(proto.Message):
    r"""Request message to execute a dashboard query.

    Attributes:
        parent (str):
            Required. The parent, under which to run this
            dashboardQuery. Format:
            projects/{project}/locations/{location}/instances/{instance}
        query (google.cloud.chronicle_v1.types.DashboardQuery):
            Required. The query to execute and get results back for.
            QueryID or 'query', 'input.time_window' fields will be used.
            Use 'native_dashboard' and 'dashboard_chart' fields if it is
            an in-dashboard query.
        filters (MutableSequence[google.cloud.chronicle_v1.types.DashboardFilter]):
            Optional. Dashboard level filters other than
            query string.
        clear_cache (bool):
            Optional. When true, the backend would read
            from the database, rather than fetching data
            directly from the cache.
        use_previous_time_range (bool):
            Optional. When true, the backend will execute
            the query against the previous time range of the
            query.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    query: "DashboardQuery" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="DashboardQuery",
    )
    filters: MutableSequence["DashboardFilter"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="DashboardFilter",
    )
    clear_cache: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    use_previous_time_range: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class QueryRuntimeError(proto.Message):
    r"""Runtime error for a dashboard query.

    Attributes:
        error_title (str):
            Short Description of the error.
        error_description (str):
            Error message
        error_severity (google.cloud.chronicle_v1.types.QueryRuntimeError.ErrorSeverity):
            Severity of the error.
        metadata (MutableSequence[google.cloud.chronicle_v1.types.QueryRuntimeError.QueryRuntimeErrorMetadata]):
            Metadata for the error.
        warning_reason (google.cloud.chronicle_v1.types.QueryRuntimeError.WarningReason):
            Reason for the error.
    """

    class ErrorSeverity(proto.Enum):
        r"""Based on ErrorSeverity, UI will choose to format the error
        differently.

        Values:
            ERROR_SEVERITY_UNSPECIFIED (0):
                Severity is unknown.
            WARNING (1):
                Severity is warning.
            SEVERE (2):
                Error is severe.
        """

        ERROR_SEVERITY_UNSPECIFIED = 0
        WARNING = 1
        SEVERE = 2

    class MetadataKey(proto.Enum):
        r"""Metadata enum to identify the metadata key.

        Values:
            METADATA_KEY_UNSPECIFIED (0):
                Key is unknown.
            ROW_LIMIT (1):
                Key is row limit.
        """

        METADATA_KEY_UNSPECIFIED = 0
        ROW_LIMIT = 1

    class WarningReason(proto.Enum):
        r"""Warning reason.

        Values:
            WARNING_REASON_UNSPECIFIED (0):
                Reason is unknown.
            ROW_LIMIT_EXCEEDED (1):
                Reason is row limit exceeded.
            DEFAULT_ROW_LIMIT_EXCEEDED (2):
                Reason is default row limit exceeded.
            CURATED_QUERY_DEFAULT_ROW_LIMIT_EXCEEDED (3):
                Reason is curated query default row limit
                exceeded.
        """

        WARNING_REASON_UNSPECIFIED = 0
        ROW_LIMIT_EXCEEDED = 1
        DEFAULT_ROW_LIMIT_EXCEEDED = 2
        CURATED_QUERY_DEFAULT_ROW_LIMIT_EXCEEDED = 3

    class QueryRuntimeErrorMetadata(proto.Message):
        r"""Metadata for the error.

        Attributes:
            key (google.cloud.chronicle_v1.types.QueryRuntimeError.MetadataKey):
                Metadata key.
            value (str):
                Metadata value.
        """

        key: "QueryRuntimeError.MetadataKey" = proto.Field(
            proto.ENUM,
            number=1,
            enum="QueryRuntimeError.MetadataKey",
        )
        value: str = proto.Field(
            proto.STRING,
            number=2,
        )

    error_title: str = proto.Field(
        proto.STRING,
        number=1,
    )
    error_description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    error_severity: ErrorSeverity = proto.Field(
        proto.ENUM,
        number=3,
        enum=ErrorSeverity,
    )
    metadata: MutableSequence[QueryRuntimeErrorMetadata] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=QueryRuntimeErrorMetadata,
    )
    warning_reason: WarningReason = proto.Field(
        proto.ENUM,
        number=5,
        enum=WarningReason,
    )


class ExecuteDashboardQueryResponse(proto.Message):
    r"""Response message for executing a dashboard query.

    Attributes:
        results (MutableSequence[google.cloud.chronicle_v1.types.ExecuteDashboardQueryResponse.ColumnData]):
            Result rows that are queried.
        data_sources (MutableSequence[google.cloud.chronicle_v1.types.DataSource]):
            Datasource of the query and results.
        last_backend_cache_refreshed_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. Last time the cache was refreshed.
            This would be used by the UI to show the last
            updated time.
        time_window (google.type.interval_pb2.Interval):
            Time window against which query was executed.
        query_runtime_errors (MutableSequence[google.cloud.chronicle_v1.types.QueryRuntimeError]):
            Runtime errors
        language_features (MutableSequence[google.cloud.chronicle_v1.types.LanguageFeature]):
            Optional. Language features found in the
            query.
    """

    class ColumnValue(proto.Message):
        r"""LINT.IfChange(stats_data) Value of the column based on data type.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            null_val (bool):
                True if the value is NULL.

                This field is a member of `oneof`_ ``value``.
            bool_val (bool):
                Boolean value.

                This field is a member of `oneof`_ ``value``.
            bytes_val (bytes):
                Bytes value.

                This field is a member of `oneof`_ ``value``.
            double_val (float):
                Double value.

                This field is a member of `oneof`_ ``value``.
            int64_val (int):
                Integer value (signed).

                This field is a member of `oneof`_ ``value``.
            uint64_val (int):
                Un-signed integer value.

                This field is a member of `oneof`_ ``value``.
            string_val (str):
                String value. Enum values are returned as
                strings.

                This field is a member of `oneof`_ ``value``.
            timestamp_val (google.protobuf.timestamp_pb2.Timestamp):
                Timestamp values. Does not handle ``interval``.

                This field is a member of `oneof`_ ``value``.
            date_val (google.type.date_pb2.Date):
                Date values.

                This field is a member of `oneof`_ ``value``.
            proto_val (google.protobuf.any_pb2.Any):
                For any proto values that are not any of the
                above.

                This field is a member of `oneof`_ ``value``.
            metadata (google.cloud.chronicle_v1.types.ExecuteDashboardQueryResponse.ColumnValue.ValueMetadata):

        """

        class ValueMetadata(proto.Message):
            r"""

            Attributes:
                links (MutableSequence[google.cloud.chronicle_v1.types.InAppLink]):
                    "Auto" generated In-app links.
                field_paths (MutableSequence[str]):

                timestamp_val (google.protobuf.timestamp_pb2.Timestamp):
                    Timestamp value to store the timestamp for
                    the case of the date and time data type.
            """

            links: MutableSequence["InAppLink"] = proto.RepeatedField(
                proto.MESSAGE,
                number=1,
                message="InAppLink",
            )
            field_paths: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=2,
            )
            timestamp_val: timestamp_pb2.Timestamp = proto.Field(
                proto.MESSAGE,
                number=3,
                message=timestamp_pb2.Timestamp,
            )

        null_val: bool = proto.Field(
            proto.BOOL,
            number=1,
            oneof="value",
        )
        bool_val: bool = proto.Field(
            proto.BOOL,
            number=2,
            oneof="value",
        )
        bytes_val: bytes = proto.Field(
            proto.BYTES,
            number=3,
            oneof="value",
        )
        double_val: float = proto.Field(
            proto.DOUBLE,
            number=4,
            oneof="value",
        )
        int64_val: int = proto.Field(
            proto.INT64,
            number=5,
            oneof="value",
        )
        uint64_val: int = proto.Field(
            proto.UINT64,
            number=6,
            oneof="value",
        )
        string_val: str = proto.Field(
            proto.STRING,
            number=7,
            oneof="value",
        )
        timestamp_val: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=8,
            oneof="value",
            message=timestamp_pb2.Timestamp,
        )
        date_val: date_pb2.Date = proto.Field(
            proto.MESSAGE,
            number=9,
            oneof="value",
            message=date_pb2.Date,
        )
        proto_val: any_pb2.Any = proto.Field(
            proto.MESSAGE,
            number=10,
            oneof="value",
            message=any_pb2.Any,
        )
        metadata: "ExecuteDashboardQueryResponse.ColumnValue.ValueMetadata" = (
            proto.Field(
                proto.MESSAGE,
                number=11,
                message="ExecuteDashboardQueryResponse.ColumnValue.ValueMetadata",
            )
        )

    class ColumnType(proto.Message):
        r"""Singular vs list of values in a column.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            value (google.cloud.chronicle_v1.types.ExecuteDashboardQueryResponse.ColumnValue):
                Single value in a column.

                This field is a member of `oneof`_ ``type``.
            list_ (google.cloud.chronicle_v1.types.ExecuteDashboardQueryResponse.ColumnType.List):
                List of values in a column e.g. IPs

                This field is a member of `oneof`_ ``type``.
        """

        class List(proto.Message):
            r"""Store list of values in a column.

            Attributes:
                values (MutableSequence[google.cloud.chronicle_v1.types.ExecuteDashboardQueryResponse.ColumnValue]):

            """

            values: MutableSequence["ExecuteDashboardQueryResponse.ColumnValue"] = (
                proto.RepeatedField(
                    proto.MESSAGE,
                    number=1,
                    message="ExecuteDashboardQueryResponse.ColumnValue",
                )
            )

        value: "ExecuteDashboardQueryResponse.ColumnValue" = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="type",
            message="ExecuteDashboardQueryResponse.ColumnValue",
        )
        list_: "ExecuteDashboardQueryResponse.ColumnType.List" = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="type",
            message="ExecuteDashboardQueryResponse.ColumnType.List",
        )

    class ColumnData(proto.Message):
        r"""

        Attributes:
            column (str):
                Used to store column names.
            values (MutableSequence[google.cloud.chronicle_v1.types.ExecuteDashboardQueryResponse.ColumnType]):
                To store column data.
            metadata (google.cloud.chronicle_v1.types.ColumnMetadata):
                To store column metadata.
        """

        column: str = proto.Field(
            proto.STRING,
            number=1,
        )
        values: MutableSequence["ExecuteDashboardQueryResponse.ColumnType"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=2,
                message="ExecuteDashboardQueryResponse.ColumnType",
            )
        )
        metadata: "ColumnMetadata" = proto.Field(
            proto.MESSAGE,
            number=3,
            message="ColumnMetadata",
        )

    results: MutableSequence[ColumnData] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=ColumnData,
    )
    data_sources: MutableSequence["DataSource"] = proto.RepeatedField(
        proto.ENUM,
        number=3,
        enum="DataSource",
    )
    last_backend_cache_refreshed_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    time_window: interval_pb2.Interval = proto.Field(
        proto.MESSAGE,
        number=5,
        message=interval_pb2.Interval,
    )
    query_runtime_errors: MutableSequence["QueryRuntimeError"] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message="QueryRuntimeError",
    )
    language_features: MutableSequence["LanguageFeature"] = proto.RepeatedField(
        proto.ENUM,
        number=7,
        enum="LanguageFeature",
    )


class DashboardFilter(proto.Message):
    r"""Dashboard level filter that can be used in native dashboards
    as well as inputs to execute query.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        id (str):
            ID of the filter.
        data_source (google.cloud.chronicle_v1.types.DataSource):
            Datasource the filter is applicable for.
        field_path (str):
            Filter field path.
        filter_operator_and_field_values (MutableSequence[google.cloud.chronicle_v1.types.FilterOperatorAndValues]):
            Operator and values. Can include multiple
            modifiers.
        display_name (str):
            Display name of the filter.
        chart_ids (MutableSequence[str]):
            Chart IDs the filter is applicable for.
        is_standard_time_range_filter (bool):
            Optional. Whether the filter is a standard
            time range filter, meaning that it has to be
            used as the query time range, and not as a
            predicate in the query.
            A chart can have at most one standard time range
            filter applied.
        is_mandatory (bool):
            Optional. Whether this filter is required to
            be populated by the dashboard consumer prior to
            the dashboard loading.
        is_standard_time_range_filter_enabled (bool):
            Optional. Whether this standard time range
            filter is enabled.

            This field is a member of `oneof`_ ``_is_standard_time_range_filter_enabled``.
        advanced_filter_config (google.cloud.chronicle_v1.types.AdvancedFilterConfig):
            Optional. Advanced filter configuration for
            the filter widget.
    """

    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    data_source: "DataSource" = proto.Field(
        proto.ENUM,
        number=2,
        enum="DataSource",
    )
    field_path: str = proto.Field(
        proto.STRING,
        number=3,
    )
    filter_operator_and_field_values: MutableSequence["FilterOperatorAndValues"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=4,
            message="FilterOperatorAndValues",
        )
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=5,
    )
    chart_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    is_standard_time_range_filter: bool = proto.Field(
        proto.BOOL,
        number=7,
    )
    is_mandatory: bool = proto.Field(
        proto.BOOL,
        number=8,
    )
    is_standard_time_range_filter_enabled: bool = proto.Field(
        proto.BOOL,
        number=9,
        optional=True,
    )
    advanced_filter_config: "AdvancedFilterConfig" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="AdvancedFilterConfig",
    )


class FilterOperatorAndValues(proto.Message):
    r"""

    Attributes:
        filter_operator (google.cloud.chronicle_v1.types.FilterOperator):
            Operator for a single filter modifier.
        field_values (MutableSequence[str]):
            Values for the modifier. All operators should
            have a single value other than 'IN' and
            'BETWEEN'. 'PAST' will have negative seconds
            like -86400 is past 1 day.
    """

    filter_operator: "FilterOperator" = proto.Field(
        proto.ENUM,
        number=1,
        enum="FilterOperator",
    )
    field_values: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class AdvancedFilterConfig(proto.Message):
    r"""Advanced filter configuration for the filter widget.

    Attributes:
        token (str):
            Required. The token name to look for in the
            query (e.g., "hostname"). The system will
            automatically wrap this in '$' (e.g.,
            "$hostname$").
        prefix (str):
            Optional. String to prepend to the final
            replaced value (e.g., "/", "^(", "\"").
        suffix (str):
            Optional. String to append to the final
            replaced value (e.g., "/", ")$", "\"").
        separator (str):
            Optional. Delimiter to join multiple selected values (e.g.,
            "\|", " OR field = ").
        multiple_allowed (bool):
            Optional. Whether to allow selection of
            multiple values.
        default_values (MutableSequence[str]):
            Optional. Default values to use if no value
            is selected/provided.
        skip_default_affixes (bool):
            Optional. Whether to skip the configured
            prefix and suffix when using default values. If
            true, default values are inserted raw (joined by
            the separator).
        value_source (google.cloud.chronicle_v1.types.AdvancedFilterConfig.ValueSource):
            Required. Source of the values for the
            filter.
    """

    class ValueSource(proto.Message):
        r"""Source of the values for the filter.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            manual_options (google.cloud.chronicle_v1.types.AdvancedFilterConfig.ManualOptions):
                Optional. Manual options provided by the
                user.

                This field is a member of `oneof`_ ``source``.
            query_options (google.cloud.chronicle_v1.types.AdvancedFilterConfig.QueryOptions):
                Optional. Query options to fetch the values
                from the query engine. This is used for the
                filter's population query.

                This field is a member of `oneof`_ ``source``.
        """

        manual_options: "AdvancedFilterConfig.ManualOptions" = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="source",
            message="AdvancedFilterConfig.ManualOptions",
        )
        query_options: "AdvancedFilterConfig.QueryOptions" = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="source",
            message="AdvancedFilterConfig.QueryOptions",
        )

    class ManualOptions(proto.Message):
        r"""Manual options provided by the user.

        Attributes:
            options (MutableSequence[str]):
                Optional. The options provided by the user.
                The max number of options is limited to 10000.
        """

        options: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )

    class QueryOptions(proto.Message):
        r"""Query options to fetch the values from the query engine.
        This is used for the filter's population query.

        Attributes:
            query (str):
                Required. The query to execute to fetch the
                values.
            column (str):
                Required. The column name to use for the
                values.
            global_time_filter_enabled (bool):
                Optional. Enable global time filter
            input (google.cloud.chronicle_v1.types.DashboardQuery.Input):
                Optional. Time range input specifically for
                the filter's population query.
        """

        query: str = proto.Field(
            proto.STRING,
            number=1,
        )
        column: str = proto.Field(
            proto.STRING,
            number=2,
        )
        global_time_filter_enabled: bool = proto.Field(
            proto.BOOL,
            number=3,
        )
        input: "DashboardQuery.Input" = proto.Field(
            proto.MESSAGE,
            number=4,
            message="DashboardQuery.Input",
        )

    token: str = proto.Field(
        proto.STRING,
        number=1,
    )
    prefix: str = proto.Field(
        proto.STRING,
        number=2,
    )
    suffix: str = proto.Field(
        proto.STRING,
        number=3,
    )
    separator: str = proto.Field(
        proto.STRING,
        number=4,
    )
    multiple_allowed: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    default_values: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    skip_default_affixes: bool = proto.Field(
        proto.BOOL,
        number=7,
    )
    value_source: ValueSource = proto.Field(
        proto.MESSAGE,
        number=8,
        message=ValueSource,
    )


class InAppLink(proto.Message):
    r"""In app linking start

    Attributes:
        url (str):
            URL to redirect to.
        label (str):
            Label for the link.
        icon_url (str):
            Icon url for the link.
    """

    url: str = proto.Field(
        proto.STRING,
        number=1,
    )
    label: str = proto.Field(
        proto.STRING,
        number=2,
    )
    icon_url: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ColumnMetadata(proto.Message):
    r"""Metadata of the column.

    Attributes:
        column (str):
            Name of the column.
        field_path (str):
            Field path of the queried field, if any.
        function_name (str):
            Name of the function used to query the field,
            if any.
        function_module (str):
            Module of the function used to query the
            field, if any.
        data_source (google.cloud.chronicle_v1.types.DataSource):
            Data source queried.
        timestamp_metadata (google.cloud.chronicle_v1.types.TimestampMetadata):
            Timestamp Metadata
        longitude (bool):
            Whether the column is a longitude field.
        latitude (bool):
            Whether the column is a latitude field.
        selected (bool):
            Whether the column is selected in the final
            response.
        unselected (bool):
            Whether the column is unselected in the final
            response.
    """

    column: str = proto.Field(
        proto.STRING,
        number=1,
    )
    field_path: str = proto.Field(
        proto.STRING,
        number=2,
    )
    function_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    function_module: str = proto.Field(
        proto.STRING,
        number=4,
    )
    data_source: "DataSource" = proto.Field(
        proto.ENUM,
        number=5,
        enum="DataSource",
    )
    timestamp_metadata: "TimestampMetadata" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="TimestampMetadata",
    )
    longitude: bool = proto.Field(
        proto.BOOL,
        number=7,
    )
    latitude: bool = proto.Field(
        proto.BOOL,
        number=8,
    )
    selected: bool = proto.Field(
        proto.BOOL,
        number=9,
    )
    unselected: bool = proto.Field(
        proto.BOOL,
        number=10,
    )


class TimestampMetadata(proto.Message):
    r"""Metadata of the timestamp column.

    Attributes:
        time_format (str):
            Time format of the timestamp column.
        time_zone (str):
            Time zone of the timestamp column.
        time_granularity (str):
            Time granularity of the timestamp column.
        is_sortable (bool):
            Whether the timestamp column is sortable in
            UI.
        is_interpolable (bool):
            Whether the timestamp column is interpolable
            in UI.
    """

    time_format: str = proto.Field(
        proto.STRING,
        number=1,
    )
    time_zone: str = proto.Field(
        proto.STRING,
        number=2,
    )
    time_granularity: str = proto.Field(
        proto.STRING,
        number=3,
    )
    is_sortable: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    is_interpolable: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
