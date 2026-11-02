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

from google.cloud.security.privateca_v1beta1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.security.privateca_v1beta1.services.certificate_authority_service",
    "google.cloud.security.privateca_v1beta1.types.resources",
    "google.cloud.security.privateca_v1beta1.types.service",
}


from .services.certificate_authority_service import (
    CertificateAuthorityServiceAsyncClient,
    CertificateAuthorityServiceClient,
)
from .types.resources import (
    Certificate,
    CertificateAuthority,
    CertificateConfig,
    CertificateDescription,
    CertificateRevocationList,
    KeyUsage,
    ObjectId,
    PublicKey,
    ReusableConfig,
    ReusableConfigValues,
    ReusableConfigWrapper,
    RevocationReason,
    Subject,
    SubjectAltNames,
    SubordinateConfig,
    X509Extension,
)
from .types.service import (
    ActivateCertificateAuthorityRequest,
    CreateCertificateAuthorityRequest,
    CreateCertificateRequest,
    DisableCertificateAuthorityRequest,
    EnableCertificateAuthorityRequest,
    FetchCertificateAuthorityCsrRequest,
    FetchCertificateAuthorityCsrResponse,
    GetCertificateAuthorityRequest,
    GetCertificateRequest,
    GetCertificateRevocationListRequest,
    GetReusableConfigRequest,
    ListCertificateAuthoritiesRequest,
    ListCertificateAuthoritiesResponse,
    ListCertificateRevocationListsRequest,
    ListCertificateRevocationListsResponse,
    ListCertificatesRequest,
    ListCertificatesResponse,
    ListReusableConfigsRequest,
    ListReusableConfigsResponse,
    OperationMetadata,
    RestoreCertificateAuthorityRequest,
    RevokeCertificateRequest,
    ScheduleDeleteCertificateAuthorityRequest,
    UpdateCertificateAuthorityRequest,
    UpdateCertificateRequest,
    UpdateCertificateRevocationListRequest,
)

__all__ = (
    "CertificateAuthorityServiceAsyncClient",
    "ActivateCertificateAuthorityRequest",
    "Certificate",
    "CertificateAuthority",
    "CertificateAuthorityServiceClient",
    "CertificateConfig",
    "CertificateDescription",
    "CertificateRevocationList",
    "CreateCertificateAuthorityRequest",
    "CreateCertificateRequest",
    "DisableCertificateAuthorityRequest",
    "EnableCertificateAuthorityRequest",
    "FetchCertificateAuthorityCsrRequest",
    "FetchCertificateAuthorityCsrResponse",
    "GetCertificateAuthorityRequest",
    "GetCertificateRequest",
    "GetCertificateRevocationListRequest",
    "GetReusableConfigRequest",
    "KeyUsage",
    "ListCertificateAuthoritiesRequest",
    "ListCertificateAuthoritiesResponse",
    "ListCertificateRevocationListsRequest",
    "ListCertificateRevocationListsResponse",
    "ListCertificatesRequest",
    "ListCertificatesResponse",
    "ListReusableConfigsRequest",
    "ListReusableConfigsResponse",
    "ObjectId",
    "OperationMetadata",
    "PublicKey",
    "RestoreCertificateAuthorityRequest",
    "ReusableConfig",
    "ReusableConfigValues",
    "ReusableConfigWrapper",
    "RevocationReason",
    "RevokeCertificateRequest",
    "ScheduleDeleteCertificateAuthorityRequest",
    "Subject",
    "SubjectAltNames",
    "SubordinateConfig",
    "UpdateCertificateAuthorityRequest",
    "UpdateCertificateRequest",
    "UpdateCertificateRevocationListRequest",
    "X509Extension",
)

api_core.check_python_version("google.cloud.security.privateca_v1beta1")
api_core.check_dependency_versions("google.cloud.security.privateca_v1beta1")
