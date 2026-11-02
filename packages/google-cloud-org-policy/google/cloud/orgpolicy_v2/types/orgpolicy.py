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

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.type.expr_pb2 as expr_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.orgpolicy_v2.types import constraint

__protobuf__ = proto.module(
    package="google.cloud.orgpolicy.v2",
    manifest={
        "Policy",
        "AlternatePolicySpec",
        "PolicySpec",
        "ListConstraintsRequest",
        "ListConstraintsResponse",
        "ListPoliciesRequest",
        "ListPoliciesResponse",
        "GetPolicyRequest",
        "GetEffectivePolicyRequest",
        "CreatePolicyRequest",
        "UpdatePolicyRequest",
        "DeletePolicyRequest",
        "CreateCustomConstraintRequest",
        "GetCustomConstraintRequest",
        "ListCustomConstraintsRequest",
        "ListCustomConstraintsResponse",
        "UpdateCustomConstraintRequest",
        "DeleteCustomConstraintRequest",
    },
)


class Policy(proto.Message):
    r"""Defines an organization policy which is used to specify
    constraints for configurations of Google Cloud resources.

    Attributes:
        name (str):
            Immutable. The resource name of the policy. Must be one of
            the following forms, where ``constraint_name`` is the name
            of the constraint which this policy configures:

            - ``projects/{project_number}/policies/{constraint_name}``
            - ``folders/{folder_id}/policies/{constraint_name}``
            - ``organizations/{organization_id}/policies/{constraint_name}``

            For example,
            ``projects/123/policies/compute.disableSerialPortAccess``.

            Note: ``projects/{project_id}/policies/{constraint_name}``
            is also an acceptable name for API requests, but responses
            will return the name using the equivalent project number.
        spec (google.cloud.orgpolicy_v2.types.PolicySpec):
            Basic information about the organization
            policy.
        alternate (google.cloud.orgpolicy_v2.types.AlternatePolicySpec):
            Deprecated.
        dry_run_spec (google.cloud.orgpolicy_v2.types.PolicySpec):
            Dry-run policy.
            Audit-only policy, can be used to monitor how
            the policy would have impacted the existing and
            future resources if it's enforced.
        etag (str):
            Optional. An opaque tag indicating the
            current state of the policy, used for
            concurrency control. This 'etag' is computed by
            the server based on the value of other fields,
            and may be sent on update and delete requests to
            ensure the client has an up-to-date value before
            proceeding.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    spec: "PolicySpec" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="PolicySpec",
    )
    alternate: "AlternatePolicySpec" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="AlternatePolicySpec",
    )
    dry_run_spec: "PolicySpec" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="PolicySpec",
    )
    etag: str = proto.Field(
        proto.STRING,
        number=5,
    )


class AlternatePolicySpec(proto.Message):
    r"""Similar to PolicySpec but with an extra 'launch' field for
    launch reference. The PolicySpec here is specific for dry-run.

    Attributes:
        launch (str):
            Reference to the launch that will be used
            while audit logging and to control the launch.
            Should be set only in the alternate policy.
        spec (google.cloud.orgpolicy_v2.types.PolicySpec):
            Specify constraint for configurations of
            Google Cloud resources.
    """

    launch: str = proto.Field(
        proto.STRING,
        number=1,
    )
    spec: "PolicySpec" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="PolicySpec",
    )


class PolicySpec(proto.Message):
    r"""Defines a Google Cloud policy specification which is used to
    specify constraints for configurations of Google Cloud
    resources.

    Attributes:
        etag (str):
            An opaque tag indicating the current version of the
            policySpec, used for concurrency control.

            This field is ignored if used in a ``CreatePolicy`` request.

            When the policy is returned from either a ``GetPolicy`` or a
            ``ListPolicies`` request, this ``etag`` indicates the
            version of the current policySpec to use when executing a
            read-modify-write loop.

            When the policy is returned from a ``GetEffectivePolicy``
            request, the ``etag`` will be unset.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time stamp this was previously updated.
            This represents the last time a call to ``CreatePolicy`` or
            ``UpdatePolicy`` was made for that policy.
        rules (MutableSequence[google.cloud.orgpolicy_v2.types.PolicySpec.PolicyRule]):
            In policies for boolean constraints, the following
            requirements apply:

            - There must be one and only one policy rule where condition
              is unset.
            - Boolean policy rules with conditions must set ``enforced``
              to the opposite of the policy rule without a condition.
            - During policy evaluation, policy rules with conditions
              that are true for a target resource take precedence.
        inherit_from_parent (bool):
            Determines the inheritance behavior for this policy.

            If ``inherit_from_parent`` is true, policy rules set higher
            up in the hierarchy (up to the closest root) are inherited
            and present in the effective policy. If it is false, then no
            rules are inherited, and this policy becomes the new root
            for evaluation. This field can be set only for policies
            which configure list constraints.
        reset (bool):
            Ignores policies set above this resource and restores the
            ``constraint_default`` enforcement behavior of the specific
            constraint at this resource. This field can be set in
            policies for either list or boolean constraints. If set,
            ``rules`` must be empty and ``inherit_from_parent`` must be
            set to false.
    """

    class PolicyRule(proto.Message):
        r"""A rule used to express this policy.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            values (google.cloud.orgpolicy_v2.types.PolicySpec.PolicyRule.StringValues):
                List of values to be used for this policy
                rule. This field can be set only in policies for
                list constraints.

                This field is a member of `oneof`_ ``kind``.
            allow_all (bool):
                Setting this to true means that all values
                are allowed. This field can be set only in
                policies for list constraints.

                This field is a member of `oneof`_ ``kind``.
            deny_all (bool):
                Setting this to true means that all values
                are denied. This field can be set only in
                policies for list constraints.

                This field is a member of `oneof`_ ``kind``.
            enforce (bool):
                If ``true``, then the policy is enforced. If ``false``, then
                any configuration is acceptable. This field can be set only
                in policies for boolean constraints.

                This field is a member of `oneof`_ ``kind``.
            condition (google.type.expr_pb2.Expr):
                A condition which determines whether this rule is used in
                the evaluation of the policy. When set, the ``expression``
                field in the \`Expr' must include from 1 to 10
                subexpressions, joined by the "\|\|" or "&&" operators. Each
                subexpression must be of the form
                "resource.matchTag('<ORG_ID>/tag_key_short_name,
                'tag_value_short_name')". or
                "resource.matchTagId('tagKeys/key_id',
                'tagValues/value_id')". where key_name and value_name are
                the resource names for Label Keys and Values. These names
                are available from the Tag Manager Service. An example
                expression is: "resource.matchTag('123456789/environment,
                'prod')". or "resource.matchTagId('tagKeys/123',
                'tagValues/456')".
            parameters (google.protobuf.struct_pb2.Struct):
                Optional. Required for managed constraints if parameters are
                defined. Passes parameter values when policy enforcement is
                enabled. Ensure that parameter value types match those
                defined in the constraint definition. For example: {
                "allowedLocations" : ["us-east1", "us-west1"], "allowAll" :
                true }
        """

        class StringValues(proto.Message):
            r"""A message that holds specific allowed and denied values. This
            message can define specific values and subtrees of the Resource
            Manager resource hierarchy (``Organizations``, ``Folders``,
            ``Projects``) that are allowed or denied. This is achieved by using
            the ``under:`` and optional ``is:`` prefixes. The ``under:`` prefix
            is used to denote resource subtree values. The ``is:`` prefix is
            used to denote specific values, and is required only if the value
            contains a ":". Values prefixed with "is:" are treated the same as
            values with no prefix. Ancestry subtrees must be in one of the
            following formats:

            - ``projects/<project-id>`` (for example,
              ``projects/tokyo-rain-123``)
            - ``folders/<folder-id>`` (for example, ``folders/1234``)
            - ``organizations/<organization-id>`` (for example,
              ``organizations/1234``)

            The ``supports_under`` field of the associated ``Constraint``
            defines whether ancestry prefixes can be used.

            Attributes:
                allowed_values (MutableSequence[str]):
                    List of values allowed at this resource.
                denied_values (MutableSequence[str]):
                    List of values denied at this resource.
            """

            allowed_values: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=1,
            )
            denied_values: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=2,
            )

        values: "PolicySpec.PolicyRule.StringValues" = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="kind",
            message="PolicySpec.PolicyRule.StringValues",
        )
        allow_all: bool = proto.Field(
            proto.BOOL,
            number=2,
            oneof="kind",
        )
        deny_all: bool = proto.Field(
            proto.BOOL,
            number=3,
            oneof="kind",
        )
        enforce: bool = proto.Field(
            proto.BOOL,
            number=4,
            oneof="kind",
        )
        condition: expr_pb2.Expr = proto.Field(
            proto.MESSAGE,
            number=5,
            message=expr_pb2.Expr,
        )
        parameters: struct_pb2.Struct = proto.Field(
            proto.MESSAGE,
            number=6,
            message=struct_pb2.Struct,
        )

    etag: str = proto.Field(
        proto.STRING,
        number=1,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    rules: MutableSequence[PolicyRule] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=PolicyRule,
    )
    inherit_from_parent: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    reset: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class ListConstraintsRequest(proto.Message):
    r"""The request sent to the [ListConstraints]
    [google.cloud.orgpolicy.v2.OrgPolicy.ListConstraints] method.

    Attributes:
        parent (str):
            Required. The Google Cloud resource that parents the
            constraint. Must be in one of the following forms:

            - ``projects/{project_number}``
            - ``projects/{project_id}``
            - ``folders/{folder_id}``
            - ``organizations/{organization_id}``
        page_size (int):
            Size of the pages to be returned. This is
            currently unsupported and will be ignored. The
            server may at any point start using this field
            to limit page size.
        page_token (str):
            Page token used to retrieve the next page.
            This is currently unsupported and will be
            ignored. The server may at any point start using
            this field.
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


class ListConstraintsResponse(proto.Message):
    r"""The response returned from the [ListConstraints]
    [google.cloud.orgpolicy.v2.OrgPolicy.ListConstraints] method.

    Attributes:
        constraints (MutableSequence[google.cloud.orgpolicy_v2.types.Constraint]):
            The collection of constraints that are
            available on the targeted resource.
        next_page_token (str):
            Page token used to retrieve the next page.
            This is currently not used.
    """

    @property
    def raw_page(self):
        return self

    constraints: MutableSequence[constraint.Constraint] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=constraint.Constraint,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListPoliciesRequest(proto.Message):
    r"""The request sent to the [ListPolicies]
    [google.cloud.orgpolicy.v2.OrgPolicy.ListPolicies] method.

    Attributes:
        parent (str):
            Required. The target Google Cloud resource that parents the
            set of constraints and policies that will be returned from
            this call. Must be in one of the following forms:

            - ``projects/{project_number}``
            - ``projects/{project_id}``
            - ``folders/{folder_id}``
            - ``organizations/{organization_id}``
        page_size (int):
            Size of the pages to be returned. This is
            currently unsupported and will be ignored. The
            server may at any point start using this field
            to limit page size.
        page_token (str):
            Page token used to retrieve the next page.
            This is currently unsupported and will be
            ignored. The server may at any point start using
            this field.
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


class ListPoliciesResponse(proto.Message):
    r"""The response returned from the [ListPolicies]
    [google.cloud.orgpolicy.v2.OrgPolicy.ListPolicies] method. It will
    be empty if no policies are set on the resource.

    Attributes:
        policies (MutableSequence[google.cloud.orgpolicy_v2.types.Policy]):
            All policies that exist on the resource. It
            will be empty if no policies are set.
        next_page_token (str):
            Page token used to retrieve the next page.
            This is currently not used, but the server may
            at any point start supplying a valid token.
    """

    @property
    def raw_page(self):
        return self

    policies: MutableSequence["Policy"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Policy",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetPolicyRequest(proto.Message):
    r"""The request sent to the [GetPolicy]
    [google.cloud.orgpolicy.v2.OrgPolicy.GetPolicy] method.

    Attributes:
        name (str):
            Required. Resource name of the policy. See
            [Policy][google.cloud.orgpolicy.v2.Policy] for naming
            requirements.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetEffectivePolicyRequest(proto.Message):
    r"""The request sent to the [GetEffectivePolicy]
    [google.cloud.orgpolicy.v2.OrgPolicy.GetEffectivePolicy] method.

    Attributes:
        name (str):
            Required. The effective policy to compute. See
            [Policy][google.cloud.orgpolicy.v2.Policy] for naming
            requirements.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreatePolicyRequest(proto.Message):
    r"""The request sent to the [CreatePolicyRequest]
    [google.cloud.orgpolicy.v2.OrgPolicy.CreatePolicy] method.

    Attributes:
        parent (str):
            Required. The Google Cloud resource that will parent the new
            policy. Must be in one of the following forms:

            - ``projects/{project_number}``
            - ``projects/{project_id}``
            - ``folders/{folder_id}``
            - ``organizations/{organization_id}``
        policy (google.cloud.orgpolicy_v2.types.Policy):
            Required. Policy to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    policy: "Policy" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Policy",
    )


class UpdatePolicyRequest(proto.Message):
    r"""The request sent to the [UpdatePolicyRequest]
    [google.cloud.orgpolicy.v2.OrgPolicy.UpdatePolicy] method.

    Attributes:
        policy (google.cloud.orgpolicy_v2.types.Policy):
            Required. Policy to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Field mask used to specify the fields to be overwritten in
            the policy by the set. The fields specified in the
            update_mask are relative to the policy, not the full
            request.
    """

    policy: "Policy" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Policy",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=3,
        message=field_mask_pb2.FieldMask,
    )


class DeletePolicyRequest(proto.Message):
    r"""The request sent to the [DeletePolicy]
    [google.cloud.orgpolicy.v2.OrgPolicy.DeletePolicy] method.

    Attributes:
        name (str):
            Required. Name of the policy to delete.
            See the policy entry for naming rules.
        etag (str):
            Optional. The current etag of policy. If an
            etag is provided and does not match the current
            etag of the policy, deletion will be blocked and
            an ABORTED error will be returned.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateCustomConstraintRequest(proto.Message):
    r"""The request sent to the [CreateCustomConstraintRequest]
    [google.cloud.orgpolicy.v2.OrgPolicy.CreateCustomConstraint] method.

    Attributes:
        parent (str):
            Required. Must be in the following form:

            - ``organizations/{organization_id}``
        custom_constraint (google.cloud.orgpolicy_v2.types.CustomConstraint):
            Required. Custom constraint to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    custom_constraint: constraint.CustomConstraint = proto.Field(
        proto.MESSAGE,
        number=2,
        message=constraint.CustomConstraint,
    )


class GetCustomConstraintRequest(proto.Message):
    r"""The request sent to the [GetCustomConstraint]
    [google.cloud.orgpolicy.v2.OrgPolicy.GetCustomConstraint] method.

    Attributes:
        name (str):
            Required. Resource name of the custom or
            managed constraint. See the custom constraint
            entry for naming requirements.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListCustomConstraintsRequest(proto.Message):
    r"""The request sent to the [ListCustomConstraints]
    [google.cloud.orgpolicy.v2.OrgPolicy.ListCustomConstraints] method.

    Attributes:
        parent (str):
            Required. The target Google Cloud resource that parents the
            set of custom constraints that will be returned from this
            call. Must be in one of the following forms:

            - ``organizations/{organization_id}``
        page_size (int):
            Size of the pages to be returned. This is
            currently unsupported and will be ignored. The
            server may at any point start using this field
            to limit page size.
        page_token (str):
            Page token used to retrieve the next page.
            This is currently unsupported and will be
            ignored. The server may at any point start using
            this field.
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


class ListCustomConstraintsResponse(proto.Message):
    r"""The response returned from the [ListCustomConstraints]
    [google.cloud.orgpolicy.v2.OrgPolicy.ListCustomConstraints] method.
    It will be empty if no custom or managed constraints are set on the
    organization resource.

    Attributes:
        custom_constraints (MutableSequence[google.cloud.orgpolicy_v2.types.CustomConstraint]):
            All custom and managed constraints that exist
            on the organization resource. It will be empty
            if no custom constraints are set.
        next_page_token (str):
            Page token used to retrieve the next page.
            This is currently not used, but the server may
            at any point start supplying a valid token.
    """

    @property
    def raw_page(self):
        return self

    custom_constraints: MutableSequence[constraint.CustomConstraint] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=constraint.CustomConstraint,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UpdateCustomConstraintRequest(proto.Message):
    r"""The request sent to the [UpdateCustomConstraintRequest]
    [google.cloud.orgpolicy.v2.OrgPolicy.UpdateCustomConstraint] method.

    Attributes:
        custom_constraint (google.cloud.orgpolicy_v2.types.CustomConstraint):
            Required. ``CustomConstraint`` to update.
    """

    custom_constraint: constraint.CustomConstraint = proto.Field(
        proto.MESSAGE,
        number=1,
        message=constraint.CustomConstraint,
    )


class DeleteCustomConstraintRequest(proto.Message):
    r"""The request sent to the [DeleteCustomConstraint]
    [google.cloud.orgpolicy.v2.OrgPolicy.DeleteCustomConstraint] method.

    Attributes:
        name (str):
            Required. Name of the custom constraint to
            delete. See the custom constraint entry for
            naming rules.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
