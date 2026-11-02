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

from google.cloud.security.privateca_v1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.security.privateca_v1.services.certificate_authority_service",
    "google.cloud.security.privateca_v1.types.resources",
    "google.cloud.security.privateca_v1.types.service",
}


from .services.certificate_authority_service import (
    CertificateAuthorityServiceAsyncClient,
    CertificateAuthorityServiceClient,
)
from .types.resources import (
    AttributeType,
    AttributeTypeAndValue,
    CaPool,
    Certificate,
    CertificateAuthority,
    CertificateConfig,
    CertificateDescription,
    CertificateExtensionConstraints,
    CertificateIdentityConstraints,
    CertificateRevocationList,
    CertificateTemplate,
    EncryptionSpec,
    KeyUsage,
    ObjectId,
    PublicKey,
    RelativeDistinguishedName,
    RevocationReason,
    Subject,
    SubjectAltNames,
    SubjectRequestMode,
    SubordinateConfig,
    X509Extension,
    X509Parameters,
)
from .types.service import (
    ActivateCertificateAuthorityRequest,
    CreateCaPoolRequest,
    CreateCertificateAuthorityRequest,
    CreateCertificateRequest,
    CreateCertificateTemplateRequest,
    DeleteCaPoolRequest,
    DeleteCertificateAuthorityRequest,
    DeleteCertificateTemplateRequest,
    DisableCertificateAuthorityRequest,
    EnableCertificateAuthorityRequest,
    FetchCaCertsRequest,
    FetchCaCertsResponse,
    FetchCertificateAuthorityCsrRequest,
    FetchCertificateAuthorityCsrResponse,
    GetCaPoolRequest,
    GetCertificateAuthorityRequest,
    GetCertificateRequest,
    GetCertificateRevocationListRequest,
    GetCertificateTemplateRequest,
    ListCaPoolsRequest,
    ListCaPoolsResponse,
    ListCertificateAuthoritiesRequest,
    ListCertificateAuthoritiesResponse,
    ListCertificateRevocationListsRequest,
    ListCertificateRevocationListsResponse,
    ListCertificatesRequest,
    ListCertificatesResponse,
    ListCertificateTemplatesRequest,
    ListCertificateTemplatesResponse,
    OperationMetadata,
    RevokeCertificateRequest,
    UndeleteCertificateAuthorityRequest,
    UpdateCaPoolRequest,
    UpdateCertificateAuthorityRequest,
    UpdateCertificateRequest,
    UpdateCertificateRevocationListRequest,
    UpdateCertificateTemplateRequest,
)

__all__ = (
    "CertificateAuthorityServiceAsyncClient",
    "ActivateCertificateAuthorityRequest",
    "AttributeType",
    "AttributeTypeAndValue",
    "CaPool",
    "Certificate",
    "CertificateAuthority",
    "CertificateAuthorityServiceClient",
    "CertificateConfig",
    "CertificateDescription",
    "CertificateExtensionConstraints",
    "CertificateIdentityConstraints",
    "CertificateRevocationList",
    "CertificateTemplate",
    "CreateCaPoolRequest",
    "CreateCertificateAuthorityRequest",
    "CreateCertificateRequest",
    "CreateCertificateTemplateRequest",
    "DeleteCaPoolRequest",
    "DeleteCertificateAuthorityRequest",
    "DeleteCertificateTemplateRequest",
    "DisableCertificateAuthorityRequest",
    "EnableCertificateAuthorityRequest",
    "EncryptionSpec",
    "FetchCaCertsRequest",
    "FetchCaCertsResponse",
    "FetchCertificateAuthorityCsrRequest",
    "FetchCertificateAuthorityCsrResponse",
    "GetCaPoolRequest",
    "GetCertificateAuthorityRequest",
    "GetCertificateRequest",
    "GetCertificateRevocationListRequest",
    "GetCertificateTemplateRequest",
    "KeyUsage",
    "ListCaPoolsRequest",
    "ListCaPoolsResponse",
    "ListCertificateAuthoritiesRequest",
    "ListCertificateAuthoritiesResponse",
    "ListCertificateRevocationListsRequest",
    "ListCertificateRevocationListsResponse",
    "ListCertificateTemplatesRequest",
    "ListCertificateTemplatesResponse",
    "ListCertificatesRequest",
    "ListCertificatesResponse",
    "ObjectId",
    "OperationMetadata",
    "PublicKey",
    "RelativeDistinguishedName",
    "RevocationReason",
    "RevokeCertificateRequest",
    "Subject",
    "SubjectAltNames",
    "SubjectRequestMode",
    "SubordinateConfig",
    "UndeleteCertificateAuthorityRequest",
    "UpdateCaPoolRequest",
    "UpdateCertificateAuthorityRequest",
    "UpdateCertificateRequest",
    "UpdateCertificateRevocationListRequest",
    "UpdateCertificateTemplateRequest",
    "X509Extension",
    "X509Parameters",
)

api_core.check_python_version("google.cloud.security.privateca_v1")
api_core.check_dependency_versions("google.cloud.security.privateca_v1")
