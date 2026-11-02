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

from google.cloud.cloudsecuritycompliance_v1.types import common

__protobuf__ = proto.module(
    package="google.cloud.cloudsecuritycompliance.v1",
    manifest={
        "ListFrameworksRequest",
        "ListFrameworksResponse",
        "GetFrameworkRequest",
        "CreateFrameworkRequest",
        "UpdateFrameworkRequest",
        "DeleteFrameworkRequest",
        "ListCloudControlsRequest",
        "ListCloudControlsResponse",
        "GetCloudControlRequest",
        "CreateCloudControlRequest",
        "UpdateCloudControlRequest",
        "DeleteCloudControlRequest",
    },
)


class ListFrameworksRequest(proto.Message):
    r"""Request message for [ListFrameworks][].

    Attributes:
        parent (str):
            Required. The parent resource name, in one of the following
            formats:

            - ``organizations/{organization}/locations/{location}``
            - ``projects/{project}/locations/{location}``.

            The only supported location is ``global``.
        page_size (int):
            Optional. The maximum number of frameworks to return. The
            default value is ``500``.

            If you exceed the maximum value of ``1000``, then the
            service uses the maximum value.
        page_token (str):
            Optional. A pagination token returned from a
            previous request to list frameworks. Provide
            this token to retrieve the next page of results.
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


class ListFrameworksResponse(proto.Message):
    r"""The response message for [ListFrameworks][]. Returns a paginated
    list of Framework resources.

    Attributes:
        frameworks (MutableSequence[google.cloud.cloudsecuritycompliance_v1.types.Framework]):
            The list of framework resources.
        next_page_token (str):
            A pagination token. To retrieve the next page
            of results, call the method again with this
            token.
    """

    @property
    def raw_page(self):
        return self

    frameworks: MutableSequence[common.Framework] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=common.Framework,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetFrameworkRequest(proto.Message):
    r"""The request message for [GetFramework][].

    Attributes:
        name (str):
            Required. The name of the framework to retrieve, in one of
            the following formats:
            ``organizations/{organization}/locations/{location}/frameworks/{framework}``
            or
            ``projects/{project}/locations/{location}/frameworks/{framework}``.

            The only supported location is ``global``.
        major_revision_id (int):
            Optional. The framework major version to retrieve. If not
            specified, the most recently updated ``revision_id`` is
            retrieved.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    major_revision_id: int = proto.Field(
        proto.INT64,
        number=2,
    )


class CreateFrameworkRequest(proto.Message):
    r"""The request message for [CreateFramework][].

    Attributes:
        parent (str):
            Required. The parent resource name, in one of the following
            formats:

            - ``organizations/{organization}/locations/{location}``
            - ``projects/{project}/locations/{location}``.

            The only supported location is ``global``.
        framework_id (str):
            Required. The identifier (ID) of the
            framework. The ID is not the full name of the
            framework; it's the last part of the full name
            of the framework.
        framework (google.cloud.cloudsecuritycompliance_v1.types.Framework):
            Required. The resource being created.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    framework_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    framework: common.Framework = proto.Field(
        proto.MESSAGE,
        number=3,
        message=common.Framework,
    )


class UpdateFrameworkRequest(proto.Message):
    r"""The request message for [UpdateFramework][].

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. A field mask is used to specify the fields to be
            overwritten in the framework resource by the update. The
            fields specified in the ``update_mask`` are relative to the
            resource, not the full request. A field is overwritten if it
            is in the mask. If you don't provide a mask then all fields
            present in the request will be overwritten.
        framework (google.cloud.cloudsecuritycompliance_v1.types.Framework):
            Required. The resource that is being updated.
        major_revision_id (int):
            Optional. The major version ID of the
            framework to update.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    framework: common.Framework = proto.Field(
        proto.MESSAGE,
        number=2,
        message=common.Framework,
    )
    major_revision_id: int = proto.Field(
        proto.INT64,
        number=3,
    )


