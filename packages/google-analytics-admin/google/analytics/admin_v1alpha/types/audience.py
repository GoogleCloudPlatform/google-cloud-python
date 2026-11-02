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
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.analytics.admin.v1alpha",
    manifest={
        "AudienceFilterScope",
        "AudienceDimensionOrMetricFilter",
        "AudienceEventFilter",
        "AudienceFilterExpression",
        "AudienceFilterExpressionList",
        "AudienceSimpleFilter",
        "AudienceSequenceFilter",
        "AudienceFilterClause",
        "AudienceEventTrigger",
        "Audience",
    },
)


class AudienceFilterScope(proto.Enum):
    r"""Specifies how to evaluate users for joining an Audience.

    Values:
        AUDIENCE_FILTER_SCOPE_UNSPECIFIED (0):
            Scope is not specified.
        AUDIENCE_FILTER_SCOPE_WITHIN_SAME_EVENT (1):
            User joins the Audience if the filter
            condition is met within one event.
        AUDIENCE_FILTER_SCOPE_WITHIN_SAME_SESSION (2):
            User joins the Audience if the filter
            condition is met within one session.
        AUDIENCE_FILTER_SCOPE_ACROSS_ALL_SESSIONS (3):
            User joins the Audience if the filter
            condition is met by any event across any
            session.
    """

    AUDIENCE_FILTER_SCOPE_UNSPECIFIED = 0
    AUDIENCE_FILTER_SCOPE_WITHIN_SAME_EVENT = 1
    AUDIENCE_FILTER_SCOPE_WITHIN_SAME_SESSION = 2
    AUDIENCE_FILTER_SCOPE_ACROSS_ALL_SESSIONS = 3


