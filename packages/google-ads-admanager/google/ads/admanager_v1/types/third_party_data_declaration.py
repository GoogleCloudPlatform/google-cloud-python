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

from google.ads.admanager_v1.types import third_party_data_declaration_type_enum

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "ThirdPartyDataDeclaration",
    },
)


class ThirdPartyDataDeclaration(proto.Message):
    r"""Represents a set of declarations about what (if any) third
    party companies are associated with a given creative. This can
    also be set on the Network to serve as a default for those
    creatives that don't have such field set.

    Attributes:
        declaration_type (google.ads.admanager_v1.types.ThirdPartyDataDeclarationTypeEnum.ThirdPartyDataDeclarationType):
            Optional. The declaration about third party
            data usage on the associated entity.
        third_party_companies (MutableSequence[str]):
            Optional. A list of ThirdPartyCompanies associated with this
            entity. Format:
            "networks/{network_code}/thirdPartyCompanies/{third_party_company}".
    """

    declaration_type: third_party_data_declaration_type_enum.ThirdPartyDataDeclarationTypeEnum.ThirdPartyDataDeclarationType = proto.Field(
        proto.ENUM,
        number=1,
        enum=third_party_data_declaration_type_enum.ThirdPartyDataDeclarationTypeEnum.ThirdPartyDataDeclarationType,
    )
    third_party_companies: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
