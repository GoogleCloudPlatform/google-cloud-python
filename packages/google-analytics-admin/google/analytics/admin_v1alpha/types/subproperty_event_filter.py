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
    package="google.analytics.admin.v1alpha",
    manifest={
        "SubpropertyEventFilterCondition",
        "SubpropertyEventFilterExpression",
        "SubpropertyEventFilterExpressionList",
        "SubpropertyEventFilterClause",
        "SubpropertyEventFilter",
    },
)


class SubpropertyEventFilterCondition(proto.Message):
    r"""A specific filter expression

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        null_filter (bool):
            A filter for null values.

            This field is a member of `oneof`_ ``one_filter``.
        string_filter (google.analytics.admin_v1alpha.types.SubpropertyEventFilterCondition.StringFilter):
            A filter for a string-type dimension that
            matches a particular pattern.

            This field is a member of `oneof`_ ``one_filter``.
        field_name (str):
            Required. The field that is being filtered.
    """

    class StringFilter(proto.Message):
        r"""A filter for a string-type dimension that matches a
        particular pattern.

        Attributes:
            match_type (google.analytics.admin_v1alpha.types.SubpropertyEventFilterCondition.StringFilter.MatchType):
                Required. The match type for the string
                filter.
            value (str):
                Required. The string value used for the
                matching.
            case_sensitive (bool):
                Optional. If true, the string value is case
                sensitive. If false, the match is
                case-insensitive.
        """

        class MatchType(proto.Enum):
            r"""How the filter will be used to determine a match.

            Values:
                MATCH_TYPE_UNSPECIFIED (0):
                    Match type unknown or not specified.
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
                PARTIAL_REGEXP (6):
                    Partial regular expression matches with the
                    string value.
            """

            MATCH_TYPE_UNSPECIFIED = 0
            EXACT = 1
            BEGINS_WITH = 2
            ENDS_WITH = 3
            CONTAINS = 4
            FULL_REGEXP = 5
            PARTIAL_REGEXP = 6

        match_type: "SubpropertyEventFilterCondition.StringFilter.MatchType" = (
            proto.Field(
                proto.ENUM,
                number=1,
                enum="SubpropertyEventFilterCondition.StringFilter.MatchType",
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

    null_filter: bool = proto.Field(
        proto.BOOL,
        number=2,
        oneof="one_filter",
    )
    string_filter: StringFilter = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="one_filter",
        message=StringFilter,
    )
    field_name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class SubpropertyEventFilterExpression(proto.Message):
    r"""A logical expression of Subproperty event filters.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        or_group (google.analytics.admin_v1alpha.types.SubpropertyEventFilterExpressionList):
            A list of expressions to OR’ed together. Must only contain
            not_expression or filter_condition expressions.

            This field is a member of `oneof`_ ``expr``.
        not_expression (google.analytics.admin_v1alpha.types.SubpropertyEventFilterExpression):
            A filter expression to be NOT'ed (inverted,
            complemented). It can only include a filter.
            This cannot be set on the top level
            SubpropertyEventFilterExpression.

            This field is a member of `oneof`_ ``expr``.
        filter_condition (google.analytics.admin_v1alpha.types.SubpropertyEventFilterCondition):
            Creates a filter that matches a specific
            event. This cannot be set on the top level
            SubpropertyEventFilterExpression.

            This field is a member of `oneof`_ ``expr``.
    """

    or_group: "SubpropertyEventFilterExpressionList" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="expr",
        message="SubpropertyEventFilterExpressionList",
    )
    not_expression: "SubpropertyEventFilterExpression" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="expr",
        message="SubpropertyEventFilterExpression",
    )
    filter_condition: "SubpropertyEventFilterCondition" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="expr",
        message="SubpropertyEventFilterCondition",
    )


class SubpropertyEventFilterExpressionList(proto.Message):
    r"""A list of Subproperty event filter expressions.

    Attributes:
        filter_expressions (MutableSequence[google.analytics.admin_v1alpha.types.SubpropertyEventFilterExpression]):
            Required. Unordered list. A list of
            Subproperty event filter expressions
    """

    filter_expressions: MutableSequence["SubpropertyEventFilterExpression"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="SubpropertyEventFilterExpression",
        )
    )


class SubpropertyEventFilterClause(proto.Message):
    r"""A clause for defining a filter. A filter may be inclusive
    (events satisfying the filter clause are included in the
    subproperty's data) or exclusive (events satisfying the filter
    clause are excluded from the subproperty's data).

    Attributes:
        filter_clause_type (google.analytics.admin_v1alpha.types.SubpropertyEventFilterClause.FilterClauseType):
            Required. The type for the filter clause.
        filter_expression (google.analytics.admin_v1alpha.types.SubpropertyEventFilterExpression):
            Required. The logical expression for what
            events are sent to the subproperty.
    """

    class FilterClauseType(proto.Enum):
        r"""Specifies whether this is an include or exclude filter
        clause.

        Values:
            FILTER_CLAUSE_TYPE_UNSPECIFIED (0):
                Filter clause type unknown or not specified.
            INCLUDE (1):
                Events will be included in the Sub property
                if the filter clause is met.
            EXCLUDE (2):
                Events will be excluded from the Sub property
                if the filter clause is met.
        """

        FILTER_CLAUSE_TYPE_UNSPECIFIED = 0
        INCLUDE = 1
        EXCLUDE = 2

    filter_clause_type: FilterClauseType = proto.Field(
        proto.ENUM,
        number=1,
        enum=FilterClauseType,
    )
    filter_expression: "SubpropertyEventFilterExpression" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="SubpropertyEventFilterExpression",
    )


class SubpropertyEventFilter(proto.Message):
    r"""A resource message representing a Google Analytics
    subproperty event filter.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Output only. Format:
            properties/{ordinary_property_id}/subpropertyEventFilters/{sub_property_event_filter}
            Example: properties/1234/subpropertyEventFilters/5678
        apply_to_property (str):
            Immutable. Resource name of the Subproperty
            that uses this filter.

            This field is a member of `oneof`_ ``_apply_to_property``.
        filter_clauses (MutableSequence[google.analytics.admin_v1alpha.types.SubpropertyEventFilterClause]):
            Required. Unordered list. Filter clauses that
            define the SubpropertyEventFilter. All clauses
            are AND'ed together to determine what data is
            sent to the subproperty.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    apply_to_property: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    filter_clauses: MutableSequence["SubpropertyEventFilterClause"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message="SubpropertyEventFilterClause",
        )
    )


__all__ = tuple(sorted(__protobuf__.manifest))
