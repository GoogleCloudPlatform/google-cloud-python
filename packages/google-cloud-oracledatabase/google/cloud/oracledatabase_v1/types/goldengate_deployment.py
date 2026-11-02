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
import google.type.dayofweek_pb2 as dayofweek_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.oracledatabase.v1",
    manifest={
        "GoldengateDeployment",
        "GoldengateDeploymentProperties",
        "GoldengateOggDeployment",
        "GoldengateMaintenanceWindow",
        "GoldengateMaintenanceConfig",
        "DeploymentDiagnosticData",
        "GoldengateBackupSchedule",
        "IngressIp",
        "GoldengateDeploymentLock",
        "GoldengatePlacement",
        "GoldengateGroupToRolesMapping",
        "CreateGoldengateDeploymentRequest",
        "DeleteGoldengateDeploymentRequest",
        "GetGoldengateDeploymentRequest",
        "ListGoldengateDeploymentsRequest",
        "ListGoldengateDeploymentsResponse",
        "StopGoldengateDeploymentRequest",
        "StartGoldengateDeploymentRequest",
    },
)


class GoldengateDeployment(proto.Message):
    r"""GoldengateDeployment Goldengate Deployment resource model.

    Attributes:
        name (str):
            Identifier. The name of the GoldengateDeployment resource in
            the following format:
            projects/{project}/locations/{region}/goldengateDeployments/{goldengate_deployment}
        properties (google.cloud.oracledatabase_v1.types.GoldengateDeploymentProperties):
            Required. The properties of the
            GoldengateDeployment.
        gcp_oracle_zone (str):
            Optional. The GCP Oracle zone where Oracle
            GoldengateDeployment is hosted. Example:
            us-east4-b-r2. If not specified, the system will
            pick a zone based on availability.
        labels (MutableMapping[str, str]):
            Optional. The labels or tags associated with
            the GoldengateDeployment.
        odb_network (str):
            Optional. The name of the OdbNetwork
            associated with the GoldengateDeployment.
        odb_subnet (str):
            Required. The name of the OdbSubnet
            associated with the GoldengateDeployment for IP
            allocation.
        entitlement_id (str):
            Output only. The ID of the subscription
            entitlement associated with the
            GoldengateDeployment
        display_name (str):
            Required. The display name for the
            GoldengateDeployment.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The date and time that the
            GoldengateDeployment was created.
        oci_url (str):
            Output only. HTTPS link to OCI resources
            exposed to Customer via UI Interface.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    properties: "GoldengateDeploymentProperties" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="GoldengateDeploymentProperties",
    )
    gcp_oracle_zone: str = proto.Field(
        proto.STRING,
        number=3,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    odb_network: str = proto.Field(
        proto.STRING,
        number=5,
    )
    odb_subnet: str = proto.Field(
        proto.STRING,
        number=6,
    )
    entitlement_id: str = proto.Field(
        proto.STRING,
        number=7,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=8,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    oci_url: str = proto.Field(
        proto.STRING,
        number=10,
    )


class GoldengateDeploymentProperties(proto.Message):
    r"""Properties of GoldengateDeployment.

    Attributes:
        ocid (str):
            Output only. OCID of the
            GoldengateDeployment.
        lifecycle_state (google.cloud.oracledatabase_v1.types.GoldengateDeploymentProperties.GoldengateDeploymentLifecycleState):
            Output only. State of the
            GoldengateDeployment.
        license_model (google.cloud.oracledatabase_v1.types.GoldengateDeploymentProperties.LicenseModel):
            Optional. The Oracle license model that
            applies to a Deployment.
        environment_type (str):
            Optional. The environment type of the
            GoldengateDeployment.
        cpu_core_count (int):
            Optional. The Minimum number of OCPUs to be
            made available for this Deployment.
        is_auto_scaling_enabled (bool):
            Optional. Indicates if auto scaling is
            enabled for the Deployment's CPU core count.
        description (str):
            Optional. The description of the
            GoldengateDeployment.
        deployment_type (str):
            Required. A valid Goldengate Deployment type. For a list of
            supported types, use the ``ListGoldengateDeploymentTypes``
            operation.
        ogg_data (google.cloud.oracledatabase_v1.types.GoldengateOggDeployment):
            Required. The ogg data of the
            GoldengateDeployment.
        maintenance_window (google.cloud.oracledatabase_v1.types.GoldengateMaintenanceWindow):
            Optional. The maintenance window of the
            GoldengateDeployment.
        maintenance_config (google.cloud.oracledatabase_v1.types.GoldengateMaintenanceConfig):
            Optional. The maintenance configuration of
            the GoldengateDeployment.
        fqdn (str):
            Output only. The Fully Qualified Domain Name
            of the GoldengateDeployment.
        lifecycle_sub_state (google.cloud.oracledatabase_v1.types.GoldengateDeploymentProperties.GoldengateDeploymentLifecycleSubState):
            Output only. The lifecycle sub-state of the
            GoldengateDeployment.
        category (google.cloud.oracledatabase_v1.types.GoldengateDeploymentProperties.GoldengateDeploymentCategory):
            Output only. The category of the
            GoldengateDeployment.
        deployment_backup_id (str):
            Output only. The deployment backup id of the
            GoldengateDeployment.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the
            GoldengateDeployment was updated.
        lifecycle_details (str):
            Output only. The lifecycle details of the
            GoldengateDeployment.
        healthy (bool):
            Output only. Whether the GoldengateDeployment
            is healthy.
        load_balancer_subnet_id (str):
            Output only. The load balancer subnet id of
            the GoldengateDeployment.
        load_balancer_id (str):
            Output only. The load balancer id of the
            GoldengateDeployment.
        nsg_ids (MutableSequence[str]):
            Output only. The nsg ids of the
            GoldengateDeployment.
        is_public (bool):
            Output only. Whether the GoldengateDeployment
            is public.
        public_ip_address (str):
            Output only. The public ip address of the
            GoldengateDeployment.
        private_ip_address (str):
            Output only. The private ip address of the
            GoldengateDeployment.
        deployment_url (str):
            Output only. The deployment url of the
            GoldengateDeployment.
        is_latest_version (bool):
            Output only. Whether the GoldengateDeployment
            is of the latest version.
        upgrade_required_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time upgrade required of the
            GoldengateDeployment.
        storage_utilization_bytes (int):
            Output only. The storage utilization in bytes
            of the GoldengateDeployment.
        is_storage_utilization_limit_exceeded (bool):
            Output only. Whether storage utilization
            limit is exceeded of the GoldengateDeployment.
        deployment_diagnostic_data (google.cloud.oracledatabase_v1.types.DeploymentDiagnosticData):
            Output only. The deployment diagnostic data
            of the GoldengateDeployment.
        backup_schedule (google.cloud.oracledatabase_v1.types.GoldengateBackupSchedule):
            Output only. The backup schedule of the
            GoldengateDeployment.
        next_maintenance_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time of next maintenance of
            the GoldengateDeployment.
        next_maintenance_action_type (google.cloud.oracledatabase_v1.types.GoldengateDeploymentProperties.NextMaintenanceActionType):
            Output only. The next maintenance action type
            of the GoldengateDeployment.
        next_maintenance_description (str):
            Output only. The next maintenance description
            of the GoldengateDeployment.
        ogg_version_support_end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time ogg version supported
            until of the GoldengateDeployment.
        ingress_ips (MutableSequence[google.cloud.oracledatabase_v1.types.IngressIp]):
            Output only. The ingress ips of the
            GoldengateDeployment.
        deployment_role (google.cloud.oracledatabase_v1.types.GoldengateDeploymentProperties.GoldengateDeploymentRoleType):
            Output only. The deployment role of the
            GoldengateDeployment.
        last_backup_schedule_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time last backup scheduled
            of the GoldengateDeployment.
        next_backup_schedule_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time next backup scheduled
            of the GoldengateDeployment.
        role_change_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the role of the
            GoldengateDeployment was changed.
        locks (MutableSequence[google.cloud.oracledatabase_v1.types.GoldengateDeploymentLock]):
            Output only. The locks of the
            GoldengateDeployment.
        placements (MutableSequence[google.cloud.oracledatabase_v1.types.GoldengatePlacement]):
            Output only. The placements of the
            GoldengateDeployment.
    """

    class GoldengateDeploymentLifecycleState(proto.Enum):
        r"""The various lifecycle states of the GoldengateDeployment.

        Values:
            GOLDENGATE_DEPLOYMENT_LIFECYCLE_STATE_UNSPECIFIED (0):
                Default unspecified value.
            CREATING (1):
                The deployment is being created.
            UPDATING (2):
                The deployment is being updated.
            ACTIVE (3):
                The deployment is active.
            INACTIVE (4):
                The deployment is inactive.
            DELETING (5):
                The deployment is being deleted.
            DELETED (6):
                The deployment is deleted.
            FAILED (7):
                The deployment failed.
            NEEDS_ATTENTION (8):
                The deployment needs attention.
            IN_PROGRESS (9):
                The deployment is in progress.
            CANCELLING (10):
                The deployment is canceling.
            CANCELLED (11):
                The deployment is canceled.
            SUCCEEDED (12):
                The deployment succeeded.
            WAITING (13):
                The deployment is waiting.
        """

        GOLDENGATE_DEPLOYMENT_LIFECYCLE_STATE_UNSPECIFIED = 0
        CREATING = 1
        UPDATING = 2
        ACTIVE = 3
        INACTIVE = 4
        DELETING = 5
        DELETED = 6
        FAILED = 7
        NEEDS_ATTENTION = 8
        IN_PROGRESS = 9
        CANCELLING = 10
        CANCELLED = 11
        SUCCEEDED = 12
        WAITING = 13

    class LicenseModel(proto.Enum):
        r"""The license model of the GoldengateDeployment.

        Values:
            LICENSE_MODEL_UNSPECIFIED (0):
                The license model is unspecified.
            LICENSE_INCLUDED (1):
                The license model is included.
            BRING_YOUR_OWN_LICENSE (2):
                The license model is bring your own license.
        """

        LICENSE_MODEL_UNSPECIFIED = 0
        LICENSE_INCLUDED = 1
        BRING_YOUR_OWN_LICENSE = 2

    class GoldengateDeploymentLifecycleSubState(proto.Enum):
        r"""The various lifecycle sub-states of the GoldengateDeployment.

        Values:
            GOLDENGATE_DEPLOYMENT_LIFECYCLE_SUB_STATE_UNSPECIFIED (0):
                The lifecycle sub-state is unspecified.
            RECOVERING (1):
                The deployment is recovering.
            STARTING (2):
                The deployment is starting.
            STOPPING (3):
                The deployment is stopping.
            MOVING (4):
                The deployment is moving.
            UPGRADING (5):
                The deployment is upgrading.
            RESTORING (6):
                The deployment is restoring.
            BACKING_UP (7):
                The deployment is backing up.
            ROLLING_BACK (8):
                The deployment is rolling back.
        """

        GOLDENGATE_DEPLOYMENT_LIFECYCLE_SUB_STATE_UNSPECIFIED = 0
        RECOVERING = 1
        STARTING = 2
        STOPPING = 3
        MOVING = 4
        UPGRADING = 5
        RESTORING = 6
        BACKING_UP = 7
        ROLLING_BACK = 8

    class GoldengateDeploymentCategory(proto.Enum):
        r"""The category of the GoldengateDeployment.

        Values:
            GOLDENGATE_DEPLOYMENT_CATEGORY_UNSPECIFIED (0):
                The category is unspecified.
            DATA_REPLICATION (1):
                The deployment is data replication.
            DATA_TRANSFORMS (2):
                The deployment is data transforms.
        """

        GOLDENGATE_DEPLOYMENT_CATEGORY_UNSPECIFIED = 0
        DATA_REPLICATION = 1
        DATA_TRANSFORMS = 2

    class NextMaintenanceActionType(proto.Enum):
        r"""The various next maintenance action types of the
        GoldengateDeployment.

        Values:
            NEXT_MAINTENANCE_ACTION_TYPE_UNSPECIFIED (0):
                The next maintenance action type is
                unspecified.
            UPGRADE (1):
                The next maintenance action type is upgrade.
        """

        NEXT_MAINTENANCE_ACTION_TYPE_UNSPECIFIED = 0
        UPGRADE = 1

    class GoldengateDeploymentRoleType(proto.Enum):
        r"""The deployment role type of the GoldengateDeployment.

        Values:
            GOLDENGATE_DEPLOYMENT_ROLE_TYPE_UNSPECIFIED (0):
                The deployment role type is unspecified.
            PRIMARY (1):
                The deployment role type is primary.
            STANDBY (2):
                The deployment role type is standby.
        """

        GOLDENGATE_DEPLOYMENT_ROLE_TYPE_UNSPECIFIED = 0
        PRIMARY = 1
        STANDBY = 2

    ocid: str = proto.Field(
        proto.STRING,
        number=1,
    )
    lifecycle_state: GoldengateDeploymentLifecycleState = proto.Field(
        proto.ENUM,
        number=2,
        enum=GoldengateDeploymentLifecycleState,
    )
    license_model: LicenseModel = proto.Field(
        proto.ENUM,
        number=3,
        enum=LicenseModel,
    )
    environment_type: str = proto.Field(
        proto.STRING,
        number=4,
    )
    cpu_core_count: int = proto.Field(
        proto.INT32,
        number=5,
    )
    is_auto_scaling_enabled: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    description: str = proto.Field(
        proto.STRING,
        number=7,
    )
    deployment_type: str = proto.Field(
        proto.STRING,
        number=8,
    )
    ogg_data: "GoldengateOggDeployment" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="GoldengateOggDeployment",
    )
    maintenance_window: "GoldengateMaintenanceWindow" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="GoldengateMaintenanceWindow",
    )
    maintenance_config: "GoldengateMaintenanceConfig" = proto.Field(
        proto.MESSAGE,
        number=11,
        message="GoldengateMaintenanceConfig",
    )
    fqdn: str = proto.Field(
        proto.STRING,
        number=12,
    )
    lifecycle_sub_state: GoldengateDeploymentLifecycleSubState = proto.Field(
        proto.ENUM,
        number=13,
        enum=GoldengateDeploymentLifecycleSubState,
    )
    category: GoldengateDeploymentCategory = proto.Field(
        proto.ENUM,
        number=14,
        enum=GoldengateDeploymentCategory,
    )
    deployment_backup_id: str = proto.Field(
        proto.STRING,
        number=15,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=16,
        message=timestamp_pb2.Timestamp,
    )
    lifecycle_details: str = proto.Field(
        proto.STRING,
        number=17,
    )
    healthy: bool = proto.Field(
        proto.BOOL,
        number=18,
    )
    load_balancer_subnet_id: str = proto.Field(
        proto.STRING,
        number=19,
    )
    load_balancer_id: str = proto.Field(
        proto.STRING,
        number=20,
    )
    nsg_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=21,
    )
    is_public: bool = proto.Field(
        proto.BOOL,
        number=22,
    )
    public_ip_address: str = proto.Field(
        proto.STRING,
        number=23,
    )
    private_ip_address: str = proto.Field(
        proto.STRING,
        number=24,
    )
    deployment_url: str = proto.Field(
        proto.STRING,
        number=25,
    )
    is_latest_version: bool = proto.Field(
        proto.BOOL,
        number=26,
    )
    upgrade_required_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=27,
        message=timestamp_pb2.Timestamp,
    )
    storage_utilization_bytes: int = proto.Field(
        proto.INT64,
        number=28,
    )
    is_storage_utilization_limit_exceeded: bool = proto.Field(
        proto.BOOL,
        number=29,
    )
    deployment_diagnostic_data: "DeploymentDiagnosticData" = proto.Field(
        proto.MESSAGE,
        number=30,
        message="DeploymentDiagnosticData",
    )
    backup_schedule: "GoldengateBackupSchedule" = proto.Field(
        proto.MESSAGE,
        number=31,
        message="GoldengateBackupSchedule",
    )
    next_maintenance_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=32,
        message=timestamp_pb2.Timestamp,
    )
    next_maintenance_action_type: NextMaintenanceActionType = proto.Field(
        proto.ENUM,
        number=33,
        enum=NextMaintenanceActionType,
    )
    next_maintenance_description: str = proto.Field(
        proto.STRING,
        number=34,
    )
    ogg_version_support_end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=35,
        message=timestamp_pb2.Timestamp,
    )
    ingress_ips: MutableSequence["IngressIp"] = proto.RepeatedField(
        proto.MESSAGE,
        number=36,
        message="IngressIp",
    )
    deployment_role: GoldengateDeploymentRoleType = proto.Field(
        proto.ENUM,
        number=37,
        enum=GoldengateDeploymentRoleType,
    )
    last_backup_schedule_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=38,
        message=timestamp_pb2.Timestamp,
    )
    next_backup_schedule_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=39,
        message=timestamp_pb2.Timestamp,
    )
    role_change_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=40,
        message=timestamp_pb2.Timestamp,
    )
    locks: MutableSequence["GoldengateDeploymentLock"] = proto.RepeatedField(
        proto.MESSAGE,
        number=41,
        message="GoldengateDeploymentLock",
    )
    placements: MutableSequence["GoldengatePlacement"] = proto.RepeatedField(
        proto.MESSAGE,
        number=42,
        message="GoldengatePlacement",
    )


class GoldengateOggDeployment(proto.Message):
    r"""The Ogg data of the GoldengateDeployment.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        admin_password (str):
            Optional. The Goldengate deployment console
            password in plain text.

            This field is a member of `oneof`_ ``deployment_password_options``.
        admin_password_secret_version (str):
            Optional. Input only. The Goldengate
            deployment console password secret version.

            This field is a member of `oneof`_ ``deployment_password_options``.
        deployment (str):
            Required. The name given to the Goldengate
            service deployment. The name must be 1 to 32
            characters long, must contain only alphanumeric
            characters and must start with a letter.
        admin_username (str):
            Required. The Goldengate deployment console
            username.
        ogg_version (str):
            Optional. Version of OGG
        certificate (str):
            Output only. The certificate of the
            GoldengateDeployment.
        credential_store (google.cloud.oracledatabase_v1.types.GoldengateOggDeployment.CredentialStore):
            Output only. The credential store of the
            GoldengateDeployment.
        identity_domain_id (str):
            Output only. The identity domain id of the
            GoldengateDeployment.
        password_secret_id (str):
            Output only. The password secret id of the
            GoldengateDeployment.
        group_roles_mapping (google.cloud.oracledatabase_v1.types.GoldengateGroupToRolesMapping):
            Output only. The group to roles mapping of
            the GoldengateDeployment.
    """

    class CredentialStore(proto.Enum):
        r"""The credential store of the GoldengateDeployment.

        Values:
            CREDENTIAL_STORE_UNSPECIFIED (0):
                The credential store is unspecified.
            GOLDENGATE (1):
                The credential store is Goldengate.
            IAM (2):
                The credential store is IAM.
        """

        CREDENTIAL_STORE_UNSPECIFIED = 0
        GOLDENGATE = 1
        IAM = 2

    admin_password: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="deployment_password_options",
    )
    admin_password_secret_version: str = proto.Field(
        proto.STRING,
        number=10,
        oneof="deployment_password_options",
    )
    deployment: str = proto.Field(
        proto.STRING,
        number=1,
    )
    admin_username: str = proto.Field(
        proto.STRING,
        number=2,
    )
    ogg_version: str = proto.Field(
        proto.STRING,
        number=4,
    )
    certificate: str = proto.Field(
        proto.STRING,
        number=5,
    )
    credential_store: CredentialStore = proto.Field(
        proto.ENUM,
        number=6,
        enum=CredentialStore,
    )
    identity_domain_id: str = proto.Field(
        proto.STRING,
        number=7,
    )
    password_secret_id: str = proto.Field(
        proto.STRING,
        number=8,
    )
    group_roles_mapping: "GoldengateGroupToRolesMapping" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="GoldengateGroupToRolesMapping",
    )


class GoldengateMaintenanceWindow(proto.Message):
    r"""The maintenance window of the GoldengateDeployment.

    Attributes:
        day (google.type.dayofweek_pb2.DayOfWeek):
            Required. Days of the week.
        start_hour (int):
            Required. Start hour for maintenance period.
            Hour is in UTC.
    """

    day: dayofweek_pb2.DayOfWeek = proto.Field(
        proto.ENUM,
        number=1,
        enum=dayofweek_pb2.DayOfWeek,
    )
    start_hour: int = proto.Field(
        proto.INT32,
        number=2,
    )


class GoldengateMaintenanceConfig(proto.Message):
    r"""The maintenance configuration of the GoldengateDeployment.

    Attributes:
        is_interim_release_auto_upgrade_enabled (bool):
            Optional. By default auto upgrade for interim releases are
            not enabled. If auto-upgrade is enabled for interim release,
            you have to specify interim_release_upgrade_period_days too.
        interim_release_upgrade_period_days (int):
            Optional. Defines auto upgrade period for
            interim releases. This period must be shorter or
            equal to bundle release upgrade period.
        bundle_release_upgrade_period_days (int):
            Optional. Defines auto upgrade period for
            bundle releases. Manually configured period
            cannot be longer than service defined period for
            bundle releases. This period must be shorter or
            equal to major release upgrade period. Not
            passing this field during create will equate to
            using the service default.
        major_release_upgrade_period_days (int):
            Optional. Defines auto upgrade period for
            major releases. Manually configured period
            cannot be longer than service defined period for
            major releases. Not passing this field during
            create will equate to using the service default.
        security_patch_upgrade_period_days (int):
            Optional. Defines auto upgrade period for
            releases with security fix. Manually configured
            period cannot be longer than service defined
            period for security releases. Not passing this
            field during create will equate to using the
            service default.
    """

    is_interim_release_auto_upgrade_enabled: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    interim_release_upgrade_period_days: int = proto.Field(
        proto.INT32,
        number=2,
    )
    bundle_release_upgrade_period_days: int = proto.Field(
        proto.INT32,
        number=3,
    )
    major_release_upgrade_period_days: int = proto.Field(
        proto.INT32,
        number=4,
    )
    security_patch_upgrade_period_days: int = proto.Field(
        proto.INT32,
        number=5,
    )


class DeploymentDiagnosticData(proto.Message):
    r"""The deployment diagnostic data.

    Attributes:
        namespace (str):
            Output only. The namespace name.
        bucket (str):
            Output only. The bucket name.
        object_ (str):
            Output only. The object name.
        diagnostic_state (google.cloud.oracledatabase_v1.types.DeploymentDiagnosticData.DiagnosticState):
            Output only. The diagnostic state.
        diagnostic_start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time diagnostic start.
        diagnostic_end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time diagnostic end.
    """

    class DiagnosticState(proto.Enum):
        r"""The possible states of the diagnostic data.

        Values:
            DIAGNOSTIC_STATE_UNSPECIFIED (0):
                The diagnostic state is unspecified.
            IN_PROGRESS (1):
                The diagnostic is in progress.
            SUCCEEDED (2):
                The diagnostic completed successfully.
            FAILED (3):
                The diagnostic failed.
        """

        DIAGNOSTIC_STATE_UNSPECIFIED = 0
        IN_PROGRESS = 1
        SUCCEEDED = 2
        FAILED = 3

    namespace: str = proto.Field(
        proto.STRING,
        number=1,
    )
    bucket: str = proto.Field(
        proto.STRING,
        number=2,
    )
    object_: str = proto.Field(
        proto.STRING,
        number=3,
    )
    diagnostic_state: DiagnosticState = proto.Field(
        proto.ENUM,
        number=4,
        enum=DiagnosticState,
    )
    diagnostic_start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    diagnostic_end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )


class GoldengateBackupSchedule(proto.Message):
    r"""The backup schedule of the GoldengateDeployment.

    Attributes:
        bucket (str):
            Output only. The bucket name.
        compartment_id (str):
            Output only. The compartment id.
        frequency_backup_scheduled (google.cloud.oracledatabase_v1.types.GoldengateBackupSchedule.FrequencyBackupScheduled):
            Output only. The frequency backup scheduled.
        metadata_only (bool):
            Output only. If metadata only.
        namespace (str):
            Output only. The namespace name.
        backup_scheduled_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp of when the backup
            was scheduled.
    """

    class FrequencyBackupScheduled(proto.Enum):
        r"""Enum for frequency backup scheduled.

        Values:
            FREQUENCY_BACKUP_SCHEDULED_UNSPECIFIED (0):
                The frequency backup scheduled is
                unspecified.
            DAILY (1):
                The frequency backup scheduled is daily.
            WEEKLY (2):
                The frequency backup scheduled is weekly.
            MONTHLY (3):
                The frequency backup scheduled is monthly.
        """

        FREQUENCY_BACKUP_SCHEDULED_UNSPECIFIED = 0
        DAILY = 1
        WEEKLY = 2
        MONTHLY = 3

    bucket: str = proto.Field(
        proto.STRING,
        number=1,
    )
    compartment_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    frequency_backup_scheduled: FrequencyBackupScheduled = proto.Field(
        proto.ENUM,
        number=3,
        enum=FrequencyBackupScheduled,
    )
    metadata_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    namespace: str = proto.Field(
        proto.STRING,
        number=5,
    )
    backup_scheduled_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )


class IngressIp(proto.Message):
    r"""The ingress IPs of the GoldengateDeployment.

    Attributes:
        ingress_ip_address (str):
            Output only. The ingress IP.
    """

    ingress_ip_address: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GoldengateDeploymentLock(proto.Message):
    r"""The lock of the GoldengateDeployment.

    Attributes:
        type_ (google.cloud.oracledatabase_v1.types.GoldengateDeploymentLock.LockType):
            Output only. The type of lock.
        compartment_id (str):
            Output only. The compartment id.
        related_resource_id (str):
            Output only. The related resource id.
        message (str):
            Output only. The message.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time created.
    """

    class LockType(proto.Enum):
        r"""The type of lock.

        Values:
            LOCK_TYPE_UNSPECIFIED (0):
                The lock type is unspecified.
            FULL (1):
                The lock type is full.
            DELETE (2):
                The lock type is delete.
        """

        LOCK_TYPE_UNSPECIFIED = 0
        FULL = 1
        DELETE = 2

    type_: LockType = proto.Field(
        proto.ENUM,
        number=1,
        enum=LockType,
    )
    compartment_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    related_resource_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    message: str = proto.Field(
        proto.STRING,
        number=4,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )


class GoldengatePlacement(proto.Message):
    r"""The placement of the GoldengateDeployment.

    Attributes:
        availability_domain (str):
            Output only. The availability domain.
        fault_domain (str):
            Output only. The fault domain.
    """

    availability_domain: str = proto.Field(
        proto.STRING,
        number=1,
    )
    fault_domain: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GoldengateGroupToRolesMapping(proto.Message):
    r"""The group to roles mapping of the GoldengateDeployment.

    Attributes:
        security_group_id (str):
            Output only. The security group id.
        administrator_group_id (str):
            Output only. The administrator group id.
        operator_group_id (str):
            Output only. The operator group id.
        user_group_id (str):
            Output only. The user group id.
    """

    security_group_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    administrator_group_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    operator_group_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    user_group_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class CreateGoldengateDeploymentRequest(proto.Message):
    r"""The request for ``GoldengateDeployment.Create``.

    Attributes:
        parent (str):
            Required. The value for parent of the
            GoldengateDeployment in the following format:
            projects/{project}/locations/{location}.
        goldengate_deployment_id (str):
            Required. The ID of the GoldengateDeployment to create. This
            value is restricted to
            (^\ `a-z <[a-z0-9-]{0,61}[a-z0-9]>`__?$) and must be a
            maximum of 63 characters in length. The value must start
            with a letter and end with a letter or a number.
        goldengate_deployment (google.cloud.oracledatabase_v1.types.GoldengateDeployment):
            Required. The resource being created.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    goldengate_deployment_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    goldengate_deployment: "GoldengateDeployment" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="GoldengateDeployment",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class DeleteGoldengateDeploymentRequest(proto.Message):
    r"""The request for ``GoldengateDeployment.Delete``.

    Attributes:
        name (str):
            Required. The name of the GoldengateDeployment in the
            following format:
            projects/{project}/locations/{location}/goldengateDeployments/{goldengate_deployment}.
        request_id (str):
            Optional. An optional ID to identify the
            request. This value is used to identify
            duplicate requests. If you make a request with
            the same request ID and the original request is
            still in progress or completed, the server
            ignores the second request. This prevents
            clients from accidentally creating duplicate
            commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetGoldengateDeploymentRequest(proto.Message):
    r"""The request for ``GoldengateDeployment.Get``.

    Attributes:
        name (str):
            Required. The name of the GoldengateDeployment in the
            following format:
            projects/{project}/locations/{location}/goldengateDeployments/{goldengate_deployment}.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListGoldengateDeploymentsRequest(proto.Message):
    r"""The request for ``GoldengateDeployment.List``.

    Attributes:
        parent (str):
            Required. The parent value for
            GoldengateDeployments in the following format:
            projects/{project}/locations/{location}.
        page_size (int):
            Optional. The maximum number of items to
            return. If unspecified, at most 50
            GoldengateDeployments will be returned. The
            maximum value is 1000; values above 1000 will be
            coerced to 1000.
        page_token (str):
            Optional. A page token, received from a
            previous ListGoldengateDeployments call. Provide
            this to retrieve the subsequent page.
        filter (str):
            Optional. An expression for filtering the
            results of the request.
        order_by (str):
            Optional. An expression for ordering the
            results of the request.
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


class ListGoldengateDeploymentsResponse(proto.Message):
    r"""The response for ``GoldengateDeployment.List``.

    Attributes:
        goldengate_deployments (MutableSequence[google.cloud.oracledatabase_v1.types.GoldengateDeployment]):
            The list of GoldengateDeployments.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Optional. Locations that could not be
            reached.
    """

    @property
    def raw_page(self):
        return self

    goldengate_deployments: MutableSequence["GoldengateDeployment"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="GoldengateDeployment",
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class StopGoldengateDeploymentRequest(proto.Message):
    r"""The request for ``GoldengateDeployment.Stop``.

    Attributes:
        name (str):
            Required. The name of the Goldengate Deployment in the
            following format:
            projects/{project}/locations/{location}/goldengateDeployments/{goldengate_deployment}.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class StartGoldengateDeploymentRequest(proto.Message):
    r"""The request for ``GoldengateDeployment.Start``.

    Attributes:
        name (str):
            Required. The name of the Goldengate Deployment in the
            following format:
            projects/{project}/locations/{location}/goldengateDeployments/{goldengate_deployment}.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
