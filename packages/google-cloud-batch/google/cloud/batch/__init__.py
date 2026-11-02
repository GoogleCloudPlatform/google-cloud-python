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
from google.cloud.batch import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.batch_v1.services.batch_service.async_client import (
    BatchServiceAsyncClient,
)
from google.cloud.batch_v1.services.batch_service.client import BatchServiceClient
from google.cloud.batch_v1.types.batch import (
    CancelJobRequest,
    CancelJobResponse,
    CreateJobRequest,
    DeleteJobRequest,
    GetJobRequest,
    GetTaskRequest,
    ListJobsRequest,
    ListJobsResponse,
    ListTasksRequest,
    ListTasksResponse,
    OperationMetadata,
)
from google.cloud.batch_v1.types.job import (
    AllocationPolicy,
    Job,
    JobNotification,
    JobStatus,
    LogsPolicy,
    ServiceAccount,
    TaskGroup,
)
from google.cloud.batch_v1.types.task import (
    ComputeResource,
    Environment,
    LifecyclePolicy,
    Runnable,
    StatusEvent,
    Task,
    TaskExecution,
    TaskSpec,
    TaskStatus,
)
from google.cloud.batch_v1.types.volume import GCS, NFS, Volume

__all__ = (
    "BatchServiceClient",
    "BatchServiceAsyncClient",
    "CancelJobRequest",
    "CancelJobResponse",
    "CreateJobRequest",
    "DeleteJobRequest",
    "GetJobRequest",
    "GetTaskRequest",
    "ListJobsRequest",
    "ListJobsResponse",
    "ListTasksRequest",
    "ListTasksResponse",
    "OperationMetadata",
    "AllocationPolicy",
    "Job",
    "JobNotification",
    "JobStatus",
    "LogsPolicy",
    "ServiceAccount",
    "TaskGroup",
    "ComputeResource",
    "Environment",
    "LifecyclePolicy",
    "Runnable",
    "StatusEvent",
    "Task",
    "TaskExecution",
    "TaskSpec",
    "TaskStatus",
    "GCS",
    "NFS",
    "Volume",
)
