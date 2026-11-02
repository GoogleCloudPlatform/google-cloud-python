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
from google.cloud.datacatalog_lineage import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.datacatalog_lineage_v1.services.lineage.async_client import (
    LineageAsyncClient,
)
from google.cloud.datacatalog_lineage_v1.services.lineage.client import LineageClient
from google.cloud.datacatalog_lineage_v1.types.lineage import (
    BatchSearchLinkProcessesRequest,
    BatchSearchLinkProcessesResponse,
    CreateLineageEventRequest,
    CreateProcessRequest,
    CreateRunRequest,
    DeleteLineageEventRequest,
    DeleteProcessRequest,
    DeleteRunRequest,
    DependencyInfo,
    DependencyType,
    EntityReference,
    EventLink,
    GetLineageEventRequest,
    GetProcessRequest,
    GetRunRequest,
    LineageEvent,
    LineageLink,
    Link,
    ListLineageEventsRequest,
    ListLineageEventsResponse,
    ListProcessesRequest,
    ListProcessesResponse,
    ListRunsRequest,
    ListRunsResponse,
    MultipleEntityReference,
    OperationMetadata,
    Origin,
    Process,
    ProcessLinkInfo,
    ProcessLinks,
    ProcessOpenLineageRunEventRequest,
    ProcessOpenLineageRunEventResponse,
    Run,
    SearchLineageStreamingRequest,
    SearchLineageStreamingResponse,
    SearchLinksRequest,
    SearchLinksResponse,
    UpdateProcessRequest,
    UpdateRunRequest,
)

__all__ = (
    "LineageClient",
    "LineageAsyncClient",
    "BatchSearchLinkProcessesRequest",
    "BatchSearchLinkProcessesResponse",
    "CreateLineageEventRequest",
    "CreateProcessRequest",
    "CreateRunRequest",
    "DeleteLineageEventRequest",
    "DeleteProcessRequest",
    "DeleteRunRequest",
    "DependencyInfo",
    "EntityReference",
    "EventLink",
    "GetLineageEventRequest",
    "GetProcessRequest",
    "GetRunRequest",
    "LineageEvent",
    "LineageLink",
    "Link",
    "ListLineageEventsRequest",
    "ListLineageEventsResponse",
    "ListProcessesRequest",
    "ListProcessesResponse",
    "ListRunsRequest",
    "ListRunsResponse",
    "MultipleEntityReference",
    "OperationMetadata",
    "Origin",
    "Process",
    "ProcessLinkInfo",
    "ProcessLinks",
    "ProcessOpenLineageRunEventRequest",
    "ProcessOpenLineageRunEventResponse",
    "Run",
    "SearchLineageStreamingRequest",
    "SearchLineageStreamingResponse",
    "SearchLinksRequest",
    "SearchLinksResponse",
    "UpdateProcessRequest",
    "UpdateRunRequest",
    "DependencyType",
)
