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

import google.iam.v1.policy_pb2 as policy_pb2  # type: ignore
import google.type.expr_pb2 as expr_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.policytroubleshooter.v1",
    manifest={
        "AccessState",
        "HeuristicRelevance",
        "AccessTuple",
        "ExplainedPolicy",
        "BindingExplanation",
    },
)


class AccessState(proto.Enum):
    r"""Whether a principal has a permission for a resource.

    Values:
        ACCESS_STATE_UNSPECIFIED (0):
            Default value. This value is unused.
        GRANTED (1):
            The principal has the permission.
        NOT_GRANTED (2):
            The principal does not have the permission.
        UNKNOWN_CONDITIONAL (3):
            The principal has the permission only if a condition
            expression evaluates to ``true``.
        UNKNOWN_INFO_DENIED (4):
            The sender of the request does not have
            access to all of the policies that Policy
            Troubleshooter needs to evaluate.
    """

    ACCESS_STATE_UNSPECIFIED = 0
    GRANTED = 1
    NOT_GRANTED = 2
    UNKNOWN_CONDITIONAL = 3
    UNKNOWN_INFO_DENIED = 4


class HeuristicRelevance(proto.Enum):
    r"""The extent to which a single data point, such as the
    existence of a binding or whether a binding includes a specific
    principal, contributes to an overall determination.

    Values:
        HEURISTIC_RELEVANCE_UNSPECIFIED (0):
            Default value. This value is unused.
        NORMAL (1):
            The data point has a limited effect on the
            result. Changing the data point is unlikely to
            affect the overall determination.
        HIGH (2):
            The data point has a strong effect on the
            result. Changing the data point is likely to
            affect the overall determination.
    """

    HEURISTIC_RELEVANCE_UNSPECIFIED = 0
    NORMAL = 1
    HIGH = 2


class AccessTuple(proto.Message):
    r"""Information about the principal, resource, and permission to
    check.

    Attributes:
        principal (str):
            Required. The principal whose access you want to check, in
            the form of the email address that represents that
            principal. For example, ``alice@example.com`` or
            ``my-service-account@my-project.iam.gserviceaccount.com``.

            The principal must be a Google Account or a service account.
            Other types of principals are not supported.
        full_resource_name (str):
            Required. The full resource name that identifies the
            resource. For example,
            ``//compute.googleapis.com/projects/my-project/zones/us-central1-a/instances/my-instance``.

            For examples of full resource names for Google Cloud
            services, see
            https://cloud.google.com/iam/help/troubleshooter/full-resource-names.
        permission (str):
            Required. The IAM permission to check for the
            specified principal and resource.

            For a complete list of IAM permissions, see
            https://cloud.google.com/iam/help/permissions/reference.

            For a complete list of predefined IAM roles and
            the permissions in each role, see
            https://cloud.google.com/iam/help/roles/reference.
    """

    principal: str = proto.Field(
        proto.STRING,
        number=1,
    )
    full_resource_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    permission: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ExplainedPolicy(proto.Message):
    r"""Details about how a specific IAM [Policy][google.iam.v1.Policy]
    contributed to the access check.

    Attributes:
        access (google.cloud.policytroubleshooter_v1.types.AccessState):
            Indicates whether *this policy* provides the specified
            permission to the specified principal for the specified
            resource.

            This field does *not* indicate whether the principal
            actually has the permission for the resource. There might be
            another policy that overrides this policy. To determine
            whether the principal actually has the permission, use the
            ``access`` field in the
            [TroubleshootIamPolicyResponse][IamChecker.TroubleshootIamPolicyResponse].
        full_resource_name (str):
            The full resource name that identifies the resource. For
            example,
            ``//compute.googleapis.com/projects/my-project/zones/us-central1-a/instances/my-instance``.

            If the sender of the request does not have access to the
            policy, this field is omitted.

            For examples of full resource names for Google Cloud
            services, see
            https://cloud.google.com/iam/help/troubleshooter/full-resource-names.
        policy (google.iam.v1.policy_pb2.Policy):
            The IAM policy attached to the resource.

            If the sender of the request does not have
            access to the policy, this field is empty.
        binding_explanations (MutableSequence[google.cloud.policytroubleshooter_v1.types.BindingExplanation]):
            Details about how each binding in the policy
            affects the principal's ability, or inability,
            to use the permission for the resource.

            If the sender of the request does not have
            access to the policy, this field is omitted.
        relevance (google.cloud.policytroubleshooter_v1.types.HeuristicRelevance):
            The relevance of this policy to the overall determination in
            the
            [TroubleshootIamPolicyResponse][IamChecker.TroubleshootIamPolicyResponse].

            If the sender of the request does not have access to the
            policy, this field is omitted.
    """

    access: "AccessState" = proto.Field(
        proto.ENUM,
        number=1,
        enum="AccessState",
    )
    full_resource_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    policy: policy_pb2.Policy = proto.Field(
        proto.MESSAGE,
        number=3,
        message=policy_pb2.Policy,
    )
    binding_explanations: MutableSequence["BindingExplanation"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="BindingExplanation",
    )
    relevance: "HeuristicRelevance" = proto.Field(
        proto.ENUM,
        number=5,
        enum="HeuristicRelevance",
    )


