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

from google.cloud.batch_v1alpha import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.batch_v1alpha.services.batch_service",
    "google.cloud.batch_v1alpha.types.batch",
    "google.cloud.batch_v1alpha.types.job",
    "google.cloud.batch_v1alpha.types.notification",
    "google.cloud.batch_v1alpha.types.resource_allowance",
    "google.cloud.batch_v1alpha.types.task",
    "google.cloud.batch_v1alpha.types.volume",
}


from .services.batch_service import BatchServiceAsyncClient, BatchServiceClient
from .types.batch import (
    CancelJobRequest,
    CancelJobResponse,
    CreateJobRequest,
    CreateResourceAllowanceRequest,
    DeleteJobRequest,
    DeleteResourceAllowanceRequest,
    GetJobRequest,
    GetResourceAllowanceRequest,
    GetTaskRequest,
    ListJobsRequest,
    ListJobsResponse,
    ListResourceAllowancesRequest,
    ListResourceAllowancesResponse,
    ListTasksRequest,
    ListTasksResponse,
    OperationMetadata,
    UpdateJobRequest,
    UpdateResourceAllowanceRequest,
)
from .types.job import (
    AllocationPolicy,
    Job,
    JobDependency,
    JobNotification,
    JobStatus,
    LogsPolicy,
    ResourceUsage,
    ServiceAccount,
    TaskGroup,
)
from .types.notification import Notification
from .types.resource_allowance import (
    CalendarPeriod,
    ResourceAllowance,
    ResourceAllowanceState,
    UsageResourceAllowance,
    UsageResourceAllowanceSpec,
    UsageResourceAllowanceStatus,
)
from .types.task import (
    ComputeResource,
    Environment,
    LifecyclePolicy,
    Runnable,
    StatusEvent,
    Task,
    TaskExecution,
    TaskResourceUsage,
    TaskSpec,
    TaskStatus,
)
from .types.volume import GCS, NFS, PD, Volume

__all__ = (
    "BatchServiceAsyncClient",
    "AllocationPolicy",
    "BatchServiceClient",
    "CalendarPeriod",
    "CancelJobRequest",
    "CancelJobResponse",
    "ComputeResource",
    "CreateJobRequest",
    "CreateResourceAllowanceRequest",
    "DeleteJobRequest",
    "DeleteResourceAllowanceRequest",
    "Environment",
    "GCS",
    "GetJobRequest",
    "GetResourceAllowanceRequest",
    "GetTaskRequest",
    "Job",
    "JobDependency",
    "JobNotification",
    "JobStatus",
    "LifecyclePolicy",
    "ListJobsRequest",
    "ListJobsResponse",
    "ListResourceAllowancesRequest",
    "ListResourceAllowancesResponse",
    "ListTasksRequest",
    "ListTasksResponse",
    "LogsPolicy",
    "NFS",
    "Notification",
    "OperationMetadata",
    "PD",
    "ResourceAllowance",
    "ResourceAllowanceState",
    "ResourceUsage",
    "Runnable",
    "ServiceAccount",
    "StatusEvent",
    "Task",
    "TaskExecution",
    "TaskGroup",
    "TaskResourceUsage",
    "TaskSpec",
    "TaskStatus",
    "UpdateJobRequest",
    "UpdateResourceAllowanceRequest",
    "UsageResourceAllowance",
    "UsageResourceAllowanceSpec",
    "UsageResourceAllowanceStatus",
    "Volume",
)

api_core.check_python_version("google.cloud.batch_v1alpha")
api_core.check_dependency_versions("google.cloud.batch_v1alpha")
