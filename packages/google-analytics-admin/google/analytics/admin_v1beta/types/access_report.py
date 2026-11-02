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
    package="google.analytics.admin.v1beta",
    manifest={
        "AccessDimension",
        "AccessMetric",
        "AccessDateRange",
        "AccessFilterExpression",
        "AccessFilterExpressionList",
        "AccessFilter",
        "AccessStringFilter",
        "AccessInListFilter",
        "AccessNumericFilter",
        "AccessBetweenFilter",
        "NumericValue",
        "AccessOrderBy",
        "AccessDimensionHeader",
        "AccessMetricHeader",
        "AccessRow",
        "AccessDimensionValue",
        "AccessMetricValue",
        "AccessQuota",
        "AccessQuotaStatus",
    },
)


class AccessDimension(proto.Message):
    r"""Dimensions are attributes of your data. For example, the dimension
    ``userEmail`` indicates the email of the user that accessed
    reporting data. Dimension values in report responses are strings.

    Attributes:
        dimension_name (str):
            The API name of the dimension. See `Data Access
            Schema <https://developers.google.com/analytics/devguides/config/admin/v1/access-api-schema>`__
            for the list of dimensions supported in this API.

            Dimensions are referenced by name in ``dimensionFilter`` and
            ``orderBys``.
    """

    dimension_name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class AccessMetric(proto.Message):
    r"""The quantitative measurements of a report. For example, the metric
    ``accessCount`` is the total number of data access records.

    Attributes:
        metric_name (str):
            The API name of the metric. See `Data Access
            Schema <https://developers.google.com/analytics/devguides/config/admin/v1/access-api-schema>`__
            for the list of metrics supported in this API.

            Metrics are referenced by name in ``metricFilter`` &
            ``orderBys``.
    """

    metric_name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class AccessDateRange(proto.Message):
    r"""A contiguous range of days: startDate, startDate + 1, ...,
    endDate.

    Attributes:
        start_date (str):
            The inclusive start date for the query in the format
            ``YYYY-MM-DD``. Cannot be after ``endDate``. The format
            ``NdaysAgo``, ``yesterday``, or ``today`` is also accepted,
            and in that case, the date is inferred based on the current
            time in the request's time zone.
        end_date (str):
            The inclusive end date for the query in the format
            ``YYYY-MM-DD``. Cannot be before ``startDate``. The format
            ``NdaysAgo``, ``yesterday``, or ``today`` is also accepted,
            and in that case, the date is inferred based on the current
            time in the request's time zone.
    """

    start_date: str = proto.Field(
        proto.STRING,
        number=1,
    )
    end_date: str = proto.Field(
        proto.STRING,
        number=2,
    )


class AccessFilterExpression(proto.Message):
    r"""Expresses dimension or metric filters. The fields in the same
    expression need to be either all dimensions or all metrics.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        and_group (google.analytics.admin_v1beta.types.AccessFilterExpressionList):
            Each of the FilterExpressions in the and_group has an AND
            relationship.

            This field is a member of `oneof`_ ``one_expression``.
        or_group (google.analytics.admin_v1beta.types.AccessFilterExpressionList):
            Each of the FilterExpressions in the or_group has an OR
            relationship.

            This field is a member of `oneof`_ ``one_expression``.
        not_expression (google.analytics.admin_v1beta.types.AccessFilterExpression):
            The FilterExpression is NOT of not_expression.

            This field is a member of `oneof`_ ``one_expression``.
        access_filter (google.analytics.admin_v1beta.types.AccessFilter):
            A primitive filter. In the same
            FilterExpression, all of the filter's field
            names need to be either all dimensions or all
            metrics.

            This field is a member of `oneof`_ ``one_expression``.
    """

    and_group: "AccessFilterExpressionList" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="one_expression",
        message="AccessFilterExpressionList",
    )
    or_group: "AccessFilterExpressionList" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="one_expression",
        message="AccessFilterExpressionList",
    )
    not_expression: "AccessFilterExpression" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="one_expression",
        message="AccessFilterExpression",
    )
    access_filter: "AccessFilter" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="one_expression",
        message="AccessFilter",
    )


