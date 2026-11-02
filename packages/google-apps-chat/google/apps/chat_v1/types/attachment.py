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

import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.chat.v1",
    manifest={
        "Attachment",
        "DriveDataRef",
        "AttachmentDataRef",
        "GetAttachmentRequest",
        "UploadAttachmentRequest",
        "UploadAttachmentResponse",
    },
)


class Attachment(proto.Message):
    r"""An attachment in Google Chat.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. Resource name of the attachment.

            Format:
            ``spaces/{space}/messages/{message}/attachments/{attachment}``.
        content_name (str):
            Output only. The original file name for the
            content, not the full path.
        content_type (str):
            Output only. The content type (MIME type) of
            the file.
        attachment_data_ref (google.apps.chat_v1.types.AttachmentDataRef):
            Optional. A reference to the attachment data.
            This field is used to create or update messages
            with attachments, or with the media API to
            download the attachment data.

            This field is a member of `oneof`_ ``data_ref``.
        drive_data_ref (google.apps.chat_v1.types.DriveDataRef):
            Output only. A reference to the Google Drive
            attachment. This field is used with the Google
            Drive API.

            This field is a member of `oneof`_ ``data_ref``.
        thumbnail_uri (str):
            Output only. The thumbnail URL which should
            be used to preview the attachment to a human
            user. Chat apps shouldn't use this URL to
            download attachment content.
        download_uri (str):
            Output only. The download URL which should be
            used to allow a human user to download the
            attachment. Chat apps shouldn't use this URL to
            download attachment content.
        source (google.apps.chat_v1.types.Attachment.Source):
            Output only. The source of the attachment.
    """

    class Source(proto.Enum):
        r"""The source of the attachment.

        Values:
            SOURCE_UNSPECIFIED (0):
                Reserved.
            DRIVE_FILE (1):
                The file is a Google Drive file.
            UPLOADED_CONTENT (2):
                The file is uploaded to Chat.
        """

        SOURCE_UNSPECIFIED = 0
        DRIVE_FILE = 1
        UPLOADED_CONTENT = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    content_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    content_type: str = proto.Field(
        proto.STRING,
        number=3,
    )
    attachment_data_ref: "AttachmentDataRef" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="data_ref",
        message="AttachmentDataRef",
    )
    drive_data_ref: "DriveDataRef" = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="data_ref",
        message="DriveDataRef",
    )
    thumbnail_uri: str = proto.Field(
        proto.STRING,
        number=5,
    )
    download_uri: str = proto.Field(
        proto.STRING,
        number=6,
    )
    source: Source = proto.Field(
        proto.ENUM,
        number=9,
        enum=Source,
    )


class DriveDataRef(proto.Message):
    r"""A reference to the data of a drive attachment.

    Attributes:
        drive_file_id (str):
            The ID for the drive file. Use with the Drive
            API.
    """

    drive_file_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class AttachmentDataRef(proto.Message):
    r"""A reference to the attachment data.

    Attributes:
        resource_name (str):
            Optional. The resource name of the attachment
            data. This field is used with the media API to
            download the attachment data.
        attachment_upload_token (str):
            Optional. Opaque token containing a reference
            to an uploaded attachment. Treated by clients as
            an opaque string and used to create or update
            Chat messages with attachments.
    """

    resource_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    attachment_upload_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetAttachmentRequest(proto.Message):
    r"""Request to get an attachment.

    Attributes:
        name (str):
            Required. Resource name of the attachment, in the form
            ``spaces/{space}/messages/{message}/attachments/{attachment}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UploadAttachmentRequest(proto.Message):
    r"""Request to upload an attachment.

    Attributes:
        parent (str):
            Required. Resource name of the Chat space in
            which the attachment is uploaded. Format
            "spaces/{space}".
        filename (str):
            Required. The filename of the attachment,
            including the file extension.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filename: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UploadAttachmentResponse(proto.Message):
    r"""Response of uploading an attachment.

    Attributes:
        attachment_data_ref (google.apps.chat_v1.types.AttachmentDataRef):
            Reference to the uploaded attachment.
    """

    attachment_data_ref: "AttachmentDataRef" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="AttachmentDataRef",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
