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

from google.cloud.contentwarehouse_v1.types import common, document

__protobuf__ = proto.module(
    package="google.cloud.contentwarehouse.v1",
    manifest={
        "ListLinkedTargetsResponse",
        "ListLinkedTargetsRequest",
        "ListLinkedSourcesResponse",
        "ListLinkedSourcesRequest",
        "DocumentLink",
        "CreateDocumentLinkRequest",
        "DeleteDocumentLinkRequest",
    },
)


class ListLinkedTargetsResponse(proto.Message):
    r"""Response message for DocumentLinkService.ListLinkedTargets.

    Attributes:
        document_links (MutableSequence[google.cloud.contentwarehouse_v1.types.DocumentLink]):
            Target document-links.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    document_links: MutableSequence["DocumentLink"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="DocumentLink",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListLinkedTargetsRequest(proto.Message):
    r"""Request message for DocumentLinkService.ListLinkedTargets.

    Attributes:
        parent (str):
            Required. The name of the document, for which all target
            links are returned. Format:
            projects/{project_number}/locations/{location}/documents/{target_document_id}.
        request_metadata (google.cloud.contentwarehouse_v1.types.RequestMetadata):
            The meta information collected about the
            document creator, used to enforce access control
            for the service.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_metadata: common.RequestMetadata = proto.Field(
        proto.MESSAGE,
        number=2,
        message=common.RequestMetadata,
    )


class ListLinkedSourcesResponse(proto.Message):
    r"""Response message for DocumentLinkService.ListLinkedSources.

    Attributes:
        document_links (MutableSequence[google.cloud.contentwarehouse_v1.types.DocumentLink]):
            Source document-links.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    document_links: MutableSequence["DocumentLink"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="DocumentLink",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListLinkedSourcesRequest(proto.Message):
    r"""Response message for DocumentLinkService.ListLinkedSources.

    Attributes:
        parent (str):
            Required. The name of the document, for which all source
            links are returned. Format:
            projects/{project_number}/locations/{location}/documents/{source_document_id}.
        page_size (int):
            The maximum number of document-links to
            return. The service may return fewer than this
            value.

            If unspecified, at most 50 document-links will
            be returned. The maximum value is 1000; values
            above 1000 will be coerced to 1000.
        page_token (str):
            A page token, received from a previous ``ListLinkedSources``
            call. Provide this to retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``ListLinkedSources`` must match the call that provided the
            page token.
        request_metadata (google.cloud.contentwarehouse_v1.types.RequestMetadata):
            The meta information collected about the
            document creator, used to enforce access control
            for the service.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )
    request_metadata: common.RequestMetadata = proto.Field(
        proto.MESSAGE,
        number=2,
        message=common.RequestMetadata,
    )


class DocumentLink(proto.Message):
    r"""A document-link between source and target document.

    Attributes:
        name (str):
            Name of this document-link. It is required that the parent
            derived form the name to be consistent with the source
            document reference. Otherwise an exception will be thrown.
            Format:
            projects/{project_number}/locations/{location}/documents/{source_document_id}/documentLinks/{document_link_id}.
        source_document_reference (google.cloud.contentwarehouse_v1.types.DocumentReference):
            Document references of the source document.
        target_document_reference (google.cloud.contentwarehouse_v1.types.DocumentReference):
            Document references of the target document.
        description (str):
            Description of this document-link.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the documentLink
            is last updated.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the documentLink
            is created.
        state (google.cloud.contentwarehouse_v1.types.DocumentLink.State):
            The state of the documentlink. If target node
            has been deleted, the link is marked as invalid.
            Removing a source node will result in removal of
            all associated links.
    """

    class State(proto.Enum):
        r"""The state of a document-link.

        Values:
            STATE_UNSPECIFIED (0):
                Unknown state of documentlink.
            ACTIVE (1):
                The documentlink has both source and target
                documents detected.
            SOFT_DELETED (2):
                Target document is deleted, and mark the
                documentlink as soft-deleted.
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        SOFT_DELETED = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    source_document_reference: document.DocumentReference = proto.Field(
        proto.MESSAGE,
        number=2,
        message=document.DocumentReference,
    )
    target_document_reference: document.DocumentReference = proto.Field(
        proto.MESSAGE,
        number=3,
        message=document.DocumentReference,
    )
    description: str = proto.Field(
        proto.STRING,
        number=4,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=7,
        enum=State,
    )


class CreateDocumentLinkRequest(proto.Message):
    r"""Request message for DocumentLinkService.CreateDocumentLink.

    Attributes:
        parent (str):
            Required. Parent of the document-link to be created. parent
            of document-link should be a document. Format:
            projects/{project_number}/locations/{location}/documents/{source_document_id}.
        document_link (google.cloud.contentwarehouse_v1.types.DocumentLink):
            Required. Document links associated with the source
            documents (source_document_id).
        request_metadata (google.cloud.contentwarehouse_v1.types.RequestMetadata):
            The meta information collected about the
            document creator, used to enforce access control
            for the service.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    document_link: "DocumentLink" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="DocumentLink",
    )
    request_metadata: common.RequestMetadata = proto.Field(
        proto.MESSAGE,
        number=3,
        message=common.RequestMetadata,
    )


class DeleteDocumentLinkRequest(proto.Message):
    r"""Request message for DocumentLinkService.DeleteDocumentLink.

    Attributes:
        name (str):
            Required. The name of the document-link to be deleted.
            Format:
            projects/{project_number}/locations/{location}/documents/{source_document_id}/documentLinks/{document_link_id}.
        request_metadata (google.cloud.contentwarehouse_v1.types.RequestMetadata):
            The meta information collected about the
            document creator, used to enforce access control
            for the service.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_metadata: common.RequestMetadata = proto.Field(
        proto.MESSAGE,
        number=2,
        message=common.RequestMetadata,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
