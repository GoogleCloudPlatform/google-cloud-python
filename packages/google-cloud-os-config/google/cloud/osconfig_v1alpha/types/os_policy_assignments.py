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

import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.osconfig_v1alpha.types import os_policy, osconfig_common

__protobuf__ = proto.module(
    package="google.cloud.osconfig.v1alpha",
    manifest={
        "OSPolicyAssignment",
        "OSPolicyAssignmentOperationMetadata",
        "CreateOSPolicyAssignmentRequest",
        "UpdateOSPolicyAssignmentRequest",
        "GetOSPolicyAssignmentRequest",
        "ListOSPolicyAssignmentsRequest",
        "ListOSPolicyAssignmentsResponse",
        "ListOSPolicyAssignmentRevisionsRequest",
        "ListOSPolicyAssignmentRevisionsResponse",
        "DeleteOSPolicyAssignmentRequest",
    },
)


class OSPolicyAssignment(proto.Message):
    r"""OS policy assignment is an API resource that is used to apply a set
    of OS policies to a dynamically targeted group of Compute Engine VM
    instances.

    An OS policy is used to define the desired state configuration for a
    Compute Engine VM instance through a set of configuration resources
    that provide capabilities such as installing or removing software
    packages, or executing a script.

    For more information, see `OS policy and OS policy
    assignment <https://cloud.google.com/compute/docs/os-configuration-management/working-with-os-policies>`__.

    Attributes:
        name (str):
            Resource name.

            Format:
            ``projects/{project_number}/locations/{location}/osPolicyAssignments/{os_policy_assignment_id}``

            This field is ignored when you create an OS policy
            assignment.
        description (str):
            OS policy assignment description.
            Length of the description is limited to 1024
            characters.
        os_policies (MutableSequence[google.cloud.osconfig_v1alpha.types.OSPolicy]):
            Required. List of OS policies to be applied
            to the VMs.
        instance_filter (google.cloud.osconfig_v1alpha.types.OSPolicyAssignment.InstanceFilter):
            Required. Filter to select VMs.
        rollout (google.cloud.osconfig_v1alpha.types.OSPolicyAssignment.Rollout):
            Required. Rollout to deploy the OS policy assignment. A
            rollout is triggered in the following situations:

            1) OSPolicyAssignment is created.
            2) OSPolicyAssignment is updated and the update contains
               changes to one of the following fields:

               - instance_filter
               - os_policies

            3) OSPolicyAssignment is deleted.
        revision_id (str):
            Output only. The assignment revision ID
            A new revision is committed whenever a rollout
            is triggered for a OS policy assignment
        revision_create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp that the revision
            was created.
        etag (str):
            The etag for this OS policy assignment.
            If this is provided on update, it must match the
            server's etag.
        rollout_state (google.cloud.osconfig_v1alpha.types.OSPolicyAssignment.RolloutState):
            Output only. OS policy assignment rollout
            state
        baseline (bool):
            Output only. Indicates that this revision has been
            successfully rolled out in this zone and new VMs will be
            assigned OS policies from this revision.

            For a given OS policy assignment, there is only one revision
            with a value of ``true`` for this field.
        deleted (bool):
            Output only. Indicates that this revision
            deletes the OS policy assignment.
        reconciling (bool):
            Output only. Indicates that reconciliation is in progress
            for the revision. This value is ``true`` when the
            ``rollout_state`` is one of:

            - IN_PROGRESS
            - CANCELLING
        uid (str):
            Output only. Server generated unique id for
            the OS policy assignment resource.
    """

    class RolloutState(proto.Enum):
        r"""OS policy assignment rollout state

        Values:
            ROLLOUT_STATE_UNSPECIFIED (0):
                Invalid value
            IN_PROGRESS (1):
                The rollout is in progress.
            CANCELLING (2):
                The rollout is being cancelled.
            CANCELLED (3):
                The rollout is cancelled.
            SUCCEEDED (4):
                The rollout has completed successfully.
        """

        ROLLOUT_STATE_UNSPECIFIED = 0
        IN_PROGRESS = 1
        CANCELLING = 2
        CANCELLED = 3
        SUCCEEDED = 4

    class LabelSet(proto.Message):
        r"""Message representing label set.

        - A label is a key value pair set for a VM.
        - A LabelSet is a set of labels.
        - Labels within a LabelSet are ANDed. In other words, a LabelSet is
          applicable for a VM only if it matches all the labels in the
          LabelSet.
        - Example: A LabelSet with 2 labels: ``env=prod`` and
          ``type=webserver`` will only be applicable for those VMs with both
          labels present.

        Attributes:
            labels (MutableMapping[str, str]):
                Labels are identified by key/value pairs in
                this map. A VM should contain all the key/value
                pairs specified in this map to be selected.
        """

        labels: MutableMapping[str, str] = proto.MapField(
            proto.STRING,
            proto.STRING,
            number=1,
        )

    class InstanceFilter(proto.Message):
        r"""Filters to select target VMs for an assignment.

        If more than one filter criteria is specified below, a VM will
        be selected if and only if it satisfies all of them.

        Attributes:
            all_ (bool):
                Target all VMs in the project. If true, no
                other criteria is permitted.
            os_short_names (MutableSequence[str]):
                Deprecated. Use the ``inventories`` field instead. A VM is
                selected if it's OS short name matches with any of the
                values provided in this list.
            inclusion_labels (MutableSequence[google.cloud.osconfig_v1alpha.types.OSPolicyAssignment.LabelSet]):
                List of label sets used for VM inclusion.

                If the list has more than one ``LabelSet``, the VM is
                included if any of the label sets are applicable for the VM.
            exclusion_labels (MutableSequence[google.cloud.osconfig_v1alpha.types.OSPolicyAssignment.LabelSet]):
                List of label sets used for VM exclusion.

                If the list has more than one label set, the VM
                is excluded if any of the label sets are
                applicable for the VM.
            inventories (MutableSequence[google.cloud.osconfig_v1alpha.types.OSPolicyAssignment.InstanceFilter.Inventory]):
                List of inventories to select VMs.

                A VM is selected if its inventory data matches
                at least one of the following inventories.
        """

        class Inventory(proto.Message):
            r"""VM inventory details.

            Attributes:
                os_short_name (str):
                    Required. The OS short name
                os_version (str):
                    The OS version

                    Prefix matches are supported if asterisk(\*) is provided as
                    the last character. For example, to match all versions with
                    a major version of ``7``, specify the following value for
                    this field ``7.*``

                    An empty string matches all OS versions.
            """

            os_short_name: str = proto.Field(
                proto.STRING,
                number=1,
            )
            os_version: str = proto.Field(
                proto.STRING,
                number=2,
            )

        all_: bool = proto.Field(
            proto.BOOL,
            number=1,
        )
        os_short_names: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )
        inclusion_labels: MutableSequence["OSPolicyAssignment.LabelSet"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=3,
                message="OSPolicyAssignment.LabelSet",
            )
        )
        exclusion_labels: MutableSequence["OSPolicyAssignment.LabelSet"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=4,
                message="OSPolicyAssignment.LabelSet",
            )
        )
        inventories: MutableSequence["OSPolicyAssignment.InstanceFilter.Inventory"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=5,
                message="OSPolicyAssignment.InstanceFilter.Inventory",
            )
        )

    class Rollout(proto.Message):
        r"""Message to configure the rollout at the zonal level for the
        OS policy assignment.

        Attributes:
            disruption_budget (google.cloud.osconfig_v1alpha.types.FixedOrPercent):
                Required. The maximum number (or percentage)
                of VMs per zone to disrupt at any given moment.
            min_wait_duration (google.protobuf.duration_pb2.Duration):
                Required. This determines the minimum duration of time to
                wait after the configuration changes are applied through the
                current rollout. A VM continues to count towards the
                ``disruption_budget`` at least until this duration of time
                has passed after configuration changes are applied.
        """

        disruption_budget: osconfig_common.FixedOrPercent = proto.Field(
            proto.MESSAGE,
            number=1,
            message=osconfig_common.FixedOrPercent,
        )
        min_wait_duration: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=2,
            message=duration_pb2.Duration,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    os_policies: MutableSequence[os_policy.OSPolicy] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=os_policy.OSPolicy,
    )
    instance_filter: InstanceFilter = proto.Field(
        proto.MESSAGE,
        number=4,
        message=InstanceFilter,
    )
    rollout: Rollout = proto.Field(
        proto.MESSAGE,
        number=5,
        message=Rollout,
    )
    revision_id: str = proto.Field(
        proto.STRING,
        number=6,
    )
    revision_create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=8,
    )
    rollout_state: RolloutState = proto.Field(
        proto.ENUM,
        number=9,
        enum=RolloutState,
    )
    baseline: bool = proto.Field(
        proto.BOOL,
        number=10,
    )
    deleted: bool = proto.Field(
        proto.BOOL,
        number=11,
    )
    reconciling: bool = proto.Field(
        proto.BOOL,
        number=12,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=13,
    )


