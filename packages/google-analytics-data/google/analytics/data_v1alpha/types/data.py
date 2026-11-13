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

import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.analytics.data.v1alpha",
    manifest={
        "Section",
        "UserCriteriaScoping",
        "UserExclusionDuration",
        "SessionCriteriaScoping",
        "SessionExclusionDuration",
        "EventCriteriaScoping",
        "EventExclusionDuration",
        "MetricAggregation",
        "MetricType",
        "RestrictedMetricType",
        "SamplingLevel",
        "DateRange",
        "Dimension",
        "DimensionExpression",
        "Metric",
        "Comparison",
        "FilterExpression",
        "FilterExpressionList",
        "Filter",
        "StringFilter",
        "InListFilter",
        "NumericFilter",
        "OrderBy",
        "BetweenFilter",
        "EmptyFilter",
        "NumericValue",
        "CohortSpec",
        "Cohort",
        "CohortsRange",
        "CohortReportSettings",
        "ResponseMetaData",
        "DimensionHeader",
        "MetricHeader",
        "Row",
        "DimensionValue",
        "MetricValue",
        "PropertyQuota",
        "QuotaStatus",
        "FunnelBreakdown",
        "FunnelNextAction",
        "Funnel",
        "FunnelStep",
        "FunnelSubReport",
        "ResponseBlock",
        "UserSegment",
        "UserSegmentCriteria",
        "UserSegmentConditionGroup",
        "UserSegmentSequenceGroup",
        "UserSequenceStep",
        "UserSegmentExclusion",
        "SessionSegment",
        "SessionSegmentCriteria",
        "SessionSegmentConditionGroup",
        "SessionSegmentExclusion",
        "EventSegment",
        "EventSegmentCriteria",
        "EventSegmentConditionGroup",
        "EventSegmentExclusion",
        "Segment",
        "SegmentFilterExpression",
        "SegmentFilterExpressionList",
        "SegmentFilter",
        "SegmentFilterScoping",
        "SegmentEventFilter",
        "SegmentParameterFilterExpression",
        "SegmentParameterFilterExpressionList",
        "SegmentParameterFilter",
        "SegmentParameterFilterScoping",
        "FunnelFilterExpression",
        "FunnelFilterExpressionList",
        "FunnelFieldFilter",
        "FunnelEventFilter",
        "FunnelParameterFilterExpression",
        "FunnelParameterFilterExpressionList",
        "FunnelParameterFilter",
        "FunnelResponseMetadata",
        "SamplingMetadata",
        "ConversionSpec",
        "DimensionMetadata",
        "MetricMetadata",
        "ComparisonMetadata",
        "ConversionMetadata",
        "PropertyChatQuota",
    },
)


class Section(proto.Enum):
    r"""Identifies if the report data is from the standard report
    data or conversion data

    Values:
        SECTION_UNSPECIFIED (0):
            Should never be specified.
        SECTION_REPORT (1):
            The report data is from the standard report
            data. Google Analytics reports include
            acquisition, engagement, and user behavior
            reports. Reports use dimensions like session
            source & landing page; reports use metrics like
            sessions, views, and engagement time.
        SECTION_ADVERTISING (2):
            The report data is from the conversion data.
            The Google Analytics Advertising section reports
            on conversion performance. Advertising reports
            use dimensions like source & medium; advertising
            reports use metrics like all conversions and ads
            cost.
    """

    SECTION_UNSPECIFIED = 0
    SECTION_REPORT = 1
    SECTION_ADVERTISING = 2


class UserCriteriaScoping(proto.Enum):
    r"""Scoping specifies which events are considered when evaluating
    if a user meets a criteria.

    Values:
        USER_CRITERIA_SCOPING_UNSPECIFIED (0):
            Unspecified criteria scoping. Do not specify.
        USER_CRITERIA_WITHIN_SAME_EVENT (1):
            If the criteria is satisfied within one
            event, the user matches the criteria.
        USER_CRITERIA_WITHIN_SAME_SESSION (2):
            If the criteria is satisfied within one
            session, the user matches the criteria.
        USER_CRITERIA_ACROSS_ALL_SESSIONS (3):
            If the criteria is satisfied by any events
            for the user, the user matches the criteria.
    """

    USER_CRITERIA_SCOPING_UNSPECIFIED = 0
    USER_CRITERIA_WITHIN_SAME_EVENT = 1
    USER_CRITERIA_WITHIN_SAME_SESSION = 2
    USER_CRITERIA_ACROSS_ALL_SESSIONS = 3


class UserExclusionDuration(proto.Enum):
    r"""Enumerates options for how long an exclusion will last if a user
    matches the ``userExclusionCriteria``.

    Values:
        USER_EXCLUSION_DURATION_UNSPECIFIED (0):
            Unspecified exclusion duration. Do not
            specify.
        USER_EXCLUSION_TEMPORARY (1):
            Temporarily exclude users from the segment during periods
            when the user meets the ``userExclusionCriteria`` condition.
        USER_EXCLUSION_PERMANENT (2):
            Permanently exclude users from the segment if the user ever
            meets the ``userExclusionCriteria`` condition.
    """

    USER_EXCLUSION_DURATION_UNSPECIFIED = 0
    USER_EXCLUSION_TEMPORARY = 1
    USER_EXCLUSION_PERMANENT = 2


class SessionCriteriaScoping(proto.Enum):
    r"""Scoping specifies which events are considered when evaluating
    if a session meets a criteria.

    Values:
        SESSION_CRITERIA_SCOPING_UNSPECIFIED (0):
            Unspecified criteria scoping. Do not specify.
        SESSION_CRITERIA_WITHIN_SAME_EVENT (1):
            If the criteria is satisfied within one
            event, the session matches the criteria.
        SESSION_CRITERIA_WITHIN_SAME_SESSION (2):
            If the criteria is satisfied within one
            session, the session matches the criteria.
    """

    SESSION_CRITERIA_SCOPING_UNSPECIFIED = 0
    SESSION_CRITERIA_WITHIN_SAME_EVENT = 1
    SESSION_CRITERIA_WITHIN_SAME_SESSION = 2


class SessionExclusionDuration(proto.Enum):
    r"""Enumerates options for how long an exclusion will last if a session
    matches the ``sessionExclusionCriteria``.

    Values:
        SESSION_EXCLUSION_DURATION_UNSPECIFIED (0):
            Unspecified exclusion duration. Do not
            specify.
        SESSION_EXCLUSION_TEMPORARY (1):
            Temporarily exclude sessions from the segment during periods
            when the session meets the ``sessionExclusionCriteria``
            condition.
        SESSION_EXCLUSION_PERMANENT (2):
            Permanently exclude sessions from the segment if the session
            ever meets the ``sessionExclusionCriteria`` condition.
    """

    SESSION_EXCLUSION_DURATION_UNSPECIFIED = 0
    SESSION_EXCLUSION_TEMPORARY = 1
    SESSION_EXCLUSION_PERMANENT = 2


class EventCriteriaScoping(proto.Enum):
    r"""Scoping specifies which events are considered when evaluating
    if an event meets a criteria.

    Values:
        EVENT_CRITERIA_SCOPING_UNSPECIFIED (0):
            Unspecified criteria scoping. Do not specify.
        EVENT_CRITERIA_WITHIN_SAME_EVENT (1):
            If the criteria is satisfied within one
            event, the event matches the criteria.
    """

    EVENT_CRITERIA_SCOPING_UNSPECIFIED = 0
    EVENT_CRITERIA_WITHIN_SAME_EVENT = 1


class EventExclusionDuration(proto.Enum):
    r"""Enumerates options for how long an exclusion will last if an event
    matches the ``eventExclusionCriteria``.

    Values:
        EVENT_EXCLUSION_DURATION_UNSPECIFIED (0):
            Unspecified exclusion duration. Do not
            specify.
        EVENT_EXCLUSION_PERMANENT (1):
            Permanently exclude events from the segment if the event
            ever meets the ``eventExclusionCriteria`` condition.
    """

    EVENT_EXCLUSION_DURATION_UNSPECIFIED = 0
    EVENT_EXCLUSION_PERMANENT = 1


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


