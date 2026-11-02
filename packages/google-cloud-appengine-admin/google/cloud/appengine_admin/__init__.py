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
from google.cloud.appengine_admin import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.appengine_admin_v1.services.applications.async_client import (
    ApplicationsAsyncClient,
)
from google.cloud.appengine_admin_v1.services.applications.client import (
    ApplicationsClient,
)
from google.cloud.appengine_admin_v1.services.authorized_certificates.async_client import (
    AuthorizedCertificatesAsyncClient,
)
from google.cloud.appengine_admin_v1.services.authorized_certificates.client import (
    AuthorizedCertificatesClient,
)
from google.cloud.appengine_admin_v1.services.authorized_domains.async_client import (
    AuthorizedDomainsAsyncClient,
)
from google.cloud.appengine_admin_v1.services.authorized_domains.client import (
    AuthorizedDomainsClient,
)
from google.cloud.appengine_admin_v1.services.domain_mappings.async_client import (
    DomainMappingsAsyncClient,
)
from google.cloud.appengine_admin_v1.services.domain_mappings.client import (
    DomainMappingsClient,
)
from google.cloud.appengine_admin_v1.services.firewall.async_client import (
    FirewallAsyncClient,
)
from google.cloud.appengine_admin_v1.services.firewall.client import FirewallClient
from google.cloud.appengine_admin_v1.services.instances.async_client import (
    InstancesAsyncClient,
)
from google.cloud.appengine_admin_v1.services.instances.client import InstancesClient
from google.cloud.appengine_admin_v1.services.services.async_client import (
    ServicesAsyncClient,
)
from google.cloud.appengine_admin_v1.services.services.client import ServicesClient
from google.cloud.appengine_admin_v1.services.versions.async_client import (
    VersionsAsyncClient,
)
from google.cloud.appengine_admin_v1.services.versions.client import VersionsClient
from google.cloud.appengine_admin_v1.types.app_yaml import (
    ApiConfigHandler,
    ApiEndpointHandler,
    AuthFailAction,
    ErrorHandler,
    HealthCheck,
    Library,
    LivenessCheck,
    LoginRequirement,
    ReadinessCheck,
    ScriptHandler,
    SecurityLevel,
    StaticFilesHandler,
    UrlMap,
)
from google.cloud.appengine_admin_v1.types.appengine import (
    AuthorizedCertificateView,
    BatchUpdateIngressRulesRequest,
    BatchUpdateIngressRulesResponse,
    CreateApplicationRequest,
    CreateAuthorizedCertificateRequest,
    CreateDomainMappingRequest,
    CreateIngressRuleRequest,
    CreateVersionRequest,
    DebugInstanceRequest,
    DeleteAuthorizedCertificateRequest,
    DeleteDomainMappingRequest,
    DeleteIngressRuleRequest,
    DeleteInstanceRequest,
    DeleteServiceRequest,
    DeleteVersionRequest,
    DomainOverrideStrategy,
    GetApplicationRequest,
    GetAuthorizedCertificateRequest,
    GetDomainMappingRequest,
    GetIngressRuleRequest,
    GetInstanceRequest,
    GetServiceRequest,
    GetVersionRequest,
    ListAuthorizedCertificatesRequest,
    ListAuthorizedCertificatesResponse,
    ListAuthorizedDomainsRequest,
    ListAuthorizedDomainsResponse,
    ListDomainMappingsRequest,
    ListDomainMappingsResponse,
    ListIngressRulesRequest,
    ListIngressRulesResponse,
    ListInstancesRequest,
    ListInstancesResponse,
    ListServicesRequest,
    ListServicesResponse,
    ListVersionsRequest,
    ListVersionsResponse,
    RepairApplicationRequest,
    UpdateApplicationRequest,
    UpdateAuthorizedCertificateRequest,
    UpdateDomainMappingRequest,
    UpdateIngressRuleRequest,
    UpdateServiceRequest,
    UpdateVersionRequest,
    VersionView,
)
from google.cloud.appengine_admin_v1.types.application import (
    Application,
    UrlDispatchRule,
)
from google.cloud.appengine_admin_v1.types.audit_data import (
    AuditData,
    CreateVersionMethod,
    UpdateServiceMethod,
)
from google.cloud.appengine_admin_v1.types.certificate import (
    AuthorizedCertificate,
    CertificateRawData,
    ManagedCertificate,
    ManagementStatus,
)
from google.cloud.appengine_admin_v1.types.deploy import (
    CloudBuildOptions,
    ContainerInfo,
    Deployment,
    FileInfo,
    ZipInfo,
)
from google.cloud.appengine_admin_v1.types.domain import AuthorizedDomain
from google.cloud.appengine_admin_v1.types.domain_mapping import (
    DomainMapping,
    ResourceRecord,
    SslSettings,
)
from google.cloud.appengine_admin_v1.types.firewall import FirewallRule
from google.cloud.appengine_admin_v1.types.instance import Instance
from google.cloud.appengine_admin_v1.types.location import LocationMetadata
from google.cloud.appengine_admin_v1.types.network_settings import NetworkSettings
from google.cloud.appengine_admin_v1.types.operation import (
    CreateVersionMetadataV1,
    OperationMetadataV1,
)
from google.cloud.appengine_admin_v1.types.service import Service, TrafficSplit
from google.cloud.appengine_admin_v1.types.version import (
    AutomaticScaling,
    BasicScaling,
    CpuUtilization,
    DiskUtilization,
    EndpointsApiService,
    Entrypoint,
    InboundServiceType,
    ManualScaling,
    Network,
    NetworkUtilization,
    RequestUtilization,
    Resources,
    ServingStatus,
    StandardSchedulerSettings,
    Version,
    Volume,
    VpcAccessConnector,
)

