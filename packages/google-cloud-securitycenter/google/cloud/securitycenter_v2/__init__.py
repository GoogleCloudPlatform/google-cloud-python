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

from google.cloud.securitycenter_v2 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.securitycenter_v2.services.security_center",
    "google.cloud.securitycenter_v2.types.access",
    "google.cloud.securitycenter_v2.types.affected_resources",
    "google.cloud.securitycenter_v2.types.agent",
    "google.cloud.securitycenter_v2.types.agent_anomaly",
    "google.cloud.securitycenter_v2.types.agent_session",
    "google.cloud.securitycenter_v2.types.ai_model",
    "google.cloud.securitycenter_v2.types.application",
    "google.cloud.securitycenter_v2.types.attack_exposure",
    "google.cloud.securitycenter_v2.types.attack_path",
    "google.cloud.securitycenter_v2.types.backup_disaster_recovery",
    "google.cloud.securitycenter_v2.types.bigquery_export",
    "google.cloud.securitycenter_v2.types.chokepoint",
    "google.cloud.securitycenter_v2.types.cloud_armor",
    "google.cloud.securitycenter_v2.types.cloud_dlp_data_profile",
    "google.cloud.securitycenter_v2.types.cloud_dlp_inspection",
    "google.cloud.securitycenter_v2.types.compliance",
    "google.cloud.securitycenter_v2.types.connection",
    "google.cloud.securitycenter_v2.types.contact_details",
    "google.cloud.securitycenter_v2.types.container",
    "google.cloud.securitycenter_v2.types.data_access_event",
    "google.cloud.securitycenter_v2.types.data_flow_event",
    "google.cloud.securitycenter_v2.types.data_retention_deletion_event",
    "google.cloud.securitycenter_v2.types.database",
    "google.cloud.securitycenter_v2.types.disk",
    "google.cloud.securitycenter_v2.types.exfiltration",
    "google.cloud.securitycenter_v2.types.external_system",
    "google.cloud.securitycenter_v2.types.file",
    "google.cloud.securitycenter_v2.types.finding",
    "google.cloud.securitycenter_v2.types.folder",
    "google.cloud.securitycenter_v2.types.group_membership",
    "google.cloud.securitycenter_v2.types.iam_binding",
    "google.cloud.securitycenter_v2.types.indicator",
    "google.cloud.securitycenter_v2.types.ip_rules",
    "google.cloud.securitycenter_v2.types.job",
    "google.cloud.securitycenter_v2.types.kernel_rootkit",
    "google.cloud.securitycenter_v2.types.kubernetes",
    "google.cloud.securitycenter_v2.types.label",
    "google.cloud.securitycenter_v2.types.load_balancer",
    "google.cloud.securitycenter_v2.types.log_entry",
    "google.cloud.securitycenter_v2.types.mitre_attack",
    "google.cloud.securitycenter_v2.types.mute_config",
    "google.cloud.securitycenter_v2.types.network",
    "google.cloud.securitycenter_v2.types.notebook",
    "google.cloud.securitycenter_v2.types.notification_config",
    "google.cloud.securitycenter_v2.types.notification_message",
    "google.cloud.securitycenter_v2.types.org_policy",
    "google.cloud.securitycenter_v2.types.process",
    "google.cloud.securitycenter_v2.types.resource",
    "google.cloud.securitycenter_v2.types.resource_value_config",
    "google.cloud.securitycenter_v2.types.security_marks",
    "google.cloud.securitycenter_v2.types.security_posture",
    "google.cloud.securitycenter_v2.types.securitycenter_service",
    "google.cloud.securitycenter_v2.types.simulation",
    "google.cloud.securitycenter_v2.types.source",
    "google.cloud.securitycenter_v2.types.toxic_combination",
    "google.cloud.securitycenter_v2.types.valued_resource",
    "google.cloud.securitycenter_v2.types.vertex_ai",
    "google.cloud.securitycenter_v2.types.vulnerability",
}


