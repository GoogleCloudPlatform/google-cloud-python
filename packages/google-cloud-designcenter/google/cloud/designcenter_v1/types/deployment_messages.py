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

from google.cloud.designcenter_v1.types import (
    best_practices,
    deployment_resources,
    enums,
    export,
    iac,
    ingestion,
    parameters,
)
from google.cloud.designcenter_v1.types import deployment as gcd_deployment

__protobuf__ = proto.module(
    package="google.cloud.designcenter.v1",
    manifest={
        "CreateApplicationRequest",
        "GetApplicationRequest",
        "ListApplicationsRequest",
        "ListApplicationsResponse",
        "UpdateApplicationRequest",
        "DeleteApplicationRequest",
        "DeployApplicationRequest",
        "DeployApplicationResponse",
        "Resource",
        "GenerateApplicationIaCRequest",
        "GenerateApplicationIaCResponse",
        "ExportApplicationIaCRequest",
        "ExportApplicationIaCResponse",
        "ImportApplicationIaCRequest",
        "ImportApplicationIaCResponse",
        "PreviewApplicationRequest",
        "PreviewApplicationResponse",
        "RecommendIAMRolesRequest",
        "RecommendIAMRolesResponse",
        "ConfigureAndDeployTemplateRequest",
        "ConfigureAndDeployTemplateResponse",
    },
)


class CreateApplicationRequest(proto.Message):
    r"""Message for creating an application.

    Attributes:
        parent (str):
            Required. The parent resource in which to create the
            application. Format:
            ``projects/$project/locations/$location/spaces/$space``
        application_id (str):
            Required. The ID of the application to
            create.
        application (google.cloud.designcenter_v1.types.Application):
            Required. The application to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    application_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    application: deployment_resources.Application = proto.Field(
        proto.MESSAGE,
        number=3,
        message=deployment_resources.Application,
    )


class GetApplicationRequest(proto.Message):
    r"""Message for getting an application.

    Attributes:
        name (str):
            Required. The application name. Format:
            ``projects/$project/locations/$location/spaces/$space/applications/$application``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListApplicationsRequest(proto.Message):
    r"""Message for requesting a list of applications.

    Attributes:
        parent (str):
            Required. The parent resource from which to
            request a list of applications.
        page_size (int):
            Optional. The maximum number of results to
            return from this request. Non-positive
             values are ignored. The presence of
            nextPageToken in the response  indicates that
            more results might be available.
        page_token (str):
            Optional. If present, then retrieve the next
            batch of results from the preceding call to this
            method. pageToken must be the value of
            nextPageToken from the previous response. The
            values of other method parameters should be
            identical to those in the previous call.
        filter (str):
            Optional. A filter that chooses which
            applications to return.
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


class ListApplicationsResponse(proto.Message):
    r"""Message for response to listing applications.

    Attributes:
        applications (MutableSequence[google.cloud.designcenter_v1.types.Application]):
            The list of applications.
        next_page_token (str):
            If there might be more results than those
            appearing in this response, then nextPageToken
            is included. To get the next set of results,
            call this method again using the value of
            nextPageToken as pageToken.
        unreachable (MutableSequence[str]):
            Unordered list. Locations that could not be
            reached.
    """

    @property
    def raw_page(self):
        return self

    applications: MutableSequence[deployment_resources.Application] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=deployment_resources.Application,
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


class UpdateApplicationRequest(proto.Message):
    r"""Message for updating an application.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The fields to overwrite in the
            application update. If you don't provide a mask,
            all fields are overwritten.
        application (google.cloud.designcenter_v1.types.Application):
            Required. The application to update.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    application: deployment_resources.Application = proto.Field(
        proto.MESSAGE,
        number=2,
        message=deployment_resources.Application,
    )


