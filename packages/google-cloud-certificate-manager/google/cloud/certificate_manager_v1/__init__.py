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

from google.cloud.certificate_manager_v1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.certificate_manager_v1.services.certificate_manager",
    "google.cloud.certificate_manager_v1.types.certificate_issuance_config",
    "google.cloud.certificate_manager_v1.types.certificate_manager",
    "google.cloud.certificate_manager_v1.types.trust_config",
}


from .services.certificate_manager import (
    CertificateManagerAsyncClient,
    CertificateManagerClient,
)
from .types.certificate_issuance_config import (
    CertificateIssuanceConfig,
    CreateCertificateIssuanceConfigRequest,
    DeleteCertificateIssuanceConfigRequest,
    GetCertificateIssuanceConfigRequest,
    ListCertificateIssuanceConfigsRequest,
    ListCertificateIssuanceConfigsResponse,
    UpdateCertificateIssuanceConfigRequest,
)
from .types.certificate_manager import (
    Certificate,
    CertificateMap,
    CertificateMapEntry,
    CreateCertificateMapEntryRequest,
    CreateCertificateMapRequest,
    CreateCertificateRequest,
    CreateDnsAuthorizationRequest,
    DeleteCertificateMapEntryRequest,
    DeleteCertificateMapRequest,
    DeleteCertificateRequest,
    DeleteDnsAuthorizationRequest,
    DnsAuthorization,
    GetCertificateMapEntryRequest,
    GetCertificateMapRequest,
    GetCertificateRequest,
    GetDnsAuthorizationRequest,
    ListCertificateMapEntriesRequest,
    ListCertificateMapEntriesResponse,
    ListCertificateMapsRequest,
    ListCertificateMapsResponse,
    ListCertificatesRequest,
    ListCertificatesResponse,
    ListDnsAuthorizationsRequest,
    ListDnsAuthorizationsResponse,
    OperationMetadata,
    ServingState,
    UpdateCertificateMapEntryRequest,
    UpdateCertificateMapRequest,
    UpdateCertificateRequest,
    UpdateDnsAuthorizationRequest,
)
from .types.trust_config import (
    CreateTrustConfigRequest,
    DeleteTrustConfigRequest,
    GetTrustConfigRequest,
    ListTrustConfigsRequest,
    ListTrustConfigsResponse,
    TrustConfig,
    UpdateTrustConfigRequest,
)

__all__ = (
    "CertificateManagerAsyncClient",
    "Certificate",
    "CertificateIssuanceConfig",
    "CertificateManagerClient",
    "CertificateMap",
    "CertificateMapEntry",
    "CreateCertificateIssuanceConfigRequest",
    "CreateCertificateMapEntryRequest",
    "CreateCertificateMapRequest",
    "CreateCertificateRequest",
    "CreateDnsAuthorizationRequest",
    "CreateTrustConfigRequest",
    "DeleteCertificateIssuanceConfigRequest",
    "DeleteCertificateMapEntryRequest",
    "DeleteCertificateMapRequest",
    "DeleteCertificateRequest",
    "DeleteDnsAuthorizationRequest",
    "DeleteTrustConfigRequest",
    "DnsAuthorization",
    "GetCertificateIssuanceConfigRequest",
    "GetCertificateMapEntryRequest",
    "GetCertificateMapRequest",
    "GetCertificateRequest",
    "GetDnsAuthorizationRequest",
    "GetTrustConfigRequest",
    "ListCertificateIssuanceConfigsRequest",
    "ListCertificateIssuanceConfigsResponse",
    "ListCertificateMapEntriesRequest",
    "ListCertificateMapEntriesResponse",
    "ListCertificateMapsRequest",
    "ListCertificateMapsResponse",
    "ListCertificatesRequest",
    "ListCertificatesResponse",
    "ListDnsAuthorizationsRequest",
    "ListDnsAuthorizationsResponse",
    "ListTrustConfigsRequest",
    "ListTrustConfigsResponse",
    "OperationMetadata",
    "ServingState",
    "TrustConfig",
    "UpdateCertificateIssuanceConfigRequest",
    "UpdateCertificateMapEntryRequest",
    "UpdateCertificateMapRequest",
    "UpdateCertificateRequest",
    "UpdateDnsAuthorizationRequest",
    "UpdateTrustConfigRequest",
)

api_core.check_python_version("google.cloud.certificate_manager_v1")
api_core.check_dependency_versions("google.cloud.certificate_manager_v1")