class SamplingLevel(proto.Enum):
    r"""Categories of sampling levels for the requests.

    Values:
        SAMPLING_LEVEL_UNSPECIFIED (0):
            Unspecified type.
        LOW (1):
            Applies a sampling level of 10 million to
            standard properties and 100 million to Google
            Analytics 360 properties.
        MEDIUM (2):
            Exclusive to Google Analytics 360 properties
            with a sampling level of 1 billion.
        UNSAMPLED (3):
            Exclusive to Google Analytics 360 properties.
            Unsampled explorations are more accurate and can
            reveal insights that aren't visible in standard
            explorations. To learn more, see
            https://support.google.com/analytics/answer/10896953.
    """

    SAMPLING_LEVEL_UNSPECIFIED = 0
    LOW = 1
    MEDIUM = 2
    UNSAMPLED = 3


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


class Dimension(proto.Message):
    r"""Dimensions are attributes of your data. For example, the
    dimension city indicates the city from which an event
    originates. Dimension values in report responses are strings;
    for example, the city could be "Paris" or "New York".

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
        dimension_expression (google.analytics.data_v1alpha.types.DimensionExpression):
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
        lower_case (google.analytics.data_v1alpha.types.DimensionExpression.CaseExpression):
            Used to convert a dimension value to lower
            case.

            This field is a member of `oneof`_ ``one_expression``.
        upper_case (google.analytics.data_v1alpha.types.DimensionExpression.CaseExpression):
            Used to convert a dimension value to upper
            case.

            This field is a member of `oneof`_ ``one_expression``.
        concatenate (google.analytics.data_v1alpha.types.DimensionExpression.ConcatenateExpression):
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
        dimension_filter (google.analytics.data_v1alpha.types.FilterExpression):
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
        and_group (google.analytics.data_v1alpha.types.FilterExpressionList):
            The FilterExpressions in and_group have an AND relationship.

            This field is a member of `oneof`_ ``expr``.
        or_group (google.analytics.data_v1alpha.types.FilterExpressionList):
            The FilterExpressions in or_group have an OR relationship.

            This field is a member of `oneof`_ ``expr``.
        not_expression (google.analytics.data_v1alpha.types.FilterExpression):
            The FilterExpression is NOT of not_expression.

            This field is a member of `oneof`_ ``expr``.
        filter (google.analytics.data_v1alpha.types.Filter):
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
        expressions (MutableSequence[google.analytics.data_v1alpha.types.FilterExpression]):
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
            The dimension name or metric name. Must be a
            name defined in dimensions or metrics.
        string_filter (google.analytics.data_v1alpha.types.StringFilter):
            Strings related filter.

            This field is a member of `oneof`_ ``one_filter``.
        in_list_filter (google.analytics.data_v1alpha.types.InListFilter):
            A filter for in list values.

            This field is a member of `oneof`_ ``one_filter``.
        numeric_filter (google.analytics.data_v1alpha.types.NumericFilter):
            A filter for numeric or date values.

            This field is a member of `oneof`_ ``one_filter``.
        between_filter (google.analytics.data_v1alpha.types.BetweenFilter):
            A filter for between two values.

            This field is a member of `oneof`_ ``one_filter``.
        empty_filter (google.analytics.data_v1alpha.types.EmptyFilter):
            A filter for empty values such as "(not set)"
            and "" values.

            This field is a member of `oneof`_ ``one_filter``.
    """

    field_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    string_filter: "StringFilter" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="one_filter",
        message="StringFilter",
    )
    in_list_filter: "InListFilter" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="one_filter",
        message="InListFilter",
    )
    numeric_filter: "NumericFilter" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="one_filter",
        message="NumericFilter",
    )
    between_filter: "BetweenFilter" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="one_filter",
        message="BetweenFilter",
    )
    empty_filter: "EmptyFilter" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="one_filter",
        message="EmptyFilter",
    )


class StringFilter(proto.Message):
    r"""The filter for string

    Attributes:
        match_type (google.analytics.data_v1alpha.types.StringFilter.MatchType):
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
        operation (google.analytics.data_v1alpha.types.NumericFilter.Operation):
            The operation type for this filter.
        value (google.analytics.data_v1alpha.types.NumericValue):
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
        metric (google.analytics.data_v1alpha.types.OrderBy.MetricOrderBy):
            Sorts results by a metric's values.

            This field is a member of `oneof`_ ``one_order_by``.
        dimension (google.analytics.data_v1alpha.types.OrderBy.DimensionOrderBy):
            Sorts results by a dimension's values.

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
            order_type (google.analytics.data_v1alpha.types.OrderBy.DimensionOrderBy.OrderType):
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
        number=4,
    )


class BetweenFilter(proto.Message):
    r"""To express that the result needs to be between two numbers
    (inclusive).

    Attributes:
        from_value (google.analytics.data_v1alpha.types.NumericValue):
            Begins with this number.
        to_value (google.analytics.data_v1alpha.types.NumericValue):
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
        cohorts (MutableSequence[google.analytics.data_v1alpha.types.Cohort]):
            Defines the selection criteria to group users
            into cohorts.
            Most cohort reports define only a single cohort.
            If multiple cohorts are specified, each cohort
            can be recognized in the report by their name.
        cohorts_range (google.analytics.data_v1alpha.types.CohortsRange):
            Cohort reports follow cohorts over an
            extended reporting date range. This range
            specifies an offset duration to follow the
            cohorts over.
        cohort_report_settings (google.analytics.data_v1alpha.types.CohortReportSettings):
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
        date_range (google.analytics.data_v1alpha.types.DateRange):
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
        granularity (google.analytics.data_v1alpha.types.CohortsRange.Granularity):
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
        schema_restriction_response (google.analytics.data_v1alpha.types.ResponseMetaData.SchemaRestrictionResponse):
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
            thresholds <https://support.google.com/analytics/answer/9383630>`__
            and `About Demographics and
            Interests <https://support.google.com/analytics/answer/2799357>`__.

            This field is a member of `oneof`_ ``_subject_to_thresholding``.
        sampling_metadatas (MutableSequence[google.analytics.data_v1alpha.types.SamplingMetadata]):
            If this report results is
            `sampled <https://support.google.com/analytics/answer/13331292>`__,
            this describes the percentage of events used in this report.
            One ``samplingMetadatas`` is populated for each date range.
            Each ``samplingMetadatas`` corresponds to a date range in
            order that date ranges were specified in the request.

            However if the results are not sampled, this field will not
            be defined.
        section (google.analytics.data_v1alpha.types.Section):
            Identifies the type of data in the report.
        data_truncation_reasons (MutableSequence[google.analytics.data_v1alpha.types.ResponseMetaData.DataTruncationReason]):
            If set, indicate there is data truncation in
            the report.
    """

    class SchemaRestrictionResponse(proto.Message):
        r"""The schema restrictions actively enforced in creating this report.
        To learn more, see `Access and data-restriction
        management <https://support.google.com/analytics/answer/10851388>`__.

        Attributes:
            active_metric_restrictions (MutableSequence[google.analytics.data_v1alpha.types.ResponseMetaData.SchemaRestrictionResponse.ActiveMetricRestriction]):
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
                restricted_metric_types (MutableSequence[google.analytics.data_v1alpha.types.RestrictedMetricType]):
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
            data_truncation_type (google.analytics.data_v1alpha.types.ResponseMetaData.DataTruncationReason.DataTruncationType):
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
            data_truncation_date_ranges (MutableSequence[google.analytics.data_v1alpha.types.ResponseMetaData.DataTruncationReason.DataTruncationDateRange]):
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
    section: "Section" = proto.Field(
        proto.ENUM,
        number=10,
        enum="Section",
    )
    data_truncation_reasons: MutableSequence[DataTruncationReason] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=11,
            message=DataTruncationReason,
        )
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
        type_ (google.analytics.data_v1alpha.types.MetricType):
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
        dimension_values (MutableSequence[google.analytics.data_v1alpha.types.DimensionValue]):
            List of requested dimension values. In a PivotReport,
            dimension_values are only listed for dimensions included in
            a pivot.
        metric_values (MutableSequence[google.analytics.data_v1alpha.types.MetricValue]):
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


