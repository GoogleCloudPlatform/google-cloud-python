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
import proto  # type: ignore
from google.cloud.config_v1.types import config

from google.cloud.designcenter_v1.types import assessment, best_practices

__protobuf__ = proto.module(
    package="google.cloud.designcenter.v1",
    manifest={
        "FetchApplicationAssessmentReportRequest",
        "FetchApplicationAssessmentReportResponse",
        "GenerateApplicationAssessmentReportRequest",
        "GenerateApplicationAssessmentReportResponse",
        "GenerateApplicationTemplateAssessmentReportRequest",
        "GenerateApplicationTemplateAssessmentReportResponse",
        "GenerateAssessmentReportRequest",
        "GenerateAssessmentReportResponse",
        "GenerateTerraformPlanAssessmentReportRequest",
        "GenerateTerraformPlanAssessmentReportResponse",
        "FetchFrameworksRequest",
        "FetchFrameworksResponse",
        "GetPolicyRequest",
        "ListPoliciesRequest",
        "ListPoliciesResponse",
        "CreatePolicyRequest",
        "UpdatePolicyRequest",
        "DeletePolicyRequest",
    },
)


class FetchApplicationAssessmentReportRequest(proto.Message):
    r"""Message for fetching an application assessment report.

    Attributes:
        name (str):
            Required. The application name in the following format:
            ``projects/$project/locations/$location/spaces/$space/applications/$application``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class FetchApplicationAssessmentReportResponse(proto.Message):
    r"""Message for response of fetching an application assessment
    report.

    Attributes:
        assessment_report (google.cloud.designcenter_v1.types.AssessmentReport):
            Assessment report for the application.
    """

    assessment_report: best_practices.AssessmentReport = proto.Field(
        proto.MESSAGE,
        number=1,
        message=best_practices.AssessmentReport,
    )


class GenerateApplicationAssessmentReportRequest(proto.Message):
    r"""Message for generating an application assessment report.

    Attributes:
        name (str):
            Required. The application name in the following format:
            ``projects/$project/locations/$location/spaces/$space/applications/$application``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GenerateApplicationAssessmentReportResponse(proto.Message):
    r"""Response for GenerateApplicationAssessmentReport.

    Attributes:
        assessment_report (google.cloud.designcenter_v1.types.AssessmentReport):
            Output only. Best practices by Design
            Assessment report
    """

    assessment_report: best_practices.AssessmentReport = proto.Field(
        proto.MESSAGE,
        number=1,
        message=best_practices.AssessmentReport,
    )


class GenerateApplicationTemplateAssessmentReportRequest(proto.Message):
    r"""Message for generate assessment report application template.

    Attributes:
        name (str):
            Required. The application template name in the following
            format:
            ``projects/$project/locations/$location/spaces/$space/applicationTemplates/$applicationTemplate``
        service_account (str):
            Optional. Deprecated: This field is no longer used since we
            moved to fast plan assessment.

            - This service account will be used to execute the preview
              process.
            - The caller must have the 'iam.serviceAccounts.actAs'
              permission on this service account. Format:
              projects/{PROJECT}/serviceAccounts/{EMAIL_ADDRESS}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    service_account: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GenerateApplicationTemplateAssessmentReportResponse(proto.Message):
    r"""Response for GenerateAssessmentReport for application
    template.

    Attributes:
        preview (google.cloud.config_v1.types.Preview):
            Deprecated: This field is no longer used
            since we moved to fast plan assessment.
            Infrastructure Manager preview.
        assessment_report (google.cloud.designcenter_v1.types.AssessmentReport):
            Best practices by Design Assessment report
    """

    preview: config.Preview = proto.Field(
        proto.MESSAGE,
        number=1,
        message=config.Preview,
    )
    assessment_report: best_practices.AssessmentReport = proto.Field(
        proto.MESSAGE,
        number=2,
        message=best_practices.AssessmentReport,
    )


class GenerateAssessmentReportRequest(proto.Message):
    r"""Deprecated: Use GenerateTerraformPlanAssessmentReportRequest
    instead.
    Message for the request to generate a best practice report for a
    given Terraform plan.

    Attributes:
        terraform_plan (bytes):
            Required. Terraform plan bytes.
        additional_frameworks (MutableSequence[str]):
            Optional. Additional Frameworks to run
            assessment against. If empty, run against
            default frameworks. Frameworks refers to the
            policies.
        space_name (str):
            Required. The name of the space at which Generate Assessment
            Report is called. Format:
            ``projects/$project/locations/$location/spaces/$space``
    """

    terraform_plan: bytes = proto.Field(
        proto.BYTES,
        number=1,
    )
    additional_frameworks: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    space_name: str = proto.Field(
        proto.STRING,
        number=3,
    )


class GenerateAssessmentReportResponse(proto.Message):
    r"""Deprecated: Use GenerateTerraformPlanAssessmentReportResponse
    instead.
    Response for GenerateAssessmentReport.

    Attributes:
        assessment_report (google.cloud.designcenter_v1.types.AssessmentReport):
            Aggregated assessment report from all
            domains.
    """

    assessment_report: best_practices.AssessmentReport = proto.Field(
        proto.MESSAGE,
        number=1,
        message=best_practices.AssessmentReport,
    )


class GenerateTerraformPlanAssessmentReportRequest(proto.Message):
    r"""Message for the request to generate a best practice report
    for a given Terraform plan at the collection level.

    Attributes:
        name (str):
            Required. The parent resource in which to
            generate the assessment report. Format:
            projects/$project/locations/$location/spaces/$space
        terraform_plan (bytes):
            Required. The raw JSON representation of the
            generated Terraform plan, provided as bytes.
        additional_frameworks (MutableSequence[str]):
            Optional. Additional Frameworks to run
            assessment against. If empty, run against
            default frameworks. Frameworks refers to the
            policies.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    terraform_plan: bytes = proto.Field(
        proto.BYTES,
        number=2,
    )
    additional_frameworks: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GenerateTerraformPlanAssessmentReportResponse(proto.Message):
    r"""Response for GenerateTerraformPlanAssessmentReport.

    Attributes:
        assessment_report (google.cloud.designcenter_v1.types.AssessmentReport):
            Aggregated assessment report from all
            domains.
    """

    assessment_report: best_practices.AssessmentReport = proto.Field(
        proto.MESSAGE,
        number=1,
        message=best_practices.AssessmentReport,
    )


