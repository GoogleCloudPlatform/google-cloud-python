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
    package="google.cloud.apptopology.v1",
    manifest={
        "GraphPattern",
        "NodePattern",
        "EdgePattern",
        "ConnectedNodePattern",
        "LabelPropertiesPattern",
    },
)


class GraphPattern(proto.Message):
    r"""Recursive graph pattern matcher to select and constrain the
    returned topology.
    AppTopology API allows cycle in the graph traversal and will
    return unique node and edge results in the response.
    SLO is guaranteed for at most 5 hops in the graph traversal.

    Attributes:
        starting_node (google.cloud.apptopology_v1.types.NodePattern):
            Required. Pattern matcher to select the
            starting nodes in the graph.
        neighbors (MutableSequence[google.cloud.apptopology_v1.types.ConnectedNodePattern]):
            Optional. Pattern matcher to match the
            connected subgraphs; all of these are ANDed.
    """

    starting_node: "NodePattern" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="NodePattern",
    )
    neighbors: MutableSequence["ConnectedNodePattern"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="ConnectedNodePattern",
    )


class NodePattern(proto.Message):
    r"""Node pattern matcher to match the node id, labels and
    properties.

    Attributes:
        alias (str):
            Optional. Represents an identifier to be referenced in
            ``property_matcher_expr``. For example, an alias for ``app``
            can be referenced as ``app.Base/location="us-central1"``.
            ``alias`` must be unique within the query, otherwise an
            error will be returned.
        label_properties_pattern (google.cloud.apptopology_v1.types.LabelPropertiesPattern):
            Optional. Matcher for labels/properties.
    """

    alias: str = proto.Field(
        proto.STRING,
        number=1,
    )
    label_properties_pattern: "LabelPropertiesPattern" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="LabelPropertiesPattern",
    )


class EdgePattern(proto.Message):
    r"""Edge pattern matcher to match the edge direction, labels and
    properties.

    Attributes:
        direction (google.cloud.apptopology_v1.types.EdgePattern.Direction):
            Required. The direction of the edge to match.
        label_properties_pattern (google.cloud.apptopology_v1.types.LabelPropertiesPattern):
            Required. Matcher for labels/properties.
        alias (str):
            Optional. Represents an identifier to be referenced in
            ``property_matcher_expr``. For example, an alias for
            ``edge`` can be referenced as
            ``edge.description = "value_1"``. ``alias`` must be unique
            within the query, otherwise an error will be returned.
    """

    class Direction(proto.Enum):
        r"""The direction of the edge to match.

        Values:
            DIRECTION_UNSPECIFIED (0):
                Defaults to DIRECTION_UNSPECIFIED.
            ANY (1):
                Match any edge direction.
            TO (2):
                Match the edge direction from source to
                destination.
            FROM (3):
                Match the edge direction from destination to
                source.
        """

        DIRECTION_UNSPECIFIED = 0
        ANY = 1
        TO = 2
        FROM = 3

    direction: Direction = proto.Field(
        proto.ENUM,
        number=1,
        enum=Direction,
    )
    label_properties_pattern: "LabelPropertiesPattern" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="LabelPropertiesPattern",
    )
    alias: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ConnectedNodePattern(proto.Message):
    r"""Edge pattern matcher to match the edge direction, labels and
    properties.

    Attributes:
        edge (google.cloud.apptopology_v1.types.EdgePattern):
            Required. To match the edge connected the
            neighbor subgraph.
        graph (google.cloud.apptopology_v1.types.GraphPattern):
            Required. Recursive matcher to match the
            neighbor subgraph.
    """

    edge: "EdgePattern" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="EdgePattern",
    )
    graph: "GraphPattern" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="GraphPattern",
    )


