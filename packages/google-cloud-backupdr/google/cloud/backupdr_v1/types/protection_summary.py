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
from __future__ import annotations

from typing import MutableMapping, MutableSequence

import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.backupdr.v1",
    manifest={
        "ListResourceBackupConfigsRequest",
        "ListResourceBackupConfigsResponse",
        "ResourceBackupConfig",
        "BackupConfigDetails",
        "PitrSettings",
        "BackupDrTemplateConfig",
        "BackupDrPlanConfig",
        "BackupDrPlanRule",
        "BackupLocation",
    },
)


class ListResourceBackupConfigsRequest(proto.Message):
    r"""Request for ListResourceBackupConfigs.

    Attributes:
        parent (str):
            Required. The project and location for which to retrieve
            resource backup configs. Format:
            'projects/{project_id}/locations/{location}'. In Google
            Cloud Backup and DR, locations map to Google Cloud regions,
            for example **us-central1**.
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will use 100 as default.
            Maximum value is 500 and values above 500 will
            be coerced to 500.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. Filtering results.
        order_by (str):
            Optional. Hint for how to order the results.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListResourceBackupConfigsResponse(proto.Message):
    r"""Response for ListResourceBackupConfigs.

    Attributes:
        resource_backup_configs (MutableSequence[google.cloud.backupdr_v1.types.ResourceBackupConfig]):
            The list of ResourceBackupConfigs for the
            specified scope.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
    """

    @property
    def raw_page(self):
        return self

    resource_backup_configs: MutableSequence["ResourceBackupConfig"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="ResourceBackupConfig",
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ResourceBackupConfig(proto.Message):
    r"""ResourceBackupConfig represents a resource along with its
    backup configurations.

    Attributes:
        name (str):
            Identifier. The resource name of the
            ResourceBackupConfig. Format:

            projects/{project}/locations/{location}/resourceBackupConfigs/{uid}
        uid (str):
            Output only. The unique identifier of the
            resource backup config.
        target_resource (str):
            Output only. The `full resource
            name <https://cloud.google.com/asset-inventory/docs/resource-name-format>`__
            of the cloud resource that this configuration applies to.
            Supported resource types are
            [ResourceBackupConfig.ResourceType][google.cloud.backupdr.v1.ResourceBackupConfig.ResourceType].
        target_resource_display_name (str):
            Output only. The human friendly name of the
            target resource.
        target_resource_type (google.cloud.backupdr_v1.types.ResourceBackupConfig.ResourceType):
            Output only. The type of the target resource.
        target_resource_labels (MutableMapping[str, str]):
            Labels associated with the target resource.
        backup_configs_details (MutableSequence[google.cloud.backupdr_v1.types.BackupConfigDetails]):
            Backup configurations applying to the target
            resource, including those targeting its
            related/child resources. For example, backup
            configuration applicable to Compute Engine disks
            will be populated in this field for a Compute
            Engine VM which has the disk associated.
        backup_configured (bool):
            Output only. Whether the target resource is configured for
            backup. This is true if the backup_configs_details is not
            empty.
        vaulted (bool):
            Output only. Whether the target resource is protected by a
            backup vault. This is true if the backup_configs_details is
            not empty and any of the
            [ResourceBackupConfig.backup_configs_details][google.cloud.backupdr.v1.ResourceBackupConfig.backup_configs_details]
            has a backup configuration with
            [BackupConfigDetails.backup_vault][google.cloud.backupdr.v1.BackupConfigDetails.backup_vault]
            set. set.
    """

    class ResourceType(proto.Enum):
        r"""The type of the cloud resource.

        Values:
            RESOURCE_TYPE_UNSPECIFIED (0):
                Resource type not set.
            CLOUD_SQL_INSTANCE (1):
                Cloud SQL instance.
            COMPUTE_ENGINE_VM (2):
                Compute Engine VM.
            COMPUTE_ENGINE_DISK (3):
                Compute Engine Disk.
            COMPUTE_ENGINE_REGIONAL_DISK (4):
                Compute Engine Regional Disk.
        """

        RESOURCE_TYPE_UNSPECIFIED = 0
        CLOUD_SQL_INSTANCE = 1
        COMPUTE_ENGINE_VM = 2
        COMPUTE_ENGINE_DISK = 3
        COMPUTE_ENGINE_REGIONAL_DISK = 4

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    target_resource: str = proto.Field(
        proto.STRING,
        number=3,
    )
    target_resource_display_name: str = proto.Field(
        proto.STRING,
        number=4,
    )
    target_resource_type: ResourceType = proto.Field(
        proto.ENUM,
        number=5,
        enum=ResourceType,
    )
    target_resource_labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=6,
    )
    backup_configs_details: MutableSequence["BackupConfigDetails"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=7,
            message="BackupConfigDetails",
        )
    )
    backup_configured: bool = proto.Field(
        proto.BOOL,
        number=8,
    )
    vaulted: bool = proto.Field(
        proto.BOOL,
        number=9,
    )


class BackupConfigDetails(proto.Message):
    r"""BackupConfigDetails has information about how the resource is
    configured for backups and about the most recent backup taken
    for this configuration.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        backup_config_source (str):
            Output only. The full resource name of the
            backup config source resource. For example,
            "//backupdr.googleapis.com/v1/projects/{project}/locations/{region}/backupPlans/{backupplanId}"
            or
            "//compute.googleapis.com/projects/{project}/locations/{region}/resourcePolicies/{resourcePolicyId}".
        backup_config_source_display_name (str):
            Output only. The display name of the backup
            config source resource.
        type_ (google.cloud.backupdr_v1.types.BackupConfigDetails.Type):
            Output only. The type of the backup config
            resource.
        state (google.cloud.backupdr_v1.types.BackupConfigDetails.State):
            Output only. The state of the backup config
            resource.
        pitr_settings (google.cloud.backupdr_v1.types.PitrSettings):
            Output only. Point in time recovery settings
            of the backup configuration resource.
        latest_successful_backup_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp of the latest
            successful backup created via this backup
            configuration.
        applicable_resource (str):
            Output only. The `full resource
            name <https://cloud.google.com/asset-inventory/docs/resource-name-format>`__
            of the resource that is applicable for the backup
            configuration. Example:
            "//compute.googleapis.com/projects/{project}/zones/{zone}/instances/{instance}".
        backup_vault (str):
            Output only. The `full resource
            name <https://cloud.google.com/asset-inventory/docs/resource-name-format>`__
            of the backup vault that will store the backups generated
            through this backup configuration. Example:
            "//backupdr.googleapis.com/v1/projects/{project}/locations/{region}/backupVaults/{backupvaultId}".
        backup_locations (MutableSequence[google.cloud.backupdr_v1.types.BackupLocation]):
            The locations where the backups are to be
            stored.
        backup_dr_plan_config (google.cloud.backupdr_v1.types.BackupDrPlanConfig):
            Google Cloud Backup and DR's Backup Plan
            specific data.

            This field is a member of `oneof`_ ``plan_specific_config``.
        backup_dr_template_config (google.cloud.backupdr_v1.types.BackupDrTemplateConfig):
            Google Cloud Backup and DR's Template
            specific data.

            This field is a member of `oneof`_ ``plan_specific_config``.
    """

    class Type(proto.Enum):
        r"""Type of the backup configuration.
        This enum may receive new values in the future.

        Values:
            TYPE_UNSPECIFIED (0):
                Backup config type is unspecified.
            CLOUD_SQL_INSTANCE_BACKUP_CONFIG (1):
                Backup config is Cloud SQL instance's
                automated backup config.
            COMPUTE_ENGINE_RESOURCE_POLICY (2):
                Backup config is Compute Engine Resource
                Policy.
            BACKUPDR_BACKUP_PLAN (3):
                Backup config is Google Cloud Backup and DR's
                Backup Plan.
            BACKUPDR_TEMPLATE (4):
                Backup config is Google Cloud Backup and DR's
                Template.
        """

        TYPE_UNSPECIFIED = 0
        CLOUD_SQL_INSTANCE_BACKUP_CONFIG = 1
        COMPUTE_ENGINE_RESOURCE_POLICY = 2
        BACKUPDR_BACKUP_PLAN = 3
        BACKUPDR_TEMPLATE = 4

    class State(proto.Enum):
        r"""The state tells whether the backup config is active or not.

        Values:
            STATE_UNSPECIFIED (0):
                Backup config state not set.
            ACTIVE (1):
                The config is in an active state protecting
                the resource
            INACTIVE (2):
                The config is currently not protecting the
                resource. Either because it is disabled or the
                owning project has been deleted without cleanup
                of the actual resource.
            ERROR (3):
                The config still exists but because of some
                error state it is not protecting the resource.
                Like the source project is deleted. For eg.
                PlanAssociation, BackupPlan is deleted.
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        INACTIVE = 2
        ERROR = 3

    backup_config_source: str = proto.Field(
        proto.STRING,
        number=1,
    )
    backup_config_source_display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    type_: Type = proto.Field(
        proto.ENUM,
        number=3,
        enum=Type,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=4,
        enum=State,
    )
    pitr_settings: "PitrSettings" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="PitrSettings",
    )
    latest_successful_backup_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    applicable_resource: str = proto.Field(
        proto.STRING,
        number=7,
    )
    backup_vault: str = proto.Field(
        proto.STRING,
        number=8,
    )
    backup_locations: MutableSequence["BackupLocation"] = proto.RepeatedField(
        proto.MESSAGE,
        number=12,
        message="BackupLocation",
    )
    backup_dr_plan_config: "BackupDrPlanConfig" = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="plan_specific_config",
        message="BackupDrPlanConfig",
    )
    backup_dr_template_config: "BackupDrTemplateConfig" = proto.Field(
        proto.MESSAGE,
        number=11,
        oneof="plan_specific_config",
        message="BackupDrTemplateConfig",
    )


