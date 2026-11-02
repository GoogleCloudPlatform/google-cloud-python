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
        "ChannelGroupFilter",
        "ChannelGroupFilterExpression",
        "ChannelGroupFilterExpressionList",
        "GroupingRule",
        "ChannelGroup",
    },
)


class ChannelGroupFilter(proto.Message):
    r"""A specific filter for a single dimension.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        string_filter (google.analytics.admin_v1alpha.types.ChannelGroupFilter.StringFilter):
            A filter for a string-type dimension that
            matches a particular pattern.

            This field is a member of `oneof`_ ``value_filter``.
        in_list_filter (google.analytics.admin_v1alpha.types.ChannelGroupFilter.InListFilter):
            A filter for a string dimension that matches
            a particular list of options.

            This field is a member of `oneof`_ ``value_filter``.
        field_name (str):
            Required. Immutable. The dimension name to
            filter.
    """

    class StringFilter(proto.Message):
        r"""Filter where the field value is a String. The match is case
        insensitive.

        Attributes:
            match_type (google.analytics.admin_v1alpha.types.ChannelGroupFilter.StringFilter.MatchType):
                Required. The match type for the string
                filter.
            value (str):
                Required. The string value to be matched
                against.
        """

        class MatchType(proto.Enum):
            r"""How the filter will be used to determine a match.

            Values:
                MATCH_TYPE_UNSPECIFIED (0):
                    Default match type.
                EXACT (1):
                    Exact match of the string value.
                BEGINS_WITH (2):
                    Begins with the string value.
                ENDS_WITH (3):
                    Ends with the string value.
                CONTAINS (4):
                    Contains the string value.
                FULL_REGEXP (5):
                    Full regular expression match with the string
                    value.
                PARTIAL_REGEXP (6):
                    Partial regular expression match with the
                    string value.
            """

            MATCH_TYPE_UNSPECIFIED = 0
            EXACT = 1
            BEGINS_WITH = 2
            ENDS_WITH = 3
            CONTAINS = 4
            FULL_REGEXP = 5
            PARTIAL_REGEXP = 6

        match_type: "ChannelGroupFilter.StringFilter.MatchType" = proto.Field(
            proto.ENUM,
            number=1,
            enum="ChannelGroupFilter.StringFilter.MatchType",
        )
        value: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class InListFilter(proto.Message):
        r"""A filter for a string dimension that matches a particular
        list of options. The match is case insensitive.

        Attributes:
            values (MutableSequence[str]):
                Required. The list of possible string values
                to match against. Must be non-empty.
        """

        values: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )

    string_filter: StringFilter = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="value_filter",
        message=StringFilter,
    )
    in_list_filter: InListFilter = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="value_filter",
        message=InListFilter,
    )
    field_name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ChannelGroupFilterExpression(proto.Message):
    r"""A logical expression of Channel Group dimension filters.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        and_group (google.analytics.admin_v1alpha.types.ChannelGroupFilterExpressionList):
            A list of expressions to be AND’ed together. It can only
            contain ChannelGroupFilterExpressions with or_group. This
            must be set for the top level ChannelGroupFilterExpression.

            This field is a member of `oneof`_ ``expr``.
        or_group (google.analytics.admin_v1alpha.types.ChannelGroupFilterExpressionList):
            A list of expressions to OR’ed together. It cannot contain
            ChannelGroupFilterExpressions with and_group or or_group.

            This field is a member of `oneof`_ ``expr``.
        not_expression (google.analytics.admin_v1alpha.types.ChannelGroupFilterExpression):
            A filter expression to be NOT'ed (that is inverted,
            complemented). It can only include a
            dimension_or_metric_filter. This cannot be set on the top
            level ChannelGroupFilterExpression.

            This field is a member of `oneof`_ ``expr``.
        filter (google.analytics.admin_v1alpha.types.ChannelGroupFilter):
            A filter on a single dimension. This cannot
            be set on the top level
            ChannelGroupFilterExpression.

            This field is a member of `oneof`_ ``expr``.
    """

    and_group: "ChannelGroupFilterExpressionList" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="expr",
        message="ChannelGroupFilterExpressionList",
    )
    or_group: "ChannelGroupFilterExpressionList" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="expr",
        message="ChannelGroupFilterExpressionList",
    )
    not_expression: "ChannelGroupFilterExpression" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="expr",
        message="ChannelGroupFilterExpression",
    )
    filter: "ChannelGroupFilter" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="expr",
        message="ChannelGroupFilter",
    )


class ChannelGroupFilterExpressionList(proto.Message):
    r"""A list of Channel Group filter expressions.

    Attributes:
        filter_expressions (MutableSequence[google.analytics.admin_v1alpha.types.ChannelGroupFilterExpression]):
            A list of Channel Group filter expressions.
    """

    filter_expressions: MutableSequence["ChannelGroupFilterExpression"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="ChannelGroupFilterExpression",
        )
    )


class GroupingRule(proto.Message):
    r"""The rules that govern how traffic is grouped into one
    channel.

    Attributes:
        display_name (str):
            Required. Customer defined display name for
            the channel.
        expression (google.analytics.admin_v1alpha.types.ChannelGroupFilterExpression):
            Required. The Filter Expression that defines
            the Grouping Rule.
    """

    display_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    expression: "ChannelGroupFilterExpression" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ChannelGroupFilterExpression",
    )


class ChannelGroup(proto.Message):
    r"""A resource message representing a Channel Group.

    Attributes:
        name (str):
            Output only. The resource name for this Channel Group
            resource. Format:
            properties/{property}/channelGroups/{channel_group}
        display_name (str):
            Required. The display name of the Channel
            Group. Max length of 80 characters.
        description (str):
            The description of the Channel Group. Max
            length of 256 characters.
        grouping_rule (MutableSequence[google.analytics.admin_v1alpha.types.GroupingRule]):
            Required. The grouping rules of channels.
            Maximum number of rules is 50.
        system_defined (bool):
            Output only. If true, then this channel group
            is the Default Channel Group predefined by
            Google Analytics. Display name and grouping
            rules cannot be updated for this channel group.
        primary (bool):
            Optional. If true, this channel group will be used as the
            default channel group for reports. Only one channel group
            can be set as ``primary`` at any time. If the ``primary``
            field gets set on a channel group, it will get unset on the
            previous primary channel group.

            The Google Analytics predefined channel group is the primary
            by default.
    """

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
    grouping_rule: MutableSequence["GroupingRule"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="GroupingRule",
    )
    system_defined: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    primary: bool = proto.Field(
        proto.BOOL,
        number=6,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
