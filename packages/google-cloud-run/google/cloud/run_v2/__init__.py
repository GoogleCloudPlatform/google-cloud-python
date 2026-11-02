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

from google.cloud.run_v2 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.run_v2.services.builds",
    "google.cloud.run_v2.services.executions",
    "google.cloud.run_v2.services.instances",
    "google.cloud.run_v2.services.jobs",
    "google.cloud.run_v2.services.revisions",
    "google.cloud.run_v2.services.services",
    "google.cloud.run_v2.services.tasks",
    "google.cloud.run_v2.services.worker_pools",
    "google.cloud.run_v2.types.build",
    "google.cloud.run_v2.types.condition",
    "google.cloud.run_v2.types.container_status",
    "google.cloud.run_v2.types.execution",
    "google.cloud.run_v2.types.execution_template",
    "google.cloud.run_v2.types.instance",
    "google.cloud.run_v2.types.instance_split",
    "google.cloud.run_v2.types.job",
    "google.cloud.run_v2.types.k8s_min",
    "google.cloud.run_v2.types.revision",
    "google.cloud.run_v2.types.revision_template",
    "google.cloud.run_v2.types.service",
    "google.cloud.run_v2.types.status",
    "google.cloud.run_v2.types.task",
    "google.cloud.run_v2.types.task_template",
    "google.cloud.run_v2.types.traffic_target",
    "google.cloud.run_v2.types.vendor_settings",
    "google.cloud.run_v2.types.worker_pool",
    "google.cloud.run_v2.types.worker_pool_revision_template",
}


from .services.builds import BuildsAsyncClient, BuildsClient
from .services.executions import ExecutionsAsyncClient, ExecutionsClient
from .services.instances import InstancesAsyncClient, InstancesClient
from .services.jobs import JobsAsyncClient, JobsClient
from .services.revisions import RevisionsAsyncClient, RevisionsClient
from .services.services import ServicesAsyncClient, ServicesClient
from .services.tasks import TasksAsyncClient, TasksClient
from .services.worker_pools import WorkerPoolsAsyncClient, WorkerPoolsClient
from .types.build import StorageSource, SubmitBuildRequest, SubmitBuildResponse
from .types.condition import Condition
from .types.container_status import ContainerStatus
from .types.execution import (
    CancelExecutionRequest,
    DeleteExecutionRequest,
    Execution,
    GetExecutionRequest,
    ListExecutionsRequest,
    ListExecutionsResponse,
)
from .types.execution_template import ExecutionTemplate
from .types.instance import (
    CreateInstanceRequest,
    DeleteInstanceRequest,
    GetInstanceRequest,
    Instance,
    ListInstancesRequest,
    ListInstancesResponse,
    StartInstanceRequest,
    StopInstanceRequest,
)
from .types.instance_split import (
    InstanceSplit,
    InstanceSplitAllocationType,
    InstanceSplitStatus,
)
from .types.job import (
    CreateJobRequest,
    DeleteJobRequest,
    ExecutionReference,
    GetJobRequest,
    Job,
    ListJobsRequest,
    ListJobsResponse,
    RunJobRequest,
    UpdateJobRequest,
)
from .types.k8s_min import (
    BuildInfo,
    CloudSqlInstance,
    Container,
    ContainerPort,
    EmptyDirVolumeSource,
    EnvVar,
    EnvVarSource,
    GCSVolumeSource,
    GRPCAction,
    HTTPGetAction,
    HTTPHeader,
    NFSVolumeSource,
    Probe,
    ResourceRequirements,
    SecretKeySelector,
    SecretVolumeSource,
    SourceCode,
    TCPSocketAction,
    VersionToPath,
    Volume,
    VolumeMount,
)
from .types.revision import (
    DeleteRevisionRequest,
    GetRevisionRequest,
    ListRevisionsRequest,
    ListRevisionsResponse,
    Revision,
)
from .types.revision_template import RevisionTemplate
from .types.service import (
    CreateServiceRequest,
    DeleteServiceRequest,
    GetServiceRequest,
    ListServicesRequest,
    ListServicesResponse,
    Service,
    UpdateServiceRequest,
)
from .types.status import RevisionScalingStatus
from .types.task import (
    GetTaskRequest,
    ListTasksRequest,
    ListTasksResponse,
    Task,
    TaskAttemptResult,
)
from .types.task_template import TaskTemplate
from .types.traffic_target import (
    TrafficTarget,
    TrafficTargetAllocationType,
    TrafficTargetStatus,
)
from .types.vendor_settings import (
    BinaryAuthorization,
    BuildConfig,
    EncryptionKeyRevocationAction,
    ExecutionEnvironment,
    IngressTraffic,
    NodeSelector,
    RevisionScaling,
    ServiceMesh,
    ServiceScaling,
    VpcAccess,
    WorkerPoolScaling,
)
from .types.worker_pool import (
    CreateWorkerPoolRequest,
    DeleteWorkerPoolRequest,
    GetWorkerPoolRequest,
    ListWorkerPoolsRequest,
    ListWorkerPoolsResponse,
    UpdateWorkerPoolRequest,
    WorkerPool,
)
from .types.worker_pool_revision_template import WorkerPoolRevisionTemplate