class PitrSettings(proto.Message):
    r"""Point in time recovery settings of the backup configuration
    resource.

    Attributes:
        retention_days (int):
            Output only. Number of days to retain the
            backup.
    """

    retention_days: int = proto.Field(
        proto.INT32,
        number=1,
    )


class BackupDrTemplateConfig(proto.Message):
    r"""Provides additional information about Google Cloud Backup
    and DR's Template backup configuration.

    Attributes:
        first_party_management_uri (str):
            Output only. The URI of the BackupDr template
            resource for the first party identity users.
        third_party_management_uri (str):
            Output only. The URI of the BackupDr template
            resource for the third party identity users.
    """

    first_party_management_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    third_party_management_uri: str = proto.Field(
        proto.STRING,
        number=2,
    )


class BackupDrPlanConfig(proto.Message):
    r"""BackupDrPlanConfig has additional information about Google
    Cloud Backup and DR's Plan backup configuration.

    Attributes:
        backup_dr_plan_rules (MutableSequence[google.cloud.backupdr_v1.types.BackupDrPlanRule]):
            Backup rules of the backup plan resource.
    """

    backup_dr_plan_rules: MutableSequence["BackupDrPlanRule"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="BackupDrPlanRule",
    )


class BackupDrPlanRule(proto.Message):
    r"""BackupDrPlanRule has rule specific information of the backup
    plan resource.

    Attributes:
        rule_id (str):
            Output only. Unique Id of the backup rule.
        last_successful_backup_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp of the latest
            successful backup created via this backup rule.
    """

    rule_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    last_successful_backup_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )


class BackupLocation(proto.Message):
    r"""BackupLocation represents a cloud location where a backup can
    be stored.

    Attributes:
        type_ (google.cloud.backupdr_v1.types.BackupLocation.Type):
            Output only. The type of the location.
        location_id (str):
            Output only. The id of the cloud location.
            Example: "us-central1".
    """

    class Type(proto.Enum):
        r"""The type of the location.

        Values:
            TYPE_UNSPECIFIED (0):
                Location type is unspecified.
            ZONAL (1):
                Location type is zonal.
            REGIONAL (2):
                Location type is regional.
            MULTI_REGIONAL (3):
                Location type is multi regional.
        """

        TYPE_UNSPECIFIED = 0
        ZONAL = 1
        REGIONAL = 2
        MULTI_REGIONAL = 3

    type_: Type = proto.Field(
        proto.ENUM,
        number=1,
        enum=Type,
    )
    location_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
