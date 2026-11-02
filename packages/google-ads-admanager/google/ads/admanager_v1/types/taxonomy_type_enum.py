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
        "TaxonomyTypeEnum",
    },
)


class TaxonomyTypeEnum(proto.Message):
    r"""Wrapper for
    [TaxonomyType][google.ads.admanager.v1.TaxonomyTypeEnum.TaxonomyType]

    """

    class TaxonomyType(proto.Enum):
        r"""The taxonomy type of the IAB defined taxonomies.
        Used for Publisher provided signals.

        Values:
            TAXONOMY_TYPE_UNSPECIFIED (0):
                Unspecified/not present
            TAXONOMY_IAB_AUDIENCE_1_1 (3):
                The IAB Audience Taxonomy v1.1.
            TAXONOMY_IAB_CONTENT_1_0 (8):
                The IAB Content Taxonomy v1.0.
            TAXONOMY_IAB_CONTENT_2_1 (4):
                The IAB Content Taxonomy v2.1.
            TAXONOMY_IAB_CONTENT_2_2 (6):
                The IAB Content Taxonomy v2.2.
            TAXONOMY_IAB_CONTENT_3_0 (5):
                The IAB Content Taxonomy v3.0.
            TAXONOMY_GOOGLE_STRUCTURED_VIDEO_1_0 (7):
                The PPS structured video signals taxonomy.
        """

        TAXONOMY_TYPE_UNSPECIFIED = 0
        TAXONOMY_IAB_AUDIENCE_1_1 = 3
        TAXONOMY_IAB_CONTENT_1_0 = 8
        TAXONOMY_IAB_CONTENT_2_1 = 4
        TAXONOMY_IAB_CONTENT_2_2 = 6
        TAXONOMY_IAB_CONTENT_3_0 = 5
        TAXONOMY_GOOGLE_STRUCTURED_VIDEO_1_0 = 7


__all__ = tuple(sorted(__protobuf__.manifest))
