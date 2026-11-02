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
    package="google.cloud.gkemulticloud.v1",
    manifest={
        "Jwk",
        "WorkloadIdentityConfig",
        "MaxPodsConstraint",
        "OperationMetadata",
        "NodeTaint",
        "NodeKubeletConfig",
        "Fleet",
        "LoggingConfig",
        "LoggingComponentConfig",
        "MonitoringConfig",
        "ManagedPrometheusConfig",
        "CloudMonitoringConfig",
        "BinaryAuthorization",
        "SecurityPostureConfig",
    },
)


class Jwk(proto.Message):
    r"""Jwk is a JSON Web Key as specified in RFC 7517.

    Attributes:
        kty (str):
            Key Type.
        alg (str):
            Algorithm.
        use (str):
            Permitted uses for the public keys.
        kid (str):
            Key ID.
        n (str):
            Used for RSA keys.
        e (str):
            Used for RSA keys.
        x (str):
            Used for ECDSA keys.
        y (str):
            Used for ECDSA keys.
        crv (str):
            Used for ECDSA keys.
    """

    kty: str = proto.Field(
        proto.STRING,
        number=1,
    )
    alg: str = proto.Field(
        proto.STRING,
        number=2,
    )
    use: str = proto.Field(
        proto.STRING,
        number=3,
    )
    kid: str = proto.Field(
        proto.STRING,
        number=4,
    )
    n: str = proto.Field(
        proto.STRING,
        number=5,
    )
    e: str = proto.Field(
        proto.STRING,
        number=6,
    )
    x: str = proto.Field(
        proto.STRING,
        number=7,
    )
    y: str = proto.Field(
        proto.STRING,
        number=8,
    )
    crv: str = proto.Field(
        proto.STRING,
        number=9,
    )


class WorkloadIdentityConfig(proto.Message):
    r"""Workload Identity settings.

    Attributes:
        issuer_uri (str):
            The OIDC issuer URL for this cluster.
        workload_pool (str):
            The Workload Identity Pool associated to the
            cluster.
        identity_provider (str):
            The ID of the OIDC Identity Provider (IdP)
            associated to the Workload Identity Pool.
    """

    issuer_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    workload_pool: str = proto.Field(
        proto.STRING,
        number=2,
    )
    identity_provider: str = proto.Field(
        proto.STRING,
        number=3,
    )


class MaxPodsConstraint(proto.Message):
    r"""Constraints applied to pods.

    Attributes:
        max_pods_per_node (int):
            Required. The maximum number of pods to
            schedule on a single node.
    """

    max_pods_per_node: int = proto.Field(
        proto.INT64,
        number=1,
    )


class OperationMetadata(proto.Message):
    r"""Metadata about a long-running operation.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which this operation
            was created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which this operation
            was completed.
        target (str):
            Output only. The name of the resource
            associated to this operation.
        status_detail (str):
            Output only. Human-readable status of the
            operation, if any.
        error_detail (str):
            Output only. Human-readable status of any
            error that occurred during the operation.
        verb (str):
            Output only. The verb associated with the API
            method which triggered this operation. Possible
            values are "create", "delete", "update" and
            "import".
        requested_cancellation (bool):
            Output only. Identifies whether cancellation has been
            requested for the operation. Operations that have
            successfully been cancelled have
            [google.longrunning.Operation.error][google.longrunning.Operation.error]
            value with a
            [google.rpc.Status.code][google.rpc.Status.code] of 1,
            corresponding to ``Code.CANCELLED``.
    """

    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    target: str = proto.Field(
        proto.STRING,
        number=3,
    )
    status_detail: str = proto.Field(
        proto.STRING,
        number=4,
    )
    error_detail: str = proto.Field(
        proto.STRING,
        number=5,
    )
    verb: str = proto.Field(
        proto.STRING,
        number=7,
    )
    requested_cancellation: bool = proto.Field(
        proto.BOOL,
        number=6,
    )


