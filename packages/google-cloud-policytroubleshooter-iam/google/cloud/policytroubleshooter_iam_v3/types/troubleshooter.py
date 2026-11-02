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
import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.rpc.status_pb2 as status_pb2  # type: ignore
import google.type.expr_pb2 as expr_pb2  # type: ignore
import proto  # type: ignore
from google.cloud.iam_v2 import Policy  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.policytroubleshooter.iam.v3",
    manifest={
        "AllowAccessState",
        "DenyAccessState",
        "RolePermissionInclusionState",
        "PermissionPatternMatchingState",
        "MembershipMatchingState",
        "HeuristicRelevance",
        "TroubleshootIamPolicyRequest",
        "TroubleshootIamPolicyResponse",
        "AccessTuple",
        "ConditionContext",
        "AllowPolicyExplanation",
        "ExplainedAllowPolicy",
        "AllowBindingExplanation",
        "DenyPolicyExplanation",
        "ExplainedDenyResource",
        "ExplainedDenyPolicy",
        "DenyRuleExplanation",
        "ConditionExplanation",
    },
)


class AllowAccessState(proto.Enum):
    r"""Whether IAM allow policies gives the principal the
    permission.

    Values:
        ALLOW_ACCESS_STATE_UNSPECIFIED (0):
            Not specified.
        ALLOW_ACCESS_STATE_GRANTED (1):
            The allow policy gives the principal the
            permission.
        ALLOW_ACCESS_STATE_NOT_GRANTED (2):
            The allow policy doesn't give the principal
            the permission.
        ALLOW_ACCESS_STATE_UNKNOWN_CONDITIONAL (3):
            The allow policy gives the principal the permission if a
            condition expression evaluate to ``true``. However, the
            sender of the request didn't provide enough context for
            Policy Troubleshooter to evaluate the condition expression.
        ALLOW_ACCESS_STATE_UNKNOWN_INFO (4):
            The sender of the request doesn't have access
            to all of the allow policies that Policy
            Troubleshooter needs to evaluate the principal's
            access.
    """

    ALLOW_ACCESS_STATE_UNSPECIFIED = 0
    ALLOW_ACCESS_STATE_GRANTED = 1
    ALLOW_ACCESS_STATE_NOT_GRANTED = 2
    ALLOW_ACCESS_STATE_UNKNOWN_CONDITIONAL = 3
    ALLOW_ACCESS_STATE_UNKNOWN_INFO = 4


class DenyAccessState(proto.Enum):
    r"""Whether IAM deny policies deny the principal the permission.

    Values:
        DENY_ACCESS_STATE_UNSPECIFIED (0):
            Not specified.
        DENY_ACCESS_STATE_DENIED (1):
            The deny policy denies the principal the
            permission.
        DENY_ACCESS_STATE_NOT_DENIED (2):
            The deny policy doesn't deny the principal
            the permission.
        DENY_ACCESS_STATE_UNKNOWN_CONDITIONAL (3):
            The deny policy denies the principal the permission if a
            condition expression evaluates to ``true``. However, the
            sender of the request didn't provide enough context for
            Policy Troubleshooter to evaluate the condition expression.
        DENY_ACCESS_STATE_UNKNOWN_INFO (4):
            The sender of the request does not have
            access to all of the deny policies that Policy
            Troubleshooter needs to evaluate the principal's
            access.
    """

    DENY_ACCESS_STATE_UNSPECIFIED = 0
    DENY_ACCESS_STATE_DENIED = 1
    DENY_ACCESS_STATE_NOT_DENIED = 2
    DENY_ACCESS_STATE_UNKNOWN_CONDITIONAL = 3
    DENY_ACCESS_STATE_UNKNOWN_INFO = 4


class RolePermissionInclusionState(proto.Enum):
    r"""Whether a role includes a specific permission.

    Values:
        ROLE_PERMISSION_INCLUSION_STATE_UNSPECIFIED (0):
            Not specified.
        ROLE_PERMISSION_INCLUDED (1):
            The permission is included in the role.
        ROLE_PERMISSION_NOT_INCLUDED (2):
            The permission is not included in the role.
        ROLE_PERMISSION_UNKNOWN_INFO (3):
            The sender of the request is not allowed to
            access the role definition.
    """

    ROLE_PERMISSION_INCLUSION_STATE_UNSPECIFIED = 0
    ROLE_PERMISSION_INCLUDED = 1
    ROLE_PERMISSION_NOT_INCLUDED = 2
    ROLE_PERMISSION_UNKNOWN_INFO = 3


class PermissionPatternMatchingState(proto.Enum):
    r"""Whether the permission in the request matches the permission
    in the policy.

    Values:
        PERMISSION_PATTERN_MATCHING_STATE_UNSPECIFIED (0):
            Not specified.
        PERMISSION_PATTERN_MATCHED (1):
            The permission in the request matches the
            permission in the policy.
        PERMISSION_PATTERN_NOT_MATCHED (2):
            The permission in the request matches the
            permission in the policy.
    """

    PERMISSION_PATTERN_MATCHING_STATE_UNSPECIFIED = 0
    PERMISSION_PATTERN_MATCHED = 1
    PERMISSION_PATTERN_NOT_MATCHED = 2


