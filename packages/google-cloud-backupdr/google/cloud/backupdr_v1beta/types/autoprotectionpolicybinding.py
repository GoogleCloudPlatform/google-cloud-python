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
    package="google.cloud.backupdr.v1beta",
    manifest={
        "AutoProtectionPolicyBinding",
        "BindingEvaluationSummary",
        "CreateAutoProtectionPolicyBindingRequest",
        "GetAutoProtectionPolicyBindingRequest",
        "ListAutoProtectionPolicyBindingsRequest",
        "ListAutoProtectionPolicyBindingsResponse",
        "InitiateDeleteAutoProtectionPolicyBindingRequest",
    },
)


class AutoProtectionPolicyBinding(proto.Message):
    r"""An AutoprotectionPolicyBinding (APPA) acts as the bridge
    between an AutoprotectionPolicy and the scope (Project, Folder,
    or Organization) where the policy should be applied.

    Attributes:
        name (str):
            Identifier. The resource name of the
            AutoProtectionPolicyBinding. Format:
            ``projects/{project}/locations/{location}/autoProtectionPolicies/{auto_protection_policy}/bindings/{binding}``
        description (str):
            Optional. A description of the binding.
        state (google.cloud.backupdr_v1beta.types.AutoProtectionPolicyBinding.State):
            Output only. The current state of the
            AutoProtectionPolicyBinding.
        scope (str):
            Required. Immutable. Resource Id of target container on
            which policy will be applied. Format: projects/{project_id}
        binding_evaluation_summary (google.cloud.backupdr_v1beta.types.BindingEvaluationSummary):
            Output only. Summaries of the last policy
            application when the job has run, with one entry
            per resource type specified in the
            AutoProtectionPolicy.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the binding
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the binding
            was last updated.
        etag (str):
            Optional. Output only. The etag for the
            binding. If this is provided on update, it must
            match the server's etag.
    """

    class State(proto.Enum):
        r"""The state of an AutoProtectionPolicyBinding.

        Values:
            STATE_UNSPECIFIED (0):
                The state of the binding is unspecified.
            CREATING (1):
                The binding is being created.
            ACTIVE (2):
                The binding is active.
            DELETION_INITIATED (3):
                The binding deletion is initiated.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        ACTIVE = 2
        DELETION_INITIATED = 3

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=3,
        enum=State,
    )
    scope: str = proto.Field(
        proto.STRING,
        number=4,
    )
    binding_evaluation_summary: "BindingEvaluationSummary" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="BindingEvaluationSummary",
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=8,
    )


class BindingEvaluationSummary(proto.Message):
    r"""BindingEvaluationSummary contains the summary of the last run
    of job that applies policy to matching resources for a given
    binding.

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


class CreateAutoProtectionPolicyBindingRequest(proto.Message):
    r"""Request message for creating an AutoProtectionPolicyBinding.

    Attributes:
        parent (str):
            Required. The parent resource where this binding will be
            created. Format:
            projects/{project}/locations/{location}/autoProtectionPolicies/{auto_protection_policy}
        auto_protection_policy_binding_id (str):
            Required. The ID to use for the binding.
            This will become the final component of the
            binding's resource name.
        auto_protection_policy_binding (google.cloud.backupdr_v1beta.types.AutoProtectionPolicyBinding):
            Required. The AutoProtectionPolicyBinding
            resource to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    auto_protection_policy_binding_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    auto_protection_policy_binding: "AutoProtectionPolicyBinding" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="AutoProtectionPolicyBinding",
    )


class GetAutoProtectionPolicyBindingRequest(proto.Message):
    r"""Request message for getting an AutoProtectionPolicyBinding.

    Attributes:
        name (str):
            Required. The name of the binding to retrieve. Format:
            projects/{project}/locations/{location}/autoProtectionPolicies/{auto_protection_policy}/bindings/{binding}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListAutoProtectionPolicyBindingsRequest(proto.Message):
    r"""Request message for ListAutoProtectionPolicyBindings.

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


class ListAutoProtectionPolicyBindingsResponse(proto.Message):
    r"""Response message for ListAutoProtectionPolicyBindings.

    Attributes:
        auto_protection_policy_bindings (MutableSequence[google.cloud.backupdr_v1beta.types.AutoProtectionPolicyBinding]):
            A list of the AutoProtectionPolicyBindings
            resources found.
        next_page_token (str):
            A token that can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Unordered list. Locations that could not be
            reached.
    """

    @property
    def raw_page(self):
        return self

    auto_protection_policy_bindings: MutableSequence["AutoProtectionPolicyBinding"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="AutoProtectionPolicyBinding",
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


class InitiateDeleteAutoProtectionPolicyBindingRequest(proto.Message):
    r"""Request message for initiating delete of an
    AutoProtectionPolicyBinding.

    Attributes:
        name (str):
            Required. The name of the binding to delete. Format:
            projects/{project}/locations/{location}/autoProtectionPolicies/{auto_protection_policy}/bindings/{binding}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
