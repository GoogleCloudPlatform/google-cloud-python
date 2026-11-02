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
from google.cloud.apptopology import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.apptopology_v1.services.app_topology.async_client import (
    AppTopologyAsyncClient,
)
from google.cloud.apptopology_v1.services.app_topology.client import AppTopologyClient
from google.cloud.apptopology_v1.types.graph import Edge, EntityContext, Graph, Node
from google.cloud.apptopology_v1.types.query import (
    ConnectedNodePattern,
    EdgePattern,
    GraphPattern,
    LabelPropertiesPattern,
    NodePattern,
)
from google.cloud.apptopology_v1.types.schema import (
    BoolValue,
    Domain,
    DoubleValue,
    EdgeRule,
    EdgeType,
    IntValue,
    LabelProperties,
    NodeGroup,
    NodeType,
    Property,
    Schema,
    StringValue,
)
from google.cloud.apptopology_v1.types.service import (
    ExploreSchemaRequest,
    ExploreSchemaResponse,
    GenerateDiscoveredResourcesTopologyRequest,
    GenerateDiscoveredResourcesTopologyResponse,
    GetDomainRequest,
    GetSchemaRequest,
    ListDomainsRequest,
    ListDomainsResponse,
    OperationMetadata,
)

__all__ = (
    "AppTopologyClient",
    "AppTopologyAsyncClient",
    "Edge",
    "EntityContext",
    "Graph",
    "Node",
    "ConnectedNodePattern",
    "EdgePattern",
    "GraphPattern",
    "LabelPropertiesPattern",
    "NodePattern",
    "BoolValue",
    "Domain",
    "DoubleValue",
    "EdgeRule",
    "EdgeType",
    "IntValue",
    "LabelProperties",
    "NodeGroup",
    "NodeType",
    "Property",
    "Schema",
    "StringValue",
    "ExploreSchemaRequest",
    "ExploreSchemaResponse",
    "GenerateDiscoveredResourcesTopologyRequest",
    "GenerateDiscoveredResourcesTopologyResponse",
    "GetDomainRequest",
    "GetSchemaRequest",
    "ListDomainsRequest",
    "ListDomainsResponse",
    "OperationMetadata",
)
