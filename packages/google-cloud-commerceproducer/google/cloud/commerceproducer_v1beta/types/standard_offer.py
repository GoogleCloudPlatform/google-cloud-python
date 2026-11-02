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

import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.commerceproducer.v1beta",
    manifest={
        "StandardOffer",
    },
)


class StandardOffer(proto.Message):
    r"""Message describing the StandardOffer resource.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        term_duration_months (int):
            Output only. Term duration of the offer in
            months. Applicable only to offers with a
            subscription price model. Additional forms of
            offer term may be added in the future.

            This field is a member of `oneof`_ ``term``.
        name (str):
            Identifier. Name of resource.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Creation time of the offer.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Last update time of the offer.
        effective_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Effective time of the offer.
            Prior to this time, the offer cannot be
            purchased or used as the base standard offer of
            a private offer.
        expire_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Expire time of the offer.
            An offer is expired if its expire time is in the
            past. An expired standard offer cannot be
            purchased or used as the base standard offer of
            a private offer.
        service_level (str):
            Output only. Identifier that distinguishes between different
            service levels of the same product that constitute distinct
            offerings to customers with different pricing.

            The service levels of a product are also referred to in some
            cases as the product's 'plans', and the ``service_level``
            value is referred to in some cases as the "plan ID".

            Multiple non-expired standard offers can share the same
            service level when they are subscription offers for
            different term durations.
        service_level_title (str):
            Output only. Title of the service level.

            Not included for ``STANDARD_OFFER_VIEW_BASIC``.
        price_model (google.cloud.commerceproducer_v1beta.types.StandardOffer.PriceModel):
            Output only. Price model of the offer.
    """

    class PriceModel(proto.Message):
        r"""Price model of the offer.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            flat_fee (google.cloud.commerceproducer_v1beta.types.StandardOffer.PriceModel.FlatFeeSubscription):
                Output only. Price configurations for the
                flat fee subscription.

                This field is a member of `oneof`_ ``subscription``.
            usage (google.cloud.commerceproducer_v1beta.types.StandardOffer.PriceModel.Usage):
                Output only. Price configurations for the
                usage part.
        """

        class SkuList(proto.Message):
            r"""A collection of SKUs.

            Attributes:
                skus (MutableSequence[str]):
                    Output only. List of SKUs by name.
            """

            skus: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=1,
            )

        class SkuGroupList(proto.Message):
            r"""A collection of SkuGroups.

            Attributes:
                sku_groups (MutableSequence[str]):
                    Output only. List of SkuGroups by name.
            """

            sku_groups: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=1,
            )

        class Usage(proto.Message):
            r"""Price configurations for the usage part.

            This message has `oneof`_ fields (mutually exclusive fields).
            For each oneof, at most one member field can be set at the same time.
            Setting any member of the oneof automatically clears all other
            members.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                sku_list (google.cloud.commerceproducer_v1beta.types.StandardOffer.PriceModel.SkuList):
                    Output only. The offer's usage fees are
                    charged against these SKUs.

                    This field is a member of `oneof`_ ``skus``.
                sku_group_list (google.cloud.commerceproducer_v1beta.types.StandardOffer.PriceModel.SkuGroupList):
                    Output only. The offer's usage fees are
                    charged against the SKUs in these groups.

                    This field is a member of `oneof`_ ``skus``.
            """

            sku_list: "StandardOffer.PriceModel.SkuList" = proto.Field(
                proto.MESSAGE,
                number=1,
                oneof="skus",
                message="StandardOffer.PriceModel.SkuList",
            )
            sku_group_list: "StandardOffer.PriceModel.SkuGroupList" = proto.Field(
                proto.MESSAGE,
                number=2,
                oneof="skus",
                message="StandardOffer.PriceModel.SkuGroupList",
            )

        class FlatFeeSubscription(proto.Message):
            r"""Price configurations for flat fee subscriptions.

            Attributes:
                sku (str):
                    Output only. Flat fee subscription SKU for
                    the offer.
            """

            sku: str = proto.Field(
                proto.STRING,
                number=1,
            )

        flat_fee: "StandardOffer.PriceModel.FlatFeeSubscription" = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="subscription",
            message="StandardOffer.PriceModel.FlatFeeSubscription",
        )
        usage: "StandardOffer.PriceModel.Usage" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="StandardOffer.PriceModel.Usage",
        )

    term_duration_months: int = proto.Field(
        proto.INT32,
        number=7,
        oneof="term",
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    effective_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    expire_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    service_level: str = proto.Field(
        proto.STRING,
        number=6,
    )
    service_level_title: str = proto.Field(
        proto.STRING,
        number=9,
    )
    price_model: PriceModel = proto.Field(
        proto.MESSAGE,
        number=8,
        message=PriceModel,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
