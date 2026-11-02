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

from google.cloud.securitycenter_v1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.securitycenter_v1.services.security_center",
    "google.cloud.securitycenter_v1.types.access",
    "google.cloud.securitycenter_v1.types.agent",
    "google.cloud.securitycenter_v1.types.agent_anomaly",
    "google.cloud.securitycenter_v1.types.agent_session",
    "google.cloud.securitycenter_v1.types.application",
    "google.cloud.securitycenter_v1.types.asset",
    "google.cloud.securitycenter_v1.types.attack_exposure",
    "google.cloud.securitycenter_v1.types.attack_path",
    "google.cloud.securitycenter_v1.types.backup_disaster_recovery",
    "google.cloud.securitycenter_v1.types.bigquery_export",
    "google.cloud.securitycenter_v1.types.chokepoint",
    "google.cloud.securitycenter_v1.types.cloud_armor",
    "google.cloud.securitycenter_v1.types.cloud_dlp_data_profile",
    "google.cloud.securitycenter_v1.types.cloud_dlp_inspection",
    "google.cloud.securitycenter_v1.types.compliance",
    "google.cloud.securitycenter_v1.types.connection",
    "google.cloud.securitycenter_v1.types.contact_details",
    "google.cloud.securitycenter_v1.types.container",
    "google.cloud.securitycenter_v1.types.database",
    "google.cloud.securitycenter_v1.types.effective_event_threat_detection_custom_module",
    "google.cloud.securitycenter_v1.types.effective_security_health_analytics_custom_module",
    "google.cloud.securitycenter_v1.types.event_threat_detection_custom_module",
    "google.cloud.securitycenter_v1.types.event_threat_detection_custom_module_validation_errors",
    "google.cloud.securitycenter_v1.types.exfiltration",
    "google.cloud.securitycenter_v1.types.external_exposure",
    "google.cloud.securitycenter_v1.types.external_system",
    "google.cloud.securitycenter_v1.types.file",
    "google.cloud.securitycenter_v1.types.finding",
    "google.cloud.securitycenter_v1.types.folder",
    "google.cloud.securitycenter_v1.types.group_membership",
    "google.cloud.securitycenter_v1.types.iam_binding",
    "google.cloud.securitycenter_v1.types.indicator",
    "google.cloud.securitycenter_v1.types.kernel_rootkit",
    "google.cloud.securitycenter_v1.types.kubernetes",
    "google.cloud.securitycenter_v1.types.label",
    "google.cloud.securitycenter_v1.types.load_balancer",
    "google.cloud.securitycenter_v1.types.log_entry",
    "google.cloud.securitycenter_v1.types.mitre_attack",
    "google.cloud.securitycenter_v1.types.mute_config",
    "google.cloud.securitycenter_v1.types.notebook",
    "google.cloud.securitycenter_v1.types.notification_config",
    "google.cloud.securitycenter_v1.types.notification_message",
    "google.cloud.securitycenter_v1.types.org_policy",
    "google.cloud.securitycenter_v1.types.organization_settings",
    "google.cloud.securitycenter_v1.types.process",
    "google.cloud.securitycenter_v1.types.resource",
    "google.cloud.securitycenter_v1.types.resource_value_config",
    "google.cloud.securitycenter_v1.types.run_asset_discovery_response",
    "google.cloud.securitycenter_v1.types.security_health_analytics_custom_config",
    "google.cloud.securitycenter_v1.types.security_health_analytics_custom_module",
    "google.cloud.securitycenter_v1.types.security_marks",
    "google.cloud.securitycenter_v1.types.security_posture",
    "google.cloud.securitycenter_v1.types.securitycenter_service",
    "google.cloud.securitycenter_v1.types.simulation",
    "google.cloud.securitycenter_v1.types.source",
    "google.cloud.securitycenter_v1.types.toxic_combination",
    "google.cloud.securitycenter_v1.types.valued_resource",
    "google.cloud.securitycenter_v1.types.vulnerability",
}