class MembershipMatchingState(proto.Enum):
    r"""Whether the principal in the request matches the principal in
    the policy.

    Values:
        MEMBERSHIP_MATCHING_STATE_UNSPECIFIED (0):
            Not specified.
        MEMBERSHIP_MATCHED (1):
            The principal in the request matches the principal in the
            policy. The principal can be included directly or
            indirectly:

            - A principal is included directly if that principal is
              listed in the role binding.
            - A principal is included indirectly if that principal is in
              a Google group, Google Workspace account, or Cloud
              Identity domain that is listed in the policy.
        MEMBERSHIP_NOT_MATCHED (2):
            The principal in the request doesn't match
            the principal in the policy.
        MEMBERSHIP_UNKNOWN_INFO (3):
            The principal in the policy is a group or
            domain, and the sender of the request doesn't
            have permission to view whether the principal in
            the request is a member of the group or domain.
        MEMBERSHIP_UNKNOWN_UNSUPPORTED (4):
            The principal is an unsupported type.
    """

    MEMBERSHIP_MATCHING_STATE_UNSPECIFIED = 0
    MEMBERSHIP_MATCHED = 1
    MEMBERSHIP_NOT_MATCHED = 2
    MEMBERSHIP_UNKNOWN_INFO = 3
    MEMBERSHIP_UNKNOWN_UNSUPPORTED = 4


class HeuristicRelevance(proto.Enum):
    r"""The extent to which a single data point contributes to an
    overall determination.

    Values:
        HEURISTIC_RELEVANCE_UNSPECIFIED (0):
            Not specified.
        HEURISTIC_RELEVANCE_NORMAL (1):
            The data point has a limited effect on the
            result. Changing the data point is unlikely to
            affect the overall determination.
        HEURISTIC_RELEVANCE_HIGH (2):
            The data point has a strong effect on the
            result. Changing the data point is likely to
            affect the overall determination.
    """

    HEURISTIC_RELEVANCE_UNSPECIFIED = 0
    HEURISTIC_RELEVANCE_NORMAL = 1
    HEURISTIC_RELEVANCE_HIGH = 2


class TroubleshootIamPolicyRequest(proto.Message):
    r"""Request for
    [TroubleshootIamPolicy][google.cloud.policytroubleshooter.iam.v3.PolicyTroubleshooter.TroubleshootIamPolicy].

    Attributes:
        access_tuple (google.cloud.policytroubleshooter_iam_v3.types.AccessTuple):
            The information to use for checking whether a
            principal has a permission for a resource.
    """

    access_tuple: "AccessTuple" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="AccessTuple",
    )


class TroubleshootIamPolicyResponse(proto.Message):
    r"""Response for
    [TroubleshootIamPolicy][google.cloud.policytroubleshooter.iam.v3.PolicyTroubleshooter.TroubleshootIamPolicy].

    Attributes:
        overall_access_state (google.cloud.policytroubleshooter_iam_v3.types.TroubleshootIamPolicyResponse.OverallAccessState):
            Indicates whether the principal has the
            specified permission for the specified resource,
            based on evaluating all types of the applicable
            IAM policies.
        access_tuple (google.cloud.policytroubleshooter_iam_v3.types.AccessTuple):
            The access tuple from the request, including
            any provided context used to evaluate the
            condition.
        allow_policy_explanation (google.cloud.policytroubleshooter_iam_v3.types.AllowPolicyExplanation):
            An explanation of how the applicable IAM
            allow policies affect the final access state.
        deny_policy_explanation (google.cloud.policytroubleshooter_iam_v3.types.DenyPolicyExplanation):
            An explanation of how the applicable IAM deny
            policies affect the final access state.
    """

    class OverallAccessState(proto.Enum):
        r"""Whether the principal has the permission on the resource.

        Values:
            OVERALL_ACCESS_STATE_UNSPECIFIED (0):
                Not specified.
            CAN_ACCESS (1):
                The principal has the permission.
            CANNOT_ACCESS (2):
                The principal doesn't have the permission.
            UNKNOWN_INFO (3):
                The principal might have the permission, but
                the sender can't access all of the information
                needed to fully evaluate the principal's access.
            UNKNOWN_CONDITIONAL (4):
                The principal might have the permission, but
                Policy Troubleshooter can't fully evaluate the
                principal's access because the sender didn't
                provide the required context to evaluate the
                condition.
        """

        OVERALL_ACCESS_STATE_UNSPECIFIED = 0
        CAN_ACCESS = 1
        CANNOT_ACCESS = 2
        UNKNOWN_INFO = 3
        UNKNOWN_CONDITIONAL = 4

    overall_access_state: OverallAccessState = proto.Field(
        proto.ENUM,
        number=1,
        enum=OverallAccessState,
    )
    access_tuple: "AccessTuple" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="AccessTuple",
    )
    allow_policy_explanation: "AllowPolicyExplanation" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="AllowPolicyExplanation",
    )
    deny_policy_explanation: "DenyPolicyExplanation" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="DenyPolicyExplanation",
    )


