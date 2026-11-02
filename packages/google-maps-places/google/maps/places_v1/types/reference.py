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

from google.maps.places_v1.types import review

__protobuf__ = proto.module(
    package="google.maps.places.v1",
    manifest={
        "References",
    },
)


class References(proto.Message):
    r"""Experimental: See
    https://developers.google.com/maps/documentation/places/web-service/experimental/places-generative
    for more details.

    Reference that the generative content is related to.

    Attributes:
        reviews (MutableSequence[google.maps.places_v1.types.Review]):
            Reviews that serve as references.
        places (MutableSequence[str]):
            The list of resource names of the referenced
            places. This name can be used in other APIs that
            accept Place resource names.
    """

    reviews: MutableSequence[review.Review] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=review.Review,
    )
    places: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
