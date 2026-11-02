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
        "ChildContentEligibilityEnum",
    },
)


class ChildContentEligibilityEnum(proto.Message):
    r"""Wrapper message for
    [ChildContentEligibility][google.ads.admanager.v1.ChildContentEligibilityEnum.ChildContentEligibility]

    """

    class ChildContentEligibility(proto.Enum):
        r"""Child content eligibility designation.

        Values:
            CHILD_CONTENT_ELIGIBILITY_UNSPECIFIED (0):
                Default value. This value is unused.
            ALLOWED (1):
                This line item is eligible to serve on
                requests that are child-directed.
            DISALLOWED (2):
                This line item is not eligible to serve on
                any requests that are child-directed.
        """

        CHILD_CONTENT_ELIGIBILITY_UNSPECIFIED = 0
        ALLOWED = 1
        DISALLOWED = 2


__all__ = tuple(sorted(__protobuf__.manifest))
