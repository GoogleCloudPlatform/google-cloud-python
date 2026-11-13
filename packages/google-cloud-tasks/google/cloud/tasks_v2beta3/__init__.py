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

from google.cloud.tasks_v2beta3 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.tasks_v2beta3.services.cloud_tasks",
    "google.cloud.tasks_v2beta3.types.cloudtasks",
    "google.cloud.tasks_v2beta3.types.cmek_config",
    "google.cloud.tasks_v2beta3.types.queue",
    "google.cloud.tasks_v2beta3.types.target",
    "google.cloud.tasks_v2beta3.types.task",
}


from .services.cloud_tasks import CloudTasksAsyncClient, CloudTasksClient
from .types.cloudtasks import (
    BatchCreateTasksMetadata,
    BatchCreateTasksRequest,
    BatchCreateTasksResponse,
    BatchDeleteTasksMetadata,
    BatchDeleteTasksRequest,
    CreateQueueRequest,
    CreateTaskRequest,
    DeleteQueueRequest,
    DeleteTaskRequest,
    GetCmekConfigRequest,
    GetQueueRequest,
    GetTaskRequest,
    ListQueuesRequest,
    ListQueuesResponse,
    ListTasksRequest,
    ListTasksResponse,
    PauseQueueRequest,
    PurgeQueueRequest,
    ResumeQueueRequest,
    RunTaskRequest,
    UpdateCmekConfigRequest,
    UpdateQueueRequest,
)
from .types.cmek_config import CmekConfig
from .types.queue import (
    Queue,
    QueueStats,
    RateLimits,
    RetryConfig,
    StackdriverLoggingConfig,
)
from .types.target import (
    AppEngineHttpQueue,
    AppEngineHttpRequest,
    AppEngineRouting,
    HttpMethod,
    HttpRequest,
    HttpTarget,
    OAuthToken,
    OidcToken,
    PathOverride,
    PullMessage,
    QueryOverride,
    UriOverride,
)
from .types.task import Attempt, Task

__all__ = (
    "CloudTasksAsyncClient",
    "AppEngineHttpQueue",
    "AppEngineHttpRequest",
    "AppEngineRouting",
    "Attempt",
    "BatchCreateTasksMetadata",
    "BatchCreateTasksRequest",
    "BatchCreateTasksResponse",
    "BatchDeleteTasksMetadata",
    "BatchDeleteTasksRequest",
    "CloudTasksClient",
    "CmekConfig",
    "CreateQueueRequest",
    "CreateTaskRequest",
    "DeleteQueueRequest",
    "DeleteTaskRequest",
    "GetCmekConfigRequest",
    "GetQueueRequest",
    "GetTaskRequest",
    "HttpMethod",
    "HttpRequest",
    "HttpTarget",
    "ListQueuesRequest",
    "ListQueuesResponse",
    "ListTasksRequest",
    "ListTasksResponse",
    "OAuthToken",
    "OidcToken",
    "PathOverride",
    "PauseQueueRequest",
    "PullMessage",
    "PurgeQueueRequest",
    "QueryOverride",
    "Queue",
    "QueueStats",
    "RateLimits",
    "ResumeQueueRequest",
    "RetryConfig",
    "RunTaskRequest",
    "StackdriverLoggingConfig",
    "Task",
    "UpdateCmekConfigRequest",
    "UpdateQueueRequest",
    "UriOverride",
)

api_core.check_python_version("google.cloud.tasks_v2beta3")
api_core.check_dependency_versions("google.cloud.tasks_v2beta3")
