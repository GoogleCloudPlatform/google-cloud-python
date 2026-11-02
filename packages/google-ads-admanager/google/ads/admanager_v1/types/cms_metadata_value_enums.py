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
        "CmsMetadataValueStatusEnum",
    },
)


class CmsMetadataValueStatusEnum(proto.Message):
    r"""Wrapper message for
    [CmsMetadataValueStatus][google.ads.admanager.v1.CmsMetadataValueStatusEnum.CmsMetadataValueStatus]

    """

    class CmsMetadataValueStatus(proto.Enum):
        r"""Status for CmsMetadataValue objects.

        Values:
            CMS_METADATA_VALUE_STATUS_UNSPECIFIED (0):
                Default value. This value is unused.
            ACTIVE (1):
                The value is active.
            ARCHIVED (2):
                The value is archived.
            INACTIVE (3):
                The value is not active.
        """

        CMS_METADATA_VALUE_STATUS_UNSPECIFIED = 0
        ACTIVE = 1
        ARCHIVED = 2
        INACTIVE = 3


__all__ = tuple(sorted(__protobuf__.manifest))
