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
        "ProgrammaticBuyer",
    },
)


class ProgrammaticBuyer(proto.Message):
    r"""Represents a programmatic buyer.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the ``ProgrammaticBuyer``.
            Format:
            ``networks/{network_code}/programmaticBuyers/{buyer_account_id}``
        buyer_account_id (int):
            Output only. The buyer account ID of the
            buyer.

            This field is a member of `oneof`_ ``_buyer_account_id``.
        display_name (str):
            Output only. The display name of the buyer.

            This field is a member of `oneof`_ ``_display_name``.
        parent_account_id (int):
            Output only. The ID of the programmatic
            buyer's sponsor. If the buyer has no sponsor,
            this field will be -1.

            This field is a member of `oneof`_ ``_parent_account_id``.
        partner_client_id (str):
            Output only. ID of the Display & Video 360
            client buyer partner ID (if Display & Video 360)
            or Authorized Buyers client buyer account ID.

            This field is a member of `oneof`_ ``_partner_client_id``.
        agency (bool):
            Output only. Whether the buyer is an
            advertising agency.

            This field is a member of `oneof`_ ``_agency``.
        preferred_deals_enabled (bool):
            Output only. Whether the buyer is enabled for
            preferred deals.

            This field is a member of `oneof`_ ``_preferred_deals_enabled``.
        programmatic_guaranteed_enabled (bool):
            Output only. Whether the buyer is enabled for
            programmatic guaranteed deals.

            This field is a member of `oneof`_ ``_programmatic_guaranteed_enabled``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    buyer_account_id: int = proto.Field(
        proto.INT64,
        number=2,
        optional=True,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=5,
        optional=True,
    )
    parent_account_id: int = proto.Field(
        proto.INT64,
        number=6,
        optional=True,
    )
    partner_client_id: str = proto.Field(
        proto.STRING,
        number=7,
        optional=True,
    )
    agency: bool = proto.Field(
        proto.BOOL,
        number=9,
        optional=True,
    )
    preferred_deals_enabled: bool = proto.Field(
        proto.BOOL,
        number=12,
        optional=True,
    )
    programmatic_guaranteed_enabled: bool = proto.Field(
        proto.BOOL,
        number=13,
        optional=True,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
