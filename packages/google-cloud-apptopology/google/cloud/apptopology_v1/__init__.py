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
import google.api_core as api_core

from google.cloud.apptopology_v1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.apptopology_v1.services.app_topology",
    "google.cloud.apptopology_v1.types.graph",
    "google.cloud.apptopology_v1.types.query",
    "google.cloud.apptopology_v1.types.schema",
    "google.cloud.apptopology_v1.types.service",
}


from .services.app_topology import AppTopologyAsyncClient, AppTopologyClient
from .types.graph import Edge, EntityContext, Graph, Node
from .types.query import (
    ConnectedNodePattern,
    EdgePattern,
    GraphPattern,
    LabelPropertiesPattern,
    NodePattern,
)
from .types.schema import (
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
from .types.service import (
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
    "AppTopologyAsyncClient",
    "AppTopologyClient",
    "BoolValue",
    "ConnectedNodePattern",
    "Domain",
    "DoubleValue",
    "Edge",
    "EdgePattern",
    "EdgeRule",
    "EdgeType",
    "EntityContext",
    "ExploreSchemaRequest",
    "ExploreSchemaResponse",
    "GenerateDiscoveredResourcesTopologyRequest",
    "GenerateDiscoveredResourcesTopologyResponse",
    "GetDomainRequest",
    "GetSchemaRequest",
    "Graph",
    "GraphPattern",
    "IntValue",
    "LabelProperties",
    "LabelPropertiesPattern",
    "ListDomainsRequest",
    "ListDomainsResponse",
    "Node",
    "NodeGroup",
    "NodePattern",
    "NodeType",
    "OperationMetadata",
    "Property",
    "Schema",
    "StringValue",
)

api_core.check_python_version("google.cloud.apptopology_v1")
api_core.check_dependency_versions("google.cloud.apptopology_v1")
