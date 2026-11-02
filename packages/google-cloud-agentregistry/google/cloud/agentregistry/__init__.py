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
from google.cloud.agentregistry import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.agentregistry_v1.services.agent_registry.async_client import (
    AgentRegistryAsyncClient,
)
from google.cloud.agentregistry_v1.services.agent_registry.client import (
    AgentRegistryClient,
)
from google.cloud.agentregistry_v1.types.agent import Agent
from google.cloud.agentregistry_v1.types.agentregistry_service import (
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
from google.cloud.agentregistry_v1.types.binding import Binding
from google.cloud.agentregistry_v1.types.endpoint import Endpoint
from google.cloud.agentregistry_v1.types.mcp_server import McpServer
from google.cloud.agentregistry_v1.types.properties import Interface
from google.cloud.agentregistry_v1.types.service import Service

__all__ = (
    "AgentRegistryClient",
    "AgentRegistryAsyncClient",
    "Agent",
    "CreateBindingRequest",
    "CreateServiceRequest",
    "DeleteBindingRequest",
    "DeleteServiceRequest",
    "FetchAvailableBindingsRequest",
    "FetchAvailableBindingsResponse",
    "GetAgentRequest",
    "GetBindingRequest",
    "GetEndpointRequest",
    "GetMcpServerRequest",
    "GetServiceRequest",
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
    "OperationMetadata",
    "SearchAgentsRequest",
    "SearchAgentsResponse",
    "SearchMcpServersRequest",
    "SearchMcpServersResponse",
    "UpdateBindingRequest",
    "UpdateServiceRequest",
    "Binding",
    "Endpoint",
    "McpServer",
    "Interface",
    "Service",
)