from .services.security_center import SecurityCenterAsyncClient, SecurityCenterClient
from .types.access import Access, Geolocation, ServiceAccountDelegationInfo
from .types.agent import Agent
from .types.agent_anomaly import AgentAnomaly, DetectorReference, InvocationReference
from .types.agent_session import AgentSession
from .types.application import Application
from .types.asset import Asset
from .types.attack_exposure import AttackExposure
from .types.attack_path import AttackPath
from .types.backup_disaster_recovery import BackupDisasterRecovery
from .types.bigquery_export import BigQueryExport
from .types.chokepoint import Chokepoint
from .types.cloud_armor import (
    AdaptiveProtection,
    Attack,
    CloudArmor,
    Requests,
    SecurityPolicy,
)
from .types.cloud_dlp_data_profile import (
    CloudDlpDataProfile,
    InfoType,
    SensitivityScore,
)
from .types.cloud_dlp_inspection import CloudDlpInspection
from .types.compliance import Compliance
from .types.connection import Connection
from .types.contact_details import Contact, ContactDetails
from .types.container import Container
from .types.database import Database
from .types.effective_event_threat_detection_custom_module import (
    EffectiveEventThreatDetectionCustomModule,
)
from .types.effective_security_health_analytics_custom_module import (
    EffectiveSecurityHealthAnalyticsCustomModule,
)
from .types.event_threat_detection_custom_module import EventThreatDetectionCustomModule
from .types.event_threat_detection_custom_module_validation_errors import (
    CustomModuleValidationError,
    CustomModuleValidationErrors,
    Position,
)
from .types.exfiltration import ExfilResource, Exfiltration
from .types.external_exposure import ExternalExposure
from .types.external_system import ExternalSystem
from .types.file import File
from .types.finding import Finding
from .types.folder import Folder
from .types.group_membership import GroupMembership
from .types.iam_binding import IamBinding
from .types.indicator import Indicator
from .types.kernel_rootkit import KernelRootkit
from .types.kubernetes import Kubernetes
from .types.label import Label
from .types.load_balancer import LoadBalancer
from .types.log_entry import CloudLoggingEntry, LogEntry
from .types.mitre_attack import MitreAttack
from .types.mute_config import MuteConfig
from .types.notebook import Notebook
from .types.notification_config import NotificationConfig
from .types.notification_message import NotificationMessage
from .types.org_policy import OrgPolicy
from .types.organization_settings import OrganizationSettings
from .types.process import EnvironmentVariable, Process
from .types.resource import (
    AwsMetadata,
    AzureMetadata,
    CloudProvider,
    Resource,
    ResourcePath,
)
from .types.resource_value_config import ResourceValue, ResourceValueConfig
from .types.run_asset_discovery_response import RunAssetDiscoveryResponse
from .types.security_health_analytics_custom_config import CustomConfig
from .types.security_health_analytics_custom_module import (
    SecurityHealthAnalyticsCustomModule,
)
from .types.security_marks import SecurityMarks
from .types.security_posture import SecurityPosture
from .types.securitycenter_service import (
    BatchCreateResourceValueConfigsRequest,
    BatchCreateResourceValueConfigsResponse,
    BulkMuteFindingsRequest,
    BulkMuteFindingsResponse,
    CreateBigQueryExportRequest,
    CreateEventThreatDetectionCustomModuleRequest,
    CreateFindingRequest,
    CreateMuteConfigRequest,
    CreateNotificationConfigRequest,
    CreateResourceValueConfigRequest,
    CreateSecurityHealthAnalyticsCustomModuleRequest,
    CreateSourceRequest,
    DeleteBigQueryExportRequest,
    DeleteEventThreatDetectionCustomModuleRequest,
    DeleteMuteConfigRequest,
    DeleteNotificationConfigRequest,
    DeleteResourceValueConfigRequest,
    DeleteSecurityHealthAnalyticsCustomModuleRequest,
    GetBigQueryExportRequest,
    GetEffectiveEventThreatDetectionCustomModuleRequest,
    GetEffectiveSecurityHealthAnalyticsCustomModuleRequest,
    GetEventThreatDetectionCustomModuleRequest,
    GetMuteConfigRequest,
    GetNotificationConfigRequest,
    GetOrganizationSettingsRequest,
    GetResourceValueConfigRequest,
    GetSecurityHealthAnalyticsCustomModuleRequest,
    GetSimulationRequest,
    GetSourceRequest,
    GetValuedResourceRequest,
    GroupAssetsRequest,
    GroupAssetsResponse,
    GroupFindingsRequest,
    GroupFindingsResponse,
    GroupResult,
    ListAssetsRequest,
    ListAssetsResponse,
    ListAttackPathsRequest,
    ListAttackPathsResponse,
    ListBigQueryExportsRequest,
    ListBigQueryExportsResponse,
    ListDescendantEventThreatDetectionCustomModulesRequest,
    ListDescendantEventThreatDetectionCustomModulesResponse,
    ListDescendantSecurityHealthAnalyticsCustomModulesRequest,
    ListDescendantSecurityHealthAnalyticsCustomModulesResponse,
    ListEffectiveEventThreatDetectionCustomModulesRequest,
    ListEffectiveEventThreatDetectionCustomModulesResponse,
    ListEffectiveSecurityHealthAnalyticsCustomModulesRequest,
    ListEffectiveSecurityHealthAnalyticsCustomModulesResponse,
    ListEventThreatDetectionCustomModulesRequest,
    ListEventThreatDetectionCustomModulesResponse,
    ListFindingsRequest,
    ListFindingsResponse,
    ListMuteConfigsRequest,
    ListMuteConfigsResponse,
    ListNotificationConfigsRequest,
    ListNotificationConfigsResponse,
    ListResourceValueConfigsRequest,
    ListResourceValueConfigsResponse,
    ListSecurityHealthAnalyticsCustomModulesRequest,
    ListSecurityHealthAnalyticsCustomModulesResponse,
    ListSourcesRequest,
    ListSourcesResponse,
    ListValuedResourcesRequest,
    ListValuedResourcesResponse,
    RunAssetDiscoveryRequest,
    SetFindingStateRequest,
    SetMuteRequest,
    SimulateSecurityHealthAnalyticsCustomModuleRequest,
    SimulateSecurityHealthAnalyticsCustomModuleResponse,
    UpdateBigQueryExportRequest,
    UpdateEventThreatDetectionCustomModuleRequest,
    UpdateExternalSystemRequest,
    UpdateFindingRequest,
    UpdateMuteConfigRequest,
    UpdateNotificationConfigRequest,
    UpdateOrganizationSettingsRequest,
    UpdateResourceValueConfigRequest,
    UpdateSecurityHealthAnalyticsCustomModuleRequest,
    UpdateSecurityMarksRequest,
    UpdateSourceRequest,
    ValidateEventThreatDetectionCustomModuleRequest,
    ValidateEventThreatDetectionCustomModuleResponse,
)
from .types.simulation import Simulation
from .types.source import Source
from .types.toxic_combination import ToxicCombination
from .types.valued_resource import ResourceValueConfigMetadata, ValuedResource
from .types.vulnerability import (
    Cve,
    Cvssv3,
    Package,
    Reference,
    SecurityBulletin,
    Vulnerability,
)

