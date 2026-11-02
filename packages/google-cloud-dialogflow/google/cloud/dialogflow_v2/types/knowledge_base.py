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

__protobuf__ = proto.module(
    package="google.cloud.dialogflow.v2",
    manifest={
        "KnowledgeBase",
        "ListKnowledgeBasesRequest",
        "ListKnowledgeBasesResponse",
        "GetKnowledgeBaseRequest",
        "CreateKnowledgeBaseRequest",
        "DeleteKnowledgeBaseRequest",
        "UpdateKnowledgeBaseRequest",
    },
)


class KnowledgeBase(proto.Message):
    r"""A knowledge base represents a collection of knowledge documents that
    you provide to Dialogflow. Your knowledge documents contain
    information that may be useful during conversations with end-users.
    Some Dialogflow features use knowledge bases when looking for a
    response to an end-user input.

    For more information, see the `knowledge base
    guide <https://cloud.google.com/dialogflow/docs/how/knowledge-bases>`__.

    Note: The ``projects.agent.knowledgeBases`` resource is deprecated;
    only use ``projects.knowledgeBases``.

    Attributes:
        name (str):
            The knowledge base resource name. The name must be empty
            when creating a knowledge base. Format:
            ``projects/<Project ID>/locations/<Location ID>/knowledgeBases/<Knowledge Base ID>``.
        display_name (str):
            Required. The display name of the knowledge
            base. The name must be 1024 bytes or less;
            otherwise, the creation request fails.
        language_code (str):
            Language which represents the KnowledgeBase.
            When the KnowledgeBase is created/updated,
            expect this to be present for non en-us
            languages. When unspecified, the default
            language code en-us applies.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListKnowledgeBasesRequest(proto.Message):
    r"""Request message for
    [KnowledgeBases.ListKnowledgeBases][google.cloud.dialogflow.v2.KnowledgeBases.ListKnowledgeBases].

    Attributes:
        parent (str):
            Required. The project to list of knowledge bases for.
            Format: ``projects/<Project ID>/locations/<Location ID>``.
        page_size (int):
            The maximum number of items to return in a
            single page. By default 10 and at most 100.
        page_token (str):
            The next_page_token value returned from a previous list
            request.
        filter (str):
            The filter expression used to filter knowledge bases
            returned by the list method. The expression has the
            following syntax:

            [AND ] ...

            The following fields and operators are supported:

            - display_name with has(:) operator
            - language_code with equals(=) operator

            Examples:

            - 'language_code=en-us' matches knowledge bases with en-us
              language code.
            - 'display_name:articles' matches knowledge bases whose
              display name contains "articles".
            - 'display_name:"Best Articles"' matches knowledge bases
              whose display name contains "Best Articles".
            - 'language_code=en-gb AND display_name=articles' matches
              all knowledge bases whose display name contains "articles"
              and whose language code is "en-gb".

            Note: An empty filter string (i.e. "") is a no-op and will
            result in no filtering.

            For more information about filtering, see `API
            Filtering <https://aip.dev/160>`__.
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


class ListKnowledgeBasesResponse(proto.Message):
    r"""Response message for
    [KnowledgeBases.ListKnowledgeBases][google.cloud.dialogflow.v2.KnowledgeBases.ListKnowledgeBases].

    Attributes:
        knowledge_bases (MutableSequence[google.cloud.dialogflow_v2.types.KnowledgeBase]):
            The list of knowledge bases.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    knowledge_bases: MutableSequence["KnowledgeBase"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="KnowledgeBase",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetKnowledgeBaseRequest(proto.Message):
    r"""Request message for
    [KnowledgeBases.GetKnowledgeBase][google.cloud.dialogflow.v2.KnowledgeBases.GetKnowledgeBase].

    Attributes:
        name (str):
            Required. The name of the knowledge base to retrieve. Format
            ``projects/<Project ID>/locations/<Location ID>/knowledgeBases/<Knowledge Base ID>``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateKnowledgeBaseRequest(proto.Message):
    r"""Request message for
    [KnowledgeBases.CreateKnowledgeBase][google.cloud.dialogflow.v2.KnowledgeBases.CreateKnowledgeBase].

    Attributes:
        parent (str):
            Required. The project to create a knowledge base for.
            Format: ``projects/<Project ID>/locations/<Location ID>``.
        knowledge_base (google.cloud.dialogflow_v2.types.KnowledgeBase):
            Required. The knowledge base to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    knowledge_base: "KnowledgeBase" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="KnowledgeBase",
    )


class DeleteKnowledgeBaseRequest(proto.Message):
    r"""Request message for
    [KnowledgeBases.DeleteKnowledgeBase][google.cloud.dialogflow.v2.KnowledgeBases.DeleteKnowledgeBase].

    Attributes:
        name (str):
            Required. The name of the knowledge base to delete. Format:
            ``projects/<Project ID>/locations/<Location ID>/knowledgeBases/<Knowledge Base ID>``.
        force (bool):
            Optional. Force deletes the knowledge base.
            When set to true, any documents in the knowledge
            base are also deleted.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class UpdateKnowledgeBaseRequest(proto.Message):
    r"""Request message for
    [KnowledgeBases.UpdateKnowledgeBase][google.cloud.dialogflow.v2.KnowledgeBases.UpdateKnowledgeBase].

    Attributes:
        knowledge_base (google.cloud.dialogflow_v2.types.KnowledgeBase):
            Required. The knowledge base to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Not specified means ``update all``. Currently,
            only ``display_name`` can be updated, an InvalidArgument
            will be returned for attempting to update other fields.
    """

    knowledge_base: "KnowledgeBase" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="KnowledgeBase",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
