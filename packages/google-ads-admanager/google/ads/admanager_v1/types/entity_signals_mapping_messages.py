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
    package="google.ads.admanager.v1",
    manifest={
        "EntitySignalsMapping",
    },
)


class EntitySignalsMapping(proto.Message):
    r"""The ``EntitySignalsMapping`` resource.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        audience_segment_id (int):
            ID of an AudienceSegment that this mapping
            belongs to.

            This field is a member of `oneof`_ ``entity``.
        content_bundle_id (int):
            ID of a ContentBundle that this mapping
            belongs to.

            This field is a member of `oneof`_ ``entity``.
        custom_targeting_value_id (int):
            ID of a CustomValue that this mapping belongs
            to.

            This field is a member of `oneof`_ ``entity``.
        name (str):
            Identifier. The resource name of the
            ``EntitySignalsMapping``. Format:
            ``networks/{network_code}/entitySignalsMappings/{entity_signals_mapping_id}``
        entity_signals_mapping_id (int):
            Output only. Deprecated: ``EntitySignalsMapping`` ID.

            This field is a member of `oneof`_ ``_entity_signals_mapping_id``.
        taxonomy_category_ids (MutableSequence[int]):
            Optional. The IDs of the categories that are
            associated with the referencing entity.
    """

    audience_segment_id: int = proto.Field(
        proto.INT64,
        number=3,
        oneof="entity",
    )
    content_bundle_id: int = proto.Field(
        proto.INT64,
        number=4,
        oneof="entity",
    )
    custom_targeting_value_id: int = proto.Field(
        proto.INT64,
        number=5,
        oneof="entity",
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    entity_signals_mapping_id: int = proto.Field(
        proto.INT64,
        number=2,
        optional=True,
    )
    taxonomy_category_ids: MutableSequence[int] = proto.RepeatedField(
        proto.INT64,
        number=6,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