class PropertyQuota(proto.Message):
    r"""Current state of all quotas for this Analytics Property. If
    any quota for a property is exhausted, all requests to that
    property will return Resource Exhausted errors.

    Attributes:
        tokens_per_day (google.analytics.data_v1alpha.types.QuotaStatus):
            Standard Analytics Properties can use up to
            200,000 tokens per day; Analytics 360 Properties
            can use 2,000,000 tokens per day. Most requests
            consume fewer than 10 tokens.
        tokens_per_hour (google.analytics.data_v1alpha.types.QuotaStatus):
            Standard Analytics Properties can use up to
            40,000 tokens per hour; Analytics 360 Properties
            can use 400,000 tokens per hour. An API request
            consumes a single number of tokens, and that
            number is deducted from all of the hourly,
            daily, and per project hourly quotas.
        concurrent_requests (google.analytics.data_v1alpha.types.QuotaStatus):
            Standard Analytics Properties can send up to
            10 concurrent requests; Analytics 360 Properties
            can use up to 50 concurrent requests.
        server_errors_per_project_per_hour (google.analytics.data_v1alpha.types.QuotaStatus):
            Standard Analytics Properties and cloud
            project pairs can have up to 10 server errors
            per hour; Analytics 360 Properties and cloud
            project pairs can have up to 50 server errors
            per hour.
        potentially_thresholded_requests_per_hour (google.analytics.data_v1alpha.types.QuotaStatus):
            Analytics Properties can send up to 120
            requests with potentially thresholded dimensions
            per hour. In a batch request, each report
            request is individually counted for this quota
            if the request contains potentially thresholded
            dimensions.
        tokens_per_project_per_hour (google.analytics.data_v1alpha.types.QuotaStatus):
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


class FunnelBreakdown(proto.Message):
    r"""Breakdowns add a dimension to the funnel table sub report
    response.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        breakdown_dimension (google.analytics.data_v1alpha.types.Dimension):
            The dimension column added to the funnel table sub report
            response. The breakdown dimension breaks down each funnel
            step. A valid ``breakdownDimension`` is required if
            ``funnelBreakdown`` is specified.
        limit (int):
            The maximum number of distinct values of the breakdown
            dimension to return in the response. A ``limit`` of ``5`` is
            used if limit is not specified. Limit must exceed zero and
            cannot exceed 15.

            This field is a member of `oneof`_ ``_limit``.
    """

    breakdown_dimension: "Dimension" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Dimension",
    )
    limit: int = proto.Field(
        proto.INT64,
        number=2,
        optional=True,
    )


class FunnelNextAction(proto.Message):
    r"""Next actions state the value for a dimension after the user has
    achieved a step but before the same user has achieved the next step.
    For example if the ``nextActionDimension`` is ``eventName``, then
    ``nextActionDimension`` in the ``i``\ th funnel step row will return
    first event after the event that qualified the user into the
    ``i``\ th funnel step but before the user achieved the ``i+1``\ th
    funnel step.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        next_action_dimension (google.analytics.data_v1alpha.types.Dimension):
            The dimension column added to the funnel visualization sub
            report response. The next action dimension returns the next
            dimension value of this dimension after the user has
            attained the ``i``\ th funnel step.

            ``nextActionDimension`` currently only supports
            ``eventName`` and most Page / Screen dimensions like
            ``pageTitle`` and ``pagePath``. ``nextActionDimension``
            cannot be a dimension expression.
        limit (int):
            The maximum number of distinct values of the breakdown
            dimension to return in the response. A ``limit`` of ``5`` is
            used if limit is not specified. Limit must exceed zero and
            cannot exceed 5.

            This field is a member of `oneof`_ ``_limit``.
    """

    next_action_dimension: "Dimension" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Dimension",
    )
    limit: int = proto.Field(
        proto.INT64,
        number=2,
        optional=True,
    )


class Funnel(proto.Message):
    r"""Configures the funnel in a funnel report request. A funnel
    reports on users as they pass through a sequence of steps.

    Funnel exploration lets you visualize the steps your users take
    to complete a task and quickly see how well they are succeeding
    or failing at each step. For example, how do prospects become
    shoppers and then become buyers? How do one time buyers become
    repeat buyers? With this information, you can improve
    inefficient or abandoned customer journeys.

    Attributes:
        is_open_funnel (bool):
            In an open funnel, users can enter the funnel
            in any step, and in a closed funnel, users must
            enter the funnel in the first step. Optional. If
            unspecified, a closed funnel is used.
        steps (MutableSequence[google.analytics.data_v1alpha.types.FunnelStep]):
            The sequential steps of this funnel.
    """

    is_open_funnel: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    steps: MutableSequence["FunnelStep"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="FunnelStep",
    )


class FunnelStep(proto.Message):
    r"""Steps define the user journey you want to measure. Steps
    contain one or more conditions that your users must meet to be
    included in that step of the funnel journey.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            The distinctive name for this step. If unspecified, steps
            will be named by a 1 based indexed name (for example "0. ",
            "1. ", etc.). This name defines string value returned by the
            ``funnelStepName`` dimension. For example, specifying
            ``name = Purchase`` in the request's third funnel step will
            produce ``3. Purchase`` in the funnel report response.
        is_directly_followed_by (bool):
            If true, this step must directly follow the previous step.
            If false, there can be events between the previous step and
            this step. If unspecified, ``isDirectlyFollowedBy`` is
            treated as false.
        within_duration_from_prior_step (google.protobuf.duration_pb2.Duration):
            If specified, this step must complete within this duration
            of the completion of the prior step.
            ``withinDurationFromPriorStep`` is inclusive of the endpoint
            at the microsecond granularity. For example a duration of 5
            seconds can be completed at 4.9 or 5.0 seconds, but not 5
            seconds and 1 microsecond.

            ``withinDurationFromPriorStep`` is optional, and if
            unspecified, steps may be separated by any time duration.

            This field is a member of `oneof`_ ``_within_duration_from_prior_step``.
        filter_expression (google.analytics.data_v1alpha.types.FunnelFilterExpression):
            The condition that your users must meet to be
            included in this step of the funnel journey.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    is_directly_followed_by: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    within_duration_from_prior_step: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=3,
        optional=True,
        message=duration_pb2.Duration,
    )
    filter_expression: "FunnelFilterExpression" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="FunnelFilterExpression",
    )


class FunnelSubReport(proto.Message):
    r"""Funnel sub reports contain the dimension and metric data
    values. For example, 12 users reached the second step of the
    funnel.

    Attributes:
        dimension_headers (MutableSequence[google.analytics.data_v1alpha.types.DimensionHeader]):
            Describes dimension columns. Funnel reports
            always include the funnel step dimension in sub
            report responses. Additional dimensions like
            breakdowns, dates, and next actions may be
            present in the response if requested.
        metric_headers (MutableSequence[google.analytics.data_v1alpha.types.MetricHeader]):
            Describes metric columns. Funnel reports
            always include active users in sub report
            responses. The funnel table includes additional
            metrics like completion rate, abandonments, and
            abandonments rate.
        rows (MutableSequence[google.analytics.data_v1alpha.types.Row]):
            Rows of dimension value combinations and
            metric values in the report.
        metadata (google.analytics.data_v1alpha.types.FunnelResponseMetadata):
            Metadata for the funnel report.
    """

    dimension_headers: MutableSequence["DimensionHeader"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="DimensionHeader",
    )
    metric_headers: MutableSequence["MetricHeader"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="MetricHeader",
    )
    rows: MutableSequence["Row"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="Row",
    )
    metadata: "FunnelResponseMetadata" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="FunnelResponseMetadata",
    )


class ResponseBlock(proto.Message):
    r"""One block of structured data in chat response.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        text (str):
            A block of text.

            This field is a member of `oneof`_ ``block``.
        table (google.analytics.data_v1alpha.types.ResponseBlock.DataTable):
            A block of table data.

            This field is a member of `oneof`_ ``block``.
    """

    class DataTableCell(proto.Message):
        r"""A cell in a data table.

        Attributes:
            value (str):
                The value of the cell.
        """

        value: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class DataTableHeader(proto.Message):
        r"""Describes a column header in a DataTable.

        Attributes:
            header (str):
                The header name.
            data_type (str):
                The data type.
        """

        header: str = proto.Field(
            proto.STRING,
            number=1,
        )
        data_type: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class DataTableRow(proto.Message):
        r"""A row in a DataTable.

        Attributes:
            columns (MutableSequence[google.analytics.data_v1alpha.types.ResponseBlock.DataTableCell]):
                The cell values in the row.
        """

        columns: MutableSequence["ResponseBlock.DataTableCell"] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="ResponseBlock.DataTableCell",
        )

    class DataTable(proto.Message):
        r"""A table of data.

        Attributes:
            headers (MutableSequence[google.analytics.data_v1alpha.types.ResponseBlock.DataTableHeader]):
                Describes dimension columns. The number of
                headers and ordering of headers matches the
                dimensions present in rows.
            rows (MutableSequence[google.analytics.data_v1alpha.types.ResponseBlock.DataTableRow]):
                Rows of dimension value combinations and
                metric values in the report.
        """

        headers: MutableSequence["ResponseBlock.DataTableHeader"] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="ResponseBlock.DataTableHeader",
        )
        rows: MutableSequence["ResponseBlock.DataTableRow"] = proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="ResponseBlock.DataTableRow",
        )

    text: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="block",
    )
    table: DataTable = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="block",
        message=DataTable,
    )


