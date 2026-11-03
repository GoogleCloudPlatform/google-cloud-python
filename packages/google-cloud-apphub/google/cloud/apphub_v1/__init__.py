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

from google.cloud.apphub_v1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.apphub_v1.services.app_hub",
    "google.cloud.apphub_v1.types.apphub_service",
    "google.cloud.apphub_v1.types.application",
    "google.cloud.apphub_v1.types.attributes",
    "google.cloud.apphub_v1.types.boundary",
    "google.cloud.apphub_v1.types.extended_metadata_schema",
    "google.cloud.apphub_v1.types.properties",
    "google.cloud.apphub_v1.types.service",
    "google.cloud.apphub_v1.types.service_project_attachment",
    "google.cloud.apphub_v1.types.workload",
}


from .services.app_hub import AppHubAsyncClient, AppHubClient
from .types.apphub_service import (
    CreateApplicationRequest,
    CreateServiceProjectAttachmentRequest,
    CreateServiceRequest,
    CreateWorkloadRequest,
    DeleteApplicationRequest,
    DeleteServiceProjectAttachmentRequest,
    DeleteServiceRequest,
    DeleteWorkloadRequest,
    DetachServiceProjectAttachmentRequest,
    DetachServiceProjectAttachmentResponse,
    GetApplicationRequest,
    GetBoundaryRequest,
    GetDiscoveredServiceRequest,
    GetDiscoveredWorkloadRequest,
    GetExtendedMetadataSchemaRequest,
    GetServiceProjectAttachmentRequest,
    GetServiceRequest,
    GetWorkloadRequest,
    ListApplicationsRequest,
    ListApplicationsResponse,
    ListDiscoveredServicesRequest,
    ListDiscoveredServicesResponse,
    ListDiscoveredWorkloadsRequest,
    ListDiscoveredWorkloadsResponse,
    ListExtendedMetadataSchemasRequest,
    ListExtendedMetadataSchemasResponse,
    ListServiceProjectAttachmentsRequest,
    ListServiceProjectAttachmentsResponse,
    ListServicesRequest,
    ListServicesResponse,
    ListWorkloadsRequest,
    ListWorkloadsResponse,
    LookupDiscoveredServiceRequest,
    LookupDiscoveredServiceResponse,
    LookupDiscoveredWorkloadRequest,
    LookupDiscoveredWorkloadResponse,
    LookupServiceProjectAttachmentRequest,
    LookupServiceProjectAttachmentResponse,
    OperationMetadata,
    UpdateApplicationRequest,
    UpdateBoundaryRequest,
    UpdateServiceRequest,
    UpdateWorkloadRequest,
)
from .types.application import (
    Application,
    ApplicationProperties,
    ApplicationType,
    Scope,
)
from .types.attributes import Attributes, ContactInfo, Criticality, Environment
from .types.boundary import Boundary
from .types.extended_metadata_schema import ExtendedMetadataSchema
from .types.properties import (
    ExtendedMetadata,
    FunctionalType,
    Identity,
    RegistrationType,
)
from .types.service import (
    DiscoveredService,
    Service,
    ServiceProperties,
    ServiceReference,
)
from .types.service_project_attachment import ServiceProjectAttachment
from .types.workload import (
    DiscoveredWorkload,
    Workload,
    WorkloadProperties,
    WorkloadReference,
)

__all__ = (
    "AppHubAsyncClient",
    "AppHubClient",
    "Application",
    "ApplicationProperties",
    "ApplicationType",
    "Attributes",
    "Boundary",
    "ContactInfo",
    "CreateApplicationRequest",
    "CreateServiceProjectAttachmentRequest",
    "CreateServiceRequest",
    "CreateWorkloadRequest",
    "Criticality",
    "DeleteApplicationRequest",
    "DeleteServiceProjectAttachmentRequest",
    "DeleteServiceRequest",
    "DeleteWorkloadRequest",
    "DetachServiceProjectAttachmentRequest",
    "DetachServiceProjectAttachmentResponse",
    "DiscoveredService",
    "DiscoveredWorkload",
    "Environment",
    "ExtendedMetadata",
    "ExtendedMetadataSchema",
    "FunctionalType",
    "GetApplicationRequest",
    "GetBoundaryRequest",
    "GetDiscoveredServiceRequest",
    "GetDiscoveredWorkloadRequest",
    "GetExtendedMetadataSchemaRequest",
    "GetServiceProjectAttachmentRequest",
    "GetServiceRequest",
    "GetWorkloadRequest",
    "Identity",
    "ListApplicationsRequest",
    "ListApplicationsResponse",
    "ListDiscoveredServicesRequest",
    "ListDiscoveredServicesResponse",
    "ListDiscoveredWorkloadsRequest",
    "ListDiscoveredWorkloadsResponse",
    "ListExtendedMetadataSchemasRequest",
    "ListExtendedMetadataSchemasResponse",
    "ListServiceProjectAttachmentsRequest",
    "ListServiceProjectAttachmentsResponse",
    "ListServicesRequest",
    "ListServicesResponse",
    "ListWorkloadsRequest",
    "ListWorkloadsResponse",
    "LookupDiscoveredServiceRequest",
    "LookupDiscoveredServiceResponse",
    "LookupDiscoveredWorkloadRequest",
    "LookupDiscoveredWorkloadResponse",
    "LookupServiceProjectAttachmentRequest",
    "LookupServiceProjectAttachmentResponse",
    "OperationMetadata",
    "RegistrationType",
    "Scope",
    "Service",
    "ServiceProjectAttachment",
    "ServiceProperties",
    "ServiceReference",
    "UpdateApplicationRequest",
    "UpdateBoundaryRequest",
    "UpdateServiceRequest",
    "UpdateWorkloadRequest",
    "Workload",
    "WorkloadProperties",
    "WorkloadReference",
)

api_core.check_python_version("google.cloud.apphub_v1")
api_core.check_dependency_versions("google.cloud.apphub_v1")
