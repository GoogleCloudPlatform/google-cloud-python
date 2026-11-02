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
        "Domain",
        "Schema",
        "NodeType",
        "EdgeType",
        "NodeGroup",
        "EdgeRule",
        "LabelProperties",
        "Property",
        "StringValue",
        "IntValue",
        "BoolValue",
        "DoubleValue",
    },
)


class Domain(proto.Message):
    r"""Domain is a pre-defined topology query domain. Each topology
    domain contains a set of nodes and edges.

    Attributes:
        name (str):
            Identifier. The pre-defined topology domain. Currently only
            SRE, DEVOPS, and SECURITY are available. Format:
            ``projects/{project}/locations/{location}/domains/{domain}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class Schema(proto.Message):
    r"""Schema is a collection of supported node & edge labels and
    properties for an overlay.

    Attributes:
        name (str):
            Identifier. The resource name of the schema. Format:
            ``projects/{project}/locations/{location}/domains/{domain}/schema``
        node_types (MutableSequence[google.cloud.apptopology_v1.types.NodeType]):
            A list of ``NodeType``\ s defined within this schema. Refer
            to the documentation of ``NodeType`` for more details.
        edge_types (MutableSequence[google.cloud.apptopology_v1.types.EdgeType]):
            A list of ``EdgeType``\ s defined within this schema. Refer
            to the documentation of ``EdgeType`` for more details.
        label_properties (MutableSequence[google.cloud.apptopology_v1.types.LabelProperties]):
            A list of supported labels and corresponding
            properties.
        edge_rules (MutableSequence[google.cloud.apptopology_v1.types.EdgeRule]):
            Edge rules. These will indicate which node types can be
            connected and through what edge type. This is a list of
            (source_node_type, edge_type, destination_node_type) tuples.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    node_types: MutableSequence["NodeType"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="NodeType",
    )
    edge_types: MutableSequence["EdgeType"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="EdgeType",
    )
    label_properties: MutableSequence["LabelProperties"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="LabelProperties",
    )
    edge_rules: MutableSequence["EdgeRule"] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message="EdgeRule",
    )


class NodeType(proto.Message):
    r"""NodeType defines the schema of a node type in the graph.

    Attributes:
        type_ (str):
            REQUIRED
            Name of the node type.
            This name is used to access the node type while
            defining the schema.
        labels (MutableSequence[str]):
            Labels attached to the node. Composable,
            namespaced building blocks that define core
            attributes through associated properties.
            Multiple labels aggregate to fully specify the
            functional traits and property schema of the
            node type.
        description (str):
            A human-readable description of the ``NodeType``.
        optional_labels (MutableSequence[str]):
            A node of this node type can have 0 or more
            of these labels. These node objects of this node
            type will have these labels alongside the
            required labels.
    """

    type_: str = proto.Field(
        proto.STRING,
        number=1,
    )
    labels: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    optional_labels: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )


class EdgeType(proto.Message):
    r"""EdgeType defines the schema of an edge type in the graph.

    Attributes:
        type_ (str):
            REQUIRED
            Name of the edge type.
            This name is used to access the edge type while
            defining the schema.
        labels (MutableSequence[str]):
            Labels attached to the edge. Composable,
            namespaced building blocks that define core
            attributes through associated properties.
            Multiple labels aggregate to fully specify the
            functional traits and property schema of the
            edge type.
        description (str):
            A human-readable description of the ``EdgeType``.
        optional_labels (MutableSequence[str]):
            An edge of this edge type can have 0 or more
            of these labels. These edge objects of this edge
            type will have these labels alongside the
            required labels.
    """

    type_: str = proto.Field(
        proto.STRING,
        number=1,
    )
    labels: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    optional_labels: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )


