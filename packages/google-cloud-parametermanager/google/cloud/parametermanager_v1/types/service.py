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

import google.iam.v1.resource_policy_member_pb2 as resource_policy_member_pb2  # type: ignore
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.parametermanager.v1",
    manifest={
        "ParameterFormat",
        "TemplateFormat",
        "View",
        "Parameter",
        "ListParametersRequest",
        "ListParametersResponse",
        "GetParameterRequest",
        "CreateParameterRequest",
        "UpdateParameterRequest",
        "DeleteParameterRequest",
        "ParameterVersion",
        "ParameterVersionPayload",
        "ListParameterVersionsRequest",
        "ListParameterVersionsResponse",
        "GetParameterVersionRequest",
        "RenderParameterVersionRequest",
        "RenderParameterVersionResponse",
        "CreateParameterVersionRequest",
        "UpdateParameterVersionRequest",
        "DeleteParameterVersionRequest",
        "Template",
        "ListTemplatesRequest",
        "ListTemplatesResponse",
        "GetTemplateRequest",
        "CreateTemplateRequest",
        "UpdateTemplateRequest",
        "DeleteTemplateRequest",
        "TemplateVersion",
        "TemplateVersionPayload",
        "ListTemplateVersionsRequest",
        "ListTemplateVersionsResponse",
        "GetTemplateVersionRequest",
        "CreateTemplateVersionRequest",
        "UpdateTemplateVersionRequest",
        "DeleteTemplateVersionRequest",
        "RenderTemplateVersionRequest",
        "RenderTemplateVersionResponse",
    },
)


class ParameterFormat(proto.Enum):
    r"""Option to specify the format of a Parameter resource
    (UNFORMATTED / YAML / JSON). This option is user specified at
    the time of creation of the resource and is immutable.

    Values:
        PARAMETER_FORMAT_UNSPECIFIED (0):
            The default / unset value.
            The API will default to the UNFORMATTED format.
        UNFORMATTED (1):
            Unformatted.
        YAML (2):
            YAML format.
        JSON (3):
            JSON format.
    """

    PARAMETER_FORMAT_UNSPECIFIED = 0
    UNFORMATTED = 1
    YAML = 2
    JSON = 3


class TemplateFormat(proto.Enum):
    r"""Option to specify the format of a Template resource (YAML /
    JSON). This option is user specified at the time of creation of
    the resource and is immutable. Templates do not support the
    UNFORMATTED format. Additional values may be added in the
    future.

    Values:
        TEMPLATE_FORMAT_UNSPECIFIED (0):
            The default / unset value.
            The API will default to the YAML format.
        TEMPLATE_FORMAT_YAML (1):
            YAML format.
        TEMPLATE_FORMAT_JSON (2):
            JSON format.
    """

    TEMPLATE_FORMAT_UNSPECIFIED = 0
    TEMPLATE_FORMAT_YAML = 1
    TEMPLATE_FORMAT_JSON = 2


class View(proto.Enum):
    r"""Option for requesting only metadata, or user provided payload
    of a ParameterVersion or TemplateVersion resource.

    Values:
        VIEW_UNSPECIFIED (0):
            The default / unset value.
            The API will default to the FULL view.
        BASIC (1):
            Include only the metadata for the resource.
        FULL (2):
            Include metadata & other relevant payload
            data as well. This is the default view.
    """

    VIEW_UNSPECIFIED = 0
    BASIC = 1
    FULL = 2