class DeleteApplicationRequest(proto.Message):
    r"""Message for deleting an application.

    Attributes:
        name (str):
            Required. The application name. Format:
            ``projects/$project/locations/$location/spaces/$space/applications/$application``
        force (bool):
            Optional. If set to true, the application's
            children are also deleted. If false, the
            application is only deleted if it has no
            children.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class DeployApplicationRequest(proto.Message):
    r"""Message for deploying an application.

    Attributes:
        name (str):
            Required. The application name. Format:
            ``projects/$project/locations/$location/spaces/$space/applications/$application``
        replace (bool):
            Optional. Flag to update the existing deployment. If not set
            or false, deploy will fail if application ``state`` is in
            the ``DEPLOYED`` state.
        worker_pool (str):
            Optional. The user-specified Worker Pool
            resource in which the Cloud Build job will
            execute. Format:

            projects/{project}/locations/{location}/workerPools/{workerPoolId}
            If this flag is omitted, the worker pool already
            defined on the application will be used. If no
            worker pool is defined on the application, the
            default Cloud Build worker pool is used. The
            worker pool must exist in the same region as the
            application.
        service_account (str):
            Optional. The email address of the service account to use
            for this deployment.

            - If provided, this service account will be used to execute
              the deployment process, taking precedence over any
              service_account specified on the Application resource.
            - The caller must have the 'iam.serviceAccounts.actAs'
              permission on this service account.
            - If this field is omitted, the system will use the
              'service_account' defined within the Application resource.
            - We recommend that you provide a service account here or on
              the Application resource. If you don't provide a service
              account, the deployment will fail. Format:
              projects/{PROJECT}/serviceAccounts/{EMAIL_ADDRESS}
        validate_only (bool):
            Optional. If set to true, the request is
            validated, but no actual deployment will occur.
            See https://google.aip.dev/163 for more details.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    replace: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    worker_pool: str = proto.Field(
        proto.STRING,
        number=4,
    )
    service_account: str = proto.Field(
        proto.STRING,
        number=5,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=6,
    )


class DeployApplicationResponse(proto.Message):
    r"""Response for DeployApplication.

    Attributes:
        deployment (google.cloud.config_v1.types.Deployment):
            Infrastructure Manager deployment.
        build_id (str):
            Cloud Build deployment id.
        deployment_group (google.cloud.config_v1.types.DeploymentGroup):
            Infrastructure Manager deployment group.
            Used for composite application deployment
            response.
    """

    deployment: config.Deployment = proto.Field(
        proto.MESSAGE,
        number=1,
        message=config.Deployment,
    )
    build_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    deployment_group: config.DeploymentGroup = proto.Field(
        proto.MESSAGE,
        number=3,
        message=config.DeploymentGroup,
    )


class Resource(proto.Message):
    r"""Status of the [Resources][]s in the deployment.

    Attributes:
        name (str):
            Output only. Identifier. The name of the
            resource.
        type_ (str):
            Output only. The type of the resource.
        state (google.cloud.designcenter_v1.types.Resource.State):
            Output only. Current state of the resource.
    """

    class State(proto.Enum):
        r"""Possible states of a resource.

        Values:
            STATE_UNSPECIFIED (0):
                The default value. This value is used if the
                state is omitted.
            PLANNED (1):
                Resource has been planned for reconcile.
            IN_PROGRESS (2):
                Resource is actively reconciling into the
                intended state.
            RECONCILED (3):
                Resource has reconciled to intended state.
            FAILED (4):
                Resource failed to reconcile.
            DRIFTED (5):
                Drift is detected in the resourece state.
            INTENDED (6):
                Resource is intended state.
        """

        STATE_UNSPECIFIED = 0
        PLANNED = 1
        IN_PROGRESS = 2
        RECONCILED = 3
        FAILED = 4
        DRIFTED = 5
        INTENDED = 6

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_: str = proto.Field(
        proto.STRING,
        number=2,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=3,
        enum=State,
    )


