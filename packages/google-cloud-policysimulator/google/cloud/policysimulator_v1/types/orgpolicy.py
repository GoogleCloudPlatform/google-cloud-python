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
from google.cloud.orgpolicy_v2.types import constraint
from google.cloud.orgpolicy_v2.types import orgpolicy as gcov_orgpolicy

__protobuf__ = proto.module(
    package="google.cloud.policysimulator.v1",
    manifest={
        "PreviewState",
        "OrgPolicyViolationsPreview",
        "OrgPolicyViolation",
        "ResourceContext",
        "OrgPolicyOverlay",
        "CreateOrgPolicyViolationsPreviewOperationMetadata",
        "ListOrgPolicyViolationsPreviewsRequest",
        "ListOrgPolicyViolationsPreviewsResponse",
        "GetOrgPolicyViolationsPreviewRequest",
        "CreateOrgPolicyViolationsPreviewRequest",
        "ListOrgPolicyViolationsRequest",
        "ListOrgPolicyViolationsResponse",
    },
)


class PreviewState(proto.Enum):
    r"""The current state of an
    [OrgPolicyViolationsPreview][google.cloud.policysimulator.v1.OrgPolicyViolationsPreview].

    Values:
        PREVIEW_STATE_UNSPECIFIED (0):
            The state is unspecified.
        PREVIEW_PENDING (1):
            The
            [OrgPolicyViolationsPreview][google.cloud.policysimulator.v1.OrgPolicyViolationsPreview]
            has not been created yet.
        PREVIEW_RUNNING (2):
            The
            [OrgPolicyViolationsPreview][google.cloud.policysimulator.v1.OrgPolicyViolationsPreview]
            is currently being created.
        PREVIEW_SUCCEEDED (3):
            The
            [OrgPolicyViolationsPreview][google.cloud.policysimulator.v1.OrgPolicyViolationsPreview]
            creation finished successfully.
        PREVIEW_FAILED (4):
            The
            [OrgPolicyViolationsPreview][google.cloud.policysimulator.v1.OrgPolicyViolationsPreview]
            creation failed with an error.
    """

    PREVIEW_STATE_UNSPECIFIED = 0
    PREVIEW_PENDING = 1
    PREVIEW_RUNNING = 2
    PREVIEW_SUCCEEDED = 3
    PREVIEW_FAILED = 4


class OrgPolicyViolationsPreview(proto.Message):
    r"""OrgPolicyViolationsPreview is a resource providing a preview of the
    violations that will exist if an OrgPolicy change is made.

    The list of violations are modeled as child resources and retrieved
    via a [ListOrgPolicyViolations][] API call. There are potentially
    more [OrgPolicyViolations][] than could fit in an embedded field.
    Thus, the use of a child resource instead of a field.

    Attributes:
        name (str):
            Output only. The resource name of the
            ``OrgPolicyViolationsPreview``. It has the following format:

            ``organizations/{organization}/locations/{location}/orgPolicyViolationsPreviews/{orgPolicyViolationsPreview}``

            Example:
            ``organizations/my-example-org/locations/global/orgPolicyViolationsPreviews/506a5f7f``
        state (google.cloud.policysimulator_v1.types.PreviewState):
            Output only. The state of the
            ``OrgPolicyViolationsPreview``.
        overlay (google.cloud.policysimulator_v1.types.OrgPolicyOverlay):
            Required. The proposed changes we are
            previewing violations for.
        violations_count (int):
            Output only. The number of [OrgPolicyViolations][] in this
            ``OrgPolicyViolationsPreview``. This count may differ from
            ``resource_summary.noncompliant_count`` because each
            [OrgPolicyViolation][google.cloud.policysimulator.v1.OrgPolicyViolation]
            is specific to a resource **and** constraint. If there are
            multiple constraints being evaluated (i.e. multiple policies
            in the overlay), a single resource may violate multiple
            constraints.
        resource_counts (google.cloud.policysimulator_v1.types.OrgPolicyViolationsPreview.ResourceCounts):
            Output only. A summary of the state of all
            resources scanned for compliance with the
            changed OrgPolicy.
        custom_constraints (MutableSequence[str]):
            Output only. The names of the constraints against which all
            ``OrgPolicyViolations`` were evaluated.

            If ``OrgPolicyOverlay`` only contains ``PolicyOverlay`` then
            it contains the name of the configured custom constraint,
            applicable to the specified policies. Otherwise it contains
            the name of the constraint specified in
            ``CustomConstraintOverlay``.

            Format:
            ``organizations/{organization_id}/customConstraints/{custom_constraint_id}``

            Example:
            ``organizations/123/customConstraints/custom.createOnlyE2TypeVms``
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when this ``OrgPolicyViolationsPreview``
            was created.
    """

    class ResourceCounts(proto.Message):
        r"""A summary of the state of all resources scanned for
        compliance with the changed OrgPolicy.

        Attributes:
            scanned (int):
                Output only. Number of resources checked for
                compliance.
                Must equal:  unenforced + noncompliant +
                compliant + error
            noncompliant (int):
                Output only. Number of scanned resources with
                at least one violation.
            compliant (int):
                Output only. Number of scanned resources with
                zero violations.
            unenforced (int):
                Output only. Number of resources where the constraint was
                not enforced, i.e. the Policy set ``enforced: false`` for
                that resource.
            errors (int):
                Output only. Number of resources that
                returned an error when scanned.
        """

        scanned: int = proto.Field(
            proto.INT32,
            number=1,
        )
        noncompliant: int = proto.Field(
            proto.INT32,
            number=2,
        )
        compliant: int = proto.Field(
            proto.INT32,
            number=3,
        )
        unenforced: int = proto.Field(
            proto.INT32,
            number=4,
        )
        errors: int = proto.Field(
            proto.INT32,
            number=5,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    state: "PreviewState" = proto.Field(
        proto.ENUM,
        number=2,
        enum="PreviewState",
    )
    overlay: "OrgPolicyOverlay" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="OrgPolicyOverlay",
    )
    violations_count: int = proto.Field(
        proto.INT32,
        number=4,
    )
    resource_counts: ResourceCounts = proto.Field(
        proto.MESSAGE,
        number=5,
        message=ResourceCounts,
    )
    custom_constraints: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )


class OrgPolicyViolation(proto.Message):
    r"""OrgPolicyViolation is a resource representing a single
    resource violating a single OrgPolicy constraint.

    Attributes:
        name (str):
            The name of the ``OrgPolicyViolation``. Example:
            organizations/my-example-org/locations/global/orgPolicyViolationsPreviews/506a5f7f/orgPolicyViolations/38ce\`
        resource (google.cloud.policysimulator_v1.types.ResourceContext):
            The resource violating the constraint.
        custom_constraint (google.cloud.orgpolicy_v2.types.CustomConstraint):
            The custom constraint being violated.
        error (google.rpc.status_pb2.Status):
            Any error encountered during the evaluation.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    resource: "ResourceContext" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ResourceContext",
    )
    custom_constraint: constraint.CustomConstraint = proto.Field(
        proto.MESSAGE,
        number=3,
        message=constraint.CustomConstraint,
    )
    error: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=4,
        message=status_pb2.Status,
    )


class ResourceContext(proto.Message):
    r"""ResourceContext provides the context we know about a
    resource. It is similar in concept to
    google.cloud.asset.v1.Resource, but focuses on the information
    specifically used by Simulator.

    Attributes:
        resource (str):
            The full name of the resource. Example:
            ``//compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1``

            See `Resource
            names <https://cloud.google.com/apis/design/resource_names#full_resource_name>`__
            for more information.
        asset_type (str):
            The asset type of the resource as defined by CAIS.

            Example: ``compute.googleapis.com/Firewall``

            See `Supported asset
            types <https://cloud.google.com/asset-inventory/docs/supported-asset-types>`__
            for more information.
        ancestors (MutableSequence[str]):
            The ancestry path of the resource in Google Cloud `resource
            hierarchy <https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy>`__,
            represented as a list of relative resource names. An
            ancestry path starts with the closest ancestor in the
            hierarchy and ends at root. If the resource is a project,
            folder, or organization, the ancestry path starts from the
            resource itself.

            Example:
            ``["projects/123456789", "folders/5432", "organizations/1234"]``
    """

    resource: str = proto.Field(
        proto.STRING,
        number=1,
    )
    asset_type: str = proto.Field(
        proto.STRING,
        number=2,
    )
    ancestors: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class OrgPolicyOverlay(proto.Message):
    r"""The proposed changes to OrgPolicy.

    Attributes:
        policies (MutableSequence[google.cloud.policysimulator_v1.types.OrgPolicyOverlay.PolicyOverlay]):
            Optional. The OrgPolicy changes to preview
            violations for.
            Any existing OrgPolicies with the same name will
            be overridden in the simulation. That is,
            violations will be determined as if all policies
            in the overlay were created or updated.
        custom_constraints (MutableSequence[google.cloud.policysimulator_v1.types.OrgPolicyOverlay.CustomConstraintOverlay]):
            Optional. The OrgPolicy CustomConstraint changes to preview
            violations for.

            Any existing CustomConstraints with the same name will be
            overridden in the simulation. That is, violations will be
            determined as if all custom constraints in the overlay were
            instantiated.

            Only a single custom_constraint is supported in the overlay
            at a time. For evaluating multiple constraints, multiple
            ``GenerateOrgPolicyViolationsPreview`` requests are made,
            where each request evaluates a single constraint.
    """

    class PolicyOverlay(proto.Message):
        r"""A change to an OrgPolicy.

        Attributes:
            policy_parent (str):
                Optional. The parent of the policy we are
                attaching to. Example: "projects/123456".
            policy (google.cloud.orgpolicy_v2.types.Policy):
                Optional. The new or updated OrgPolicy.
        """

        policy_parent: str = proto.Field(
            proto.STRING,
            number=1,
        )
        policy: gcov_orgpolicy.Policy = proto.Field(
            proto.MESSAGE,
            number=2,
            message=gcov_orgpolicy.Policy,
        )

    class CustomConstraintOverlay(proto.Message):
        r"""A change to an OrgPolicy custom constraint.

        Attributes:
            custom_constraint_parent (str):
                Optional. Resource the constraint is attached
                to. Example: "organization/987654".
            custom_constraint (google.cloud.orgpolicy_v2.types.CustomConstraint):
                Optional. The new or updated custom
                constraint.
        """

        custom_constraint_parent: str = proto.Field(
            proto.STRING,
            number=1,
        )
        custom_constraint: constraint.CustomConstraint = proto.Field(
            proto.MESSAGE,
            number=2,
            message=constraint.CustomConstraint,
        )

    policies: MutableSequence[PolicyOverlay] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=PolicyOverlay,
    )
    custom_constraints: MutableSequence[CustomConstraintOverlay] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=CustomConstraintOverlay,
    )


class CreateOrgPolicyViolationsPreviewOperationMetadata(proto.Message):
    r"""CreateOrgPolicyViolationsPreviewOperationMetadata is metadata
    about an OrgPolicyViolationsPreview generations operation.

    Attributes:
        request_time (google.protobuf.timestamp_pb2.Timestamp):
            Time when the request was received.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Time when the request started processing,
            i.e., when the state was set to RUNNING.
        state (google.cloud.policysimulator_v1.types.PreviewState):
            Output only. The current state of the
            operation.
        resources_found (int):
            Total number of resources that need scanning. Should equal
            resource_scanned + resources_pending
        resources_scanned (int):
            Number of resources already scanned.
        resources_pending (int):
            Number of resources still to scan.
    """

    request_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    state: "PreviewState" = proto.Field(
        proto.ENUM,
        number=3,
        enum="PreviewState",
    )
    resources_found: int = proto.Field(
        proto.INT32,
        number=4,
    )
    resources_scanned: int = proto.Field(
        proto.INT32,
        number=5,
    )
    resources_pending: int = proto.Field(
        proto.INT32,
        number=6,
    )


class ListOrgPolicyViolationsPreviewsRequest(proto.Message):
    r"""ListOrgPolicyViolationsPreviewsRequest is the request message for
    [OrgPolicyViolationsPreviewService.ListOrgPolicyViolationsPreviews][google.cloud.policysimulator.v1.OrgPolicyViolationsPreviewService.ListOrgPolicyViolationsPreviews].

    Attributes:
        parent (str):
            Required. The parent the violations are scoped to. Format:
            ``organizations/{organization}/locations/{location}``

            Example: ``organizations/my-example-org/locations/global``
        page_size (int):
            Optional. The maximum number of items to
            return. The service may return fewer than this
            value. If unspecified, at most 5 items will be
            returned. The maximum value is 10; values above
            10 will be coerced to 10.
        page_token (str):
            Optional. A page token, received from a
            previous call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters must match
            the call that provided the page token.
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


