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
        "Share",
        "SharedTemplate",
        "SharedTemplateRevision",
    },
)


class Share(proto.Message):
    r"""A catalog share between spaces.

    Attributes:
        name (str):
            Identifier. The share name in the following format:
            ``projects/$project/locations/$location/spaces/$space/catalogs/$catalog/shares/$share``
        destination_space (str):
            Required. The space resource path to which the catalog is
            shared. Format is
            ``projects/$project/locations/$location/spaces/$space``
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The share creation timestamp.
        state (google.cloud.designcenter_v1.types.Share.State):
            Output only. The state of the share.
    """

    class State(proto.Enum):
        r"""The share status, which indicates whether the catalog is in
        sync.

        Values:
            STATE_UNSPECIFIED (0):
                The state of the share is unknown.
            IN_SYNC (1):
                The share is in sync with the shared template
                catalog.
            OUT_OF_SYNC (2):
                The share is out of sync with the shared
                template catalog.
        """

        STATE_UNSPECIFIED = 0
        IN_SYNC = 1
        OUT_OF_SYNC = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    destination_space: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=4,
        enum=State,
    )


class SharedTemplate(proto.Message):
    r"""A read-only template that is shared with a space.

    Attributes:
        name (str):
            Identifier. The shared template name.
            ``projects/$project/locations/$location/spaces/$space/sharedTemplates/$sharedTemplate``
        display_name (str):
            Optional. The shared template display name.
        description (str):
            Optional. The shared template description.
        origin_template (str):
            Output only. The origin template of the
            shared template.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The shared template creation
            timestamp.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The shared template update
            timestamp.
        latest_revision_id (str):
            Output only. Latest revision of the shared
            template.
        template_category (google.cloud.designcenter_v1.types.TemplateCategory):
            Required. The category of the template.
        type_ (google.cloud.designcenter_v1.types.TemplateType):
            Optional. The Application Design Center
            assembly template type.
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
    origin_template: str = proto.Field(
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


class SharedTemplateRevision(proto.Message):
    r"""A read-only template revision that is shared with a space.

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
            Identifier. The shared template revision name.
            $sharedTemplate is a server-generated UUID.
            ``projects/$project/locations/$location/spaces/$space/sharedTemplates/$sharedTemplate/revisions/$revision``
        description (str):
            Optional. The shared template revision
            description.
        type_ (google.cloud.designcenter_v1.types.TemplateType):
            Optional. The Application Design Center
            assembly template type.
        shared_template_metadata (google.cloud.designcenter_v1.types.TFBlueprintMetadata):
            Output only. The shared template metadata.
        origin_template_revision (str):
            Output only. The shared template revision
            refers to the following catalog template
            revision.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The shared template revision
            creation timestamp.
        application_template_revision (google.cloud.designcenter_v1.types.SerializedApplicationTemplate):
            Output only. The serialized application
            template revision.
        helm_chart_metadata (google.cloud.designcenter_v1.types.HelmChartMetadata):
            Output only. The helm chart metadata.
        template_category (google.cloud.designcenter_v1.types.TemplateCategory):
            Output only. The category of the template.
        logical_products (MutableSequence[google.cloud.designcenter_v1.types.LogicalProduct]):
            Output only. The Product Main logical product
            type information.
        annotations (MutableMapping[str, str]):
            Optional. The annotations of the shared
            template revision. Key is the annotation name.
            Value is the annotation value.
        inferred_metadata (google.cloud.designcenter_v1.types.InferredMetadata):
            Output only. Metadata that was automatically
            inferred from the template content.
        resource_types (MutableSequence[google.cloud.designcenter_v1.types.ResourceType]):
            Output only. The resource types present in
            the template revision.
        iac_source (google.cloud.designcenter_v1.types.IACSource):
            Output only. Indicates the IaC source format
            of this shared template revision.
        application_parameters (MutableSequence[google.cloud.designcenter_v1.types.Parameter]):
            Optional. The values provided for the input
            variables.
    """

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
        number=10,
        oneof="artifact_location",
    )
    developer_connect_source_config: ingestion.DeveloperConnectSourceConfig = (
        proto.Field(
            proto.MESSAGE,
            number=13,
            oneof="artifact_location",
            message=ingestion.DeveloperConnectSourceConfig,
        )
    )
    oci_repo: ingestion.OciRepo = proto.Field(
        proto.MESSAGE,
        number=15,
        oneof="artifact_location",
        message=ingestion.OciRepo,
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=12,
    )
    type_: enums.TemplateType = proto.Field(
        proto.ENUM,
        number=2,
        enum=enums.TemplateType,
    )
    shared_template_metadata: metadata_.TFBlueprintMetadata = proto.Field(
        proto.MESSAGE,
        number=6,
        message=metadata_.TFBlueprintMetadata,
    )
    origin_template_revision: str = proto.Field(
        proto.STRING,
        number=7,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    application_template_revision: authoring.SerializedApplicationTemplate = (
        proto.Field(
            proto.MESSAGE,
            number=11,
            message=authoring.SerializedApplicationTemplate,
        )
    )
    helm_chart_metadata: metadata_.HelmChartMetadata = proto.Field(
        proto.MESSAGE,
        number=14,
        message=metadata_.HelmChartMetadata,
    )
    template_category: enums.TemplateCategory = proto.Field(
        proto.ENUM,
        number=16,
        enum=enums.TemplateCategory,
    )
    logical_products: MutableSequence[metadata_.LogicalProduct] = proto.RepeatedField(
        proto.MESSAGE,
        number=17,
        message=metadata_.LogicalProduct,
    )
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=18,
    )
    inferred_metadata: metadata_.InferredMetadata = proto.Field(
        proto.MESSAGE,
        number=19,
        message=metadata_.InferredMetadata,
    )
    resource_types: MutableSequence[metadata_.ResourceType] = proto.RepeatedField(
        proto.MESSAGE,
        number=21,
        message=metadata_.ResourceType,
    )
    iac_source: enums.IACSource = proto.Field(
        proto.ENUM,
        number=24,
        enum=enums.IACSource,
    )
    application_parameters: MutableSequence[parameters.Parameter] = proto.RepeatedField(
        proto.MESSAGE,
        number=25,
        message=parameters.Parameter,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
