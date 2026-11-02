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
    package="google.cloud.gkehub.v1",
    manifest={
        "Fleet",
        "DefaultClusterConfig",
        "SecurityPostureConfig",
        "BinaryAuthorizationConfig",
        "CompliancePostureConfig",
        "FleetLifecycleState",
        "Namespace",
        "NamespaceLifecycleState",
        "RBACRoleBinding",
        "RBACRoleBindingLifecycleState",
        "Scope",
        "ScopeLifecycleState",
        "MembershipBinding",
        "MembershipBindingLifecycleState",
    },
)


class Fleet(proto.Message):
    r"""Fleet contains the Fleet-wide metadata and configuration.

    Attributes:
        name (str):
            Output only. The full, unique resource name of this fleet in
            the format of
            ``projects/{project}/locations/{location}/fleets/{fleet}``.

            Each Google Cloud project can have at most one fleet
            resource, named "default".
        display_name (str):
            Optional. A user-assigned display name of the Fleet. When
            present, it must be between 4 to 30 characters. Allowed
            characters are: lowercase and uppercase letters, numbers,
            hyphen, single-quote, double-quote, space, and exclamation
            point.

            Example: ``Production Fleet``
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. When the Fleet was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. When the Fleet was last updated.
        delete_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. When the Fleet was deleted.
        uid (str):
            Output only. Google-generated UUID for this
            resource. This is unique across all Fleet
            resources. If a Fleet resource is deleted and
            another resource with the same name is created,
            it gets a different uid.
        state (google.cloud.gkehub_v1.types.FleetLifecycleState):
            Output only. State of the namespace resource.
        default_cluster_config (google.cloud.gkehub_v1.types.DefaultClusterConfig):
            Optional. The default cluster configurations
            to apply across the fleet.
        labels (MutableMapping[str, str]):
            Optional. Labels for this Fleet.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    delete_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=6,
    )
    state: "FleetLifecycleState" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="FleetLifecycleState",
    )
    default_cluster_config: "DefaultClusterConfig" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="DefaultClusterConfig",
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=11,
    )


class DefaultClusterConfig(proto.Message):
    r"""DefaultClusterConfig describes the default cluster
    configurations to be applied to all clusters born-in-fleet.

    Attributes:
        security_posture_config (google.cloud.gkehub_v1.types.SecurityPostureConfig):
            Enable/Disable Security Posture features for
            the cluster.
        binary_authorization_config (google.cloud.gkehub_v1.types.BinaryAuthorizationConfig):
            Optional. Enable/Disable binary authorization
            features for the cluster.
        compliance_posture_config (google.cloud.gkehub_v1.types.CompliancePostureConfig):
            Optional. Enable/Disable Compliance Posture
            features for the cluster. Note that on
            UpdateFleet, only full replacement of this field
            is allowed. Users are not allowed for partial
            updates through field mask.
    """

    security_posture_config: "SecurityPostureConfig" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="SecurityPostureConfig",
    )
    binary_authorization_config: "BinaryAuthorizationConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="BinaryAuthorizationConfig",
    )
    compliance_posture_config: "CompliancePostureConfig" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="CompliancePostureConfig",
    )


class SecurityPostureConfig(proto.Message):
    r"""SecurityPostureConfig defines the flags needed to
    enable/disable features for the Security Posture API.

    Attributes:
        mode (google.cloud.gkehub_v1.types.SecurityPostureConfig.Mode):
            Sets which mode to use for Security Posture
            features.
        vulnerability_mode (google.cloud.gkehub_v1.types.SecurityPostureConfig.VulnerabilityMode):
            Sets which mode to use for vulnerability
            scanning.
    """

    class Mode(proto.Enum):
        r"""Mode defines enablement mode for GKE Security posture
        features.

        Values:
            MODE_UNSPECIFIED (0):
                Default value not specified.
            DISABLED (1):
                Disables Security Posture features on the
                cluster.
            BASIC (2):
                Applies Security Posture features on the
                cluster.
            ENTERPRISE (3):
                Applies the Security Posture off cluster
                Enterprise level features.
        """

        MODE_UNSPECIFIED = 0
        DISABLED = 1
        BASIC = 2
        ENTERPRISE = 3

    class VulnerabilityMode(proto.Enum):
        r"""VulnerabilityMode defines enablement mode for vulnerability
        scanning.

        Values:
            VULNERABILITY_MODE_UNSPECIFIED (0):
                Default value not specified.
            VULNERABILITY_DISABLED (1):
                Disables vulnerability scanning on the
                cluster.
            VULNERABILITY_BASIC (2):
                Applies basic vulnerability scanning on the
                cluster.
            VULNERABILITY_ENTERPRISE (3):
                Applies the Security Posture's vulnerability
                on cluster Enterprise level features.
        """

        VULNERABILITY_MODE_UNSPECIFIED = 0
        VULNERABILITY_DISABLED = 1
        VULNERABILITY_BASIC = 2
        VULNERABILITY_ENTERPRISE = 3

    mode: Mode = proto.Field(
        proto.ENUM,
        number=1,
        enum=Mode,
    )
    vulnerability_mode: VulnerabilityMode = proto.Field(
        proto.ENUM,
        number=2,
        enum=VulnerabilityMode,
    )


class BinaryAuthorizationConfig(proto.Message):
    r"""BinaryAuthorizationConfig defines the fleet level
    configuration of binary authorization feature.

    Attributes:
        evaluation_mode (google.cloud.gkehub_v1.types.BinaryAuthorizationConfig.EvaluationMode):
            Optional. Mode of operation for binauthz
            policy evaluation.
        policy_bindings (MutableSequence[google.cloud.gkehub_v1.types.BinaryAuthorizationConfig.PolicyBinding]):
            Optional. Binauthz policies that apply to
            this cluster.
    """

    class EvaluationMode(proto.Enum):
        r"""Binary Authorization mode of operation.

        Values:
            EVALUATION_MODE_UNSPECIFIED (0):
                Default value
            DISABLED (1):
                Disable BinaryAuthorization
            POLICY_BINDINGS (2):
                Use Binary Authorization with the policies specified in
                policy_bindings.
        """

        EVALUATION_MODE_UNSPECIFIED = 0
        DISABLED = 1
        POLICY_BINDINGS = 2

    class PolicyBinding(proto.Message):
        r"""Binauthz policy that applies to this cluster.

        Attributes:
            name (str):
                The relative resource name of the binauthz platform policy
                to audit. GKE platform policies have the following format:
                ``projects/{project_number}/platforms/gke/policies/{policy_id}``.
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )

    evaluation_mode: EvaluationMode = proto.Field(
        proto.ENUM,
        number=1,
        enum=EvaluationMode,
    )
    policy_bindings: MutableSequence[PolicyBinding] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=PolicyBinding,
    )


