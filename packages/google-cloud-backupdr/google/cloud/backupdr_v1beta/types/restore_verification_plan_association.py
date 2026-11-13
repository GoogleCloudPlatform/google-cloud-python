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
import google.rpc.status_pb2 as status_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.backupdr.v1beta",
    manifest={
        "RestoreVerificationPlanAssociation",
        "TriggerSummary",
        "CreateRestoreVerificationPlanAssociationRequest",
        "GetRestoreVerificationPlanAssociationRequest",
        "ListRestoreVerificationPlanAssociationsRequest",
        "ListRestoreVerificationPlanAssociationsResponse",
        "DeleteRestoreVerificationPlanAssociationRequest",
        "TriggerRestoreVerificationRequest",
        "TriggerRestoreVerificationResponse",
    },
)


class RestoreVerificationPlanAssociation(proto.Message):
    r"""A ``RestoreVerificationPlanAssociation`` binds a specific workload
    to a ``RestoreVerificationPlan``.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        restore_template (str):
            Required. Immutable. The canonical name of
            the RestoreTemplate to trigger.

            This field is a member of `oneof`_ ``association``.
        name (str):
            Output only. Identifier. The resource name of the
            ``RestoreVerificationPlanAssociation``.

            Format:
            ``projects/{project}/locations/{location}/restoreVerificationPlans/{restore_verification_plan}/associations/{association}``
        description (str):
            Optional. The description of the
            ``RestoreVerificationPlanAssociation`` resource.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the association
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the association
            was updated.
        state (google.cloud.backupdr_v1beta.types.RestoreVerificationPlanAssociation.State):
            Output only. The ``State`` for the
            ``RestoreVerificationPlanAssociation``.
        trigger_summary (google.cloud.backupdr_v1beta.types.TriggerSummary):
            Output only. Results of the most recent
            automated restore initiation and the next
            scheduled execution time.
        resource_type (str):
            Required. Immutable. The type of the Google Cloud resource
            (e.g., ``compute.googleapis.com/Instance``,
            ``sqladmin.googleapis.com/Instance``).
        labels (MutableMapping[str, str]):
            Optional. User-defined labels.
    """

    class State(proto.Enum):
        r"""``State`` enumerates the possible states for a
        ``RestoreVerificationPlanAssociation``.

        Values:
            STATE_UNSPECIFIED (0):
                State not set.
            CREATING (1):
                The resource is being created.
            ACTIVE (2):
                The resource has been created and is fully
                usable.
            DELETING (3):
                The resource is being deleted.
            INACTIVE (4):
                The resource has been created but is not
                usable.
            UPDATING (5):
                The resource is being updated.
            ERROR (6):
                The resource is in an error state due to a
                configuration issue.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        ACTIVE = 2
        DELETING = 3
        INACTIVE = 4
        UPDATING = 5
        ERROR = 6

    restore_template: str = proto.Field(
        proto.STRING,
        number=8,
        oneof="association",
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
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
    state: State = proto.Field(
        proto.ENUM,
        number=5,
        enum=State,
    )
    trigger_summary: "TriggerSummary" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="TriggerSummary",
    )
    resource_type: str = proto.Field(
        proto.STRING,
        number=7,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=9,
    )


class TriggerSummary(proto.Message):
    r"""``TriggerSummary`` contains the results of the most recent automated
    restore initiation and the next scheduled execution time.

    Attributes:
        last_trigger_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time of the most recent
            trigger initiation.
        next_trigger_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The scheduled time of the next
            trigger initiation.
        last_trigger_error (google.rpc.status_pb2.Status):
            Output only. The error status of the most
            recent failed trigger.
        last_verification_execution (str):
            Output only. The resource name of the most recent initiated
            RestoreTemplateExecution. Format:
            ``projects/{project}/locations/{location}/restoreTemplates/{restore_template}/executions/{execution}``
    """

    last_trigger_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    next_trigger_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    last_trigger_error: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=3,
        message=status_pb2.Status,
    )
    last_verification_execution: str = proto.Field(
        proto.STRING,
        number=4,
    )


class CreateRestoreVerificationPlanAssociationRequest(proto.Message):
    r"""Request message for CreateRestoreVerificationPlanAssociation.

    Attributes:
        parent (str):
            Required. The parent resource where this association will be
            created. Format:
            ``projects/{project}/locations/{location}/restoreVerificationPlans/{restore_verification_plan}``
        restore_verification_plan_association_id (str):
            Required. The ID to use for the association, which will
            become the final component of the association's resource
            name.

            This value should be 1-63 characters, and valid characters
            are /[a-z0-9\_-]/.
        restore_verification_plan_association (google.cloud.backupdr_v1beta.types.RestoreVerificationPlanAssociation):
            Required. The
            RestoreVerificationPlanAssociation resource to
            create.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know that the server has already received the
            duplicate request and can avoid responding with
            an error. The request ID must be a valid UUID
            with the exception that zero UUID is not
            supported
            (00000000-0000-0000-0000-000000000000).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    restore_verification_plan_association_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    restore_verification_plan_association: "RestoreVerificationPlanAssociation" = (
        proto.Field(
            proto.MESSAGE,
            number=3,
            message="RestoreVerificationPlanAssociation",
        )
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class GetRestoreVerificationPlanAssociationRequest(proto.Message):
    r"""Request message for GetRestoreVerificationPlanAssociation.

    Attributes:
        name (str):
            Required. The resource name of the
            RestoreVerificationPlanAssociation to retrieve. Format:
            ``projects/{project}/locations/{location}/restoreVerificationPlans/{restore_verification_plan}/associations/{association}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListRestoreVerificationPlanAssociationsRequest(proto.Message):
    r"""Request message for ListRestoreVerificationPlanAssociations.

    Attributes:
        parent (str):
            Required. The parent RestoreVerificationPlan name. Format:
            ``projects/{project}/locations/{location}/restoreVerificationPlans/{restore_verification_plan}``
        page_size (int):
            Optional. The maximum number of associations
            to return. The service may return fewer than
            this value. If unspecified, at most 500
            associations will be returned. The maximum value
            is 1000; values above 1000 will be coerced to
            1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListRestoreVerificationPlanAssociations`` call. Provide
            this to retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``ListRestoreVerificationPlanAssociations`` must match the
            call that provided the page token.
        filter (str):
            Optional. Filtering results.
        order_by (str):
            Optional. Hint for how to order the results.
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


class ListRestoreVerificationPlanAssociationsResponse(proto.Message):
    r"""Response message for ListRestoreVerificationPlanAssociations.

    Attributes:
        restore_verification_plan_associations (MutableSequence[google.cloud.backupdr_v1beta.types.RestoreVerificationPlanAssociation]):
            The list of
            RestoreVerificationPlanAssociations.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Unordered list. Locations that could not be
            reached.
    """

    @property
    def raw_page(self):
        return self

    restore_verification_plan_associations: MutableSequence[
        "RestoreVerificationPlanAssociation"
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="RestoreVerificationPlanAssociation",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class DeleteRestoreVerificationPlanAssociationRequest(proto.Message):
    r"""Request message for DeleteRestoreVerificationPlanAssociation.

    Attributes:
        name (str):
            Required. The resource name of the
            RestoreVerificationPlanAssociation to delete. Format:
            ``projects/{project}/locations/{location}/restoreVerificationPlans/{restore_verification_plan}/associations/{association}``
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know that the server has already received the
            duplicate request and can avoid responding with
            an error. The request ID must be a valid UUID
            with the exception that zero UUID is not
            supported
            (00000000-0000-0000-0000-000000000000).
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class TriggerRestoreVerificationRequest(proto.Message):
    r"""Request message for TriggerRestoreVerification.

    Attributes:
        name (str):
            Required. The resource name of the
            RestoreVerificationPlanAssociation to trigger. Format:
            ``projects/{project}/locations/{location}/restoreVerificationPlans/{restore_verification_plan}/associations/{association}``
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know that the server has already received the
            duplicate request and can avoid responding with
            an error. The request ID must be a valid UUID
            with the exception that zero UUID is not
            supported
            (00000000-0000-0000-0000-000000000000).
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class TriggerRestoreVerificationResponse(proto.Message):
    r"""Response message for TriggerRestoreVerification.

    Attributes:
        restore_template_execution (str):
            Output only. The resource name of the initiated
            RestoreTemplateExecution. Format:
            ``projects/{project}/locations/{location}/restoreTemplates/{restore_template}/executions/{execution}``
    """

    restore_template_execution: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
