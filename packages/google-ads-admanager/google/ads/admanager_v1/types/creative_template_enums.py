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
        "CreativeTemplateTypeEnum",
        "CreativeTemplateStatusEnum",
    },
)


class CreativeTemplateTypeEnum(proto.Message):
    r"""Wrapper message for
    [CreativeTemplateType][google.ads.admanager.v1.CreativeTemplateTypeEnum.CreativeTemplateType]

    """

    class CreativeTemplateType(proto.Enum):
        r"""Describes type of the creative template.

        Values:
            CREATIVE_TEMPLATE_TYPE_UNSPECIFIED (0):
                Default value. This value is unused.
            STANDARD (1):
                Creative templates that are included in Ad
                Manager by default.
            CUSTOM (2):
                Creative templates created by an
                administrator or other user in the network.
        """

        CREATIVE_TEMPLATE_TYPE_UNSPECIFIED = 0
        STANDARD = 1
        CUSTOM = 2


class CreativeTemplateStatusEnum(proto.Message):
    r"""Wrapper message for
    [CreativeTemplateStatus][google.ads.admanager.v1.CreativeTemplateStatusEnum.CreativeTemplateStatus]

    """

    class CreativeTemplateStatus(proto.Enum):
        r"""Describes status of the creative template

        Values:
            CREATIVE_TEMPLATE_STATUS_UNSPECIFIED (0):
                Default value. This value is unused.
            ACTIVE (1):
                The CreativeTemplate is active
            DELETED (2):
                The CreativeTemplate is deleted. Creatives
                created from this CreativeTemplate can no longer
                serve.
            INACTIVE (3):
                The CreativeTemplate is inactive. Users
                cannot create new creatives from this template,
                but existing ones can be edited and continue to
                serve
        """

        CREATIVE_TEMPLATE_STATUS_UNSPECIFIED = 0
        ACTIVE = 1
        DELETED = 2
        INACTIVE = 3


__all__ = tuple(sorted(__protobuf__.manifest))
