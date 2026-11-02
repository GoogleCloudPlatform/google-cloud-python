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

from google.ads.admanager_v1.types import cms_metadata_key_enums

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "CmsMetadataKey",
    },
)


class CmsMetadataKey(proto.Message):
    r"""Key associated with a piece of content from a publisher's
    CMS.

    Attributes:
        name (str):
            Identifier. The resource name of the ``CmsMetadataKey``.
            Format:
            ``networks/{network_code}/cmsMetadataKeys/{cms_metadata_key_id}``
        display_name (str):
            Required. The key of a key-value pair.
        status (google.ads.admanager_v1.types.CmsMetadataKeyStatusEnum.CmsMetadataKeyStatus):
            Output only. The status of this CMS metadata
            key.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    status: cms_metadata_key_enums.CmsMetadataKeyStatusEnum.CmsMetadataKeyStatus = (
        proto.Field(
            proto.ENUM,
            number=4,
            enum=cms_metadata_key_enums.CmsMetadataKeyStatusEnum.CmsMetadataKeyStatus,
        )
    )


__all__ = tuple(sorted(__protobuf__.manifest))