class GenerateApplicationIaCRequest(proto.Message):
    r"""Request message for GenerateApplicationIaC method.

    Attributes:
        name (str):
            Required. The name of the application.
        iac_format (google.cloud.designcenter_v1.types.IACFormat):
            Optional. The IaC format to generate.
        gcs_uri (str):
            Optional. DEPRECATED: Use the 'artifact_location' field
            instead. The Cloud Storage URI to write the generated IaC
            to.
        artifact_location (google.cloud.designcenter_v1.types.ArtifactLocation):
            Optional. Specifies the destination for the
            generated IaC, which can be Cloud Storage or a
            Developer Connect repository.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    iac_format: enums.IACFormat = proto.Field(
        proto.ENUM,
        number=2,
        enum=enums.IACFormat,
    )
    gcs_uri: str = proto.Field(
        proto.STRING,
        number=3,
    )
    artifact_location: export.ArtifactLocation = proto.Field(
        proto.MESSAGE,
        number=4,
        message=export.ArtifactLocation,
    )


class GenerateApplicationIaCResponse(proto.Message):
    r"""Response message for GenerateApplicationIaC method.

    Attributes:
        gcs_uri (str):
            DEPRECATED: Use the 'artifact_location' field instead. The
            Cloud Storage URI of the generated IaC.
        artifact_location (google.cloud.designcenter_v1.types.ArtifactLocation):
            The destination where the generated IaC was
            written.
        root_modules_metadata (google.cloud.designcenter_v1.types.RootModulesMetadata):
            Root modules metadata of the application.
    """

    gcs_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    artifact_location: export.ArtifactLocation = proto.Field(
        proto.MESSAGE,
        number=2,
        message=export.ArtifactLocation,
    )
    root_modules_metadata: iac.RootModulesMetadata = proto.Field(
        proto.MESSAGE,
        number=3,
        message=iac.RootModulesMetadata,
    )


class ExportApplicationIaCRequest(proto.Message):
    r"""Request message for ExportApplicationIaC method.

    Attributes:
        name (str):
            Required. The name of the application.
        iac_format (google.cloud.designcenter_v1.types.IACFormat):
            Optional. The IaC format to generate.
        artifact_location (google.cloud.designcenter_v1.types.ArtifactLocation):
            Optional. Specifies the destination for the
            generated IaC, which can be Cloud Storage or a
            Developer Connect repository.
        export_iac_config (google.cloud.designcenter_v1.types.ExportIaCConfig):
            Optional. Configuration for exporting IaC.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    iac_format: enums.IACFormat = proto.Field(
        proto.ENUM,
        number=2,
        enum=enums.IACFormat,
    )
    artifact_location: export.ArtifactLocation = proto.Field(
        proto.MESSAGE,
        number=3,
        message=export.ArtifactLocation,
    )
    export_iac_config: export.ExportIaCConfig = proto.Field(
        proto.MESSAGE,
        number=4,
        message=export.ExportIaCConfig,
    )


class ExportApplicationIaCResponse(proto.Message):
    r"""Response message for ExportApplicationIaC method.

    Attributes:
        artifact_location (google.cloud.designcenter_v1.types.ArtifactLocation):
            The destination where the generated IaC was
            written.
        root_modules_metadata (google.cloud.designcenter_v1.types.RootModulesMetadata):
            Root modules metadata of the application.
    """

    artifact_location: export.ArtifactLocation = proto.Field(
        proto.MESSAGE,
        number=1,
        message=export.ArtifactLocation,
    )
    root_modules_metadata: iac.RootModulesMetadata = proto.Field(
        proto.MESSAGE,
        number=2,
        message=iac.RootModulesMetadata,
    )


class ImportApplicationIaCRequest(proto.Message):
    r"""Request message for ImportApplicationIaC method.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        gcs_uri (str):
            Optional. The Cloud Storage URI of the
            terraform code.

            This field is a member of `oneof`_ ``source``.
        iac_module (google.cloud.designcenter_v1.types.IaCModule):
            Optional. The IaC module to import.

            This field is a member of `oneof`_ ``source``.
        name (str):
            Required. The name of the application.
        allow_partial_import (bool):
            Optional. If set to true, partially imports
            the valid edits in the IaC and ignores the
            invalid changes. Defaults to false, which means
            any edits which can't be imported must result in
            an error.
        validate_iac (bool):
            Optional. If set to true, the IaC is
            validated against the golden terraform without
            importing. Defaults to false.
    """

    gcs_uri: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="source",
    )
    iac_module: ingestion.IaCModule = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="source",
        message=ingestion.IaCModule,
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    allow_partial_import: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    validate_iac: bool = proto.Field(
        proto.BOOL,
        number=6,
    )


class ImportApplicationIaCResponse(proto.Message):
    r"""Response message for ImportApplicationIaC method.

    Attributes:
        application (google.cloud.designcenter_v1.types.Application):
            Application template corresponding to the
            imported IaC.
        errors (MutableSequence[google.cloud.designcenter_v1.types.ImportIaCError]):
            Errors encountered during import.
        state (google.cloud.designcenter_v1.types.ImportApplicationIaCResponse.State):
            The state of the import.
    """

    class State(proto.Enum):
        r"""State of Import.

        Values:
            STATE_UNSPECIFIED (0):
                Default.
            SUCCEEDED (1):
                The import was successful.
            FAILED (2):
                The import failed.
        """

        STATE_UNSPECIFIED = 0
        SUCCEEDED = 1
        FAILED = 2

    application: deployment_resources.Application = proto.Field(
        proto.MESSAGE,
        number=1,
        message=deployment_resources.Application,
    )
    errors: MutableSequence[ingestion.ImportIaCError] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=ingestion.ImportIaCError,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=3,
        enum=State,
    )


