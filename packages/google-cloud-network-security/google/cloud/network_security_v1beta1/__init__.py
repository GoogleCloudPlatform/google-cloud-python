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

from google.cloud.network_security_v1beta1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.network_security_v1beta1.services.dns_threat_detector_service",
    "google.cloud.network_security_v1beta1.services.network_security",
    "google.cloud.network_security_v1beta1.types.authorization_policy",
    "google.cloud.network_security_v1beta1.types.client_tls_policy",
    "google.cloud.network_security_v1beta1.types.common",
    "google.cloud.network_security_v1beta1.types.dns_threat_detector",
    "google.cloud.network_security_v1beta1.types.network_security",
    "google.cloud.network_security_v1beta1.types.server_tls_policy",
    "google.cloud.network_security_v1beta1.types.tls",
}


from .services.dns_threat_detector_service import (
    DnsThreatDetectorServiceAsyncClient,
    DnsThreatDetectorServiceClient,
)
from .services.network_security import NetworkSecurityAsyncClient, NetworkSecurityClient
from .types.authorization_policy import (
    AuthorizationPolicy,
    CreateAuthorizationPolicyRequest,
    DeleteAuthorizationPolicyRequest,
    GetAuthorizationPolicyRequest,
    ListAuthorizationPoliciesRequest,
    ListAuthorizationPoliciesResponse,
    UpdateAuthorizationPolicyRequest,
)
from .types.client_tls_policy import (
    ClientTlsPolicy,
    CreateClientTlsPolicyRequest,
    DeleteClientTlsPolicyRequest,
    GetClientTlsPolicyRequest,
    ListClientTlsPoliciesRequest,
    ListClientTlsPoliciesResponse,
    UpdateClientTlsPolicyRequest,
)
from .types.common import OperationMetadata
from .types.dns_threat_detector import (
    CreateDnsThreatDetectorRequest,
    DeleteDnsThreatDetectorRequest,
    DnsThreatDetector,
    GetDnsThreatDetectorRequest,
    ListDnsThreatDetectorsRequest,
    ListDnsThreatDetectorsResponse,
    UpdateDnsThreatDetectorRequest,
)
from .types.server_tls_policy import (
    CreateServerTlsPolicyRequest,
    DeleteServerTlsPolicyRequest,
    GetServerTlsPolicyRequest,
    ListServerTlsPoliciesRequest,
    ListServerTlsPoliciesResponse,
    ServerTlsPolicy,
    UpdateServerTlsPolicyRequest,
)
from .types.tls import (
    CertificateProvider,
    CertificateProviderInstance,
    GrpcEndpoint,
    ValidationCA,
)

__all__ = (
    "DnsThreatDetectorServiceAsyncClient",
    "NetworkSecurityAsyncClient",
    "AuthorizationPolicy",
    "CertificateProvider",
    "CertificateProviderInstance",
    "ClientTlsPolicy",
    "CreateAuthorizationPolicyRequest",
    "CreateClientTlsPolicyRequest",
    "CreateDnsThreatDetectorRequest",
    "CreateServerTlsPolicyRequest",
    "DeleteAuthorizationPolicyRequest",
    "DeleteClientTlsPolicyRequest",
    "DeleteDnsThreatDetectorRequest",
    "DeleteServerTlsPolicyRequest",
    "DnsThreatDetector",
    "DnsThreatDetectorServiceClient",
    "GetAuthorizationPolicyRequest",
    "GetClientTlsPolicyRequest",
    "GetDnsThreatDetectorRequest",
    "GetServerTlsPolicyRequest",
    "GrpcEndpoint",
    "ListAuthorizationPoliciesRequest",
    "ListAuthorizationPoliciesResponse",
    "ListClientTlsPoliciesRequest",
    "ListClientTlsPoliciesResponse",
    "ListDnsThreatDetectorsRequest",
    "ListDnsThreatDetectorsResponse",
    "ListServerTlsPoliciesRequest",
    "ListServerTlsPoliciesResponse",
    "NetworkSecurityClient",
    "OperationMetadata",
    "ServerTlsPolicy",
    "UpdateAuthorizationPolicyRequest",
    "UpdateClientTlsPolicyRequest",
    "UpdateDnsThreatDetectorRequest",
    "UpdateServerTlsPolicyRequest",
    "ValidationCA",
)

api_core.check_python_version("google.cloud.network_security_v1beta1")
api_core.check_dependency_versions("google.cloud.network_security_v1beta1")
