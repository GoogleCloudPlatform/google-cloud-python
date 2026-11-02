# -*- coding: utf-8 -*-
# Copyright 2025 Google LLC
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

import proto  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.gkehub.configmanagement.v1",
    manifest={
        "DeploymentState",
        "MembershipState",
        "MembershipSpec",
        "ConfigSync",
        "GitConfig",
        "OciConfig",
        "PolicyController",
        "HierarchyControllerConfig",
        "HierarchyControllerDeploymentState",
        "HierarchyControllerVersion",
        "HierarchyControllerState",
        "OperatorState",
        "InstallError",
        "ConfigSyncState",
        "ConfigSyncError",
        "ConfigSyncVersion",
        "ConfigSyncDeploymentState",
        "SyncState",
        "SyncError",
        "ErrorResource",
        "GroupVersionKind",
        "PolicyControllerState",
        "PolicyControllerVersion",
        "GatekeeperDeploymentState",
    },
)


class DeploymentState(proto.Enum):
    r"""Enum representing the state of an ACM's deployment on a
    cluster

    Values:
        DEPLOYMENT_STATE_UNSPECIFIED (0):
            Deployment's state cannot be determined
        NOT_INSTALLED (1):
            Deployment is not installed
        INSTALLED (2):
            Deployment is installed
        ERROR (3):
            Deployment was attempted to be installed, but
            has errors
        PENDING (4):
            Deployment is installing or terminating
    """

    DEPLOYMENT_STATE_UNSPECIFIED = 0
    NOT_INSTALLED = 1
    INSTALLED = 2
    ERROR = 3
    PENDING = 4


class MembershipState(proto.Message):
    r"""**Anthos Config Management**: State for a single cluster.

    Attributes:
        cluster_name (str):
            This field is set to the ``cluster_name`` field of the
            Membership Spec if it is not empty. Otherwise, it is set to
            the cluster's fleet membership name.
        membership_spec (google.cloud.gkehub.configmanagement_v1.types.MembershipSpec):
            Membership configuration in the cluster. This
            represents the actual state in the cluster,
            while the MembershipSpec in the FeatureSpec
            represents the intended state
        operator_state (google.cloud.gkehub.configmanagement_v1.types.OperatorState):
            Current install status of ACM's Operator
        config_sync_state (google.cloud.gkehub.configmanagement_v1.types.ConfigSyncState):
            Current sync status
        policy_controller_state (google.cloud.gkehub.configmanagement_v1.types.PolicyControllerState):
            PolicyController status
        hierarchy_controller_state (google.cloud.gkehub.configmanagement_v1.types.HierarchyControllerState):
            Hierarchy Controller status
    """

    cluster_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    membership_spec: "MembershipSpec" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="MembershipSpec",
    )
    operator_state: "OperatorState" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="OperatorState",
    )
    config_sync_state: "ConfigSyncState" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="ConfigSyncState",
    )
    policy_controller_state: "PolicyControllerState" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="PolicyControllerState",
    )
    hierarchy_controller_state: "HierarchyControllerState" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="HierarchyControllerState",
    )


class MembershipSpec(proto.Message):
    r"""**Anthos Config Management**: Configuration for a single cluster.
    Intended to parallel the ConfigManagement CR.

    Attributes:
        config_sync (google.cloud.gkehub.configmanagement_v1.types.ConfigSync):
            Config Sync configuration for the cluster.
        policy_controller (google.cloud.gkehub.configmanagement_v1.types.PolicyController):
            Policy Controller configuration for the
            cluster.
        hierarchy_controller (google.cloud.gkehub.configmanagement_v1.types.HierarchyControllerConfig):
            Hierarchy Controller configuration for the
            cluster.
        version (str):
            Version of ACM installed.
        cluster (str):
            The user-specified cluster name used by
            Config Sync cluster-name-selector annotation or
            ClusterSelector, for applying configs to only a
            subset of clusters.
            Omit this field if the cluster's fleet
            membership name is used by Config Sync
            cluster-name-selector annotation or
            ClusterSelector. Set this field if a name
            different from the cluster's fleet membership
            name is used by Config Sync
            cluster-name-selector annotation or
            ClusterSelector.
        management (google.cloud.gkehub.configmanagement_v1.types.MembershipSpec.Management):
            Enables automatic Feature management.
    """

    class Management(proto.Enum):
        r"""Whether to automatically manage the Feature.

        Values:
            MANAGEMENT_UNSPECIFIED (0):
                Unspecified
            MANAGEMENT_AUTOMATIC (1):
                Google will manage the Feature for the
                cluster.
            MANAGEMENT_MANUAL (2):
                User will manually manage the Feature for the
                cluster.
        """

        MANAGEMENT_UNSPECIFIED = 0
        MANAGEMENT_AUTOMATIC = 1
        MANAGEMENT_MANUAL = 2

    config_sync: "ConfigSync" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="ConfigSync",
    )
    policy_controller: "PolicyController" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="PolicyController",
    )
    hierarchy_controller: "HierarchyControllerConfig" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="HierarchyControllerConfig",
    )
    version: str = proto.Field(
        proto.STRING,
        number=10,
    )
    cluster: str = proto.Field(
        proto.STRING,
        number=11,
    )
    management: Management = proto.Field(
        proto.ENUM,
        number=12,
        enum=Management,
    )