class NodeTaint(proto.Message):
    r"""The taint content for the node taint.

    Attributes:
        key (str):
            Required. Key for the taint.
        value (str):
            Required. Value for the taint.
        effect (google.cloud.gke_multicloud_v1.types.NodeTaint.Effect):
            Required. The taint effect.
    """

    class Effect(proto.Enum):
        r"""The taint effect.

        Values:
            EFFECT_UNSPECIFIED (0):
                Not set.
            NO_SCHEDULE (1):
                Do not allow new pods to schedule onto the
                node unless they tolerate the taint, but allow
                all pods submitted to Kubelet without going
                through the scheduler to start, and allow all
                already-running pods to continue running.
                Enforced by the scheduler.
            PREFER_NO_SCHEDULE (2):
                Like TaintEffectNoSchedule, but the scheduler
                tries not to schedule new pods onto the node,
                rather than prohibiting new pods from scheduling
                onto the node entirely. Enforced by the
                scheduler.
            NO_EXECUTE (3):
                Evict any already-running pods that do not
                tolerate the taint. Currently enforced by
                NodeController.
        """

        EFFECT_UNSPECIFIED = 0
        NO_SCHEDULE = 1
        PREFER_NO_SCHEDULE = 2
        NO_EXECUTE = 3

    key: str = proto.Field(
        proto.STRING,
        number=1,
    )
    value: str = proto.Field(
        proto.STRING,
        number=2,
    )
    effect: Effect = proto.Field(
        proto.ENUM,
        number=3,
        enum=Effect,
    )


class NodeKubeletConfig(proto.Message):
    r"""Configuration for node pool kubelet options.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        insecure_kubelet_readonly_port_enabled (bool):
            Optional. Enable the insecure kubelet read
            only port.
        cpu_manager_policy (str):
            Optional. Control the CPU management policy on the node. See
            https://kubernetes.io/docs/tasks/administer-cluster/cpu-management-policies/

            The following values are allowed.

            - "none": the default, which represents the existing
              scheduling behavior.
            - "static": allows pods with certain resource
              characteristics to be granted increased CPU affinity and
              exclusivity on the node. The default value is 'none' if
              unspecified.

            This field is a member of `oneof`_ ``_cpu_manager_policy``.
        cpu_cfs_quota (bool):
            Optional. Enable CPU CFS quota enforcement
            for containers that specify CPU limits.

            This option is enabled by default which makes
            kubelet use CFS quota
            (https://www.kernel.org/doc/Documentation/scheduler/sched-bwc.txt)
            to enforce container CPU limits. Otherwise, CPU
            limits will not be enforced at all.

            Disable this option to mitigate CPU throttling
            problems while still having your pods to be in
            Guaranteed QoS class by specifying the CPU
            limits.

            The default value is 'true' if unspecified.

            This field is a member of `oneof`_ ``_cpu_cfs_quota``.
        cpu_cfs_quota_period (str):
            Optional. Set the CPU CFS quota period value
            'cpu.cfs_period_us'.

            The string must be a sequence of decimal numbers, each with
            optional fraction and a unit suffix, such as "300ms". Valid
            time units are "ns", "us" (or "µs"), "ms", "s", "m", "h".
            The value must be a positive duration.

            The default value is '100ms' if unspecified.

            This field is a member of `oneof`_ ``_cpu_cfs_quota_period``.
        pod_pids_limit (int):
            Optional. Set the Pod PID limits. See
            https://kubernetes.io/docs/concepts/policy/pid-limiting/#pod-pid-limits

            Controls the maximum number of processes allowed
            to run in a pod. The value must be greater than
            or equal to 1024 and less than 4194304.

            This field is a member of `oneof`_ ``_pod_pids_limit``.
    """

    insecure_kubelet_readonly_port_enabled: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    cpu_manager_policy: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    cpu_cfs_quota: bool = proto.Field(
        proto.BOOL,
        number=3,
        optional=True,
    )
    cpu_cfs_quota_period: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )
    pod_pids_limit: int = proto.Field(
        proto.INT64,
        number=5,
        optional=True,
    )


class Fleet(proto.Message):
    r"""Fleet related configuration.

    Fleets are a Google Cloud concept for logically organizing clusters,
    letting you use and manage multi-cluster capabilities and apply
    consistent policies across your systems.

    See `Anthos
    Fleets <https://cloud.google.com/anthos/multicluster-management/fleets>`__
    for more details on Anthos multi-cluster capabilities using Fleets.

    Attributes:
        project (str):
            Required. The name of the Fleet host project where this
            cluster will be registered.

            Project names are formatted as
            ``projects/<project-number>``.
        membership (str):
            Output only. The name of the managed Hub Membership resource
            associated to this cluster.

            Membership names are formatted as
            ``projects/<project-number>/locations/global/membership/<cluster-id>``.
    """

    project: str = proto.Field(
        proto.STRING,
        number=1,
    )
    membership: str = proto.Field(
        proto.STRING,
        number=2,
    )


class LoggingConfig(proto.Message):
    r"""Parameters that describe the Logging configuration in a
    cluster.

    Attributes:
        component_config (google.cloud.gke_multicloud_v1.types.LoggingComponentConfig):
            The configuration of the logging components;
    """

    component_config: "LoggingComponentConfig" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="LoggingComponentConfig",
    )