class UserSegment(proto.Message):
    r"""User segments are subsets of users who engaged with your site
    or app. For example, users who have previously purchased; users
    who added items to their shopping carts, but didn’t complete a
    purchase.

    Attributes:
        user_inclusion_criteria (google.analytics.data_v1alpha.types.UserSegmentCriteria):
            Defines which users are included in this
            segment. Optional.
        exclusion (google.analytics.data_v1alpha.types.UserSegmentExclusion):
            Defines which users are excluded in this
            segment. Optional.
    """

    user_inclusion_criteria: "UserSegmentCriteria" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="UserSegmentCriteria",
    )
    exclusion: "UserSegmentExclusion" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="UserSegmentExclusion",
    )


class UserSegmentCriteria(proto.Message):
    r"""A user matches a criteria if the user's events meet the
    conditions in the criteria.

    Attributes:
        and_condition_groups (MutableSequence[google.analytics.data_v1alpha.types.UserSegmentConditionGroup]):
            A user matches this criteria if the user matches each of
            these ``andConditionGroups`` and each of the
            ``andSequenceGroups``. ``andConditionGroups`` may be empty
            if ``andSequenceGroups`` are specified.
        and_sequence_groups (MutableSequence[google.analytics.data_v1alpha.types.UserSegmentSequenceGroup]):
            A user matches this criteria if the user matches each of
            these ``andSequenceGroups`` and each of the
            ``andConditionGroups``. ``andSequenceGroups`` may be empty
            if ``andConditionGroups`` are specified.
    """

    and_condition_groups: MutableSequence["UserSegmentConditionGroup"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="UserSegmentConditionGroup",
        )
    )
    and_sequence_groups: MutableSequence["UserSegmentSequenceGroup"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="UserSegmentSequenceGroup",
        )
    )


class UserSegmentConditionGroup(proto.Message):
    r"""Conditions tell Analytics what data to include in or exclude
    from the segment.

    Attributes:
        condition_scoping (google.analytics.data_v1alpha.types.UserCriteriaScoping):
            Data is included or excluded from the segment based on if it
            matches the condition group. This scoping defines how many
            events the ``segmentFilterExpression`` is evaluated on
            before the condition group is determined to be matched or
            not. For example if
            ``conditionScoping = USER_CRITERIA_WITHIN_SAME_SESSION``,
            the expression is evaluated on all events in a session, and
            then, the condition group is determined to be matched or not
            for this user. For example if
            ``conditionScoping = USER_CRITERIA_WITHIN_SAME_EVENT``, the
            expression is evaluated on a single event, and then, the
            condition group is determined to be matched or not for this
            user.

            Optional. If unspecified,
            ``conditionScoping = ACROSS_ALL_SESSIONS`` is used.
        segment_filter_expression (google.analytics.data_v1alpha.types.SegmentFilterExpression):
            Data is included or excluded from the segment
            based on if it matches this expression.
            Expressions express criteria on dimension,
            metrics, and/or parameters.
    """

    condition_scoping: "UserCriteriaScoping" = proto.Field(
        proto.ENUM,
        number=1,
        enum="UserCriteriaScoping",
    )
    segment_filter_expression: "SegmentFilterExpression" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="SegmentFilterExpression",
    )


class UserSegmentSequenceGroup(proto.Message):
    r"""Define conditions that must occur in a specific order for the
    user to be a member of the segment.

    Attributes:
        sequence_scoping (google.analytics.data_v1alpha.types.UserCriteriaScoping):
            All sequence steps must be satisfied in the scoping for the
            user to match the sequence. For example if
            ``sequenceScoping = USER_CRITERIA_WITHIN_SAME_SESSION``, all
            sequence steps must complete within one session for the user
            to match the sequence.
            ``sequenceScoping = USER_CRITERIA_WITHIN_SAME_EVENT`` is not
            supported.

            Optional. If unspecified,
            ``conditionScoping = ACROSS_ALL_SESSIONS`` is used.
        sequence_maximum_duration (google.protobuf.duration_pb2.Duration):
            Defines the time period in which the whole sequence must
            occur; for example, 30 Minutes. ``sequenceMaximumDuration``
            is inclusive of the endpoint at the microsecond granularity.
            For example a sequence with a maximum duration of 5 seconds
            can be completed at 4.9 or 5.0 seconds, but not 5 seconds
            and 1 microsecond.

            ``sequenceMaximumDuration`` is optional, and if unspecified,
            sequences can be completed in any time duration.
        user_sequence_steps (MutableSequence[google.analytics.data_v1alpha.types.UserSequenceStep]):
            An ordered sequence of condition steps. A user's events must
            complete each step in order for the user to match the
            ``UserSegmentSequenceGroup``.
    """

    sequence_scoping: "UserCriteriaScoping" = proto.Field(
        proto.ENUM,
        number=1,
        enum="UserCriteriaScoping",
    )
    sequence_maximum_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=2,
        message=duration_pb2.Duration,
    )
    user_sequence_steps: MutableSequence["UserSequenceStep"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="UserSequenceStep",
    )


class UserSequenceStep(proto.Message):
    r"""A condition that must occur in the specified step order for
    this user to match the sequence.

    Attributes:
        is_directly_followed_by (bool):
            If true, the event satisfying this step must be the very
            next event after the event satifying the last step. If
            false, this step indirectly follows the prior step; for
            example, there may be events between the prior step and this
            step. ``isDirectlyFollowedBy`` must be false for the first
            step.
        step_scoping (google.analytics.data_v1alpha.types.UserCriteriaScoping):
            This sequence step must be satisfied in the scoping for the
            user to match the sequence. For example if
            ``sequenceScoping = WITHIN_SAME_SESSION``, this sequence
            steps must complete within one session for the user to match
            the sequence. ``stepScoping = ACROSS_ALL_SESSIONS`` is only
            allowed if the ``sequenceScoping = ACROSS_ALL_SESSIONS``.

            Optional. If unspecified, ``stepScoping`` uses the same
            ``UserCriteriaScoping`` as the ``sequenceScoping``.
        segment_filter_expression (google.analytics.data_v1alpha.types.SegmentFilterExpression):
            A user matches this sequence step if their
            events match this expression. Expressions
            express criteria on dimension, metrics, and/or
            parameters.
    """

    is_directly_followed_by: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    step_scoping: "UserCriteriaScoping" = proto.Field(
        proto.ENUM,
        number=2,
        enum="UserCriteriaScoping",
    )
    segment_filter_expression: "SegmentFilterExpression" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="SegmentFilterExpression",
    )


class UserSegmentExclusion(proto.Message):
    r"""Specifies which users are excluded in this segment.

    Attributes:
        user_exclusion_duration (google.analytics.data_v1alpha.types.UserExclusionDuration):
            Specifies how long an exclusion will last if a user matches
            the ``userExclusionCriteria``.

            Optional. If unspecified, ``userExclusionDuration`` of
            ``USER_EXCLUSION_TEMPORARY`` is used.
        user_exclusion_criteria (google.analytics.data_v1alpha.types.UserSegmentCriteria):
            If a user meets this condition, the user is excluded from
            membership in the segment for the ``userExclusionDuration``.
    """

    user_exclusion_duration: "UserExclusionDuration" = proto.Field(
        proto.ENUM,
        number=1,
        enum="UserExclusionDuration",
    )
    user_exclusion_criteria: "UserSegmentCriteria" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="UserSegmentCriteria",
    )


class SessionSegment(proto.Message):
    r"""Session segments are subsets of the sessions that occurred on
    your site or app: for example, all the sessions that originated
    from a particular advertising campaign.

    Attributes:
        session_inclusion_criteria (google.analytics.data_v1alpha.types.SessionSegmentCriteria):
            Defines which sessions are included in this
            segment. Optional.
        exclusion (google.analytics.data_v1alpha.types.SessionSegmentExclusion):
            Defines which sessions are excluded in this
            segment. Optional.
    """

    session_inclusion_criteria: "SessionSegmentCriteria" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="SessionSegmentCriteria",
    )
    exclusion: "SessionSegmentExclusion" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="SessionSegmentExclusion",
    )