class BindingExplanation(proto.Message):
    r"""Details about how a binding in a policy affects a principal's
    ability to use a permission.

    Attributes:
        access (google.cloud.policytroubleshooter_v1.types.AccessState):
            Required. Indicates whether *this binding* provides the
            specified permission to the specified principal for the
            specified resource.

            This field does *not* indicate whether the principal
            actually has the permission for the resource. There might be
            another binding that overrides this binding. To determine
            whether the principal actually has the permission, use the
            ``access`` field in the
            [TroubleshootIamPolicyResponse][IamChecker.TroubleshootIamPolicyResponse].
        role (str):
            The role that this binding grants. For example,
            ``roles/compute.serviceAgent``.

            For a complete list of predefined IAM roles, as well as the
            permissions in each role, see
            https://cloud.google.com/iam/help/roles/reference.
        role_permission (google.cloud.policytroubleshooter_v1.types.BindingExplanation.RolePermission):
            Indicates whether the role granted by this
            binding contains the specified permission.
        role_permission_relevance (google.cloud.policytroubleshooter_v1.types.HeuristicRelevance):
            The relevance of the permission's existence,
            or nonexistence, in the role to the overall
            determination for the entire policy.
        memberships (MutableMapping[str, google.cloud.policytroubleshooter_v1.types.BindingExplanation.AnnotatedMembership]):
            Indicates whether each principal in the binding includes the
            principal specified in the request, either directly or
            indirectly. Each key identifies a principal in the binding,
            and each value indicates whether the principal in the
            binding includes the principal in the request.

            For example, suppose that a binding includes the following
            principals:

            - ``user:alice@example.com``
            - ``group:product-eng@example.com``

            You want to troubleshoot access for
            ``user:bob@example.com``. This user is a principal of the
            group ``group:product-eng@example.com``.

            For the first principal in the binding, the key is
            ``user:alice@example.com``, and the ``membership`` field in
            the value is set to ``MEMBERSHIP_NOT_INCLUDED``.

            For the second principal in the binding, the key is
            ``group:product-eng@example.com``, and the ``membership``
            field in the value is set to ``MEMBERSHIP_INCLUDED``.
        relevance (google.cloud.policytroubleshooter_v1.types.HeuristicRelevance):
            The relevance of this binding to the overall
            determination for the entire policy.
        condition (google.type.expr_pb2.Expr):
            A condition expression that prevents this binding from
            granting access unless the expression evaluates to ``true``.

            To learn about IAM Conditions, see
            https://cloud.google.com/iam/help/conditions/overview.
    """

    class RolePermission(proto.Enum):
        r"""Whether a role includes a specific permission.

        Values:
            ROLE_PERMISSION_UNSPECIFIED (0):
                Default value. This value is unused.
            ROLE_PERMISSION_INCLUDED (1):
                The permission is included in the role.
            ROLE_PERMISSION_NOT_INCLUDED (2):
                The permission is not included in the role.
            ROLE_PERMISSION_UNKNOWN_INFO_DENIED (3):
                The sender of the request is not allowed to
                access the binding.
        """

        ROLE_PERMISSION_UNSPECIFIED = 0
        ROLE_PERMISSION_INCLUDED = 1
        ROLE_PERMISSION_NOT_INCLUDED = 2
        ROLE_PERMISSION_UNKNOWN_INFO_DENIED = 3

    class Membership(proto.Enum):
        r"""Whether the binding includes the principal.

        Values:
            MEMBERSHIP_UNSPECIFIED (0):
                Default value. This value is unused.
            MEMBERSHIP_INCLUDED (1):
                The binding includes the principal. The principal can be
                included directly or indirectly. For example:

                - A principal is included directly if that principal is
                  listed in the binding.
                - A principal is included indirectly if that principal is in
                  a Google group or Google Workspace domain that is listed
                  in the binding.
            MEMBERSHIP_NOT_INCLUDED (2):
                The binding does not include the principal.
            MEMBERSHIP_UNKNOWN_INFO_DENIED (3):
                The sender of the request is not allowed to
                access the binding.
            MEMBERSHIP_UNKNOWN_UNSUPPORTED (4):
                The principal is an unsupported type. Only
                Google Accounts and service accounts are
                supported.
        """

        MEMBERSHIP_UNSPECIFIED = 0
        MEMBERSHIP_INCLUDED = 1
        MEMBERSHIP_NOT_INCLUDED = 2
        MEMBERSHIP_UNKNOWN_INFO_DENIED = 3
        MEMBERSHIP_UNKNOWN_UNSUPPORTED = 4

    class AnnotatedMembership(proto.Message):
        r"""Details about whether the binding includes the principal.

        Attributes:
            membership (google.cloud.policytroubleshooter_v1.types.BindingExplanation.Membership):
                Indicates whether the binding includes the
                principal.
            relevance (google.cloud.policytroubleshooter_v1.types.HeuristicRelevance):
                The relevance of the principal's status to
                the overall determination for the binding.
        """

        membership: "BindingExplanation.Membership" = proto.Field(
            proto.ENUM,
            number=1,
            enum="BindingExplanation.Membership",
        )
        relevance: "HeuristicRelevance" = proto.Field(
            proto.ENUM,
            number=2,
            enum="HeuristicRelevance",
        )

    access: "AccessState" = proto.Field(
        proto.ENUM,
        number=1,
        enum="AccessState",
    )
    role: str = proto.Field(
        proto.STRING,
        number=2,
    )
    role_permission: RolePermission = proto.Field(
        proto.ENUM,
        number=3,
        enum=RolePermission,
    )
    role_permission_relevance: "HeuristicRelevance" = proto.Field(
        proto.ENUM,
        number=4,
        enum="HeuristicRelevance",
    )
    memberships: MutableMapping[str, AnnotatedMembership] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=5,
        message=AnnotatedMembership,
    )
    relevance: "HeuristicRelevance" = proto.Field(
        proto.ENUM,
        number=6,
        enum="HeuristicRelevance",
    )
    condition: expr_pb2.Expr = proto.Field(
        proto.MESSAGE,
        number=7,
        message=expr_pb2.Expr,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
