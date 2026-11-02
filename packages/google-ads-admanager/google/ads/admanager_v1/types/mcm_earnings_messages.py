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

import google.type.date_pb2 as date_pb2  # type: ignore
import google.type.money_pb2 as money_pb2  # type: ignore
import proto  # type: ignore

from google.ads.admanager_v1.types import mcm_enums

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "McmEarnings",
        "EarningsProductBreakdown",
    },
)


class McmEarnings(proto.Message):
    r"""The earnings for a given month between a parent and child
    publisher in MCM


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        month (google.type.date_pb2.Date):
            Output only. The year and month that the MCM
            earnings data applies to. The date will be
            specified as the first of the month.

            This field is a member of `oneof`_ ``_month``.
        delegation_type (google.ads.admanager_v1.types.DelegationTypeEnum.DelegationType):
            Output only. The current type of MCM
            delegation between the parent and child
            publisher.

            This field is a member of `oneof`_ ``_delegation_type``.
        parent (str):
            Output only. The parent publisher in the MCM relationship.
            Format: ``networks/{network_code}``
        parent_display_name (str):
            Output only. The name of the parent
            publisher.

            This field is a member of `oneof`_ ``_parent_display_name``.
        child (str):
            Output only. The resource name of the ``ChildPublisher``'s
            Ad Manager network in the MCM relationship. Format:
            ``networks/{network_code}``
        child_publisher (str):
            Output only. The resource name of the child publisher in the
            MCM relationship. Format:
            "networks/{network_code}/childPublishers/{child_publisher_id}".

            This field is a member of `oneof`_ ``_child_publisher``.
        child_display_name (str):
            Output only. The name of the child publisher
            in the MCM relationship.

            This field is a member of `oneof`_ ``_child_display_name``.
        total_earnings (google.type.money_pb2.Money):
            Output only. The total earnings for the
            month.

            This field is a member of `oneof`_ ``_total_earnings``.
        parent_payment (google.type.money_pb2.Money):
            Output only. The portion of the total
            earnings paid to the parent publisher.

            This field is a member of `oneof`_ ``_parent_payment``.
        child_payment (google.type.money_pb2.Money):
            Output only. The portion of the total
            earnings paid to the child publisher.

            This field is a member of `oneof`_ ``_child_payment``.
        deductions (google.type.money_pb2.Money):
            Output only. The deductions for the month due
            to spam in micro units. Null for earnings prior
            to August 2020.

            This field is a member of `oneof`_ ``_deductions``.
        earnings_product_breakdown (MutableSequence[google.ads.admanager_v1.types.EarningsProductBreakdown]):
            Output only. The product type breakdown of
            earnings for a given month between a parent and
            child publisher in MCM.
    """

    month: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=1,
        optional=True,
        message=date_pb2.Date,
    )
    delegation_type: mcm_enums.DelegationTypeEnum.DelegationType = proto.Field(
        proto.ENUM,
        number=2,
        optional=True,
        enum=mcm_enums.DelegationTypeEnum.DelegationType,
    )
    parent: str = proto.Field(
        proto.STRING,
        number=3,
    )
    parent_display_name: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )
    child: str = proto.Field(
        proto.STRING,
        number=5,
    )
    child_publisher: str = proto.Field(
        proto.STRING,
        number=6,
        optional=True,
    )
    child_display_name: str = proto.Field(
        proto.STRING,
        number=7,
        optional=True,
    )
    total_earnings: money_pb2.Money = proto.Field(
        proto.MESSAGE,
        number=8,
        optional=True,
        message=money_pb2.Money,
    )
    parent_payment: money_pb2.Money = proto.Field(
        proto.MESSAGE,
        number=9,
        optional=True,
        message=money_pb2.Money,
    )
    child_payment: money_pb2.Money = proto.Field(
        proto.MESSAGE,
        number=10,
        optional=True,
        message=money_pb2.Money,
    )
    deductions: money_pb2.Money = proto.Field(
        proto.MESSAGE,
        number=11,
        optional=True,
        message=money_pb2.Money,
    )
    earnings_product_breakdown: MutableSequence["EarningsProductBreakdown"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=12,
            message="EarningsProductBreakdown",
        )
    )


class EarningsProductBreakdown(proto.Message):
    r"""The product type breakdown of earnings for a given month
    between a parent and child publisher in MCM.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        product_type (google.ads.admanager_v1.types.McmEarningsProductTypeEnum.McmEarningsProductType):
            The syndication product type of the child's
            earnings in MCM.

            This field is a member of `oneof`_ ``_product_type``.
        total_earnings (google.type.money_pb2.Money):
            The total earnings for the specified product
            type for the month.

            This field is a member of `oneof`_ ``_total_earnings``.
        parent_payment (google.type.money_pb2.Money):
            The portion of the total earnings for the
            specified product type paid to the parent
            publisher.

            This field is a member of `oneof`_ ``_parent_payment``.
        child_payment (google.type.money_pb2.Money):
            The portion of the total earnings for the
            specified product type paid to the child
            publisher.

            This field is a member of `oneof`_ ``_child_payment``.
        deductions (google.type.money_pb2.Money):
            The deductions for the specified product type
            for the month due to spam.

            This field is a member of `oneof`_ ``_deductions``.
    """

    product_type: mcm_enums.McmEarningsProductTypeEnum.McmEarningsProductType = (
        proto.Field(
            proto.ENUM,
            number=1,
            optional=True,
            enum=mcm_enums.McmEarningsProductTypeEnum.McmEarningsProductType,
        )
    )
    total_earnings: money_pb2.Money = proto.Field(
        proto.MESSAGE,
        number=2,
        optional=True,
        message=money_pb2.Money,
    )
    parent_payment: money_pb2.Money = proto.Field(
        proto.MESSAGE,
        number=3,
        optional=True,
        message=money_pb2.Money,
    )
    child_payment: money_pb2.Money = proto.Field(
        proto.MESSAGE,
        number=4,
        optional=True,
        message=money_pb2.Money,
    )
    deductions: money_pb2.Money = proto.Field(
        proto.MESSAGE,
        number=5,
        optional=True,
        message=money_pb2.Money,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
