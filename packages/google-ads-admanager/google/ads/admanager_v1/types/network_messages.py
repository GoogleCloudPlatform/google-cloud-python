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

from google.ads.admanager_v1.types import (
    third_party_data_declaration as gaa_third_party_data_declaration,
)

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "Network",
        "DefaultThirdPartyDataDeclaration",
    },
)


class Network(proto.Message):
    r"""The Network resource.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the Network. Format:
            networks/{network_code}
        display_name (str):
            Optional. Display name for Network.

            This field is a member of `oneof`_ ``_display_name``.
        network_code (str):
            Output only. Network Code.

            This field is a member of `oneof`_ ``_network_code``.
        property_code (str):
            Output only. Property code.

            This field is a member of `oneof`_ ``_property_code``.
        time_zone (str):
            Output only. Time zone associated with the
            delivery of orders and reporting.

            This field is a member of `oneof`_ ``_time_zone``.
        currency_code (str):
            Output only. Primary currency code, in
            ISO-4217 format.

            This field is a member of `oneof`_ ``_currency_code``.
        secondary_currency_codes (MutableSequence[str]):
            Optional. Currency codes that can be used as
            an alternative to the primary currency code for
            trafficking Line Items.
        effective_root_ad_unit (str):
            Output only. Top most `Ad
            Unit <google.ads.admanager.v1.AdUnit>`__ to which descendant
            Ad Units can be added. Format:
            networks/{network_code}/adUnits/{ad_unit}

            This field is a member of `oneof`_ ``_effective_root_ad_unit``.
        test_network (bool):
            Output only. Whether this is a test network.

            This field is a member of `oneof`_ ``_test_network``.
        network_id (int):
            Output only. Network ID.

            This field is a member of `oneof`_ ``_network_id``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    network_code: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    property_code: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )
    time_zone: str = proto.Field(
        proto.STRING,
        number=5,
        optional=True,
    )
    currency_code: str = proto.Field(
        proto.STRING,
        number=6,
        optional=True,
    )
    secondary_currency_codes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )
    effective_root_ad_unit: str = proto.Field(
        proto.STRING,
        number=8,
        optional=True,
    )
    test_network: bool = proto.Field(
        proto.BOOL,
        number=10,
        optional=True,
    )
    network_id: int = proto.Field(
        proto.INT64,
        number=11,
        optional=True,
    )


class DefaultThirdPartyDataDeclaration(proto.Message):
    r"""The ``DefaultThirdPartyDataDeclaration`` singleton resource.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the
            ``DefaultThirdPartyDataDeclaration``. Format:
            ``networks/{network_code}/defaultThirdPartyDataDeclaration``
        third_party_data_declaration (google.ads.admanager_v1.types.ThirdPartyDataDeclaration):
            Optional. Returns the default
            [ThirdPartyDataDeclaration][google.ads.admanager.v1.ThirdPartyDataDeclaration]
            for this network. If this setting has never been updated on
            your network, then this API response will be unset.

            This field is a member of `oneof`_ ``_third_party_data_declaration``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    third_party_data_declaration: gaa_third_party_data_declaration.ThirdPartyDataDeclaration = proto.Field(
        proto.MESSAGE,
        number=2,
        optional=True,
        message=gaa_third_party_data_declaration.ThirdPartyDataDeclaration,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