class ConfigSync(proto.Message):
    r"""Configuration for Config Sync

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        git (google.cloud.gkehub.configmanagement_v1.types.GitConfig):
            Git repo configuration for the cluster.
        source_format (str):
            Specifies whether the Config Sync Repo is
            in "hierarchical" or "unstructured" mode.
        enabled (bool):
            Enables the installation of ConfigSync.
            If set to true, ConfigSync resources will be
            created and the other ConfigSync fields will be
            applied if exist.
            If set to false, all other ConfigSync fields
            will be ignored, ConfigSync resources will be
            deleted.
            If omitted, ConfigSync resources will be managed
            depends on the presence of the git or oci field.

            This field is a member of `oneof`_ ``_enabled``.
        prevent_drift (bool):
            Set to true to enable the Config Sync admission webhook to
            prevent drifts. If set to ``false``, disables the Config
            Sync admission webhook and does not prevent drifts.
        oci (google.cloud.gkehub.configmanagement_v1.types.OciConfig):
            OCI repo configuration for the cluster
        metrics_gcp_service_account_email (str):
            The Email of the Google Cloud Service Account (GSA) used for
            exporting Config Sync metrics to Cloud Monitoring when
            Workload Identity is enabled. The GSA should have the
            Monitoring Metric Writer (roles/monitoring.metricWriter) IAM
            role. The Kubernetes ServiceAccount ``default`` in the
            namespace ``config-management-monitoring`` should be bound
            to the GSA.
    """

    git: "GitConfig" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="GitConfig",
    )
    source_format: str = proto.Field(
        proto.STRING,
        number=8,
    )
    enabled: bool = proto.Field(
        proto.BOOL,
        number=10,
        optional=True,
    )
    prevent_drift: bool = proto.Field(
        proto.BOOL,
        number=11,
    )
    oci: "OciConfig" = proto.Field(
        proto.MESSAGE,
        number=12,
        message="OciConfig",
    )
    metrics_gcp_service_account_email: str = proto.Field(
        proto.STRING,
        number=15,
    )


class GitConfig(proto.Message):
    r"""Git repo configuration for a single cluster.

    Attributes:
        sync_repo (str):
            The URL of the Git repository to use as the
            source of truth.
        sync_branch (str):
            The branch of the repository to sync from.
            Default: master.
        policy_dir (str):
            The path within the Git repository that
            represents the top level of the repo to sync.
            Default: the root directory of the repository.
        sync_wait_secs (int):
            Period in seconds between consecutive syncs.
            Default: 15.
        sync_rev (str):
            Git revision (tag or hash) to check out.
            Default HEAD.
        secret_type (str):
            Type of secret configured for access to the
            Git repo. Must be one of ssh, cookiefile,
            gcenode, token, gcpserviceaccount or none. The
            validation of this is case-sensitive. Required.
        https_proxy (str):
            URL for the HTTPS proxy to be used when
            communicating with the Git repo.
        gcp_service_account_email (str):
            The Google Cloud Service Account Email used for auth when
            secret_type is gcpServiceAccount.
    """

    sync_repo: str = proto.Field(
        proto.STRING,
        number=1,
    )
    sync_branch: str = proto.Field(
        proto.STRING,
        number=2,
    )
    policy_dir: str = proto.Field(
        proto.STRING,
        number=3,
    )
    sync_wait_secs: int = proto.Field(
        proto.INT64,
        number=4,
    )
    sync_rev: str = proto.Field(
        proto.STRING,
        number=5,
    )
    secret_type: str = proto.Field(
        proto.STRING,
        number=6,
    )
    https_proxy: str = proto.Field(
        proto.STRING,
        number=7,
    )
    gcp_service_account_email: str = proto.Field(
        proto.STRING,
        number=8,
    )


