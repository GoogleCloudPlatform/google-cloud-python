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

from google.cloud.contentwarehouse_v1.types import synonymset

__protobuf__ = proto.module(
    package="google.cloud.contentwarehouse.v1",
    manifest={
        "CreateSynonymSetRequest",
        "GetSynonymSetRequest",
        "ListSynonymSetsRequest",
        "ListSynonymSetsResponse",
        "UpdateSynonymSetRequest",
        "DeleteSynonymSetRequest",
    },
)


class CreateSynonymSetRequest(proto.Message):
    r"""Request message for SynonymSetService.CreateSynonymSet.

    Attributes:
        parent (str):
            Required. The parent name. Format:
            projects/{project_number}/locations/{location}.
        synonym_set (google.cloud.contentwarehouse_v1.types.SynonymSet):
            Required. The synonymSet to be created for a
            context
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    synonym_set: synonymset.SynonymSet = proto.Field(
        proto.MESSAGE,
        number=2,
        message=synonymset.SynonymSet,
    )


class GetSynonymSetRequest(proto.Message):
    r"""Request message for SynonymSetService.GetSynonymSet.
    Will return synonymSet for a certain context.

    Attributes:
        name (str):
            Required. The name of the synonymSet to retrieve Format:
            projects/{project_number}/locations/{location}/synonymSets/{context}.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListSynonymSetsRequest(proto.Message):
    r"""Request message for SynonymSetService.ListSynonymSets.
    Will return all synonymSets belonging to the customer project.

    Attributes:
        parent (str):
            Required. The parent name. Format:
            projects/{project_number}/locations/{location}.
        page_size (int):
            The maximum number of synonymSets to return.
            The service may return fewer than this value. If
            unspecified, at most 50 rule sets will be
            returned. The maximum value is 1000; values
            above 1000 will be coerced to 1000.
        page_token (str):
            A page token, received from a previous ``ListSynonymSets``
            call. Provide this to retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``ListSynonymSets`` must match the call that provided the
            page token.
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


class ListSynonymSetsResponse(proto.Message):
    r"""Response message for SynonymSetService.ListSynonymSets.

    Attributes:
        synonym_sets (MutableSequence[google.cloud.contentwarehouse_v1.types.SynonymSet]):
            The synonymSets from the specified parent.
        next_page_token (str):
            A page token, received from a previous ``ListSynonymSets``
            call. Provide this to retrieve the subsequent page.
    """

    @property
    def raw_page(self):
        return self

    synonym_sets: MutableSequence[synonymset.SynonymSet] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=synonymset.SynonymSet,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UpdateSynonymSetRequest(proto.Message):
    r"""Request message for SynonymSetService.UpdateSynonymSet.
    Removes the SynonymSet for the specified context and replaces it
    with the SynonymSet in this request.

    Attributes:
        name (str):
            Required. The name of the synonymSet to update Format:
            projects/{project_number}/locations/{location}/synonymSets/{context}.
        synonym_set (google.cloud.contentwarehouse_v1.types.SynonymSet):
            Required. The synonymSet to be updated for
            the customer
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    synonym_set: synonymset.SynonymSet = proto.Field(
        proto.MESSAGE,
        number=2,
        message=synonymset.SynonymSet,
    )


class DeleteSynonymSetRequest(proto.Message):
    r"""Request message for SynonymSetService.DeleteSynonymSet.

    Attributes:
        name (str):
            Required. The name of the synonymSet to delete Format:
            projects/{project_number}/locations/{location}/synonymSets/{context}.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