class AudienceDimensionOrMetricFilter(proto.Message):
    r"""A specific filter for a single dimension or metric.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        string_filter (google.analytics.admin_v1alpha.types.AudienceDimensionOrMetricFilter.StringFilter):
            A filter for a string-type dimension that
            matches a particular pattern.

            This field is a member of `oneof`_ ``one_filter``.
        in_list_filter (google.analytics.admin_v1alpha.types.AudienceDimensionOrMetricFilter.InListFilter):
            A filter for a string dimension that matches
            a particular list of options.

            This field is a member of `oneof`_ ``one_filter``.
        numeric_filter (google.analytics.admin_v1alpha.types.AudienceDimensionOrMetricFilter.NumericFilter):
            A filter for numeric or date values on a
            dimension or metric.

            This field is a member of `oneof`_ ``one_filter``.
        between_filter (google.analytics.admin_v1alpha.types.AudienceDimensionOrMetricFilter.BetweenFilter):
            A filter for numeric or date values between
            certain values on a dimension or metric.

            This field is a member of `oneof`_ ``one_filter``.
        field_name (str):
            Required. Immutable. The dimension name or metric name to
            filter. If the field name refers to a custom dimension or
            metric, a scope prefix will be added to the front of the
            custom dimensions or metric name. For more on scope prefixes
            or custom dimensions/metrics, reference the [Google
            Analytics Data API documentation]
            (https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema#custom_dimensions).
        at_any_point_in_time (bool):
            Optional. Indicates whether this filter needs dynamic
            evaluation or not. If set to true, users join the Audience
            if they ever met the condition (static evaluation). If unset
            or set to false, user evaluation for an Audience is dynamic;
            users are added to an Audience when they meet the conditions
            and then removed when they no longer meet them.

            This can only be set when Audience scope is
            ACROSS_ALL_SESSIONS.
        in_any_n_day_period (int):
            Optional. If set, specifies the time window for which to
            evaluate data in number of days. If not set, then audience
            data is evaluated against lifetime data (For example,
            infinite time window).

            For example, if set to 1 day, only the current day's data is
            evaluated. The reference point is the current day when
            at_any_point_in_time is unset or false.

            It can only be set when Audience scope is
            ACROSS_ALL_SESSIONS and cannot be greater than 60 days.
    """

    class StringFilter(proto.Message):
        r"""A filter for a string-type dimension that matches a
        particular pattern.

        Attributes:
            match_type (google.analytics.admin_v1alpha.types.AudienceDimensionOrMetricFilter.StringFilter.MatchType):
                Required. The match type for the string
                filter.
            value (str):
                Required. The string value to be matched
                against.
            case_sensitive (bool):
                Optional. If true, the match is
                case-sensitive. If false, the match is
                case-insensitive.
        """

        class MatchType(proto.Enum):
            r"""The match type for the string filter.

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
                    Full regular expression matches with the
                    string value.
            """

            MATCH_TYPE_UNSPECIFIED = 0
            EXACT = 1
            BEGINS_WITH = 2
            ENDS_WITH = 3
            CONTAINS = 4
            FULL_REGEXP = 5

        match_type: "AudienceDimensionOrMetricFilter.StringFilter.MatchType" = (
            proto.Field(
                proto.ENUM,
                number=1,
                enum="AudienceDimensionOrMetricFilter.StringFilter.MatchType",
            )
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
        r"""A filter for a string dimension that matches a particular
        list of options.

        Attributes:
            values (MutableSequence[str]):
                Required. The list of possible string values
                to match against. Must be non-empty.
            case_sensitive (bool):
                Optional. If true, the match is
                case-sensitive. If false, the match is
                case-insensitive.
        """

        values: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )
        case_sensitive: bool = proto.Field(
            proto.BOOL,
            number=2,
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
                Integer value.

                This field is a member of `oneof`_ ``one_value``.
            double_value (float):
                Double value.

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

    class NumericFilter(proto.Message):
        r"""A filter for numeric or date values on a dimension or metric.

        Attributes:
            operation (google.analytics.admin_v1alpha.types.AudienceDimensionOrMetricFilter.NumericFilter.Operation):
                Required. The operation applied to a numeric
                filter.
            value (google.analytics.admin_v1alpha.types.AudienceDimensionOrMetricFilter.NumericValue):
                Required. The numeric or date value to match
                against.
        """

        class Operation(proto.Enum):
            r"""The operation applied to a numeric filter.

            Values:
                OPERATION_UNSPECIFIED (0):
                    Unspecified.
                EQUAL (1):
                    Equal.
                LESS_THAN (2):
                    Less than.
                GREATER_THAN (4):
                    Greater than.
            """

            OPERATION_UNSPECIFIED = 0
            EQUAL = 1
            LESS_THAN = 2
            GREATER_THAN = 4

        operation: "AudienceDimensionOrMetricFilter.NumericFilter.Operation" = (
            proto.Field(
                proto.ENUM,
                number=1,
                enum="AudienceDimensionOrMetricFilter.NumericFilter.Operation",
            )
        )
        value: "AudienceDimensionOrMetricFilter.NumericValue" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="AudienceDimensionOrMetricFilter.NumericValue",
        )

    class BetweenFilter(proto.Message):
        r"""A filter for numeric or date values between certain values on
        a dimension or metric.

        Attributes:
            from_value (google.analytics.admin_v1alpha.types.AudienceDimensionOrMetricFilter.NumericValue):
                Required. Begins with this number, inclusive.
            to_value (google.analytics.admin_v1alpha.types.AudienceDimensionOrMetricFilter.NumericValue):
                Required. Ends with this number, inclusive.
        """

        from_value: "AudienceDimensionOrMetricFilter.NumericValue" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="AudienceDimensionOrMetricFilter.NumericValue",
        )
        to_value: "AudienceDimensionOrMetricFilter.NumericValue" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="AudienceDimensionOrMetricFilter.NumericValue",
        )

    string_filter: StringFilter = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="one_filter",
        message=StringFilter,
    )
    in_list_filter: InListFilter = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="one_filter",
        message=InListFilter,
    )
    numeric_filter: NumericFilter = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="one_filter",
        message=NumericFilter,
    )
    between_filter: BetweenFilter = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="one_filter",
        message=BetweenFilter,
    )
    field_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    at_any_point_in_time: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    in_any_n_day_period: int = proto.Field(
        proto.INT32,
        number=7,
    )


