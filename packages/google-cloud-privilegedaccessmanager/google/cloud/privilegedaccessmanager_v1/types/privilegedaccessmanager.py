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
import google.rpc.status_pb2 as status_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.privilegedaccessmanager.v1",
    manifest={
        "CheckOnboardingStatusRequest",
        "CheckOnboardingStatusResponse",
        "Entitlement",
        "AccessControlEntry",
        "ApprovalWorkflow",
        "ManualApprovals",
        "PrivilegedAccess",
        "ListEntitlementsRequest",
        "ListEntitlementsResponse",
        "SearchEntitlementsRequest",
        "SearchEntitlementsResponse",
        "GetEntitlementRequest",
        "CreateEntitlementRequest",
        "DeleteEntitlementRequest",
        "UpdateEntitlementRequest",
        "Grant",
        "Justification",
        "ListGrantsRequest",
        "ListGrantsResponse",
        "SearchGrantsRequest",
        "SearchGrantsResponse",
        "GetGrantRequest",
        "ApproveGrantRequest",
        "DenyGrantRequest",
        "RevokeGrantRequest",
        "CreateGrantRequest",
        "OperationMetadata",
    },
)


class CheckOnboardingStatusRequest(proto.Message):
    r"""Request message for ``CheckOnboardingStatus`` method.

    Attributes:
        parent (str):
            Required. The resource for which the onboarding status
            should be checked. Should be in one of the following
            formats:

            - ``projects/{project-number|project-id}/locations/{region}``
            - ``folders/{folder-number}/locations/{region}``
            - ``organizations/{organization-number}/locations/{region}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CheckOnboardingStatusResponse(proto.Message):
    r"""Response message for ``CheckOnboardingStatus`` method.

    Attributes:
        service_account (str):
            The service account that PAM uses to act on
            this resource.
        findings (MutableSequence[google.cloud.privilegedaccessmanager_v1.types.CheckOnboardingStatusResponse.Finding]):
            List of issues that are preventing PAM from
            functioning for this resource and need to be
            fixed to complete onboarding. Some issues might
            not be detected or reported.
    """

    class Finding(proto.Message):
        r"""Finding represents an issue which prevents PAM from
        functioning properly for this resource.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            iam_access_denied (google.cloud.privilegedaccessmanager_v1.types.CheckOnboardingStatusResponse.Finding.IAMAccessDenied):
                PAM's service account is being denied access
                by Cloud IAM.

                This field is a member of `oneof`_ ``finding_type``.
        """

        class IAMAccessDenied(proto.Message):
            r"""PAM's service account is being denied access by Cloud IAM.
            This can be fixed by granting a role that contains the missing
            permissions to the service account or exempting it from deny
            policies if they are blocking the access.

            Attributes:
                missing_permissions (MutableSequence[str]):
                    List of permissions that are being denied.
            """

            missing_permissions: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=1,
            )

        iam_access_denied: "CheckOnboardingStatusResponse.Finding.IAMAccessDenied" = (
            proto.Field(
                proto.MESSAGE,
                number=1,
                oneof="finding_type",
                message="CheckOnboardingStatusResponse.Finding.IAMAccessDenied",
            )
        )

    service_account: str = proto.Field(
        proto.STRING,
        number=1,
    )
    findings: MutableSequence[Finding] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=Finding,
    )


class Entitlement(proto.Message):
    r"""An entitlement defines the eligibility of a set of users to
    obtain predefined access for some time possibly after going
    through an approval workflow.

    Attributes:
        name (str):
            Identifier. Name of the entitlement. Possible formats:

            - ``organizations/{organization-number}/locations/{region}/entitlements/{entitlement-id}``
            - ``folders/{folder-number}/locations/{region}/entitlements/{entitlement-id}``
            - ``projects/{project-id|project-number}/locations/{region}/entitlements/{entitlement-id}``
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Create time stamp.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Update time stamp.
        eligible_users (MutableSequence[google.cloud.privilegedaccessmanager_v1.types.AccessControlEntry]):
            Optional. Who can create grants using this
            entitlement. This list should contain at most
            one entry.
        approval_workflow (google.cloud.privilegedaccessmanager_v1.types.ApprovalWorkflow):
            Optional. The approvals needed before access
            are granted to a requester. No approvals are
            needed if this field is null.
        privileged_access (google.cloud.privilegedaccessmanager_v1.types.PrivilegedAccess):
            The access granted to a requester on
            successful approval.
        max_request_duration (google.protobuf.duration_pb2.Duration):
            Required. The maximum amount of time that
            access is granted for a request. A requester can
            ask for a duration less than this, but never
            more.
        state (google.cloud.privilegedaccessmanager_v1.types.Entitlement.State):
            Output only. Current state of this
            entitlement.
        requester_justification_config (google.cloud.privilegedaccessmanager_v1.types.Entitlement.RequesterJustificationConfig):
            Required. The manner in which the requester
            should provide a justification for requesting
            access.
        additional_notification_targets (google.cloud.privilegedaccessmanager_v1.types.Entitlement.AdditionalNotificationTargets):
            Optional. Additional email addresses to be
            notified based on actions taken.
        etag (str):
            An ``etag`` is used for optimistic concurrency control as a
            way to prevent simultaneous updates to the same entitlement.
            An ``etag`` is returned in the response to
            ``GetEntitlement`` and the caller should put the ``etag`` in
            the request to ``UpdateEntitlement`` so that their change is
            applied on the same version. If this field is omitted or if
            there is a mismatch while updating an entitlement, then the
            server rejects the request.
    """

    class State(proto.Enum):
        r"""Different states an entitlement can be in.

        Values:
            STATE_UNSPECIFIED (0):
                Unspecified state. This value is never
                returned by the server.
            CREATING (1):
                The entitlement is being created.
            AVAILABLE (2):
                The entitlement is available for requesting
                access.
            DELETING (3):
                The entitlement is being deleted.
            DELETED (4):
                The entitlement has been deleted.
            UPDATING (5):
                The entitlement is being updated.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        AVAILABLE = 2
        DELETING = 3
        DELETED = 4
        UPDATING = 5

    class RequesterJustificationConfig(proto.Message):
        r"""Defines how a requester must provide a justification when
        requesting access.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            not_mandatory (google.cloud.privilegedaccessmanager_v1.types.Entitlement.RequesterJustificationConfig.NotMandatory):
                This option means the requester isn't
                required to provide a justification.

                This field is a member of `oneof`_ ``justification_type``.
            unstructured (google.cloud.privilegedaccessmanager_v1.types.Entitlement.RequesterJustificationConfig.Unstructured):
                This option means the requester must provide
                a string as justification. If this is selected,
                the server allows the requester to provide a
                justification but doesn't validate it.

                This field is a member of `oneof`_ ``justification_type``.
        """

        class NotMandatory(proto.Message):
            r"""The justification is not mandatory but can be provided in any
            of the supported formats.

            """

        class Unstructured(proto.Message):
            r"""The requester has to provide a justification in the form of a
            string.

            """

        not_mandatory: "Entitlement.RequesterJustificationConfig.NotMandatory" = (
            proto.Field(
                proto.MESSAGE,
                number=1,
                oneof="justification_type",
                message="Entitlement.RequesterJustificationConfig.NotMandatory",
            )
        )
        unstructured: "Entitlement.RequesterJustificationConfig.Unstructured" = (
            proto.Field(
                proto.MESSAGE,
                number=2,
                oneof="justification_type",
                message="Entitlement.RequesterJustificationConfig.Unstructured",
            )
        )

    class AdditionalNotificationTargets(proto.Message):
        r"""``AdditionalNotificationTargets`` includes email addresses to be
        notified.

        Attributes:
            admin_email_recipients (MutableSequence[str]):
                Optional. Additional email addresses to be
                notified when a principal (requester) is granted
                access.
            requester_email_recipients (MutableSequence[str]):
                Optional. Additional email address to be
                notified about an eligible entitlement.
        """

        admin_email_recipients: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )
        requester_email_recipients: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    eligible_users: MutableSequence["AccessControlEntry"] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message="AccessControlEntry",
    )
    approval_workflow: "ApprovalWorkflow" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="ApprovalWorkflow",
    )
    privileged_access: "PrivilegedAccess" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="PrivilegedAccess",
    )
    max_request_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=8,
        message=duration_pb2.Duration,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=9,
        enum=State,
    )
    requester_justification_config: RequesterJustificationConfig = proto.Field(
        proto.MESSAGE,
        number=10,
        message=RequesterJustificationConfig,
    )
    additional_notification_targets: AdditionalNotificationTargets = proto.Field(
        proto.MESSAGE,
        number=11,
        message=AdditionalNotificationTargets,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=12,
    )


