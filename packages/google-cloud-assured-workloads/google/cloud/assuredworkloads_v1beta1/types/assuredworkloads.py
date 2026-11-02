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

__protobuf__ = proto.module(
    package="google.cloud.assuredworkloads.v1beta1",
    manifest={
        "CreateWorkloadRequest",
        "UpdateWorkloadRequest",
        "RestrictAllowedResourcesRequest",
        "RestrictAllowedResourcesResponse",
        "DeleteWorkloadRequest",
        "GetWorkloadRequest",
        "AnalyzeWorkloadMoveRequest",
        "AnalyzeWorkloadMoveResponse",
        "ListWorkloadsRequest",
        "ListWorkloadsResponse",
        "Workload",
        "CreateWorkloadOperationMetadata",
    },
)


class CreateWorkloadRequest(proto.Message):
    r"""Request for creating a workload.

    Attributes:
        parent (str):
            Required. The resource name of the new Workload's parent.
            Must be of the form
            ``organizations/{org_id}/locations/{location_id}``.
        workload (google.cloud.assuredworkloads_v1beta1.types.Workload):
            Required. Assured Workload to create
        external_id (str):
            Optional. A identifier associated with the
            workload and underlying projects which allows
            for the break down of billing costs for a
            workload. The value provided for the identifier
            will add a label to the workload and contained
            projects with the identifier as the value.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    workload: "Workload" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Workload",
    )
    external_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class UpdateWorkloadRequest(proto.Message):
    r"""Request for Updating a workload.

    Attributes:
        workload (google.cloud.assuredworkloads_v1beta1.types.Workload):
            Required. The workload to update. The workload's ``name``
            field is used to identify the workload to be updated.
            Format:
            organizations/{org_id}/locations/{location_id}/workloads/{workload_id}
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The list of fields to be updated.
    """

    workload: "Workload" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Workload",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class RestrictAllowedResourcesRequest(proto.Message):
    r"""Request for restricting list of available resources in
    Workload environment.

    Attributes:
        name (str):
            Required. The resource name of the Workload. This is the
            workloads's relative path in the API, formatted as
            "organizations/{organization_id}/locations/{location_id}/workloads/{workload_id}".
            For example,
            "organizations/123/locations/us-east1/workloads/assured-workload-1".
        restriction_type (google.cloud.assuredworkloads_v1beta1.types.RestrictAllowedResourcesRequest.RestrictionType):
            Required. The type of restriction for using
            gcp products in the Workload environment.
    """

    class RestrictionType(proto.Enum):
        r"""The type of restriction.

        Values:
            RESTRICTION_TYPE_UNSPECIFIED (0):
                Unknown restriction type.
            ALLOW_ALL_GCP_RESOURCES (1):
                Allow the use all of all gcp products,
                irrespective of the compliance posture. This
                effectively removes gcp.restrictServiceUsage
                OrgPolicy on the AssuredWorkloads Folder.
            ALLOW_COMPLIANT_RESOURCES (2):
                Based on Workload's compliance regime,
                allowed list changes. See -
                https://cloud.google.com/assured-workloads/docs/supported-products
                for the list of supported resources.
        """

        RESTRICTION_TYPE_UNSPECIFIED = 0
        ALLOW_ALL_GCP_RESOURCES = 1
        ALLOW_COMPLIANT_RESOURCES = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    restriction_type: RestrictionType = proto.Field(
        proto.ENUM,
        number=2,
        enum=RestrictionType,
    )


class RestrictAllowedResourcesResponse(proto.Message):
    r"""Response for restricting the list of allowed resources."""


class DeleteWorkloadRequest(proto.Message):
    r"""Request for deleting a Workload.

    Attributes:
        name (str):
            Required. The ``name`` field is used to identify the
            workload. Format:
            organizations/{org_id}/locations/{location_id}/workloads/{workload_id}
        etag (str):
            Optional. The etag of the workload.
            If this is provided, it must match the server's
            etag.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetWorkloadRequest(proto.Message):
    r"""Request for fetching a workload.

    Attributes:
        name (str):
            Required. The resource name of the Workload to fetch. This
            is the workloads's relative path in the API, formatted as
            "organizations/{organization_id}/locations/{location_id}/workloads/{workload_id}".
            For example,
            "organizations/123/locations/us-east1/workloads/assured-workload-1".
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class AnalyzeWorkloadMoveRequest(proto.Message):
    r"""A request to analyze a hypothetical move of a source project
    or project-based workload to a target (destination) folder-based
    workload.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        source (str):
            The source type is a project-based workload. Specify the
            workloads's relative resource name, formatted as:
            "organizations/{ORGANIZATION_ID}/locations/{LOCATION_ID}/workloads/{WORKLOAD_ID}"
            For example:
            "organizations/123/locations/us-east1/workloads/assured-workload-1".

            This field is a member of `oneof`_ ``projectOrWorkloadResource``.
        project (str):
            The source type is a project. Specify the project's relative
            resource name, formatted as either a project number or a
            project ID: "projects/{PROJECT_NUMBER}" or
            "projects/{PROJECT_ID}" For example: "projects/951040570662"
            when specifying a project number, or
            "projects/my-project-123" when specifying a project ID.

            This field is a member of `oneof`_ ``projectOrWorkloadResource``.
        target (str):
            Required. The resource ID of the folder-based destination
            workload. This workload is where the source project will
            hypothetically be moved to. Specify the workload's relative
            resource name, formatted as:
            "organizations/{ORGANIZATION_ID}/locations/{LOCATION_ID}/workloads/{WORKLOAD_ID}"
            For example:
            "organizations/123/locations/us-east1/workloads/assured-workload-2".
    """

    source: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="projectOrWorkloadResource",
    )
    project: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="projectOrWorkloadResource",
    )
    target: str = proto.Field(
        proto.STRING,
        number=2,
    )


class AnalyzeWorkloadMoveResponse(proto.Message):
    r"""A response that includes the analysis of the hypothetical
    resource move.

    Attributes:
        blockers (MutableSequence[str]):
            A list of blockers that should be addressed
            before moving the source project or
            project-based workload to the destination
            folder-based workload.
    """

    blockers: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class ListWorkloadsRequest(proto.Message):
    r"""Request for fetching workloads in an organization.

    Attributes:
        parent (str):
            Required. Parent Resource to list workloads from. Must be of
            the form ``organizations/{org_id}/locations/{location}``.
        page_size (int):
            Page size.
        page_token (str):
            Page token returned from previous request.
            Page token contains context from previous
            request. Page token needs to be passed in the
            second and following requests.
        filter (str):
            A custom filter for filtering by properties
            of a workload. At this time, only filtering by
            labels is supported.
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


