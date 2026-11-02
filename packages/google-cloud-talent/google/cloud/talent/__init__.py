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
from google.cloud.talent import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.talent_v4.services.company_service.async_client import (
    CompanyServiceAsyncClient,
)
from google.cloud.talent_v4.services.company_service.client import CompanyServiceClient
from google.cloud.talent_v4.services.completion.async_client import (
    CompletionAsyncClient,
)
from google.cloud.talent_v4.services.completion.client import CompletionClient
from google.cloud.talent_v4.services.event_service.async_client import (
    EventServiceAsyncClient,
)
from google.cloud.talent_v4.services.event_service.client import EventServiceClient
from google.cloud.talent_v4.services.job_service.async_client import (
    JobServiceAsyncClient,
)
from google.cloud.talent_v4.services.job_service.client import JobServiceClient
from google.cloud.talent_v4.services.tenant_service.async_client import (
    TenantServiceAsyncClient,
)
from google.cloud.talent_v4.services.tenant_service.client import TenantServiceClient
from google.cloud.talent_v4.types.common import (
    BatchOperationMetadata,
    CommuteMethod,
    CompanySize,
    CompensationInfo,
    CustomAttribute,
    DegreeType,
    DeviceInfo,
    EmploymentType,
    HtmlSanitization,
    JobBenefit,
    JobCategory,
    JobLevel,
    Location,
    PostingRegion,
    RequestMetadata,
    ResponseMetadata,
    SpellingCorrection,
    TimestampRange,
    Visibility,
)
from google.cloud.talent_v4.types.company import Company
from google.cloud.talent_v4.types.company_service import (
    CreateCompanyRequest,
    DeleteCompanyRequest,
    GetCompanyRequest,
    ListCompaniesRequest,
    ListCompaniesResponse,
    UpdateCompanyRequest,
)
from google.cloud.talent_v4.types.completion_service import (
    CompleteQueryRequest,
    CompleteQueryResponse,
)
from google.cloud.talent_v4.types.event import ClientEvent, JobEvent
from google.cloud.talent_v4.types.event_service import CreateClientEventRequest
from google.cloud.talent_v4.types.filters import (
    CommuteFilter,
    CompensationFilter,
    JobQuery,
    LocationFilter,
)
from google.cloud.talent_v4.types.histogram import HistogramQuery, HistogramQueryResult
from google.cloud.talent_v4.types.job import Job
from google.cloud.talent_v4.types.job_service import (
    BatchCreateJobsRequest,
    BatchCreateJobsResponse,
    BatchDeleteJobsRequest,
    BatchDeleteJobsResponse,
    BatchUpdateJobsRequest,
    BatchUpdateJobsResponse,
    CreateJobRequest,
    DeleteJobRequest,
    GetJobRequest,
    JobResult,
    JobView,
    ListJobsRequest,
    ListJobsResponse,
    SearchJobsRequest,
    SearchJobsResponse,
    UpdateJobRequest,
)
from google.cloud.talent_v4.types.tenant import Tenant
from google.cloud.talent_v4.types.tenant_service import (
    CreateTenantRequest,
    DeleteTenantRequest,
    GetTenantRequest,
    ListTenantsRequest,
    ListTenantsResponse,
    UpdateTenantRequest,
)

__all__ = (
    "CompanyServiceClient",
    "CompanyServiceAsyncClient",
    "CompletionClient",
    "CompletionAsyncClient",
    "EventServiceClient",
    "EventServiceAsyncClient",
    "JobServiceClient",
    "JobServiceAsyncClient",
    "TenantServiceClient",
    "TenantServiceAsyncClient",
    "BatchOperationMetadata",
    "CompensationInfo",
    "CustomAttribute",
    "DeviceInfo",
    "Location",
    "RequestMetadata",
    "ResponseMetadata",
    "SpellingCorrection",
    "TimestampRange",
    "CommuteMethod",
    "CompanySize",
    "DegreeType",
    "EmploymentType",
    "HtmlSanitization",
    "JobBenefit",
    "JobCategory",
    "JobLevel",
    "PostingRegion",
    "Visibility",
    "Company",
    "CreateCompanyRequest",
    "DeleteCompanyRequest",
    "GetCompanyRequest",
    "ListCompaniesRequest",
    "ListCompaniesResponse",
    "UpdateCompanyRequest",
    "CompleteQueryRequest",
    "CompleteQueryResponse",
    "ClientEvent",
    "JobEvent",
    "CreateClientEventRequest",
    "CommuteFilter",
    "CompensationFilter",
    "JobQuery",
    "LocationFilter",
    "HistogramQuery",
    "HistogramQueryResult",
    "Job",
    "BatchCreateJobsRequest",
    "BatchCreateJobsResponse",
    "BatchDeleteJobsRequest",
    "BatchDeleteJobsResponse",
    "BatchUpdateJobsRequest",
    "BatchUpdateJobsResponse",
    "CreateJobRequest",
    "DeleteJobRequest",
    "GetJobRequest",
    "JobResult",
    "ListJobsRequest",
    "ListJobsResponse",
    "SearchJobsRequest",
    "SearchJobsResponse",
    "UpdateJobRequest",
    "JobView",
    "Tenant",
    "CreateTenantRequest",
    "DeleteTenantRequest",
    "GetTenantRequest",
    "ListTenantsRequest",
    "ListTenantsResponse",
    "UpdateTenantRequest",
)
