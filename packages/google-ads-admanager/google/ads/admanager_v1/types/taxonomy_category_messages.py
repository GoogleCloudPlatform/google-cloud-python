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

from google.ads.admanager_v1.types import taxonomy_type_enum

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "TaxonomyCategory",
    },
)


class TaxonomyCategory(proto.Message):
    r"""The ``TaxonomyCategory`` resource.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the ``TaxonomyCategory``.
            Format:
            ``networks/{network_code}/taxonomyCategories/{taxonomy_category_id}``
        taxonomy_category_id (int):
            Output only. Deprecated: ``TaxonomyCategory`` ID.

            This field is a member of `oneof`_ ``_taxonomy_category_id``.
        display_name (str):
            Output only. Display name of the ``TaxonomyCategory``.

            This field is a member of `oneof`_ ``_display_name``.
        grouping_only (bool):
            Output only. Whether this ``TaxonomyCategory`` only serves
            to group its children.

            This field is a member of `oneof`_ ``_grouping_only``.
        parent_taxonomy_category_id (int):
            Output only. The ID of the parent category this
            ``TaxonomyCategory`` descends from.

            This field is a member of `oneof`_ ``_parent_taxonomy_category_id``.
        taxonomy_type (google.ads.admanager_v1.types.TaxonomyTypeEnum.TaxonomyType):
            Output only. The taxonomy that this ``TaxonomyCategory``
            belongs to.

            This field is a member of `oneof`_ ``_taxonomy_type``.
        ancestor_names (MutableSequence[str]):
            Output only. The list of names of the ancestors of this
            ``TaxonomyCategory``.
        ancestor_taxonomy_category_ids (MutableSequence[int]):
            Output only. The list of IDs of the ancestors of this
            ``TaxonomyCategory``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    taxonomy_category_id: int = proto.Field(
        proto.INT64,
        number=2,
        optional=True,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    grouping_only: bool = proto.Field(
        proto.BOOL,
        number=5,
        optional=True,
    )
    parent_taxonomy_category_id: int = proto.Field(
        proto.INT64,
        number=6,
        optional=True,
    )
    taxonomy_type: taxonomy_type_enum.TaxonomyTypeEnum.TaxonomyType = proto.Field(
        proto.ENUM,
        number=9,
        optional=True,
        enum=taxonomy_type_enum.TaxonomyTypeEnum.TaxonomyType,
    )
    ancestor_names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )
    ancestor_taxonomy_category_ids: MutableSequence[int] = proto.RepeatedField(
        proto.INT64,
        number=8,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