class ListWorkloadsResponse(proto.Message):
    r"""Response of ListWorkloads endpoint.

    Attributes:
        workloads (MutableSequence[google.cloud.assuredworkloads_v1beta1.types.Workload]):
            List of Workloads under a given parent.
        next_page_token (str):
            The next page token. Return empty if reached
            the last page.
    """

    @property
    def raw_page(self):
        return self

    workloads: MutableSequence["Workload"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Workload",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class Workload(proto.Message):
    r"""An Workload object for managing highly regulated workloads of
    cloud customers.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Optional. The resource name of the workload.
            Format:

            organizations/{organization}/locations/{location}/workloads/{workload}

            Read-only.
        display_name (str):
            Required. The user-assigned display name of
            the Workload. When present it must be between 4
            to 30 characters. Allowed characters are:
            lowercase and uppercase letters, numbers,
            hyphen, and spaces.

            Example: My Workload
        resources (MutableSequence[google.cloud.assuredworkloads_v1beta1.types.Workload.ResourceInfo]):
            Output only. The resources associated with
            this workload. These resources will be created
            when creating the workload. If any of the
            projects already exist, the workload creation
            will fail. Always read only.
        compliance_regime (google.cloud.assuredworkloads_v1beta1.types.Workload.ComplianceRegime):
            Required. Immutable. Compliance Regime
            associated with this workload.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Immutable. The Workload creation
            timestamp.
        billing_account (str):
            Output only. The billing account used for the resources
            which are direct children of workload. This billing account
            is initially associated with the resources created as part
            of Workload creation. After the initial creation of these
            resources, the customer can change the assigned billing
            account. The resource name has the form
            ``billingAccounts/{billing_account_id}``. For example,
            ``billingAccounts/012345-567890-ABCDEF``.
        il4_settings (google.cloud.assuredworkloads_v1beta1.types.Workload.IL4Settings):
            Input only. Immutable. Settings specific to
            resources needed for IL4.

            This field is a member of `oneof`_ ``compliance_regime_settings``.
        cjis_settings (google.cloud.assuredworkloads_v1beta1.types.Workload.CJISSettings):
            Input only. Immutable. Settings specific to
            resources needed for CJIS.

            This field is a member of `oneof`_ ``compliance_regime_settings``.
        fedramp_high_settings (google.cloud.assuredworkloads_v1beta1.types.Workload.FedrampHighSettings):
            Input only. Immutable. Settings specific to
            resources needed for FedRAMP High.

            This field is a member of `oneof`_ ``compliance_regime_settings``.
        fedramp_moderate_settings (google.cloud.assuredworkloads_v1beta1.types.Workload.FedrampModerateSettings):
            Input only. Immutable. Settings specific to
            resources needed for FedRAMP Moderate.

            This field is a member of `oneof`_ ``compliance_regime_settings``.
        etag (str):
            Optional. ETag of the workload, it is
            calculated on the basis of the Workload
            contents. It will be used in Update & Delete
            operations.
        labels (MutableMapping[str, str]):
            Optional. Labels applied to the workload.
        provisioned_resources_parent (str):
            Input only. The parent resource for the resources managed by
            this Assured Workload. May be either empty or a folder
            resource which is a child of the Workload parent. If not
            specified all resources are created under the parent
            organization. Format: folders/{folder_id}
        kms_settings (google.cloud.assuredworkloads_v1beta1.types.Workload.KMSSettings):
            Input only. Settings used to create a CMEK crypto key. When
            set, a project with a KMS CMEK key is provisioned. This
            field is deprecated as of Feb 28, 2022. In order to create a
            Keyring, callers should specify, ENCRYPTION_KEYS_PROJECT or
            KEYRING in ResourceSettings.resource_type field.
        resource_settings (MutableSequence[google.cloud.assuredworkloads_v1beta1.types.Workload.ResourceSettings]):
            Input only. Resource properties that are used
            to customize workload resources. These
            properties (such as custom project id) will be
            used to create workload resources if possible.
            This field is optional.
        kaj_enrollment_state (google.cloud.assuredworkloads_v1beta1.types.Workload.KajEnrollmentState):
            Output only. Represents the KAJ enrollment
            state of the given workload.
        enable_sovereign_controls (bool):
            Optional. Indicates the sovereignty status of
            the given workload. Currently meant to be used
            by Europe/Canada customers.
        saa_enrollment_response (google.cloud.assuredworkloads_v1beta1.types.Workload.SaaEnrollmentResponse):
            Output only. Represents the SAA enrollment
            response of the given workload. SAA enrollment
            response is queried during GetWorkload call. In
            failure cases, user friendly error message is
            shown in SAA details page.
        compliant_but_disallowed_services (MutableSequence[str]):
            Output only. Urls for services which are
            compliant for this Assured Workload, but which
            are currently disallowed by the
            ResourceUsageRestriction org policy. Invoke
            RestrictAllowedResources endpoint to allow your
            project developers to use these services in
            their environment.".
    """

    class ComplianceRegime(proto.Enum):
        r"""Supported Compliance Regimes.

        Values:
            COMPLIANCE_REGIME_UNSPECIFIED (0):
                Unknown compliance regime.
            IL4 (1):
                Information protection as per DoD IL4
                requirements.
            CJIS (2):
                Criminal Justice Information Services (CJIS)
                Security policies.
            FEDRAMP_HIGH (3):
                FedRAMP High data protection controls
            FEDRAMP_MODERATE (4):
                FedRAMP Moderate data protection controls
            US_REGIONAL_ACCESS (5):
                Assured Workloads For US Regions data
                protection controls
            HIPAA (6):
                Health Insurance Portability and
                Accountability Act controls
            HITRUST (7):
                Health Information Trust Alliance controls
            EU_REGIONS_AND_SUPPORT (8):
                Assured Workloads For EU Regions and Support
                controls
            CA_REGIONS_AND_SUPPORT (9):
                Assured Workloads For Canada Regions and
                Support controls
            ITAR (10):
                International Traffic in Arms Regulations
            AU_REGIONS_AND_US_SUPPORT (11):
                Assured Workloads for Australia Regions and
                Support controls
        """

        COMPLIANCE_REGIME_UNSPECIFIED = 0
        IL4 = 1
        CJIS = 2
        FEDRAMP_HIGH = 3
        FEDRAMP_MODERATE = 4
        US_REGIONAL_ACCESS = 5
        HIPAA = 6
        HITRUST = 7
        EU_REGIONS_AND_SUPPORT = 8
        CA_REGIONS_AND_SUPPORT = 9
        ITAR = 10
        AU_REGIONS_AND_US_SUPPORT = 11

    class KajEnrollmentState(proto.Enum):
        r"""Key Access Justifications(KAJ) Enrollment State.

        Values:
            KAJ_ENROLLMENT_STATE_UNSPECIFIED (0):
                Default State for KAJ Enrollment.
            KAJ_ENROLLMENT_STATE_PENDING (1):
                Pending State for KAJ Enrollment.
            KAJ_ENROLLMENT_STATE_COMPLETE (2):
                Complete State for KAJ Enrollment.
        """

        KAJ_ENROLLMENT_STATE_UNSPECIFIED = 0
        KAJ_ENROLLMENT_STATE_PENDING = 1
        KAJ_ENROLLMENT_STATE_COMPLETE = 2

    class ResourceInfo(proto.Message):
        r"""Represent the resources that are children of this Workload.

        Attributes:
            resource_id (int):
                Resource identifier. For a project this represents
                project_number.
            resource_type (google.cloud.assuredworkloads_v1beta1.types.Workload.ResourceInfo.ResourceType):
                Indicates the type of resource.
        """

        class ResourceType(proto.Enum):
            r"""The type of resource.

            Values:
                RESOURCE_TYPE_UNSPECIFIED (0):
                    Unknown resource type.
                CONSUMER_PROJECT (1):
                    Deprecated. Existing workloads will continue
                    to support this, but new CreateWorkloadRequests
                    should not specify this as an input value.
                CONSUMER_FOLDER (4):
                    Consumer Folder.
                ENCRYPTION_KEYS_PROJECT (2):
                    Consumer project containing encryption keys.
                KEYRING (3):
                    Keyring resource that hosts encryption keys.
            """

            RESOURCE_TYPE_UNSPECIFIED = 0
            CONSUMER_PROJECT = 1
            CONSUMER_FOLDER = 4
            ENCRYPTION_KEYS_PROJECT = 2
            KEYRING = 3

        resource_id: int = proto.Field(
            proto.INT64,
            number=1,
        )
        resource_type: "Workload.ResourceInfo.ResourceType" = proto.Field(
            proto.ENUM,
            number=2,
            enum="Workload.ResourceInfo.ResourceType",
        )

    class KMSSettings(proto.Message):
        r"""Settings specific to the Key Management Service.

        Attributes:
            next_rotation_time (google.protobuf.timestamp_pb2.Timestamp):
                Required. Input only. Immutable. The time at
                which the Key Management Service will
                automatically create a new version of the crypto
                key and mark it as the primary.
            rotation_period (google.protobuf.duration_pb2.Duration):
                Required. Input only. Immutable. [next_rotation_time] will
                be advanced by this period when the Key Management Service
                automatically rotates a key. Must be at least 24 hours and
                at most 876,000 hours.
        """

        next_rotation_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=1,
            message=timestamp_pb2.Timestamp,
        )
        rotation_period: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=2,
            message=duration_pb2.Duration,
        )

    class IL4Settings(proto.Message):
        r"""Settings specific to resources needed for IL4.

        Attributes:
            kms_settings (google.cloud.assuredworkloads_v1beta1.types.Workload.KMSSettings):
                Input only. Immutable. Settings used to
                create a CMEK crypto key.
        """

        kms_settings: "Workload.KMSSettings" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="Workload.KMSSettings",
        )

    class CJISSettings(proto.Message):
        r"""Settings specific to resources needed for CJIS.

        Attributes:
            kms_settings (google.cloud.assuredworkloads_v1beta1.types.Workload.KMSSettings):
                Input only. Immutable. Settings used to
                create a CMEK crypto key.
        """

        kms_settings: "Workload.KMSSettings" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="Workload.KMSSettings",
        )

    class FedrampHighSettings(proto.Message):
        r"""Settings specific to resources needed for FedRAMP High.

        Attributes:
            kms_settings (google.cloud.assuredworkloads_v1beta1.types.Workload.KMSSettings):
                Input only. Immutable. Settings used to
                create a CMEK crypto key.
        """

        kms_settings: "Workload.KMSSettings" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="Workload.KMSSettings",
        )

    class FedrampModerateSettings(proto.Message):
        r"""Settings specific to resources needed for FedRAMP Moderate.

        Attributes:
            kms_settings (google.cloud.assuredworkloads_v1beta1.types.Workload.KMSSettings):
                Input only. Immutable. Settings used to
                create a CMEK crypto key.
        """

        kms_settings: "Workload.KMSSettings" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="Workload.KMSSettings",
        )

    class ResourceSettings(proto.Message):
        r"""Represent the custom settings for the resources to be
        created.

        Attributes:
            resource_id (str):
                Resource identifier. For a project this represents
                project_id. If the project is already taken, the workload
                creation will fail. For KeyRing, this represents the
                keyring_id. For a folder, don't set this value as folder_id
                is assigned by Google.
            resource_type (google.cloud.assuredworkloads_v1beta1.types.Workload.ResourceInfo.ResourceType):
                Indicates the type of resource. This field should be
                specified to correspond the id to the right project type
                (CONSUMER_PROJECT or ENCRYPTION_KEYS_PROJECT)
            display_name (str):
                User-assigned resource display name.
                If not empty it will be used to create a
                resource with the specified name.
        """

        resource_id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        resource_type: "Workload.ResourceInfo.ResourceType" = proto.Field(
            proto.ENUM,
            number=2,
            enum="Workload.ResourceInfo.ResourceType",
        )
        display_name: str = proto.Field(
            proto.STRING,
            number=3,
        )

    class SaaEnrollmentResponse(proto.Message):
        r"""Signed Access Approvals (SAA) enrollment response.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            setup_status (google.cloud.assuredworkloads_v1beta1.types.Workload.SaaEnrollmentResponse.SetupState):
                Indicates SAA enrollment status of a given
                workload.

                This field is a member of `oneof`_ ``_setup_status``.
            setup_errors (MutableSequence[google.cloud.assuredworkloads_v1beta1.types.Workload.SaaEnrollmentResponse.SetupError]):
                Indicates SAA enrollment setup error if any.
        """

        class SetupState(proto.Enum):
            r"""Setup state of SAA enrollment.

            Values:
                SETUP_STATE_UNSPECIFIED (0):
                    Unspecified.
                STATUS_PENDING (1):
                    SAA enrollment pending.
                STATUS_COMPLETE (2):
                    SAA enrollment comopleted.
            """

            SETUP_STATE_UNSPECIFIED = 0
            STATUS_PENDING = 1
            STATUS_COMPLETE = 2

        class SetupError(proto.Enum):
            r"""Setup error of SAA enrollment.

            Values:
                SETUP_ERROR_UNSPECIFIED (0):
                    Unspecified.
                ERROR_INVALID_BASE_SETUP (1):
                    Invalid states for all customers, to be
                    redirected to AA UI for additional details.
                ERROR_MISSING_EXTERNAL_SIGNING_KEY (2):
                    Returned when there is not an EKM key
                    configured.
                ERROR_NOT_ALL_SERVICES_ENROLLED (3):
                    Returned when there are no enrolled services
                    or the customer is enrolled in CAA only for a
                    subset of services.
                ERROR_SETUP_CHECK_FAILED (4):
                    Returned when exception was encountered
                    during evaluation of other criteria.
            """

            SETUP_ERROR_UNSPECIFIED = 0
            ERROR_INVALID_BASE_SETUP = 1
            ERROR_MISSING_EXTERNAL_SIGNING_KEY = 2
            ERROR_NOT_ALL_SERVICES_ENROLLED = 3
            ERROR_SETUP_CHECK_FAILED = 4

        setup_status: "Workload.SaaEnrollmentResponse.SetupState" = proto.Field(
            proto.ENUM,
            number=1,
            optional=True,
            enum="Workload.SaaEnrollmentResponse.SetupState",
        )
        setup_errors: MutableSequence["Workload.SaaEnrollmentResponse.SetupError"] = (
            proto.RepeatedField(
                proto.ENUM,
                number=2,
                enum="Workload.SaaEnrollmentResponse.SetupError",
            )
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    resources: MutableSequence[ResourceInfo] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=ResourceInfo,
    )
    compliance_regime: ComplianceRegime = proto.Field(
        proto.ENUM,
        number=4,
        enum=ComplianceRegime,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    billing_account: str = proto.Field(
        proto.STRING,
        number=6,
    )
    il4_settings: IL4Settings = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="compliance_regime_settings",
        message=IL4Settings,
    )
    cjis_settings: CJISSettings = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="compliance_regime_settings",
        message=CJISSettings,
    )
    fedramp_high_settings: FedrampHighSettings = proto.Field(
        proto.MESSAGE,
        number=11,
        oneof="compliance_regime_settings",
        message=FedrampHighSettings,
    )
    fedramp_moderate_settings: FedrampModerateSettings = proto.Field(
        proto.MESSAGE,
        number=12,
        oneof="compliance_regime_settings",
        message=FedrampModerateSettings,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=9,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=10,
    )
    provisioned_resources_parent: str = proto.Field(
        proto.STRING,
        number=13,
    )
    kms_settings: KMSSettings = proto.Field(
        proto.MESSAGE,
        number=14,
        message=KMSSettings,
    )
    resource_settings: MutableSequence[ResourceSettings] = proto.RepeatedField(
        proto.MESSAGE,
        number=15,
        message=ResourceSettings,
    )
    kaj_enrollment_state: KajEnrollmentState = proto.Field(
        proto.ENUM,
        number=17,
        enum=KajEnrollmentState,
    )
    enable_sovereign_controls: bool = proto.Field(
        proto.BOOL,
        number=18,
    )
    saa_enrollment_response: SaaEnrollmentResponse = proto.Field(
        proto.MESSAGE,
        number=20,
        message=SaaEnrollmentResponse,
    )
    compliant_but_disallowed_services: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=24,
    )


class CreateWorkloadOperationMetadata(proto.Message):
    r"""Operation metadata to give request details of CreateWorkload.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. Time when the operation was
            created.
        display_name (str):
            Optional. The display name of the workload.
        parent (str):
            Optional. The parent of the workload.
        compliance_regime (google.cloud.assuredworkloads_v1beta1.types.Workload.ComplianceRegime):
            Optional. Compliance controls that should be
            applied to the resources managed by the
            workload.
        resource_settings (MutableSequence[google.cloud.assuredworkloads_v1beta1.types.Workload.ResourceSettings]):
            Optional. Resource properties in the input
            that are used for creating/customizing workload
            resources.
    """

    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    parent: str = proto.Field(
        proto.STRING,
        number=3,
    )
    compliance_regime: "Workload.ComplianceRegime" = proto.Field(
        proto.ENUM,
        number=4,
        enum="Workload.ComplianceRegime",
    )
    resource_settings: MutableSequence["Workload.ResourceSettings"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=5,
            message="Workload.ResourceSettings",
        )
    )


__all__ = tuple(sorted(__protobuf__.manifest))
