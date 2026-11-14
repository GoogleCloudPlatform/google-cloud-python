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

"""Thin Python SDK for Google Cloud Storage backed by a Rust gRPC-over-UDS sidecar."""

from google.cloud.storage_uds.client import (
    AsyncUdsStorageClient,
    ListObjectsResult,
    ObjectMetadata,
    PingInfo,
    UdsStorageClient,
)
from google.cloud.storage_uds.server_manager import (
    AcceleratorServerManager,
    AcceleratorStartupError,
    ProcessMetrics,
    read_process_metrics,
)

__version__ = "0.1.0"

__all__ = [
    "AcceleratorServerManager",
    "AcceleratorStartupError",
    "AsyncUdsStorageClient",
    "ListObjectsResult",
    "ObjectMetadata",
    "PingInfo",
    "ProcessMetrics",
    "UdsStorageClient",
    "__version__",
    "read_process_metrics",
]