class NodeGroup(proto.Message):
    r"""NodeGroup represents a dynamic collection of nodes that
    satisfy specific criteria. A node is considered part of this
    group if it matches the defined constraints.

    Attributes:
        any_labels (MutableSequence[str]):
            Optional. A node must have at least one of
            these labels to be included in the group. If
            empty or unset, this constraint is not applied.
    """

    any_labels: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class EdgeRule(proto.Message):
    r"""EdgeRule defines the connection rules for nodes in the graph.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        src_node_type (str):
            Optional. The specific node type name that
            acts as the source for this edge.

            This field is a member of `oneof`_ ``source_node``.
        src_node_group (google.cloud.apptopology_v1.types.NodeGroup):
            Optional. A dynamic group of nodes, defined
            by label constraints, that can act as the source
            for this edge.

            This field is a member of `oneof`_ ``source_node``.
        dest_node_type (str):
            Optional. The specific node type name that
            acts as the destination for this edge.

            This field is a member of `oneof`_ ``destination_node``.
        dest_node_group (google.cloud.apptopology_v1.types.NodeGroup):
            Optional. A dynamic group of nodes, defined
            by label constraints, that can act as the
            destination for this edge.

            This field is a member of `oneof`_ ``destination_node``.
        edge_type (str):
            Optional. Name of the connected edge type.
    """

    src_node_type: str = proto.Field(
        proto.STRING,
        number=4,
        oneof="source_node",
    )
    src_node_group: "NodeGroup" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="source_node",
        message="NodeGroup",
    )
    dest_node_type: str = proto.Field(
        proto.STRING,
        number=6,
        oneof="destination_node",
    )
    dest_node_group: "NodeGroup" = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="destination_node",
        message="NodeGroup",
    )
    edge_type: str = proto.Field(
        proto.STRING,
        number=3,
    )


class LabelProperties(proto.Message):
    r"""Identifier for the label and corresponding properties.

    Attributes:
        label (str):
            Full qualified name of the label.
        properties (MutableSequence[google.cloud.apptopology_v1.types.Property]):
            List of properties associated with the label.
        description (str):
            A human-readable description of the label.
    """

    label: str = proto.Field(
        proto.STRING,
        number=1,
    )
    properties: MutableSequence["Property"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="Property",
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )


class Property(proto.Message):
    r"""Property defines the schema of a property in the graph.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        string_value (google.cloud.apptopology_v1.types.StringValue):
            StringValue represents a property that has a
            string value type.

            This field is a member of `oneof`_ ``value``.
        int_value (google.cloud.apptopology_v1.types.IntValue):
            IntValue represents a property that has an
            integer value type.

            This field is a member of `oneof`_ ``value``.
        bool_value (google.cloud.apptopology_v1.types.BoolValue):
            BoolValue represents a property that has a
            boolean value type.

            This field is a member of `oneof`_ ``value``.
        double_value (google.cloud.apptopology_v1.types.DoubleValue):
            DoubleValue represents a property that has a
            double value type.

            This field is a member of `oneof`_ ``value``.
        name (str):
            ``name`` is the key string to identify the property in
            ``Node``\ s & ``Edge``\ s. Examples: ``ProjectId``,
            ``Base/displayName`` etc.
        description (str):
            A human-readable description of the ``PropertyType``,
            explaining its meaning, purpose, and any constraints or
            expectations on its value.
    """

    string_value: "StringValue" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="value",
        message="StringValue",
    )
    int_value: "IntValue" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="value",
        message="IntValue",
    )
    bool_value: "BoolValue" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="value",
        message="BoolValue",
    )
    double_value: "DoubleValue" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="value",
        message="DoubleValue",
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=10,
    )


class StringValue(proto.Message):
    r"""StringValue represents a property that has a string value
    type.

    Attributes:
        repeated (bool):
            OPTIONAL
            Whether the property is repeated.
        allowed_values (MutableSequence[str]):
            OPTIONAL
            Allowed values for the property. If provided,
            the property value must be one of the allowed
            values.
    """

    repeated: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    allowed_values: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class IntValue(proto.Message):
    r"""IntValue represents a property that has an integer value
    type.

    Attributes:
        repeated (bool):
            OPTIONAL
            Whether the property is repeated.
        allowed_values (MutableSequence[int]):
            OPTIONAL
            Allowed values for the property. If provided,
            the property value must be one of the allowed
            values.
    """

    repeated: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    allowed_values: MutableSequence[int] = proto.RepeatedField(
        proto.INT64,
        number=2,
    )


class BoolValue(proto.Message):
    r"""BoolValue represents a property that has a boolean value
    type.

    Attributes:
        repeated (bool):
            OPTIONAL
            Whether the property is repeated.
        allowed_values (MutableSequence[bool]):
            OPTIONAL
            Allowed values for the property. If provided,
            the property value must be one of the allowed
            values.
    """

    repeated: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    allowed_values: MutableSequence[bool] = proto.RepeatedField(
        proto.BOOL,
        number=2,
    )


class DoubleValue(proto.Message):
    r"""DoubleValue represents a property that has a double value
    type.

    Attributes:
        repeated (bool):
            OPTIONAL
            Whether the property is repeated.
        allowed_values (MutableSequence[float]):
            OPTIONAL
            Allowed values for the property. If provided,
            the property value must be one of the allowed
            values.
    """

    repeated: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    allowed_values: MutableSequence[float] = proto.RepeatedField(
        proto.DOUBLE,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
