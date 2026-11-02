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

from google.cloud.websecurityscanner_v1alpha.types import finding

__protobuf__ = proto.module(
    package="google.cloud.websecurityscanner.v1alpha",
    manifest={
        "FindingTypeStats",
    },
)


class FindingTypeStats(proto.Message):
    r"""A FindingTypeStats resource represents stats regarding a
    specific FindingType of Findings under a given ScanRun.

    Attributes:
        finding_type (google.cloud.websecurityscanner_v1alpha.types.Finding.FindingType):
            The finding type associated with the stats.
        finding_count (int):
            The count of findings belonging to this
            finding type.
    """

    finding_type: finding.Finding.FindingType = proto.Field(
        proto.ENUM,
        number=1,
        enum=finding.Finding.FindingType,
    )
    finding_count: int = proto.Field(
        proto.INT32,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