class OciConfig(proto.Message):
    r"""OCI repo configuration for a single cluster

    Attributes:
        sync_repo (str):
            The OCI image repository URL for the package to sync from.
            e.g.
            ``LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY_NAME/PACKAGE_NAME``.
        policy_dir (str):
            The absolute path of the directory that
            contains the local resources.  Default: the root
            directory of the image.
        sync_wait_secs (int):
            Period in seconds between consecutive syncs.
            Default: 15.
        secret_type (str):
            Type of secret configured for access to the
            Git repo.
        gcp_service_account_email (str):
            The Google Cloud Service Account Email used for auth when
            secret_type is gcpServiceAccount.
    """

    sync_repo: str = proto.Field(
        proto.STRING,
        number=1,
    )
    policy_dir: str = proto.Field(
        proto.STRING,
        number=2,
    )
    sync_wait_secs: int = proto.Field(
        proto.INT64,
        number=3,
    )
    secret_type: str = proto.Field(
        proto.STRING,
        number=4,
    )
    gcp_service_account_email: str = proto.Field(
        proto.STRING,
        number=5,
    )


class PolicyController(proto.Message):
    r"""Configuration for Policy Controller

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        enabled (bool):
            Enables the installation of Policy
            Controller. If false, the rest of
            PolicyController fields take no effect.
        template_library_installed (bool):
            Installs the default template library along
            with Policy Controller.

            This field is a member of `oneof`_ ``_template_library_installed``.
        audit_interval_seconds (int):
            Sets the interval for Policy Controller Audit
            Scans (in seconds). When set to 0, this disables
            audit functionality altogether.

            This field is a member of `oneof`_ ``_audit_interval_seconds``.
        exemptable_namespaces (MutableSequence[str]):
            The set of namespaces that are excluded from
            Policy Controller checks. Namespaces do not need
            to currently exist on the cluster.
        referential_rules_enabled (bool):
            Enables the ability to use Constraint
            Templates that reference to objects other than
            the object currently being evaluated.
        log_denies_enabled (bool):
            Logs all denies and dry run failures.
    """

    enabled: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    template_library_installed: bool = proto.Field(
        proto.BOOL,
        number=2,
        optional=True,
    )
    audit_interval_seconds: int = proto.Field(
        proto.INT64,
        number=3,
        optional=True,
    )
    exemptable_namespaces: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    referential_rules_enabled: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    log_denies_enabled: bool = proto.Field(
        proto.BOOL,
        number=6,
    )


class HierarchyControllerConfig(proto.Message):
    r"""Configuration for Hierarchy Controller

    Attributes:
        enabled (bool):
            Whether Hierarchy Controller is enabled in
            this cluster.
        enable_pod_tree_labels (bool):
            Whether pod tree labels are enabled in this
            cluster.
        enable_hierarchical_resource_quota (bool):
            Whether hierarchical resource quota is
            enabled in this cluster.
    """

    enabled: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    enable_pod_tree_labels: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    enable_hierarchical_resource_quota: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class HierarchyControllerDeploymentState(proto.Message):
    r"""Deployment state for Hierarchy Controller

    Attributes:
        hnc (google.cloud.gkehub.configmanagement_v1.types.DeploymentState):
            The deployment state for open source HNC
            (e.g. v0.7.0-hc.0)
        extension (google.cloud.gkehub.configmanagement_v1.types.DeploymentState):
            The deployment state for Hierarchy Controller
            extension (e.g. v0.7.0-hc.1)
    """

    hnc: "DeploymentState" = proto.Field(
        proto.ENUM,
        number=1,
        enum="DeploymentState",
    )
    extension: "DeploymentState" = proto.Field(
        proto.ENUM,
        number=2,
        enum="DeploymentState",
    )


class HierarchyControllerVersion(proto.Message):
    r"""Version for Hierarchy Controller

    Attributes:
        hnc (str):
            Version for open source HNC
        extension (str):
            Version for Hierarchy Controller extension
    """

    hnc: str = proto.Field(
        proto.STRING,
        number=1,
    )
    extension: str = proto.Field(
        proto.STRING,
        number=2,
    )