class AccessFilterExpressionList(proto.Message):
    r"""A list of filter expressions.

    Attributes:
        expressions (MutableSequence[google.analytics.admin_v1beta.types.AccessFilterExpression]):
            A list of filter expressions.
    """

    expressions: MutableSequence["AccessFilterExpression"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="AccessFilterExpression",
    )


class AccessFilter(proto.Message):
    r"""An expression to filter dimension or metric values.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        string_filter (google.analytics.admin_v1beta.types.AccessStringFilter):
            Strings related filter.

            This field is a member of `oneof`_ ``one_filter``.
        in_list_filter (google.analytics.admin_v1beta.types.AccessInListFilter):
            A filter for in list values.

            This field is a member of `oneof`_ ``one_filter``.
        numeric_filter (google.analytics.admin_v1beta.types.AccessNumericFilter):
            A filter for numeric or date values.

            This field is a member of `oneof`_ ``one_filter``.
        between_filter (google.analytics.admin_v1beta.types.AccessBetweenFilter):
            A filter for two values.

            This field is a member of `oneof`_ ``one_filter``.
        field_name (str):
            The dimension name or metric name.
    """

    string_filter: "AccessStringFilter" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="one_filter",
        message="AccessStringFilter",
    )
    in_list_filter: "AccessInListFilter" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="one_filter",
        message="AccessInListFilter",
    )
    numeric_filter: "AccessNumericFilter" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="one_filter",
        message="AccessNumericFilter",
    )
    between_filter: "AccessBetweenFilter" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="one_filter",
        message="AccessBetweenFilter",
    )
    field_name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class AccessStringFilter(proto.Message):
    r"""The filter for strings.

    Attributes:
        match_type (google.analytics.admin_v1beta.types.AccessStringFilter.MatchType):
            The match type for this filter.
        value (str):
            The string value used for the matching.
        case_sensitive (bool):
            If true, the string value is case sensitive.
    """

    class MatchType(proto.Enum):
        r"""The match type of a string filter.

        Values:
            MATCH_TYPE_UNSPECIFIED (0):
                Unspecified
            EXACT (1):
                Exact match of the string value.
            BEGINS_WITH (2):
                Begins with the string value.
            ENDS_WITH (3):
                Ends with the string value.
            CONTAINS (4):
                Contains the string value.
            FULL_REGEXP (5):
                Full match for the regular expression with
                the string value.
            PARTIAL_REGEXP (6):
                Partial match for the regular expression with
                the string value.
        """

        MATCH_TYPE_UNSPECIFIED = 0
        EXACT = 1
        BEGINS_WITH = 2
        ENDS_WITH = 3
        CONTAINS = 4
        FULL_REGEXP = 5
        PARTIAL_REGEXP = 6

    match_type: MatchType = proto.Field(
        proto.ENUM,
        number=1,
        enum=MatchType,
    )
    value: str = proto.Field(
        proto.STRING,
        number=2,
    )
    case_sensitive: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class AccessInListFilter(proto.Message):
    r"""The result needs to be in a list of string values.

    Attributes:
        values (MutableSequence[str]):
            The list of string values. Must be non-empty.
        case_sensitive (bool):
            If true, the string value is case sensitive.
    """

    values: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    case_sensitive: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class AccessNumericFilter(proto.Message):
    r"""Filters for numeric or date values.

    Attributes:
        operation (google.analytics.admin_v1beta.types.AccessNumericFilter.Operation):
            The operation type for this filter.
        value (google.analytics.admin_v1beta.types.NumericValue):
            A numeric value or a date value.
    """

    class Operation(proto.Enum):
        r"""The operation applied to a numeric filter.

        Values:
            OPERATION_UNSPECIFIED (0):
                Unspecified.
            EQUAL (1):
                Equal
            LESS_THAN (2):
                Less than
            LESS_THAN_OR_EQUAL (3):
                Less than or equal
            GREATER_THAN (4):
                Greater than
            GREATER_THAN_OR_EQUAL (5):
                Greater than or equal
        """

        OPERATION_UNSPECIFIED = 0
        EQUAL = 1
        LESS_THAN = 2
        LESS_THAN_OR_EQUAL = 3
        GREATER_THAN = 4
        GREATER_THAN_OR_EQUAL = 5

    operation: Operation = proto.Field(
        proto.ENUM,
        number=1,
        enum=Operation,
    )
    value: "NumericValue" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="NumericValue",
    )


