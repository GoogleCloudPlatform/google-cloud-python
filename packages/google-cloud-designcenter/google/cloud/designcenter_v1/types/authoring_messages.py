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

from google.cloud.designcenter_v1.types import authoring, export, iac, ingestion

__protobuf__ = proto.module(
    package="google.cloud.designcenter.v1",
    manifest={
        "ListApplicationTemplatesRequest",
        "ListApplicationTemplatesResponse",
        "GetApplicationTemplateRequest",
        "CreateApplicationTemplateRequest",
        "UpdateApplicationTemplateRequest",
        "DeleteApplicationTemplateRequest",
        "CommitApplicationTemplateRequest",
        "SnapshotApplicationTemplateRequest",
        "SnapshotApplicationTemplateResponse",
        "ImportApplicationTemplateRequest",
        "GenerateApplicationTemplateRevisionIaCRequest",
        "GenerateApplicationTemplateRevisionIaCResponse",
        "GenerateApplicationTemplateIaCRequest",
        "GenerateApplicationTemplateIaCResponse",
        "ExportApplicationTemplateIaCRequest",
        "ExportApplicationTemplateIaCResponse",
        "ExportApplicationTemplateRevisionIaCRequest",
        "ExportApplicationTemplateRevisionIaCResponse",
        "ImportApplicationTemplateIaCRequest",
        "ImportApplicationTemplateIaCResponse",
        "IngestApplicationTemplateIaCRequest",
        "IngestApplicationTemplateIaCResponse",
        "ListComponentsRequest",
        "ListComponentsResponse",
        "GetComponentRequest",
        "CreateComponentRequest",
        "UpdateComponentRequest",
        "DeleteComponentRequest",
        "ListConnectionsRequest",
        "ListConnectionsResponse",
        "GetConnectionRequest",
        "CreateConnectionRequest",
        "UpdateConnectionRequest",
        "DeleteConnectionRequest",
        "ImportSerializedApplicationTemplateRequest",
        "ListApplicationTemplateRevisionsRequest",
        "ListApplicationTemplateRevisionsResponse",
        "GetApplicationTemplateRevisionRequest",
        "DeleteApplicationTemplateRevisionRequest",
        "ListApplicationTemplateSystemRevisionsRequest",
        "ListApplicationTemplateSystemRevisionsResponse",
        "GetApplicationTemplateSystemRevisionRequest",
    },
)


class ListApplicationTemplatesRequest(proto.Message):
    r"""Message for requesting a list of application templates.

    Attributes:
        parent (str):
            Required. The parent resource from which to
            list application templates.
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
            Optional. A filter that chooses which shared
            template revisions to return.
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


class ListApplicationTemplatesResponse(proto.Message):
    r"""Message for response to listing application templates.

    Attributes:
        application_templates (MutableSequence[google.cloud.designcenter_v1.types.ApplicationTemplate]):
            The list of application templates.
        next_page_token (str):
            If there might be more results than those
            appearing in this response, then nextPageToken
            is included. To get the next set of results,
            call this method again using the value of
            nextPageToken as pageToken.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    application_templates: MutableSequence[authoring.ApplicationTemplate] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=authoring.ApplicationTemplate,
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


class GetApplicationTemplateRequest(proto.Message):
    r"""Message for getting an application template.

    Attributes:
        name (str):
            Required. The application template name.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateApplicationTemplateRequest(proto.Message):
    r"""Message for creating an application template.

    Attributes:
        parent (str):
            Required. The parent resource in which to
            create the application template.
        application_template_id (str):
            Required. The ID of the application template
            to create.
        application_template (google.cloud.designcenter_v1.types.ApplicationTemplate):
            Required. The application template to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    application_template_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    application_template: authoring.ApplicationTemplate = proto.Field(
        proto.MESSAGE,
        number=3,
        message=authoring.ApplicationTemplate,
    )


