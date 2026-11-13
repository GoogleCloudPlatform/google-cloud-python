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

from google.cloud.servicedirectory_v1beta1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.servicedirectory_v1beta1.services.lookup_service",
    "google.cloud.servicedirectory_v1beta1.services.registration_service",
    "google.cloud.servicedirectory_v1beta1.types.endpoint",
    "google.cloud.servicedirectory_v1beta1.types.lookup_service",
    "google.cloud.servicedirectory_v1beta1.types.namespace",
    "google.cloud.servicedirectory_v1beta1.types.registration_service",
    "google.cloud.servicedirectory_v1beta1.types.service",
}


from .services.lookup_service import LookupServiceAsyncClient, LookupServiceClient
from .services.registration_service import (
    RegistrationServiceAsyncClient,
    RegistrationServiceClient,
)
from .types.endpoint import Endpoint
from .types.lookup_service import ResolveServiceRequest, ResolveServiceResponse
from .types.namespace import Namespace
from .types.registration_service import (
    CreateEndpointRequest,
    CreateNamespaceRequest,
    CreateServiceRequest,
    DeleteEndpointRequest,
    DeleteNamespaceRequest,
    DeleteServiceRequest,
    GetEndpointRequest,
    GetNamespaceRequest,
    GetServiceRequest,
    ListEndpointsRequest,
    ListEndpointsResponse,
    ListNamespacesRequest,
    ListNamespacesResponse,
    ListServicesRequest,
    ListServicesResponse,
    UpdateEndpointRequest,
    UpdateNamespaceRequest,
    UpdateServiceRequest,
)
from .types.service import Service

__all__ = (
    "LookupServiceAsyncClient",
    "RegistrationServiceAsyncClient",
    "CreateEndpointRequest",
    "CreateNamespaceRequest",
    "CreateServiceRequest",
    "DeleteEndpointRequest",
    "DeleteNamespaceRequest",
    "DeleteServiceRequest",
    "Endpoint",
    "GetEndpointRequest",
    "GetNamespaceRequest",
    "GetServiceRequest",
    "ListEndpointsRequest",
    "ListEndpointsResponse",
    "ListNamespacesRequest",
    "ListNamespacesResponse",
    "ListServicesRequest",
    "ListServicesResponse",
    "LookupServiceClient",
    "Namespace",
    "RegistrationServiceClient",
    "ResolveServiceRequest",
    "ResolveServiceResponse",
    "Service",
    "UpdateEndpointRequest",
    "UpdateNamespaceRequest",
    "UpdateServiceRequest",
)

api_core.check_python_version("google.cloud.servicedirectory_v1beta1")
api_core.check_dependency_versions("google.cloud.servicedirectory_v1beta1")
