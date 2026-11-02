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
from google.cloud.servicemanagement import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.servicemanagement_v1.services.service_manager.async_client import (
    ServiceManagerAsyncClient,
)
from google.cloud.servicemanagement_v1.services.service_manager.client import (
    ServiceManagerClient,
)
from google.cloud.servicemanagement_v1.types.resources import (
    ChangeReport,
    ConfigFile,
    ConfigRef,
    ConfigSource,
    Diagnostic,
    ManagedService,
    OperationMetadata,
    Rollout,
)
from google.cloud.servicemanagement_v1.types.servicemanager import (
    CreateServiceConfigRequest,
    CreateServiceRequest,
    CreateServiceRolloutRequest,
    DeleteServiceRequest,
    EnableServiceResponse,
    GenerateConfigReportRequest,
    GenerateConfigReportResponse,
    GetServiceConfigRequest,
    GetServiceRequest,
    GetServiceRolloutRequest,
    ListServiceConfigsRequest,
    ListServiceConfigsResponse,
    ListServiceRolloutsRequest,
    ListServiceRolloutsResponse,
    ListServicesRequest,
    ListServicesResponse,
    SubmitConfigSourceRequest,
    SubmitConfigSourceResponse,
    UndeleteServiceRequest,
    UndeleteServiceResponse,
)

__all__ = (
    "ServiceManagerClient",
    "ServiceManagerAsyncClient",
    "ChangeReport",
    "ConfigFile",
    "ConfigRef",
    "ConfigSource",
    "Diagnostic",
    "ManagedService",
    "OperationMetadata",
    "Rollout",
    "CreateServiceConfigRequest",
    "CreateServiceRequest",
    "CreateServiceRolloutRequest",
    "DeleteServiceRequest",
    "EnableServiceResponse",
    "GenerateConfigReportRequest",
    "GenerateConfigReportResponse",
    "GetServiceConfigRequest",
    "GetServiceRequest",
    "GetServiceRolloutRequest",
    "ListServiceConfigsRequest",
    "ListServiceConfigsResponse",
    "ListServiceRolloutsRequest",
    "ListServiceRolloutsResponse",
    "ListServicesRequest",
    "ListServicesResponse",
    "SubmitConfigSourceRequest",
    "SubmitConfigSourceResponse",
    "UndeleteServiceRequest",
    "UndeleteServiceResponse",
)