class UpdateApplicationTemplateRequest(proto.Message):
    r"""Message for updating an application template.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The fields to overwrite in the application
            template update. The fields specified in the update_mask are
            relative to the resource, not the full request. A field will
            be overwritten if it is in the mask. If you don't provide a
            mask, all fields are overwritten.
        application_template (google.cloud.designcenter_v1.types.ApplicationTemplate):
            Required. The application template to update.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    application_template: authoring.ApplicationTemplate = proto.Field(
        proto.MESSAGE,
        number=2,
        message=authoring.ApplicationTemplate,
    )


class DeleteApplicationTemplateRequest(proto.Message):
    r"""Message for deleting an application template.

    Attributes:
        name (str):
            Required. The application template name.
        force (bool):
            Optional. If set to true, the application
            template's children are also deleted. If false,
            the application template is only deleted if it
            has no children.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class CommitApplicationTemplateRequest(proto.Message):
    r"""Request message for CommitApplicationTemplate method.

    Attributes:
        name (str):
            Required. The name of the application
            template.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class SnapshotApplicationTemplateRequest(proto.Message):
    r"""Message for snapshotting an application template
    asynchronously.

    Attributes:
        name (str):
            Required. The name of the application
            template.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class SnapshotApplicationTemplateResponse(proto.Message):
    r"""Response message for snapshotting an application template
    asynchronously.

    Attributes:
        application_template_revision (google.cloud.designcenter_v1.types.ApplicationTemplateRevision):
            The created application template revision.
    """

    application_template_revision: authoring.ApplicationTemplateRevision = proto.Field(
        proto.MESSAGE,
        number=1,
        message=authoring.ApplicationTemplateRevision,
    )


class ImportApplicationTemplateRequest(proto.Message):
    r"""Request message for ImportApplicationTemplate method.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        application_template_revision_uri (str):
            Optional. The source URI for application
            template revision.

            This field is a member of `oneof`_ ``source``.
        shared_template_revision_uri (str):
            Optional. The source URI for catalog
            template.

            This field is a member of `oneof`_ ``source``.
        serialized_application_template (google.cloud.designcenter_v1.types.SerializedApplicationTemplate):
            Optional. The serialized application template
            to be imported.

            This field is a member of `oneof`_ ``source``.
        application_template_system_revision (str):
            Optional. The system revision to be imported.
            Used when user tries to Restore (rev X) or
            perform Undo/Redo operations.

            This field is a member of `oneof`_ ``source``.
        name (str):
            Required. The name of the application
            template.
        annotations (MutableMapping[str, str]):
            Optional. Annotations to be stored with the new system
            revision created as a result of this import. Sample
            annotations from agentic workflows might look like {
            "designcenter.googleapis.com/agent_id": "gemini-3-flash-v1",
            "designcenter.googleapis.com/llm_agent_summary": "Restored
            to revision Rev-100",
            "designcenter.googleapis.com/external_ref_id":
            "trace-uuid-88921-xyz", }
    """

    application_template_revision_uri: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="source",
    )
    shared_template_revision_uri: str = proto.Field(
        proto.STRING,
        number=4,
        oneof="source",
    )
    serialized_application_template: authoring.SerializedApplicationTemplate = (
        proto.Field(
            proto.MESSAGE,
            number=5,
            oneof="source",
            message=authoring.SerializedApplicationTemplate,
        )
    )
    application_template_system_revision: str = proto.Field(
        proto.STRING,
        number=6,
        oneof="source",
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=7,
    )


class GenerateApplicationTemplateRevisionIaCRequest(proto.Message):
    r"""Request message for GenerateApplicationTemplateRevisionIaC
    method.

    Attributes:
        name (str):
            Required. The name of the application
            template revision.
        iac_format (google.cloud.designcenter_v1.types.GenerateApplicationTemplateRevisionIaCRequest.IACFormat):
            Optional. The IaC format to generate.
        artifact_location (google.cloud.designcenter_v1.types.ArtifactLocation):
            Optional. Specifies the destination for the
            generated IaC, which can be Cloud Storage or a
            Developer Connect repository.
    """

    class IACFormat(proto.Enum):
        r"""The IaC format to generate.

        Values:
            IAC_FORMAT_UNSPECIFIED (0):
                IaC format is unspecified.
            TERRAFORM (1):
                IaC format is Terraform.
            HELM (2):
                IaC format is HELM.
        """

        IAC_FORMAT_UNSPECIFIED = 0
        TERRAFORM = 1
        HELM = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    iac_format: IACFormat = proto.Field(
        proto.ENUM,
        number=2,
        enum=IACFormat,
    )
    artifact_location: export.ArtifactLocation = proto.Field(
        proto.MESSAGE,
        number=3,
        message=export.ArtifactLocation,
    )