class ListOrgPolicyViolationsPreviewsResponse(proto.Message):
    r"""ListOrgPolicyViolationsPreviewsResponse is the response message for
    [OrgPolicyViolationsPreviewService.ListOrgPolicyViolationsPreviews][google.cloud.policysimulator.v1.OrgPolicyViolationsPreviewService.ListOrgPolicyViolationsPreviews].

    Attributes:
        org_policy_violations_previews (MutableSequence[google.cloud.policysimulator_v1.types.OrgPolicyViolationsPreview]):
            The list of OrgPolicyViolationsPreview
        next_page_token (str):
            A token that you can use to retrieve the next
            page of results. If this field is omitted, there
            are no subsequent pages.
    """

    @property
    def raw_page(self):
        return self

    org_policy_violations_previews: MutableSequence["OrgPolicyViolationsPreview"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="OrgPolicyViolationsPreview",
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetOrgPolicyViolationsPreviewRequest(proto.Message):
    r"""GetOrgPolicyViolationsPreviewRequest is the request message for
    [OrgPolicyViolationsPreviewService.GetOrgPolicyViolationsPreview][google.cloud.policysimulator.v1.OrgPolicyViolationsPreviewService.GetOrgPolicyViolationsPreview].

    Attributes:
        name (str):
            Required. The name of the
            OrgPolicyViolationsPreview to get.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateOrgPolicyViolationsPreviewRequest(proto.Message):
    r"""CreateOrgPolicyViolationsPreviewRequest is the request message for
    [OrgPolicyViolationsPreviewService.CreateOrgPolicyViolationsPreview][google.cloud.policysimulator.v1.OrgPolicyViolationsPreviewService.CreateOrgPolicyViolationsPreview].

    Attributes:
        parent (str):
            Required. The organization under which this
            [OrgPolicyViolationsPreview][google.cloud.policysimulator.v1.OrgPolicyViolationsPreview]
            will be created.

            Example: ``organizations/my-example-org/locations/global``
        org_policy_violations_preview (google.cloud.policysimulator_v1.types.OrgPolicyViolationsPreview):
            Required. The
            [OrgPolicyViolationsPreview][google.cloud.policysimulator.v1.OrgPolicyViolationsPreview]
            to generate.
        org_policy_violations_preview_id (str):
            Optional. An optional user-specified ID for the
            [OrgPolicyViolationsPreview][google.cloud.policysimulator.v1.OrgPolicyViolationsPreview].
            If not provided, a random ID will be generated.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    org_policy_violations_preview: "OrgPolicyViolationsPreview" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="OrgPolicyViolationsPreview",
    )
    org_policy_violations_preview_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListOrgPolicyViolationsRequest(proto.Message):
    r"""ListOrgPolicyViolationsRequest is the request message for
    [OrgPolicyViolationsPreviewService.ListOrgPolicyViolations][google.cloud.policysimulator.v1.OrgPolicyViolationsPreviewService.ListOrgPolicyViolations].

    Attributes:
        parent (str):
            Required. The OrgPolicyViolationsPreview to
            get OrgPolicyViolations from. Format:

            organizations/{organization}/locations/{location}/orgPolicyViolationsPreviews/{orgPolicyViolationsPreview}
        page_size (int):
            Optional. The maximum number of items to
            return. The service may return fewer than this
            value. If unspecified, at most 1000 items will
            be returned. The maximum value is 1000; values
            above 1000 will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a
            previous call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters must match
            the call that provided the page token.
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


class ListOrgPolicyViolationsResponse(proto.Message):
    r"""ListOrgPolicyViolationsResponse is the response message for
    [OrgPolicyViolationsPreviewService.ListOrgPolicyViolations][google.cloud.policysimulator.v1.OrgPolicyViolationsPreviewService.ListOrgPolicyViolations]

    Attributes:
        org_policy_violations (MutableSequence[google.cloud.policysimulator_v1.types.OrgPolicyViolation]):
            The list of OrgPolicyViolations
        next_page_token (str):
            A token that you can use to retrieve the next
            page of results. If this field is omitted, there
            are no subsequent pages.
    """

    @property
    def raw_page(self):
        return self

    org_policy_violations: MutableSequence["OrgPolicyViolation"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="OrgPolicyViolation",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