class CompliancePostureConfig(proto.Message):
    r"""CompliancePostureConfig defines the settings needed to
    enable/disable features for the Compliance Posture.

    Attributes:
        mode (google.cloud.gkehub_v1.types.CompliancePostureConfig.Mode):
            Defines the enablement mode for Compliance
            Posture.
        compliance_standards (MutableSequence[google.cloud.gkehub_v1.types.CompliancePostureConfig.ComplianceStandard]):
            List of enabled compliance standards.
    """

    class Mode(proto.Enum):
        r"""

        Values:
            MODE_UNSPECIFIED (0):
                Default value not specified.
            DISABLED (1):
                Disables Compliance Posture features on the
                cluster.
            ENABLED (2):
                Enables Compliance Posture features on the
                cluster.
        """

        MODE_UNSPECIFIED = 0
        DISABLED = 1
        ENABLED = 2

    class ComplianceStandard(proto.Message):
        r"""

        Attributes:
            standard (str):
                Name of the compliance standard.
        """

        standard: str = proto.Field(
            proto.STRING,
            number=1,
        )

    mode: Mode = proto.Field(
        proto.ENUM,
        number=1,
        enum=Mode,
    )
    compliance_standards: MutableSequence[ComplianceStandard] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=ComplianceStandard,
    )


