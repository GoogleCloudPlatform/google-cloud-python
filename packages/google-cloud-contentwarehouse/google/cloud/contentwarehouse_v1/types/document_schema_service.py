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

from google.cloud.contentwarehouse_v1.types import (
    document_schema as gcc_document_schema,
)

__protobuf__ = proto.module(
    package="google.cloud.contentwarehouse.v1",
    manifest={
        "CreateDocumentSchemaRequest",
        "GetDocumentSchemaRequest",
        "UpdateDocumentSchemaRequest",
        "DeleteDocumentSchemaRequest",
        "ListDocumentSchemasRequest",
        "ListDocumentSchemasResponse",
    },
)


class CreateDocumentSchemaRequest(proto.Message):
    r"""Request message for
    DocumentSchemaService.CreateDocumentSchema.

    Attributes:
        parent (str):
            Required. The parent name.
        document_schema (google.cloud.contentwarehouse_v1.types.DocumentSchema):
            Required. The document schema to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    document_schema: gcc_document_schema.DocumentSchema = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcc_document_schema.DocumentSchema,
    )


class GetDocumentSchemaRequest(proto.Message):
    r"""Request message for DocumentSchemaService.GetDocumentSchema.

    Attributes:
        name (str):
            Required. The name of the document schema to
            retrieve.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateDocumentSchemaRequest(proto.Message):
    r"""Request message for
    DocumentSchemaService.UpdateDocumentSchema.

    Attributes:
        name (str):
            Required. The name of the document schema to update. Format:
            projects/{project_number}/locations/{location}/documentSchemas/{document_schema_id}.
        document_schema (google.cloud.contentwarehouse_v1.types.DocumentSchema):
            Required. The document schema to update with.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    document_schema: gcc_document_schema.DocumentSchema = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcc_document_schema.DocumentSchema,
    )


class DeleteDocumentSchemaRequest(proto.Message):
    r"""Request message for
    DocumentSchemaService.DeleteDocumentSchema.

    Attributes:
        name (str):
            Required. The name of the document schema to
            delete.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListDocumentSchemasRequest(proto.Message):
    r"""Request message for
    DocumentSchemaService.ListDocumentSchemas.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of document
            schemas. Format:
            projects/{project_number}/locations/{location}.
        page_size (int):
            The maximum number of document schemas to
            return. The service may return fewer than this
            value. If unspecified, at most 50 document
            schemas will be returned. The maximum value is
            1000; values above 1000 will be coerced to 1000.
        page_token (str):
            A page token, received from a previous
            ``ListDocumentSchemas`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListDocumentSchemas`` must match the call that provided
            the page token.
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


class ListDocumentSchemasResponse(proto.Message):
    r"""Response message for
    DocumentSchemaService.ListDocumentSchemas.

    Attributes:
        document_schemas (MutableSequence[google.cloud.contentwarehouse_v1.types.DocumentSchema]):
            The document schemas from the specified
            parent.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    document_schemas: MutableSequence[gcc_document_schema.DocumentSchema] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=gcc_document_schema.DocumentSchema,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