class HierarchyControllerState(proto.Message):
    r"""State for Hierarchy Controller

    Attributes:
        version (google.cloud.gkehub.configmanagement_v1.types.HierarchyControllerVersion):
            The version for Hierarchy Controller
        state (google.cloud.gkehub.configmanagement_v1.types.HierarchyControllerDeploymentState):
            The deployment state for Hierarchy Controller
    """

    version: "HierarchyControllerVersion" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="HierarchyControllerVersion",
    )
    state: "HierarchyControllerDeploymentState" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="HierarchyControllerDeploymentState",
    )


class OperatorState(proto.Message):
    r"""State information for an ACM's Operator

    Attributes:
        version (str):
            The semenatic version number of the operator
        deployment_state (google.cloud.gkehub.configmanagement_v1.types.DeploymentState):
            The state of the Operator's deployment
        errors (MutableSequence[google.cloud.gkehub.configmanagement_v1.types.InstallError]):
            Install errors.
    """

    version: str = proto.Field(
        proto.STRING,
        number=1,
    )
    deployment_state: "DeploymentState" = proto.Field(
        proto.ENUM,
        number=2,
        enum="DeploymentState",
    )
    errors: MutableSequence["InstallError"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="InstallError",
    )


class InstallError(proto.Message):
    r"""Errors pertaining to the installation of ACM

    Attributes:
        error_message (str):
            A string representing the user facing error
            message
    """

    error_message: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ConfigSyncState(proto.Message):
    r"""State information for ConfigSync

    Attributes:
        version (google.cloud.gkehub.configmanagement_v1.types.ConfigSyncVersion):
            The version of ConfigSync deployed
        deployment_state (google.cloud.gkehub.configmanagement_v1.types.ConfigSyncDeploymentState):
            Information about the deployment of
            ConfigSync, including the version of the various
            Pods deployed
        sync_state (google.cloud.gkehub.configmanagement_v1.types.SyncState):
            The state of ConfigSync's process to sync
            configs to a cluster
        errors (MutableSequence[google.cloud.gkehub.configmanagement_v1.types.ConfigSyncError]):
            Errors pertaining to the installation of
            Config Sync.
        rootsync_crd (google.cloud.gkehub.configmanagement_v1.types.ConfigSyncState.CRDState):
            The state of the RootSync CRD
        reposync_crd (google.cloud.gkehub.configmanagement_v1.types.ConfigSyncState.CRDState):
            The state of the Reposync CRD
        state (google.cloud.gkehub.configmanagement_v1.types.ConfigSyncState.State):
            The state of CS
            This field summarizes the other fields in this
            message.
    """

    class CRDState(proto.Enum):
        r"""CRDState representing the state of a CRD

        Values:
            CRD_STATE_UNSPECIFIED (0):
                CRD's state cannot be determined
            NOT_INSTALLED (1):
                CRD is not installed
            INSTALLED (2):
                CRD is installed
            TERMINATING (3):
                CRD is terminating (i.e., it has been deleted
                and is cleaning up)
            INSTALLING (4):
                CRD is installing
        """

        CRD_STATE_UNSPECIFIED = 0
        NOT_INSTALLED = 1
        INSTALLED = 2
        TERMINATING = 3
        INSTALLING = 4

    class State(proto.Enum):
        r"""

        Values:
            STATE_UNSPECIFIED (0):
                CS's state cannot be determined.
            CONFIG_SYNC_NOT_INSTALLED (1):
                CS is not installed.
            CONFIG_SYNC_INSTALLED (2):
                The expected CS version is installed
                successfully.
            CONFIG_SYNC_ERROR (3):
                CS encounters errors.
            CONFIG_SYNC_PENDING (4):
                CS is installing or terminating.
        """

        STATE_UNSPECIFIED = 0
        CONFIG_SYNC_NOT_INSTALLED = 1
        CONFIG_SYNC_INSTALLED = 2
        CONFIG_SYNC_ERROR = 3
        CONFIG_SYNC_PENDING = 4

    version: "ConfigSyncVersion" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="ConfigSyncVersion",
    )
    deployment_state: "ConfigSyncDeploymentState" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ConfigSyncDeploymentState",
    )
    sync_state: "SyncState" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="SyncState",
    )
    errors: MutableSequence["ConfigSyncError"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="ConfigSyncError",
    )
    rootsync_crd: CRDState = proto.Field(
        proto.ENUM,
        number=5,
        enum=CRDState,
    )
    reposync_crd: CRDState = proto.Field(
        proto.ENUM,
        number=6,
        enum=CRDState,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=7,
        enum=State,
    )


