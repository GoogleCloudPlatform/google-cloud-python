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
    package="google.analytics.data.v1beta",
    manifest={
        "MetricAggregation",
        "MetricType",
        "RestrictedMetricType",
        "Compatibility",
        "DateRange",
        "MinuteRange",
        "Dimension",
        "DimensionExpression",
        "Metric",
        "Comparison",
        "FilterExpression",
        "FilterExpressionList",
        "Filter",
        "OrderBy",
        "Pivot",
        "CohortSpec",
        "Cohort",
        "CohortsRange",
        "CohortReportSettings",
        "ResponseMetaData",
        "SamplingMetadata",
        "DimensionHeader",
        "MetricHeader",
        "PivotHeader",
        "PivotDimensionHeader",
        "Row",
        "DimensionValue",
        "MetricValue",
        "NumericValue",
        "PropertyQuota",
        "QuotaStatus",
        "DimensionMetadata",
        "MetricMetadata",
        "ComparisonMetadata",
        "DimensionCompatibility",
        "MetricCompatibility",
    },
)


class MetricAggregation(proto.Enum):
    r"""Represents aggregation of metrics.

    Values:
        METRIC_AGGREGATION_UNSPECIFIED (0):
            Unspecified operator.
        TOTAL (1):
            SUM operator.
        MINIMUM (5):
            Minimum operator.
        MAXIMUM (6):
            Maximum operator.
        COUNT (4):
            Count operator.
    """

    METRIC_AGGREGATION_UNSPECIFIED = 0
    TOTAL = 1
    MINIMUM = 5
    MAXIMUM = 6
    COUNT = 4


class MetricType(proto.Enum):
    r"""A metric's value type.

    Values:
        METRIC_TYPE_UNSPECIFIED (0):
            Unspecified type.
        TYPE_INTEGER (1):
            Integer type.
        TYPE_FLOAT (2):
            Floating point type.
        TYPE_SECONDS (4):
            A duration of seconds; a special floating
            point type.
        TYPE_MILLISECONDS (5):
            A duration in milliseconds; a special
            floating point type.
        TYPE_MINUTES (6):
            A duration in minutes; a special floating
            point type.
        TYPE_HOURS (7):
            A duration in hours; a special floating point
            type.
        TYPE_STANDARD (8):
            A custom metric of standard type; a special
            floating point type.
        TYPE_CURRENCY (9):
            An amount of money; a special floating point
            type.
        TYPE_FEET (10):
            A length in feet; a special floating point
            type.
        TYPE_MILES (11):
            A length in miles; a special floating point
            type.
        TYPE_METERS (12):
            A length in meters; a special floating point
            type.
        TYPE_KILOMETERS (13):
            A length in kilometers; a special floating
            point type.
    """

    METRIC_TYPE_UNSPECIFIED = 0
    TYPE_INTEGER = 1
    TYPE_FLOAT = 2
    TYPE_SECONDS = 4
    TYPE_MILLISECONDS = 5
    TYPE_MINUTES = 6
    TYPE_HOURS = 7
    TYPE_STANDARD = 8
    TYPE_CURRENCY = 9
    TYPE_FEET = 10
    TYPE_MILES = 11
    TYPE_METERS = 12
    TYPE_KILOMETERS = 13


class RestrictedMetricType(proto.Enum):
    r"""Categories of data that you may be restricted from viewing on
    certain Google Analytics properties.

    Values:
        RESTRICTED_METRIC_TYPE_UNSPECIFIED (0):
            Unspecified type.
        COST_DATA (1):
            Cost metrics such as ``adCost``.
        REVENUE_DATA (2):
            Revenue metrics such as ``purchaseRevenue``.
    """

    RESTRICTED_METRIC_TYPE_UNSPECIFIED = 0
    COST_DATA = 1
    REVENUE_DATA = 2


class Compatibility(proto.Enum):
    r"""The compatibility types for a single dimension or metric.

    Values:
        COMPATIBILITY_UNSPECIFIED (0):
            Unspecified compatibility.
        COMPATIBLE (1):
            The dimension or metric is compatible. This
            dimension or metric can be successfully added to
            a report.
        INCOMPATIBLE (2):
            The dimension or metric is incompatible. This
            dimension or metric cannot be successfully added
            to a report.
    """

    COMPATIBILITY_UNSPECIFIED = 0
    COMPATIBLE = 1
    INCOMPATIBLE = 2


class DateRange(proto.Message):
    r"""A contiguous set of days: ``startDate``, ``startDate + 1``, ...,
    ``endDate``. Requests are allowed up to 4 date ranges.

    Attributes:
        start_date (str):
            The inclusive start date for the query in the format
            ``YYYY-MM-DD``. Cannot be after ``end_date``. The format
            ``NdaysAgo``, ``yesterday``, or ``today`` is also accepted,
            and in that case, the date is inferred based on the
            property's reporting time zone.
        end_date (str):
            The inclusive end date for the query in the format
            ``YYYY-MM-DD``. Cannot be before ``start_date``. The format
            ``NdaysAgo``, ``yesterday``, or ``today`` is also accepted,
            and in that case, the date is inferred based on the
            property's reporting time zone.
        name (str):
            Assigns a name to this date range. The dimension
            ``dateRange`` is valued to this name in a report response.
            If set, cannot begin with ``date_range_`` or ``RESERVED_``.
            If not set, date ranges are named by their zero based index
            in the request: ``date_range_0``, ``date_range_1``, etc.
    """

    start_date: str = proto.Field(
        proto.STRING,
        number=1,
    )
    end_date: str = proto.Field(
        proto.STRING,
        number=2,
    )
    name: str = proto.Field(
        proto.STRING,
        number=3,
    )


class MinuteRange(proto.Message):
    r"""A contiguous set of minutes: ``startMinutesAgo``,
    ``startMinutesAgo + 1``, ..., ``endMinutesAgo``. Requests are
    allowed up to 2 minute ranges.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        start_minutes_ago (int):
            The inclusive start minute for the query as a number of
            minutes before now. For example, ``"startMinutesAgo": 29``
            specifies the report should include event data from 29
            minutes ago and after. Cannot be after ``endMinutesAgo``.

            If unspecified, ``startMinutesAgo`` is defaulted to 29.
            Standard Analytics properties can request up to the last 30
            minutes of event data (``startMinutesAgo <= 29``), and 360
            Analytics properties can request up to the last 60 minutes
            of event data (``startMinutesAgo <= 59``).

            This field is a member of `oneof`_ ``_start_minutes_ago``.
        end_minutes_ago (int):
            The inclusive end minute for the query as a number of
            minutes before now. Cannot be before ``startMinutesAgo``.
            For example, ``"endMinutesAgo": 15`` specifies the report
            should include event data from prior to 15 minutes ago.

            If unspecified, ``endMinutesAgo`` is defaulted to 0.
            Standard Analytics properties can request any minute in the
            last 30 minutes of event data (``endMinutesAgo <= 29``), and
            360 Analytics properties can request any minute in the last
            60 minutes of event data (``endMinutesAgo <= 59``).

            This field is a member of `oneof`_ ``_end_minutes_ago``.
        name (str):
            Assigns a name to this minute range. The dimension
            ``dateRange`` is valued to this name in a report response.
            If set, cannot begin with ``date_range_`` or ``RESERVED_``.
            If not set, minute ranges are named by their zero based
            index in the request: ``date_range_0``, ``date_range_1``,
            etc.
    """

    start_minutes_ago: int = proto.Field(
        proto.INT32,
        number=1,
        optional=True,
    )
    end_minutes_ago: int = proto.Field(
        proto.INT32,
        number=2,
        optional=True,
    )
    name: str = proto.Field(
        proto.STRING,
        number=3,
    )


