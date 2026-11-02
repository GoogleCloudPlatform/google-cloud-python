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
    package="google.cloud.accessapproval.v1",
    manifest={
        "EnrollmentLevel",
        "AccessLocations",
        "AccessReason",
        "SignatureInfo",
        "ApproveDecision",
        "DismissDecision",
        "ResourceProperties",
        "ApprovalRequest",
        "EnrolledService",
        "AccessApprovalSettings",
        "AccessApprovalServiceAccount",
        "ListApprovalRequestsMessage",
        "ListApprovalRequestsResponse",
        "GetApprovalRequestMessage",
        "ApproveApprovalRequestMessage",
        "DismissApprovalRequestMessage",
        "InvalidateApprovalRequestMessage",
        "GetAccessApprovalSettingsMessage",
        "UpdateAccessApprovalSettingsMessage",
        "DeleteAccessApprovalSettingsMessage",
        "GetAccessApprovalServiceAccountMessage",
    },
)


class EnrollmentLevel(proto.Enum):
    r"""Represents the type of enrollment for a given service to
    Access Approval.

    Values:
        ENROLLMENT_LEVEL_UNSPECIFIED (0):
            Default value for proto, shouldn't be used.
        BLOCK_ALL (1):
            Service is enrolled in Access Approval for
            all requests
    """

    ENROLLMENT_LEVEL_UNSPECIFIED = 0
    BLOCK_ALL = 1


class AccessLocations(proto.Message):
    r"""Home office and physical location of the principal.

    Attributes:
        principal_office_country (str):
            The "home office" location of the principal. A two-letter
            country code (ISO 3166-1 alpha-2), such as "US", "DE" or
            "GB" or a region code. In some limited situations Google
            systems may refer refer to a region code instead of a
            country code. Possible Region Codes:

            - ASI: Asia
            - EUR: Europe
            - OCE: Oceania
            - AFR: Africa
            - NAM: North America
            - SAM: South America
            - ANT: Antarctica
            - ANY: Any location
        principal_physical_location_country (str):
            Physical location of the principal at the time of the
            access. A two-letter country code (ISO 3166-1 alpha-2), such
            as "US", "DE" or "GB" or a region code. In some limited
            situations Google systems may refer refer to a region code
            instead of a country code. Possible Region Codes:

            - ASI: Asia
            - EUR: Europe
            - OCE: Oceania
            - AFR: Africa
            - NAM: North America
            - SAM: South America
            - ANT: Antarctica
            - ANY: Any location
    """

    principal_office_country: str = proto.Field(
        proto.STRING,
        number=1,
    )
    principal_physical_location_country: str = proto.Field(
        proto.STRING,
        number=2,
    )


class AccessReason(proto.Message):
    r"""

    Attributes:
        type_ (google.cloud.accessapproval_v1.types.AccessReason.Type):
            Type of access justification.
        detail (str):
            More detail about certain reason types. See
            comments for each type above.
    """

    class Type(proto.Enum):
        r"""Type of access justification.

        Values:
            TYPE_UNSPECIFIED (0):
                Default value for proto, shouldn't be used.
            CUSTOMER_INITIATED_SUPPORT (1):
                Customer made a request or raised an issue that required the
                principal to access customer data. ``detail`` is of the form
                ("#####" is the issue ID):

                - "Feedback Report: #####"
                - "Case Number: #####"
                - "Case ID: #####"
                - "E-PIN Reference: #####"
                - "Google-#####"
                - "T-#####".
            GOOGLE_INITIATED_SERVICE (2):
                The principal accessed customer data in order
                to diagnose or resolve a suspected issue in
                services. Often this access is used to confirm
                that customers are not affected by a suspected
                service issue or to remediate a reversible
                system issue.
            GOOGLE_INITIATED_REVIEW (3):
                Google initiated service for security, fraud,
                abuse, or compliance purposes.
            THIRD_PARTY_DATA_REQUEST (4):
                The principal was compelled to access
                customer data in order to respond to a legal
                third party data request or process, including
                legal processes from customers themselves.
            GOOGLE_RESPONSE_TO_PRODUCTION_ALERT (5):
                The principal accessed customer data in order
                to diagnose or resolve a suspected issue in
                services or a known outage.
        """

        TYPE_UNSPECIFIED = 0
        CUSTOMER_INITIATED_SUPPORT = 1
        GOOGLE_INITIATED_SERVICE = 2
        GOOGLE_INITIATED_REVIEW = 3
        THIRD_PARTY_DATA_REQUEST = 4
        GOOGLE_RESPONSE_TO_PRODUCTION_ALERT = 5

    type_: Type = proto.Field(
        proto.ENUM,
        number=1,
        enum=Type,
    )
    detail: str = proto.Field(
        proto.STRING,
        number=2,
    )