class AccessControlEntry(proto.Message):
    r"""``AccessControlEntry`` is used to control who can do some operation.

    Attributes:
        principals (MutableSequence[str]):
            Optional. Users who are allowed for the
            operation. Each entry should be a valid v1 IAM
            principal identifier. The format for these is
            documented at:

            https://cloud.google.com/iam/docs/principal-identifiers#v1
    """

    principals: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class ApprovalWorkflow(proto.Message):
    r"""Different types of approval workflows that can be used to
    gate privileged access granting.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        manual_approvals (google.cloud.privilegedaccessmanager_v1.types.ManualApprovals):
            An approval workflow where users designated
            as approvers review and act on the grants.

            This field is a member of `oneof`_ ``approval_workflow``.
    """

    manual_approvals: "ManualApprovals" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="approval_workflow",
        message="ManualApprovals",
    )


class ManualApprovals(proto.Message):
    r"""A manual approval workflow where users who are designated as
    approvers need to call the ``ApproveGrant``/``DenyGrant`` APIs for a
    grant. The workflow can consist of multiple serial steps where each
    step defines who can act as approver in that step and how many of
    those users should approve before the workflow moves to the next
    step.

    This can be used to create approval workflows such as:

    - Require an approval from any user in a group G.
    - Require an approval from any k number of users from a Group G.
    - Require an approval from any user in a group G and then from a
      user U.

    A single user might be part of the ``approvers`` ACL for multiple
    steps in this workflow, but they can only approve once and that
    approval is only considered to satisfy the approval step at which it
    was granted.

    Attributes:
        require_approver_justification (bool):
            Optional. Do the approvers need to provide a
            justification for their actions?
        steps (MutableSequence[google.cloud.privilegedaccessmanager_v1.types.ManualApprovals.Step]):
            Optional. List of approval steps in this
            workflow. These steps are followed in the
            specified order sequentially. Only 1 step is
            supported.
    """

    class Step(proto.Message):
        r"""Step represents a logical step in a manual approval workflow.

        Attributes:
            approvers (MutableSequence[google.cloud.privilegedaccessmanager_v1.types.AccessControlEntry]):
                Optional. The potential set of approvers in
                this step. This list must contain at most one
                entry.
            approvals_needed (int):
                Required. How many users from the above list
                need to approve. If there aren't enough distinct
                users in the list, then the workflow
                indefinitely blocks. Should always be greater
                than 0. 1 is the only supported value.
            approver_email_recipients (MutableSequence[str]):
                Optional. Additional email addresses to be
                notified when a grant is pending approval.
        """

        approvers: MutableSequence["AccessControlEntry"] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="AccessControlEntry",
        )
        approvals_needed: int = proto.Field(
            proto.INT32,
            number=2,
        )
        approver_email_recipients: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=3,
        )

    require_approver_justification: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    steps: MutableSequence[Step] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=Step,
    )