class Dimension(proto.Message):
    r"""Dimensions are attributes of your data. For example, the
    dimension city indicates the city from which an event
    originates. Dimension values in report responses are strings;
    for example, the city could be "Paris" or "New York". Requests
    are allowed up to 9 dimensions.

    Attributes:
        name (str):
            The name of the dimension. See the `API
            Dimensions <https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema#dimensions>`__
            for the list of dimension names supported by core reporting
            methods such as ``runReport`` and ``batchRunReports``. See
            `Realtime
            Dimensions <https://developers.google.com/analytics/devguides/reporting/data/v1/realtime-api-schema#dimensions>`__
            for the list of dimension names supported by the
            ``runRealtimeReport`` method. See `Funnel
            Dimensions <https://developers.google.com/analytics/devguides/reporting/data/v1/exploration-api-schema#dimensions>`__
            for the list of dimension names supported by the
            ``runFunnelReport`` method.

            If ``dimensionExpression`` is specified, ``name`` can be any
            string that you would like within the allowed character set.
            For example if a ``dimensionExpression`` concatenates
            ``country`` and ``city``, you could call that dimension
            ``countryAndCity``. Dimension names that you choose must
            match the regular expression ``^[a-zA-Z0-9_]$``.

            Dimensions are referenced by ``name`` in
            ``dimensionFilter``, ``orderBys``, ``dimensionExpression``,
            and ``pivots``.
        dimension_expression (google.analytics.data_v1beta.types.DimensionExpression):
            One dimension can be the result of an
            expression of multiple dimensions. For example,
            dimension "country, city": concatenate(country,
            ", ", city).
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    dimension_expression: "DimensionExpression" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="DimensionExpression",
    )


class DimensionExpression(proto.Message):
    r"""Used to express a dimension which is the result of a formula of
    multiple dimensions. Example usages:

    1) lower_case(dimension)
    2) concatenate(dimension1, symbol, dimension2).

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        lower_case (google.analytics.data_v1beta.types.DimensionExpression.CaseExpression):
            Used to convert a dimension value to lower
            case.

            This field is a member of `oneof`_ ``one_expression``.
        upper_case (google.analytics.data_v1beta.types.DimensionExpression.CaseExpression):
            Used to convert a dimension value to upper
            case.

            This field is a member of `oneof`_ ``one_expression``.
        concatenate (google.analytics.data_v1beta.types.DimensionExpression.ConcatenateExpression):
            Used to combine dimension values to a single
            dimension. For example, dimension "country,
            city": concatenate(country, ", ", city).

            This field is a member of `oneof`_ ``one_expression``.
    """

    class CaseExpression(proto.Message):
        r"""Used to convert a dimension value to a single case.

        Attributes:
            dimension_name (str):
                Name of a dimension. The name must refer back
                to a name in dimensions field of the request.
        """

        dimension_name: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class ConcatenateExpression(proto.Message):
        r"""Used to combine dimension values to a single dimension.

        Attributes:
            dimension_names (MutableSequence[str]):
                Names of dimensions. The names must refer
                back to names in the dimensions field of the
                request.
            delimiter (str):
                The delimiter placed between dimension names.

                Delimiters are often single characters such as "\|" or ","
                but can be longer strings. If a dimension value contains the
                delimiter, both will be present in response with no
                distinction. For example if dimension 1 value = "US,FR",
                dimension 2 value = "JP", and delimiter = ",", then the
                response will contain "US,FR,JP".
        """

        dimension_names: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )
        delimiter: str = proto.Field(
            proto.STRING,
            number=2,
        )

    lower_case: CaseExpression = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="one_expression",
        message=CaseExpression,
    )
    upper_case: CaseExpression = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="one_expression",
        message=CaseExpression,
    )
    concatenate: ConcatenateExpression = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="one_expression",
        message=ConcatenateExpression,
    )


class Metric(proto.Message):
    r"""The quantitative measurements of a report. For example, the metric
    ``eventCount`` is the total number of events. Requests are allowed
    up to 10 metrics.

    Attributes:
        name (str):
            The name of the metric. See the `API
            Metrics <https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema#metrics>`__
            for the list of metric names supported by core reporting
            methods such as ``runReport`` and ``batchRunReports``. See
            `Realtime
            Metrics <https://developers.google.com/analytics/devguides/reporting/data/v1/realtime-api-schema#metrics>`__
            for the list of metric names supported by the
            ``runRealtimeReport`` method. See `Funnel
            Metrics <https://developers.google.com/analytics/devguides/reporting/data/v1/exploration-api-schema#metrics>`__
            for the list of metric names supported by the
            ``runFunnelReport`` method.

            If ``expression`` is specified, ``name`` can be any string
            that you would like within the allowed character set. For
            example if ``expression`` is ``screenPageViews/sessions``,
            you could call that metric's name = ``viewsPerSession``.
            Metric names that you choose must match the regular
            expression ``^[a-zA-Z0-9_]$``.

            Metrics are referenced by ``name`` in ``metricFilter``,
            ``orderBys``, and metric ``expression``.
        expression (str):
            A mathematical expression for derived metrics. For example,
            the metric Event count per user is
            ``eventCount/totalUsers``.
        invisible (bool):
            Indicates if a metric is invisible in the report response.
            If a metric is invisible, the metric will not produce a
            column in the response, but can be used in ``metricFilter``,
            ``orderBys``, or a metric ``expression``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    expression: str = proto.Field(
        proto.STRING,
        number=2,
    )
    invisible: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class Comparison(proto.Message):
    r"""Defines an individual comparison. Most requests will include
    multiple comparisons so that the report compares between the
    comparisons.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Each comparison produces separate rows in the
            response. In the response, this comparison is
            identified by this name. If name is unspecified,
            we will use the saved comparisons display name.

            This field is a member of `oneof`_ ``_name``.
        dimension_filter (google.analytics.data_v1beta.types.FilterExpression):
            A basic comparison.

            This field is a member of `oneof`_ ``one_comparison``.
        comparison (str):
            A saved comparison identified by the
            comparison's resource name. For example,
            'comparisons/1234'.

            This field is a member of `oneof`_ ``one_comparison``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    dimension_filter: "FilterExpression" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="one_comparison",
        message="FilterExpression",
    )
    comparison: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="one_comparison",
    )


class FilterExpression(proto.Message):
    r"""To express dimension or metric filters. The fields in the
    same FilterExpression need to be either all dimensions or all
    metrics.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        and_group (google.analytics.data_v1beta.types.FilterExpressionList):
            The FilterExpressions in and_group have an AND relationship.

            This field is a member of `oneof`_ ``expr``.
        or_group (google.analytics.data_v1beta.types.FilterExpressionList):
            The FilterExpressions in or_group have an OR relationship.

            This field is a member of `oneof`_ ``expr``.
        not_expression (google.analytics.data_v1beta.types.FilterExpression):
            The FilterExpression is NOT of not_expression.

            This field is a member of `oneof`_ ``expr``.
        filter (google.analytics.data_v1beta.types.Filter):
            A primitive filter. In the same
            FilterExpression, all of the filter's field
            names need to be either all dimensions or all
            metrics.

            This field is a member of `oneof`_ ``expr``.
    """

    and_group: "FilterExpressionList" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="expr",
        message="FilterExpressionList",
    )
    or_group: "FilterExpressionList" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="expr",
        message="FilterExpressionList",
    )
    not_expression: "FilterExpression" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="expr",
        message="FilterExpression",
    )
    filter: "Filter" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="expr",
        message="Filter",
    )


class FilterExpressionList(proto.Message):
    r"""A list of filter expressions.

    Attributes:
        expressions (MutableSequence[google.analytics.data_v1beta.types.FilterExpression]):
            A list of filter expressions.
    """

    expressions: MutableSequence["FilterExpression"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="FilterExpression",
    )


class Filter(proto.Message):
    r"""An expression to filter dimension or metric values.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        field_name (str):
            The dimension name or metric name.

            In most methods, dimensions & metrics can be
            used for the first time in this field. However
            in a RunPivotReportRequest, this field must be
            additionally specified by name in the
            RunPivotReportRequest's dimensions or metrics.
        string_filter (google.analytics.data_v1beta.types.Filter.StringFilter):
            Strings related filter.

            This field is a member of `oneof`_ ``one_filter``.
        in_list_filter (google.analytics.data_v1beta.types.Filter.InListFilter):
            A filter for in list values.

            This field is a member of `oneof`_ ``one_filter``.
        numeric_filter (google.analytics.data_v1beta.types.Filter.NumericFilter):
            A filter for numeric or date values.

            This field is a member of `oneof`_ ``one_filter``.
        between_filter (google.analytics.data_v1beta.types.Filter.BetweenFilter):
            A filter for two values.

            This field is a member of `oneof`_ ``one_filter``.
        empty_filter (google.analytics.data_v1beta.types.Filter.EmptyFilter):
            A filter for empty values such as "(not set)"
            and "" values.

            This field is a member of `oneof`_ ``one_filter``.
    """

    class StringFilter(proto.Message):
        r"""The filter for string

        Attributes:
            match_type (google.analytics.data_v1beta.types.Filter.StringFilter.MatchType):
                The match type for this filter.
            value (str):
                The string value used for the matching.
            case_sensitive (bool):
                If true, the string value is case sensitive.
        """

        class MatchType(proto.Enum):
            r"""The match type of a string filter

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

        match_type: "Filter.StringFilter.MatchType" = proto.Field(
            proto.ENUM,
            number=1,
            enum="Filter.StringFilter.MatchType",
        )
        value: str = proto.Field(
            proto.STRING,
            number=2,
        )
        case_sensitive: bool = proto.Field(
            proto.BOOL,
            number=3,
        )

    class InListFilter(proto.Message):
        r"""The result needs to be in a list of string values.

        Attributes:
            values (MutableSequence[str]):
                The list of string values.
                Must be non-empty.
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

    class NumericFilter(proto.Message):
        r"""Filters for numeric or date values.

        Attributes:
            operation (google.analytics.data_v1beta.types.Filter.NumericFilter.Operation):
                The operation type for this filter.
            value (google.analytics.data_v1beta.types.NumericValue):
                A numeric value or a date value.
        """

        class Operation(proto.Enum):
            r"""The operation applied to a numeric filter

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

        operation: "Filter.NumericFilter.Operation" = proto.Field(
            proto.ENUM,
            number=1,
            enum="Filter.NumericFilter.Operation",
        )
        value: "NumericValue" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="NumericValue",
        )

    class BetweenFilter(proto.Message):
        r"""To express that the result needs to be between two numbers
        (inclusive).

        Attributes:
            from_value (google.analytics.data_v1beta.types.NumericValue):
                Begins with this number.
            to_value (google.analytics.data_v1beta.types.NumericValue):
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

    class EmptyFilter(proto.Message):
        r"""Filter for empty values."""

    field_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    string_filter: StringFilter = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="one_filter",
        message=StringFilter,
    )
    in_list_filter: InListFilter = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="one_filter",
        message=InListFilter,
    )
    numeric_filter: NumericFilter = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="one_filter",
        message=NumericFilter,
    )
    between_filter: BetweenFilter = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="one_filter",
        message=BetweenFilter,
    )
    empty_filter: EmptyFilter = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="one_filter",
        message=EmptyFilter,
    )


class OrderBy(proto.Message):
    r"""Order bys define how rows will be sorted in the response. For
    example, ordering rows by descending event count is one
    ordering, and ordering rows by the event name string is a
    different ordering.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        metric (google.analytics.data_v1beta.types.OrderBy.MetricOrderBy):
            Sorts results by a metric's values.

            This field is a member of `oneof`_ ``one_order_by``.
        dimension (google.analytics.data_v1beta.types.OrderBy.DimensionOrderBy):
            Sorts results by a dimension's values.

            This field is a member of `oneof`_ ``one_order_by``.
        pivot (google.analytics.data_v1beta.types.OrderBy.PivotOrderBy):
            Sorts results by a metric's values within a
            pivot column group.

            This field is a member of `oneof`_ ``one_order_by``.
        desc (bool):
            If true, sorts by descending order.
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
            order_type (google.analytics.data_v1beta.types.OrderBy.DimensionOrderBy.OrderType):
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
        order_type: "OrderBy.DimensionOrderBy.OrderType" = proto.Field(
            proto.ENUM,
            number=2,
            enum="OrderBy.DimensionOrderBy.OrderType",
        )

    class PivotOrderBy(proto.Message):
        r"""Sorts by a pivot column group.

        Attributes:
            metric_name (str):
                In the response to order by, order rows by
                this column. Must be a metric name from the
                request.
            pivot_selections (MutableSequence[google.analytics.data_v1beta.types.OrderBy.PivotOrderBy.PivotSelection]):
                Used to select a dimension name and value
                pivot. If multiple pivot selections are given,
                the sort occurs on rows where all pivot
                selection dimension name and value pairs match
                the row's dimension name and value pair.
        """

        class PivotSelection(proto.Message):
            r"""A pair of dimension names and values. Rows with this dimension pivot
            pair are ordered by the metric's value.

            For example if pivots = {{"browser", "Chrome"}} and metric_name =
            "Sessions", then the rows will be sorted based on Sessions in
            Chrome.

            ::

                ---------|----------|----------------|----------|----------------
                         |  Chrome  |    Chrome      |  Safari  |     Safari
                ---------|----------|----------------|----------|----------------
                 Country | Sessions | Pages/Sessions | Sessions | Pages/Sessions
                ---------|----------|----------------|----------|----------------
                    US   |    2     |       2        |     3    |        1
                ---------|----------|----------------|----------|----------------
                  Canada |    3     |       1        |     4    |        1
                ---------|----------|----------------|----------|----------------

            Attributes:
                dimension_name (str):
                    Must be a dimension name from the request.
                dimension_value (str):
                    Order by only when the named dimension is
                    this value.
            """

            dimension_name: str = proto.Field(
                proto.STRING,
                number=1,
            )
            dimension_value: str = proto.Field(
                proto.STRING,
                number=2,
            )

        metric_name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        pivot_selections: MutableSequence["OrderBy.PivotOrderBy.PivotSelection"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=2,
                message="OrderBy.PivotOrderBy.PivotSelection",
            )
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
    pivot: PivotOrderBy = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="one_order_by",
        message=PivotOrderBy,
    )
    desc: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class Pivot(proto.Message):
    r"""Describes the visible dimension columns and rows in the
    report response.

    Attributes:
        field_names (MutableSequence[str]):
            Dimension names for visible columns in the
            report response. Including "dateRange" produces
            a date range column; for each row in the
            response, dimension values in the date range
            column will indicate the corresponding date
            range from the request.
        order_bys (MutableSequence[google.analytics.data_v1beta.types.OrderBy]):
            Specifies how dimensions are ordered in the pivot. In the
            first Pivot, the OrderBys determine Row and
            PivotDimensionHeader ordering; in subsequent Pivots, the
            OrderBys determine only PivotDimensionHeader ordering.
            Dimensions specified in these OrderBys must be a subset of
            Pivot.field_names.
        offset (int):
            The row count of the start row. The first row
            is counted as row 0.
        limit (int):
            The number of unique combinations of dimension values to
            return in this pivot. The ``limit`` parameter is required. A
            ``limit`` of 10,000 is common for single pivot requests.

            The product of the ``limit`` for each ``pivot`` in a
            ``RunPivotReportRequest`` must not exceed 250,000. For
            example, a two pivot request with ``limit: 1000`` in each
            pivot will fail because the product is ``1,000,000``.
        metric_aggregations (MutableSequence[google.analytics.data_v1beta.types.MetricAggregation]):
            Aggregate the metrics by dimensions in this pivot using the
            specified metric_aggregations.
    """

    field_names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    order_bys: MutableSequence["OrderBy"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="OrderBy",
    )
    offset: int = proto.Field(
        proto.INT64,
        number=3,
    )
    limit: int = proto.Field(
        proto.INT64,
        number=4,
    )
    metric_aggregations: MutableSequence["MetricAggregation"] = proto.RepeatedField(
        proto.ENUM,
        number=5,
        enum="MetricAggregation",
    )


