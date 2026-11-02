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

from google.cloud.backupdr_v1beta.types import (
    autoprotectionpolicy,
    autoprotectionpolicybinding,
)

__protobuf__ = proto.module(
    package="google.cloud.backupdr.v1beta",
    manifest={
        "AppliedAutoProtectionPolicy",
        "ListAppliedAutoProtectionPoliciesRequest",
        "ListAppliedAutoProtectionPoliciesResponse",
    },
)


class AppliedAutoProtectionPolicy(proto.Message):
    r"""AppliedAutoProtectionPolicy is a read-only view of
    AutoProtectionPolicy and AutoProtectionPolicyBinding resources
    that apply to a given workload project.

    Attributes:
        name (str):
            Identifier. Canonical resource name.
            Format:

            projects/{workload-project-number}/locations/{location}/appliedAutoProtectionPolicies/{id}.
        source_binding (str):
            Output only. The full resource name of the
            AutoProtectionPolicyBinding that applies the source policy
            to a scope including this workload project. e.g.,
            projects/{admin-project}/locations/{location}/autoProtectionPolicies/{policy_id}/autoProtectionPolicyBindings/{binding_id}.
        criteria (google.cloud.backupdr_v1beta.types.Criteria):
            Output only. The criteria resources must meet
            for this rule to apply. From
            AutoProtectionPolicy.criteria.
        backup_plan_details (MutableSequence[google.cloud.backupdr_v1beta.types.BackupPlanDetail]):
            Output only. The set of backup plan configurations,
            mirroring the backup_plan_details from the source
            AutoProtectionPolicy. Each element specifies a backup plan
            for a given resource type.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp indicating when the
            binding was last modified.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp indicating when the
            binding was last created.
        binding_evaluation_summary (google.cloud.backupdr_v1beta.types.BindingEvaluationSummary):
            Output only. The summary of the last policy
            application when the job has run.
        status (google.cloud.backupdr_v1beta.types.AppliedAutoProtectionPolicy.State):
            Output only. The status of the applied auto
            protection policy.
    """

    class State(proto.Enum):
        r"""Represents the various states an applied auto protection
        policy can be in.

        Values:
            STATE_UNSPECIFIED (0):
                State is not specified.
            CREATING (1):
                The policy is in the process of being
                applied.
            ACTIVE (2):
                The policy has been applied and is active.
            DELETION_INITIATED (3):
                The policy is in the process of being
                removed.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        ACTIVE = 2
        DELETION_INITIATED = 3

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    source_binding: str = proto.Field(
        proto.STRING,
        number=2,
    )
    criteria: autoprotectionpolicy.Criteria = proto.Field(
        proto.MESSAGE,
        number=3,
        message=autoprotectionpolicy.Criteria,
    )
    backup_plan_details: MutableSequence[autoprotectionpolicy.BackupPlanDetail] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=4,
            message=autoprotectionpolicy.BackupPlanDetail,
        )
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    binding_evaluation_summary: autoprotectionpolicybinding.BindingEvaluationSummary = (
        proto.Field(
            proto.MESSAGE,
            number=7,
            message=autoprotectionpolicybinding.BindingEvaluationSummary,
        )
    )
    status: State = proto.Field(
        proto.ENUM,
        number=8,
        enum=State,
    )


class ListAppliedAutoProtectionPoliciesRequest(proto.Message):
    r"""Request message for listing AppliedAutoProtectionPolicies.

    Attributes:
        parent (str):
            Required. The project and location for which
            to retrieve the list of applied policies.
            Format: projects/{project}/locations/{location}
        page_size (int):
            Optional. The maximum number of applied
            policies to return in a single page.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListAppliedAutoProtectionPolicies`` call.
        filter (str):
            Optional. A filter expression that filters
            resources listed in the response.
        order_by (str):
            Optional. An expression that sorts the
            results in the response.
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


class ListAppliedAutoProtectionPoliciesResponse(proto.Message):
    r"""Response message for ListAppliedAutoProtectionPolicies.

    Attributes:
        applied_auto_protection_policies (MutableSequence[google.cloud.backupdr_v1beta.types.AppliedAutoProtectionPolicy]):
            A list of the AppliedAutoProtectionPolicy
            resources found.
        next_page_token (str):
            A token that can be sent as ``page_token`` to retrieve the
            next page.
        unreachable (MutableSequence[str]):
            Unordered list. Locations that could not be
            reached.
    """

    @property
    def raw_page(self):
        return self

    applied_auto_protection_policies: MutableSequence["AppliedAutoProtectionPolicy"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="AppliedAutoProtectionPolicy",
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
