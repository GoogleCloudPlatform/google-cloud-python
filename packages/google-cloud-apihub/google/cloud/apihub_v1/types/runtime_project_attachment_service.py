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

__protobuf__ = proto.module(
    package="google.cloud.apihub.v1",
    manifest={
        "CreateRuntimeProjectAttachmentRequest",
        "GetRuntimeProjectAttachmentRequest",
        "ListRuntimeProjectAttachmentsRequest",
        "ListRuntimeProjectAttachmentsResponse",
        "DeleteRuntimeProjectAttachmentRequest",
        "LookupRuntimeProjectAttachmentRequest",
        "LookupRuntimeProjectAttachmentResponse",
        "RuntimeProjectAttachment",
    },
)


class CreateRuntimeProjectAttachmentRequest(proto.Message):
    r"""The
    [CreateRuntimeProjectAttachment][google.cloud.apihub.v1.RuntimeProjectAttachmentService.CreateRuntimeProjectAttachment]
    method's request.

    Attributes:
        parent (str):
            Required. The parent resource for the Runtime Project
            Attachment. Format:
            ``projects/{project}/locations/{location}``
        runtime_project_attachment_id (str):
            Required. The ID to use for the Runtime Project Attachment,
            which will become the final component of the Runtime Project
            Attachment's name. The ID must be the same as the project ID
            of the Google cloud project specified in the
            runtime_project_attachment.runtime_project field.
        runtime_project_attachment (google.cloud.apihub_v1.types.RuntimeProjectAttachment):
            Required. The Runtime Project Attachment to
            create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    runtime_project_attachment_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    runtime_project_attachment: "RuntimeProjectAttachment" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="RuntimeProjectAttachment",
    )


class GetRuntimeProjectAttachmentRequest(proto.Message):
    r"""The
    [GetRuntimeProjectAttachment][google.cloud.apihub.v1.RuntimeProjectAttachmentService.GetRuntimeProjectAttachment]
    method's request.

    Attributes:
        name (str):
            Required. The name of the API resource to retrieve. Format:
            ``projects/{project}/locations/{location}/runtimeProjectAttachments/{runtime_project_attachment}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListRuntimeProjectAttachmentsRequest(proto.Message):
    r"""The
    [ListRuntimeProjectAttachments][google.cloud.apihub.v1.RuntimeProjectAttachmentService.ListRuntimeProjectAttachments]
    method's request.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of runtime
            project attachments. Format:
            ``projects/{project}/locations/{location}``
        page_size (int):
            Optional. The maximum number of runtime
            project attachments to return. The service may
            return fewer than this value. If unspecified, at
            most 50 runtime project attachments will be
            returned. The maximum value is 1000; values
            above 1000 will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListRuntimeProjectAttachments`` call. Provide this to
            retrieve the subsequent page.

            When paginating, all other parameters (except page_size)
            provided to ``ListRuntimeProjectAttachments`` must match the
            call that provided the page token.
        filter (str):
            Optional. An expression that filters the list of
            RuntimeProjectAttachments.

            A filter expression consists of a field name, a comparison
            operator, and a value for filtering. The value must be a
            string. All standard operators as documented at
            https://google.aip.dev/160 are supported.

            The following fields in the ``RuntimeProjectAttachment`` are
            eligible for filtering:

            - ``name`` - The name of the RuntimeProjectAttachment.
            - ``create_time`` - The time at which the
              RuntimeProjectAttachment was created. The value should be
              in the (RFC3339)[https://tools.ietf.org/html/rfc3339]
              format.
            - ``runtime_project`` - The Google cloud project associated
              with the RuntimeProjectAttachment.
        order_by (str):
            Optional. Hint for how to order the results.
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


class ListRuntimeProjectAttachmentsResponse(proto.Message):
    r"""The
    [ListRuntimeProjectAttachments][google.cloud.apihub.v1.RuntimeProjectAttachmentService.ListRuntimeProjectAttachments]
    method's response.

    Attributes:
        runtime_project_attachments (MutableSequence[google.cloud.apihub_v1.types.RuntimeProjectAttachment]):
            List of runtime project attachments.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    runtime_project_attachments: MutableSequence["RuntimeProjectAttachment"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="RuntimeProjectAttachment",
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteRuntimeProjectAttachmentRequest(proto.Message):
    r"""The
    [DeleteRuntimeProjectAttachment][google.cloud.apihub.v1.RuntimeProjectAttachmentService.DeleteRuntimeProjectAttachment]
    method's request.

    Attributes:
        name (str):
            Required. The name of the Runtime Project Attachment to
            delete. Format:
            ``projects/{project}/locations/{location}/runtimeProjectAttachments/{runtime_project_attachment}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class LookupRuntimeProjectAttachmentRequest(proto.Message):
    r"""The
    [LookupRuntimeProjectAttachment][google.cloud.apihub.v1.RuntimeProjectAttachmentService.LookupRuntimeProjectAttachment]
    method's request.

    Attributes:
        name (str):
            Required. Runtime project ID to look up runtime project
            attachment for. Lookup happens across all regions. Expected
            format: ``projects/{project}/locations/{location}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class LookupRuntimeProjectAttachmentResponse(proto.Message):
    r"""The
    [ListRuntimeProjectAttachments][google.cloud.apihub.v1.RuntimeProjectAttachmentService.ListRuntimeProjectAttachments]
    method's response.

    Attributes:
        runtime_project_attachment (google.cloud.apihub_v1.types.RuntimeProjectAttachment):
            Runtime project attachment for a project if
            exists, empty otherwise.
    """

    runtime_project_attachment: "RuntimeProjectAttachment" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="RuntimeProjectAttachment",
    )


class RuntimeProjectAttachment(proto.Message):
    r"""Runtime project attachment represents an attachment from the
    runtime project to the host project. Api Hub looks for
    deployments in the attached runtime projects and creates
    corresponding resources in Api Hub for the discovered
    deployments.

    Attributes:
        name (str):
            Identifier. The resource name of a runtime project
            attachment. Format:
            "projects/{project}/locations/{location}/runtimeProjectAttachments/{runtime_project_attachment}".
        runtime_project (str):
            Required. Immutable. Google cloud project
            name in the format: "projects/abc" or
            "projects/123". As input, project name with
            either project id or number are accepted. As
            output, this field will contain project number.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Create time.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    runtime_project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
