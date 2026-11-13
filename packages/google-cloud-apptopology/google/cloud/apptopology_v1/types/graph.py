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

import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.apptopology.v1",
    manifest={
        "Graph",
        "EntityContext",
        "Node",
        "Edge",
    },
)


class Graph(proto.Message):
    r"""Represents a graph structure composed of nodes and edges.

    Attributes:
        nodes (MutableSequence[google.cloud.apptopology_v1.types.Node]):
            A collection of unique nodes that make up the
            graph.
        edges (MutableSequence[google.cloud.apptopology_v1.types.Edge]):
            Collection of unique edges connecting the ``nodes`` in the
            graph. Both source and destination nodes for each edges will
            be present in the ``nodes`` list.
    """

    nodes: MutableSequence["Node"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Node",
    )
    edges: MutableSequence["Edge"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="Edge",
    )


class EntityContext(proto.Message):
    r"""Represents the context of an entity (node or edge) in the
    graph.

    Attributes:
        type_ (str):
            The primary, namespaced type dictating the node naming
            format and supported labels, and defined in the ``Schema``
            (Schema.node_types/edge_types.name), e.g.,
            ``Base/compute.googleapis.com/Instance``.
    """

    type_: str = proto.Field(
        proto.STRING,
        number=1,
    )


class Node(proto.Message):
    r"""Represents a single node in the graph.

    Attributes:
        properties (google.protobuf.struct_pb2.Struct):
            Properties associated with the node.
            Refer to
            https://apptopology.googleapis.com/v1/GetSchema
            for a detailed list of node properties.
        name (str):
            The global unique name of the node.
            For standard Google Cloud Platform resources,
            this MUST be the canonical Full Resource Name.

            Examples:

            - type: compute.googleapis.com/Instance
              name:

            "//compute.googleapis.com/projects/my-project-id/zones/us-central1-a/instances/my-vm-1"

            - type: container.googleapis.com/Cluster
              name:

            "//container.googleapis.com/projects/my-project-id/locations/us-central1/clusters/my-cluster".
        labels (MutableSequence[str]):
            Labels attached to the node. Composable,
            namespaced building blocks that define core
            attributes through associated properties.
            Multiple labels aggregate to fully specify the
            functional traits and property schema of the
            node type.
        context (google.cloud.apptopology_v1.types.EntityContext):
            The context of the node.
    """

    properties: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=3,
        message=struct_pb2.Struct,
    )
    name: str = proto.Field(
        proto.STRING,
        number=4,
    )
    labels: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    context: "EntityContext" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="EntityContext",
    )


class Edge(proto.Message):
    r"""Represents a single edge connecting two nodes in the graph.

    Attributes:
        properties (google.protobuf.struct_pb2.Struct):
            Properties associated with the edge.
            Refer to
            https://apptopology.googleapis.com/v1/GetSchema
            for a detailed list of edge properties.
        source_node_name (str):
            The name of the source node for this edge. This is the
            ``name`` field in the Node.
        destination_node_name (str):
            The name of the destination node for this edge. This is the
            ``name`` field in the Node.
        labels (MutableSequence[str]):
            Labels attached to the edge. Composable,
            namespaced building blocks that define core
            attributes through associated properties.
            Multiple labels aggregate to fully specify the
            functional traits and property schema of the
            edge type.
        context (google.cloud.apptopology_v1.types.EntityContext):
            The context of the edge.
    """

    properties: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=5,
        message=struct_pb2.Struct,
    )
    source_node_name: str = proto.Field(
        proto.STRING,
        number=6,
    )
    destination_node_name: str = proto.Field(
        proto.STRING,
        number=7,
    )
    labels: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=8,
    )
    context: "EntityContext" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="EntityContext",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