class AccessBetweenFilter(proto.Message):
    r"""To express that the result needs to be between two numbers
    (inclusive).

    Attributes:
        from_value (google.analytics.admin_v1beta.types.NumericValue):
            Begins with this number.
        to_value (google.analytics.admin_v1beta.types.NumericValue):
            Ends with this number.
    """

    from_value: "NumericValue" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="NumericValue",
    )
    to_value: "NumericValue" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="NumericValue",
    )


class NumericValue(proto.Message):
    r"""To represent a number.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        int64_value (int):
            Integer value

            This field is a member of `oneof`_ ``one_value``.
        double_value (float):
            Double value

            This field is a member of `oneof`_ ``one_value``.
    """

    int64_value: int = proto.Field(
        proto.INT64,
        number=1,
        oneof="one_value",
    )
    double_value: float = proto.Field(
        proto.DOUBLE,
        number=2,
        oneof="one_value",
    )


class AccessOrderBy(proto.Message):
    r"""Order bys define how rows will be sorted in the response. For
    example, ordering rows by descending access count is one
    ordering, and ordering rows by the country string is a different
    ordering.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        metric (google.analytics.admin_v1beta.types.AccessOrderBy.MetricOrderBy):
            Sorts results by a metric's values.

            This field is a member of `oneof`_ ``one_order_by``.
        dimension (google.analytics.admin_v1beta.types.AccessOrderBy.DimensionOrderBy):
            Sorts results by a dimension's values.

            This field is a member of `oneof`_ ``one_order_by``.
        desc (bool):
            If true, sorts by descending order. If false
            or unspecified, sorts in ascending order.
    """

    class MetricOrderBy(proto.Message):
        r"""Sorts by metric values.

        Attributes:
            metric_name (str):
                A metric name in the request to order by.
        """

        metric_name: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class DimensionOrderBy(proto.Message):
        r"""Sorts by dimension values.

        Attributes:
            dimension_name (str):
                A dimension name in the request to order by.
            order_type (google.analytics.admin_v1beta.types.AccessOrderBy.DimensionOrderBy.OrderType):
                Controls the rule for dimension value
                ordering.
        """

        class OrderType(proto.Enum):
            r"""Rule to order the string dimension values by.

            Values:
                ORDER_TYPE_UNSPECIFIED (0):
                    Unspecified.
                ALPHANUMERIC (1):
                    Alphanumeric sort by Unicode code point. For
                    example, "2" < "A" < "X" < "b" < "z".
                CASE_INSENSITIVE_ALPHANUMERIC (2):
                    Case insensitive alphanumeric sort by lower
                    case Unicode code point. For example, "2" < "A"
                    < "b" < "X" < "z".
                NUMERIC (3):
                    Dimension values are converted to numbers before sorting.
                    For example in NUMERIC sort, "25" < "100", and in
                    ``ALPHANUMERIC`` sort, "100" < "25". Non-numeric dimension
                    values all have equal ordering value below all numeric
                    values.
            """

            ORDER_TYPE_UNSPECIFIED = 0
            ALPHANUMERIC = 1
            CASE_INSENSITIVE_ALPHANUMERIC = 2
            NUMERIC = 3

        dimension_name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        order_type: "AccessOrderBy.DimensionOrderBy.OrderType" = proto.Field(
            proto.ENUM,
            number=2,
            enum="AccessOrderBy.DimensionOrderBy.OrderType",
        )

    metric: MetricOrderBy = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="one_order_by",
        message=MetricOrderBy,
    )
    dimension: DimensionOrderBy = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="one_order_by",
        message=DimensionOrderBy,
    )
    desc: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class AccessDimensionHeader(proto.Message):
    r"""Describes a dimension column in the report. Dimensions
    requested in a report produce column entries within rows and
    DimensionHeaders. However, dimensions used exclusively within
    filters or expressions do not produce columns in a report;
    correspondingly, those dimensions do not produce headers.

    Attributes:
        dimension_name (str):
            The dimension's name; for example
            'userEmail'.
    """

    dimension_name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class AccessMetricHeader(proto.Message):
    r"""Describes a metric column in the report. Visible metrics
    requested in a report produce column entries within rows and
    MetricHeaders. However, metrics used exclusively within filters
    or expressions do not produce columns in a report;
    correspondingly, those metrics do not produce headers.

    Attributes:
        metric_name (str):
            The metric's name; for example 'accessCount'.
    """

    metric_name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class AccessRow(proto.Message):
    r"""Access report data for each row.

    Attributes:
        dimension_values (MutableSequence[google.analytics.admin_v1beta.types.AccessDimensionValue]):
            List of dimension values. These values are in
            the same order as specified in the request.
        metric_values (MutableSequence[google.analytics.admin_v1beta.types.AccessMetricValue]):
            List of metric values. These values are in
            the same order as specified in the request.
    """

    dimension_values: MutableSequence["AccessDimensionValue"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="AccessDimensionValue",
    )
    metric_values: MutableSequence["AccessMetricValue"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="AccessMetricValue",
    )


