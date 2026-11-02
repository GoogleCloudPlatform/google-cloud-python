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
from google.cloud.domains import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.domains_v1.services.domains.async_client import DomainsAsyncClient
from google.cloud.domains_v1.services.domains.client import DomainsClient
from google.cloud.domains_v1.types.domains import (
    AuthorizationCode,
    ConfigureContactSettingsRequest,
    ConfigureDnsSettingsRequest,
    ConfigureManagementSettingsRequest,
    ContactNotice,
    ContactPrivacy,
    ContactSettings,
    DeleteRegistrationRequest,
    DnsSettings,
    DomainNotice,
    ExportRegistrationRequest,
    GetRegistrationRequest,
    ListRegistrationsRequest,
    ListRegistrationsResponse,
    ManagementSettings,
    OperationMetadata,
    RegisterDomainRequest,
    RegisterParameters,
    Registration,
    ResetAuthorizationCodeRequest,
    RetrieveAuthorizationCodeRequest,
    RetrieveRegisterParametersRequest,
    RetrieveRegisterParametersResponse,
    RetrieveTransferParametersRequest,
    RetrieveTransferParametersResponse,
    SearchDomainsRequest,
    SearchDomainsResponse,
    TransferDomainRequest,
    TransferLockState,
    TransferParameters,
    UpdateRegistrationRequest,
)

__all__ = (
    "DomainsClient",
    "DomainsAsyncClient",
    "AuthorizationCode",
    "ConfigureContactSettingsRequest",
    "ConfigureDnsSettingsRequest",
    "ConfigureManagementSettingsRequest",
    "ContactSettings",
    "DeleteRegistrationRequest",
    "DnsSettings",
    "ExportRegistrationRequest",
    "GetRegistrationRequest",
    "ListRegistrationsRequest",
    "ListRegistrationsResponse",
    "ManagementSettings",
    "OperationMetadata",
    "RegisterDomainRequest",
    "RegisterParameters",
    "Registration",
    "ResetAuthorizationCodeRequest",
    "RetrieveAuthorizationCodeRequest",
    "RetrieveRegisterParametersRequest",
    "RetrieveRegisterParametersResponse",
    "RetrieveTransferParametersRequest",
    "RetrieveTransferParametersResponse",
    "SearchDomainsRequest",
    "SearchDomainsResponse",
    "TransferDomainRequest",
    "TransferParameters",
    "UpdateRegistrationRequest",
    "ContactNotice",
    "ContactPrivacy",
    "DomainNotice",
    "TransferLockState",
)
