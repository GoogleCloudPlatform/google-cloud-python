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
        "GrpProviderEnum",
    },
)


class GrpProviderEnum(proto.Message):
    r"""Wrapper message for
    [GrpProvider][google.ads.admanager.v1.GrpProviderEnum.GrpProvider]

    """

    class GrpProvider(proto.Enum):
        r"""Represents available GRP providers that a line item will have
        its target demographic measured by.

        Values:
            GRP_PROVIDER_UNSPECIFIED (0):
                Default value. This value is unused.
            GOOGLE (1):
                Google's GRP provider.
            NIELSEN (2):
                Nielsen's GRP provider.
        """

        GRP_PROVIDER_UNSPECIFIED = 0
        GOOGLE = 1
        NIELSEN = 2


__all__ = tuple(sorted(__protobuf__.manifest))
