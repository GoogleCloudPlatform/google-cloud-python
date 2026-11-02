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
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.backupdr.v1beta",
    manifest={
        "AutoProtectionPolicy",
        "BackupPlanDetail",
        "Criteria",
        "MatchingCondition",
        "PolicyEvaluationSummary",
        "BindingSummary",
        "KeyValuePair",
        "CreateAutoProtectionPolicyRequest",
        "GetAutoProtectionPolicyRequest",
        "UpdateAutoProtectionPolicyRequest",
        "DeleteAutoProtectionPolicyRequest",
        "ListAutoProtectionPoliciesRequest",
        "ListAutoProtectionPoliciesResponse",
    },
)


class AutoProtectionPolicy(proto.Message):
    r"""An AutoprotectionPolicy is a policy resource designed to
    automate backup management, moving from manual per-resource
    protection to a bulk approach. The policy dynamically discovers
    and applies a specified backup plan to all eligible resources
    that match its defined scope and criteria.

    Attributes:
        name (str):
            Identifier. The resource name of the AutoprotectionPolicy.
            Format:
            ``projects/{project}/locations/{location}/autoProtectionPolicies/{auto_protection_policy}``
        description (str):
            Optional. A description of the policy.
        backup_plan_details (MutableSequence[google.cloud.backupdr_v1beta.types.BackupPlanDetail]):
            Required. The backup plan details for
            matching resources.
        criteria (google.cloud.backupdr_v1beta.types.Criteria):
            Required. The criteria for matching
            resources.
        state (google.cloud.backupdr_v1beta.types.AutoProtectionPolicy.State):
            Output only. The current state of the
            AutoprotectionPolicy.
        etag (str):
            Output only. The etag for the policy.
            If this is provided on update, it must match the
            server's etag, otherwise the request will be
            rejected with an ABORTED error.
        binding_summary (google.cloud.backupdr_v1beta.types.BindingSummary):
            Output only. Summary of total count of
            different containers covered through this
            policy.
        policy_evaluation_summary (google.cloud.backupdr_v1beta.types.PolicyEvaluationSummary):
            Output only. Summary of last policy
            application when job was run per workload type.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the policy
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the policy
            was last updated.
    """

    class State(proto.Enum):
        r"""The state of an AutoprotectionPolicy.

        Values:
            STATE_UNSPECIFIED (0):
                The state of the policy is unspecified.
            CREATING (1):
                The policy is being created.
            ACTIVE (2):
                The policy is active and protecting matching
                resources.
            UPDATING (3):
                The policy is being updated.
            DELETING (4):
                The policy is being deleted.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        ACTIVE = 2
        UPDATING = 3
        DELETING = 4

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    backup_plan_details: MutableSequence["BackupPlanDetail"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="BackupPlanDetail",
    )
    criteria: "Criteria" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="Criteria",
    )
    state: State = proto.Field(
        proto.ENUM,
        number=5,
        enum=State,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=6,
    )
    binding_summary: "BindingSummary" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="BindingSummary",
    )
    policy_evaluation_summary: "PolicyEvaluationSummary" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="PolicyEvaluationSummary",
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )


class BackupPlanDetail(proto.Message):
    r"""BackupPlanDetail defines configuration of protection.

    Attributes:
        resource_type (str):
            Required. The type of resource that this policy will
            automatically protect. For MVP,
            ``compute.googleapis.com/Instance`` and
            ``compute.googleapis.com/Disk`` are supported.
        backup_plan (str):
            Required. The resource name of the BackupPlan
            to apply to resources that match the policy's
            criteria. This backup plan must be in the same
            location as AutoProtectionPolicy. Format:

            projects/{project}/locations/{location}/backupPlans/{backupPlanId}
    """

    resource_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    backup_plan: str = proto.Field(
        proto.STRING,
        number=2,
    )


class Criteria(proto.Message):
    r"""Criteria specifies a set of criteria for matching resources.

    Attributes:
        matching_conditions (MutableSequence[google.cloud.backupdr_v1beta.types.MatchingCondition]):
            Required. A list of matching conditions that
            a resource must meet to be protected by the
            policy.
    """

    matching_conditions: MutableSequence["MatchingCondition"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="MatchingCondition",
    )


class MatchingCondition(proto.Message):
    r"""MatchingCondition specifies a set of conditions for matching
    resources.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        label_condition (google.cloud.backupdr_v1beta.types.KeyValuePair):
            Optional. A condition that matches resources
            based on their labels. For MVP, this is limited
            to a single label match.

            This field is a member of `oneof`_ ``condition``.
    """

    label_condition: "KeyValuePair" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="condition",
        message="KeyValuePair",
    )


class PolicyEvaluationSummary(proto.Message):
    r"""PolicyEvaluationSummary contains the summary of the last run
    of job that applies policy to matching resources.

    Attributes:
        matching_resource_count (int):
            Output only. The number of resources that
            currently match the policy's criteria.
        protected_resource_count (int):
            Output only. The number of matching resources
            that are successfully protected.
        failed_resource_count (int):
            Output only. The number of matching resources
            whose protection failed during job run.
    """

    matching_resource_count: int = proto.Field(
        proto.INT64,
        number=1,
    )
    protected_resource_count: int = proto.Field(
        proto.INT64,
        number=2,
    )
    failed_resource_count: int = proto.Field(
        proto.INT64,
        number=3,
    )


class BindingSummary(proto.Message):
    r"""BindingSummary contains count of different containers covered
    through this policy.

    Attributes:
        project_count (int):
            Output only. Total count of Projects
            protected with this policy.
    """

    project_count: int = proto.Field(
        proto.INT64,
        number=1,
    )


class KeyValuePair(proto.Message):
    r"""KeyValuePair defines a key-value pair for matching resource
    labels.

    Attributes:
        key (str):
            Required. The key of the label to match. This must be in the
            format ``{label_key}``. The key must match the regex
            Format:``[\p{Ll}\p{Lo}][\p{Ll}\p{Lo}\p{N}_-]{0,62}``.
        values (MutableSequence[str]):
            Required. The values of the label to match. There will be
            explicit “OR” between values of array. Each value must be in
            the format ``{label_value}``. The value must match the regex
            Format: ``[\\p{Ll}\\p{Lo}\\p{N}_-]{1,63}``.
    """

    key: str = proto.Field(
        proto.STRING,
        number=1,
    )
    values: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class CreateAutoProtectionPolicyRequest(proto.Message):
    r"""Request message for creating an AutoProtectionPolicy.

    Attributes:
        parent (str):
            Required. The parent resource where this
            policy will be created. Format:
            projects/{project}/locations/{location}
        auto_protection_policy_id (str):
            Required. The ID to use for the policy.
            This will become the final component of the
            policy's resource name.
        auto_protection_policy (google.cloud.backupdr_v1beta.types.AutoProtectionPolicy):
            Required. The AutoProtectionPolicy resource
            to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    auto_protection_policy_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    auto_protection_policy: "AutoProtectionPolicy" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="AutoProtectionPolicy",
    )