class LabelPropertiesPattern(proto.Message):
    r"""Matcher for label and property. The matcher accepts both
    exact match and expression.

    Attributes:
        label_matcher_expr (str):
            Required. Matcher expression for labels. Allow OR / AND
            operators; The syntax is defined by the following grammar:

            - The label expression can use either ``OR`` or ``AND``
              operator, but not a combination of both. Example:
              ``AppHub/Application``,
              ``AppHub/Workload OR AppHub/Service``
        property_matcher_expr (str):
            Optional. The syntax of the filter is defined by the
            following grammar: https://google.aip.dev/160.

            Referencing properties of graph elements using traversal
            operator ``.``. Repeated properties cannot be traversed.
            e.g. ``e.NodeName``, where ``e`` is a node or edge alias.

            The following properties are supported for all node and edge
            types:

            - ``Labels``: repeated string property. Can be used to
              combine conditions between labels and properties. e.g.
              ``e.Labels : "label_1"`` to match a node/edge with label
              ``label_1``.
            - ``NodeName/EdgeName``: string property. Support for
              filtering by node or edge names. e.g.
              ``app.NodeName = "apphub.io/Application"``

            Other properties types can be found at
            https://apptopology.googleapis.com/v1/GetSchema

            The following operators are supported on properties:

            1. Checking if a non-repeated property of a graph element is
               equal to a scalar value using the equality operator
               ``=``.

            - LHS must be a node/edge property.
            - RHS must be a scalar literal.
            - Supported value types: string (enclosed in double quotes),
              int, double, and boolean. e.g. ``e.project = "project_1"``

            2. Checking if a non-repeated property of a graph element
               satisfies a condition using the comparison operators
               ``>``, ``<``, ``>=``, ``<=``.

            - LHS must be a node/edge property.
            - RHS must be a scalar literal.
            - Supported value types: string (enclosed in double quotes),
              int, double. e.g. ``e.NumericProperty < 0.1``

            3. Checking if a scalar value is present in a repeated
               property HAS operator ``:``.

            - LHS must be a repeated property.
            - RHS must be a scalar literal.
            - Supported value types: string (enclosed in double quotes),
              int, double. e.g. ``e.Labels : "label_1"``, where
              ``e.Labels`` is a repeated string property.

            4. Checking if a property is present using HAS_PROPERTY
               operator ``:``.

            - LHS must be a node or edge alias.
            - RHS must be a property name. e.g. ``e : Base/Location``,
              where ``e`` is a node or edge alias.

            5. Combining multiple filters using logical operators :
               ``AND``, and ``OR``.

            - Parentheses must be used to resolve ambiguity. e.g.
              ``e.Base/Location = "us-central1" AND e.project = "project_1"``

            6. The following custom functions are supported:

               - **EQUALS_ANY(arg1, arg2, arg3, ...)**

                 - Checks if ``arg1`` (a non-repeated property) equals
                   any of the subsequent scalar literal arguments.
                 - arg1: non-repeated property. Supported value types:
                   string (enclosed in double quotes), int, double.
                 - arg2, arg3, ...: The remaining arguments are literal
                   values to compare against. All the arguments must be
                   of the same type.
                 - e.g.
                   ``EQUALS_ANY(e.project, "project_1", "project_2")``

               - **CONTAINS_ANY(arg1, arg2, arg3, ...)**

                 - Checks if a repeated property has any of the given
                   scalar literals. arg1: repeated_property. Supported
                   element types: string (enclosed in double quotes),
                   int, double.
                 - arg2, arg3, ...: The remaining arguments are literal
                   values to compare against. All the arguments must be
                   of the same type.
                 - e.g.
                   ``CONTAINS_ANY(e.folders, "folder_1", "folder_2")``

               - **CONTAINS_ANY_LESS_THAN(arg1, arg2)**

                 - Checks if a repeated property has any element less
                   than the given scalar literal.
                 - arg1: repeated_property. Supported element types are:
                   int, double.
                 - arg2: scalar literal
                 - e.g.
                   ``CONTAINS_ANY_LESS_THAN(e.NumericProperty, 0.1)``

               - **CONTAINS_ANY_GREATER_THAN(arg1, arg2)**

                 - Checks if a repeated property has any element greater
                   than the given scalar literal.
                 - arg1: repeated_property. Supported element types are:
                   int, double.
                 - arg2: scalar literal
                 - e.g.
                   ``CONTAINS_ANY_GREATER_THAN(e.NumericProperty, 0.1)``

               - **CONTAINS_ANY_LESS_OR_EQUAL(arg1, arg2)**

                 - Checks if a repeated property has any element less
                   than or equal to the given scalar literal.
                 - arg1: repeated_property. Supported element types are:
                   int, double.
                 - arg2: scalar literal
                 - e.g.
                   ``CONTAINS_ANY_LESS_OR_EQUAL(e.NumericProperty, 0.1)``

               - **CONTAINS_ANY_GREATER_OR_EQUAL(arg1, arg2)**

                 - Checks if a repeated property has any element greater
                   than or equal to the given scalar literal.
                 - arg1: repeated_property. Supported element types are:
                   int, double.
                 - arg2: scalar literal
                 - e.g.
                   ``CONTAINS_ANY_GREATER_OR_EQUAL(e.NumericProperty, 0.1)``

            NOTE:

            - For Alert nodes, only the equality operator ``=`` is
              supported. The expression cannot be a composite boolean
              expression (i.e., combining multiple conditions with
              AND/OR is not supported; it must be simple). e.g.
              ``a.NodeName = "alert-1"`` is supported, but
              ``a.NodeName = "alert-1" OR a.NodeName = "alert-2"`` is
              not supported.
            - For traffic edges, filters cannot be added.
    """

    label_matcher_expr: str = proto.Field(
        proto.STRING,
        number=1,
    )
    property_matcher_expr: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
