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
        "CreativeThirdPartyDataDeclarationStatusEnum",
    },
)


class CreativeThirdPartyDataDeclarationStatusEnum(proto.Message):
    r"""Wrapper message for
    [CreativeThirdPartyDataDeclarationStatus][google.ads.admanager.v1.CreativeThirdPartyDataDeclarationStatusEnum.CreativeThirdPartyDataDeclarationStatus]

    """

    class CreativeThirdPartyDataDeclarationStatus(proto.Enum):
        r"""The "status" of the ThirdPartyDataDeclaration associated with
        a given creative.

        This is calculated by comparing the companies detected by
        automated scanning/parsing, with the companies the publisher has
        declared in the ThirdPartyDataDeclaration.

        Values:
            CREATIVE_THIRD_PARTY_DATA_DECLARATION_STATUS_UNSPECIFIED (0):
                Default value. This value is unused.
            COMPLETE (1):
                All companies detected in scanning exist in
                the associated ThirdPartyDataDeclaration.

                This could be because there were no detected
                companies, or all the detected companies exist
                in the associated declaration.
            INCOMPLETE (2):
                There are companies detected in scanning that
                do not exist in the associated
                ThirdPartyDataDeclaration.

                This could be because there is no declaration,
                at either the creative level or network level,
                or the declaration is missing companies.
            UNSCANNED (3):
                This entity has not been recently scanned.

                This can happen either because there is no
                scanning data for this creative, or the scanning
                data is stale (because the creative is not
                associated with any active line items / eligible
                to serve).
        """

        CREATIVE_THIRD_PARTY_DATA_DECLARATION_STATUS_UNSPECIFIED = 0
        COMPLETE = 1
        INCOMPLETE = 2
        UNSCANNED = 3


__all__ = tuple(sorted(__protobuf__.manifest))
