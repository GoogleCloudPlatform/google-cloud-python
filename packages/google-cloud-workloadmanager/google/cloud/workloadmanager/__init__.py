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
from google.cloud.workloadmanager import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.workloadmanager_v1.services.workload_manager.async_client import (
    WorkloadManagerAsyncClient,
)
from google.cloud.workloadmanager_v1.services.workload_manager.client import (
    WorkloadManagerClient,
)
from google.cloud.workloadmanager_v1.types.service import (
    AgentCommand,
    BigQueryDestination,
    Command,
    CreateEvaluationRequest,
    DeleteEvaluationRequest,
    DeleteExecutionRequest,
    Evaluation,
    Execution,
    ExecutionResult,
    GceInstanceFilter,
    GetEvaluationRequest,
    GetExecutionRequest,
    ListEvaluationsRequest,
    ListEvaluationsResponse,
    ListExecutionResultsRequest,
    ListExecutionResultsResponse,
    ListExecutionsRequest,
    ListExecutionsResponse,
    ListRulesRequest,
    ListRulesResponse,
    ListScannedResourcesRequest,
    ListScannedResourcesResponse,
    OperationMetadata,
    Resource,
    ResourceFilter,
    ResourceStatus,
    Rule,
    RuleExecutionResult,
    RuleOutput,
    RunEvaluationRequest,
    ScannedResource,
    ShellCommand,
    UpdateEvaluationRequest,
    ViolationDetails,
)

__all__ = (
    "WorkloadManagerClient",
    "WorkloadManagerAsyncClient",
    "AgentCommand",
    "BigQueryDestination",
    "Command",
    "CreateEvaluationRequest",
    "DeleteEvaluationRequest",
    "DeleteExecutionRequest",
    "Evaluation",
    "Execution",
    "ExecutionResult",
    "GceInstanceFilter",
    "GetEvaluationRequest",
    "GetExecutionRequest",
    "ListEvaluationsRequest",
    "ListEvaluationsResponse",
    "ListExecutionResultsRequest",
    "ListExecutionResultsResponse",
    "ListExecutionsRequest",
    "ListExecutionsResponse",
    "ListRulesRequest",
    "ListRulesResponse",
    "ListScannedResourcesRequest",
    "ListScannedResourcesResponse",
    "OperationMetadata",
    "Resource",
    "ResourceFilter",
    "ResourceStatus",
    "Rule",
    "RuleExecutionResult",
    "RuleOutput",
    "RunEvaluationRequest",
    "ScannedResource",
    "ShellCommand",
    "UpdateEvaluationRequest",
    "ViolationDetails",
)
