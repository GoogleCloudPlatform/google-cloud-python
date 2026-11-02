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
    package="google.devtools.artifactregistry.v1",
    manifest={
        "Attachment",
        "ListAttachmentsRequest",
        "ListAttachmentsResponse",
        "GetAttachmentRequest",
        "CreateAttachmentRequest",
        "DeleteAttachmentRequest",
    },
)


class Attachment(proto.Message):
    r"""An Attachment refers to additional metadata that can be
    attached to artifacts in Artifact Registry. An attachment
    consists of one or more files.

    Attributes:
        name (str):
            The name of the attachment. E.g.
            ``projects/p1/locations/us/repositories/repo/attachments/sbom``.
        target (str):
            Required. The target the attachment is for, can be a
            Version, Package or Repository. E.g.
            ``projects/p1/locations/us-central1/repositories/repo1/packages/p1/versions/v1``.
        type_ (str):
            Type of attachment. E.g. ``application/vnd.spdx+json``
        attachment_namespace (str):
            The namespace this attachment belongs to. E.g. If an
            attachment is created by artifact analysis, namespace is set
            to ``artifactanalysis.googleapis.com``.
        annotations (MutableMapping[str, str]):
            Optional. User annotations. These attributes
            can only be set and used by the user, and not by
            Artifact Registry. See
            https://google.aip.dev/128#annotations for more
            details such as format and size limitations.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the attachment was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the attachment was
            last updated.
        files (MutableSequence[str]):
            Required. The files that belong to this attachment. If the
            file ID part contains slashes, they are escaped. E.g.
            ``projects/p1/locations/us-central1/repositories/repo1/files/sha:<sha-of-file>``.
        oci_version_name (str):
            Output only. The name of the OCI version that this
            attachment created. Only populated for Docker attachments.
            E.g.
            ``projects/p1/locations/us-central1/repositories/repo1/packages/p1/versions/v1``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    target: str = proto.Field(
        proto.STRING,
        number=2,
    )
    type_: str = proto.Field(
        proto.STRING,
        number=3,
    )
    attachment_namespace: str = proto.Field(
        proto.STRING,
        number=4,
    )
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
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
    files: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=8,
    )
    oci_version_name: str = proto.Field(
        proto.STRING,
        number=9,
    )


class ListAttachmentsRequest(proto.Message):
    r"""The request to list attachments.

    Attributes:
        parent (str):
            Required. The name of the parent resource
            whose attachments will be listed.
        filter (str):
            Optional. An expression for filtering the results of the
            request. Filter rules are case insensitive. The fields
            eligible for filtering are:

            - ``target``
            - ``type``
            - ``attachment_namespace``
        page_size (int):
            The maximum number of attachments to return.
            Maximum page size is 1,000.
        page_token (str):
            The next_page_token value returned from a previous list
            request, if any.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
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


class ListAttachmentsResponse(proto.Message):
    r"""The response from listing attachments.

    Attributes:
        attachments (MutableSequence[google.cloud.artifactregistry_v1.types.Attachment]):
            The attachments returned.
        next_page_token (str):
            The token to retrieve the next page of
            attachments, or empty if there are no more
            attachments to return.
    """

    @property
    def raw_page(self):
        return self

    attachments: MutableSequence["Attachment"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Attachment",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetAttachmentRequest(proto.Message):
    r"""The request to retrieve an attachment.

    Attributes:
        name (str):
            Required. The name of the attachment to
            retrieve.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateAttachmentRequest(proto.Message):
    r"""The request to create a new attachment.

    Attributes:
        parent (str):
            Required. The name of the parent resource
            where the attachment will be created.
        attachment_id (str):
            Required. The attachment id to use for this
            attachment.
        attachment (google.cloud.artifactregistry_v1.types.Attachment):
            Required. The attachment to be created.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    attachment_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    attachment: "Attachment" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Attachment",
    )


class DeleteAttachmentRequest(proto.Message):
    r"""The request to delete an attachment.

    Attributes:
        name (str):
            Required. The name of the attachment to
            delete.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