__all__ = (
    "SecurityCenterAsyncClient",
    "Access",
    "AdaptiveProtection",
    "Agent",
    "AgentAnomaly",
    "AgentSession",
    "Application",
    "Asset",
    "Attack",
    "AttackExposure",
    "AttackPath",
    "AwsMetadata",
    "AzureMetadata",
    "BackupDisasterRecovery",
    "BatchCreateResourceValueConfigsRequest",
    "BatchCreateResourceValueConfigsResponse",
    "BigQueryExport",
    "BulkMuteFindingsRequest",
    "BulkMuteFindingsResponse",
    "Chokepoint",
    "CloudArmor",
    "CloudDlpDataProfile",
    "CloudDlpInspection",
    "CloudLoggingEntry",
    "CloudProvider",
    "Compliance",
    "Connection",
    "Contact",
    "ContactDetails",
    "Container",
    "CreateBigQueryExportRequest",
    "CreateEventThreatDetectionCustomModuleRequest",
    "CreateFindingRequest",
    "CreateMuteConfigRequest",
    "CreateNotificationConfigRequest",
    "CreateResourceValueConfigRequest",
    "CreateSecurityHealthAnalyticsCustomModuleRequest",
    "CreateSourceRequest",
    "CustomConfig",
    "CustomModuleValidationError",
    "CustomModuleValidationErrors",
    "Cve",
    "Cvssv3",
    "Database",
    "DeleteBigQueryExportRequest",
    "DeleteEventThreatDetectionCustomModuleRequest",
    "DeleteMuteConfigRequest",
    "DeleteNotificationConfigRequest",
    "DeleteResourceValueConfigRequest",
    "DeleteSecurityHealthAnalyticsCustomModuleRequest",
    "DetectorReference",
    "EffectiveEventThreatDetectionCustomModule",
    "EffectiveSecurityHealthAnalyticsCustomModule",
    "EnvironmentVariable",
    "EventThreatDetectionCustomModule",
    "ExfilResource",
    "Exfiltration",
    "ExternalExposure",
    "ExternalSystem",
    "File",
    "Finding",
    "Folder",
    "Geolocation",
    "GetBigQueryExportRequest",
    "GetEffectiveEventThreatDetectionCustomModuleRequest",
    "GetEffectiveSecurityHealthAnalyticsCustomModuleRequest",
    "GetEventThreatDetectionCustomModuleRequest",
    "GetMuteConfigRequest",
    "GetNotificationConfigRequest",
    "GetOrganizationSettingsRequest",
    "GetResourceValueConfigRequest",
    "GetSecurityHealthAnalyticsCustomModuleRequest",
    "GetSimulationRequest",
    "GetSourceRequest",
    "GetValuedResourceRequest",
    "GroupAssetsRequest",
    "GroupAssetsResponse",
    "GroupFindingsRequest",
    "GroupFindingsResponse",
    "GroupMembership",
    "GroupResult",
    "IamBinding",
    "Indicator",
    "InfoType",
    "InvocationReference",
    "KernelRootkit",
    "Kubernetes",
    "Label",
    "ListAssetsRequest",
    "ListAssetsResponse",
    "ListAttackPathsRequest",
    "ListAttackPathsResponse",
    "ListBigQueryExportsRequest",
    "ListBigQueryExportsResponse",
    "ListDescendantEventThreatDetectionCustomModulesRequest",
    "ListDescendantEventThreatDetectionCustomModulesResponse",
    "ListDescendantSecurityHealthAnalyticsCustomModulesRequest",
    "ListDescendantSecurityHealthAnalyticsCustomModulesResponse",
    "ListEffectiveEventThreatDetectionCustomModulesRequest",
    "ListEffectiveEventThreatDetectionCustomModulesResponse",
    "ListEffectiveSecurityHealthAnalyticsCustomModulesRequest",
    "ListEffectiveSecurityHealthAnalyticsCustomModulesResponse",
    "ListEventThreatDetectionCustomModulesRequest",
    "ListEventThreatDetectionCustomModulesResponse",
    "ListFindingsRequest",
    "ListFindingsResponse",
    "ListMuteConfigsRequest",
    "ListMuteConfigsResponse",
    "ListNotificationConfigsRequest",
    "ListNotificationConfigsResponse",
    "ListResourceValueConfigsRequest",
    "ListResourceValueConfigsResponse",
    "ListSecurityHealthAnalyticsCustomModulesRequest",
    "ListSecurityHealthAnalyticsCustomModulesResponse",
    "ListSourcesRequest",
    "ListSourcesResponse",
    "ListValuedResourcesRequest",
    "ListValuedResourcesResponse",
    "LoadBalancer",
    "LogEntry",
    "MitreAttack",
    "MuteConfig",
    "Notebook",
    "NotificationConfig",
    "NotificationMessage",
    "OrgPolicy",
    "OrganizationSettings",
    "Package",
    "Position",
    "Process",
    "Reference",
    "Requests",
    "Resource",
    "ResourcePath",
    "ResourceValue",
    "ResourceValueConfig",
    "ResourceValueConfigMetadata",
    "RunAssetDiscoveryRequest",
    "RunAssetDiscoveryResponse",
    "SecurityBulletin",
    "SecurityCenterClient",
    "SecurityHealthAnalyticsCustomModule",
    "SecurityMarks",
    "SecurityPolicy",
    "SecurityPosture",
    "SensitivityScore",
    "ServiceAccountDelegationInfo",
    "SetFindingStateRequest",
    "SetMuteRequest",
    "SimulateSecurityHealthAnalyticsCustomModuleRequest",
    "SimulateSecurityHealthAnalyticsCustomModuleResponse",
    "Simulation",
    "Source",
    "ToxicCombination",
    "UpdateBigQueryExportRequest",
    "UpdateEventThreatDetectionCustomModuleRequest",
    "UpdateExternalSystemRequest",
    "UpdateFindingRequest",
    "UpdateMuteConfigRequest",
    "UpdateNotificationConfigRequest",
    "UpdateOrganizationSettingsRequest",
    "UpdateResourceValueConfigRequest",
    "UpdateSecurityHealthAnalyticsCustomModuleRequest",
    "UpdateSecurityMarksRequest",
    "UpdateSourceRequest",
    "ValidateEventThreatDetectionCustomModuleRequest",
    "ValidateEventThreatDetectionCustomModuleResponse",
    "ValuedResource",
    "Vulnerability",
)

api_core.check_python_version("google.cloud.securitycenter_v1")
api_core.check_dependency_versions("google.cloud.securitycenter_v1")