class LoggingComponentConfig(proto.Message):
    r"""Parameters that describe the Logging component configuration
    in a cluster.

    Attributes:
        enable_components (MutableSequence[google.cloud.gke_multicloud_v1.types.LoggingComponentConfig.Component]):
            The components to be enabled.
    """

    class Component(proto.Enum):
        r"""The components of the logging configuration;

        Values:
            COMPONENT_UNSPECIFIED (0):
                No component is specified
            SYSTEM_COMPONENTS (1):
                This indicates that system logging components
                is enabled.
            WORKLOADS (2):
                This indicates that user workload logging
                component is enabled.
        """

        COMPONENT_UNSPECIFIED = 0
        SYSTEM_COMPONENTS = 1
        WORKLOADS = 2

    enable_components: MutableSequence[Component] = proto.RepeatedField(
        proto.ENUM,
        number=1,
        enum=Component,
    )


class MonitoringConfig(proto.Message):
    r"""Parameters that describe the Monitoring configuration in a
    cluster.

    Attributes:
        managed_prometheus_config (google.cloud.gke_multicloud_v1.types.ManagedPrometheusConfig):
            Enable Google Cloud Managed Service for
            Prometheus in the cluster.
        cloud_monitoring_config (google.cloud.gke_multicloud_v1.types.CloudMonitoringConfig):
            Optionally enable GKE metrics.
            Only for Attached Clusters.
    """

    managed_prometheus_config: "ManagedPrometheusConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ManagedPrometheusConfig",
    )
    cloud_monitoring_config: "CloudMonitoringConfig" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="CloudMonitoringConfig",
    )


class ManagedPrometheusConfig(proto.Message):
    r"""ManagedPrometheusConfig defines the configuration for
    Google Cloud Managed Service for Prometheus.

    Attributes:
        enabled (bool):
            Enable Managed Collection.
    """

    enabled: bool = proto.Field(
        proto.BOOL,
        number=1,
    )


class CloudMonitoringConfig(proto.Message):
    r"""CloudMonitoringConfig defines the configuration for
    built-in Cloud Logging and Monitoring.
    Only for Attached Clusters.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        enabled (bool):
            Enable GKE-native logging and metrics.
            Only for Attached Clusters.

            This field is a member of `oneof`_ ``_enabled``.
    """

    enabled: bool = proto.Field(
        proto.BOOL,
        number=1,
        optional=True,
    )


class BinaryAuthorization(proto.Message):
    r"""Configuration for Binary Authorization.

    Attributes:
        evaluation_mode (google.cloud.gke_multicloud_v1.types.BinaryAuthorization.EvaluationMode):
            Mode of operation for binauthz policy
            evaluation. If unspecified, defaults to
            DISABLED.
    """

    class EvaluationMode(proto.Enum):
        r"""Binary Authorization mode of operation.

        Values:
            EVALUATION_MODE_UNSPECIFIED (0):
                Default value
            DISABLED (1):
                Disable BinaryAuthorization
            PROJECT_SINGLETON_POLICY_ENFORCE (2):
                Enforce Kubernetes admission requests with
                BinaryAuthorization using the project's
                singleton policy.
        """

        EVALUATION_MODE_UNSPECIFIED = 0
        DISABLED = 1
        PROJECT_SINGLETON_POLICY_ENFORCE = 2

    evaluation_mode: EvaluationMode = proto.Field(
        proto.ENUM,
        number=1,
        enum=EvaluationMode,
    )


class SecurityPostureConfig(proto.Message):
    r"""SecurityPostureConfig defines the flags needed to
    enable/disable features for the Security Posture API.

    Attributes:
        vulnerability_mode (google.cloud.gke_multicloud_v1.types.SecurityPostureConfig.VulnerabilityMode):
            Sets which mode to use for vulnerability
            scanning.
    """

    class VulnerabilityMode(proto.Enum):
        r"""VulnerabilityMode defines enablement mode for vulnerability
        scanning.

        Values:
            VULNERABILITY_MODE_UNSPECIFIED (0):
                Default value not specified.
            VULNERABILITY_DISABLED (1):
                Disables vulnerability scanning on the
                cluster.
            VULNERABILITY_ENTERPRISE (2):
                Applies the Security Posture's vulnerability
                on cluster Enterprise level features.
        """

        VULNERABILITY_MODE_UNSPECIFIED = 0
        VULNERABILITY_DISABLED = 1
        VULNERABILITY_ENTERPRISE = 2

    vulnerability_mode: VulnerabilityMode = proto.Field(
        proto.ENUM,
        number=1,
        enum=VulnerabilityMode,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