class PrivilegedAccess(proto.Message):
    r"""Privileged access that this service can be used to gate.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        gcp_iam_access (google.cloud.privilegedaccessmanager_v1.types.PrivilegedAccess.GcpIamAccess):
            Access to a Google Cloud resource through
            IAM.

            This field is a member of `oneof`_ ``access_type``.
    """

    class GcpIamAccess(proto.Message):
        r"""``GcpIamAccess`` represents IAM based access control on a Google
        Cloud resource. Refer to https://cloud.google.com/iam/docs to
        understand more about IAM.

        Attributes:
            resource_type (str):
                Required. The type of this resource.
            resource (str):
                Required. Name of the resource.
            role_bindings (MutableSequence[google.cloud.privilegedaccessmanager_v1.types.PrivilegedAccess.GcpIamAccess.RoleBinding]):
                Required. Role bindings that are created on
                successful grant.
        """

        class RoleBinding(proto.Message):
            r"""IAM role bindings that are created after a successful grant.

            Attributes:
                role (str):
                    Required. IAM role to be granted.
                    https://cloud.google.com/iam/docs/roles-overview.
                condition_expression (str):
                    Optional. The expression field of the IAM
                    condition to be associated with the role. If
                    specified, a user with an active grant for this
                    entitlement is able to access the resource only
                    if this condition evaluates to true for their
                    request.

                    This field uses the same CEL format as IAM and
                    supports all attributes that IAM supports,
                    except tags.
                    https://cloud.google.com/iam/docs/conditions-overview#attributes.
            """

            role: str = proto.Field(
                proto.STRING,
                number=1,
            )
            condition_expression: str = proto.Field(
                proto.STRING,
                number=2,
            )

        resource_type: str = proto.Field(
            proto.STRING,
            number=1,
        )
        resource: str = proto.Field(
            proto.STRING,
            number=2,
        )
        role_bindings: MutableSequence["PrivilegedAccess.GcpIamAccess.RoleBinding"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=4,
                message="PrivilegedAccess.GcpIamAccess.RoleBinding",
            )
        )

    gcp_iam_access: GcpIamAccess = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="access_type",
        message=GcpIamAccess,
    )