class SignatureInfo(proto.Message):
    r"""Information about the digital signature of the resource.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        signature (bytes):
            The digital signature.
        google_public_key_pem (str):
            The public key for the Google default
            signing, encoded in PEM format. The signature
            was created using a private key which may be
            verified using this public key.

            This field is a member of `oneof`_ ``verification_info``.
        customer_kms_key_version (str):
            The resource name of the customer
            CryptoKeyVersion used for signing.

            This field is a member of `oneof`_ ``verification_info``.
    """

    signature: bytes = proto.Field(
        proto.BYTES,
        number=1,
    )
    google_public_key_pem: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="verification_info",
    )
    customer_kms_key_version: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="verification_info",
    )


class ApproveDecision(proto.Message):
    r"""A decision that has been made to approve access to a
    resource.

    Attributes:
        approve_time (google.protobuf.timestamp_pb2.Timestamp):
            The time at which approval was granted.
        expire_time (google.protobuf.timestamp_pb2.Timestamp):
            The time at which the approval expires.
        invalidate_time (google.protobuf.timestamp_pb2.Timestamp):
            If set, denotes the timestamp at which the
            approval is invalidated.
        signature_info (google.cloud.accessapproval_v1.types.SignatureInfo):
            The signature for the ApprovalRequest and
            details on how it was signed.
        auto_approved (bool):
            True when the request has been auto-approved.
    """

    approve_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    expire_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    invalidate_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    signature_info: "SignatureInfo" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="SignatureInfo",
    )
    auto_approved: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class DismissDecision(proto.Message):
    r"""A decision that has been made to dismiss an approval request.

    Attributes:
        dismiss_time (google.protobuf.timestamp_pb2.Timestamp):
            The time at which the approval request was
            dismissed.
        implicit (bool):
            This field will be true if the
            ApprovalRequest was implicitly dismissed due to
            inaction by the access approval approvers (the
            request is not acted on by the approvers before
            the exiration time).
    """

    dismiss_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    implicit: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class ResourceProperties(proto.Message):
    r"""The properties associated with the resource of the request.

    Attributes:
        excludes_descendants (bool):
            Whether an approval will exclude the
            descendants of the resource being requested.
    """

    excludes_descendants: bool = proto.Field(
        proto.BOOL,
        number=1,
    )