class AudienceEventFilter(proto.Message):
    r"""A filter that matches events of a single event name. If an
    event parameter is specified, only the subset of events that
    match both the single event name and the parameter filter
    expressions match this event filter.

    Attributes:
        event_name (str):
            Required. Immutable. The name of the event to
            match against.
        event_parameter_filter_expression (google.analytics.admin_v1alpha.types.AudienceFilterExpression):
            Optional. If specified, this filter matches events that
            match both the single event name and the parameter filter
            expressions. AudienceEventFilter inside the parameter filter
            expression cannot be set (For example, nested event filters
            are not supported). This should be a single and_group of
            dimension_or_metric_filter or not_expression; ANDs of ORs
            are not supported. Also, if it includes a filter for
            "eventCount", only that one will be considered; all the
            other filters will be ignored.
    """

    event_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    event_parameter_filter_expression: "AudienceFilterExpression" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="AudienceFilterExpression",
    )


class AudienceFilterExpression(proto.Message):
    r"""A logical expression of Audience dimension, metric, or event
    filters.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        and_group (google.analytics.admin_v1alpha.types.AudienceFilterExpressionList):
            A list of expressions to be AND’ed together. It can only
            contain AudienceFilterExpressions with or_group. This must
            be set for the top level AudienceFilterExpression.

            This field is a member of `oneof`_ ``expr``.
        or_group (google.analytics.admin_v1alpha.types.AudienceFilterExpressionList):
            A list of expressions to OR’ed together. It cannot contain
            AudienceFilterExpressions with and_group or or_group.

            This field is a member of `oneof`_ ``expr``.
        not_expression (google.analytics.admin_v1alpha.types.AudienceFilterExpression):
            A filter expression to be NOT'ed (For example, inverted,
            complemented). It can only include a
            dimension_or_metric_filter. This cannot be set on the top
            level AudienceFilterExpression.

            This field is a member of `oneof`_ ``expr``.
        dimension_or_metric_filter (google.analytics.admin_v1alpha.types.AudienceDimensionOrMetricFilter):
            A filter on a single dimension or metric.
            This cannot be set on the top level
            AudienceFilterExpression.

            This field is a member of `oneof`_ ``expr``.
        event_filter (google.analytics.admin_v1alpha.types.AudienceEventFilter):
            Creates a filter that matches a specific
            event. This cannot be set on the top level
            AudienceFilterExpression.

            This field is a member of `oneof`_ ``expr``.
    """

    and_group: "AudienceFilterExpressionList" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="expr",
        message="AudienceFilterExpressionList",
    )
    or_group: "AudienceFilterExpressionList" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="expr",
        message="AudienceFilterExpressionList",
    )
    not_expression: "AudienceFilterExpression" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="expr",
        message="AudienceFilterExpression",
    )
    dimension_or_metric_filter: "AudienceDimensionOrMetricFilter" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="expr",
        message="AudienceDimensionOrMetricFilter",
    )
    event_filter: "AudienceEventFilter" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="expr",
        message="AudienceEventFilter",
    )


class AudienceFilterExpressionList(proto.Message):
    r"""A list of Audience filter expressions.

    Attributes:
        filter_expressions (MutableSequence[google.analytics.admin_v1alpha.types.AudienceFilterExpression]):
            A list of Audience filter expressions.
    """

    filter_expressions: MutableSequence["AudienceFilterExpression"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="AudienceFilterExpression",
        )
    )


class AudienceSimpleFilter(proto.Message):
    r"""Defines a simple filter that a user must satisfy to be a
    member of the Audience.

    Attributes:
        scope (google.analytics.admin_v1alpha.types.AudienceFilterScope):
            Required. Immutable. Specifies the scope for
            this filter.
        filter_expression (google.analytics.admin_v1alpha.types.AudienceFilterExpression):
            Required. Immutable. A logical expression of
            Audience dimension, metric, or event filters.
    """

    scope: "AudienceFilterScope" = proto.Field(
        proto.ENUM,
        number=1,
        enum="AudienceFilterScope",
    )
    filter_expression: "AudienceFilterExpression" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="AudienceFilterExpression",
    )


