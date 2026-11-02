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

from google.cloud.retail_v2alpha.types import common
from google.cloud.retail_v2alpha.types import project as gcr_project

__protobuf__ = proto.module(
    package="google.cloud.retail.v2alpha",
    manifest={
        "GetProjectRequest",
        "AcceptTermsRequest",
        "EnrollSolutionRequest",
        "EnrollSolutionResponse",
        "EnrollSolutionMetadata",
        "ListEnrolledSolutionsRequest",
        "ListEnrolledSolutionsResponse",
        "GetLoggingConfigRequest",
        "UpdateLoggingConfigRequest",
        "GetAlertConfigRequest",
        "UpdateAlertConfigRequest",
    },
)


class GetProjectRequest(proto.Message):
    r"""Request for GetProject method.

    Attributes:
        name (str):
            Required. Full resource name of the project. Format:
            ``projects/{project_number_or_id}/retailProject``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class AcceptTermsRequest(proto.Message):
    r"""Request for AcceptTerms method.

    Attributes:
        project (str):
            Required. Full resource name of the project. Format:
            ``projects/{project_number_or_id}/retailProject``
    """

    project: str = proto.Field(
        proto.STRING,
        number=1,
    )


class EnrollSolutionRequest(proto.Message):
    r"""Request for EnrollSolution method.

    Attributes:
        project (str):
            Required. Full resource name of parent. Format:
            ``projects/{project_number_or_id}``
        solution (google.cloud.retail_v2alpha.types.SolutionType):
            Required. Solution to enroll.
    """

    project: str = proto.Field(
        proto.STRING,
        number=1,
    )
    solution: common.SolutionType = proto.Field(
        proto.ENUM,
        number=2,
        enum=common.SolutionType,
    )


class EnrollSolutionResponse(proto.Message):
    r"""Response for EnrollSolution method.

    Attributes:
        enrolled_solution (google.cloud.retail_v2alpha.types.SolutionType):
            Retail API solution that the project has
            enrolled.
    """

    enrolled_solution: common.SolutionType = proto.Field(
        proto.ENUM,
        number=1,
        enum=common.SolutionType,
    )


class EnrollSolutionMetadata(proto.Message):
    r"""Metadata related to the EnrollSolution method.
    This will be returned by the
    google.longrunning.Operation.metadata field.

    """


class ListEnrolledSolutionsRequest(proto.Message):
    r"""Request for ListEnrolledSolutions method.

    Attributes:
        parent (str):
            Required. Full resource name of parent. Format:
            ``projects/{project_number_or_id}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListEnrolledSolutionsResponse(proto.Message):
    r"""Response for ListEnrolledSolutions method.

    Attributes:
        enrolled_solutions (MutableSequence[google.cloud.retail_v2alpha.types.SolutionType]):
            Retail API solutions that the project has
            enrolled.
    """

    enrolled_solutions: MutableSequence[common.SolutionType] = proto.RepeatedField(
        proto.ENUM,
        number=1,
        enum=common.SolutionType,
    )


class GetLoggingConfigRequest(proto.Message):
    r"""Request for
    [ProjectService.GetLoggingConfig][google.cloud.retail.v2alpha.ProjectService.GetLoggingConfig]
    method.

    Attributes:
        name (str):
            Required. Full LoggingConfig resource name. Format:
            projects/{project_number}/loggingConfig
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateLoggingConfigRequest(proto.Message):
    r"""Request for
    [ProjectService.UpdateLoggingConfig][google.cloud.retail.v2alpha.ProjectService.UpdateLoggingConfig]
    method.

    Attributes:
        logging_config (google.cloud.retail_v2alpha.types.LoggingConfig):
            Required. The
            [LoggingConfig][google.cloud.retail.v2alpha.LoggingConfig]
            to update.

            If the caller does not have permission to update the
            [LoggingConfig][google.cloud.retail.v2alpha.LoggingConfig],
            then a PERMISSION_DENIED error is returned.

            If the
            [LoggingConfig][google.cloud.retail.v2alpha.LoggingConfig]
            to update does not exist, a NOT_FOUND error is returned.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Indicates which fields in the provided
            [LoggingConfig][google.cloud.retail.v2alpha.LoggingConfig]
            to update. The following are the only supported fields:

            - [LoggingConfig.default_log_generation_rule][google.cloud.retail.v2alpha.LoggingConfig.default_log_generation_rule]
            - [LoggingConfig.service_log_generation_rules][google.cloud.retail.v2alpha.LoggingConfig.service_log_generation_rules]

            If not set, all supported fields are updated.
    """

    logging_config: gcr_project.LoggingConfig = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcr_project.LoggingConfig,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class GetAlertConfigRequest(proto.Message):
    r"""Request for
    [ProjectService.GetAlertConfig][google.cloud.retail.v2alpha.ProjectService.GetAlertConfig]
    method.

    Attributes:
        name (str):
            Required. Full AlertConfig resource name. Format:
            projects/{project_number}/alertConfig
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateAlertConfigRequest(proto.Message):
    r"""Request for
    [ProjectService.UpdateAlertConfig][google.cloud.retail.v2alpha.ProjectService.UpdateAlertConfig]
    method.

    Attributes:
        alert_config (google.cloud.retail_v2alpha.types.AlertConfig):
            Required. The
            [AlertConfig][google.cloud.retail.v2alpha.AlertConfig] to
            update.

            If the caller does not have permission to update the
            [AlertConfig][google.cloud.retail.v2alpha.AlertConfig], then
            a PERMISSION_DENIED error is returned.

            If the
            [AlertConfig][google.cloud.retail.v2alpha.AlertConfig] to
            update does not exist, a NOT_FOUND error is returned.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Indicates which fields in the provided
            [AlertConfig][google.cloud.retail.v2alpha.AlertConfig] to
            update. If not set, all supported fields are updated.
    """

    alert_config: gcr_project.AlertConfig = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcr_project.AlertConfig,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