class Parameter(proto.Message):
    r"""Message describing Parameter resource

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. [Output only] The resource name of the Parameter
            in the format ``projects/*/locations/*/parameters/*``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. [Output only] Create time stamp
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. [Output only] Update time stamp
        labels (MutableMapping[str, str]):
            Optional. Labels as key value pairs
        format_ (google.cloud.parametermanager_v1.types.ParameterFormat):
            Optional. Specifies the format of a
            Parameter.
        policy_member (google.iam.v1.resource_policy_member_pb2.ResourcePolicyMember):
            Output only. [Output-only] policy member strings of a Google
            Cloud resource.
        kms_key (str):
            Optional. Customer managed encryption key (CMEK) to use for
            encrypting the Parameter Versions. If not set, the default
            Google-managed encryption key will be used. Cloud KMS
            CryptoKeys must reside in the same location as the
            Parameter. The expected format is
            ``projects/*/locations/*/keyRings/*/cryptoKeys/*``.

            This field is a member of `oneof`_ ``_kms_key``.
        tags (MutableMapping[str, str]):
            Optional. Input only. Immutable. Tag keys and tag values
            that are bound to this Parameter. You must represent each
            item in the map as:
            ``"<tag-key-namespaced-name>" : "<tag-value-short-name>"``.

            For example, a single resource can have the following tags:

            ::

                 "123/environment": "production",
                 "123/costCenter": "marketing",

            Tags are used to organize and group resources.

            Tags can be used to control policy evaluation for the
            resource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    format_: "ParameterFormat" = proto.Field(
        proto.ENUM,
        number=5,
        enum="ParameterFormat",
    )
    policy_member: resource_policy_member_pb2.ResourcePolicyMember = proto.Field(
        proto.MESSAGE,
        number=6,
        message=resource_policy_member_pb2.ResourcePolicyMember,
    )
    kms_key: str = proto.Field(
        proto.STRING,
        number=7,
        optional=True,
    )
    tags: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=8,
    )


class ListParametersRequest(proto.Message):
    r"""Message for requesting list of Parameters

    Attributes:
        parent (str):
            Required. Parent value for ListParametersRequest in the
            format ``projects/*/locations/*``.
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListParameters`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListParameters`` must match the call that provided the
            page token.
        filter (str):
            Optional. Filtering results
        order_by (str):
            Optional. Hint for how to order the results
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


class ListParametersResponse(proto.Message):
    r"""Message for response to listing Parameters

    Attributes:
        parameters (MutableSequence[google.cloud.parametermanager_v1.types.Parameter]):
            The list of Parameters
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Unordered list. Locations that could not be
            reached.
    """

    @property
    def raw_page(self):
        return self

    parameters: MutableSequence["Parameter"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Parameter",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetParameterRequest(proto.Message):
    r"""Message for getting a Parameter

    Attributes:
        name (str):
            Required. Name of the resource in the format
            ``projects/*/locations/*/parameters/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateParameterRequest(proto.Message):
    r"""Message for creating a Parameter

    Attributes:
        parent (str):
            Required. Value for parent in the format
            ``projects/*/locations/*``.
        parameter_id (str):
            Required. Id of the Parameter resource
        parameter (google.cloud.parametermanager_v1.types.Parameter):
            Required. The Parameter resource being
            created
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    parameter_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    parameter: "Parameter" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Parameter",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateParameterRequest(proto.Message):
    r"""Message for updating a Parameter

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the Parameter resource by the update. The
            fields specified in the update_mask are relative to the
            resource, not the full request. A mutable field will be
            overwritten if it is in the mask. If the user does not
            provide a mask then all mutable fields present in the
            request will be overwritten.
        parameter (google.cloud.parametermanager_v1.types.Parameter):
            Required. The Parameter resource being
            updated
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    parameter: "Parameter" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Parameter",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteParameterRequest(proto.Message):
    r"""Message for deleting a Parameter

    Attributes:
        name (str):
            Required. Name of the resource in the format
            ``projects/*/locations/*/parameters/*``.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes after the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ParameterVersion(proto.Message):
    r"""Message describing ParameterVersion resource

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. [Output only] The resource name of the
            ParameterVersion in the format
            ``projects/*/locations/*/parameters/*/versions/*``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. [Output only] Create time stamp
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. [Output only] Update time stamp
        disabled (bool):
            Optional. Disabled boolean to determine if a
            ParameterVersion acts as a metadata only
            resource (payload is never returned if disabled
            is true). If true any calls will always default
            to BASIC view even if the user explicitly passes
            FULL view as part of the request. A render call
            on a disabled resource fails with an error.
            Default value is False.
        payload (google.cloud.parametermanager_v1.types.ParameterVersionPayload):
            Required. Immutable. Payload content of a
            ParameterVersion resource.  This is only
            returned when the request provides the View
            value of FULL (default for GET request).
        kms_key_version (str):
            Optional. Output only. [Output only] The resource name of
            the KMS key version used to encrypt the ParameterVersion
            payload. This field is populated only if the Parameter
            resource has customer managed encryption key (CMEK)
            configured.

            This field is a member of `oneof`_ ``_kms_key_version``.
        checksum_source (google.cloud.parametermanager_v1.types.ParameterVersion.ChecksumSource):
            Optional. Output only. [Output only] The source of the
            checksum.

            This field is a member of `oneof`_ ``_checksum_source``.
    """

    class ChecksumSource(proto.Enum):
        r"""The source of the checksum.

        Values:
            CHECKSUM_SOURCE_UNSPECIFIED (0):
                The default / unset value.
            SERVER_GENERATED (1):
                The checksum was generated by the server.
            USER_SPECIFIED (2):
                The checksum was provided by the user.
        """

        CHECKSUM_SOURCE_UNSPECIFIED = 0
        SERVER_GENERATED = 1
        USER_SPECIFIED = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    disabled: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    payload: "ParameterVersionPayload" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="ParameterVersionPayload",
    )
    kms_key_version: str = proto.Field(
        proto.STRING,
        number=6,
        optional=True,
    )
    checksum_source: ChecksumSource = proto.Field(
        proto.ENUM,
        number=7,
        optional=True,
        enum=ChecksumSource,
    )


class ParameterVersionPayload(proto.Message):
    r"""Message for storing a ParameterVersion resource's payload
    data


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        data (bytes):
            Required. bytes data for storing payload.
        data_crc32c (int):
            Optional. [Optional] The integrity checksum of the payload.
            If provided, the server will verify that the checksum
            matches the payload. If not provided, the server will
            generate the checksum.

            This field is a member of `oneof`_ ``_data_crc32c``.
    """

    data: bytes = proto.Field(
        proto.BYTES,
        number=1,
    )
    data_crc32c: int = proto.Field(
        proto.INT64,
        number=3,
        optional=True,
    )


class ListParameterVersionsRequest(proto.Message):
    r"""Message for requesting list of ParameterVersions

    Attributes:
        parent (str):
            Required. Parent value for ListParameterVersionsRequest in
            the format ``projects/*/locations/*/parameters/*``.
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListParameterVersions`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListParameterVersions`` must match the call that provided
            the page token.
        filter (str):
            Optional. Filtering results
        order_by (str):
            Optional. Hint for how to order the results
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


class ListParameterVersionsResponse(proto.Message):
    r"""Message for response to listing ParameterVersions

    Attributes:
        parameter_versions (MutableSequence[google.cloud.parametermanager_v1.types.ParameterVersion]):
            The list of ParameterVersions
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Unordered list. Locations that could not be
            reached.
    """

    @property
    def raw_page(self):
        return self

    parameter_versions: MutableSequence["ParameterVersion"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ParameterVersion",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetParameterVersionRequest(proto.Message):
    r"""Message for getting a ParameterVersion

    Attributes:
        name (str):
            Required. Name of the resource in the format
            ``projects/*/locations/*/parameters/*/versions/*``.
        view (google.cloud.parametermanager_v1.types.View):
            Optional. View of the ParameterVersion.
            In the default FULL view, all metadata & payload
            associated with the ParameterVersion will be
            returned.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    view: "View" = proto.Field(
        proto.ENUM,
        number=6,
        enum="View",
    )


class RenderParameterVersionRequest(proto.Message):
    r"""Message for getting a ParameterVersionRender

    Attributes:
        name (str):
            Required. Name of the resource
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class RenderParameterVersionResponse(proto.Message):
    r"""Message describing RenderParameterVersionResponse resource

    Attributes:
        parameter_version (str):
            Output only. Resource identifier of a ParameterVersion in
            the format
            ``projects/*/locations/*/parameters/*/versions/*``.
        payload (google.cloud.parametermanager_v1.types.ParameterVersionPayload):
            Payload content of a ParameterVersion
            resource.
        rendered_payload (bytes):
            Output only. Server generated rendered
            version of the user provided payload data
            (ParameterVersionPayload) which has
            substitutions of all (if any) references to a
            SecretManager SecretVersion resources. This
            substitution only works for a Parameter which is
            in JSON or YAML format.
    """

    parameter_version: str = proto.Field(
        proto.STRING,
        number=1,
    )
    payload: "ParameterVersionPayload" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ParameterVersionPayload",
    )
    rendered_payload: bytes = proto.Field(
        proto.BYTES,
        number=3,
    )


class CreateParameterVersionRequest(proto.Message):
    r"""Message for creating a ParameterVersion

    Attributes:
        parent (str):
            Required. Value for parent in the format
            ``projects/*/locations/*/parameters/*``.
        parameter_version_id (str):
            Required. Id of the ParameterVersion resource
        parameter_version (google.cloud.parametermanager_v1.types.ParameterVersion):
            Required. The ParameterVersion resource being
            created
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    parameter_version_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    parameter_version: "ParameterVersion" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="ParameterVersion",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateParameterVersionRequest(proto.Message):
    r"""Message for updating a ParameterVersion

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the ParameterVersion resource by the update.
            The fields specified in the update_mask are relative to the
            resource, not the full request. A mutable field will be
            overwritten if it is in the mask. If the user does not
            provide a mask then all mutable fields present in the
            request will be overwritten.
        parameter_version (google.cloud.parametermanager_v1.types.ParameterVersion):
            Required. The ParameterVersion resource being
            updated
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    parameter_version: "ParameterVersion" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ParameterVersion",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteParameterVersionRequest(proto.Message):
    r"""Message for deleting a ParameterVersion

    Attributes:
        name (str):
            Required. Name of the resource in the format
            ``projects/*/locations/*/parameters/*/versions/*``.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes after the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class Template(proto.Message):
    r"""Message describing Template resource

    Attributes:
        name (str):
            Identifier. The resource name of the Template in the format
            ``projects/*/locations/*/templates/*``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Create time stamp
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Update time stamp
        labels (MutableMapping[str, str]):
            Optional. Labels as key value pairs
        format_ (google.cloud.parametermanager_v1.types.TemplateFormat):
            Optional. Specifies the format of a Template.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    format_: "TemplateFormat" = proto.Field(
        proto.ENUM,
        number=5,
        enum="TemplateFormat",
    )


class ListTemplatesRequest(proto.Message):
    r"""Message for requesting list of Templates

    Attributes:
        parent (str):
            Required. Parent value for ListTemplatesRequest in the
            format ``projects/*/locations/*``.
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListTemplates`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListTemplates`` must match the call that provided the page
            token.
        filter (str):
            Optional. Filtering results
        order_by (str):
            Optional. Hint for how to order the results
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


class ListTemplatesResponse(proto.Message):
    r"""Message for response to listing Templates

    Attributes:
        templates (MutableSequence[google.cloud.parametermanager_v1.types.Template]):
            The list of Templates
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Unordered list. Locations that could not be
            reached.
    """

    @property
    def raw_page(self):
        return self

    templates: MutableSequence["Template"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Template",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetTemplateRequest(proto.Message):
    r"""Message for getting a Template

    Attributes:
        name (str):
            Required. Name of the resource in the format
            ``projects/*/locations/*/templates/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateTemplateRequest(proto.Message):
    r"""Message for creating a Template

    Attributes:
        parent (str):
            Required. Value for parent in the format
            ``projects/*/locations/*``.
        template_id (str):
            Required. Id of the Template resource
        template (google.cloud.parametermanager_v1.types.Template):
            Required. The Template resource being created
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    template_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    template: "Template" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Template",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateTemplateRequest(proto.Message):
    r"""Message for updating a Template

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the Template resource by the update. The
            fields specified in the update_mask are relative to the
            resource, not the full request. A mutable field will be
            overwritten if it is in the mask. If the user does not
            provide a mask then all mutable fields present in the
            request will be overwritten.
        template (google.cloud.parametermanager_v1.types.Template):
            Required. The Template resource being updated
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    template: "Template" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Template",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteTemplateRequest(proto.Message):
    r"""Message for deleting a Template

    Attributes:
        name (str):
            Required. Name of the resource in the format
            ``projects/*/locations/*/templates/*``.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes after the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class TemplateVersion(proto.Message):
    r"""Message describing TemplateVersion resource

    Attributes:
        name (str):
            Identifier. The resource name of the TemplateVersion in the
            format ``projects/*/locations/*/templates/*/versions/*``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Create time stamp
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Update time stamp
        disabled (bool):
            Optional. Disabled boolean to determine if a
            TemplateVersion acts as a metadata only resource
            (payload is never returned if disabled is true).
        payload (google.cloud.parametermanager_v1.types.TemplateVersionPayload):
            Required. Immutable. Payload content of a
            TemplateVersion resource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    disabled: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    payload: "TemplateVersionPayload" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="TemplateVersionPayload",
    )


class TemplateVersionPayload(proto.Message):
    r"""Message for storing a TemplateVersion resource's payload data

    Attributes:
        data (bytes):
            Required. bytes data for storing payload.
    """

    data: bytes = proto.Field(
        proto.BYTES,
        number=1,
    )


class ListTemplateVersionsRequest(proto.Message):
    r"""Message for requesting list of TemplateVersions

    Attributes:
        parent (str):
            Required. Parent value for ListTemplateVersionsRequest in
            the format ``projects/*/locations/*/templates/*``.
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListTemplateVersions`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListTemplateVersions`` must match the call that provided
            the page token.
        filter (str):
            Optional. Filtering results
        order_by (str):
            Optional. Hint for how to order the results
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


class ListTemplateVersionsResponse(proto.Message):
    r"""Message for response to listing TemplateVersions

    Attributes:
        template_versions (MutableSequence[google.cloud.parametermanager_v1.types.TemplateVersion]):
            The list of TemplateVersions
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Unordered list. Locations that could not be
            reached.
    """

    @property
    def raw_page(self):
        return self

    template_versions: MutableSequence["TemplateVersion"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="TemplateVersion",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetTemplateVersionRequest(proto.Message):
    r"""Message for getting a TemplateVersion

    Attributes:
        name (str):
            Required. Name of the resource in the format
            ``projects/*/locations/*/templates/*/versions/*``.
        view (google.cloud.parametermanager_v1.types.View):
            Optional. Specifies the view of the
            TemplateVersion to return. In the default FULL
            view, all metadata & payload associated with the
            TemplateVersion will be returned.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    view: "View" = proto.Field(
        proto.ENUM,
        number=2,
        enum="View",
    )


class CreateTemplateVersionRequest(proto.Message):
    r"""Message for creating a TemplateVersion

    Attributes:
        parent (str):
            Required. Value for parent in the format
            ``projects/*/locations/*/templates/*``.
        template_version_id (str):
            Required. Id of the TemplateVersion resource
        template_version (google.cloud.parametermanager_v1.types.TemplateVersion):
            Required. The TemplateVersion resource being
            created
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    template_version_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    template_version: "TemplateVersion" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="TemplateVersion",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateTemplateVersionRequest(proto.Message):
    r"""Message for updating a TemplateVersion

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the TemplateVersion resource by the update.
            The fields specified in the update_mask are relative to the
            resource, not the full request. A mutable field will be
            overwritten if it is in the mask. If the user does not
            provide a mask then all mutable fields present in the
            request will be overwritten.
        template_version (google.cloud.parametermanager_v1.types.TemplateVersion):
            Required. The TemplateVersion resource being
            updated
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    template_version: "TemplateVersion" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="TemplateVersion",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteTemplateVersionRequest(proto.Message):
    r"""Message for deleting a TemplateVersion

    Attributes:
        name (str):
            Required. Name of the resource in the format
            ``projects/*/locations/*/templates/*/versions/*``.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes after the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class RenderTemplateVersionRequest(proto.Message):
    r"""Message describing RenderTemplateVersionRequest resource

    Attributes:
        name (str):
            Required. Name of the resource
        parameter_version (str):
            Required. Parameter version used to render
            the template version.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    parameter_version: str = proto.Field(
        proto.STRING,
        number=2,
    )


class RenderTemplateVersionResponse(proto.Message):
    r"""Message describing RenderTemplateVersionResponse resource

    Attributes:
        template_version (str):
            Resource identifier of a TemplateVersion in the format
            ``projects/*/locations/*/templates/*/versions/*``.
        payload (google.cloud.parametermanager_v1.types.TemplateVersionPayload):
            Payload content of a TemplateVersion
            resource.
        rendered_payload (bytes):
            Output only. Server generated rendered
            version of the user provided payload data
            (TemplateVersionPayload) which has all the
            variables resolved using the provided parameter
            version.
        template_format (google.cloud.parametermanager_v1.types.TemplateFormat):
            Output only. Format of the template version.
        parameter_version (str):
            Output only. The resource name of the ParameterVersion used
            to render the template version in the format
            ``projects/*/locations/*/parameters/*/versions/*``.
    """

    template_version: str = proto.Field(
        proto.STRING,
        number=1,
    )
    payload: "TemplateVersionPayload" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="TemplateVersionPayload",
    )
    rendered_payload: bytes = proto.Field(
        proto.BYTES,
        number=3,
    )
    template_format: "TemplateFormat" = proto.Field(
        proto.ENUM,
        number=4,
        enum="TemplateFormat",
    )
    parameter_version: str = proto.Field(
        proto.STRING,
        number=5,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