class FleetLifecycleState(proto.Message):
    r"""FleetLifecycleState describes the state of a Fleet resource.

    Attributes:
        code (google.cloud.gkehub_v1.types.FleetLifecycleState.Code):
            Output only. The current state of the Fleet
            resource.
    """

    class Code(proto.Enum):
        r"""Code describes the state of a Fleet resource.

        Values:
            CODE_UNSPECIFIED (0):
                The code is not set.
            CREATING (1):
                The fleet is being created.
            READY (2):
                The fleet active.
            DELETING (3):
                The fleet is being deleted.
            UPDATING (4):
                The fleet is being updated.
        """

        CODE_UNSPECIFIED = 0
        CREATING = 1
        READY = 2
        DELETING = 3
        UPDATING = 4

    code: Code = proto.Field(
        proto.ENUM,
        number=1,
        enum=Code,
    )


class Namespace(proto.Message):
    r"""Namespace represents a namespace across the Fleet

    Attributes:
        name (str):
            The resource name for the namespace
            ``projects/{project}/locations/{location}/namespaces/{namespace}``
        uid (str):
            Output only. Google-generated UUID for this
            resource. This is unique across all namespace
            resources. If a namespace resource is deleted
            and another resource with the same name is
            created, it gets a different uid.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. When the namespace was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. When the namespace was last
            updated.
        delete_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. When the namespace was deleted.
        state (google.cloud.gkehub_v1.types.NamespaceLifecycleState):
            Output only. State of the namespace resource.
        scope (str):
            Required. Scope associated with the namespace
        namespace_labels (MutableMapping[str, str]):
            Optional. Namespace-level cluster namespace labels. These
            labels are applied to the related namespace of the member
            clusters bound to the parent Scope. Scope-level labels
            (``namespace_labels`` in the Fleet Scope resource) take
            precedence over Namespace-level labels if they share a key.
            Keys and values must be Kubernetes-conformant.
        labels (MutableMapping[str, str]):
            Optional. Labels for this Namespace.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    delete_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    state: "NamespaceLifecycleState" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="NamespaceLifecycleState",
    )
    scope: str = proto.Field(
        proto.STRING,
        number=8,
    )
    namespace_labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=9,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=10,
    )


class NamespaceLifecycleState(proto.Message):
    r"""NamespaceLifecycleState describes the state of a Namespace
    resource.

    Attributes:
        code (google.cloud.gkehub_v1.types.NamespaceLifecycleState.Code):
            Output only. The current state of the
            Namespace resource.
    """

    class Code(proto.Enum):
        r"""Code describes the state of a Namespace resource.

        Values:
            CODE_UNSPECIFIED (0):
                The code is not set.
            CREATING (1):
                The namespace is being created.
            READY (2):
                The namespace active.
            DELETING (3):
                The namespace is being deleted.
            UPDATING (4):
                The namespace is being updated.
        """

        CODE_UNSPECIFIED = 0
        CREATING = 1
        READY = 2
        DELETING = 3
        UPDATING = 4

    code: Code = proto.Field(
        proto.ENUM,
        number=1,
        enum=Code,
    )


class RBACRoleBinding(proto.Message):
    r"""RBACRoleBinding represents a rbacrolebinding across the Fleet

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        user (str):
            user is the name of the user as seen by the
            kubernetes cluster, example "alice" or
            "alice@domain.tld".

            This field is a member of `oneof`_ ``principal``.
        group (str):
            group is the group, as seen by the kubernetes
            cluster.

            This field is a member of `oneof`_ ``principal``.
        name (str):
            The resource name for the rbacrolebinding
            ``projects/{project}/locations/{location}/scopes/{scope}/rbacrolebindings/{rbacrolebinding}``
            or
            ``projects/{project}/locations/{location}/memberships/{membership}/rbacrolebindings/{rbacrolebinding}``
        uid (str):
            Output only. Google-generated UUID for this
            resource. This is unique across all
            rbacrolebinding resources. If a rbacrolebinding
            resource is deleted and another resource with
            the same name is created, it gets a different
            uid.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. When the rbacrolebinding was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. When the rbacrolebinding was
            last updated.
        delete_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. When the rbacrolebinding was
            deleted.
        state (google.cloud.gkehub_v1.types.RBACRoleBindingLifecycleState):
            Output only. State of the rbacrolebinding
            resource.
        role (google.cloud.gkehub_v1.types.RBACRoleBinding.Role):
            Required. Role to bind to the principal
        labels (MutableMapping[str, str]):
            Optional. Labels for this RBACRolebinding.
    """

    class Role(proto.Message):
        r"""Role is the type for Kubernetes roles

        Attributes:
            predefined_role (google.cloud.gkehub_v1.types.RBACRoleBinding.Role.PredefinedRoles):
                predefined_role is the Kubernetes default role to use
            custom_role (str):
                Optional. custom_role is the name of a custom
                KubernetesClusterRole to use.
        """

        class PredefinedRoles(proto.Enum):
            r"""PredefinedRoles is an ENUM representation of the default
            Kubernetes Roles

            Values:
                UNKNOWN (0):
                    UNKNOWN
                ADMIN (1):
                    ADMIN has EDIT and RBAC permissions
                EDIT (2):
                    EDIT can edit all resources except RBAC
                VIEW (3):
                    VIEW can only read resources
                ANTHOS_SUPPORT (4):
                    ANTHOS_SUPPORT gives Google Support read-only access to a
                    number of cluster resources.
            """

            UNKNOWN = 0
            ADMIN = 1
            EDIT = 2
            VIEW = 3
            ANTHOS_SUPPORT = 4

        predefined_role: "RBACRoleBinding.Role.PredefinedRoles" = proto.Field(
            proto.ENUM,
            number=1,
            enum="RBACRoleBinding.Role.PredefinedRoles",
        )
        custom_role: str = proto.Field(
            proto.STRING,
            number=2,
        )

    user: str = proto.Field(
        proto.STRING,
        number=7,
        oneof="principal",
    )
    group: str = proto.Field(
        proto.STRING,
        number=8,
        oneof="principal",
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    delete_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    state: "RBACRoleBindingLifecycleState" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="RBACRoleBindingLifecycleState",
    )
    role: Role = proto.Field(
        proto.MESSAGE,
        number=9,
        message=Role,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=10,
    )


class RBACRoleBindingLifecycleState(proto.Message):
    r"""RBACRoleBindingLifecycleState describes the state of a
    RbacRoleBinding resource.

    Attributes:
        code (google.cloud.gkehub_v1.types.RBACRoleBindingLifecycleState.Code):
            Output only. The current state of the
            rbacrolebinding resource.
    """

    class Code(proto.Enum):
        r"""Code describes the state of a rbacrolebinding resource.

        Values:
            CODE_UNSPECIFIED (0):
                The code is not set.
            CREATING (1):
                The rbacrolebinding is being created.
            READY (2):
                The rbacrolebinding active.
            DELETING (3):
                The rbacrolebinding is being deleted.
            UPDATING (4):
                The rbacrolebinding is being updated.
        """

        CODE_UNSPECIFIED = 0
        CREATING = 1
        READY = 2
        DELETING = 3
        UPDATING = 4

    code: Code = proto.Field(
        proto.ENUM,
        number=1,
        enum=Code,
    )


class Scope(proto.Message):
    r"""Scope represents a Scope in a Fleet.

    Attributes:
        name (str):
            The resource name for the scope
            ``projects/{project}/locations/{location}/scopes/{scope}``
        uid (str):
            Output only. Google-generated UUID for this
            resource. This is unique across all scope
            resources. If a scope resource is deleted and
            another resource with the same name is created,
            it gets a different uid.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. When the scope was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. When the scope was last updated.
        delete_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. When the scope was deleted.
        state (google.cloud.gkehub_v1.types.ScopeLifecycleState):
            Output only. State of the scope resource.
        namespace_labels (MutableMapping[str, str]):
            Optional. Scope-level cluster namespace labels. For the
            member clusters bound to the Scope, these labels are applied
            to each namespace under the Scope. Scope-level labels take
            precedence over Namespace-level labels (``namespace_labels``
            in the Fleet Namespace resource) if they share a key. Keys
            and values must be Kubernetes-conformant.
        labels (MutableMapping[str, str]):
            Optional. Labels for this Scope.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    delete_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    state: "ScopeLifecycleState" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="ScopeLifecycleState",
    )
    namespace_labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=8,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=9,
    )


