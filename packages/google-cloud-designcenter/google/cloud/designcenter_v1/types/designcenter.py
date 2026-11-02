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

from google.cloud.designcenter_v1.types import deployment_messages

__protobuf__ = proto.module(
    package="google.cloud.designcenter.v1",
    manifest={
        "OperationMetadata",
        "PreviewOperationMetadata",
        "GenerateAssessmentReportOperationMetadata",
        "ApplicationOperationMetadata",
        "ProvisionDeploymentGroupOperationMetadata",
        "DeploymentUnitProgress",
        "DeploymentOperationMetadata",
        "DeploymentAttemptMetadata",
    },
)


class OperationMetadata(proto.Message):
    r"""Represents the metadata of the long-running operation.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        deployment_metadata (google.cloud.designcenter_v1.types.DeploymentOperationMetadata):
            Output only. The application deployment
            metadata this operation is associated with.

            This field is a member of `oneof`_ ``resource_metadata``.
        preview_metadata (google.cloud.designcenter_v1.types.PreviewOperationMetadata):
            Output only. The application preview metadata
            this operation is associated with.

            This field is a member of `oneof`_ ``resource_metadata``.
        application_metadata (google.cloud.designcenter_v1.types.ApplicationOperationMetadata):
            Output only. The application delete metadata
            this operation is associated with.

            This field is a member of `oneof`_ ``resource_metadata``.
        deployment_group_metadata (google.cloud.designcenter_v1.types.ProvisionDeploymentGroupOperationMetadata):
            Output only. The Provision Deployment Group
            Metadata this operation is associated with.

            This field is a member of `oneof`_ ``resource_metadata``.
        generate_assessment_report_metadata (google.cloud.designcenter_v1.types.GenerateAssessmentReportOperationMetadata):
            Output only. The Generate Assessment Report
            Metadata this operation is associated with.

            This field is a member of `oneof`_ ``resource_metadata``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation was
            created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation finished
            running.
        target (str):
            Output only. The server defined resource path
            for the target of the operation.
        verb (str):
            Output only. Name of the verb executed by the
            operation.
        status_message (str):
            Output only. Human readable status of the
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

    deployment_metadata: "DeploymentOperationMetadata" = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="resource_metadata",
        message="DeploymentOperationMetadata",
    )
    preview_metadata: "PreviewOperationMetadata" = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="resource_metadata",
        message="PreviewOperationMetadata",
    )
    application_metadata: "ApplicationOperationMetadata" = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="resource_metadata",
        message="ApplicationOperationMetadata",
    )
    deployment_group_metadata: "ProvisionDeploymentGroupOperationMetadata" = (
        proto.Field(
            proto.MESSAGE,
            number=11,
            oneof="resource_metadata",
            message="ProvisionDeploymentGroupOperationMetadata",
        )
    )
    generate_assessment_report_metadata: "GenerateAssessmentReportOperationMetadata" = (
        proto.Field(
            proto.MESSAGE,
            number=12,
            oneof="resource_metadata",
            message="GenerateAssessmentReportOperationMetadata",
        )
    )
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


class PreviewOperationMetadata(proto.Message):
    r"""Ephemeral metadata depicting the state of the preview
    operation.

    Attributes:
        preview_step (str):
            Output only. The current step of the preview.
            The possible steps a preview may be running as
            returned by the Infrastructure. Manager.
        preview_build (str):
            Output only. Cloud Build instance UUID
            associated with the preview operation.
        preview_logs (str):
            Output only. Location of the preview operation logs in
            ``gs://{bucket}/{object}`` format.
        resources (MutableSequence[google.cloud.designcenter_v1.types.Resource]):
            Details of the [Resources][]s in the deployment.
    """

    preview_step: str = proto.Field(
        proto.STRING,
        number=2,
    )
    preview_build: str = proto.Field(
        proto.STRING,
        number=3,
    )
    preview_logs: str = proto.Field(
        proto.STRING,
        number=4,
    )
    resources: MutableSequence[deployment_messages.Resource] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message=deployment_messages.Resource,
    )


class GenerateAssessmentReportOperationMetadata(proto.Message):
    r"""Ephemeral metadata depicting the state of assessment report
    generation.

    Attributes:
        step (google.cloud.designcenter_v1.types.GenerateAssessmentReportOperationMetadata.AssessmentStep):
            Output only. The current step of the generate
            assessment report operation.
    """

    class AssessmentStep(proto.Enum):
        r"""Steps in generating an assessment report.

        Values:
            ASSESSMENT_STEP_UNSPECIFIED (0):
                Unspecified step.
            FAST_PLAN (1):
                Generating Terraform fast plan.
            ASSESSMENT_REPORT (2):
                Generating BPBD assessment report.
            SUCCEEDED (3):
                Succeeded.
            FAILED (4):
                Failed.
        """

        ASSESSMENT_STEP_UNSPECIFIED = 0
        FAST_PLAN = 1
        ASSESSMENT_REPORT = 2
        SUCCEEDED = 3
        FAILED = 4

    step: AssessmentStep = proto.Field(
        proto.ENUM,
        number=1,
        enum=AssessmentStep,
    )


class ApplicationOperationMetadata(proto.Message):
    r"""Ephemeral metadata depicting the state of the delete
    operation.

    Attributes:
        step (str):
            Output only. The current step of the delete
            operation. Associated with Infrastructure
            Manager and App Hub.
        build (str):
            Output only. Cloud Build instance UUID
            associated with the delete operation.
    """

    step: str = proto.Field(
        proto.STRING,
        number=1,
    )
    build: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ProvisionDeploymentGroupOperationMetadata(proto.Message):
    r"""Represents the Provision Deployment Group operation metadata.

    Attributes:
        deployment_step (google.cloud.designcenter_v1.types.ProvisionDeploymentGroupOperationMetadata.DeploymentStep):
            Output only. Current step of deploying
            composite application
        deployment_unit_progress (MutableSequence[google.cloud.designcenter_v1.types.DeploymentUnitProgress]):
            Output only. List of deployment unit
            deployment progress
    """

    class DeploymentStep(proto.Enum):
        r"""Current Deployment Operation Step

        Values:
            DEPLOYMENT_STEP_UNSPECIFIED (0):
                Unspecified deployment step.
            GENERATING_TERRAFORM_CONTENT (1):
                Generating Terraform content for the
                application.
            DEPLOYING (2):
                Deploying the application.
            SUCCEEDED (3):
                Operation was successful.
            FAILED (4):
                Operation failed.
        """

        DEPLOYMENT_STEP_UNSPECIFIED = 0
        GENERATING_TERRAFORM_CONTENT = 1
        DEPLOYING = 2
        SUCCEEDED = 3
        FAILED = 4

    deployment_step: DeploymentStep = proto.Field(
        proto.ENUM,
        number=1,
        enum=DeploymentStep,
    )
    deployment_unit_progress: MutableSequence["DeploymentUnitProgress"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="DeploymentUnitProgress",
        )
    )


class DeploymentUnitProgress(proto.Message):
    r"""Single deployment unit progress info

    Attributes:
        unit_id (str):
            Output only. Deployment unit ID
        deployment (str):
            Output only. Deployment resource of deploying
            unit ID
        deployment_unit_step (str):
            Output only. Current deployment unit step
        deployment_build (str):
            Output only. Deployment build uuid
        deployment_step (str):
            Output only. Current deployment step
    """

    unit_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    deployment: str = proto.Field(
        proto.STRING,
        number=2,
    )
    deployment_unit_step: str = proto.Field(
        proto.STRING,
        number=3,
    )
    deployment_build: str = proto.Field(
        proto.STRING,
        number=4,
    )
    deployment_step: str = proto.Field(
        proto.STRING,
        number=5,
    )


class DeploymentOperationMetadata(proto.Message):
    r"""Ephemeral metadata depicting the state of the deployment
    operation.

    Attributes:
        deployment (str):
            Output only. The name of the deployment
            associated with the application.
        deployment_step (str):
            Output only. The current step of the
            deployment. This will mimic the DeploymentStep
            enum in the deployment proto.
        deployment_build (str):
            Output only. Cloud Build instance UUID
            associated with this deployment.
        deployment_logs (str):
            Output only. Location of the deployment operation logs in
            ``gs://{bucket}/{object}`` format.
        resources (MutableSequence[google.cloud.designcenter_v1.types.Resource]):
            Details of the [Resources][]s in the deployment.
        previous_attempt (google.cloud.designcenter_v1.types.DeploymentAttemptMetadata):
            Previous deployment attempt metadata.
    """

    deployment: str = proto.Field(
        proto.STRING,
        number=1,
    )
    deployment_step: str = proto.Field(
        proto.STRING,
        number=5,
    )
    deployment_build: str = proto.Field(
        proto.STRING,
        number=6,
    )
    deployment_logs: str = proto.Field(
        proto.STRING,
        number=7,
    )
    resources: MutableSequence[deployment_messages.Resource] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message=deployment_messages.Resource,
    )
    previous_attempt: "DeploymentAttemptMetadata" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="DeploymentAttemptMetadata",
    )


class DeploymentAttemptMetadata(proto.Message):
    r"""DeploymentAttemptMetadata represents a previous deployment
    attempt for an operation that failed due to a retryable error.

    Attributes:
        attempt (int):
            The sequential number of the attempt
            (starting from 1).
        error_detail (str):
            Human readable string that summarizes the
            deployment error issue.
        build (str):
            The build or execution ID associated with
            this specific attempt. This can be used to link
            back to logs or trace information.
    """

    attempt: int = proto.Field(
        proto.INT32,
        number=1,
    )
    error_detail: str = proto.Field(
        proto.STRING,
        number=2,
    )
    build: str = proto.Field(
        proto.STRING,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
