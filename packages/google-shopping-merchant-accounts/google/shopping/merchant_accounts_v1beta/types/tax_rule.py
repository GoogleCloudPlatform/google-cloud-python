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

import google.type.interval_pb2 as interval_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.shopping.merchant.accounts.v1beta",
    manifest={
        "TaxRule",
    },
)


class TaxRule(proto.Message):
    r"""Primary type convension

    percent micro : 100% = 1 000 000 and 1% = 10 000
                    cannot be negative.

    Information about tax nexus and related parameters applicable to
    orders delivered to the area covered by a single tax admin.
    Nexus is created when a merchant is doing business in an area
    administered by tax admin (only US states are supported for
    nexus configuration). If merchant has nexus in a US state,
    merchant needs to pay tax to all tax authorities associated with
    the shipping destination.
    Next Id : 8

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        location_id (int):
            The admin_id or criteria_id of the region in which this rule
            is applicable.

            This field is a member of `oneof`_ ``location``.
        post_code_range (google.shopping.merchant_accounts_v1beta.types.TaxRule.TaxPostalCodeRange):
            The range of postal codes in which this rule
            is applicable.

            This field is a member of `oneof`_ ``location``.
        use_google_rate (bool):
            Rate that depends on delivery location: if
            merchant has a nexus in corresponding US state,
            rates from authorities with jurisdiction over
            delivery area are added up.

            This field is a member of `oneof`_ ``rate_calculation``.
        self_specified_rate_micros (int):
            A fixed rate specified in micros, where 100% = 1_000_000.
            Suitable for origin-based states.

            This field is a member of `oneof`_ ``rate_calculation``.
        region_code (str):
            Region code in which this rule is applicable
        shipping_taxed (bool):
            If set, shipping charge is taxed (at the same
            rate as product) when delivering to this admin's
            area. Can only be set on US states without
            category.
        effective_time_period (google.type.interval_pb2.Interval):
            Required. Time period when this rule is effective. If the
            duration is missing from effective_time listed, then it is
            open ended to the future. The start of this time period is
            inclusive, and the end is exclusive.
    """

    class TaxPostalCodeRange(proto.Message):
        r"""A range of postal codes that defines the area.

        Attributes:
            start (str):
                Required. The start of the postal code range,
                which is also the smallest in the range.
            end (str):
                The end of the postal code range. Will be the
                same as start if not specified.
        """

        start: str = proto.Field(
            proto.STRING,
            number=1,
        )
        end: str = proto.Field(
            proto.STRING,
            number=2,
        )

    location_id: int = proto.Field(
        proto.INT64,
        number=2,
        oneof="location",
    )
    post_code_range: TaxPostalCodeRange = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="location",
        message=TaxPostalCodeRange,
    )
    use_google_rate: bool = proto.Field(
        proto.BOOL,
        number=4,
        oneof="rate_calculation",
    )
    self_specified_rate_micros: int = proto.Field(
        proto.INT64,
        number=5,
        oneof="rate_calculation",
    )
    region_code: str = proto.Field(
        proto.STRING,
        number=1,
    )
    shipping_taxed: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    effective_time_period: interval_pb2.Interval = proto.Field(
        proto.MESSAGE,
        number=7,
        message=interval_pb2.Interval,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