from .services.security_center import SecurityCenterAsyncClient, SecurityCenterClient
from .types.access import Access, Geolocation, ServiceAccountDelegationInfo
from .types.affected_resources import AffectedResources
from .types.agent import Agent
from .types.agent_anomaly import AgentAnomaly, DetectorReference, InvocationReference
from .types.agent_session import AgentSession
from .types.ai_model import AiModel
from .types.application import Application
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
from .types.cloud_dlp_data_profile import CloudDlpDataProfile
from .types.cloud_dlp_inspection import CloudDlpInspection
from .types.compliance import Compliance
from .types.connection import Connection
from .types.contact_details import Contact, ContactDetails
from .types.container import Container
from .types.data_access_event import DataAccessEvent
from .types.data_flow_event import DataFlowEvent
from .types.data_retention_deletion_event import DataRetentionDeletionEvent
from .types.database import Database
from .types.disk import Disk
from .types.exfiltration import ExfilResource, Exfiltration
from .types.external_system import ExternalSystem
from .types.file import File
from .types.finding import Finding
from .types.folder import Folder
from .types.group_membership import GroupMembership
from .types.iam_binding import IamBinding
from .types.indicator import Indicator
from .types.ip_rules import Allowed, Denied, IpRule, IpRules
from .types.job import Job, JobState
from .types.kernel_rootkit import KernelRootkit
from .types.kubernetes import Kubernetes
from .types.label import Label
from .types.load_balancer import LoadBalancer
from .types.log_entry import CloudLoggingEntry, LogEntry
from .types.mitre_attack import MitreAttack
from .types.mute_config import MuteConfig
from .types.network import Network
from .types.notebook import Notebook
from .types.notification_config import NotificationConfig
from .types.notification_message import NotificationMessage
from .types.org_policy import OrgPolicy
from .types.process import EnvironmentVariable, Process
from .types.resource import (
    AwsMetadata,
    AzureMetadata,
    CloudProvider,
    GcpMetadata,
    Resource,
    ResourcePath,
)
from .types.resource_value_config import ResourceValue, ResourceValueConfig
from .types.security_marks import SecurityMarks
from .types.security_posture import SecurityPosture
from .types.securitycenter_service import (
    BatchCreateResourceValueConfigsRequest,
    BatchCreateResourceValueConfigsResponse,
    BigQueryDestination,
    BulkMuteFindingsRequest,
    BulkMuteFindingsResponse,
    CreateBigQueryExportRequest,
    CreateFindingRequest,
    CreateMuteConfigRequest,
    CreateNotificationConfigRequest,
    CreateResourceValueConfigRequest,
    CreateSourceRequest,
    DeleteBigQueryExportRequest,
    DeleteMuteConfigRequest,
    DeleteNotificationConfigRequest,
    DeleteResourceValueConfigRequest,
    ExportFindingsMetadata,
    ExportFindingsResponse,
    GetBigQueryExportRequest,
    GetMuteConfigRequest,
    GetNotificationConfigRequest,
    GetResourceValueConfigRequest,
    GetSimulationRequest,
    GetSourceRequest,
    GetValuedResourceRequest,
    GroupFindingsRequest,
    GroupFindingsResponse,
    GroupResult,
    ListAttackPathsRequest,
    ListAttackPathsResponse,
    ListBigQueryExportsRequest,
    ListBigQueryExportsResponse,
    ListFindingsRequest,
    ListFindingsResponse,
    ListMuteConfigsRequest,
    ListMuteConfigsResponse,
    ListNotificationConfigsRequest,
    ListNotificationConfigsResponse,
    ListResourceValueConfigsRequest,
    ListResourceValueConfigsResponse,
    ListSourcesRequest,
    ListSourcesResponse,
    ListValuedResourcesRequest,
    ListValuedResourcesResponse,
    SetFindingStateRequest,
    SetMuteRequest,
    UpdateBigQueryExportRequest,
    UpdateExternalSystemRequest,
    UpdateFindingRequest,
    UpdateMuteConfigRequest,
    UpdateNotificationConfigRequest,
    UpdateResourceValueConfigRequest,
    UpdateSecurityMarksRequest,
    UpdateSourceRequest,
)
from .types.simulation import Simulation
from .types.source import Source
from .types.toxic_combination import ToxicCombination
from .types.valued_resource import ResourceValueConfigMetadata, ValuedResource
from .types.vertex_ai import VertexAi
from .types.vulnerability import (
    Cve,
    Cvssv3,
    Cwe,
    Package,
    Reference,
    SecurityBulletin,
    Vulnerability,
)

