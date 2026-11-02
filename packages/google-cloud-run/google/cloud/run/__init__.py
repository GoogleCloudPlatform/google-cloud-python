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
from google.cloud.run import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.run_v2.services.builds.async_client import BuildsAsyncClient
from google.cloud.run_v2.services.builds.client import BuildsClient
from google.cloud.run_v2.services.executions.async_client import ExecutionsAsyncClient
from google.cloud.run_v2.services.executions.client import ExecutionsClient
from google.cloud.run_v2.services.instances.async_client import InstancesAsyncClient
from google.cloud.run_v2.services.instances.client import InstancesClient
from google.cloud.run_v2.services.jobs.async_client import JobsAsyncClient
from google.cloud.run_v2.services.jobs.client import JobsClient
from google.cloud.run_v2.services.revisions.async_client import RevisionsAsyncClient
from google.cloud.run_v2.services.revisions.client import RevisionsClient
from google.cloud.run_v2.services.services.async_client import ServicesAsyncClient
from google.cloud.run_v2.services.services.client import ServicesClient
from google.cloud.run_v2.services.tasks.async_client import TasksAsyncClient
from google.cloud.run_v2.services.tasks.client import TasksClient
from google.cloud.run_v2.services.worker_pools.async_client import (
    WorkerPoolsAsyncClient,
)
from google.cloud.run_v2.services.worker_pools.client import WorkerPoolsClient
from google.cloud.run_v2.types.build import (
    StorageSource,
    SubmitBuildRequest,
    SubmitBuildResponse,
)
from google.cloud.run_v2.types.condition import Condition
from google.cloud.run_v2.types.container_status import ContainerStatus
from google.cloud.run_v2.types.execution import (
    CancelExecutionRequest,
    DeleteExecutionRequest,
    Execution,
    GetExecutionRequest,
    ListExecutionsRequest,
    ListExecutionsResponse,
)
from google.cloud.run_v2.types.execution_template import ExecutionTemplate
from google.cloud.run_v2.types.instance import (
    CreateInstanceRequest,
    DeleteInstanceRequest,
    GetInstanceRequest,
    Instance,
    ListInstancesRequest,
    ListInstancesResponse,
    StartInstanceRequest,
    StopInstanceRequest,
)
from google.cloud.run_v2.types.instance_split import (
    InstanceSplit,
    InstanceSplitAllocationType,
    InstanceSplitStatus,
)
from google.cloud.run_v2.types.job import (
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
from google.cloud.run_v2.types.k8s_min import (
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
from google.cloud.run_v2.types.revision import (
    DeleteRevisionRequest,
    GetRevisionRequest,
    ListRevisionsRequest,
    ListRevisionsResponse,
    Revision,
)
from google.cloud.run_v2.types.revision_template import RevisionTemplate
from google.cloud.run_v2.types.service import (
    CreateServiceRequest,
    DeleteServiceRequest,
    GetServiceRequest,
    ListServicesRequest,
    ListServicesResponse,
    Service,
    UpdateServiceRequest,
)
from google.cloud.run_v2.types.status import RevisionScalingStatus
from google.cloud.run_v2.types.task import (
    GetTaskRequest,
    ListTasksRequest,
    ListTasksResponse,
    Task,
    TaskAttemptResult,
)
from google.cloud.run_v2.types.task_template import TaskTemplate
from google.cloud.run_v2.types.traffic_target import (
    TrafficTarget,
    TrafficTargetAllocationType,
    TrafficTargetStatus,
)
from google.cloud.run_v2.types.vendor_settings import (
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
from google.cloud.run_v2.types.worker_pool import (
    CreateWorkerPoolRequest,
    DeleteWorkerPoolRequest,
    GetWorkerPoolRequest,
    ListWorkerPoolsRequest,
    ListWorkerPoolsResponse,
    UpdateWorkerPoolRequest,
    WorkerPool,
)
from google.cloud.run_v2.types.worker_pool_revision_template import (
    WorkerPoolRevisionTemplate,
)

__all__ = (
    "BuildsClient",
    "BuildsAsyncClient",
    "ExecutionsClient",
    "ExecutionsAsyncClient",
    "InstancesClient",
    "InstancesAsyncClient",
    "JobsClient",
    "JobsAsyncClient",
    "RevisionsClient",
    "RevisionsAsyncClient",
    "ServicesClient",
    "ServicesAsyncClient",
    "TasksClient",
    "TasksAsyncClient",
    "WorkerPoolsClient",
    "WorkerPoolsAsyncClient",
    "StorageSource",
    "SubmitBuildRequest",
    "SubmitBuildResponse",
    "Condition",
    "ContainerStatus",
    "CancelExecutionRequest",
    "DeleteExecutionRequest",
    "Execution",
    "GetExecutionRequest",
    "ListExecutionsRequest",
    "ListExecutionsResponse",
    "ExecutionTemplate",
    "CreateInstanceRequest",
    "DeleteInstanceRequest",
    "GetInstanceRequest",
    "Instance",
    "ListInstancesRequest",
    "ListInstancesResponse",
    "StartInstanceRequest",
    "StopInstanceRequest",
    "InstanceSplit",
    "InstanceSplitStatus",
    "InstanceSplitAllocationType",
    "CreateJobRequest",
    "DeleteJobRequest",
    "ExecutionReference",
    "GetJobRequest",
    "Job",
    "ListJobsRequest",
    "ListJobsResponse",
    "RunJobRequest",
    "UpdateJobRequest",
    "BuildInfo",
    "CloudSqlInstance",
    "Container",
    "ContainerPort",
    "EmptyDirVolumeSource",
    "EnvVar",
    "EnvVarSource",
    "GCSVolumeSource",
    "GRPCAction",
    "HTTPGetAction",
    "HTTPHeader",
    "NFSVolumeSource",
    "Probe",
    "ResourceRequirements",
    "SecretKeySelector",
    "SecretVolumeSource",
    "SourceCode",
    "TCPSocketAction",
    "VersionToPath",
    "Volume",
    "VolumeMount",
    "DeleteRevisionRequest",
    "GetRevisionRequest",
    "ListRevisionsRequest",
    "ListRevisionsResponse",
    "Revision",
    "RevisionTemplate",
    "CreateServiceRequest",
    "DeleteServiceRequest",
    "GetServiceRequest",
    "ListServicesRequest",
    "ListServicesResponse",
    "Service",
    "UpdateServiceRequest",
    "RevisionScalingStatus",
    "GetTaskRequest",
    "ListTasksRequest",
    "ListTasksResponse",
    "Task",
    "TaskAttemptResult",
    "TaskTemplate",
    "TrafficTarget",
    "TrafficTargetStatus",
    "TrafficTargetAllocationType",
    "BinaryAuthorization",
    "BuildConfig",
    "NodeSelector",
    "RevisionScaling",
    "ServiceMesh",
    "ServiceScaling",
    "VpcAccess",
    "WorkerPoolScaling",
    "EncryptionKeyRevocationAction",
    "ExecutionEnvironment",
    "IngressTraffic",
    "CreateWorkerPoolRequest",
    "DeleteWorkerPoolRequest",
    "GetWorkerPoolRequest",
    "ListWorkerPoolsRequest",
    "ListWorkerPoolsResponse",
    "UpdateWorkerPoolRequest",
    "WorkerPool",
    "WorkerPoolRevisionTemplate",
)