class GetAutoProtectionPolicyRequest(proto.Message):
    r"""Request message for getting an AutoProtectionPolicy.

    Attributes:
        name (str):
            Required. The name of the policy to retrieve. Format:
            projects/{project}/locations/{location}/autoProtectionPolicies/{auto_protection_policy}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateAutoProtectionPolicyRequest(proto.Message):
    r"""Request message for updating an AutoProtectionPolicy.

    Attributes:
        auto_protection_policy (google.cloud.backupdr_v1beta.types.AutoProtectionPolicy):
            Required. The policy to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten in the AutoProtectionPolicy resource by the
            update. The fields specified in the update_mask are relative
            to the resource, not the full request. A field will be
            overwritten if it is in the mask. If the user does not
            provide a mask then all fields will be overwritten.
    """

    auto_protection_policy: "AutoProtectionPolicy" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="AutoProtectionPolicy",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteAutoProtectionPolicyRequest(proto.Message):
    r"""Request message for deleting an AutoProtectionPolicy.

    Attributes:
        name (str):
            Required. The name of the policy to delete. Format:
            projects/{project}/locations/{location}/autoProtectionPolicies/{auto_protection_policy}
        etag (str):
            The current etag of the AutoProtectionPolicy.
            If an etag is provided and does not match the
            current etag of the connection, the request will
            be rejected with an ABORTED error.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListAutoProtectionPoliciesRequest(proto.Message):
    r"""Request message for ListAutoProtectionPolicies.

    Attributes:
        parent (str):
            Required. The project and location for which
            to retrieve the list of policies. Format:
            projects/{project}/locations/{location}
        page_size (int):
            Optional. The maximum number of policies to
            return in a single page. If unspecified, a
            server-default value will be used.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListAutoProtectionPolicies`` call. Provide this to
            retrieve the subsequent page.
        filter (str):
            Optional. A filter expression that filters
            resources listed in the response. The following
            fields are filterable:
        order_by (str):
            Optional. An expression that sorts the
            results in the response. The following fields
            are sortable:
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


class ListAutoProtectionPoliciesResponse(proto.Message):
    r"""Response message for ListAutoProtectionPolicies.

    Attributes:
        auto_protection_policies (MutableSequence[google.cloud.backupdr_v1beta.types.AutoProtectionPolicy]):
            A list of the AutoProtectionPolicy resources
            found.
        next_page_token (str):
            A token that can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    auto_protection_policies: MutableSequence["AutoProtectionPolicy"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="AutoProtectionPolicy",
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


__all__ = tuple(sorted(__protobuf__.manifest))