class ScopeLifecycleState(proto.Message):
    r"""ScopeLifecycleState describes the state of a Scope resource.

    Attributes:
        code (google.cloud.gkehub_v1.types.ScopeLifecycleState.Code):
            Output only. The current state of the scope
            resource.
    """

    class Code(proto.Enum):
        r"""Code describes the state of a Scope resource.

        Values:
            CODE_UNSPECIFIED (0):
                The code is not set.
            CREATING (1):
                The scope is being created.
            READY (2):
                The scope active.
            DELETING (3):
                The scope is being deleted.
            UPDATING (4):
                The scope is being updated.
        """

        CODE_UNSPECIFIED = 0
        CREATING = 1
        READY = 2
        DELETING = 3
        UPDATING = 4

    code: Code = proto.Field(
        proto.ENUM,
        number=1,
        enum=Code,
    )


class MembershipBinding(proto.Message):
    r"""MembershipBinding is a subresource of a Membership,
    representing what Fleet Scopes (or other, future Fleet
    resources) a Membership is bound to.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        scope (str):
            A Scope resource name in the format
            ``projects/*/locations/*/scopes/*``.

            This field is a member of `oneof`_ ``target``.
        name (str):
            The resource name for the membershipbinding itself
            ``projects/{project}/locations/{location}/memberships/{membership}/bindings/{membershipbinding}``
        uid (str):
            Output only. Google-generated UUID for this
            resource. This is unique across all
            membershipbinding resources. If a
            membershipbinding resource is deleted and
            another resource with the same name is created,
            it gets a different uid.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. When the membership binding was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. When the membership binding was
            last updated.
        delete_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. When the membership binding was
            deleted.
        state (google.cloud.gkehub_v1.types.MembershipBindingLifecycleState):
            Output only. State of the membership binding
            resource.
        labels (MutableMapping[str, str]):
            Optional. Labels for this MembershipBinding.
    """

    scope: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="target",
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    delete_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    state: "MembershipBindingLifecycleState" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="MembershipBindingLifecycleState",
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=9,
    )


class MembershipBindingLifecycleState(proto.Message):
    r"""MembershipBindingLifecycleState describes the state of a
    Binding resource.

    Attributes:
        code (google.cloud.gkehub_v1.types.MembershipBindingLifecycleState.Code):
            Output only. The current state of the
            MembershipBinding resource.
    """

    class Code(proto.Enum):
        r"""Code describes the state of a MembershipBinding resource.

        Values:
            CODE_UNSPECIFIED (0):
                The code is not set.
            CREATING (1):
                The membershipbinding is being created.
            READY (2):
                The membershipbinding active.
            DELETING (3):
                The membershipbinding is being deleted.
            UPDATING (4):
                The membershipbinding is being updated.
        """

        CODE_UNSPECIFIED = 0
        CREATING = 1
        READY = 2
        DELETING = 3
        UPDATING = 4

    code: Code = proto.Field(
        proto.ENUM,
        number=1,
        enum=Code,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
