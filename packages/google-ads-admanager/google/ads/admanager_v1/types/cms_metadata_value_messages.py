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

from google.ads.admanager_v1.types import cms_metadata_value_enums

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "CmsMetadataValue",
    },
)


class CmsMetadataValue(proto.Message):
    r"""Key value pair associated with a piece of content from a
    publisher's CMS.

    Attributes:
        name (str):
            Identifier. The resource name of the ``CmsMetadataValue``.
            Format:
            ``networks/{network_code}/cmsMetadataValues/{cms_metadata_value_id}``
        display_name (str):
            The value of this key-value pair.
        key (str):
            Required. Immutable. The resource name of the
            CmsMetadataKey. Format:
            "networks/{network_code}/cmsMetadataKey/{cms_metadata_key_id}".
        status (google.ads.admanager_v1.types.CmsMetadataValueStatusEnum.CmsMetadataValueStatus):
            Output only. The status of this CMS metadata
            value.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    key: str = proto.Field(
        proto.STRING,
        number=5,
    )
    status: cms_metadata_value_enums.CmsMetadataValueStatusEnum.CmsMetadataValueStatus = proto.Field(
        proto.ENUM,
        number=6,
        enum=cms_metadata_value_enums.CmsMetadataValueStatusEnum.CmsMetadataValueStatus,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