class DeleteFrameworkRequest(proto.Message):
    r"""Request message for [DeleteFramework][].

    Attributes:
        name (str):
            Required. The name of the resource, in one of the following
            formats:
            ``organizations/{organization}/locations/{location}/frameworks/{framework}``
            or
            ``projects/{project}/locations/{location}/frameworks/{framework}``.

            The only supported location is ``global``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListCloudControlsRequest(proto.Message):
    r"""Request message for [ListCloudControls][].

    Attributes:
        parent (str):
            Required. The parent resource name, in one of the following
            formats:

            - ``organizations/{organization}/locations/{location}``
            - ``projects/{project}/locations/{location}``.

            The only supported location is ``global``.
        page_size (int):
            Optional. The maximum number of cloud controls to return.
            The default value is ``500``.

            If you exceed the maximum value of ``1000``, then the
            service uses the maximum value.
        page_token (str):
            Optional. A pagination token that's returned from a previous
            request to list cloud controls. Provide this token to
            retrieve the next page of results.

            When paginating, the parent that you provide to the
            [ListCloudControls][google.cloud.cloudsecuritycompliance.v1.Config.ListCloudControls]
            request must match the call that provided the page token.
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


class ListCloudControlsResponse(proto.Message):
    r"""The response message for [ListCloudControls][].

    Attributes:
        cloud_controls (MutableSequence[google.cloud.cloudsecuritycompliance_v1.types.CloudControl]):
            The list of CloudControl resources.
        next_page_token (str):
            A pagination token. To retrieve the next page
            of results, call the method again with this
            token.
    """

    @property
    def raw_page(self):
        return self

    cloud_controls: MutableSequence[common.CloudControl] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=common.CloudControl,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetCloudControlRequest(proto.Message):
    r"""The request message for [GetCloudControl][].

    Attributes:
        name (str):
            Required. The name of the cloud control to retrieve, in one
            of the following formats:
            ``organizations/{organization}/locations/{location}/cloudControls/{cloud_control}``
            or
            ``projects/{project}/locations/{location}/cloudControls/{cloud_control}``.

            The only supported location is ``global``.
        major_revision_id (int):
            Optional. The major version of the cloud control to
            retrieve. If not specified, the most recently updated
            ``revision_id`` is retrieved.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    major_revision_id: int = proto.Field(
        proto.INT64,
        number=2,
    )


class CreateCloudControlRequest(proto.Message):
    r"""The request message for [CreateCloudControl][].

    Attributes:
        parent (str):
            Required. The parent resource name, in one of the following
            formats:

            - ``organizations/{organization}/locations/{location}``.
            - ``projects/{project}/locations/{location}``.

            The only supported location is ``global``.
        cloud_control_id (str):
            Required. The identifier for the cloud control, which is the
            last segment of the cloud control name. The format is
            ``^[a-zA-Z][a-zA-Z0-9-]{0,61}[a-zA-Z0-9]$``.
        cloud_control (google.cloud.cloudsecuritycompliance_v1.types.CloudControl):
            Required. The cloud control that's being
            created.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    cloud_control_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    cloud_control: common.CloudControl = proto.Field(
        proto.MESSAGE,
        number=3,
        message=common.CloudControl,
    )


class UpdateCloudControlRequest(proto.Message):
    r"""The request message for [UpdateCloudControl][].

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Use a field mask to specify the fields to be
            overwritten in the cloud control during the update. The
            fields that you specify in the ``update_mask`` are relative
            to the cloud control, not the full request. A field is
            overwritten if it is in the mask. If you don't provide a
            mask, all fields in the request are updated.

            You can update the following fields:

            - Display name
            - Description
            - Parameters
            - Rules
            - Parameter specification
        cloud_control (google.cloud.cloudsecuritycompliance_v1.types.CloudControl):
            Required. The cloud control that you're
            updating.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    cloud_control: common.CloudControl = proto.Field(
        proto.MESSAGE,
        number=2,
        message=common.CloudControl,
    )


class DeleteCloudControlRequest(proto.Message):
    r"""The request message for [DeleteCloudControl][].

    Attributes:
        name (str):
            Required. The name of the cloud control to delete, in one of
            the following formats:
            ``organizations/{organization}/locations/{location}/CloudControls/{CloudControl}``
            or
            ``projects/{project}/locations/{location}/CloudControls/{CloudControl}``.

            The only supported location is ``global``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
