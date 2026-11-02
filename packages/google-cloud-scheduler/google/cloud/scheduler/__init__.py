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
from google.cloud.scheduler import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.scheduler_v1.services.cloud_scheduler.async_client import (
    CloudSchedulerAsyncClient,
)
from google.cloud.scheduler_v1.services.cloud_scheduler.client import (
    CloudSchedulerClient,
)
from google.cloud.scheduler_v1.types.cloudscheduler import (
    CreateJobRequest,
    DeleteJobRequest,
    GetJobRequest,
    ListJobsRequest,
    ListJobsResponse,
    PauseJobRequest,
    ResumeJobRequest,
    RunJobRequest,
    UpdateJobRequest,
)
from google.cloud.scheduler_v1.types.job import Job, RetryConfig
from google.cloud.scheduler_v1.types.target import (
    AppEngineHttpTarget,
    AppEngineRouting,
    HttpMethod,
    HttpTarget,
    OAuthToken,
    OidcToken,
    PubsubTarget,
)

__all__ = (
    "CloudSchedulerClient",
    "CloudSchedulerAsyncClient",
    "CreateJobRequest",
    "DeleteJobRequest",
    "GetJobRequest",
    "ListJobsRequest",
    "ListJobsResponse",
    "PauseJobRequest",
    "ResumeJobRequest",
    "RunJobRequest",
    "UpdateJobRequest",
    "Job",
    "RetryConfig",
    "AppEngineHttpTarget",
    "AppEngineRouting",
    "HttpTarget",
    "OAuthToken",
    "OidcToken",
    "PubsubTarget",
    "HttpMethod",
)