__all__ = (
    "ApplicationsClient",
    "ApplicationsAsyncClient",
    "AuthorizedCertificatesClient",
    "AuthorizedCertificatesAsyncClient",
    "AuthorizedDomainsClient",
    "AuthorizedDomainsAsyncClient",
    "DomainMappingsClient",
    "DomainMappingsAsyncClient",
    "FirewallClient",
    "FirewallAsyncClient",
    "InstancesClient",
    "InstancesAsyncClient",
    "ServicesClient",
    "ServicesAsyncClient",
    "VersionsClient",
    "VersionsAsyncClient",
    "ApiConfigHandler",
    "ApiEndpointHandler",
    "ErrorHandler",
    "HealthCheck",
    "Library",
    "LivenessCheck",
    "ReadinessCheck",
    "ScriptHandler",
    "StaticFilesHandler",
    "UrlMap",
    "AuthFailAction",
    "LoginRequirement",
    "SecurityLevel",
    "BatchUpdateIngressRulesRequest",
    "BatchUpdateIngressRulesResponse",
    "CreateApplicationRequest",
    "CreateAuthorizedCertificateRequest",
    "CreateDomainMappingRequest",
    "CreateIngressRuleRequest",
    "CreateVersionRequest",
    "DebugInstanceRequest",
    "DeleteAuthorizedCertificateRequest",
    "DeleteDomainMappingRequest",
    "DeleteIngressRuleRequest",
    "DeleteInstanceRequest",
    "DeleteServiceRequest",
    "DeleteVersionRequest",
    "GetApplicationRequest",
    "GetAuthorizedCertificateRequest",
    "GetDomainMappingRequest",
    "GetIngressRuleRequest",
    "GetInstanceRequest",
    "GetServiceRequest",
    "GetVersionRequest",
    "ListAuthorizedCertificatesRequest",
    "ListAuthorizedCertificatesResponse",
    "ListAuthorizedDomainsRequest",
    "ListAuthorizedDomainsResponse",
    "ListDomainMappingsRequest",
    "ListDomainMappingsResponse",
    "ListIngressRulesRequest",
    "ListIngressRulesResponse",
    "ListInstancesRequest",
    "ListInstancesResponse",
    "ListServicesRequest",
    "ListServicesResponse",
    "ListVersionsRequest",
    "ListVersionsResponse",
    "RepairApplicationRequest",
    "UpdateApplicationRequest",
    "UpdateAuthorizedCertificateRequest",
    "UpdateDomainMappingRequest",
    "UpdateIngressRuleRequest",
    "UpdateServiceRequest",
    "UpdateVersionRequest",
    "AuthorizedCertificateView",
    "DomainOverrideStrategy",
    "VersionView",
    "Application",
    "UrlDispatchRule",
    "AuditData",
    "CreateVersionMethod",
    "UpdateServiceMethod",
    "AuthorizedCertificate",
    "CertificateRawData",
    "ManagedCertificate",
    "ManagementStatus",
    "CloudBuildOptions",
    "ContainerInfo",
    "Deployment",
    "FileInfo",
    "ZipInfo",
    "AuthorizedDomain",
    "DomainMapping",
    "ResourceRecord",
    "SslSettings",
    "FirewallRule",
    "Instance",
    "LocationMetadata",
    "NetworkSettings",
    "CreateVersionMetadataV1",
    "OperationMetadataV1",
    "Service",
    "TrafficSplit",
    "AutomaticScaling",
    "BasicScaling",
    "CpuUtilization",
    "DiskUtilization",
    "EndpointsApiService",
    "Entrypoint",
    "ManualScaling",
    "Network",
    "NetworkUtilization",
    "RequestUtilization",
    "Resources",
    "StandardSchedulerSettings",
    "Version",
    "Volume",
    "VpcAccessConnector",
    "InboundServiceType",
    "ServingStatus",
)