class SessionSegmentCriteria(proto.Message):
    r"""A session matches a criteria if the session's events meet the
    conditions in the criteria.

    Attributes:
        and_condition_groups (MutableSequence[google.analytics.data_v1alpha.types.SessionSegmentConditionGroup]):
            A session matches this criteria if the session matches each
            of these ``andConditionGroups``.
    """

    and_condition_groups: MutableSequence["SessionSegmentConditionGroup"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="SessionSegmentConditionGroup",
        )
    )


class SessionSegmentConditionGroup(proto.Message):
    r"""Conditions tell Analytics what data to include in or exclude
    from the segment.

    Attributes:
        condition_scoping (google.analytics.data_v1alpha.types.SessionCriteriaScoping):
            Data is included or excluded from the segment based on if it
            matches the condition group. This scoping defines how many
            events the ``segmentFilterExpression`` is evaluated on
            before the condition group is determined to be matched or
            not. For example if
            ``conditionScoping = SESSION_CRITERIA_WITHIN_SAME_SESSION``,
            the expression is evaluated on all events in a session, and
            then, the condition group is determined to be matched or not
            for this session. For example if
            ``conditionScoping = SESSION_CRITERIA_WITHIN_SAME_EVENT``,
            the expression is evaluated on a single event, and then, the
            condition group is determined to be matched or not for this
            session.

            Optional. If unspecified, a ``conditionScoping`` of
            ``WITHIN_SAME_SESSION`` is used.
        segment_filter_expression (google.analytics.data_v1alpha.types.SegmentFilterExpression):
            Data is included or excluded from the segment
            based on if it matches this expression.
            Expressions express criteria on dimension,
            metrics, and/or parameters.
    """

    condition_scoping: "SessionCriteriaScoping" = proto.Field(
        proto.ENUM,
        number=1,
        enum="SessionCriteriaScoping",
    )
    segment_filter_expression: "SegmentFilterExpression" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="SegmentFilterExpression",
    )


class SessionSegmentExclusion(proto.Message):
    r"""Specifies which sessions are excluded in this segment.

    Attributes:
        session_exclusion_duration (google.analytics.data_v1alpha.types.SessionExclusionDuration):
            Specifies how long an exclusion will last if a session
            matches the ``sessionExclusionCriteria``.

            Optional. If unspecified, a ``sessionExclusionDuration`` of
            ``SESSION_EXCLUSION_TEMPORARY`` is used.
        session_exclusion_criteria (google.analytics.data_v1alpha.types.SessionSegmentCriteria):
            If a session meets this condition, the session is excluded
            from membership in the segment for the
            ``sessionExclusionDuration``.
    """

    session_exclusion_duration: "SessionExclusionDuration" = proto.Field(
        proto.ENUM,
        number=1,
        enum="SessionExclusionDuration",
    )
    session_exclusion_criteria: "SessionSegmentCriteria" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="SessionSegmentCriteria",
    )


class EventSegment(proto.Message):
    r"""Event segments are subsets of events that were triggered on your
    site or app. for example, all purchase events made in a particular
    location; app_exception events that occurred on a specific operating
    system.

    Attributes:
        event_inclusion_criteria (google.analytics.data_v1alpha.types.EventSegmentCriteria):
            Defines which events are included in this
            segment. Optional.
        exclusion (google.analytics.data_v1alpha.types.EventSegmentExclusion):
            Defines which events are excluded in this
            segment. Optional.
    """

    event_inclusion_criteria: "EventSegmentCriteria" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="EventSegmentCriteria",
    )
    exclusion: "EventSegmentExclusion" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="EventSegmentExclusion",
    )


class EventSegmentCriteria(proto.Message):
    r"""An event matches a criteria if the event meet the conditions
    in the criteria.

    Attributes:
        and_condition_groups (MutableSequence[google.analytics.data_v1alpha.types.EventSegmentConditionGroup]):
            An event matches this criteria if the event matches each of
            these ``andConditionGroups``.
    """

    and_condition_groups: MutableSequence["EventSegmentConditionGroup"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="EventSegmentConditionGroup",
        )
    )


class EventSegmentConditionGroup(proto.Message):
    r"""Conditions tell Analytics what data to include in or exclude
    from the segment.

    Attributes:
        condition_scoping (google.analytics.data_v1alpha.types.EventCriteriaScoping):
            ``conditionScoping`` should always be
            ``EVENT_CRITERIA_WITHIN_SAME_EVENT``.

            Optional. If unspecified, a ``conditionScoping`` of
            ``EVENT_CRITERIA_WITHIN_SAME_EVENT`` is used.
        segment_filter_expression (google.analytics.data_v1alpha.types.SegmentFilterExpression):
            Data is included or excluded from the segment
            based on if it matches this expression.
            Expressions express criteria on dimension,
            metrics, and/or parameters.
    """

    condition_scoping: "EventCriteriaScoping" = proto.Field(
        proto.ENUM,
        number=1,
        enum="EventCriteriaScoping",
    )
    segment_filter_expression: "SegmentFilterExpression" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="SegmentFilterExpression",
    )


class EventSegmentExclusion(proto.Message):
    r"""Specifies which events are excluded in this segment.

    Attributes:
        event_exclusion_duration (google.analytics.data_v1alpha.types.EventExclusionDuration):
            ``eventExclusionDuration`` should always be
            ``PERMANENTLY_EXCLUDE``.

            Optional. If unspecified, an ``eventExclusionDuration`` of
            ``EVENT_EXCLUSION_PERMANENT`` is used.
        event_exclusion_criteria (google.analytics.data_v1alpha.types.EventSegmentCriteria):
            If an event meets this condition, the event is excluded from
            membership in the segment for the
            ``eventExclusionDuration``.
    """

    event_exclusion_duration: "EventExclusionDuration" = proto.Field(
        proto.ENUM,
        number=1,
        enum="EventExclusionDuration",
    )
    event_exclusion_criteria: "EventSegmentCriteria" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="EventSegmentCriteria",
    )