class AccessTuple(proto.Message):
    r"""Information about the principal, resource, and permission to
    check.

    Attributes:
        principal (str):
            Required. The email address of the principal whose access
            you want to check. For example, ``alice@example.com`` or
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
            Required. The IAM permission to check for, either in the
            ``v1`` permission format or the ``v2`` permission format.

            For a complete list of IAM permissions in the ``v1`` format,
            see https://cloud.google.com/iam/help/permissions/reference.

            For a list of IAM permissions in the ``v2`` format, see
            https://cloud.google.com/iam/help/deny/supported-permissions.

            For a complete list of predefined IAM roles and the
            permissions in each role, see
            https://cloud.google.com/iam/help/roles/reference.
        permission_fqdn (str):
            Output only. The permission that Policy Troubleshooter
            checked for, in the ``v2`` format.
        condition_context (google.cloud.policytroubleshooter_iam_v3.types.ConditionContext):
            Optional. Additional context for the request,
            such as the request time or IP address. This
            context allows Policy Troubleshooter to
            troubleshoot conditional role bindings and deny
            rules.
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
    permission_fqdn: str = proto.Field(
        proto.STRING,
        number=4,
    )
    condition_context: "ConditionContext" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="ConditionContext",
    )


class ConditionContext(proto.Message):
    r"""Additional context for troubleshooting conditional role
    bindings and deny rules.

    Attributes:
        resource (google.cloud.policytroubleshooter_iam_v3.types.ConditionContext.Resource):
            Represents a target resource that is involved
            with a network activity. If multiple resources
            are involved with an activity, this must be the
            primary one.
        destination (google.cloud.policytroubleshooter_iam_v3.types.ConditionContext.Peer):
            The destination of a network activity, such
            as accepting a TCP connection. In a multi-hop
            network activity, the destination represents the
            receiver of the last hop.
        request (google.cloud.policytroubleshooter_iam_v3.types.ConditionContext.Request):
            Represents a network request, such as an HTTP
            request.
        effective_tags (MutableSequence[google.cloud.policytroubleshooter_iam_v3.types.ConditionContext.EffectiveTag]):
            Output only. The effective tags on the
            resource. The effective tags are fetched during
            troubleshooting.
    """

    class Resource(proto.Message):
        r"""Core attributes for a resource. A resource is an
        addressable (named) entity provided by the destination service.
        For example, a Compute Engine instance.

        Attributes:
            service (str):
                The name of the service that this resource belongs to, such
                as ``compute.googleapis.com``. The service name might not
                match the DNS hostname that actually serves the request.

                For a full list of resource service values, see
                https://cloud.google.com/iam/help/conditions/resource-services
            name (str):
                The stable identifier (name) of a resource on the
                ``service``. A resource can be logically identified as
                ``//{resource.service}/{resource.name}``. Unlike the
                resource URI, the resource name doesn't contain any protocol
                and version information.

                For a list of full resource name formats, see
                https://cloud.google.com/iam/help/troubleshooter/full-resource-names
            type_ (str):
                The type of the resource, in the format
                ``{service}/{kind}``.

                For a full list of resource type values, see
                https://cloud.google.com/iam/help/conditions/resource-types
        """

        service: str = proto.Field(
            proto.STRING,
            number=1,
        )
        name: str = proto.Field(
            proto.STRING,
            number=2,
        )
        type_: str = proto.Field(
            proto.STRING,
            number=3,
        )

    class Peer(proto.Message):
        r"""This message defines attributes for a node that handles a network
        request. The node can be either a service or an application that
        sends, forwards, or receives the request. Service peers should fill
        in ``principal`` and ``labels`` as appropriate.

        Attributes:
            ip (str):
                The IPv4 or IPv6 address of the peer.
            port (int):
                The network port of the peer.
        """

        ip: str = proto.Field(
            proto.STRING,
            number=1,
        )
        port: int = proto.Field(
            proto.INT64,
            number=2,
        )

    class Request(proto.Message):
        r"""This message defines attributes for an HTTP request. If the
        actual request is not an HTTP request, the runtime system should
        try to map the actual request to an equivalent HTTP request.

        Attributes:
            receive_time (google.protobuf.timestamp_pb2.Timestamp):
                Optional. The timestamp when the destination
                service receives the first byte of the request.
        """

        receive_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=1,
            message=timestamp_pb2.Timestamp,
        )

    class EffectiveTag(proto.Message):
        r"""A tag that applies to a resource during policy evaluation. Tags can
        be either directly bound to a resource or inherited from its
        ancestor. ``EffectiveTag`` contains the ``name`` and
        ``namespaced_name`` of the tag value and tag key, with additional
        fields of ``inherited`` to indicate the inheritance status of the
        effective tag.

        Attributes:
            tag_value (str):
                Output only. Resource name for TagValue in the format
                ``tagValues/456``.
            namespaced_tag_value (str):
                Output only. The namespaced name of the TagValue. Can be in
                the form
                ``{organization_id}/{tag_key_short_name}/{tag_value_short_name}``
                or
                ``{project_id}/{tag_key_short_name}/{tag_value_short_name}``
                or
                ``{project_number}/{tag_key_short_name}/{tag_value_short_name}``.
            tag_key (str):
                Output only. The name of the TagKey, in the format
                ``tagKeys/{id}``, such as ``tagKeys/123``.
            namespaced_tag_key (str):
                Output only. The namespaced name of the TagKey. Can be in
                the form ``{organization_id}/{tag_key_short_name}`` or
                ``{project_id}/{tag_key_short_name}`` or
                ``{project_number}/{tag_key_short_name}``.
            tag_key_parent_name (str):
                The parent name of the tag key. Must be in the format
                ``organizations/{organization_id}`` or
                ``projects/{project_number}``
            inherited (bool):
                Output only. Indicates the inheritance status
                of a tag value attached to the given resource.
                If the tag value is inherited from one of the
                resource's ancestors, inherited will be true. If
                false, then the tag value is directly attached
                to the resource, inherited will be false.
        """

        tag_value: str = proto.Field(
            proto.STRING,
            number=1,
        )
        namespaced_tag_value: str = proto.Field(
            proto.STRING,
            number=2,
        )
        tag_key: str = proto.Field(
            proto.STRING,
            number=3,
        )
        namespaced_tag_key: str = proto.Field(
            proto.STRING,
            number=4,
        )
        tag_key_parent_name: str = proto.Field(
            proto.STRING,
            number=6,
        )
        inherited: bool = proto.Field(
            proto.BOOL,
            number=5,
        )

    resource: Resource = proto.Field(
        proto.MESSAGE,
        number=1,
        message=Resource,
    )
    destination: Peer = proto.Field(
        proto.MESSAGE,
        number=2,
        message=Peer,
    )
    request: Request = proto.Field(
        proto.MESSAGE,
        number=3,
        message=Request,
    )
    effective_tags: MutableSequence[EffectiveTag] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=EffectiveTag,
    )


class AllowPolicyExplanation(proto.Message):
    r"""Details about how the relevant IAM allow policies affect the
    final access state.

    Attributes:
        allow_access_state (google.cloud.policytroubleshooter_iam_v3.types.AllowAccessState):
            Indicates whether the principal has the
            specified permission for the specified resource,
            based on evaluating all applicable IAM allow
            policies.
        explained_policies (MutableSequence[google.cloud.policytroubleshooter_iam_v3.types.ExplainedAllowPolicy]):
            List of IAM allow policies that were
            evaluated to check the principal's permissions,
            with annotations to indicate how each policy
            contributed to the final result.

            The list of policies includes the policy for the
            resource itself, as well as allow policies that
            are inherited from higher levels of the resource
            hierarchy, including the organization, the
            folder, and the project.

            To learn more about the resource hierarchy, see
            https://cloud.google.com/iam/help/resource-hierarchy.
        relevance (google.cloud.policytroubleshooter_iam_v3.types.HeuristicRelevance):
            The relevance of the allow policy type to the
            overall access state.
    """

    allow_access_state: "AllowAccessState" = proto.Field(
        proto.ENUM,
        number=1,
        enum="AllowAccessState",
    )
    explained_policies: MutableSequence["ExplainedAllowPolicy"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="ExplainedAllowPolicy",
    )
    relevance: "HeuristicRelevance" = proto.Field(
        proto.ENUM,
        number=3,
        enum="HeuristicRelevance",
    )


class ExplainedAllowPolicy(proto.Message):
    r"""Details about how a specific IAM allow policy contributed to
    the final access state.

    Attributes:
        allow_access_state (google.cloud.policytroubleshooter_iam_v3.types.AllowAccessState):
            Required. Indicates whether *this policy* provides the
            specified permission to the specified principal for the
            specified resource.

            This field does *not* indicate whether the principal
            actually has the permission for the resource. There might be
            another policy that overrides this policy. To determine
            whether the principal actually has the permission, use the
            ``overall_access_state`` field in the
            [TroubleshootIamPolicyResponse][google.cloud.policytroubleshooter.iam.v3.TroubleshootIamPolicyResponse].
        full_resource_name (str):
            The full resource name that identifies the resource. For
            example,
            ``//compute.googleapis.com/projects/my-project/zones/us-central1-a/instances/my-instance``.

            If the sender of the request does not have access to the
            policy, this field is omitted.

            For examples of full resource names for Google Cloud
            services, see
            https://cloud.google.com/iam/help/troubleshooter/full-resource-names.
        binding_explanations (MutableSequence[google.cloud.policytroubleshooter_iam_v3.types.AllowBindingExplanation]):
            Details about how each role binding in the
            policy affects the principal's ability, or
            inability, to use the permission for the
            resource. The order of the role bindings matches
            the role binding order in the policy.

            If the sender of the request does not have
            access to the policy, this field is omitted.
        relevance (google.cloud.policytroubleshooter_iam_v3.types.HeuristicRelevance):
            The relevance of this policy to the overall access state in
            the
            [TroubleshootIamPolicyResponse][google.cloud.policytroubleshooter.iam.v3.TroubleshootIamPolicyResponse].

            If the sender of the request does not have access to the
            policy, this field is omitted.
        policy (google.iam.v1.policy_pb2.Policy):
            The IAM allow policy attached to the
            resource.
            If the sender of the request does not have
            access to the policy, this field is empty.
    """

    allow_access_state: "AllowAccessState" = proto.Field(
        proto.ENUM,
        number=1,
        enum="AllowAccessState",
    )
    full_resource_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    binding_explanations: MutableSequence["AllowBindingExplanation"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message="AllowBindingExplanation",
        )
    )
    relevance: "HeuristicRelevance" = proto.Field(
        proto.ENUM,
        number=4,
        enum="HeuristicRelevance",
    )
    policy: policy_pb2.Policy = proto.Field(
        proto.MESSAGE,
        number=5,
        message=policy_pb2.Policy,
    )


class AllowBindingExplanation(proto.Message):
    r"""Details about how a role binding in an allow policy affects a
    principal's ability to use a permission.

    Attributes:
        allow_access_state (google.cloud.policytroubleshooter_iam_v3.types.AllowAccessState):
            Required. Indicates whether *this role binding* gives the
            specified permission to the specified principal on the
            specified resource.

            This field does *not* indicate whether the principal
            actually has the permission on the resource. There might be
            another role binding that overrides this role binding. To
            determine whether the principal actually has the permission,
            use the ``overall_access_state`` field in the
            [TroubleshootIamPolicyResponse][google.cloud.policytroubleshooter.iam.v3.TroubleshootIamPolicyResponse].
        role (str):
            The role that this role binding grants. For example,
            ``roles/compute.admin``.

            For a complete list of predefined IAM roles, as well as the
            permissions in each role, see
            https://cloud.google.com/iam/help/roles/reference.
        role_permission (google.cloud.policytroubleshooter_iam_v3.types.RolePermissionInclusionState):
            Indicates whether the role granted by this
            role binding contains the specified permission.
        role_permission_relevance (google.cloud.policytroubleshooter_iam_v3.types.HeuristicRelevance):
            The relevance of the permission's existence,
            or nonexistence, in the role to the overall
            determination for the entire policy.
        combined_membership (google.cloud.policytroubleshooter_iam_v3.types.AllowBindingExplanation.AnnotatedAllowMembership):
            The combined result of all memberships.
            Indicates if the principal is included in any
            role binding, either directly or indirectly.
        memberships (MutableMapping[str, google.cloud.policytroubleshooter_iam_v3.types.AllowBindingExplanation.AnnotatedAllowMembership]):
            Indicates whether each role binding includes the principal
            specified in the request, either directly or indirectly.
            Each key identifies a principal in the role binding, and
            each value indicates whether the principal in the role
            binding includes the principal in the request.

            For example, suppose that a role binding includes the
            following principals:

            - ``user:alice@example.com``
            - ``group:product-eng@example.com``

            You want to troubleshoot access for
            ``user:bob@example.com``. This user is a member of the group
            ``group:product-eng@example.com``.

            For the first principal in the role binding, the key is
            ``user:alice@example.com``, and the ``membership`` field in
            the value is set to ``NOT_INCLUDED``.

            For the second principal in the role binding, the key is
            ``group:product-eng@example.com``, and the ``membership``
            field in the value is set to ``INCLUDED``.
        relevance (google.cloud.policytroubleshooter_iam_v3.types.HeuristicRelevance):
            The relevance of this role binding to the
            overall determination for the entire policy.
        condition (google.type.expr_pb2.Expr):
            A condition expression that specifies when
            the role binding grants access.
            To learn about IAM Conditions, see
            https://cloud.google.com/iam/help/conditions/overview.
        condition_explanation (google.cloud.policytroubleshooter_iam_v3.types.ConditionExplanation):
            Condition evaluation state for this role
            binding.
    """

    class AnnotatedAllowMembership(proto.Message):
        r"""Details about whether the role binding includes the
        principal.

        Attributes:
            membership (google.cloud.policytroubleshooter_iam_v3.types.MembershipMatchingState):
                Indicates whether the role binding includes
                the principal.
            relevance (google.cloud.policytroubleshooter_iam_v3.types.HeuristicRelevance):
                The relevance of the principal's status to
                the overall determination for the role binding.
        """

        membership: "MembershipMatchingState" = proto.Field(
            proto.ENUM,
            number=1,
            enum="MembershipMatchingState",
        )
        relevance: "HeuristicRelevance" = proto.Field(
            proto.ENUM,
            number=2,
            enum="HeuristicRelevance",
        )

    allow_access_state: "AllowAccessState" = proto.Field(
        proto.ENUM,
        number=1,
        enum="AllowAccessState",
    )
    role: str = proto.Field(
        proto.STRING,
        number=2,
    )
    role_permission: "RolePermissionInclusionState" = proto.Field(
        proto.ENUM,
        number=3,
        enum="RolePermissionInclusionState",
    )
    role_permission_relevance: "HeuristicRelevance" = proto.Field(
        proto.ENUM,
        number=4,
        enum="HeuristicRelevance",
    )
    combined_membership: AnnotatedAllowMembership = proto.Field(
        proto.MESSAGE,
        number=5,
        message=AnnotatedAllowMembership,
    )
    memberships: MutableMapping[str, AnnotatedAllowMembership] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=6,
        message=AnnotatedAllowMembership,
    )
    relevance: "HeuristicRelevance" = proto.Field(
        proto.ENUM,
        number=7,
        enum="HeuristicRelevance",
    )
    condition: expr_pb2.Expr = proto.Field(
        proto.MESSAGE,
        number=8,
        message=expr_pb2.Expr,
    )
    condition_explanation: "ConditionExplanation" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="ConditionExplanation",
    )


class DenyPolicyExplanation(proto.Message):
    r"""Details about how the relevant IAM deny policies affect the
    final access state.

    Attributes:
        deny_access_state (google.cloud.policytroubleshooter_iam_v3.types.DenyAccessState):
            Indicates whether the principal is denied the
            specified permission for the specified resource,
            based on evaluating all applicable IAM deny
            policies.
        explained_resources (MutableSequence[google.cloud.policytroubleshooter_iam_v3.types.ExplainedDenyResource]):
            List of resources with IAM deny policies that
            were evaluated to check the principal's denied
            permissions, with annotations to indicate how
            each policy contributed to the final result.

            The list of resources includes the policy for
            the resource itself, as well as policies that
            are inherited from higher levels of the resource
            hierarchy, including the organization, the
            folder, and the project. The order of the
            resources starts from the resource and climbs up
            the resource hierarchy.

            To learn more about the resource hierarchy, see
            https://cloud.google.com/iam/help/resource-hierarchy.
        relevance (google.cloud.policytroubleshooter_iam_v3.types.HeuristicRelevance):
            The relevance of the deny policy result to
            the overall access state.
        permission_deniable (bool):
            Indicates whether the permission to
            troubleshoot is supported in deny policies.
    """

    deny_access_state: "DenyAccessState" = proto.Field(
        proto.ENUM,
        number=1,
        enum="DenyAccessState",
    )
    explained_resources: MutableSequence["ExplainedDenyResource"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="ExplainedDenyResource",
    )
    relevance: "HeuristicRelevance" = proto.Field(
        proto.ENUM,
        number=3,
        enum="HeuristicRelevance",
    )
    permission_deniable: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class ExplainedDenyResource(proto.Message):
    r"""Details about how a specific resource contributed to the deny
    policy evaluation.

    Attributes:
        deny_access_state (google.cloud.policytroubleshooter_iam_v3.types.DenyAccessState):
            Required. Indicates whether any policies attached to *this
            resource* deny the specific permission to the specified
            principal for the specified resource.

            This field does *not* indicate whether the principal
            actually has the permission for the resource. There might be
            another policy that overrides this policy. To determine
            whether the principal actually has the permission, use the
            ``overall_access_state`` field in the
            [TroubleshootIamPolicyResponse][google.cloud.policytroubleshooter.iam.v3.TroubleshootIamPolicyResponse].
        full_resource_name (str):
            The full resource name that identifies the resource. For
            example,
            ``//compute.googleapis.com/projects/my-project/zones/us-central1-a/instances/my-instance``.

            If the sender of the request does not have access to the
            policy, this field is omitted.

            For examples of full resource names for Google Cloud
            services, see
            https://cloud.google.com/iam/help/troubleshooter/full-resource-names.
        explained_policies (MutableSequence[google.cloud.policytroubleshooter_iam_v3.types.ExplainedDenyPolicy]):
            List of IAM deny policies that were evaluated
            to check the principal's denied permissions,
            with annotations to indicate how each policy
            contributed to the final result.
        relevance (google.cloud.policytroubleshooter_iam_v3.types.HeuristicRelevance):
            The relevance of this policy to the overall access state in
            the
            [TroubleshootIamPolicyResponse][google.cloud.policytroubleshooter.iam.v3.TroubleshootIamPolicyResponse].

            If the sender of the request does not have access to the
            policy, this field is omitted.
    """

    deny_access_state: "DenyAccessState" = proto.Field(
        proto.ENUM,
        number=1,
        enum="DenyAccessState",
    )
    full_resource_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    explained_policies: MutableSequence["ExplainedDenyPolicy"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="ExplainedDenyPolicy",
    )
    relevance: "HeuristicRelevance" = proto.Field(
        proto.ENUM,
        number=4,
        enum="HeuristicRelevance",
    )


class ExplainedDenyPolicy(proto.Message):
    r"""Details about how a specific IAM deny policy
    [Policy][google.iam.v2.Policy] contributed to the access check.

    Attributes:
        deny_access_state (google.cloud.policytroubleshooter_iam_v3.types.DenyAccessState):
            Required. Indicates whether *this policy* denies the
            specified permission to the specified principal for the
            specified resource.

            This field does *not* indicate whether the principal
            actually has the permission for the resource. There might be
            another policy that overrides this policy. To determine
            whether the principal actually has the permission, use the
            ``overall_access_state`` field in the
            [TroubleshootIamPolicyResponse][google.cloud.policytroubleshooter.iam.v3.TroubleshootIamPolicyResponse].
        policy (google.cloud.iam_v2.Policy):
            The IAM deny policy attached to the resource.

            If the sender of the request does not have
            access to the policy, this field is omitted.
        rule_explanations (MutableSequence[google.cloud.policytroubleshooter_iam_v3.types.DenyRuleExplanation]):
            Details about how each rule in the policy
            affects the principal's inability to use the
            permission for the resource. The order of the
            deny rule matches the order of the rules in the
            deny policy.

            If the sender of the request does not have
            access to the policy, this field is omitted.
        relevance (google.cloud.policytroubleshooter_iam_v3.types.HeuristicRelevance):
            The relevance of this policy to the overall access state in
            the
            [TroubleshootIamPolicyResponse][google.cloud.policytroubleshooter.iam.v3.TroubleshootIamPolicyResponse].

            If the sender of the request does not have access to the
            policy, this field is omitted.
    """

    deny_access_state: "DenyAccessState" = proto.Field(
        proto.ENUM,
        number=1,
        enum="DenyAccessState",
    )
    policy: Policy = proto.Field(
        proto.MESSAGE,
        number=2,
        message=Policy,
    )
    rule_explanations: MutableSequence["DenyRuleExplanation"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="DenyRuleExplanation",
    )
    relevance: "HeuristicRelevance" = proto.Field(
        proto.ENUM,
        number=4,
        enum="HeuristicRelevance",
    )


class DenyRuleExplanation(proto.Message):
    r"""Details about how a deny rule in a deny policy affects a
    principal's ability to use a permission.

    Attributes:
        deny_access_state (google.cloud.policytroubleshooter_iam_v3.types.DenyAccessState):
            Required. Indicates whether *this rule* denies the specified
            permission to the specified principal for the specified
            resource.

            This field does *not* indicate whether the principal is
            actually denied on the permission for the resource. There
            might be another rule that overrides this rule. To determine
            whether the principal actually has the permission, use the
            ``overall_access_state`` field in the
            [TroubleshootIamPolicyResponse][google.cloud.policytroubleshooter.iam.v3.TroubleshootIamPolicyResponse].
        combined_denied_permission (google.cloud.policytroubleshooter_iam_v3.types.DenyRuleExplanation.AnnotatedPermissionMatching):
            Indicates whether the permission in the
            request is listed as a denied permission in the
            deny rule.
        denied_permissions (MutableMapping[str, google.cloud.policytroubleshooter_iam_v3.types.DenyRuleExplanation.AnnotatedPermissionMatching]):
            Lists all denied permissions in the deny rule
            and indicates whether each permission matches
            the permission in the request.

            Each key identifies a denied permission in the
            rule, and each value indicates whether the
            denied permission matches the permission in the
            request.
        combined_exception_permission (google.cloud.policytroubleshooter_iam_v3.types.DenyRuleExplanation.AnnotatedPermissionMatching):
            Indicates whether the permission in the
            request is listed as an exception permission in
            the deny rule.
        exception_permissions (MutableMapping[str, google.cloud.policytroubleshooter_iam_v3.types.DenyRuleExplanation.AnnotatedPermissionMatching]):
            Lists all exception permissions in the deny
            rule and indicates whether each permission
            matches the permission in the request.

            Each key identifies a exception permission in
            the rule, and each value indicates whether the
            exception permission matches the permission in
            the request.
        combined_denied_principal (google.cloud.policytroubleshooter_iam_v3.types.DenyRuleExplanation.AnnotatedDenyPrincipalMatching):
            Indicates whether the principal is listed as
            a denied principal in the deny rule, either
            directly or through membership in a principal
            set.
        denied_principals (MutableMapping[str, google.cloud.policytroubleshooter_iam_v3.types.DenyRuleExplanation.AnnotatedDenyPrincipalMatching]):
            Lists all denied principals in the deny rule
            and indicates whether each principal matches the
            principal in the request, either directly or
            through membership in a principal set.

            Each key identifies a denied principal in the
            rule, and each value indicates whether the
            denied principal matches the principal in the
            request.
        combined_exception_principal (google.cloud.policytroubleshooter_iam_v3.types.DenyRuleExplanation.AnnotatedDenyPrincipalMatching):
            Indicates whether the principal is listed as
            an exception principal in the deny rule, either
            directly or through membership in a principal
            set.
        exception_principals (MutableMapping[str, google.cloud.policytroubleshooter_iam_v3.types.DenyRuleExplanation.AnnotatedDenyPrincipalMatching]):
            Lists all exception principals in the deny
            rule and indicates whether each principal
            matches the principal in the request, either
            directly or through membership in a principal
            set.

            Each key identifies a exception principal in the
            rule, and each value indicates whether the
            exception principal matches the principal in the
            request.
        relevance (google.cloud.policytroubleshooter_iam_v3.types.HeuristicRelevance):
            The relevance of this role binding to the
            overall determination for the entire policy.
        condition (google.type.expr_pb2.Expr):
            A condition expression that specifies when
            the deny rule denies the principal access.

            To learn about IAM Conditions, see
            https://cloud.google.com/iam/help/conditions/overview.
        condition_explanation (google.cloud.policytroubleshooter_iam_v3.types.ConditionExplanation):
            Condition evaluation state for this role
            binding.
    """

    class AnnotatedPermissionMatching(proto.Message):
        r"""Details about whether the permission in the request is denied
        by the deny rule.

        Attributes:
            permission_matching_state (google.cloud.policytroubleshooter_iam_v3.types.PermissionPatternMatchingState):
                Indicates whether the permission in the
                request is denied by the deny rule.
            relevance (google.cloud.policytroubleshooter_iam_v3.types.HeuristicRelevance):
                The relevance of the permission status to the
                overall determination for the rule.
        """

        permission_matching_state: "PermissionPatternMatchingState" = proto.Field(
            proto.ENUM,
            number=1,
            enum="PermissionPatternMatchingState",
        )
        relevance: "HeuristicRelevance" = proto.Field(
            proto.ENUM,
            number=2,
            enum="HeuristicRelevance",
        )

    class AnnotatedDenyPrincipalMatching(proto.Message):
        r"""Details about whether the principal in the request is listed
        as a denied principal in the deny rule, either directly or
        through membership in a principal set.

        Attributes:
            membership (google.cloud.policytroubleshooter_iam_v3.types.MembershipMatchingState):
                Indicates whether the principal is listed as
                a denied principal in the deny rule, either
                directly or through membership in a principal
                set.
            relevance (google.cloud.policytroubleshooter_iam_v3.types.HeuristicRelevance):
                The relevance of the principal's status to
                the overall determination for the role binding.
        """

        membership: "MembershipMatchingState" = proto.Field(
            proto.ENUM,
            number=1,
            enum="MembershipMatchingState",
        )
        relevance: "HeuristicRelevance" = proto.Field(
            proto.ENUM,
            number=2,
            enum="HeuristicRelevance",
        )

    deny_access_state: "DenyAccessState" = proto.Field(
        proto.ENUM,
        number=1,
        enum="DenyAccessState",
    )
    combined_denied_permission: AnnotatedPermissionMatching = proto.Field(
        proto.MESSAGE,
        number=2,
        message=AnnotatedPermissionMatching,
    )
    denied_permissions: MutableMapping[str, AnnotatedPermissionMatching] = (
        proto.MapField(
            proto.STRING,
            proto.MESSAGE,
            number=3,
            message=AnnotatedPermissionMatching,
        )
    )
    combined_exception_permission: AnnotatedPermissionMatching = proto.Field(
        proto.MESSAGE,
        number=4,
        message=AnnotatedPermissionMatching,
    )
    exception_permissions: MutableMapping[str, AnnotatedPermissionMatching] = (
        proto.MapField(
            proto.STRING,
            proto.MESSAGE,
            number=5,
            message=AnnotatedPermissionMatching,
        )
    )
    combined_denied_principal: AnnotatedDenyPrincipalMatching = proto.Field(
        proto.MESSAGE,
        number=6,
        message=AnnotatedDenyPrincipalMatching,
    )
    denied_principals: MutableMapping[str, AnnotatedDenyPrincipalMatching] = (
        proto.MapField(
            proto.STRING,
            proto.MESSAGE,
            number=7,
            message=AnnotatedDenyPrincipalMatching,
        )
    )
    combined_exception_principal: AnnotatedDenyPrincipalMatching = proto.Field(
        proto.MESSAGE,
        number=8,
        message=AnnotatedDenyPrincipalMatching,
    )
    exception_principals: MutableMapping[str, AnnotatedDenyPrincipalMatching] = (
        proto.MapField(
            proto.STRING,
            proto.MESSAGE,
            number=9,
            message=AnnotatedDenyPrincipalMatching,
        )
    )
    relevance: "HeuristicRelevance" = proto.Field(
        proto.ENUM,
        number=10,
        enum="HeuristicRelevance",
    )
    condition: expr_pb2.Expr = proto.Field(
        proto.MESSAGE,
        number=11,
        message=expr_pb2.Expr,
    )
    condition_explanation: "ConditionExplanation" = proto.Field(
        proto.MESSAGE,
        number=12,
        message="ConditionExplanation",
    )


class ConditionExplanation(proto.Message):
    r"""Explanation for how a condition affects a principal's access

    Attributes:
        value (google.protobuf.struct_pb2.Value):
            Value of the condition.
        errors (MutableSequence[google.rpc.status_pb2.Status]):
            Any errors that prevented complete evaluation
            of the condition expression.
        evaluation_states (MutableSequence[google.cloud.policytroubleshooter_iam_v3.types.ConditionExplanation.EvaluationState]):
            The value of each statement of the condition expression. The
            value can be ``true``, ``false``, or ``null``. The value is
            ``null`` if the statement can't be evaluated.
    """

    class EvaluationState(proto.Message):
        r"""Evaluated state of a condition expression.

        Attributes:
            start (int):
                Start position of an expression in the
                condition, by character.
            end (int):
                End position of an expression in the condition, by
                character, end included, for example: the end position of
                the first part of ``a==b || c==d`` would be 4.
            value (google.protobuf.struct_pb2.Value):
                Value of this expression.
            errors (MutableSequence[google.rpc.status_pb2.Status]):
                Any errors that prevented complete evaluation
                of the condition expression.
        """

        start: int = proto.Field(
            proto.INT32,
            number=1,
        )
        end: int = proto.Field(
            proto.INT32,
            number=2,
        )
        value: struct_pb2.Value = proto.Field(
            proto.MESSAGE,
            number=3,
            message=struct_pb2.Value,
        )
        errors: MutableSequence[status_pb2.Status] = proto.RepeatedField(
            proto.MESSAGE,
            number=4,
            message=status_pb2.Status,
        )

    value: struct_pb2.Value = proto.Field(
        proto.MESSAGE,
        number=1,
        message=struct_pb2.Value,
    )
    errors: MutableSequence[status_pb2.Status] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=status_pb2.Status,
    )
    evaluation_states: MutableSequence[EvaluationState] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=EvaluationState,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
