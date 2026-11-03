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

from google.cloud.designcenter_v1.types import (
    authoring,
    enums,
    ingestion,
    metadata_,
    parameters,
)

__protobuf__ = proto.module(
    package="google.cloud.designcenter.v1",
    manifest={
        "Space",
        "Catalog",
        "CatalogTemplate",
        "CatalogTemplateRevision",
    },
)


class Space(proto.Message):
    r"""Space is a top level resource for managing teams building
    applications through Application Design Center.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The space name.
        display_name (str):
            Optional. Display name for the space.
        description (str):
            Optional. Description for the space.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Space creation timestamp.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Space update timestamp
        enable_gcp_shared_templates (bool):
            Optional. Flag to enable Google opinionated
            shared templates.

            This field is a member of `oneof`_ ``_enable_gcp_shared_templates``.
        gcs_bucket (str):
            Optional. An existing Google Cloud Storage bucket that you
            want to use instead of creating a new bucket during
            Application Design Center setup. If not provided, a default
            bucket is created during setup. The bucket must exist in the
            same project as the space. If the bucket name does not exist
            in the same project as the space, the request fails with an
            INVALID_ARGUMENT error. If you do not have access to the
            bucket, the request fails with a PERMISSION_DENIED error.
            Format: {$bucket_name} For example, if the Cloud Storage
            bucket URI is gs://{$bucket_name}, the format is
            {$bucket_name}.
        tags (MutableMapping[str, str]):
            Optional. Input only. Immutable. Tags are key/values bound
            to space resource. Example:

            ::

                 "123/environment": "production"
                 "123/costCenter": "marketing"

            For more information on tag creation and management, see
            https://cloud.google.com/resource-manager/docs/tags/tags-overview.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    enable_gcp_shared_templates: bool = proto.Field(
        proto.BOOL,
        number=6,
        optional=True,
    )
    gcs_bucket: str = proto.Field(
        proto.STRING,
        number=7,
    )
    tags: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=8,
    )


class Catalog(proto.Message):
    r"""A catalog is a collection of templates.

    Attributes:
        name (str):
            Identifier. The catalog name in the following format:
            ``projects/$project/locations/$location/spaces/$space/catalogs/$catalog``
        display_name (str):
            Optional. The catalog display name.
        description (str):
            Optional. The catalog description.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The catalog creation timestamp.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The catalog update timestamp.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )


class CatalogTemplate(proto.Message):
    r"""A template inside a catalog.

    Attributes:
        name (str):
            Identifier. The catalog template name in following format:
            ``projects/$project/locations/$location/spaces/$space/catalogs/$catalog/templates/$template``
        display_name (str):
            Optional. The display name of a catalog
            template.
        description (str):
            Optional. The catalog template description.
        uuid (str):
            Output only. The template revisions UUID.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The catalog template creation
            timestamp.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The catalog template update
            timestamp.
        latest_revision_id (str):
            Output only. Latest revision of the template.
        template_category (google.cloud.designcenter_v1.types.TemplateCategory):
            Required. The category of the Application
            Design Center application template.
        type_ (google.cloud.designcenter_v1.types.TemplateType):
            Optional. The Application Design Center
            application template type.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=7,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    uuid: str = proto.Field(
        proto.STRING,
        number=5,
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
    latest_revision_id: str = proto.Field(
        proto.STRING,
        number=6,
    )
    template_category: enums.TemplateCategory = proto.Field(
        proto.ENUM,
        number=8,
        enum=enums.TemplateCategory,
    )
    type_: enums.TemplateType = proto.Field(
        proto.ENUM,
        number=9,
        enum=enums.TemplateType,
    )


class CatalogTemplateRevision(proto.Message):
    r"""Template revisions inside a catalog.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        git_source (google.cloud.designcenter_v1.types.GitSource):
            Optional. The git source.

            This field is a member of `oneof`_ ``artifact_location``.
        gcs_source_uri (str):
            Optional. Deprecated: Added new field tf_module_gcs_uri. The
            Cloud Storage URI, which must be in the format gs://[bucket]
            or gs://[bucket]/[object].

            This field is a member of `oneof`_ ``artifact_location``.
        application_template_revision_source (str):
            Optional. The application template revision
            source.

            This field is a member of `oneof`_ ``artifact_location``.
        developer_connect_source_config (google.cloud.designcenter_v1.types.DeveloperConnectSourceConfig):
            Optional. Configuration for fetching content
            from source code repository such as GitHub or
            Bitbucket through Developer Connect.

            This field is a member of `oneof`_ ``artifact_location``.
        oci_repo (google.cloud.designcenter_v1.types.OciRepo):
            Optional. The Open Container Initiative (OCI)
            repo source that contains helm charts.

            This field is a member of `oneof`_ ``artifact_location``.
        name (str):
            Identifier. The catalog template revision name.
            ``projects/$project/locations/$location/spaces/$space/catalogs/$catalog/templates/$template/revisions/$revision``
        description (str):
            Optional. The catalog template revision
            description.
        type_ (google.cloud.designcenter_v1.types.TemplateType):
            Optional. The Application Design Center
            application template type.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The catalog template creation
            timestamp.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The catalog template update
            timestamp.
        template_metadata (google.cloud.designcenter_v1.types.TFBlueprintMetadata):
            Output only. Template metadata related to
            Terraform input and output.
        state (google.cloud.designcenter_v1.types.CatalogTemplateRevision.State):
            Output only. The template state
            (validating/ready/invalid).
        application_template_revision (google.cloud.designcenter_v1.types.SerializedApplicationTemplate):
            Output only. The application template
            revision.
        helm_chart_metadata (google.cloud.designcenter_v1.types.HelmChartMetadata):
            Output only. The helm chart metadata.
        uuid (str):
            Output only. UUID of the template revision.
        metadata_input (google.cloud.designcenter_v1.types.MetadataInput):
            Optional. Metadata input.
        template_category (google.cloud.designcenter_v1.types.TemplateCategory):
            Output only. The category of the template.
        logical_products (MutableSequence[google.cloud.designcenter_v1.types.LogicalProduct]):
            Output only. The Product Main logical product
            type information.
        annotations (MutableMapping[str, str]):
            Optional. The annotations of the template
            revision. Key is the annotation name. Value is
            the annotation value.
        inferred_metadata (google.cloud.designcenter_v1.types.InferredMetadata):
            Output only. Metadata that was automatically
            inferred from the template content. This field
            can be updated by the system as it gets new
            information.
        resource_types (MutableSequence[google.cloud.designcenter_v1.types.ResourceType]):
            Output only. The resource types present in
            the template revision.
        iac_source (google.cloud.designcenter_v1.types.IACSource):
            Output only. Indicates the IaC source format
            of this catalog template revision.
        application_parameters (MutableSequence[google.cloud.designcenter_v1.types.Parameter]):
            Optional. The values provided for the input
            variables.
    """

    class State(proto.Enum):
        r"""The template state.

        Values:
            STATE_UNSPECIFIED (0):
                Default.
            VALIDATING (1):
                The template is being validated.
            ACTIVE (2):
                The template is ready to be used.
            INVALID (3):
                The template is invalid.
        """

        STATE_UNSPECIFIED = 0
        VALIDATING = 1
        ACTIVE = 2
        INVALID = 3

    git_source: ingestion.GitSource = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="artifact_location",
        message=ingestion.GitSource,
    )
    gcs_source_uri: str = proto.Field(
        proto.STRING,
        number=20,
        oneof="artifact_location",
    )
    application_template_revision_source: str = proto.Field(
        proto.STRING,
        number=11,
        oneof="artifact_location",
    )
    developer_connect_source_config: ingestion.DeveloperConnectSourceConfig = (
        proto.Field(
            proto.MESSAGE,
            number=15,
            oneof="artifact_location",
            message=ingestion.DeveloperConnectSourceConfig,
        )
    )
    oci_repo: ingestion.OciRepo = proto.Field(
        proto.MESSAGE,
        number=17,
        oneof="artifact_location",
        message=ingestion.OciRepo,
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=14,
    )
    type_: enums.TemplateType = proto.Field(
        proto.ENUM,
        number=2,
        enum=enums.TemplateType,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    template_metadata: metadata_.TFBlueprintMetadata = proto.Field(
        proto.MESSAGE,
        number=8,
        message=metadata_.TFBlueprintMetadata,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=9,
        enum=State,
    )
    application_template_revision: authoring.SerializedApplicationTemplate = (
        proto.Field(
            proto.MESSAGE,
            number=12,
            message=authoring.SerializedApplicationTemplate,
        )
    )
    helm_chart_metadata: metadata_.HelmChartMetadata = proto.Field(
        proto.MESSAGE,
        number=16,
        message=metadata_.HelmChartMetadata,
    )
    uuid: str = proto.Field(
        proto.STRING,
        number=13,
    )
    metadata_input: metadata_.MetadataInput = proto.Field(
        proto.MESSAGE,
        number=18,
        message=metadata_.MetadataInput,
    )
    template_category: enums.TemplateCategory = proto.Field(
        proto.ENUM,
        number=19,
        enum=enums.TemplateCategory,
    )
    logical_products: MutableSequence[metadata_.LogicalProduct] = proto.RepeatedField(
        proto.MESSAGE,
        number=21,
        message=metadata_.LogicalProduct,
    )
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=22,
    )
    inferred_metadata: metadata_.InferredMetadata = proto.Field(
        proto.MESSAGE,
        number=23,
        message=metadata_.InferredMetadata,
    )
    resource_types: MutableSequence[metadata_.ResourceType] = proto.RepeatedField(
        proto.MESSAGE,
        number=24,
        message=metadata_.ResourceType,
    )
    iac_source: enums.IACSource = proto.Field(
        proto.ENUM,
        number=27,
        enum=enums.IACSource,
    )
    application_parameters: MutableSequence[parameters.Parameter] = proto.RepeatedField(
        proto.MESSAGE,
        number=28,
        message=parameters.Parameter,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