class Segment(proto.Message):
    r"""A segment is a subset of your Analytics data. For example, of your
    entire set of users, one segment might be users from a particular
    country or city. Another segment might be users who purchase a
    particular line of products or who visit a specific part of your
    site or trigger certain events in your app.

    To learn more, see `Segment
    Builder <https://support.google.com/analytics/answer/9304353>`__.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            The name for this segment. If unspecified, segments are
            named "Segment". This name defines string value returned by
            the ``segment`` dimension. The ``segment`` dimension
            prefixes segment names by the 1-based index number of the
            segment in the request (for example "1. Segment", "2.
            Segment", etc.).
        user_segment (google.analytics.data_v1alpha.types.UserSegment):
            User segments are subsets of users who
            engaged with your site or app.

            This field is a member of `oneof`_ ``one_segment_scope``.
        session_segment (google.analytics.data_v1alpha.types.SessionSegment):
            Session segments are subsets of the sessions
            that occurred on your site or app.

            This field is a member of `oneof`_ ``one_segment_scope``.
        event_segment (google.analytics.data_v1alpha.types.EventSegment):
            Event segments are subsets of events that
            were triggered on your site or app.

            This field is a member of `oneof`_ ``one_segment_scope``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    user_segment: "UserSegment" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="one_segment_scope",
        message="UserSegment",
    )
    session_segment: "SessionSegment" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="one_segment_scope",
        message="SessionSegment",
    )
    event_segment: "EventSegment" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="one_segment_scope",
        message="EventSegment",
    )


class SegmentFilterExpression(proto.Message):
    r"""Expresses combinations of segment filters.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        and_group (google.analytics.data_v1alpha.types.SegmentFilterExpressionList):
            The SegmentFilterExpression in ``andGroup`` have an AND
            relationship.

            This field is a member of `oneof`_ ``expr``.
        or_group (google.analytics.data_v1alpha.types.SegmentFilterExpressionList):
            The SegmentFilterExpression in ``orGroup`` have an OR
            relationship.

            This field is a member of `oneof`_ ``expr``.
        not_expression (google.analytics.data_v1alpha.types.SegmentFilterExpression):
            The SegmentFilterExpression is NOT of ``notExpression``.

            This field is a member of `oneof`_ ``expr``.
        segment_filter (google.analytics.data_v1alpha.types.SegmentFilter):
            A primitive segment filter.

            This field is a member of `oneof`_ ``expr``.
        segment_event_filter (google.analytics.data_v1alpha.types.SegmentEventFilter):
            Creates a filter that matches events of a
            single event name. If a parameter filter
            expression is specified, only the subset of
            events that match both the single event name and
            the parameter filter expressions match this
            event filter.

            This field is a member of `oneof`_ ``expr``.
    """

    and_group: "SegmentFilterExpressionList" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="expr",
        message="SegmentFilterExpressionList",
    )
    or_group: "SegmentFilterExpressionList" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="expr",
        message="SegmentFilterExpressionList",
    )
    not_expression: "SegmentFilterExpression" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="expr",
        message="SegmentFilterExpression",
    )
    segment_filter: "SegmentFilter" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="expr",
        message="SegmentFilter",
    )
    segment_event_filter: "SegmentEventFilter" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="expr",
        message="SegmentEventFilter",
    )


class SegmentFilterExpressionList(proto.Message):
    r"""A list of segment filter expressions.

    Attributes:
        expressions (MutableSequence[google.analytics.data_v1alpha.types.SegmentFilterExpression]):
            The list of segment filter expressions
    """

    expressions: MutableSequence["SegmentFilterExpression"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="SegmentFilterExpression",
    )


class SegmentFilter(proto.Message):
    r"""An expression to filter dimension or metric values.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        field_name (str):
            The dimension name or metric name.
        string_filter (google.analytics.data_v1alpha.types.StringFilter):
            Strings related filter.

            This field is a member of `oneof`_ ``one_filter``.
        in_list_filter (google.analytics.data_v1alpha.types.InListFilter):
            A filter for in list values.

            This field is a member of `oneof`_ ``one_filter``.
        numeric_filter (google.analytics.data_v1alpha.types.NumericFilter):
            A filter for numeric or date values.

            This field is a member of `oneof`_ ``one_filter``.
        between_filter (google.analytics.data_v1alpha.types.BetweenFilter):
            A filter for between two values.

            This field is a member of `oneof`_ ``one_filter``.
        filter_scoping (google.analytics.data_v1alpha.types.SegmentFilterScoping):
            Specifies the scope for the filter.
    """

    field_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    string_filter: "StringFilter" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="one_filter",
        message="StringFilter",
    )
    in_list_filter: "InListFilter" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="one_filter",
        message="InListFilter",
    )
    numeric_filter: "NumericFilter" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="one_filter",
        message="NumericFilter",
    )
    between_filter: "BetweenFilter" = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="one_filter",
        message="BetweenFilter",
    )
    filter_scoping: "SegmentFilterScoping" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="SegmentFilterScoping",
    )


class SegmentFilterScoping(proto.Message):
    r"""Scopings specify how the dimensions & metrics of multiple
    events should be considered when evaluating a segment filter.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        at_any_point_in_time (bool):
            If ``atAnyPointInTime`` is true, this filter evaluates to
            true for all events if it evaluates to true for any event in
            the date range of the request.

            This ``atAnyPointInTime`` parameter does not extend the date
            range of events in the report. If ``atAnyPointInTime`` is
            true, only events within the report's date range are
            considered when evaluating this filter.

            This ``atAnyPointInTime`` is only able to be specified if
            the criteria scoping is ``ACROSS_ALL_SESSIONS`` and is not
            able to be specified in sequences.

            If the criteria scoping is ``ACROSS_ALL_SESSIONS``,
            ``atAnyPointInTime`` = false is used if unspecified.

            This field is a member of `oneof`_ ``_at_any_point_in_time``.
    """

    at_any_point_in_time: bool = proto.Field(
        proto.BOOL,
        number=1,
        optional=True,
    )


class SegmentEventFilter(proto.Message):
    r"""Creates a filter that matches events of a single event name.
    If a parameter filter expression is specified, only the subset
    of events that match both the single event name and the
    parameter filter expressions match this event filter.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        event_name (str):
            This filter matches events of this single
            event name. Event name is required.

            This field is a member of `oneof`_ ``_event_name``.
        segment_parameter_filter_expression (google.analytics.data_v1alpha.types.SegmentParameterFilterExpression):
            If specified, this filter matches events that
            match both the single event name and the
            parameter filter expressions.

            Inside the parameter filter expression, only
            parameter filters are available.

            This field is a member of `oneof`_ ``_segment_parameter_filter_expression``.
    """

    event_name: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    segment_parameter_filter_expression: "SegmentParameterFilterExpression" = (
        proto.Field(
            proto.MESSAGE,
            number=2,
            optional=True,
            message="SegmentParameterFilterExpression",
        )
    )


class SegmentParameterFilterExpression(proto.Message):
    r"""Expresses combinations of segment filter on parameters.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        and_group (google.analytics.data_v1alpha.types.SegmentParameterFilterExpressionList):
            The SegmentParameterFilterExpression in ``andGroup`` have an
            AND relationship.

            This field is a member of `oneof`_ ``expr``.
        or_group (google.analytics.data_v1alpha.types.SegmentParameterFilterExpressionList):
            The SegmentParameterFilterExpression in ``orGroup`` have an
            OR relationship.

            This field is a member of `oneof`_ ``expr``.
        not_expression (google.analytics.data_v1alpha.types.SegmentParameterFilterExpression):
            The SegmentParameterFilterExpression is NOT of
            ``notExpression``.

            This field is a member of `oneof`_ ``expr``.
        segment_parameter_filter (google.analytics.data_v1alpha.types.SegmentParameterFilter):
            A primitive segment parameter filter.

            This field is a member of `oneof`_ ``expr``.
    """

    and_group: "SegmentParameterFilterExpressionList" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="expr",
        message="SegmentParameterFilterExpressionList",
    )
    or_group: "SegmentParameterFilterExpressionList" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="expr",
        message="SegmentParameterFilterExpressionList",
    )
    not_expression: "SegmentParameterFilterExpression" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="expr",
        message="SegmentParameterFilterExpression",
    )
    segment_parameter_filter: "SegmentParameterFilter" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="expr",
        message="SegmentParameterFilter",
    )


class SegmentParameterFilterExpressionList(proto.Message):
    r"""A list of segment parameter filter expressions.

    Attributes:
        expressions (MutableSequence[google.analytics.data_v1alpha.types.SegmentParameterFilterExpression]):
            The list of segment parameter filter
            expressions.
    """

    expressions: MutableSequence["SegmentParameterFilterExpression"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="SegmentParameterFilterExpression",
        )
    )


class SegmentParameterFilter(proto.Message):
    r"""An expression to filter parameter values in a segment.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        event_parameter_name (str):
            This filter will be evaluated on the specified event
            parameter. Event parameters are logged as parameters of the
            event. Event parameters include fields like
            "firebase_screen" & "currency".

            Event parameters can only be used in segments & funnels and
            can only be used in a descendent filter from an EventFilter.
            In a descendent filter from an EventFilter either event or
            item parameters should be used.

            This field is a member of `oneof`_ ``one_parameter``.
        item_parameter_name (str):
            This filter will be evaluated on the specified item
            parameter. Item parameters are logged as parameters in the
            item array. Item parameters include fields like "item_name"
            & "item_category".

            Item parameters can only be used in segments & funnels and
            can only be used in a descendent filter from an EventFilter.
            In a descendent filter from an EventFilter either event or
            item parameters should be used.

            Item parameters are only available in ecommerce events. To
            learn more about ecommerce events, see the [Measure
            ecommerce]
            (https://developers.google.com/analytics/devguides/collection/ga4/ecommerce)
            guide.

            This field is a member of `oneof`_ ``one_parameter``.
        string_filter (google.analytics.data_v1alpha.types.StringFilter):
            Strings related filter.

            This field is a member of `oneof`_ ``one_filter``.
        in_list_filter (google.analytics.data_v1alpha.types.InListFilter):
            A filter for in list values.

            This field is a member of `oneof`_ ``one_filter``.
        numeric_filter (google.analytics.data_v1alpha.types.NumericFilter):
            A filter for numeric or date values.

            This field is a member of `oneof`_ ``one_filter``.
        between_filter (google.analytics.data_v1alpha.types.BetweenFilter):
            A filter for between two values.

            This field is a member of `oneof`_ ``one_filter``.
        filter_scoping (google.analytics.data_v1alpha.types.SegmentParameterFilterScoping):
            Specifies the scope for the filter.
    """

    event_parameter_name: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="one_parameter",
    )
    item_parameter_name: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="one_parameter",
    )
    string_filter: "StringFilter" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="one_filter",
        message="StringFilter",
    )
    in_list_filter: "InListFilter" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="one_filter",
        message="InListFilter",
    )
    numeric_filter: "NumericFilter" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="one_filter",
        message="NumericFilter",
    )
    between_filter: "BetweenFilter" = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="one_filter",
        message="BetweenFilter",
    )
    filter_scoping: "SegmentParameterFilterScoping" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="SegmentParameterFilterScoping",
    )


class SegmentParameterFilterScoping(proto.Message):
    r"""Scopings specify how multiple events should be considered
    when evaluating a segment parameter filter.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        in_any_n_day_period (int):
            Accumulates the parameter over the specified period of days
            before applying the filter. Only supported if criteria
            scoping is ``ACROSS_ALL_SESSIONS`` or
            ``WITHIN_SAME_SESSION``. Only supported if the parameter is
            ``event_count``.

            For example if ``inAnyNDayPeriod`` is 3, the event_name is
            "purchase", the event parameter is "event_count", and the
            Filter's criteria is greater than 5, this filter will
            accumulate the event count of purchase events over every 3
            consecutive day period in the report's date range; a user
            will pass this Filter's criteria to be included in this
            segment if their count of purchase events exceeds 5 in any 3
            consecutive day period. For example, the periods 2021-11-01
            to 2021-11-03, 2021-11-02 to 2021-11-04, 2021-11-03 to
            2021-11-05, and etc. will be considered.

            The date range is not extended for the purpose of having a
            full N day window near the start of the date range. For
            example if a report is for 2021-11-01 to 2021-11-10 and
            ``inAnyNDayPeriod`` = 3, the first two day period will be
            effectively shortened because no event data outside the
            report's date range will be read. For example, the first
            four periods will effectively be: 2021-11-01 to 2021-11-01,
            2021-11-01 to 2021-11-02, 2021-11-01 to 2021-11-03, and
            2021-11-02 to 2021-11-04.

            ``inAnyNDayPeriod`` is optional. If not specified, the
            ``segmentParameterFilter`` is applied to each event
            individually.

            This field is a member of `oneof`_ ``_in_any_n_day_period``.
    """

    in_any_n_day_period: int = proto.Field(
        proto.INT64,
        number=1,
        optional=True,
    )


class FunnelFilterExpression(proto.Message):
    r"""Expresses combinations of funnel filters.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        and_group (google.analytics.data_v1alpha.types.FunnelFilterExpressionList):
            The FunnelFilterExpression in ``andGroup`` have an AND
            relationship.

            This field is a member of `oneof`_ ``expr``.
        or_group (google.analytics.data_v1alpha.types.FunnelFilterExpressionList):
            The FunnelFilterExpression in ``orGroup`` have an OR
            relationship.

            This field is a member of `oneof`_ ``expr``.
        not_expression (google.analytics.data_v1alpha.types.FunnelFilterExpression):
            The FunnelFilterExpression is NOT of ``notExpression``.

            This field is a member of `oneof`_ ``expr``.
        funnel_field_filter (google.analytics.data_v1alpha.types.FunnelFieldFilter):
            A funnel filter for a dimension or metric.

            This field is a member of `oneof`_ ``expr``.
        funnel_event_filter (google.analytics.data_v1alpha.types.FunnelEventFilter):
            Creates a filter that matches events of a
            single event name. If a parameter filter
            expression is specified, only the subset of
            events that match both the single event name and
            the parameter filter expressions match this
            event filter.

            This field is a member of `oneof`_ ``expr``.
    """

    and_group: "FunnelFilterExpressionList" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="expr",
        message="FunnelFilterExpressionList",
    )
    or_group: "FunnelFilterExpressionList" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="expr",
        message="FunnelFilterExpressionList",
    )
    not_expression: "FunnelFilterExpression" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="expr",
        message="FunnelFilterExpression",
    )
    funnel_field_filter: "FunnelFieldFilter" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="expr",
        message="FunnelFieldFilter",
    )
    funnel_event_filter: "FunnelEventFilter" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="expr",
        message="FunnelEventFilter",
    )


class FunnelFilterExpressionList(proto.Message):
    r"""A list of funnel filter expressions.

    Attributes:
        expressions (MutableSequence[google.analytics.data_v1alpha.types.FunnelFilterExpression]):
            The list of funnel filter expressions.
    """

    expressions: MutableSequence["FunnelFilterExpression"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="FunnelFilterExpression",
    )


class FunnelFieldFilter(proto.Message):
    r"""An expression to filter dimension or metric values.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        field_name (str):
            The dimension name or metric name.
        string_filter (google.analytics.data_v1alpha.types.StringFilter):
            Strings related filter.

            This field is a member of `oneof`_ ``one_filter``.
        in_list_filter (google.analytics.data_v1alpha.types.InListFilter):
            A filter for in list values.

            This field is a member of `oneof`_ ``one_filter``.
        numeric_filter (google.analytics.data_v1alpha.types.NumericFilter):
            A filter for numeric or date values.

            This field is a member of `oneof`_ ``one_filter``.
        between_filter (google.analytics.data_v1alpha.types.BetweenFilter):
            A filter for between two values.

            This field is a member of `oneof`_ ``one_filter``.
    """

    field_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    string_filter: "StringFilter" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="one_filter",
        message="StringFilter",
    )
    in_list_filter: "InListFilter" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="one_filter",
        message="InListFilter",
    )
    numeric_filter: "NumericFilter" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="one_filter",
        message="NumericFilter",
    )
    between_filter: "BetweenFilter" = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="one_filter",
        message="BetweenFilter",
    )


class FunnelEventFilter(proto.Message):
    r"""Creates a filter that matches events of a single event name.
    If a parameter filter expression is specified, only the subset
    of events that match both the single event name and the
    parameter filter expressions match this event filter.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        event_name (str):
            This filter matches events of this single
            event name. Event name is required.

            This field is a member of `oneof`_ ``_event_name``.
        funnel_parameter_filter_expression (google.analytics.data_v1alpha.types.FunnelParameterFilterExpression):
            If specified, this filter matches events that
            match both the single event name and the
            parameter filter expressions.

            Inside the parameter filter expression, only
            parameter filters are available.

            This field is a member of `oneof`_ ``_funnel_parameter_filter_expression``.
    """

    event_name: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    funnel_parameter_filter_expression: "FunnelParameterFilterExpression" = proto.Field(
        proto.MESSAGE,
        number=2,
        optional=True,
        message="FunnelParameterFilterExpression",
    )


class FunnelParameterFilterExpression(proto.Message):
    r"""Expresses combinations of funnel filters on parameters.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        and_group (google.analytics.data_v1alpha.types.FunnelParameterFilterExpressionList):
            The FunnelParameterFilterExpression in ``andGroup`` have an
            AND relationship.

            This field is a member of `oneof`_ ``expr``.
        or_group (google.analytics.data_v1alpha.types.FunnelParameterFilterExpressionList):
            The FunnelParameterFilterExpression in ``orGroup`` have an
            OR relationship.

            This field is a member of `oneof`_ ``expr``.
        not_expression (google.analytics.data_v1alpha.types.FunnelParameterFilterExpression):
            The FunnelParameterFilterExpression is NOT of
            ``notExpression``.

            This field is a member of `oneof`_ ``expr``.
        funnel_parameter_filter (google.analytics.data_v1alpha.types.FunnelParameterFilter):
            A primitive funnel parameter filter.

            This field is a member of `oneof`_ ``expr``.
    """

    and_group: "FunnelParameterFilterExpressionList" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="expr",
        message="FunnelParameterFilterExpressionList",
    )
    or_group: "FunnelParameterFilterExpressionList" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="expr",
        message="FunnelParameterFilterExpressionList",
    )
    not_expression: "FunnelParameterFilterExpression" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="expr",
        message="FunnelParameterFilterExpression",
    )
    funnel_parameter_filter: "FunnelParameterFilter" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="expr",
        message="FunnelParameterFilter",
    )


class FunnelParameterFilterExpressionList(proto.Message):
    r"""A list of funnel parameter filter expressions.

    Attributes:
        expressions (MutableSequence[google.analytics.data_v1alpha.types.FunnelParameterFilterExpression]):
            The list of funnel parameter filter
            expressions.
    """

    expressions: MutableSequence["FunnelParameterFilterExpression"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="FunnelParameterFilterExpression",
        )
    )


class FunnelParameterFilter(proto.Message):
    r"""An expression to filter parameter values in a funnel.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        event_parameter_name (str):
            This filter will be evaluated on the specified event
            parameter. Event parameters are logged as parameters of the
            event. Event parameters include fields like
            "firebase_screen" & "currency".

            Event parameters can only be used in segments & funnels and
            can only be used in a descendent filter from an EventFilter.
            In a descendent filter from an EventFilter either event or
            item parameters should be used.

            This field is a member of `oneof`_ ``one_parameter``.
        item_parameter_name (str):
            This filter will be evaluated on the specified item
            parameter. Item parameters are logged as parameters in the
            item array. Item parameters include fields like "item_name"
            & "item_category".

            Item parameters can only be used in segments & funnels and
            can only be used in a descendent filter from an EventFilter.
            In a descendent filter from an EventFilter either event or
            item parameters should be used.

            Item parameters are only available in ecommerce events. To
            learn more about ecommerce events, see the [Measure
            ecommerce]
            (https://developers.google.com/analytics/devguides/collection/ga4/ecommerce)
            guide.

            This field is a member of `oneof`_ ``one_parameter``.
        string_filter (google.analytics.data_v1alpha.types.StringFilter):
            Strings related filter.

            This field is a member of `oneof`_ ``one_filter``.
        in_list_filter (google.analytics.data_v1alpha.types.InListFilter):
            A filter for in list values.

            This field is a member of `oneof`_ ``one_filter``.
        numeric_filter (google.analytics.data_v1alpha.types.NumericFilter):
            A filter for numeric or date values.

            This field is a member of `oneof`_ ``one_filter``.
        between_filter (google.analytics.data_v1alpha.types.BetweenFilter):
            A filter for between two values.

            This field is a member of `oneof`_ ``one_filter``.
    """

    event_parameter_name: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="one_parameter",
    )
    item_parameter_name: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="one_parameter",
    )
    string_filter: "StringFilter" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="one_filter",
        message="StringFilter",
    )
    in_list_filter: "InListFilter" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="one_filter",
        message="InListFilter",
    )
    numeric_filter: "NumericFilter" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="one_filter",
        message="NumericFilter",
    )
    between_filter: "BetweenFilter" = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="one_filter",
        message="BetweenFilter",
    )


class FunnelResponseMetadata(proto.Message):
    r"""The funnel report's response metadata carries additional
    information about the funnel report.

    Attributes:
        sampling_metadatas (MutableSequence[google.analytics.data_v1alpha.types.SamplingMetadata]):
            If funnel report results are
            `sampled <https://support.google.com/analytics/answer/13331292>`__,
            this describes what percentage of events were used in this
            funnel report. One ``samplingMetadatas`` is populated for
            each date range. Each ``samplingMetadatas`` corresponds to a
            date range in order that date ranges were specified in the
            request.

            However if the results are not sampled, this field will not
            be defined.
    """

    sampling_metadatas: MutableSequence["SamplingMetadata"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="SamplingMetadata",
    )


class SamplingMetadata(proto.Message):
    r"""If funnel report results are
    `sampled <https://support.google.com/analytics/answer/13331292>`__,
    this metadata describes what percentage of events were used in this
    funnel report for a date range. Sampling is the practice of
    analyzing a subset of all data in order to uncover the meaningful
    information in the larger data set.

    Attributes:
        samples_read_count (int):
            The total number of events read in this
            sampled report for a date range. This is the
            size of the subset this property's data that was
            analyzed in this funnel report.
        sampling_space_size (int):
            The total number of events present in this property's data
            that could have been analyzed in this funnel report for a
            date range. Sampling uncovers the meaningful information
            about the larger data set, and this is the size of the
            larger data set.

            To calculate the percentage of available data that was used
            in this funnel report, compute
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


class ConversionSpec(proto.Message):
    r"""Controls conversion reporting.

    <aside class="caution">
      This feature may not be available to your Google Analytics
    property. The   Google Analytics team is actively working to
    expand this feature to more   properties. Please reach out to
    your
      <a href="https://support.google.com/analytics/gethelp">support
    team</a> if   you have questions about the eligibility of your
    property. </aside>

    Attributes:
        conversion_actions (MutableSequence[str]):
            The conversion action IDs to include in the report. If
            empty, all conversions are included. Valid conversion action
            IDs can be retrieved from the ``conversion_action`` field
            within the ``conversions`` list in the response of the
            ``GetMetadata`` method. For example,
            'conversionActions/1234'.
        attribution_model (google.analytics.data_v1alpha.types.ConversionSpec.AttributionModel):
            The attribution model to use in the Conversion Report. If
            unspecified, ``DATA_DRIVEN`` is used.
    """

    class AttributionModel(proto.Enum):
        r"""Attribution model to use in the Conversion Report

        Values:
            ATTRIBUTION_MODEL_UNSPECIFIED (0):
                Unspecified attribution model.
            DATA_DRIVEN (1):
                Attribution was based on the paid and organic
                data driven model
            LAST_CLICK (2):
                Attribution was based on the paid and organic
                last click model
        """

        ATTRIBUTION_MODEL_UNSPECIFIED = 0
        DATA_DRIVEN = 1
        LAST_CLICK = 2

    conversion_actions: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    attribution_model: AttributionModel = proto.Field(
        proto.ENUM,
        number=2,
        enum=AttributionModel,
    )


class DimensionMetadata(proto.Message):
    r"""Explains a dimension.

    Attributes:
        api_name (str):
            This dimension's name. Usable in
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
        sections (MutableSequence[google.analytics.data_v1alpha.types.Section]):
            Specifies the Google Analytics sections this
            dimension applies to.
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
        number=6,
    )
    sections: MutableSequence["Section"] = proto.RepeatedField(
        proto.ENUM,
        number=7,
        enum="Section",
    )


class MetricMetadata(proto.Message):
    r"""Explains a metric.

    Attributes:
        api_name (str):
            A metric name. Usable in `Metric <#Metric>`__'s ``name``.
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
        type_ (google.analytics.data_v1alpha.types.MetricType):
            The type of this metric.
        expression (str):
            The mathematical expression for this derived metric. Can be
            used in `Metric <#Metric>`__'s ``expression`` field for
            equivalent reports. Most metrics are not expressions, and
            for non-expressions, this field is empty.
        custom_definition (bool):
            True if the metric is a custom metric for
            this property.
        blocked_reasons (MutableSequence[google.analytics.data_v1alpha.types.MetricMetadata.BlockedReason]):
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
        sections (MutableSequence[google.analytics.data_v1alpha.types.Section]):
            Specifies the Google Analytics sections this
            metric applies to.
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
        number=9,
    )
    sections: MutableSequence["Section"] = proto.RepeatedField(
        proto.ENUM,
        number=10,
        enum="Section",
    )


class ComparisonMetadata(proto.Message):
    r"""The metadata for a single comparison.

    Attributes:
        api_name (str):
            This comparison's resource name. Usable in
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


class ConversionMetadata(proto.Message):
    r"""The metadata for a single conversion.

    <aside class="caution">
      This feature may not be available to your Google Analytics
    property. The   Google Analytics team is actively working to
    expand this feature to more   properties. Please reach out to
    your
      <a href="https://support.google.com/analytics/gethelp">support
    team</a> if   you have questions about the eligibility of your
    property. </aside>

    Attributes:
        conversion_action (str):
            The unique identifier of the conversion action. This ID is
            used to specify which conversions to include in a report by
            populating the ``conversion_actions`` field in the
            ``ConversionsSpec`` of a report request. For example,
            'conversionActions/1234'.
        display_name (str):
            This conversion's name within the Google
            Analytics user interface.
    """

    conversion_action: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )


class PropertyChatQuota(proto.Message):
    r"""Property quota for chatbot specific fields.

    Attributes:
        tokens_per_day (google.analytics.data_v1alpha.types.QuotaStatus):
            Chat tokens consumed per day.
        tokens_per_hour (google.analytics.data_v1alpha.types.QuotaStatus):
            Chat tokens consumed per hour.
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


__all__ = tuple(sorted(__protobuf__.manifest))
