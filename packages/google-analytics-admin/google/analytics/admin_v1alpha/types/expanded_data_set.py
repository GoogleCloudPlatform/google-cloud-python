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

import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.analytics.admin.v1alpha",
    manifest={
        "ExpandedDataSetFilter",
        "ExpandedDataSetFilterExpression",
        "ExpandedDataSetFilterExpressionList",
        "ExpandedDataSet",
    },
)


class ExpandedDataSetFilter(proto.Message):
    r"""A specific filter for a single dimension

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        string_filter (google.analytics.admin_v1alpha.types.ExpandedDataSetFilter.StringFilter):
            A filter for a string-type dimension that
            matches a particular pattern.

            This field is a member of `oneof`_ ``one_filter``.
        in_list_filter (google.analytics.admin_v1alpha.types.ExpandedDataSetFilter.InListFilter):
            A filter for a string dimension that matches
            a particular list of options.

            This field is a member of `oneof`_ ``one_filter``.
        field_name (str):
            Required. The dimension name to filter.
    """

    class StringFilter(proto.Message):
        r"""A filter for a string-type dimension that matches a
        particular pattern.

        Attributes:
            match_type (google.analytics.admin_v1alpha.types.ExpandedDataSetFilter.StringFilter.MatchType):
                Required. The match type for the string
                filter.
            value (str):
                Required. The string value to be matched
                against.
            case_sensitive (bool):
                Optional. If true, the match is case-sensitive. If false,
                the match is case-insensitive. Must be true when match_type
                is EXACT. Must be false when match_type is CONTAINS.
        """

        class MatchType(proto.Enum):
            r"""The match type for the string filter.

            Values:
                MATCH_TYPE_UNSPECIFIED (0):
                    Unspecified
                EXACT (1):
                    Exact match of the string value.
                CONTAINS (2):
                    Contains the string value.
            """

            MATCH_TYPE_UNSPECIFIED = 0
            EXACT = 1
            CONTAINS = 2

        match_type: "ExpandedDataSetFilter.StringFilter.MatchType" = proto.Field(
            proto.ENUM,
            number=1,
            enum="ExpandedDataSetFilter.StringFilter.MatchType",
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
                case-insensitive. Must be true.
        """

        values: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )
        case_sensitive: bool = proto.Field(
            proto.BOOL,
            number=2,
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
    field_name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ExpandedDataSetFilterExpression(proto.Message):
    r"""A logical expression of EnhancedDataSet dimension filters.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        and_group (google.analytics.admin_v1alpha.types.ExpandedDataSetFilterExpressionList):
            A list of expressions to be AND’ed together. It must contain
            a ExpandedDataSetFilterExpression with either not_expression
            or dimension_filter. This must be set for the top level
            ExpandedDataSetFilterExpression.

            This field is a member of `oneof`_ ``expr``.
        not_expression (google.analytics.admin_v1alpha.types.ExpandedDataSetFilterExpression):
            A filter expression to be NOT'ed (that is, inverted,
            complemented). It must include a dimension_filter. This
            cannot be set on the top level
            ExpandedDataSetFilterExpression.

            This field is a member of `oneof`_ ``expr``.
        filter (google.analytics.admin_v1alpha.types.ExpandedDataSetFilter):
            A filter on a single dimension. This cannot
            be set on the top level
            ExpandedDataSetFilterExpression.

            This field is a member of `oneof`_ ``expr``.
    """

    and_group: "ExpandedDataSetFilterExpressionList" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="expr",
        message="ExpandedDataSetFilterExpressionList",
    )
    not_expression: "ExpandedDataSetFilterExpression" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="expr",
        message="ExpandedDataSetFilterExpression",
    )
    filter: "ExpandedDataSetFilter" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="expr",
        message="ExpandedDataSetFilter",
    )


class ExpandedDataSetFilterExpressionList(proto.Message):
    r"""A list of ExpandedDataSet filter expressions.

    Attributes:
        filter_expressions (MutableSequence[google.analytics.admin_v1alpha.types.ExpandedDataSetFilterExpression]):
            A list of ExpandedDataSet filter expressions.
    """

    filter_expressions: MutableSequence["ExpandedDataSetFilterExpression"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="ExpandedDataSetFilterExpression",
        )
    )


class ExpandedDataSet(proto.Message):
    r"""A resource message representing an ``ExpandedDataSet``.

    Attributes:
        name (str):
            Output only. The resource name for this ExpandedDataSet
            resource. Format:
            properties/{property_id}/expandedDataSets/{expanded_data_set}
        display_name (str):
            Required. The display name of the
            ExpandedDataSet. Max 200 chars.
        description (str):
            Optional. The description of the
            ExpandedDataSet. Max 50 chars.
        dimension_names (MutableSequence[str]):
            Immutable. The list of dimensions included in the
            ExpandedDataSet. See the `API
            Dimensions <https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema#dimensions>`__
            for the list of dimension names.
        metric_names (MutableSequence[str]):
            Immutable. The list of metrics included in the
            ExpandedDataSet. See the `API
            Metrics <https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema#metrics>`__
            for the list of dimension names.
        dimension_filter_expression (google.analytics.admin_v1alpha.types.ExpandedDataSetFilterExpression):
            Immutable. A logical expression of ExpandedDataSet filters
            applied to dimension included in the ExpandedDataSet. This
            filter is used to reduce the number of rows and thus the
            chance of encountering ``other`` row.
        data_collection_start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when expanded data set
            began (or will begin) collecing data.
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
    dimension_names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    metric_names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    dimension_filter_expression: "ExpandedDataSetFilterExpression" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="ExpandedDataSetFilterExpression",
    )
    data_collection_start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