class ApprovalRequest(proto.Message):
    r"""A request for the customer to approve access to a resource.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            The resource name of the request. Format is
            "{projects|folders|organizations}/{id}/approvalRequests/{approval_request}".
        requested_resource_name (str):
            The resource for which approval is being requested. The
            format of the resource name is defined at
            https://cloud.google.com/apis/design/resource_names. The
            resource name here may either be a "full" resource name
            (e.g. "//library.googleapis.com/shelves/shelf1/books/book2")
            or a "relative" resource name (e.g.
            "shelves/shelf1/books/book2") as described in the resource
            name specification.
        requested_resource_properties (google.cloud.accessapproval_v1.types.ResourceProperties):
            Properties related to the resource represented by
            requested_resource_name.
        requested_reason (google.cloud.accessapproval_v1.types.AccessReason):
            The justification for which approval is being
            requested.
        requested_locations (google.cloud.accessapproval_v1.types.AccessLocations):
            The locations for which approval is being
            requested.
        request_time (google.protobuf.timestamp_pb2.Timestamp):
            The time at which approval was requested.
        requested_expiration (google.protobuf.timestamp_pb2.Timestamp):
            The requested expiration for the approval. If
            the request is approved, access will be granted
            from the time of approval until the expiration
            time.
        approve (google.cloud.accessapproval_v1.types.ApproveDecision):
            Access was approved.

            This field is a member of `oneof`_ ``decision``.
        dismiss (google.cloud.accessapproval_v1.types.DismissDecision):
            The request was dismissed.

            This field is a member of `oneof`_ ``decision``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requested_resource_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    requested_resource_properties: "ResourceProperties" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="ResourceProperties",
    )
    requested_reason: "AccessReason" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="AccessReason",
    )
    requested_locations: "AccessLocations" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="AccessLocations",
    )
    request_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    requested_expiration: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    approve: "ApproveDecision" = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="decision",
        message="ApproveDecision",
    )
    dismiss: "DismissDecision" = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="decision",
        message="DismissDecision",
    )


class EnrolledService(proto.Message):
    r"""Represents the enrollment of a cloud resource into a specific
    service.

    Attributes:
        cloud_product (str):
            The product for which Access Approval will be enrolled.
            Allowed values are listed below (case-sensitive):

            - all
            - GA
            - App Engine
            - BigQuery
            - Cloud Bigtable
            - Cloud Key Management Service
            - Compute Engine
            - Cloud Dataflow
            - Cloud Dataproc
            - Cloud DLP
            - Cloud EKM
            - Cloud HSM
            - Cloud Identity and Access Management
            - Cloud Logging
            - Cloud Pub/Sub
            - Cloud Spanner
            - Cloud SQL
            - Cloud Storage
            - Google Kubernetes Engine
            - Organization Policy Serivice
            - Persistent Disk
            - Resource Manager
            - Secret Manager
            - Speaker ID

            Note: These values are supported as input for legacy
            purposes, but will not be returned from the API.

            - all
            - ga-only
            - appengine.googleapis.com
            - bigquery.googleapis.com
            - bigtable.googleapis.com
            - container.googleapis.com
            - cloudkms.googleapis.com
            - cloudresourcemanager.googleapis.com
            - cloudsql.googleapis.com
            - compute.googleapis.com
            - dataflow.googleapis.com
            - dataproc.googleapis.com
            - dlp.googleapis.com
            - iam.googleapis.com
            - logging.googleapis.com
            - orgpolicy.googleapis.com
            - pubsub.googleapis.com
            - spanner.googleapis.com
            - secretmanager.googleapis.com
            - speakerid.googleapis.com
            - storage.googleapis.com

            Calls to UpdateAccessApprovalSettings using 'all' or any of
            the XXX.googleapis.com will be translated to the associated
            product name ('all', 'App Engine', etc.).

            Note: 'all' will enroll the resource in all products
            supported at both 'GA' and 'Preview' levels.

            More information about levels of support is available at
            https://cloud.google.com/access-approval/docs/supported-services
        enrollment_level (google.cloud.accessapproval_v1.types.EnrollmentLevel):
            The enrollment level of the service.
    """

    cloud_product: str = proto.Field(
        proto.STRING,
        number=1,
    )
    enrollment_level: "EnrollmentLevel" = proto.Field(
        proto.ENUM,
        number=2,
        enum="EnrollmentLevel",
    )


class AccessApprovalSettings(proto.Message):
    r"""Settings on a Project/Folder/Organization related to Access
    Approval.

    Attributes:
        name (str):
            The resource name of the settings. Format is one of:

            - "projects/{project}/accessApprovalSettings"
            - "folders/{folder}/accessApprovalSettings"
            - "organizations/{organization}/accessApprovalSettings".
        notification_emails (MutableSequence[str]):
            A list of email addresses to which
            notifications relating to approval requests
            should be sent. Notifications relating to a
            resource will be sent to all emails in the
            settings of ancestor resources of that resource.
            A maximum of 50 email addresses are allowed.
        enrolled_services (MutableSequence[google.cloud.accessapproval_v1.types.EnrolledService]):
            A list of Google Cloud Services for which the given resource
            has Access Approval enrolled. Access requests for the
            resource given by name against any of these services
            contained here will be required to have explicit approval.
            If name refers to an organization, enrollment can be done
            for individual services. If name refers to a folder or
            project, enrollment can only be done on an all or nothing
            basis.

            If a cloud_product is repeated in this list, the first entry
            will be honored and all following entries will be discarded.
            A maximum of 10 enrolled services will be enforced, to be
            expanded as the set of supported services is expanded.
        enrolled_ancestor (bool):
            Output only. This field is read only (not
            settable via UpdateAccessApprovalSettings
            method). If the field is true, that indicates
            that at least one service is enrolled for Access
            Approval in one or more ancestors of the Project
            or Folder (this field will always be unset for
            the organization since organizations do not have
            ancestors).
        active_key_version (str):
            The asymmetric crypto key version to use for signing
            approval requests. Empty active_key_version indicates that a
            Google-managed key should be used for signing. This property
            will be ignored if set by an ancestor of this resource, and
            new non-empty values may not be set.
        ancestor_has_active_key_version (bool):
            Output only. This field is read only (not settable via
            UpdateAccessApprovalSettings method). If the field is true,
            that indicates that an ancestor of this Project or Folder
            has set active_key_version (this field will always be unset
            for the organization since organizations do not have
            ancestors).
        invalid_key_version (bool):
            Output only. This field is read only (not settable via
            UpdateAccessApprovalSettings method). If the field is true,
            that indicates that there is some configuration issue with
            the active_key_version configured at this level in the
            resource hierarchy (e.g. it doesn't exist or the Access
            Approval service account doesn't have the correct
            permissions on it, etc.) This key version is not necessarily
            the effective key version at this level, as key versions are
            inherited top-down.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    notification_emails: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    enrolled_services: MutableSequence["EnrolledService"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="EnrolledService",
    )
    enrolled_ancestor: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    active_key_version: str = proto.Field(
        proto.STRING,
        number=6,
    )
    ancestor_has_active_key_version: bool = proto.Field(
        proto.BOOL,
        number=7,
    )
    invalid_key_version: bool = proto.Field(
        proto.BOOL,
        number=8,
    )


