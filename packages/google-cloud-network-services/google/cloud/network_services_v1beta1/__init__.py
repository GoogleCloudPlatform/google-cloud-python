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

from google.cloud.network_services_v1beta1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.network_services_v1beta1.services.dep_service",
    "google.cloud.network_services_v1beta1.services.network_services",
    "google.cloud.network_services_v1beta1.types.common",
    "google.cloud.network_services_v1beta1.types.dep",
    "google.cloud.network_services_v1beta1.types.endpoint_policy",
    "google.cloud.network_services_v1beta1.types.network_services",
}


from .services.dep_service import DepServiceAsyncClient, DepServiceClient
from .services.network_services import NetworkServicesAsyncClient, NetworkServicesClient
from .types.common import EndpointMatcher, OperationMetadata, TrafficPortSelector
from .types.dep import (
    CreateExtensionBindingRequest,
    CreateLbRouteExtensionRequest,
    CreateLbTrafficExtensionRequest,
    DeleteExtensionBindingRequest,
    DeleteLbRouteExtensionRequest,
    DeleteLbTrafficExtensionRequest,
    EventType,
    ExtensionBinding,
    ExtensionChain,
    GetExtensionBindingRequest,
    GetLbRouteExtensionRequest,
    GetLbTrafficExtensionRequest,
    LbRouteExtension,
    LbTrafficExtension,
    ListExtensionBindingsRequest,
    ListExtensionBindingsResponse,
    ListLbRouteExtensionsRequest,
    ListLbRouteExtensionsResponse,
    ListLbTrafficExtensionsRequest,
    ListLbTrafficExtensionsResponse,
    LoadBalancingScheme,
    UpdateExtensionBindingRequest,
    UpdateLbRouteExtensionRequest,
    UpdateLbTrafficExtensionRequest,
)
from .types.endpoint_policy import (
    CreateEndpointPolicyRequest,
    DeleteEndpointPolicyRequest,
    EndpointPolicy,
    GetEndpointPolicyRequest,
    ListEndpointPoliciesRequest,
    ListEndpointPoliciesResponse,
    UpdateEndpointPolicyRequest,
)

__all__ = (
    "DepServiceAsyncClient",
    "NetworkServicesAsyncClient",
    "CreateEndpointPolicyRequest",
    "CreateExtensionBindingRequest",
    "CreateLbRouteExtensionRequest",
    "CreateLbTrafficExtensionRequest",
    "DeleteEndpointPolicyRequest",
    "DeleteExtensionBindingRequest",
    "DeleteLbRouteExtensionRequest",
    "DeleteLbTrafficExtensionRequest",
    "DepServiceClient",
    "EndpointMatcher",
    "EndpointPolicy",
    "EventType",
    "ExtensionBinding",
    "ExtensionChain",
    "GetEndpointPolicyRequest",
    "GetExtensionBindingRequest",
    "GetLbRouteExtensionRequest",
    "GetLbTrafficExtensionRequest",
    "LbRouteExtension",
    "LbTrafficExtension",
    "ListEndpointPoliciesRequest",
    "ListEndpointPoliciesResponse",
    "ListExtensionBindingsRequest",
    "ListExtensionBindingsResponse",
    "ListLbRouteExtensionsRequest",
    "ListLbRouteExtensionsResponse",
    "ListLbTrafficExtensionsRequest",
    "ListLbTrafficExtensionsResponse",
    "LoadBalancingScheme",
    "NetworkServicesClient",
    "OperationMetadata",
    "TrafficPortSelector",
    "UpdateEndpointPolicyRequest",
    "UpdateExtensionBindingRequest",
    "UpdateLbRouteExtensionRequest",
    "UpdateLbTrafficExtensionRequest",
)

api_core.check_python_version("google.cloud.network_services_v1beta1")
api_core.check_dependency_versions("google.cloud.network_services_v1beta1")