class AudienceSequenceFilter(proto.Message):
    r"""Defines filters that must occur in a specific order for the
    user to be a member of the Audience.

    Attributes:
        scope (google.analytics.admin_v1alpha.types.AudienceFilterScope):
            Required. Immutable. Specifies the scope for
            this filter.
        sequence_maximum_duration (google.protobuf.duration_pb2.Duration):
            Optional. Defines the time period in which
            the whole sequence must occur.
        sequence_steps (MutableSequence[google.analytics.admin_v1alpha.types.AudienceSequenceFilter.AudienceSequenceStep]):
            Required. An ordered sequence of steps. A
            user must complete each step in order to join
            the sequence filter.
    """

    class AudienceSequenceStep(proto.Message):
        r"""A condition that must occur in the specified step order for
        this user to match the sequence.

        Attributes:
            scope (google.analytics.admin_v1alpha.types.AudienceFilterScope):
                Required. Immutable. Specifies the scope for
                this step.
            immediately_follows (bool):
                Optional. If true, the event satisfying this
                step must be the very next event after the event
                satisfying the last step. If unset or false,
                this step indirectly follows the prior step; for
                example, there may be events between the prior
                step and this step. It is ignored for the first
                step.
            constraint_duration (google.protobuf.duration_pb2.Duration):
                Optional. When set, this step must be satisfied within the
                constraint_duration of the previous step (For example, t[i]
                - t[i-1] <= constraint_duration). If not set, there is no
                duration requirement (the duration is effectively
                unlimited). It is ignored for the first step.
            filter_expression (google.analytics.admin_v1alpha.types.AudienceFilterExpression):
                Required. Immutable. A logical expression of
                Audience dimension, metric, or event filters in
                each step.
        """

        scope: "AudienceFilterScope" = proto.Field(
            proto.ENUM,
            number=1,
            enum="AudienceFilterScope",
        )
        immediately_follows: bool = proto.Field(
            proto.BOOL,
            number=2,
        )
        constraint_duration: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=3,
            message=duration_pb2.Duration,
        )
        filter_expression: "AudienceFilterExpression" = proto.Field(
            proto.MESSAGE,
            number=4,
            message="AudienceFilterExpression",
        )

    scope: "AudienceFilterScope" = proto.Field(
        proto.ENUM,
        number=1,
        enum="AudienceFilterScope",
    )
    sequence_maximum_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=2,
        message=duration_pb2.Duration,
    )
    sequence_steps: MutableSequence[AudienceSequenceStep] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=AudienceSequenceStep,
    )


class AudienceFilterClause(proto.Message):
    r"""A clause for defining either a simple or sequence filter. A
    filter can be inclusive (For example, users satisfying the
    filter clause are included in the Audience) or exclusive (For
    example, users satisfying the filter clause are excluded from
    the Audience).

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        simple_filter (google.analytics.admin_v1alpha.types.AudienceSimpleFilter):
            A simple filter that a user must satisfy to
            be a member of the Audience.

            This field is a member of `oneof`_ ``filter``.
        sequence_filter (google.analytics.admin_v1alpha.types.AudienceSequenceFilter):
            Filters that must occur in a specific order
            for the user to be a member of the Audience.

            This field is a member of `oneof`_ ``filter``.
        clause_type (google.analytics.admin_v1alpha.types.AudienceFilterClause.AudienceClauseType):
            Required. Specifies whether this is an
            include or exclude filter clause.
    """

    class AudienceClauseType(proto.Enum):
        r"""Specifies whether this is an include or exclude filter
        clause.

        Values:
            AUDIENCE_CLAUSE_TYPE_UNSPECIFIED (0):
                Unspecified clause type.
            INCLUDE (1):
                Users will be included in the Audience if the
                filter clause is met.
            EXCLUDE (2):
                Users will be excluded from the Audience if
                the filter clause is met.
        """

        AUDIENCE_CLAUSE_TYPE_UNSPECIFIED = 0
        INCLUDE = 1
        EXCLUDE = 2

    simple_filter: "AudienceSimpleFilter" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="filter",
        message="AudienceSimpleFilter",
    )
    sequence_filter: "AudienceSequenceFilter" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="filter",
        message="AudienceSequenceFilter",
    )
    clause_type: AudienceClauseType = proto.Field(
        proto.ENUM,
        number=1,
        enum=AudienceClauseType,
    )


