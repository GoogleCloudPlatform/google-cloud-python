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
        "VastRedirectTypeEnum",
    },
)


class VastRedirectTypeEnum(proto.Message):
    r"""Wrapper message for
    [VastRedirectType][google.ads.admanager.v1.VastRedirectTypeEnum.VastRedirectType]

    """

    class VastRedirectType(proto.Enum):
        r"""The types of VAST ads that a ``VastRedirectCreative`` can point to.

        Values:
            VAST_REDIRECT_TYPE_UNSPECIFIED (0):
                Default value. This value is unused.
            LINEAR (1):
                The VAST XML contains only linear ads.
            LINEAR_AND_NON_LINEAR (2):
                The VAST XML contains both linear and
                nonlinear ads.
            NON_LINEAR (4):
                The VAST XML contains only nonlinear ads.
        """

        VAST_REDIRECT_TYPE_UNSPECIFIED = 0
        LINEAR = 1
        LINEAR_AND_NON_LINEAR = 2
        NON_LINEAR = 4


__all__ = tuple(sorted(__protobuf__.manifest))