__all__ = (
    "BuildsAsyncClient",
    "ExecutionsAsyncClient",
    "InstancesAsyncClient",
    "JobsAsyncClient",
    "RevisionsAsyncClient",
    "ServicesAsyncClient",
    "TasksAsyncClient",
    "WorkerPoolsAsyncClient",
    "BinaryAuthorization",
    "BuildConfig",
    "BuildInfo",
    "BuildsClient",
    "CancelExecutionRequest",
    "CloudSqlInstance",
    "Condition",
    "Container",
    "ContainerPort",
    "ContainerStatus",
    "CreateInstanceRequest",
    "CreateJobRequest",
    "CreateServiceRequest",
    "CreateWorkerPoolRequest",
    "DeleteExecutionRequest",
    "DeleteInstanceRequest",
    "DeleteJobRequest",
    "DeleteRevisionRequest",
    "DeleteServiceRequest",
    "DeleteWorkerPoolRequest",
    "EmptyDirVolumeSource",
    "EncryptionKeyRevocationAction",
    "EnvVar",
    "EnvVarSource",
    "Execution",
    "ExecutionEnvironment",
    "ExecutionReference",
    "ExecutionTemplate",
    "ExecutionsClient",
    "GCSVolumeSource",
    "GRPCAction",
    "GetExecutionRequest",
    "GetInstanceRequest",
    "GetJobRequest",
    "GetRevisionRequest",
    "GetServiceRequest",
    "GetTaskRequest",
    "GetWorkerPoolRequest",
    "HTTPGetAction",
    "HTTPHeader",
    "IngressTraffic",
    "Instance",
    "InstanceSplit",
    "InstanceSplitAllocationType",
    "InstanceSplitStatus",
    "InstancesClient",
    "Job",
    "JobsClient",
    "ListExecutionsRequest",
    "ListExecutionsResponse",
    "ListInstancesRequest",
    "ListInstancesResponse",
    "ListJobsRequest",
    "ListJobsResponse",
    "ListRevisionsRequest",
    "ListRevisionsResponse",
    "ListServicesRequest",
    "ListServicesResponse",
    "ListTasksRequest",
    "ListTasksResponse",
    "ListWorkerPoolsRequest",
    "ListWorkerPoolsResponse",
    "NFSVolumeSource",
    "NodeSelector",
    "Probe",
    "ResourceRequirements",
    "Revision",
    "RevisionScaling",
    "RevisionScalingStatus",
    "RevisionTemplate",
    "RevisionsClient",
    "RunJobRequest",
    "SecretKeySelector",
    "SecretVolumeSource",
    "Service",
    "ServiceMesh",
    "ServiceScaling",
    "ServicesClient",
    "SourceCode",
    "StartInstanceRequest",
    "StopInstanceRequest",
    "StorageSource",
    "SubmitBuildRequest",
    "SubmitBuildResponse",
    "TCPSocketAction",
    "Task",
    "TaskAttemptResult",
    "TaskTemplate",
    "TasksClient",
    "TrafficTarget",
    "TrafficTargetAllocationType",
    "TrafficTargetStatus",
    "UpdateJobRequest",
    "UpdateServiceRequest",
    "UpdateWorkerPoolRequest",
    "VersionToPath",
    "Volume",
    "VolumeMount",
    "VpcAccess",
    "WorkerPool",
    "WorkerPoolRevisionTemplate",
    "WorkerPoolScaling",
    "WorkerPoolsClient",
)

api_core.check_python_version("google.cloud.run_v2")
api_core.check_dependency_versions("google.cloud.run_v2")