class CohortSpec(proto.Message):
    r"""The specification of cohorts for a cohort report.

    Cohort reports create a time series of user retention for the
    cohort. For example, you could select the cohort of users that were
    acquired in the first week of September and follow that cohort for
    the next six weeks. Selecting the users acquired in the first week
    of September cohort is specified in the ``cohort`` object. Following
    that cohort for the next six weeks is specified in the
    ``cohortsRange`` object.

    For examples, see `Cohort Report
    Examples <https://developers.google.com/analytics/devguides/reporting/data/v1/advanced#cohort_report_examples>`__.

    The report response could show a weekly time series where say your
    app has retained 60% of this cohort after three weeks and 25% of
    this cohort after six weeks. These two percentages can be calculated
    by the metric ``cohortActiveUsers/cohortTotalUsers`` and will be
    separate rows in the report.

    Attributes:
        cohorts (MutableSequence[google.analytics.data_v1beta.types.Cohort]):
            Defines the selection criteria to group users
            into cohorts.
            Most cohort reports define only a single cohort.
            If multiple cohorts are specified, each cohort
            can be recognized in the report by their name.
        cohorts_range (google.analytics.data_v1beta.types.CohortsRange):
            Cohort reports follow cohorts over an
            extended reporting date range. This range
            specifies an offset duration to follow the
            cohorts over.
        cohort_report_settings (google.analytics.data_v1beta.types.CohortReportSettings):
            Optional settings for a cohort report.
    """

    cohorts: MutableSequence["Cohort"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Cohort",
    )
    cohorts_range: "CohortsRange" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="CohortsRange",
    )
    cohort_report_settings: "CohortReportSettings" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="CohortReportSettings",
    )