class GenerateApplicationTemplateRevisionIaCResponse(proto.Message):
    r"""Response message for GenerateApplicationTemplateRevisionIaC
    method.

    Attributes:
        artifact_location (google.cloud.designcenter_v1.types.ArtifactLocation):
            The destination where the generated IaC was
            written.
        root_modules_metadata (google.cloud.designcenter_v1.types.RootModulesMetadata):
            Root modules metadata of the application
            template revision.
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


class GenerateApplicationTemplateIaCRequest(proto.Message):
    r"""Request message for GenerateApplicationTemplateIaC method.

    Attributes:
        name (str):
            Required. The name of the application
            template.
        iac_format (google.cloud.designcenter_v1.types.GenerateApplicationTemplateIaCRequest.IACFormat):
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

    class IACFormat(proto.Enum):
        r"""The IaC format to generate.

        Values:
            IAC_FORMAT_UNSPECIFIED (0):
                IaC format is unspecified.
            TERRAFORM (1):
                IaC format is Terraform.
            HELM (2):
                IaC format is HELM.
        """

        IAC_FORMAT_UNSPECIFIED = 0
        TERRAFORM = 1
        HELM = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    iac_format: IACFormat = proto.Field(
        proto.ENUM,
        number=2,
        enum=IACFormat,
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


class GenerateApplicationTemplateIaCResponse(proto.Message):
    r"""Response message for GenerateApplicationTemplateIaC method.

    Attributes:
        gcs_uri (str):
            DEPRECATED: Use the 'artifact_location' field instead. The
            Cloud Storage URI of the generated IaC.
        artifact_location (google.cloud.designcenter_v1.types.ArtifactLocation):
            The destination where the generated IaC was
            written.
        root_modules_metadata (google.cloud.designcenter_v1.types.RootModulesMetadata):
            Root modules metadata of the application
            template.
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


class ExportApplicationTemplateIaCRequest(proto.Message):
    r"""Request message for ExportApplicationTemplateIaC method.

    Attributes:
        name (str):
            Required. The name of the application
            template.
        artifact_location (google.cloud.designcenter_v1.types.ArtifactLocation):
            Optional. Specifies the destination for the
            generated IaC, which can be Cloud Storage or a
            Developer Connect repository. Default is Google
            Cloud Storage.
        export_iac_config (google.cloud.designcenter_v1.types.ExportIaCConfig):
            Optional. Configuration for exporting IaC.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    artifact_location: export.ArtifactLocation = proto.Field(
        proto.MESSAGE,
        number=3,
        message=export.ArtifactLocation,
    )
    export_iac_config: export.ExportIaCConfig = proto.Field(
        proto.MESSAGE,
        number=5,
        message=export.ExportIaCConfig,
    )


class ExportApplicationTemplateIaCResponse(proto.Message):
    r"""Response message for ExportApplicationTemplateIaC method.

    Attributes:
        artifact_location (google.cloud.designcenter_v1.types.ArtifactLocation):
            The destination where the generated IaC was
            written.
        root_modules_metadata (google.cloud.designcenter_v1.types.RootModulesMetadata):
            Root modules metadata of the application
            template.
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


class ExportApplicationTemplateRevisionIaCRequest(proto.Message):
    r"""Request message for ExportApplicationTemplateRevisionIaC
    method.

    Attributes:
        name (str):
            Required. The name of the application
            template revision.
        artifact_location (google.cloud.designcenter_v1.types.ArtifactLocation):
            Optional. Specifies the destination for the
            generated IaC, which can be Cloud Storage or a
            Developer Connect repository. Default is Google
            Cloud Storage.
        export_iac_config (google.cloud.designcenter_v1.types.ExportIaCConfig):
            Optional. Configuration for exporting IaC.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    artifact_location: export.ArtifactLocation = proto.Field(
        proto.MESSAGE,
        number=3,
        message=export.ArtifactLocation,
    )
    export_iac_config: export.ExportIaCConfig = proto.Field(
        proto.MESSAGE,
        number=5,
        message=export.ExportIaCConfig,
    )


class ExportApplicationTemplateRevisionIaCResponse(proto.Message):
    r"""Response message for ExportApplicationTemplateRevisionIaC
    method.

    Attributes:
        artifact_location (google.cloud.designcenter_v1.types.ArtifactLocation):
            The destination where the generated IaC was
            written.
        root_modules_metadata (google.cloud.designcenter_v1.types.RootModulesMetadata):
            Root modules metadata of the application
            template revision.
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


class ImportApplicationTemplateIaCRequest(proto.Message):
    r"""Request message for ImportApplicationTemplateIaC method.

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
        developer_connect_source_config (google.cloud.designcenter_v1.types.DeveloperConnectSourceConfig):
            Optional. Configuration for fetching content
            from source code repository such as GitHub or
            Bitbucket through Developer Connect.

            This field is a member of `oneof`_ ``source``.
        name (str):
            Required. The name of the application
            template.
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
    developer_connect_source_config: ingestion.DeveloperConnectSourceConfig = (
        proto.Field(
            proto.MESSAGE,
            number=7,
            oneof="source",
            message=ingestion.DeveloperConnectSourceConfig,
        )
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


class ImportApplicationTemplateIaCResponse(proto.Message):
    r"""Response message for ImportApplicationTemplateIaC method.

    Attributes:
        application_template (google.cloud.designcenter_v1.types.ApplicationTemplate):
            Application template corresponding to the
            imported IaC.
        errors (MutableSequence[google.cloud.designcenter_v1.types.ImportIaCError]):
            Errors encountered during import.
        state (google.cloud.designcenter_v1.types.ImportApplicationTemplateIaCResponse.State):
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

    application_template: authoring.ApplicationTemplate = proto.Field(
        proto.MESSAGE,
        number=1,
        message=authoring.ApplicationTemplate,
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


class IngestApplicationTemplateIaCRequest(proto.Message):
    r"""Request message for IngestApplicationTemplateIaC method.

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
            Optional. The IaC configuration to import.

            This field is a member of `oneof`_ ``source``.
        devconnect_source_config (google.cloud.designcenter_v1.types.DeveloperConnectSourceConfig):
            Optional. Configuration for fetching content
            from source code repository such as GitHub or
            Bitbucket through Developer Connect.

            This field is a member of `oneof`_ ``source``.
        git_source (google.cloud.designcenter_v1.types.GitSource):
            Optional. The git source.

            This field is a member of `oneof`_ ``source``.
        name (str):
            Required. The name of the application
            template.
        validate_catalog_compatibility (bool):
            Optional. If set to true, validates if the
            imported IaC is compatible with the catalog.
        raw_terraform_import_enabled (bool):
            Optional. If set to true, imports the IaC as
            raw terraform and does not attempt SAT
            conversion.
    """

    gcs_uri: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="source",
    )
    iac_module: ingestion.IaCModule = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="source",
        message=ingestion.IaCModule,
    )
    devconnect_source_config: ingestion.DeveloperConnectSourceConfig = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="source",
        message=ingestion.DeveloperConnectSourceConfig,
    )
    git_source: ingestion.GitSource = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="source",
        message=ingestion.GitSource,
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    validate_catalog_compatibility: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    raw_terraform_import_enabled: bool = proto.Field(
        proto.BOOL,
        number=7,
    )


class IngestApplicationTemplateIaCResponse(proto.Message):
    r"""Response message for IngestApplicationTemplateIaC method.

    Attributes:
        application_template (google.cloud.designcenter_v1.types.ApplicationTemplate):
            Application template corresponding to the
            imported IaC.
        errors (MutableSequence[google.cloud.designcenter_v1.types.ImportIaCError]):
            Errors encountered during import.
        state (google.cloud.designcenter_v1.types.ImportApplicationTemplateIaCResponse.State):
            The state of the import.
    """

    application_template: authoring.ApplicationTemplate = proto.Field(
        proto.MESSAGE,
        number=1,
        message=authoring.ApplicationTemplate,
    )
    errors: MutableSequence[ingestion.ImportIaCError] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=ingestion.ImportIaCError,
    )
    state: "ImportApplicationTemplateIaCResponse.State" = proto.Field(
        proto.ENUM,
        number=3,
        enum="ImportApplicationTemplateIaCResponse.State",
    )


class ListComponentsRequest(proto.Message):
    r"""Message for requesting a list of components.

    Attributes:
        parent (str):
            Required. The parent resource from which the
            list of components is requested.
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
            components to return.
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


class ListComponentsResponse(proto.Message):
    r"""Message for response to listing components.

    Attributes:
        components (MutableSequence[google.cloud.designcenter_v1.types.Component]):
            The list of components.
        next_page_token (str):
            If there might be more results than those
            appearing in this response, then nextPageToken
            is included. To get the next set of results,
            call this method again using the value of
            nextPageToken as pageToken.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    components: MutableSequence[authoring.Component] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=authoring.Component,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetComponentRequest(proto.Message):
    r"""Message for getting a component.

    Attributes:
        name (str):
            Required. The component name.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateComponentRequest(proto.Message):
    r"""Message for creating a component.

    Attributes:
        parent (str):
            Required. The parent resource in which to
            create the component.
        component_id (str):
            Required. The ID of the component to create.
        component (google.cloud.designcenter_v1.types.Component):
            Required. The component to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    component_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    component: authoring.Component = proto.Field(
        proto.MESSAGE,
        number=3,
        message=authoring.Component,
    )


class UpdateComponentRequest(proto.Message):
    r"""Message for updating a component.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The fields to overwrite in the
            component update. If you don't provide a mask,
            all fields are overwritten.
        component (google.cloud.designcenter_v1.types.Component):
            Required. The component to update.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    component: authoring.Component = proto.Field(
        proto.MESSAGE,
        number=2,
        message=authoring.Component,
    )


class DeleteComponentRequest(proto.Message):
    r"""Message for deleting a component.

    Attributes:
        name (str):
            Required. The component name.
        force (bool):
            Optional. If set to true, the component's
            children are also deleted. If false, the
            component is only deleted if it has no children.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class ListConnectionsRequest(proto.Message):
    r"""Message for requesting a list of connections.

    Attributes:
        parent (str):
            Required. The parent resource from which to
            request a list of connections.
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
            Optional. A filter that chooses which
            connections to return.
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


class ListConnectionsResponse(proto.Message):
    r"""Message for response to listing connections.

    Attributes:
        connections (MutableSequence[google.cloud.designcenter_v1.types.Connection]):
            The list of connections.
        next_page_token (str):
            If there might be more results than those
            appearing in this response, then nextPageToken
            is included. To get the next set of results,
            call this method again using the value of
            nextPageToken as pageToken.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    connections: MutableSequence[authoring.Connection] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=authoring.Connection,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetConnectionRequest(proto.Message):
    r"""Message for getting a connection.

    Attributes:
        name (str):
            Required. Name of the resource
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateConnectionRequest(proto.Message):
    r"""Message for creating a connection.

    Attributes:
        parent (str):
            Required. The parent resource in which to
            create a connection.
        connection_id (str):
            Required. The ID of the connection to create.
        connection (google.cloud.designcenter_v1.types.Connection):
            Required. The connection to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    connection_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    connection: authoring.Connection = proto.Field(
        proto.MESSAGE,
        number=3,
        message=authoring.Connection,
    )


class UpdateConnectionRequest(proto.Message):
    r"""Message for updating a connection.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Fields to overwrite in the connection update. The
            fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. If you don't provide a mask, all
            fields are overwritten.
        connection (google.cloud.designcenter_v1.types.Connection):
            Required. The connection to update.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    connection: authoring.Connection = proto.Field(
        proto.MESSAGE,
        number=2,
        message=authoring.Connection,
    )


class DeleteConnectionRequest(proto.Message):
    r"""Message for deleting a connection.

    Attributes:
        name (str):
            Required. The connection name.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ImportSerializedApplicationTemplateRequest(proto.Message):
    r"""Request message for ImportSerializedApplicationTemplate.

    Attributes:
        name (str):
            Required. The name of the application
            template.
        serialized_application_template (google.cloud.designcenter_v1.types.SerializedApplicationTemplate):
            Required. The serialized application template
            to be imported.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    serialized_application_template: authoring.SerializedApplicationTemplate = (
        proto.Field(
            proto.MESSAGE,
            number=2,
            message=authoring.SerializedApplicationTemplate,
        )
    )


class ListApplicationTemplateRevisionsRequest(proto.Message):
    r"""Message for requesting a list of application template
    revisions.

    Attributes:
        parent (str):
            Required. The parent from which to list
            application template revisions.
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
            application template revisions to return.
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


class ListApplicationTemplateRevisionsResponse(proto.Message):
    r"""Message for response to listing application template
    revisions.

    Attributes:
        application_template_revisions (MutableSequence[google.cloud.designcenter_v1.types.ApplicationTemplateRevision]):
            The list of application template revisions.
        next_page_token (str):
            If there might be more results than those
            appearing in this response, then nextPageToken
            is included. To get the next set of results,
            call this method again using the value of
            nextPageToken as pageToken.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    application_template_revisions: MutableSequence[
        authoring.ApplicationTemplateRevision
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=authoring.ApplicationTemplateRevision,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetApplicationTemplateRevisionRequest(proto.Message):
    r"""Message for getting an application template revision.

    Attributes:
        name (str):
            Required. The application template revision
            name.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteApplicationTemplateRevisionRequest(proto.Message):
    r"""Message for deleting an application template revision.

    Attributes:
        name (str):
            Required. The application template revision
            name.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListApplicationTemplateSystemRevisionsRequest(proto.Message):
    r"""Message for requesting a list of application template system
    revisions.

    Attributes:
        parent (str):
            Required. The parent Application Template from which to list
            the system revisions. Format:
            projects/{project}/locations/{location}/spaces/{space}/applicationTemplates/{application_template}
        page_size (int):
            Optional. The maximum number of system
            revisions to return. The service may return
            fewer than this value. If unspecified, at most
            50 system revisions will be returned. The
            maximum value is 1000; values above 1000 will be
            coerced to 1000.
        page_token (str):
            Optional. If present, then retrieve the next
            batch of results from the preceding call to this
            method. pageToken must be the value of
            nextPageToken from the previous response. The
            values of other method parameters should be
            identical to those in the previous call.
        filter (str):
            Optional. A filter expression that filters
            system revisions listed in the response. See
            https://google.aip.dev/160 for more information
            on the grammar.
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


class ListApplicationTemplateSystemRevisionsResponse(proto.Message):
    r"""Message for response to listing application template system
    revisions.

    Attributes:
        application_template_system_revisions (MutableSequence[google.cloud.designcenter_v1.types.ApplicationTemplateSystemRevision]):
            The list of application template system
            revisions.
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

    application_template_system_revisions: MutableSequence[
        authoring.ApplicationTemplateSystemRevision
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=authoring.ApplicationTemplateSystemRevision,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetApplicationTemplateSystemRevisionRequest(proto.Message):
    r"""Message for getting an ApplicationTemplateSystemRevision.

    Attributes:
        name (str):
            Required. The name of the ApplicationTemplateSystemRevision
            to retrieve. Format:
            projects/{project}/locations/{location}/spaces/{space}/applicationTemplates/{application_template}/systemRevisions/{system_revision}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
