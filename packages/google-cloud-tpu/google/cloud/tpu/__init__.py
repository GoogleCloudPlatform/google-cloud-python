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
from google.cloud.tpu import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.tpu_v1.services.tpu.async_client import TpuAsyncClient
from google.cloud.tpu_v1.services.tpu.client import TpuClient
from google.cloud.tpu_v1.types.cloud_tpu import (
    AcceleratorType,
    CreateNodeRequest,
    DeleteNodeRequest,
    GetAcceleratorTypeRequest,
    GetNodeRequest,
    GetTensorFlowVersionRequest,
    ListAcceleratorTypesRequest,
    ListAcceleratorTypesResponse,
    ListNodesRequest,
    ListNodesResponse,
    ListTensorFlowVersionsRequest,
    ListTensorFlowVersionsResponse,
    NetworkEndpoint,
    Node,
    OperationMetadata,
    ReimageNodeRequest,
    SchedulingConfig,
    StartNodeRequest,
    StopNodeRequest,
    Symptom,
    TensorFlowVersion,
)

__all__ = (
    "TpuClient",
    "TpuAsyncClient",
    "AcceleratorType",
    "CreateNodeRequest",
    "DeleteNodeRequest",
    "GetAcceleratorTypeRequest",
    "GetNodeRequest",
    "GetTensorFlowVersionRequest",
    "ListAcceleratorTypesRequest",
    "ListAcceleratorTypesResponse",
    "ListNodesRequest",
    "ListNodesResponse",
    "ListTensorFlowVersionsRequest",
    "ListTensorFlowVersionsResponse",
    "NetworkEndpoint",
    "Node",
    "OperationMetadata",
    "ReimageNodeRequest",
    "SchedulingConfig",
    "StartNodeRequest",
    "StopNodeRequest",
    "Symptom",
    "TensorFlowVersion",
)
