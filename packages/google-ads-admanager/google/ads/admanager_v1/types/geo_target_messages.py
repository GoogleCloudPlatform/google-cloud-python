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
        "GeoTarget",
    },
)


class GeoTarget(proto.Message):
    r"""Represents a location in the world, for targeting.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the ``GeoTarget``. Format:
            ``networks/{network_code}/geoTargets/{geo_target_id}``
        display_name (str):
            Output only. The display name of the
            GeoTarget.

            This field is a member of `oneof`_ ``_display_name``.
        canonical_parent (str):
            Output only. The name of the direct parent that defines the
            canonical name of the geo target. For example, if the
            current geo target is "San Francisco", its canonical name
            would be "San Francisco, California, United States" thus the
            canonical_parent would be the name of California and the
            canonical_parent of California would be the name of United
            states Format:
            ``networks/{network_code}/geoTargets/{geo_target}``

            This field is a member of `oneof`_ ``_canonical_parent``.
        parent_names (MutableSequence[str]):
            Output only. All parents of the geo target
            ordered by ascending size.
        region_code (str):
            Output only. The Unicode CLDR region code of
            the geo target.

            This field is a member of `oneof`_ ``_region_code``.
        type_ (str):
            Output only. The location type (unlocalized)
            for this geographical entity.

            This field is a member of `oneof`_ ``_type``.
        targetable (bool):
            Output only. Whether the geo target is
            targetable.

            This field is a member of `oneof`_ ``_targetable``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    canonical_parent: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    parent_names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    region_code: str = proto.Field(
        proto.STRING,
        number=5,
        optional=True,
    )
    type_: str = proto.Field(
        proto.STRING,
        number=6,
        optional=True,
    )
    targetable: bool = proto.Field(
        proto.BOOL,
        number=7,
        optional=True,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
