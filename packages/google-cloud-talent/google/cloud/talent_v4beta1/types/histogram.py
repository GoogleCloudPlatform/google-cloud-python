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
    package="google.cloud.talent.v4beta1",
    manifest={
        "HistogramQuery",
        "HistogramQueryResult",
    },
)


class HistogramQuery(proto.Message):
    r"""The histogram request.

    Attributes:
        histogram_query (str):
            An expression specifies a histogram request against matching
            resources (for example, jobs, profiles) for searches.

            See
            [SearchJobsRequest.histogram_queries][google.cloud.talent.v4beta1.SearchJobsRequest.histogram_queries]
            and
            [SearchProfilesRequest.histogram_queries][google.cloud.talent.v4beta1.SearchProfilesRequest.histogram_queries]
            for details about syntax.
    """

    histogram_query: str = proto.Field(
        proto.STRING,
        number=1,
    )


class HistogramQueryResult(proto.Message):
    r"""Histogram result that matches
    [HistogramQuery][google.cloud.talent.v4beta1.HistogramQuery]
    specified in searches.

    Attributes:
        histogram_query (str):
            Requested histogram expression.
        histogram (MutableMapping[str, int]):
            A map from the values of the facet associated with distinct
            values to the number of matching entries with corresponding
            value.

            The key format is:

            - (for string histogram) string values stored in the field.
            - (for named numeric bucket) name specified in ``bucket()``
              function, like for ``bucket(0, MAX, "non-negative")``, the
              key will be ``non-negative``.
            - (for anonymous numeric bucket) range formatted as
              ``<low>-<high>``, for example, ``0-1000``, ``MIN-0``, and
              ``0-MAX``.
    """

    histogram_query: str = proto.Field(
        proto.STRING,
        number=1,
    )
    histogram: MutableMapping[str, int] = proto.MapField(
        proto.STRING,
        proto.INT64,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
