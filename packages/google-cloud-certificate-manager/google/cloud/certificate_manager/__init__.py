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
from google.cloud.certificate_manager import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.certificate_manager_v1.services.certificate_manager.async_client import (
    CertificateManagerAsyncClient,
)
from google.cloud.certificate_manager_v1.services.certificate_manager.client import (
    CertificateManagerClient,
)
from google.cloud.certificate_manager_v1.types.certificate_issuance_config import (
    CertificateIssuanceConfig,
    CreateCertificateIssuanceConfigRequest,
    DeleteCertificateIssuanceConfigRequest,
    GetCertificateIssuanceConfigRequest,
    ListCertificateIssuanceConfigsRequest,
    ListCertificateIssuanceConfigsResponse,
    UpdateCertificateIssuanceConfigRequest,
)
from google.cloud.certificate_manager_v1.types.certificate_manager import (
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
from google.cloud.certificate_manager_v1.types.trust_config import (
    CreateTrustConfigRequest,
    DeleteTrustConfigRequest,
    GetTrustConfigRequest,
    ListTrustConfigsRequest,
    ListTrustConfigsResponse,
    TrustConfig,
    UpdateTrustConfigRequest,
)

__all__ = (
    "CertificateManagerClient",
    "CertificateManagerAsyncClient",
    "CertificateIssuanceConfig",
    "CreateCertificateIssuanceConfigRequest",
    "DeleteCertificateIssuanceConfigRequest",
    "GetCertificateIssuanceConfigRequest",
    "ListCertificateIssuanceConfigsRequest",
    "ListCertificateIssuanceConfigsResponse",
    "UpdateCertificateIssuanceConfigRequest",
    "Certificate",
    "CertificateMap",
    "CertificateMapEntry",
    "CreateCertificateMapEntryRequest",
    "CreateCertificateMapRequest",
    "CreateCertificateRequest",
    "CreateDnsAuthorizationRequest",
    "DeleteCertificateMapEntryRequest",
    "DeleteCertificateMapRequest",
    "DeleteCertificateRequest",
    "DeleteDnsAuthorizationRequest",
    "DnsAuthorization",
    "GetCertificateMapEntryRequest",
    "GetCertificateMapRequest",
    "GetCertificateRequest",
    "GetDnsAuthorizationRequest",
    "ListCertificateMapEntriesRequest",
    "ListCertificateMapEntriesResponse",
    "ListCertificateMapsRequest",
    "ListCertificateMapsResponse",
    "ListCertificatesRequest",
    "ListCertificatesResponse",
    "ListDnsAuthorizationsRequest",
    "ListDnsAuthorizationsResponse",
    "OperationMetadata",
    "UpdateCertificateMapEntryRequest",
    "UpdateCertificateMapRequest",
    "UpdateCertificateRequest",
    "UpdateDnsAuthorizationRequest",
    "ServingState",
    "CreateTrustConfigRequest",
    "DeleteTrustConfigRequest",
    "GetTrustConfigRequest",
    "ListTrustConfigsRequest",
    "ListTrustConfigsResponse",
    "TrustConfig",
    "UpdateTrustConfigRequest",
)