class AccessApprovalServiceAccount(proto.Message):
    r"""Access Approval service account related to a
    project/folder/organization.

    Attributes:
        name (str):
            The resource name of the Access Approval service account.
            Format is one of:

            - "projects/{project}/serviceAccount"
            - "folders/{folder}/serviceAccount"
            - "organizations/{organization}/serviceAccount".
        account_email (str):
            Email address of the service account.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    account_email: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListApprovalRequestsMessage(proto.Message):
    r"""Request to list approval requests.

    Attributes:
        parent (str):
            The parent resource. This may be
            "projects/{project}", "folders/{folder}", or
            "organizations/{organization}".
        filter (str):
            A filter on the type of approval requests to retrieve. Must
            be one of the following values:

            - [not set]: Requests that are pending or have active
              approvals.
            - ALL: All requests.
            - PENDING: Only pending requests.
            - ACTIVE: Only active (i.e. currently approved) requests.
            - DISMISSED: Only requests that have been dismissed, or
              requests that are not approved and past expiration.
            - EXPIRED: Only requests that have been approved, and the
              approval has expired.
            - HISTORY: Active, dismissed and expired requests.
        page_size (int):
            Requested page size.
        page_token (str):
            A token identifying the page of results to
            return.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListApprovalRequestsResponse(proto.Message):
    r"""Response to listing of ApprovalRequest objects.

    Attributes:
        approval_requests (MutableSequence[google.cloud.accessapproval_v1.types.ApprovalRequest]):
            Approval request details.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more.
    """

    @property
    def raw_page(self):
        return self

    approval_requests: MutableSequence["ApprovalRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ApprovalRequest",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetApprovalRequestMessage(proto.Message):
    r"""Request to get an approval request.

    Attributes:
        name (str):
            The name of the approval request to retrieve. Format:
            "{projects|folders|organizations}/{id}/approvalRequests/{approval_request}".
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ApproveApprovalRequestMessage(proto.Message):
    r"""Request to approve an ApprovalRequest.

    Attributes:
        name (str):
            Name of the approval request to approve.
        expire_time (google.protobuf.timestamp_pb2.Timestamp):
            The expiration time of this approval.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    expire_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )


class DismissApprovalRequestMessage(proto.Message):
    r"""Request to dismiss an approval request.

    Attributes:
        name (str):
            Name of the ApprovalRequest to dismiss.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class InvalidateApprovalRequestMessage(proto.Message):
    r"""Request to invalidate an existing approval.

    Attributes:
        name (str):
            Name of the ApprovalRequest to invalidate.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetAccessApprovalSettingsMessage(proto.Message):
    r"""Request to get access approval settings.

    Attributes:
        name (str):
            The name of the AccessApprovalSettings to retrieve. Format:
            "{projects|folders|organizations}/{id}/accessApprovalSettings".
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateAccessApprovalSettingsMessage(proto.Message):
    r"""Request to update access approval settings.

    Attributes:
        settings (google.cloud.accessapproval_v1.types.AccessApprovalSettings):
            The new AccessApprovalSettings.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The update mask applies to the settings. Only the top level
            fields of AccessApprovalSettings (notification_emails &
            enrolled_services) are supported. For each field, if it is
            included, the currently stored value will be entirely
            overwritten with the value of the field passed in this
            request.

            For the ``FieldMask`` definition, see
            https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask
            If this field is left unset, only the notification_emails
            field will be updated.
    """

    settings: "AccessApprovalSettings" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="AccessApprovalSettings",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteAccessApprovalSettingsMessage(proto.Message):
    r"""Request to delete access approval settings.

    Attributes:
        name (str):
            Name of the AccessApprovalSettings to delete.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetAccessApprovalServiceAccountMessage(proto.Message):
    r"""Request to get an Access Approval service account.

    Attributes:
        name (str):
            Name of the AccessApprovalServiceAccount to
            retrieve.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