class ConfigSyncError(proto.Message):
    r"""Errors pertaining to the installation of Config Sync

    Attributes:
        error_message (str):
            A string representing the user facing error
            message
    """

    error_message: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ConfigSyncVersion(proto.Message):
    r"""Specific versioning information pertaining to ConfigSync's
    Pods

    Attributes:
        importer (str):
            Version of the deployed importer pod
        syncer (str):
            Version of the deployed syncer pod
        git_sync (str):
            Version of the deployed git-sync pod
        monitor (str):
            Version of the deployed monitor pod
        reconciler_manager (str):
            Version of the deployed reconciler-manager
            pod
        root_reconciler (str):
            Version of the deployed reconciler container
            in root-reconciler pod
        admission_webhook (str):
            Version of the deployed admission_webhook pod
    """

    importer: str = proto.Field(
        proto.STRING,
        number=1,
    )
    syncer: str = proto.Field(
        proto.STRING,
        number=2,
    )
    git_sync: str = proto.Field(
        proto.STRING,
        number=3,
    )
    monitor: str = proto.Field(
        proto.STRING,
        number=4,
    )
    reconciler_manager: str = proto.Field(
        proto.STRING,
        number=5,
    )
    root_reconciler: str = proto.Field(
        proto.STRING,
        number=6,
    )
    admission_webhook: str = proto.Field(
        proto.STRING,
        number=7,
    )


class ConfigSyncDeploymentState(proto.Message):
    r"""The state of ConfigSync's deployment on a cluster

    Attributes:
        importer (google.cloud.gkehub.configmanagement_v1.types.DeploymentState):
            Deployment state of the importer pod
        syncer (google.cloud.gkehub.configmanagement_v1.types.DeploymentState):
            Deployment state of the syncer pod
        git_sync (google.cloud.gkehub.configmanagement_v1.types.DeploymentState):
            Deployment state of the git-sync pod
        monitor (google.cloud.gkehub.configmanagement_v1.types.DeploymentState):
            Deployment state of the monitor pod
        reconciler_manager (google.cloud.gkehub.configmanagement_v1.types.DeploymentState):
            Deployment state of reconciler-manager pod
        root_reconciler (google.cloud.gkehub.configmanagement_v1.types.DeploymentState):
            Deployment state of root-reconciler
        admission_webhook (google.cloud.gkehub.configmanagement_v1.types.DeploymentState):
            Deployment state of admission-webhook
    """

    importer: "DeploymentState" = proto.Field(
        proto.ENUM,
        number=1,
        enum="DeploymentState",
    )
    syncer: "DeploymentState" = proto.Field(
        proto.ENUM,
        number=2,
        enum="DeploymentState",
    )
    git_sync: "DeploymentState" = proto.Field(
        proto.ENUM,
        number=3,
        enum="DeploymentState",
    )
    monitor: "DeploymentState" = proto.Field(
        proto.ENUM,
        number=4,
        enum="DeploymentState",
    )
    reconciler_manager: "DeploymentState" = proto.Field(
        proto.ENUM,
        number=5,
        enum="DeploymentState",
    )
    root_reconciler: "DeploymentState" = proto.Field(
        proto.ENUM,
        number=6,
        enum="DeploymentState",
    )
    admission_webhook: "DeploymentState" = proto.Field(
        proto.ENUM,
        number=7,
        enum="DeploymentState",
    )


class SyncState(proto.Message):
    r"""State indicating an ACM's progress syncing configurations to
    a cluster

    Attributes:
        source_token (str):
            Token indicating the state of the repo.
        import_token (str):
            Token indicating the state of the importer.
        sync_token (str):
            Token indicating the state of the syncer.
        last_sync (str):
            Deprecated: use last_sync_time instead. Timestamp of when
            ACM last successfully synced the repo The time format is
            specified in https://golang.org/pkg/time/#Time.String
        last_sync_time (google.protobuf.timestamp_pb2.Timestamp):
            Timestamp type of when ACM last successfully
            synced the repo
        code (google.cloud.gkehub.configmanagement_v1.types.SyncState.SyncCode):
            Sync status code
        errors (MutableSequence[google.cloud.gkehub.configmanagement_v1.types.SyncError]):
            A list of errors resulting from problematic
            configs. This list will be truncated after 100
            errors, although it is unlikely for that many
            errors to simultaneously exist.
    """

    class SyncCode(proto.Enum):
        r"""An enum representing Config Sync's status of syncing configs
        to a cluster.

        Values:
            SYNC_CODE_UNSPECIFIED (0):
                Config Sync cannot determine a sync code
            SYNCED (1):
                Config Sync successfully synced the git Repo
                with the cluster
            PENDING (2):
                Config Sync is in the progress of syncing a
                new change
            ERROR (3):
                Indicates an error configuring Config Sync,
                and user action is required
            NOT_CONFIGURED (4):
                Config Sync has been installed but not
                configured
            NOT_INSTALLED (5):
                Config Sync has not been installed
            UNAUTHORIZED (6):
                Error authorizing with the cluster
            UNREACHABLE (7):
                Cluster could not be reached
        """

        SYNC_CODE_UNSPECIFIED = 0
        SYNCED = 1
        PENDING = 2
        ERROR = 3
        NOT_CONFIGURED = 4
        NOT_INSTALLED = 5
        UNAUTHORIZED = 6
        UNREACHABLE = 7

    source_token: str = proto.Field(
        proto.STRING,
        number=1,
    )
    import_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    sync_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    last_sync: str = proto.Field(
        proto.STRING,
        number=4,
    )
    last_sync_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    code: SyncCode = proto.Field(
        proto.ENUM,
        number=5,
        enum=SyncCode,
    )
    errors: MutableSequence["SyncError"] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message="SyncError",
    )


