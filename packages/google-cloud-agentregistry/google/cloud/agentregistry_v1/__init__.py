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

from google.cloud.agentregistry_v1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.agentregistry_v1.services.agent_registry",
    "google.cloud.agentregistry_v1.types.agent",
    "google.cloud.agentregistry_v1.types.agentregistry_service",
    "google.cloud.agentregistry_v1.types.binding",
    "google.cloud.agentregistry_v1.types.endpoint",
    "google.cloud.agentregistry_v1.types.mcp_server",
    "google.cloud.agentregistry_v1.types.properties",
    "google.cloud.agentregistry_v1.types.service",
}


from .services.agent_registry import AgentRegistryAsyncClient, AgentRegistryClient
from .types.agent import Agent
from .types.agentregistry_service import (
    CreateBindingRequest,
    CreateServiceRequest,
    DeleteBindingRequest,
    DeleteServiceRequest,
    FetchAvailableBindingsRequest,
    FetchAvailableBindingsResponse,
    GetAgentRequest,
    GetBindingRequest,
    GetEndpointRequest,
    GetMcpServerRequest,
    GetServiceRequest,
    ListAgentsRequest,
    ListAgentsResponse,
    ListBindingsRequest,
    ListBindingsResponse,
    ListEndpointsRequest,
    ListEndpointsResponse,
    ListMcpServersRequest,
    ListMcpServersResponse,
    ListServicesRequest,
    ListServicesResponse,
    OperationMetadata,
    SearchAgentsRequest,
    SearchAgentsResponse,
    SearchMcpServersRequest,
    SearchMcpServersResponse,
    UpdateBindingRequest,
    UpdateServiceRequest,
)
from .types.binding import Binding
from .types.endpoint import Endpoint
from .types.mcp_server import McpServer
from .types.properties import Interface
from .types.service import Service

__all__ = (
    "AgentRegistryAsyncClient",
    "Agent",
    "AgentRegistryClient",
    "Binding",
    "CreateBindingRequest",
    "CreateServiceRequest",
    "DeleteBindingRequest",
    "DeleteServiceRequest",
    "Endpoint",
    "FetchAvailableBindingsRequest",
    "FetchAvailableBindingsResponse",
    "GetAgentRequest",
    "GetBindingRequest",
    "GetEndpointRequest",
    "GetMcpServerRequest",
    "GetServiceRequest",
    "Interface",
    "ListAgentsRequest",
    "ListAgentsResponse",
    "ListBindingsRequest",
    "ListBindingsResponse",
    "ListEndpointsRequest",
    "ListEndpointsResponse",
    "ListMcpServersRequest",
    "ListMcpServersResponse",
    "ListServicesRequest",
    "ListServicesResponse",
    "McpServer",
    "OperationMetadata",
    "SearchAgentsRequest",
    "SearchAgentsResponse",
    "SearchMcpServersRequest",
    "SearchMcpServersResponse",
    "Service",
    "UpdateBindingRequest",
    "UpdateServiceRequest",
)

api_core.check_python_version("google.cloud.agentregistry_v1")
api_core.check_dependency_versions("google.cloud.agentregistry_v1")
