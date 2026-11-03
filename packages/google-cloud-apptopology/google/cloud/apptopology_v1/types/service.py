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

from google.cloud.apptopology_v1.types import graph as gca_graph
from google.cloud.apptopology_v1.types import query, schema

__protobuf__ = proto.module(
    package="google.cloud.apptopology.v1",
    manifest={
        "OperationMetadata",
        "GenerateDiscoveredResourcesTopologyRequest",
        "GenerateDiscoveredResourcesTopologyResponse",
        "GetSchemaRequest",
        "ExploreSchemaRequest",
        "ExploreSchemaResponse",
        "GetDomainRequest",
        "ListDomainsRequest",
        "ListDomainsResponse",
    },
)


class OperationMetadata(proto.Message):
    r"""Represents the metadata of the long-running operation.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation was
            created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation finished
            running.
        target (str):
            Output only. Server-defined resource path for
            the target of the operation.
        verb (str):
            Output only. Name of the verb executed by the
            operation.
        status_message (str):
            Output only. Human-readable status of the
            operation, if any.
        requested_cancellation (bool):
            Output only. Identifies whether the user has requested
            cancellation of the operation. Operations that have been
            cancelled successfully have
            [google.longrunning.Operation.error][google.longrunning.Operation.error]
            value with a
            [google.rpc.Status.code][google.rpc.Status.code] of ``1``,
            corresponding to ``Code.CANCELLED``.
        api_version (str):
            Output only. API version used to start the
            operation.
    """

    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    target: str = proto.Field(
        proto.STRING,
        number=3,
    )
    verb: str = proto.Field(
        proto.STRING,
        number=4,
    )
    status_message: str = proto.Field(
        proto.STRING,
        number=5,
    )
    requested_cancellation: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    api_version: str = proto.Field(
        proto.STRING,
        number=7,
    )


class GenerateDiscoveredResourcesTopologyRequest(proto.Message):
    r"""Request for GenerateDiscoveredResourcesTopology.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        filter (google.cloud.apptopology_v1.types.GraphPattern):
            Filters for the topology nodes and edges;
            Detail format see GraphPattern proto. A separate
            'LookupSchema' method will be added that will
            return the necessary information to be able to
            construct these filters.

            This field is a member of `oneof`_ ``query``.
        name (str):
            Required. The project to query discoverable resources on.
            Expected format:
            ``projects/{project}/locations/{location}/discoveredResourcesTopology``.
            Only ``global`` location is supported.
        topology_domains (MutableSequence[str]):
            Required. The full resource name of the domain of the app
            topology. Format:
            ``projects/{project}/locations/{location}/domains/{domain}``
            Caller must have apptopology.domains.get permission on each
            of the domains.
    """

    filter: query.GraphPattern = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="query",
        message=query.GraphPattern,
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    topology_domains: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class GenerateDiscoveredResourcesTopologyResponse(proto.Message):
    r"""Response for GenerateDiscoveredResourcesTopology.

    Attributes:
        graph (google.cloud.apptopology_v1.types.Graph):
            The generated topology graph.
    """

    graph: gca_graph.Graph = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gca_graph.Graph,
    )


class GetSchemaRequest(proto.Message):
    r"""Request for GetSchema.

    Attributes:
        name (str):
            Required. The name of the singleton domain schema resource.
            Format:
            ``projects/{project}/locations/{location}/domains/{domain}/schema``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ExploreSchemaRequest(proto.Message):
    r"""Request for ExploreSchema.

    Attributes:
        name (str):
            Required. The name of the singleton domain schema resource.
            Format:
            ``projects/{project}/locations/{location}/domains/{domain}/schema``
        start_labels (MutableSequence[str]):
            Optional. Starting label names to begin traversal.
            Substring, case-insensitive matches are performed against
            allowed label names in the schema. A maximum of 10
            ``start_labels`` can be specified; providing more will
            result in an ``INVALID_ARGUMENT`` error. If ``start_labels``
            is unset or empty, all authorized node types will be used as
            the starting set.
        depth (int):
            Optional. The maximum depth of BFS traversal
            hops to perform from the starting node types or
            label names. Defaults to 0 if unspecified.
        page_size (int):
            Optional. The maximum number of schema elements to return in
            a single page.

            - The service might return fewer elements than this value if
              adding another edge and its required endpoint nodes
              exceeds ``page_size``.
            - If omitted or set to 0, default (100) will be used.
            - Minimum page_size is 3 to ensure at least one edge and its
              endpoint nodes fit on a page; values below 3 (e.g. 1 or 2)
              are changed to 3.
            - Maximum value is 500.
        page_token (str):
            Optional. A page token received from a previous
            ``ExploreSchema`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters (except page_size)
            provided to ``ExploreSchema`` must match the call that
            provided the page token.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    start_labels: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    depth: int = proto.Field(
        proto.INT32,
        number=4,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=5,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=6,
    )


class ExploreSchemaResponse(proto.Message):
    r"""Response for ExploreSchema.

    Attributes:
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
        next_page_token (str):
            A token to retrieve the next page of results,
            or empty if there are no more results in the
            traversal set.
    """

    @property
    def raw_page(self):
        return self

    node_types: MutableSequence[schema.NodeType] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=schema.NodeType,
    )
    edge_types: MutableSequence[schema.EdgeType] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=schema.EdgeType,
    )
    label_properties: MutableSequence[schema.LabelProperties] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=schema.LabelProperties,
    )
    edge_rules: MutableSequence[schema.EdgeRule] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=schema.EdgeRule,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=5,
    )


class GetDomainRequest(proto.Message):
    r"""Request for GetDomain.

    Attributes:
        name (str):
            Required. The name of the domain to retrieve. Format:
            ``projects/{project}/locations/{location}/domains/{domain}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListDomainsRequest(proto.Message):
    r"""Request for ListDomains.

    Attributes:
        parent (str):
            Required. The parent location to list domains for. Format:
            ``projects/{project}/locations/{location}`` Only ``global``
            location is supported.
        page_size (int):
            Optional. The maximum number of domains to
            return. The service may return fewer than this
            value. If unspecified, at most 50 domains will
            be returned. The maximum value is 1000; values
            above 1000 will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListDomains`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListDomains`` must match the call that provided the page
            token.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListDomainsResponse(proto.Message):
    r"""Response for ListDomains.

    Attributes:
        domains (MutableSequence[google.cloud.apptopology_v1.types.Domain]):
            The domains in the specified location.
        next_page_token (str):
            A token that can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    domains: MutableSequence[schema.Domain] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=schema.Domain,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