class AudienceEventTrigger(proto.Message):
    r"""Specifies an event to log when a user joins the Audience.

    Attributes:
        event_name (str):
            Required. The event name that will be logged.
        log_condition (google.analytics.admin_v1alpha.types.AudienceEventTrigger.LogCondition):
            Required. When to log the event.
    """

    class LogCondition(proto.Enum):
        r"""Determines when to log the event.

        Values:
            LOG_CONDITION_UNSPECIFIED (0):
                Log condition is not specified.
            AUDIENCE_JOINED (1):
                The event should be logged only when a user
                is joined.
            AUDIENCE_MEMBERSHIP_RENEWED (2):
                The event should be logged whenever the
                Audience condition is met, even if the user is
                already a member of the Audience.
        """

        LOG_CONDITION_UNSPECIFIED = 0
        AUDIENCE_JOINED = 1
        AUDIENCE_MEMBERSHIP_RENEWED = 2

    event_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    log_condition: LogCondition = proto.Field(
        proto.ENUM,
        number=2,
        enum=LogCondition,
    )


class Audience(proto.Message):
    r"""A resource message representing an Audience.

    Attributes:
        name (str):
            Output only. The resource name for this
            Audience resource. Format:
            properties/{propertyId}/audiences/{audienceId}
        display_name (str):
            Required. The display name of the Audience.
        description (str):
            Required. The description of the Audience.
        membership_duration_days (int):
            Required. Immutable. The duration a user
            should stay in an Audience. It cannot be set to
            more than 540 days.
        ads_personalization_enabled (bool):
            Output only. It is automatically set by GA to
            false if this is an NPA Audience and is excluded
            from ads personalization.
        event_trigger (google.analytics.admin_v1alpha.types.AudienceEventTrigger):
            Optional. Specifies an event to log when a
            user joins the Audience. If not set, no event is
            logged when a user joins the Audience.
        exclusion_duration_mode (google.analytics.admin_v1alpha.types.Audience.AudienceExclusionDurationMode):
            Immutable. Specifies how long an exclusion
            lasts for users that meet the exclusion filter.
            It is applied to all EXCLUDE filter clauses and
            is ignored when there is no EXCLUDE filter
            clause in the Audience.
        filter_clauses (MutableSequence[google.analytics.admin_v1alpha.types.AudienceFilterClause]):
            Required. Immutable. Unordered list. Filter
            clauses that define the Audience. All clauses
            will be AND’ed together.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when the Audience was
            created.
    """

    class AudienceExclusionDurationMode(proto.Enum):
        r"""Specifies how long an exclusion lasts for users that meet the
        exclusion filter.

        Values:
            AUDIENCE_EXCLUSION_DURATION_MODE_UNSPECIFIED (0):
                Not specified.
            EXCLUDE_TEMPORARILY (1):
                Exclude users from the Audience during
                periods when they meet the filter clause.
            EXCLUDE_PERMANENTLY (2):
                Exclude users from the Audience if they've
                ever met the filter clause.
        """

        AUDIENCE_EXCLUSION_DURATION_MODE_UNSPECIFIED = 0
        EXCLUDE_TEMPORARILY = 1
        EXCLUDE_PERMANENTLY = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    membership_duration_days: int = proto.Field(
        proto.INT32,
        number=4,
    )
    ads_personalization_enabled: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    event_trigger: "AudienceEventTrigger" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="AudienceEventTrigger",
    )
    exclusion_duration_mode: AudienceExclusionDurationMode = proto.Field(
        proto.ENUM,
        number=7,
        enum=AudienceExclusionDurationMode,
    )
    filter_clauses: MutableSequence["AudienceFilterClause"] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message="AudienceFilterClause",
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