class ListEntitlementsRequest(proto.Message):
    r"""Message for requesting list of entitlements.

    Attributes:
        parent (str):
            Required. The parent which owns the
            entitlement resources.
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, the server picks an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
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


class ListEntitlementsResponse(proto.Message):
    r"""Message for response to listing entitlements.

    Attributes:
        entitlements (MutableSequence[google.cloud.privilegedaccessmanager_v1.types.Entitlement]):
            The list of entitlements.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    entitlements: MutableSequence["Entitlement"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Entitlement",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class SearchEntitlementsRequest(proto.Message):
    r"""Request message for ``SearchEntitlements`` method.

    Attributes:
        parent (str):
            Required. The parent which owns the
            entitlement resources.
        caller_access_type (google.cloud.privilegedaccessmanager_v1.types.SearchEntitlementsRequest.CallerAccessType):
            Required. Only entitlements where the calling
            user has this access are returned.
        filter (str):
            Optional. Only entitlements matching this
            filter are returned in the response.
        page_size (int):
            Optional. Requested page size. The server may
            return fewer items than requested. If
            unspecified, the server picks an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
    """

    class CallerAccessType(proto.Enum):
        r"""Different types of access a user can have on the entitlement
        resource.

        Values:
            CALLER_ACCESS_TYPE_UNSPECIFIED (0):
                Unspecified access type.
            GRANT_REQUESTER (1):
                The user has access to create grants using
                this entitlement.
            GRANT_APPROVER (2):
                The user has access to approve/deny grants
                created under this entitlement.
        """

        CALLER_ACCESS_TYPE_UNSPECIFIED = 0
        GRANT_REQUESTER = 1
        GRANT_APPROVER = 2

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    caller_access_type: CallerAccessType = proto.Field(
        proto.ENUM,
        number=2,
        enum=CallerAccessType,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=3,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=4,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=5,
    )


class SearchEntitlementsResponse(proto.Message):
    r"""Response message for ``SearchEntitlements`` method.

    Attributes:
        entitlements (MutableSequence[google.cloud.privilegedaccessmanager_v1.types.Entitlement]):
            The list of entitlements.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
    """

    @property
    def raw_page(self):
        return self

    entitlements: MutableSequence["Entitlement"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Entitlement",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetEntitlementRequest(proto.Message):
    r"""Message for getting an entitlement.

    Attributes:
        name (str):
            Required. Name of the resource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateEntitlementRequest(proto.Message):
    r"""Message for creating an entitlement.

    Attributes:
        parent (str):
            Required. Name of the parent resource for the entitlement.
            Possible formats:

            - ``organizations/{organization-number}/locations/{region}``
            - ``folders/{folder-number}/locations/{region}``
            - ``projects/{project-id|project-number}/locations/{region}``
        entitlement_id (str):
            Required. The ID to use for this entitlement. This becomes
            the last part of the resource name.

            This value should be 4-63 characters in length, and valid
            characters are "[a-z]", "[0-9]", and "-". The first
            character should be from [a-z].

            This value should be unique among all other entitlements
            under the specified ``parent``.
        entitlement (google.cloud.privilegedaccessmanager_v1.types.Entitlement):
            Required. The resource being created
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server knows to
            ignore the request if it has already been
            completed. The server guarantees this for at
            least 60 minutes after the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, ignores the second request and returns the
            previous operation's response. This prevents
            clients from accidentally creating duplicate
            entitlements.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    entitlement_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    entitlement: "Entitlement" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Entitlement",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class DeleteEntitlementRequest(proto.Message):
    r"""Message for deleting an entitlement.

    Attributes:
        name (str):
            Required. Name of the resource.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server knows to
            ignore the request if it has already been
            completed. The server guarantees this for at
            least 60 minutes after the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, ignores the second request.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        force (bool):
            Optional. If set to true, any child grant
            under this entitlement is also deleted.
            (Otherwise, the request only works if the
            entitlement has no child grant.)
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class UpdateEntitlementRequest(proto.Message):
    r"""Message for updating an entitlement.

    Attributes:
        entitlement (google.cloud.privilegedaccessmanager_v1.types.Entitlement):
            Required. The entitlement resource that is
            updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The list of fields to update. A field is
            overwritten if, and only if, it is in the mask. Any
            immutable fields set in the mask are ignored by the server.
            Repeated fields and map fields are only allowed in the last
            position of a ``paths`` string and overwrite the existing
            values. Hence an update to a repeated field or a map should
            contain the entire list of values. The fields specified in
            the update_mask are relative to the resource and not to the
            request. (e.g. ``MaxRequestDuration``; *not*
            ``entitlement.MaxRequestDuration``) A value of '\*' for this
            field refers to full replacement of the resource.
    """

    entitlement: "Entitlement" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Entitlement",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class Grant(proto.Message):
    r"""A grant represents a request from a user for obtaining the
    access specified in an entitlement they are eligible for.

    Attributes:
        name (str):
            Identifier. Name of this grant. Possible formats:

            - ``organizations/{organization-number}/locations/{region}/entitlements/{entitlement-id}/grants/{grant-id}``
            - ``folders/{folder-number}/locations/{region}/entitlements/{entitlement-id}/grants/{grant-id}``
            - ``projects/{project-id|project-number}/locations/{region}/entitlements/{entitlement-id}/grants/{grant-id}``

            The last segment of this name (``{grant-id}``) is
            autogenerated.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Create time stamp.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Update time stamp.
        requester (str):
            Output only. Username of the user who created
            this grant.
        requested_duration (google.protobuf.duration_pb2.Duration):
            Required. The amount of time access is needed for. This
            value should be less than the ``max_request_duration`` value
            of the entitlement.
        justification (google.cloud.privilegedaccessmanager_v1.types.Justification):
            Optional. Justification of why this access is
            needed.
        state (google.cloud.privilegedaccessmanager_v1.types.Grant.State):
            Output only. Current state of this grant.
        timeline (google.cloud.privilegedaccessmanager_v1.types.Grant.Timeline):
            Output only. Timeline of this grant.
        privileged_access (google.cloud.privilegedaccessmanager_v1.types.PrivilegedAccess):
            Output only. The access that would be granted
            by this grant.
        audit_trail (google.cloud.privilegedaccessmanager_v1.types.Grant.AuditTrail):
            Output only. Audit trail of access provided
            by this grant. If unspecified then access was
            never granted.
        additional_email_recipients (MutableSequence[str]):
            Optional. Additional email addresses to
            notify for all the actions performed on the
            grant.
        externally_modified (bool):
            Output only. Flag set by the PAM system to indicate that
            policy bindings made by this grant have been modified from
            outside PAM.

            After it is set, this flag remains set forever irrespective
            of the grant state. A ``true`` value here indicates that PAM
            no longer has any certainty on the access a user has because
            of this grant.
    """

    class State(proto.Enum):
        r"""Different states a grant can be in.

        Values:
            STATE_UNSPECIFIED (0):
                Unspecified state. This value is never
                returned by the server.
            APPROVAL_AWAITED (1):
                The entitlement had an approval workflow
                configured and this grant is waiting for the
                workflow to complete.
            DENIED (3):
                The approval workflow completed with a denied
                result. No access is granted for this grant.
                This is a terminal state.
            SCHEDULED (4):
                The approval workflow completed successfully
                with an approved result or none was configured.
                Access is provided at an appropriate time.
            ACTIVATING (5):
                Access is being given.
            ACTIVE (6):
                Access was successfully given and is
                currently active.
            ACTIVATION_FAILED (7):
                The system could not give access due to a
                non-retriable error. This is a terminal state.
            EXPIRED (8):
                Expired after waiting for the approval
                workflow to complete. This is a terminal state.
            REVOKING (9):
                Access is being revoked.
            REVOKED (10):
                Access was revoked by a user. This is a
                terminal state.
            ENDED (11):
                System took back access as the requested
                duration was over. This is a terminal state.
            WITHDRAWING (12):
                Access is being withdrawn.
            WITHDRAWN (13):
                Grant was withdrawn by the grant owner. This
                is a terminal state.
        """

        STATE_UNSPECIFIED = 0
        APPROVAL_AWAITED = 1
        DENIED = 3
        SCHEDULED = 4
        ACTIVATING = 5
        ACTIVE = 6
        ACTIVATION_FAILED = 7
        EXPIRED = 8
        REVOKING = 9
        REVOKED = 10
        ENDED = 11
        WITHDRAWING = 12
        WITHDRAWN = 13

    class Timeline(proto.Message):
        r"""Timeline of a grant describing what happened to it and when.

        Attributes:
            events (MutableSequence[google.cloud.privilegedaccessmanager_v1.types.Grant.Timeline.Event]):
                Output only. The events that have occurred on this grant.
                This list contains entries in the same order as they
                occurred. The first entry is always be of type ``Requested``
                and there is always at least one entry in this array.
        """

        class Event(proto.Message):
            r"""A single operation on the grant.

            This message has `oneof`_ fields (mutually exclusive fields).
            For each oneof, at most one member field can be set at the same time.
            Setting any member of the oneof automatically clears all other
            members.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                requested (google.cloud.privilegedaccessmanager_v1.types.Grant.Timeline.Event.Requested):
                    The grant was requested.

                    This field is a member of `oneof`_ ``event``.
                approved (google.cloud.privilegedaccessmanager_v1.types.Grant.Timeline.Event.Approved):
                    The grant was approved.

                    This field is a member of `oneof`_ ``event``.
                denied (google.cloud.privilegedaccessmanager_v1.types.Grant.Timeline.Event.Denied):
                    The grant was denied.

                    This field is a member of `oneof`_ ``event``.
                revoked (google.cloud.privilegedaccessmanager_v1.types.Grant.Timeline.Event.Revoked):
                    The grant was revoked.

                    This field is a member of `oneof`_ ``event``.
                scheduled (google.cloud.privilegedaccessmanager_v1.types.Grant.Timeline.Event.Scheduled):
                    The grant has been scheduled to give access.

                    This field is a member of `oneof`_ ``event``.
                activated (google.cloud.privilegedaccessmanager_v1.types.Grant.Timeline.Event.Activated):
                    The grant was successfully activated to give
                    access.

                    This field is a member of `oneof`_ ``event``.
                activation_failed (google.cloud.privilegedaccessmanager_v1.types.Grant.Timeline.Event.ActivationFailed):
                    There was a non-retriable error while trying
                    to give access.

                    This field is a member of `oneof`_ ``event``.
                expired (google.cloud.privilegedaccessmanager_v1.types.Grant.Timeline.Event.Expired):
                    The approval workflow did not complete in the
                    necessary duration, and so the grant is expired.

                    This field is a member of `oneof`_ ``event``.
                ended (google.cloud.privilegedaccessmanager_v1.types.Grant.Timeline.Event.Ended):
                    Access given by the grant ended automatically
                    as the approved duration was over.

                    This field is a member of `oneof`_ ``event``.
                externally_modified (google.cloud.privilegedaccessmanager_v1.types.Grant.Timeline.Event.ExternallyModified):
                    The policy bindings made by grant have been
                    modified outside of PAM.

                    This field is a member of `oneof`_ ``event``.
                withdrawn (google.cloud.privilegedaccessmanager_v1.types.Grant.Timeline.Event.Withdrawn):
                    The grant was withdrawn.

                    This field is a member of `oneof`_ ``event``.
                event_time (google.protobuf.timestamp_pb2.Timestamp):
                    Output only. The time (as recorded at server)
                    when this event occurred.
            """

            class Requested(proto.Message):
                r"""An event representing that a grant was requested.

                Attributes:
                    expire_time (google.protobuf.timestamp_pb2.Timestamp):
                        Output only. The time at which this grant
                        expires unless the approval workflow completes.
                        If omitted, then the request never expires.
                """

                expire_time: timestamp_pb2.Timestamp = proto.Field(
                    proto.MESSAGE,
                    number=1,
                    message=timestamp_pb2.Timestamp,
                )

            class Approved(proto.Message):
                r"""An event representing that the grant was approved.

                Attributes:
                    reason (str):
                        Output only. The reason provided by the
                        approver for approving the grant.
                    actor (str):
                        Output only. Username of the user who
                        approved the grant.
                """

                reason: str = proto.Field(
                    proto.STRING,
                    number=1,
                )
                actor: str = proto.Field(
                    proto.STRING,
                    number=2,
                )

            class Denied(proto.Message):
                r"""An event representing that the grant was denied.

                Attributes:
                    reason (str):
                        Output only. The reason provided by the
                        approver for denying the grant.
                    actor (str):
                        Output only. Username of the user who denied
                        the grant.
                """

                reason: str = proto.Field(
                    proto.STRING,
                    number=1,
                )
                actor: str = proto.Field(
                    proto.STRING,
                    number=2,
                )

            class Revoked(proto.Message):
                r"""An event representing that the grant was revoked.

                Attributes:
                    reason (str):
                        Output only. The reason provided by the user
                        for revoking the grant.
                    actor (str):
                        Output only. Username of the user who revoked
                        the grant.
                """

                reason: str = proto.Field(
                    proto.STRING,
                    number=1,
                )
                actor: str = proto.Field(
                    proto.STRING,
                    number=2,
                )

            class Withdrawn(proto.Message):
                r"""An event representing that the grant was withdrawn."""

            class Scheduled(proto.Message):
                r"""An event representing that the grant has been scheduled to be
                activated later.

                Attributes:
                    scheduled_activation_time (google.protobuf.timestamp_pb2.Timestamp):
                        Output only. The time at which the access is
                        granted.
                """

                scheduled_activation_time: timestamp_pb2.Timestamp = proto.Field(
                    proto.MESSAGE,
                    number=1,
                    message=timestamp_pb2.Timestamp,
                )

            class Activated(proto.Message):
                r"""An event representing that the grant was successfully
                activated.

                """

            class ActivationFailed(proto.Message):
                r"""An event representing that the grant activation failed.

                Attributes:
                    error (google.rpc.status_pb2.Status):
                        Output only. The error that occurred while
                        activating the grant.
                """

                error: status_pb2.Status = proto.Field(
                    proto.MESSAGE,
                    number=1,
                    message=status_pb2.Status,
                )

            class Expired(proto.Message):
                r"""An event representing that the grant was expired."""

            class Ended(proto.Message):
                r"""An event representing that the grant has ended."""

            class ExternallyModified(proto.Message):
                r"""An event representing that the policy bindings made by this
                grant were modified externally.

                """

            requested: "Grant.Timeline.Event.Requested" = proto.Field(
                proto.MESSAGE,
                number=2,
                oneof="event",
                message="Grant.Timeline.Event.Requested",
            )
            approved: "Grant.Timeline.Event.Approved" = proto.Field(
                proto.MESSAGE,
                number=3,
                oneof="event",
                message="Grant.Timeline.Event.Approved",
            )
            denied: "Grant.Timeline.Event.Denied" = proto.Field(
                proto.MESSAGE,
                number=4,
                oneof="event",
                message="Grant.Timeline.Event.Denied",
            )
            revoked: "Grant.Timeline.Event.Revoked" = proto.Field(
                proto.MESSAGE,
                number=5,
                oneof="event",
                message="Grant.Timeline.Event.Revoked",
            )
            scheduled: "Grant.Timeline.Event.Scheduled" = proto.Field(
                proto.MESSAGE,
                number=6,
                oneof="event",
                message="Grant.Timeline.Event.Scheduled",
            )
            activated: "Grant.Timeline.Event.Activated" = proto.Field(
                proto.MESSAGE,
                number=7,
                oneof="event",
                message="Grant.Timeline.Event.Activated",
            )
            activation_failed: "Grant.Timeline.Event.ActivationFailed" = proto.Field(
                proto.MESSAGE,
                number=8,
                oneof="event",
                message="Grant.Timeline.Event.ActivationFailed",
            )
            expired: "Grant.Timeline.Event.Expired" = proto.Field(
                proto.MESSAGE,
                number=10,
                oneof="event",
                message="Grant.Timeline.Event.Expired",
            )
            ended: "Grant.Timeline.Event.Ended" = proto.Field(
                proto.MESSAGE,
                number=11,
                oneof="event",
                message="Grant.Timeline.Event.Ended",
            )
            externally_modified: "Grant.Timeline.Event.ExternallyModified" = (
                proto.Field(
                    proto.MESSAGE,
                    number=12,
                    oneof="event",
                    message="Grant.Timeline.Event.ExternallyModified",
                )
            )
            withdrawn: "Grant.Timeline.Event.Withdrawn" = proto.Field(
                proto.MESSAGE,
                number=13,
                oneof="event",
                message="Grant.Timeline.Event.Withdrawn",
            )
            event_time: timestamp_pb2.Timestamp = proto.Field(
                proto.MESSAGE,
                number=1,
                message=timestamp_pb2.Timestamp,
            )

        events: MutableSequence["Grant.Timeline.Event"] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="Grant.Timeline.Event",
        )

    class AuditTrail(proto.Message):
        r"""Audit trail for the access provided by this grant.

        Attributes:
            access_grant_time (google.protobuf.timestamp_pb2.Timestamp):
                Output only. The time at which access was
                given.
            access_remove_time (google.protobuf.timestamp_pb2.Timestamp):
                Output only. The time at which the system
                removed access. This could be because of an
                automatic expiry or because of a revocation.

                If unspecified, then access hasn't been removed
                yet.
        """

        access_grant_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=1,
            message=timestamp_pb2.Timestamp,
        )
        access_remove_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=2,
            message=timestamp_pb2.Timestamp,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    requester: str = proto.Field(
        proto.STRING,
        number=4,
    )
    requested_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=5,
        message=duration_pb2.Duration,
    )
    justification: "Justification" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="Justification",
    )
    state: State = proto.Field(
        proto.ENUM,
        number=7,
        enum=State,
    )
    timeline: Timeline = proto.Field(
        proto.MESSAGE,
        number=8,
        message=Timeline,
    )
    privileged_access: "PrivilegedAccess" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="PrivilegedAccess",
    )
    audit_trail: AuditTrail = proto.Field(
        proto.MESSAGE,
        number=10,
        message=AuditTrail,
    )
    additional_email_recipients: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=11,
    )
    externally_modified: bool = proto.Field(
        proto.BOOL,
        number=12,
    )


class Justification(proto.Message):
    r"""Justification represents a justification for requesting
    access.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        unstructured_justification (str):
            A free form textual justification. The system
            only ensures that this is not empty. No other
            kind of validation is performed on the string.

            This field is a member of `oneof`_ ``justification``.
    """

    unstructured_justification: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="justification",
    )


class ListGrantsRequest(proto.Message):
    r"""Message for requesting list of grants.

    Attributes:
        parent (str):
            Required. The parent resource which owns the
            grants.
        page_size (int):
            Optional. Requested page size. The server may
            return fewer items than requested. If
            unspecified, the server picks an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. Filtering results.
        order_by (str):
            Optional. Hint for how to order the results
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


class ListGrantsResponse(proto.Message):
    r"""Message for response to listing grants.

    Attributes:
        grants (MutableSequence[google.cloud.privilegedaccessmanager_v1.types.Grant]):
            The list of grants.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    grants: MutableSequence["Grant"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Grant",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class SearchGrantsRequest(proto.Message):
    r"""Request message for ``SearchGrants`` method.

    Attributes:
        parent (str):
            Required. The parent which owns the grant
            resources.
        caller_relationship (google.cloud.privilegedaccessmanager_v1.types.SearchGrantsRequest.CallerRelationshipType):
            Required. Only grants which the caller is
            related to by this relationship are returned in
            the response.
        filter (str):
            Optional. Only grants matching this filter
            are returned in the response.
        page_size (int):
            Optional. Requested page size. The server may
            return fewer items than requested. If
            unspecified, server picks an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
    """

    class CallerRelationshipType(proto.Enum):
        r"""Different types of relationships a user can have with a
        grant.

        Values:
            CALLER_RELATIONSHIP_TYPE_UNSPECIFIED (0):
                Unspecified caller relationship type.
            HAD_CREATED (1):
                The user created this grant by calling ``CreateGrant``
                earlier.
            CAN_APPROVE (2):
                The user is an approver for the entitlement
                that this grant is parented under and can
                currently approve/deny it.
            HAD_APPROVED (3):
                The caller had successfully approved/denied
                this grant earlier.
        """

        CALLER_RELATIONSHIP_TYPE_UNSPECIFIED = 0
        HAD_CREATED = 1
        CAN_APPROVE = 2
        HAD_APPROVED = 3

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    caller_relationship: CallerRelationshipType = proto.Field(
        proto.ENUM,
        number=2,
        enum=CallerRelationshipType,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=3,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=4,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=5,
    )


class SearchGrantsResponse(proto.Message):
    r"""Response message for ``SearchGrants`` method.

    Attributes:
        grants (MutableSequence[google.cloud.privilegedaccessmanager_v1.types.Grant]):
            The list of grants.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
    """

    @property
    def raw_page(self):
        return self

    grants: MutableSequence["Grant"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Grant",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetGrantRequest(proto.Message):
    r"""Message for getting a grant.

    Attributes:
        name (str):
            Required. Name of the resource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ApproveGrantRequest(proto.Message):
    r"""Request message for ``ApproveGrant`` method.

    Attributes:
        name (str):
            Required. Name of the grant resource which is
            being approved.
        reason (str):
            Optional. The reason for approving this grant. This is
            required if the ``require_approver_justification`` field of
            the ``ManualApprovals`` workflow used in this grant is true.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    reason: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DenyGrantRequest(proto.Message):
    r"""Request message for ``DenyGrant`` method.

    Attributes:
        name (str):
            Required. Name of the grant resource which is
            being denied.
        reason (str):
            Optional. The reason for denying this grant. This is
            required if ``require_approver_justification`` field of the
            ``ManualApprovals`` workflow used in this grant is true.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    reason: str = proto.Field(
        proto.STRING,
        number=2,
    )


class RevokeGrantRequest(proto.Message):
    r"""Request message for ``RevokeGrant`` method.

    Attributes:
        name (str):
            Required. Name of the grant resource which is
            being revoked.
        reason (str):
            Optional. The reason for revoking this grant.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    reason: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateGrantRequest(proto.Message):
    r"""Message for creating a grant

    Attributes:
        parent (str):
            Required. Name of the parent entitlement for
            which this grant is being requested.
        grant (google.cloud.privilegedaccessmanager_v1.types.Grant):
            Required. The resource being created.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server knows to
            ignore the request if it has already been
            completed. The server guarantees this for at
            least 60 minutes after the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, ignores the second request. This prevents
            clients from accidentally creating duplicate
            grants.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    grant: "Grant" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Grant",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class OperationMetadata(proto.Message):
    r"""Represents the metadata of the long-running operation.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation was
            created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation finished
            running.
        target (str):
            Output only. Server-defined resource path for
            the target of the operation.
        verb (str):
            Output only. Name of the verb executed by the
            operation.
        status_message (str):
            Output only. Human-readable status of the
            operation, if any.
        requested_cancellation (bool):
            Output only. Identifies whether the user has requested
            cancellation of the operation. Operations that have been
            cancelled successfully have [Operation.error][] value with a
            [google.rpc.Status.code][google.rpc.Status.code] of 1,
            corresponding to ``Code.CANCELLED``.
        api_version (str):
            Output only. API version used to start the
            operation.
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
    verb: str = proto.Field(
        proto.STRING,
        number=4,
    )
    status_message: str = proto.Field(
        proto.STRING,
        number=5,
    )
    requested_cancellation: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    api_version: str = proto.Field(
        proto.STRING,
        number=7,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
