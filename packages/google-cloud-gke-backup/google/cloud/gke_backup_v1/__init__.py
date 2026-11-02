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

from google.cloud.gke_backup_v1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.gke_backup_v1.services.backup_for_gke",
    "google.cloud.gke_backup_v1.types.backup",
    "google.cloud.gke_backup_v1.types.backup_channel",
    "google.cloud.gke_backup_v1.types.backup_plan",
    "google.cloud.gke_backup_v1.types.backup_plan_binding",
    "google.cloud.gke_backup_v1.types.common",
    "google.cloud.gke_backup_v1.types.gkebackup",
    "google.cloud.gke_backup_v1.types.restore",
    "google.cloud.gke_backup_v1.types.restore_channel",
    "google.cloud.gke_backup_v1.types.restore_plan",
    "google.cloud.gke_backup_v1.types.restore_plan_binding",
    "google.cloud.gke_backup_v1.types.volume",
}


from .services.backup_for_gke import BackupForGKEAsyncClient, BackupForGKEClient
from .types.backup import Backup
from .types.backup_channel import BackupChannel
from .types.backup_plan import BackupPlan, ExclusionWindow, RpoConfig
from .types.backup_plan_binding import BackupPlanBinding
from .types.common import (
    EncryptionKey,
    NamespacedName,
    NamespacedNames,
    Namespaces,
    VolumeTypeEnum,
)
from .types.gkebackup import (
    CreateBackupChannelRequest,
    CreateBackupPlanRequest,
    CreateBackupRequest,
    CreateRestoreChannelRequest,
    CreateRestorePlanRequest,
    CreateRestoreRequest,
    DeleteBackupChannelRequest,
    DeleteBackupPlanRequest,
    DeleteBackupRequest,
    DeleteRestoreChannelRequest,
    DeleteRestorePlanRequest,
    DeleteRestoreRequest,
    GetBackupChannelRequest,
    GetBackupIndexDownloadUrlRequest,
    GetBackupIndexDownloadUrlResponse,
    GetBackupPlanBindingRequest,
    GetBackupPlanRequest,
    GetBackupRequest,
    GetRestoreChannelRequest,
    GetRestorePlanBindingRequest,
    GetRestorePlanRequest,
    GetRestoreRequest,
    GetVolumeBackupRequest,
    GetVolumeRestoreRequest,
    ListBackupChannelsRequest,
    ListBackupChannelsResponse,
    ListBackupPlanBindingsRequest,
    ListBackupPlanBindingsResponse,
    ListBackupPlansRequest,
    ListBackupPlansResponse,
    ListBackupsRequest,
    ListBackupsResponse,
    ListRestoreChannelsRequest,
    ListRestoreChannelsResponse,
    ListRestorePlanBindingsRequest,
    ListRestorePlanBindingsResponse,
    ListRestorePlansRequest,
    ListRestorePlansResponse,
    ListRestoresRequest,
    ListRestoresResponse,
    ListVolumeBackupsRequest,
    ListVolumeBackupsResponse,
    ListVolumeRestoresRequest,
    ListVolumeRestoresResponse,
    OperationMetadata,
    UpdateBackupChannelRequest,
    UpdateBackupPlanRequest,
    UpdateBackupRequest,
    UpdateRestoreChannelRequest,
    UpdateRestorePlanRequest,
    UpdateRestoreRequest,
)
from .types.restore import (
    ResourceSelector,
    Restore,
    RestoreConfig,
    VolumeDataRestorePolicyOverride,
)
from .types.restore_channel import RestoreChannel
from .types.restore_plan import RestorePlan
from .types.restore_plan_binding import RestorePlanBinding
from .types.volume import VolumeBackup, VolumeRestore

__all__ = (
    "BackupForGKEAsyncClient",
    "Backup",
    "BackupChannel",
    "BackupForGKEClient",
    "BackupPlan",
    "BackupPlanBinding",
    "CreateBackupChannelRequest",
    "CreateBackupPlanRequest",
    "CreateBackupRequest",
    "CreateRestoreChannelRequest",
    "CreateRestorePlanRequest",
    "CreateRestoreRequest",
    "DeleteBackupChannelRequest",
    "DeleteBackupPlanRequest",
    "DeleteBackupRequest",
    "DeleteRestoreChannelRequest",
    "DeleteRestorePlanRequest",
    "DeleteRestoreRequest",
    "EncryptionKey",
    "ExclusionWindow",
    "GetBackupChannelRequest",
    "GetBackupIndexDownloadUrlRequest",
    "GetBackupIndexDownloadUrlResponse",
    "GetBackupPlanBindingRequest",
    "GetBackupPlanRequest",
    "GetBackupRequest",
    "GetRestoreChannelRequest",
    "GetRestorePlanBindingRequest",
    "GetRestorePlanRequest",
    "GetRestoreRequest",
    "GetVolumeBackupRequest",
    "GetVolumeRestoreRequest",
    "ListBackupChannelsRequest",
    "ListBackupChannelsResponse",
    "ListBackupPlanBindingsRequest",
    "ListBackupPlanBindingsResponse",
    "ListBackupPlansRequest",
    "ListBackupPlansResponse",
    "ListBackupsRequest",
    "ListBackupsResponse",
    "ListRestoreChannelsRequest",
    "ListRestoreChannelsResponse",
    "ListRestorePlanBindingsRequest",
    "ListRestorePlanBindingsResponse",
    "ListRestorePlansRequest",
    "ListRestorePlansResponse",
    "ListRestoresRequest",
    "ListRestoresResponse",
    "ListVolumeBackupsRequest",
    "ListVolumeBackupsResponse",
    "ListVolumeRestoresRequest",
    "ListVolumeRestoresResponse",
    "NamespacedName",
    "NamespacedNames",
    "Namespaces",
    "OperationMetadata",
    "ResourceSelector",
    "Restore",
    "RestoreChannel",
    "RestoreConfig",
    "RestorePlan",
    "RestorePlanBinding",
    "RpoConfig",
    "UpdateBackupChannelRequest",
    "UpdateBackupPlanRequest",
    "UpdateBackupRequest",
    "UpdateRestoreChannelRequest",
    "UpdateRestorePlanRequest",
    "UpdateRestoreRequest",
    "VolumeBackup",
    "VolumeDataRestorePolicyOverride",
    "VolumeRestore",
    "VolumeTypeEnum",
)

api_core.check_python_version("google.cloud.gke_backup_v1")
api_core.check_dependency_versions("google.cloud.gke_backup_v1")