class OSPolicyAssignmentOperationMetadata(proto.Message):
    r"""OS policy assignment operation metadata provided by OS policy
    assignment API methods that return long running operations.

    Attributes:
        os_policy_assignment (str):
            Reference to the ``OSPolicyAssignment`` API resource.

            Format:
            ``projects/{project_number}/locations/{location}/osPolicyAssignments/{os_policy_assignment_id@revision_id}``
        api_method (google.cloud.osconfig_v1alpha.types.OSPolicyAssignmentOperationMetadata.APIMethod):
            The OS policy assignment API method.
        rollout_state (google.cloud.osconfig_v1alpha.types.OSPolicyAssignmentOperationMetadata.RolloutState):
            State of the rollout
        rollout_start_time (google.protobuf.timestamp_pb2.Timestamp):
            Rollout start time
        rollout_update_time (google.protobuf.timestamp_pb2.Timestamp):
            Rollout update time
    """

    class APIMethod(proto.Enum):
        r"""The OS policy assignment API method.

        Values:
            API_METHOD_UNSPECIFIED (0):
                Invalid value
            CREATE (1):
                Create OS policy assignment API method
            UPDATE (2):
                Update OS policy assignment API method
            DELETE (3):
                Delete OS policy assignment API method
        """

        API_METHOD_UNSPECIFIED = 0
        CREATE = 1
        UPDATE = 2
        DELETE = 3

    class RolloutState(proto.Enum):
        r"""State of the rollout

        Values:
            ROLLOUT_STATE_UNSPECIFIED (0):
                Invalid value
            IN_PROGRESS (1):
                The rollout is in progress.
            CANCELLING (2):
                The rollout is being cancelled.
            CANCELLED (3):
                The rollout is cancelled.
            SUCCEEDED (4):
                The rollout has completed successfully.
        """

        ROLLOUT_STATE_UNSPECIFIED = 0
        IN_PROGRESS = 1
        CANCELLING = 2
        CANCELLED = 3
        SUCCEEDED = 4

    os_policy_assignment: str = proto.Field(
        proto.STRING,
        number=1,
    )
    api_method: APIMethod = proto.Field(
        proto.ENUM,
        number=2,
        enum=APIMethod,
    )
    rollout_state: RolloutState = proto.Field(
        proto.ENUM,
        number=3,
        enum=RolloutState,
    )
    rollout_start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    rollout_update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )


class CreateOSPolicyAssignmentRequest(proto.Message):
    r"""A request message to create an OS policy assignment

    Attributes:
        parent (str):
            Required. The parent resource name in the
            form: projects/{project}/locations/{location}
        os_policy_assignment (google.cloud.osconfig_v1alpha.types.OSPolicyAssignment):
            Required. The OS policy assignment to be
            created.
        os_policy_assignment_id (str):
            Required. The logical name of the OS policy assignment in
            the project with the following restrictions:

            - Must contain only lowercase letters, numbers, and hyphens.
            - Must start with a letter.
            - Must be between 1-63 characters.
            - Must end with a number or a letter.
            - Must be unique within the project.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    os_policy_assignment: "OSPolicyAssignment" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="OSPolicyAssignment",
    )
    os_policy_assignment_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class UpdateOSPolicyAssignmentRequest(proto.Message):
    r"""A request message to update an OS policy assignment

    Attributes:
        os_policy_assignment (google.cloud.osconfig_v1alpha.types.OSPolicyAssignment):
            Required. The updated OS policy assignment.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask that controls which
            fields of the assignment should be updated.
    """

    os_policy_assignment: "OSPolicyAssignment" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="OSPolicyAssignment",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class GetOSPolicyAssignmentRequest(proto.Message):
    r"""A request message to get an OS policy assignment

    Attributes:
        name (str):
            Required. The resource name of OS policy assignment.

            Format:
            ``projects/{project}/locations/{location}/osPolicyAssignments/{os_policy_assignment}@{revisionId}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListOSPolicyAssignmentsRequest(proto.Message):
    r"""A request message to list OS policy assignments for a parent
    resource

    Attributes:
        parent (str):
            Required. The parent resource name.
        page_size (int):
            The maximum number of assignments to return.
        page_token (str):
            A pagination token returned from a previous call to
            ``ListOSPolicyAssignments`` that indicates where this
            listing should continue from.
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


class ListOSPolicyAssignmentsResponse(proto.Message):
    r"""A response message for listing all assignments under given
    parent.

    Attributes:
        os_policy_assignments (MutableSequence[google.cloud.osconfig_v1alpha.types.OSPolicyAssignment]):
            The list of assignments
        next_page_token (str):
            The pagination token to retrieve the next
            page of OS policy assignments.
    """

    @property
    def raw_page(self):
        return self

    os_policy_assignments: MutableSequence["OSPolicyAssignment"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="OSPolicyAssignment",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListOSPolicyAssignmentRevisionsRequest(proto.Message):
    r"""A request message to list revisions for a OS policy
    assignment

    Attributes:
        name (str):
            Required. The name of the OS policy
            assignment to list revisions for.
        page_size (int):
            The maximum number of revisions to return.
        page_token (str):
            A pagination token returned from a previous call to
            ``ListOSPolicyAssignmentRevisions`` that indicates where
            this listing should continue from.
    """

    name: str = proto.Field(
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


class ListOSPolicyAssignmentRevisionsResponse(proto.Message):
    r"""A response message for listing all revisions for a OS policy
    assignment.

    Attributes:
        os_policy_assignments (MutableSequence[google.cloud.osconfig_v1alpha.types.OSPolicyAssignment]):
            The OS policy assignment revisions
        next_page_token (str):
            The pagination token to retrieve the next
            page of OS policy assignment revisions.
    """

    @property
    def raw_page(self):
        return self

    os_policy_assignments: MutableSequence["OSPolicyAssignment"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="OSPolicyAssignment",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteOSPolicyAssignmentRequest(proto.Message):
    r"""A request message for deleting a OS policy assignment.

    Attributes:
        name (str):
            Required. The name of the OS policy
            assignment to be deleted
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