__all__ = (
    "SecurityCenterAsyncClient",
    "Access",
    "AdaptiveProtection",
    "AffectedResources",
    "Agent",
    "AgentAnomaly",
    "AgentSession",
    "AiModel",
    "Allowed",
    "Application",
    "Attack",
    "AttackExposure",
    "AttackPath",
    "AwsMetadata",
    "AzureMetadata",
    "BackupDisasterRecovery",
    "BatchCreateResourceValueConfigsRequest",
    "BatchCreateResourceValueConfigsResponse",
    "BigQueryDestination",
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
    "CreateFindingRequest",
    "CreateMuteConfigRequest",
    "CreateNotificationConfigRequest",
    "CreateResourceValueConfigRequest",
    "CreateSourceRequest",
    "Cve",
    "Cvssv3",
    "Cwe",
    "DataAccessEvent",
    "DataFlowEvent",
    "DataRetentionDeletionEvent",
    "Database",
    "DeleteBigQueryExportRequest",
    "DeleteMuteConfigRequest",
    "DeleteNotificationConfigRequest",
    "DeleteResourceValueConfigRequest",
    "Denied",
    "DetectorReference",
    "Disk",
    "EnvironmentVariable",
    "ExfilResource",
    "Exfiltration",
    "ExportFindingsMetadata",
    "ExportFindingsResponse",
    "ExternalSystem",
    "File",
    "Finding",
    "Folder",
    "GcpMetadata",
    "Geolocation",
    "GetBigQueryExportRequest",
    "GetMuteConfigRequest",
    "GetNotificationConfigRequest",
    "GetResourceValueConfigRequest",
    "GetSimulationRequest",
    "GetSourceRequest",
    "GetValuedResourceRequest",
    "GroupFindingsRequest",
    "GroupFindingsResponse",
    "GroupMembership",
    "GroupResult",
    "IamBinding",
    "Indicator",
    "InvocationReference",
    "IpRule",
    "IpRules",
    "Job",
    "JobState",
    "KernelRootkit",
    "Kubernetes",
    "Label",
    "ListAttackPathsRequest",
    "ListAttackPathsResponse",
    "ListBigQueryExportsRequest",
    "ListBigQueryExportsResponse",
    "ListFindingsRequest",
    "ListFindingsResponse",
    "ListMuteConfigsRequest",
    "ListMuteConfigsResponse",
    "ListNotificationConfigsRequest",
    "ListNotificationConfigsResponse",
    "ListResourceValueConfigsRequest",
    "ListResourceValueConfigsResponse",
    "ListSourcesRequest",
    "ListSourcesResponse",
    "ListValuedResourcesRequest",
    "ListValuedResourcesResponse",
    "LoadBalancer",
    "LogEntry",
    "MitreAttack",
    "MuteConfig",
    "Network",
    "Notebook",
    "NotificationConfig",
    "NotificationMessage",
    "OrgPolicy",
    "Package",
    "Process",
    "Reference",
    "Requests",
    "Resource",
    "ResourcePath",
    "ResourceValue",
    "ResourceValueConfig",
    "ResourceValueConfigMetadata",
    "SecurityBulletin",
    "SecurityCenterClient",
    "SecurityMarks",
    "SecurityPolicy",
    "SecurityPosture",
    "ServiceAccountDelegationInfo",
    "SetFindingStateRequest",
    "SetMuteRequest",
    "Simulation",
    "Source",
    "ToxicCombination",
    "UpdateBigQueryExportRequest",
    "UpdateExternalSystemRequest",
    "UpdateFindingRequest",
    "UpdateMuteConfigRequest",
    "UpdateNotificationConfigRequest",
    "UpdateResourceValueConfigRequest",
    "UpdateSecurityMarksRequest",
    "UpdateSourceRequest",
    "ValuedResource",
    "VertexAi",
    "Vulnerability",
)

api_core.check_python_version("google.cloud.securitycenter_v2")
api_core.check_dependency_versions("google.cloud.securitycenter_v2")