class PreviewApplicationRequest(proto.Message):
    r"""Message for previewing an application.

    Attributes:
        name (str):
            Required. The application name in the following format:
            ``projects/$project/locations/$location/spaces/$space/applications/$application``
        worker_pool (str):
            Optional. The user-specified Worker Pool
            resource in which the Cloud Build job will
            execute. Format:

            projects/{project}/locations/{location}/workerPools/{workerPoolId}
            If this flag is omitted, the worker pool already
            defined on the application will be used. If no
            worker pool is defined on the application, the
            default Cloud Build worker pool is used. The
            worker pool must exist in the same region as the
            application.
        service_account (str):
            Optional. The email address of the service account to use
            for this preview operation.

            - If provided, this service account will be used to execute
              the preview process, taking precedence over any
              service_account specified on the Application resource.
            - The caller must have the 'iam.serviceAccounts.actAs'
              permission on this service account.
            - If this field is omitted, the system will use the
              'service_account' defined within the Application resource.
            - We recommend that you provide a service account here or on
              the Application resource. If you don't provide a service
              account, the preview will fail. Format:
              projects/{PROJECT}/serviceAccounts/{EMAIL_ADDRESS}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    worker_pool: str = proto.Field(
        proto.STRING,
        number=2,
    )
    service_account: str = proto.Field(
        proto.STRING,
        number=3,
    )


class PreviewApplicationResponse(proto.Message):
    r"""Response for PreviewApplication.

    Attributes:
        preview (google.cloud.config_v1.types.Preview):
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


class RecommendIAMRolesRequest(proto.Message):
    r"""Request message for ``RecommendIAMRoles``.

    Attributes:
        name (str):
            Required. The name of the application
            resource for which to recommend IAM roles.
            Format:

            projects/$project/locations/$location/spaces/$space/applications/$application
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class RecommendIAMRolesResponse(proto.Message):
    r"""Response message for ``RecommendIAMRoles``.

    Attributes:
        project_configurations (MutableSequence[google.cloud.designcenter_v1.types.RolesAndApisConfig]):
            A list of project configurations containing
            recommended IAM roles and required APIs for each
            target Google Cloud project in the application
            infrastructure.
    """

    project_configurations: MutableSequence[gcd_deployment.RolesAndApisConfig] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=gcd_deployment.RolesAndApisConfig,
        )
    )


class ConfigureAndDeployTemplateRequest(proto.Message):
    r"""Request message for ConfigureAndDeployTemplate.

    Attributes:
        parent (str):
            Required. The parent resource where the template will be
            deployed. Format:
            ``projects/{project}/locations/{location}``
        template_uri (str):
            Required. The URI or identifier of the
            template to configure and deploy.
        space_id (str):
            Required. The space ID where the template and
            application will be created.
        template_parameters (MutableSequence[google.cloud.designcenter_v1.types.Parameter]):
            Optional. Template configuration parameters
            (key-value pairs).
        service_account (str):
            Optional. The resource name of the service account to use
            for this deployment.

            - If provided, this service account will be used to execute
              the deployment process.
            - The caller must have the ``iam.serviceAccounts.actAs``
              permission on this service account.
            - If this field is omitted, a default system service account
              will be used. Format:
              projects/{PROJECT}/serviceAccounts/{EMAIL_ADDRESS}
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    template_uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    space_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    template_parameters: MutableSequence[parameters.Parameter] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=parameters.Parameter,
    )
    service_account: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ConfigureAndDeployTemplateResponse(proto.Message):
    r"""Response message for ConfigureAndDeployTemplate.
    Populated inside Operation.response upon LRO completion.

    Attributes:
        application_uri (str):
            The URI of the deployed application.
        application_template_uri (str):
            The URI of the application template.
        deployment_metadata (google.cloud.designcenter_v1.types.DeploymentMetadata):
            The deployment metadata of the deployed
            application.
        deployment_state (google.cloud.designcenter_v1.types.Application.State):
            The deployment state of the deployed
            application.
    """

    application_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    application_template_uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    deployment_metadata: gcd_deployment.DeploymentMetadata = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gcd_deployment.DeploymentMetadata,
    )
    deployment_state: deployment_resources.Application.State = proto.Field(
        proto.ENUM,
        number=4,
        enum=deployment_resources.Application.State,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