class Cohort(proto.Message):
    r"""Defines a cohort selection criteria. A cohort is a group of users
    who share a common characteristic. For example, users with the same
    ``firstSessionDate`` belong to the same cohort.

    Attributes:
        name (str):
            Assigns a name to this cohort. The dimension ``cohort`` is
            valued to this name in a report response. If set, cannot
            begin with ``cohort_`` or ``RESERVED_``. If not set, cohorts
            are named by their zero based index ``cohort_0``,
            ``cohort_1``, etc.
        dimension (str):
            Dimension used by the cohort. Required and only supports
            ``firstSessionDate``.
        date_range (google.analytics.data_v1beta.types.DateRange):
            The cohort selects users whose first touch date is between
            start date and end date defined in the ``dateRange``. This
            ``dateRange`` does not specify the full date range of event
            data that is present in a cohort report. In a cohort report,
            this ``dateRange`` is extended by the granularity and offset
            present in the ``cohortsRange``; event data for the extended
            reporting date range is present in a cohort report.

            In a cohort request, this ``dateRange`` is required and the
            ``dateRanges`` in the ``RunReportRequest`` or
            ``RunPivotReportRequest`` must be unspecified.

            This ``dateRange`` should generally be aligned with the
            cohort's granularity. If ``CohortsRange`` uses daily
            granularity, this ``dateRange`` can be a single day. If
            ``CohortsRange`` uses weekly granularity, this ``dateRange``
            can be aligned to a week boundary, starting at Sunday and
            ending Saturday. If ``CohortsRange`` uses monthly
            granularity, this ``dateRange`` can be aligned to a month,
            starting at the first and ending on the last day of the
            month.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    dimension: str = proto.Field(
        proto.STRING,
        number=2,
    )
    date_range: "DateRange" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="DateRange",
    )


class CohortsRange(proto.Message):
    r"""Configures the extended reporting date range for a cohort
    report. Specifies an offset duration to follow the cohorts over.

    Attributes:
        granularity (google.analytics.data_v1beta.types.CohortsRange.Granularity):
            Required. The granularity used to interpret the
            ``startOffset`` and ``endOffset`` for the extended reporting
            date range for a cohort report.
        start_offset (int):
            ``startOffset`` specifies the start date of the extended
            reporting date range for a cohort report. ``startOffset`` is
            commonly set to 0 so that reports contain data from the
            acquisition of the cohort forward.

            If ``granularity`` is ``DAILY``, the ``startDate`` of the
            extended reporting date range is ``startDate`` of the cohort
            plus ``startOffset`` days.

            If ``granularity`` is ``WEEKLY``, the ``startDate`` of the
            extended reporting date range is ``startDate`` of the cohort
            plus ``startOffset * 7`` days.

            If ``granularity`` is ``MONTHLY``, the ``startDate`` of the
            extended reporting date range is ``startDate`` of the cohort
            plus ``startOffset * 30`` days.
        end_offset (int):
            Required. ``endOffset`` specifies the end date of the
            extended reporting date range for a cohort report.
            ``endOffset`` can be any positive integer but is commonly
            set to 5 to 10 so that reports contain data on the cohort
            for the next several granularity time periods.

            If ``granularity`` is ``DAILY``, the ``endDate`` of the
            extended reporting date range is ``endDate`` of the cohort
            plus ``endOffset`` days.

            If ``granularity`` is ``WEEKLY``, the ``endDate`` of the
            extended reporting date range is ``endDate`` of the cohort
            plus ``endOffset * 7`` days.

            If ``granularity`` is ``MONTHLY``, the ``endDate`` of the
            extended reporting date range is ``endDate`` of the cohort
            plus ``endOffset * 30`` days.
    """

    class Granularity(proto.Enum):
        r"""The granularity used to interpret the ``startOffset`` and
        ``endOffset`` for the extended reporting date range for a cohort
        report.

        Values:
            GRANULARITY_UNSPECIFIED (0):
                Should never be specified.
            DAILY (1):
                Daily granularity. Commonly used if the cohort's
                ``dateRange`` is a single day and the request contains
                ``cohortNthDay``.
            WEEKLY (2):
                Weekly granularity. Commonly used if the cohort's
                ``dateRange`` is a week in duration (starting on Sunday and
                ending on Saturday) and the request contains
                ``cohortNthWeek``.
            MONTHLY (3):
                Monthly granularity. Commonly used if the cohort's
                ``dateRange`` is a month in duration and the request
                contains ``cohortNthMonth``.
        """

        GRANULARITY_UNSPECIFIED = 0
        DAILY = 1
        WEEKLY = 2
        MONTHLY = 3

    granularity: Granularity = proto.Field(
        proto.ENUM,
        number=1,
        enum=Granularity,
    )
    start_offset: int = proto.Field(
        proto.INT32,
        number=2,
    )
    end_offset: int = proto.Field(
        proto.INT32,
        number=3,
    )


class CohortReportSettings(proto.Message):
    r"""Optional settings of a cohort report.

    Attributes:
        accumulate (bool):
            If true, accumulates the result from first touch day to the
            end day. Not supported in ``RunReportRequest``.
    """

    accumulate: bool = proto.Field(
        proto.BOOL,
        number=1,
    )


class ResponseMetaData(proto.Message):
    r"""Response's metadata carrying additional information about the
    report content.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        data_loss_from_other_row (bool):
            If true, indicates some buckets of dimension combinations
            are rolled into "(other)" row. This can happen for high
            cardinality reports.

            The metadata parameter dataLossFromOtherRow is populated
            based on the aggregated data table used in the report. The
            parameter will be accurately populated regardless of the
            filters and limits in the report.

            For example, the (other) row could be dropped from the
            report because the request contains a filter on
            sessionSource = google. This parameter will still be
            populated if data loss from other row was present in the
            input aggregate data used to generate this report.

            To learn more, see `About the (other) row and data
            sampling <https://support.google.com/analytics/answer/13208658#reports>`__.
        schema_restriction_response (google.analytics.data_v1beta.types.ResponseMetaData.SchemaRestrictionResponse):
            Describes the schema restrictions actively enforced in
            creating this report. To learn more, see `Access and
            data-restriction
            management <https://support.google.com/analytics/answer/10851388>`__.

            This field is a member of `oneof`_ ``_schema_restriction_response``.
        currency_code (str):
            The currency code used in this report. Intended to be used
            in formatting currency metrics like ``purchaseRevenue`` for
            visualization. If currency_code was specified in the
            request, this response parameter will echo the request
            parameter; otherwise, this response parameter is the
            property's current currency_code.

            Currency codes are string encodings of currency types from
            the ISO 4217 standard
            (https://en.wikipedia.org/wiki/ISO_4217); for example "USD",
            "EUR", "JPY". To learn more, see
            https://support.google.com/analytics/answer/9796179.

            This field is a member of `oneof`_ ``_currency_code``.
        time_zone (str):
            The property's current timezone. Intended to be used to
            interpret time-based dimensions like ``hour`` and
            ``minute``. Formatted as strings from the IANA Time Zone
            database (https://www.iana.org/time-zones); for example
            "America/New_York" or "Asia/Tokyo".

            This field is a member of `oneof`_ ``_time_zone``.
        empty_reason (str):
            If empty reason is specified, the report is
            empty for this reason.

            This field is a member of `oneof`_ ``_empty_reason``.
        subject_to_thresholding (bool):
            If ``subjectToThresholding`` is true, this report is subject
            to thresholding and only returns data that meets the minimum
            aggregation thresholds. It is possible for a request to be
            subject to thresholding thresholding and no data is absent
            from the report, and this happens when all data is above the
            thresholds. To learn more, see `Data
            thresholds <https://support.google.com/analytics/answer/9383630>`__.

            This field is a member of `oneof`_ ``_subject_to_thresholding``.
        sampling_metadatas (MutableSequence[google.analytics.data_v1beta.types.SamplingMetadata]):
            If this report results is
            `sampled <https://support.google.com/analytics/answer/13331292>`__,
            this describes the percentage of events used in this report.
            One ``samplingMetadatas`` is populated for each date range.
            Each ``samplingMetadatas`` corresponds to a date range in
            order that date ranges were specified in the request.

            However if the results are not sampled, this field will not
            be defined.
        data_truncation_reasons (MutableSequence[google.analytics.data_v1beta.types.ResponseMetaData.DataTruncationReason]):
            If set, indicate there is data truncation in
            the report.
    """

    class SchemaRestrictionResponse(proto.Message):
        r"""The schema restrictions actively enforced in creating this report.
        To learn more, see `Access and data-restriction
        management <https://support.google.com/analytics/answer/10851388>`__.

        Attributes:
            active_metric_restrictions (MutableSequence[google.analytics.data_v1beta.types.ResponseMetaData.SchemaRestrictionResponse.ActiveMetricRestriction]):
                All restrictions actively enforced in creating the report.
                For example, ``purchaseRevenue`` always has the restriction
                type ``REVENUE_DATA``. However, this active response
                restriction is only populated if the user's custom role
                disallows access to ``REVENUE_DATA``.
        """

        class ActiveMetricRestriction(proto.Message):
            r"""A metric actively restricted in creating the report.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                metric_name (str):
                    The name of the restricted metric.

                    This field is a member of `oneof`_ ``_metric_name``.
                restricted_metric_types (MutableSequence[google.analytics.data_v1beta.types.RestrictedMetricType]):
                    The reason for this metric's restriction.
            """

            metric_name: str = proto.Field(
                proto.STRING,
                number=1,
                optional=True,
            )
            restricted_metric_types: MutableSequence["RestrictedMetricType"] = (
                proto.RepeatedField(
                    proto.ENUM,
                    number=2,
                    enum="RestrictedMetricType",
                )
            )

        active_metric_restrictions: MutableSequence[
            "ResponseMetaData.SchemaRestrictionResponse.ActiveMetricRestriction"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="ResponseMetaData.SchemaRestrictionResponse.ActiveMetricRestriction",
        )

    class DataTruncationReason(proto.Message):
        r"""Describes a reason for data truncation in the report.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            data_truncation_type (google.analytics.data_v1beta.types.ResponseMetaData.DataTruncationReason.DataTruncationType):
                The type of data truncation.

                This field is a member of `oneof`_ ``_data_truncation_type``.
            data_truncation_message (str):
                A descriptive message explaining the data
                truncation.

                This field is a member of `oneof`_ ``_data_truncation_message``.
            data_truncation_date (str):
                The data truncation date in the format
                YYYY-MM-DD. Indicates data before this date is
                truncated.

                This field is a member of `oneof`_ ``_data_truncation_date``.
            data_truncation_date_ranges (MutableSequence[google.analytics.data_v1beta.types.ResponseMetaData.DataTruncationReason.DataTruncationDateRange]):
                The truncated date ranges.
        """

        class DataTruncationType(proto.Enum):
            r"""The type of data truncation.

            Values:
                DATA_TRUNCATION_TYPE_UNSPECIFIED (0):
                    Unspecified type.
                DATA_TRUNCATION_TYPE_RULES_BASED_MODELS (1):
                    Data is truncated in attribution report for
                    rules-based models golden date.
                DATA_TRUNCATION_TYPE_DATA_DRIVEN_ATTRIBUTION (2):
                    Data is truncated in attribution report for
                    data driven attribution golden date.
                DATA_TRUNCATION_TYPE_DV360 (3):
                    Data is truncated because DV360 policy does
                    not permit data older than 2 years from being
                    returned.
                DATA_TRUNCATION_TYPE_CM360 (4):
                    Data is truncated because CM360 policy does
                    not permit data older than 2 years from being
                    returned.
                DATA_TRUNCATION_TYPE_ITEM_SCOPED_ECOMMERCE_METRICS (5):
                    New item-scoped ecommerce metrics only have
                    data after a specific date.
                DATA_TRUNCATION_TYPE_EVENT_SCOPED_ECOMMERCE_METRICS (6):
                    New event-scoped ecommerce metrics only have
                    data after a specific date.
                DATA_TRUNCATION_TYPE_DATE_RANGE (7):
                    Query date range may not be fully served.
                DATA_TRUNCATION_TYPE_PROPERTY (8):
                    Data truncated because the query attempts to
                    read event data prior to its retention date.
                DATA_TRUNCATION_TYPE_CONVERSIONS (9):
                    Data is truncated in conversions report.
                DATA_TRUNCATION_TYPE_GOOGLE_ADS (10):
                    Data is truncated due to Google Ads 36 month
                    retention policy.
            """

            DATA_TRUNCATION_TYPE_UNSPECIFIED = 0
            DATA_TRUNCATION_TYPE_RULES_BASED_MODELS = 1
            DATA_TRUNCATION_TYPE_DATA_DRIVEN_ATTRIBUTION = 2
            DATA_TRUNCATION_TYPE_DV360 = 3
            DATA_TRUNCATION_TYPE_CM360 = 4
            DATA_TRUNCATION_TYPE_ITEM_SCOPED_ECOMMERCE_METRICS = 5
            DATA_TRUNCATION_TYPE_EVENT_SCOPED_ECOMMERCE_METRICS = 6
            DATA_TRUNCATION_TYPE_DATE_RANGE = 7
            DATA_TRUNCATION_TYPE_PROPERTY = 8
            DATA_TRUNCATION_TYPE_CONVERSIONS = 9
            DATA_TRUNCATION_TYPE_GOOGLE_ADS = 10

        class DataTruncationDateRange(proto.Message):
            r"""Define the truncated date range from start_date to end_date.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                start_date (str):
                    The start date in the format YYYY-MM-DD
                    (inclusive).

                    This field is a member of `oneof`_ ``_start_date``.
                end_date (str):
                    The end date in the format YYYY-MM-DD
                    (inclusive).

                    This field is a member of `oneof`_ ``_end_date``.
            """

            start_date: str = proto.Field(
                proto.STRING,
                number=1,
                optional=True,
            )
            end_date: str = proto.Field(
                proto.STRING,
                number=2,
                optional=True,
            )

        data_truncation_type: "ResponseMetaData.DataTruncationReason.DataTruncationType" = proto.Field(
            proto.ENUM,
            number=1,
            optional=True,
            enum="ResponseMetaData.DataTruncationReason.DataTruncationType",
        )
        data_truncation_message: str = proto.Field(
            proto.STRING,
            number=2,
            optional=True,
        )
        data_truncation_date: str = proto.Field(
            proto.STRING,
            number=3,
            optional=True,
        )
        data_truncation_date_ranges: MutableSequence[
            "ResponseMetaData.DataTruncationReason.DataTruncationDateRange"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=4,
            message="ResponseMetaData.DataTruncationReason.DataTruncationDateRange",
        )

    data_loss_from_other_row: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    schema_restriction_response: SchemaRestrictionResponse = proto.Field(
        proto.MESSAGE,
        number=4,
        optional=True,
        message=SchemaRestrictionResponse,
    )
    currency_code: str = proto.Field(
        proto.STRING,
        number=5,
        optional=True,
    )
    time_zone: str = proto.Field(
        proto.STRING,
        number=6,
        optional=True,
    )
    empty_reason: str = proto.Field(
        proto.STRING,
        number=7,
        optional=True,
    )
    subject_to_thresholding: bool = proto.Field(
        proto.BOOL,
        number=8,
        optional=True,
    )
    sampling_metadatas: MutableSequence["SamplingMetadata"] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message="SamplingMetadata",
    )
    data_truncation_reasons: MutableSequence[DataTruncationReason] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=10,
            message=DataTruncationReason,
        )
    )


class SamplingMetadata(proto.Message):
    r"""If this report results is
    `sampled <https://support.google.com/analytics/answer/13331292>`__,
    this describes the percentage of events used in this report.
    Sampling is the practice of analyzing a subset of all data in order
    to uncover the meaningful information in the larger data set.

    Attributes:
        samples_read_count (int):
            The total number of events read in this
            sampled report for a date range. This is the
            size of the subset this property's data that was
            analyzed in this report.
        sampling_space_size (int):
            The total number of events present in this property's data
            that could have been analyzed in this report for a date
            range. Sampling uncovers the meaningful information about
            the larger data set, and this is the size of the larger data
            set.

            To calculate the percentage of available data that was used
            in this report, compute
            ``samplesReadCount/samplingSpaceSize``.
    """

    samples_read_count: int = proto.Field(
        proto.INT64,
        number=1,
    )
    sampling_space_size: int = proto.Field(
        proto.INT64,
        number=2,
    )


class DimensionHeader(proto.Message):
    r"""Describes a dimension column in the report. Dimensions
    requested in a report produce column entries within rows and
    DimensionHeaders. However, dimensions used exclusively within
    filters or expressions do not produce columns in a report;
    correspondingly, those dimensions do not produce headers.

    Attributes:
        name (str):
            The dimension's name.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class MetricHeader(proto.Message):
    r"""Describes a metric column in the report. Visible metrics
    requested in a report produce column entries within rows and
    MetricHeaders. However, metrics used exclusively within filters
    or expressions do not produce columns in a report;
    correspondingly, those metrics do not produce headers.

    Attributes:
        name (str):
            The metric's name.
        type_ (google.analytics.data_v1beta.types.MetricType):
            The metric's data type.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_: "MetricType" = proto.Field(
        proto.ENUM,
        number=2,
        enum="MetricType",
    )


class PivotHeader(proto.Message):
    r"""Dimensions' values in a single pivot.

    Attributes:
        pivot_dimension_headers (MutableSequence[google.analytics.data_v1beta.types.PivotDimensionHeader]):
            The size is the same as the cardinality of
            the corresponding dimension combinations.
        row_count (int):
            The cardinality of the pivot. The total number of rows for
            this pivot's fields regardless of how the parameters
            ``offset`` and ``limit`` are specified in the request.
    """

    pivot_dimension_headers: MutableSequence["PivotDimensionHeader"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="PivotDimensionHeader",
        )
    )
    row_count: int = proto.Field(
        proto.INT32,
        number=2,
    )


class PivotDimensionHeader(proto.Message):
    r"""Summarizes dimension values from a row for this pivot.

    Attributes:
        dimension_values (MutableSequence[google.analytics.data_v1beta.types.DimensionValue]):
            Values of multiple dimensions in a pivot.
    """

    dimension_values: MutableSequence["DimensionValue"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="DimensionValue",
    )


class Row(proto.Message):
    r"""Report data for each row. For example if RunReportRequest contains:

    .. code:: none

       "dimensions": [
         {
           "name": "eventName"
         },
         {
           "name": "countryId"
         }
       ],
       "metrics": [
         {
           "name": "eventCount"
         }
       ]

    One row with 'in_app_purchase' as the eventName, 'JP' as the
    countryId, and 15 as the eventCount, would be:

    .. code:: none

       "dimensionValues": [
         {
           "value": "in_app_purchase"
         },
         {
           "value": "JP"
         }
       ],
       "metricValues": [
         {
           "value": "15"
         }
       ]

    Attributes:
        dimension_values (MutableSequence[google.analytics.data_v1beta.types.DimensionValue]):
            List of requested dimension values. In a PivotReport,
            dimension_values are only listed for dimensions included in
            a pivot.
        metric_values (MutableSequence[google.analytics.data_v1beta.types.MetricValue]):
            List of requested visible metric values.
    """

    dimension_values: MutableSequence["DimensionValue"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="DimensionValue",
    )
    metric_values: MutableSequence["MetricValue"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="MetricValue",
    )


class DimensionValue(proto.Message):
    r"""The value of a dimension.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        value (str):
            Value as a string if the dimension type is a
            string.

            This field is a member of `oneof`_ ``one_value``.
    """

    value: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="one_value",
    )


class MetricValue(proto.Message):
    r"""The value of a metric.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        value (str):
            Measurement value. See MetricHeader for type.

            This field is a member of `oneof`_ ``one_value``.
    """

    value: str = proto.Field(
        proto.STRING,
        number=4,
        oneof="one_value",
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


class PropertyQuota(proto.Message):
    r"""Current state of all quotas for this Analytics Property. If
    any quota for a property is exhausted, all requests to that
    property will return Resource Exhausted errors.

    Attributes:
        tokens_per_day (google.analytics.data_v1beta.types.QuotaStatus):
            Standard Analytics Properties can use up to
            200,000 tokens per day; Analytics 360 Properties
            can use 2,000,000 tokens per day. Most requests
            consume fewer than 10 tokens.
        tokens_per_hour (google.analytics.data_v1beta.types.QuotaStatus):
            Standard Analytics Properties can use up to
            40,000 tokens per hour; Analytics 360 Properties
            can use 400,000 tokens per hour. An API request
            consumes a single number of tokens, and that
            number is deducted from all of the hourly,
            daily, and per project hourly quotas.
        concurrent_requests (google.analytics.data_v1beta.types.QuotaStatus):
            Standard Analytics Properties can send up to
            10 concurrent requests; Analytics 360 Properties
            can use up to 50 concurrent requests.
        server_errors_per_project_per_hour (google.analytics.data_v1beta.types.QuotaStatus):
            Standard Analytics Properties and cloud
            project pairs can have up to 10 server errors
            per hour; Analytics 360 Properties and cloud
            project pairs can have up to 50 server errors
            per hour.
        potentially_thresholded_requests_per_hour (google.analytics.data_v1beta.types.QuotaStatus):
            Analytics Properties can send up to 120
            requests with potentially thresholded dimensions
            per hour. In a batch request, each report
            request is individually counted for this quota
            if the request contains potentially thresholded
            dimensions.
        tokens_per_project_per_hour (google.analytics.data_v1beta.types.QuotaStatus):
            Analytics Properties can use up to 35% of
            their tokens per project per hour. This amounts
            to standard Analytics Properties can use up to
            14,000 tokens per project per hour, and
            Analytics 360 Properties can use 140,000 tokens
            per project per hour. An API request consumes a
            single number of tokens, and that number is
            deducted from all of the hourly, daily, and per
            project hourly quotas.
    """

    tokens_per_day: "QuotaStatus" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="QuotaStatus",
    )
    tokens_per_hour: "QuotaStatus" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="QuotaStatus",
    )
    concurrent_requests: "QuotaStatus" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="QuotaStatus",
    )
    server_errors_per_project_per_hour: "QuotaStatus" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="QuotaStatus",
    )
    potentially_thresholded_requests_per_hour: "QuotaStatus" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="QuotaStatus",
    )
    tokens_per_project_per_hour: "QuotaStatus" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="QuotaStatus",
    )


class QuotaStatus(proto.Message):
    r"""Current state for a particular quota group.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        consumed (int):
            Quota consumed by this request.

            This field is a member of `oneof`_ ``_consumed``.
        remaining (int):
            Quota remaining after this request.

            This field is a member of `oneof`_ ``_remaining``.
    """

    consumed: int = proto.Field(
        proto.INT32,
        number=1,
        optional=True,
    )
    remaining: int = proto.Field(
        proto.INT32,
        number=2,
        optional=True,
    )


class DimensionMetadata(proto.Message):
    r"""Explains a dimension.

    Attributes:
        api_name (str):
            This dimension's name. Useable in
            `Dimension <#Dimension>`__'s ``name``. For example,
            ``eventName``.
        ui_name (str):
            This dimension's name within the Google Analytics user
            interface. For example, ``Event name``.
        description (str):
            Description of how this dimension is used and
            calculated.
        deprecated_api_names (MutableSequence[str]):
            Still usable but deprecated names for this dimension. If
            populated, this dimension is available by either ``apiName``
            or one of ``deprecatedApiNames`` for a period of time. After
            the deprecation period, the dimension will be available only
            by ``apiName``.
        custom_definition (bool):
            True if the dimension is custom to this
            property. This includes user, event, & item
            scoped custom dimensions; to learn more about
            custom dimensions, see
            https://support.google.com/analytics/answer/14240153.
            This also include custom channel groups; to
            learn more about custom channel groups, see
            https://support.google.com/analytics/answer/13051316.
        category (str):
            The display name of the category that this
            dimension belongs to. Similar dimensions and
            metrics are categorized together.
    """

    api_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    ui_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    deprecated_api_names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    custom_definition: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    category: str = proto.Field(
        proto.STRING,
        number=7,
    )


class MetricMetadata(proto.Message):
    r"""Explains a metric.

    Attributes:
        api_name (str):
            A metric name. Useable in `Metric <#Metric>`__'s ``name``.
            For example, ``eventCount``.
        ui_name (str):
            This metric's name within the Google Analytics user
            interface. For example, ``Event count``.
        description (str):
            Description of how this metric is used and
            calculated.
        deprecated_api_names (MutableSequence[str]):
            Still usable but deprecated names for this metric. If
            populated, this metric is available by either ``apiName`` or
            one of ``deprecatedApiNames`` for a period of time. After
            the deprecation period, the metric will be available only by
            ``apiName``.
        type_ (google.analytics.data_v1beta.types.MetricType):
            The type of this metric.
        expression (str):
            The mathematical expression for this derived metric. Can be
            used in `Metric <#Metric>`__'s ``expression`` field for
            equivalent reports. Most metrics are not expressions, and
            for non-expressions, this field is empty.
        custom_definition (bool):
            True if the metric is a custom metric for
            this property.
        blocked_reasons (MutableSequence[google.analytics.data_v1beta.types.MetricMetadata.BlockedReason]):
            If reasons are specified, your access is blocked to this
            metric for this property. API requests from you to this
            property for this metric will succeed; however, the report
            will contain only zeros for this metric. API requests with
            metric filters on blocked metrics will fail. If reasons are
            empty, you have access to this metric.

            To learn more, see `Access and data-restriction
            management <https://support.google.com/analytics/answer/10851388>`__.
        category (str):
            The display name of the category that this
            metrics belongs to. Similar dimensions and
            metrics are categorized together.
    """

    class BlockedReason(proto.Enum):
        r"""Justifications for why this metric is blocked.

        Values:
            BLOCKED_REASON_UNSPECIFIED (0):
                Will never be specified in API response.
            NO_REVENUE_METRICS (1):
                If present, your access is blocked to revenue
                related metrics for this property, and this
                metric is revenue related.
            NO_COST_METRICS (2):
                If present, your access is blocked to cost
                related metrics for this property, and this
                metric is cost related.
        """

        BLOCKED_REASON_UNSPECIFIED = 0
        NO_REVENUE_METRICS = 1
        NO_COST_METRICS = 2

    api_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    ui_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    deprecated_api_names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    type_: "MetricType" = proto.Field(
        proto.ENUM,
        number=5,
        enum="MetricType",
    )
    expression: str = proto.Field(
        proto.STRING,
        number=6,
    )
    custom_definition: bool = proto.Field(
        proto.BOOL,
        number=7,
    )
    blocked_reasons: MutableSequence[BlockedReason] = proto.RepeatedField(
        proto.ENUM,
        number=8,
        enum=BlockedReason,
    )
    category: str = proto.Field(
        proto.STRING,
        number=10,
    )


class ComparisonMetadata(proto.Message):
    r"""The metadata for a single comparison.

    Attributes:
        api_name (str):
            This comparison's resource name. Useable in
            `Comparison <#Comparison>`__'s ``comparison`` field. For
            example, 'comparisons/1234'.
        ui_name (str):
            This comparison's name within the Google
            Analytics user interface.
        description (str):
            This comparison's description.
    """

    api_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    ui_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DimensionCompatibility(proto.Message):
    r"""The compatibility for a single dimension.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        dimension_metadata (google.analytics.data_v1beta.types.DimensionMetadata):
            The dimension metadata contains the API name
            for this compatibility information. The
            dimension metadata also contains other helpful
            information like the UI name and description.

            This field is a member of `oneof`_ ``_dimension_metadata``.
        compatibility (google.analytics.data_v1beta.types.Compatibility):
            The compatibility of this dimension. If the
            compatibility is COMPATIBLE, this dimension can
            be successfully added to the report.

            This field is a member of `oneof`_ ``_compatibility``.
    """

    dimension_metadata: "DimensionMetadata" = proto.Field(
        proto.MESSAGE,
        number=1,
        optional=True,
        message="DimensionMetadata",
    )
    compatibility: "Compatibility" = proto.Field(
        proto.ENUM,
        number=2,
        optional=True,
        enum="Compatibility",
    )


class MetricCompatibility(proto.Message):
    r"""The compatibility for a single metric.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        metric_metadata (google.analytics.data_v1beta.types.MetricMetadata):
            The metric metadata contains the API name for
            this compatibility information. The metric
            metadata also contains other helpful information
            like the UI name and description.

            This field is a member of `oneof`_ ``_metric_metadata``.
        compatibility (google.analytics.data_v1beta.types.Compatibility):
            The compatibility of this metric. If the
            compatibility is COMPATIBLE, this metric can be
            successfully added to the report.

            This field is a member of `oneof`_ ``_compatibility``.
    """

    metric_metadata: "MetricMetadata" = proto.Field(
        proto.MESSAGE,
        number=1,
        optional=True,
        message="MetricMetadata",
    )
    compatibility: "Compatibility" = proto.Field(
        proto.ENUM,
        number=2,
        optional=True,
        enum="Compatibility",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