class SyncError(proto.Message):
    r"""An ACM created error representing a problem syncing
    configurations

    Attributes:
        code (str):
            An ACM defined error code
        error_message (str):
            A description of the error
        error_resources (MutableSequence[google.cloud.gkehub.configmanagement_v1.types.ErrorResource]):
            A list of config(s) associated with the
            error, if any
    """

    code: str = proto.Field(
        proto.STRING,
        number=1,
    )
    error_message: str = proto.Field(
        proto.STRING,
        number=2,
    )
    error_resources: MutableSequence["ErrorResource"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="ErrorResource",
    )


class ErrorResource(proto.Message):
    r"""Model for a config file in the git repo with an associated
    Sync error

    Attributes:
        source_path (str):
            Path in the git repo of the erroneous config
        resource_name (str):
            Metadata name of the resource that is causing
            an error
        resource_namespace (str):
            Namespace of the resource that is causing an
            error
        resource_gvk (google.cloud.gkehub.configmanagement_v1.types.GroupVersionKind):
            Group/version/kind of the resource that is
            causing an error
    """

    source_path: str = proto.Field(
        proto.STRING,
        number=1,
    )
    resource_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    resource_namespace: str = proto.Field(
        proto.STRING,
        number=3,
    )
    resource_gvk: "GroupVersionKind" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="GroupVersionKind",
    )


class GroupVersionKind(proto.Message):
    r"""A Kubernetes object's GVK

    Attributes:
        group (str):
            Kubernetes Group
        version (str):
            Kubernetes Version
        kind (str):
            Kubernetes Kind
    """

    group: str = proto.Field(
        proto.STRING,
        number=1,
    )
    version: str = proto.Field(
        proto.STRING,
        number=2,
    )
    kind: str = proto.Field(
        proto.STRING,
        number=3,
    )


class PolicyControllerState(proto.Message):
    r"""State for PolicyControllerState.

    Attributes:
        version (google.cloud.gkehub.configmanagement_v1.types.PolicyControllerVersion):
            The version of Gatekeeper Policy Controller
            deployed.
        deployment_state (google.cloud.gkehub.configmanagement_v1.types.GatekeeperDeploymentState):
            The state about the policy controller
            installation.
    """

    version: "PolicyControllerVersion" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="PolicyControllerVersion",
    )
    deployment_state: "GatekeeperDeploymentState" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="GatekeeperDeploymentState",
    )


class PolicyControllerVersion(proto.Message):
    r"""The build version of Gatekeeper Policy Controller is using.

    Attributes:
        version (str):
            The gatekeeper image tag that is composed of
            ACM version, git tag, build number.
    """

    version: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GatekeeperDeploymentState(proto.Message):
    r"""State of Policy Controller installation.

    Attributes:
        gatekeeper_controller_manager_state (google.cloud.gkehub.configmanagement_v1.types.DeploymentState):
            Status of gatekeeper-controller-manager pod.
        gatekeeper_audit (google.cloud.gkehub.configmanagement_v1.types.DeploymentState):
            Status of gatekeeper-audit deployment.
    """

    gatekeeper_controller_manager_state: "DeploymentState" = proto.Field(
        proto.ENUM,
        number=1,
        enum="DeploymentState",
    )
    gatekeeper_audit: "DeploymentState" = proto.Field(
        proto.ENUM,
        number=2,
        enum="DeploymentState",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