class AccessDimensionValue(proto.Message):
    r"""The value of a dimension.

    Attributes:
        value (str):
            The dimension value. For example, this value
            may be 'France' for the 'country' dimension.
    """

    value: str = proto.Field(
        proto.STRING,
        number=1,
    )


class AccessMetricValue(proto.Message):
    r"""The value of a metric.

    Attributes:
        value (str):
            The measurement value. For example, this
            value may be '13'.
    """

    value: str = proto.Field(
        proto.STRING,
        number=1,
    )


class AccessQuota(proto.Message):
    r"""Current state of all quotas for this Analytics property. If
    any quota for a property is exhausted, all requests to that
    property will return Resource Exhausted errors.

    Attributes:
        tokens_per_day (google.analytics.admin_v1beta.types.AccessQuotaStatus):
            Properties can use 250,000 tokens per day.
            Most requests consume fewer than 10 tokens.
        tokens_per_hour (google.analytics.admin_v1beta.types.AccessQuotaStatus):
            Properties can use 50,000 tokens per hour. An
            API request consumes a single number of tokens,
            and that number is deducted from all of the
            hourly, daily, and per project hourly quotas.
        concurrent_requests (google.analytics.admin_v1beta.types.AccessQuotaStatus):
            Properties can use up to 50 concurrent
            requests.
        server_errors_per_project_per_hour (google.analytics.admin_v1beta.types.AccessQuotaStatus):
            Properties and cloud project pairs can have
            up to 50 server errors per hour.
        tokens_per_project_per_hour (google.analytics.admin_v1beta.types.AccessQuotaStatus):
            Properties can use up to 25% of their tokens
            per project per hour. This amounts to Analytics
            360 Properties can use 12,500 tokens per project
            per hour. An API request consumes a single
            number of tokens, and that number is deducted
            from all of the hourly, daily, and per project
            hourly quotas.
    """

    tokens_per_day: "AccessQuotaStatus" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="AccessQuotaStatus",
    )
    tokens_per_hour: "AccessQuotaStatus" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="AccessQuotaStatus",
    )
    concurrent_requests: "AccessQuotaStatus" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="AccessQuotaStatus",
    )
    server_errors_per_project_per_hour: "AccessQuotaStatus" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="AccessQuotaStatus",
    )
    tokens_per_project_per_hour: "AccessQuotaStatus" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="AccessQuotaStatus",
    )


class AccessQuotaStatus(proto.Message):
    r"""Current state for a particular quota group.

    Attributes:
        consumed (int):
            Quota consumed by this request.
        remaining (int):
            Quota remaining after this request.
    """

    consumed: int = proto.Field(
        proto.INT32,
        number=1,
    )
    remaining: int = proto.Field(
        proto.INT32,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