class FetchFrameworksRequest(proto.Message):
    r"""Request for FetchFrameworks rpc

    Attributes:
        parent (str):
            Required. The parent resource name.
            Format: projects/{project}/locations/{location}
        projects (MutableSequence[str]):
            Optional. Projects to fetch frameworks for.
            Format: projects/{project}
        page_size (int):
            Optional. The maximum number of results to
            return from this request. Non-positive values
            are ignored. The presence of nextPageToken in
            the response indicates that more results might
            be available.
        page_token (str):
            Optional. If present, then retrieve the next
            batch of results from the preceding call to this
            method. pageToken must be the value of
            nextPageToken from the previous response. The
            values of other method parameters should be
            identical to those in the previous call.
        filter (str):
            Optional. Filter for frameworks list.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    projects: MutableSequence[str] = proto.RepeatedField(
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
    filter: str = proto.Field(
        proto.STRING,
        number=5,
    )


class FetchFrameworksResponse(proto.Message):
    r"""Response for FetchFrameworks rpc

    Attributes:
        frameworks (MutableSequence[google.cloud.designcenter_v1.types.Framework]):
            The list of frameworks.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    frameworks: MutableSequence[assessment.Framework] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=assessment.Framework,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetPolicyRequest(proto.Message):
    r"""Message for getting a policy.

    Attributes:
        name (str):
            Required. The policy name in the following format:
            ``projects/$project/locations/$location/spaces/$space/applicationTemplates/$applicationTemplate/policies/$policy``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListPoliciesRequest(proto.Message):
    r"""Message for requesting a list of policies.

    Attributes:
        parent (str):
            Required. The parent application template from which
            policies are listed in the following format:
            ``projects/$project/locations/$location/spaces/$space/applicationTemplates/$applicationTemplate``
        page_size (int):
            Optional. The maximum number of results to
            return from this request. Non-positive values
            are ignored. The presence of nextPageToken in
            the response indicates that more results might
            be available.
        page_token (str):
            Optional. If present, retrieve the next batch
            of results from the preceding call to this
            method. pageToken must be the value of
            nextPageToken from the previous response. The
            values of other method parameters should be
            identical to those in the previous call.
        filter (str):
            Optional. A filter that chooses which
            policies to return.
        order_by (str):
            Optional. How the results should be sorted.
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


class ListPoliciesResponse(proto.Message):
    r"""Message for response to listing policies.

    Attributes:
        policies (MutableSequence[google.cloud.designcenter_v1.types.Policy]):
            A list of policies.
        next_page_token (str):
            If there might be more results than those
            appearing in this response, then nextPageToken
            is included. To get the next set of results,
            call this method again using the value of
            nextPageToken as pageToken.
    """

    @property
    def raw_page(self):
        return self

    policies: MutableSequence[best_practices.Policy] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=best_practices.Policy,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreatePolicyRequest(proto.Message):
    r"""Message for creating a policy.

    Attributes:
        parent (str):
            Required. The parent resource in which to create the policy
            in the following format:
            ``projects/$project/locations/$location/spaces/$space/applicationTemplates/$applicationTemplate``
        policy_id (str):
            Required. The ID of the policy to create.
        policy (google.cloud.designcenter_v1.types.Policy):
            Required. The policy to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    policy_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    policy: best_practices.Policy = proto.Field(
        proto.MESSAGE,
        number=3,
        message=best_practices.Policy,
    )


class UpdatePolicyRequest(proto.Message):
    r"""Message for updating a policy.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The fields to overwrite in the policy update. The
            fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. If you don't provide a mask, all
            fields are overwritten.
        policy (google.cloud.designcenter_v1.types.Policy):
            Required. The policy to update.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    policy: best_practices.Policy = proto.Field(
        proto.MESSAGE,
        number=2,
        message=best_practices.Policy,
    )


class DeletePolicyRequest(proto.Message):
    r"""Message for deleting a policy.

    Attributes:
        name (str):
            Required. The policy name in the following format:
            ``projects/$project/locations/$location/spaces/$space/applicationTemplates/$applicationTemplate/policies/$policy``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
