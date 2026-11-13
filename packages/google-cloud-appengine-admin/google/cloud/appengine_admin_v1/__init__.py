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

from google.cloud.appengine_admin_v1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.appengine_admin_v1.services.applications",
    "google.cloud.appengine_admin_v1.services.authorized_certificates",
    "google.cloud.appengine_admin_v1.services.authorized_domains",
    "google.cloud.appengine_admin_v1.services.domain_mappings",
    "google.cloud.appengine_admin_v1.services.firewall",
    "google.cloud.appengine_admin_v1.services.instances",
    "google.cloud.appengine_admin_v1.services.services",
    "google.cloud.appengine_admin_v1.services.versions",
    "google.cloud.appengine_admin_v1.types.app_yaml",
    "google.cloud.appengine_admin_v1.types.appengine",
    "google.cloud.appengine_admin_v1.types.application",
    "google.cloud.appengine_admin_v1.types.audit_data",
    "google.cloud.appengine_admin_v1.types.certificate",
    "google.cloud.appengine_admin_v1.types.deploy",
    "google.cloud.appengine_admin_v1.types.deployed_files",
    "google.cloud.appengine_admin_v1.types.domain",
    "google.cloud.appengine_admin_v1.types.domain_mapping",
    "google.cloud.appengine_admin_v1.types.firewall",
    "google.cloud.appengine_admin_v1.types.instance",
    "google.cloud.appengine_admin_v1.types.location",
    "google.cloud.appengine_admin_v1.types.network_settings",
    "google.cloud.appengine_admin_v1.types.operation",
    "google.cloud.appengine_admin_v1.types.service",
    "google.cloud.appengine_admin_v1.types.version",
}


from .services.applications import ApplicationsAsyncClient, ApplicationsClient
from .services.authorized_certificates import (
    AuthorizedCertificatesAsyncClient,
    AuthorizedCertificatesClient,
)
from .services.authorized_domains import (
    AuthorizedDomainsAsyncClient,
    AuthorizedDomainsClient,
)
from .services.domain_mappings import DomainMappingsAsyncClient, DomainMappingsClient
from .services.firewall import FirewallAsyncClient, FirewallClient
from .services.instances import InstancesAsyncClient, InstancesClient
from .services.services import ServicesAsyncClient, ServicesClient
from .services.versions import VersionsAsyncClient, VersionsClient
from .types.app_yaml import (
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
from .types.appengine import (
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
from .types.application import Application, UrlDispatchRule
from .types.audit_data import AuditData, CreateVersionMethod, UpdateServiceMethod
from .types.certificate import (
    AuthorizedCertificate,
    CertificateRawData,
    ManagedCertificate,
    ManagementStatus,
)
from .types.deploy import (
    CloudBuildOptions,
    ContainerInfo,
    Deployment,
    FileInfo,
    ZipInfo,
)
from .types.domain import AuthorizedDomain
from .types.domain_mapping import DomainMapping, ResourceRecord, SslSettings
from .types.firewall import FirewallRule
from .types.instance import Instance
from .types.location import LocationMetadata
from .types.network_settings import NetworkSettings
from .types.operation import CreateVersionMetadataV1, OperationMetadataV1
from .types.service import Service, TrafficSplit
from .types.version import (
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
    "ApplicationsAsyncClient",
    "AuthorizedCertificatesAsyncClient",
    "AuthorizedDomainsAsyncClient",
    "DomainMappingsAsyncClient",
    "FirewallAsyncClient",
    "InstancesAsyncClient",
    "ServicesAsyncClient",
    "VersionsAsyncClient",
    "ApiConfigHandler",
    "ApiEndpointHandler",
    "Application",
    "ApplicationsClient",
    "AuditData",
    "AuthFailAction",
    "AuthorizedCertificate",
    "AuthorizedCertificateView",
    "AuthorizedCertificatesClient",
    "AuthorizedDomain",
    "AuthorizedDomainsClient",
    "AutomaticScaling",
    "BasicScaling",
    "BatchUpdateIngressRulesRequest",
    "BatchUpdateIngressRulesResponse",
    "CertificateRawData",
    "CloudBuildOptions",
    "ContainerInfo",
    "CpuUtilization",
    "CreateApplicationRequest",
    "CreateAuthorizedCertificateRequest",
    "CreateDomainMappingRequest",
    "CreateIngressRuleRequest",
    "CreateVersionMetadataV1",
    "CreateVersionMethod",
    "CreateVersionRequest",
    "DebugInstanceRequest",
    "DeleteAuthorizedCertificateRequest",
    "DeleteDomainMappingRequest",
    "DeleteIngressRuleRequest",
    "DeleteInstanceRequest",
    "DeleteServiceRequest",
    "DeleteVersionRequest",
    "Deployment",
    "DiskUtilization",
    "DomainMapping",
    "DomainMappingsClient",
    "DomainOverrideStrategy",
    "EndpointsApiService",
    "Entrypoint",
    "ErrorHandler",
    "FileInfo",
    "FirewallClient",
    "FirewallRule",
    "GetApplicationRequest",
    "GetAuthorizedCertificateRequest",
    "GetDomainMappingRequest",
    "GetIngressRuleRequest",
    "GetInstanceRequest",
    "GetServiceRequest",
    "GetVersionRequest",
    "HealthCheck",
    "InboundServiceType",
    "Instance",
    "InstancesClient",
    "Library",
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
    "LivenessCheck",
    "LocationMetadata",
    "LoginRequirement",
    "ManagedCertificate",
    "ManagementStatus",
    "ManualScaling",
    "Network",
    "NetworkSettings",
    "NetworkUtilization",
    "OperationMetadataV1",
    "ReadinessCheck",
    "RepairApplicationRequest",
    "RequestUtilization",
    "ResourceRecord",
    "Resources",
    "ScriptHandler",
    "SecurityLevel",
    "Service",
    "ServicesClient",
    "ServingStatus",
    "SslSettings",
    "StandardSchedulerSettings",
    "StaticFilesHandler",
    "TrafficSplit",
    "UpdateApplicationRequest",
    "UpdateAuthorizedCertificateRequest",
    "UpdateDomainMappingRequest",
    "UpdateIngressRuleRequest",
    "UpdateServiceMethod",
    "UpdateServiceRequest",
    "UpdateVersionRequest",
    "UrlDispatchRule",
    "UrlMap",
    "Version",
    "VersionView",
    "VersionsClient",
    "Volume",
    "VpcAccessConnector",
    "ZipInfo",
)

api_core.check_python_version("google.cloud.appengine_admin_v1")
api_core.check_dependency_versions("google.cloud.appengine_admin_v1")
