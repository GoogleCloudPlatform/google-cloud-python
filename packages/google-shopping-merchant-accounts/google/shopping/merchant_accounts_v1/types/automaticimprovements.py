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

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.shopping.merchant.accounts.v1",
    manifest={
        "AutomaticImprovements",
        "AutomaticItemUpdates",
        "AutomaticImageImprovements",
        "AutomaticShippingImprovements",
        "GetAutomaticImprovementsRequest",
        "UpdateAutomaticImprovementsRequest",
    },
)


class AutomaticImprovements(proto.Message):
    r"""Collection of information related to the `automatic
    improvements <https://developers.google.com/shopping-content/guides/automatic-improvements>`__
    of an account.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the automatic improvements.
            Format: ``accounts/{account}/automaticImprovements``.
        item_updates (google.shopping.merchant_accounts_v1.types.AutomaticItemUpdates):
            Turning on `item
            updates <https://support.google.com/merchants/answer/3246284>`__
            allows Google to automatically update items for you. When
            item updates are on, Google uses the structured data markup
            on the website and advanced data extractors to update the
            price and availability of the items. When the item updates
            are off, items with mismatched data aren't shown. This field
            is only updated (cleared) if provided in the update mask.

            This field is a member of `oneof`_ ``_item_updates``.
        image_improvements (google.shopping.merchant_accounts_v1.types.AutomaticImageImprovements):
            This improvement will attempt to automatically correct
            submitted images if they don't meet the `image
            requirements <https://support.google.com/merchants/answer/6324350>`__,
            for example, removing overlays. If successful, the image
            will be replaced and approved. This improvement is only
            applied to images of disapproved offers. For more
            information see: `Automatic image
            improvements <https://support.google.com/merchants/answer/9242973>`__
            This field is only updated (cleared) if provided in the
            update mask.

            This field is a member of `oneof`_ ``_image_improvements``.
        shipping_improvements (google.shopping.merchant_accounts_v1.types.AutomaticShippingImprovements):
            Not available for `advanced
            accounts <https://support.google.com/merchants/answer/188487>`__.
            By turning on `automatic shipping
            improvements <https://support.google.com/merchants/answer/10027038>`__,
            you are allowing Google to improve the accuracy of your
            delivery times shown to shoppers using Google. More accurate
            delivery times, especially when faster, typically lead to
            better conversion rates. Google will improve your estimated
            delivery times based on various factors:

            - Delivery address of an order
            - Current handling time and shipping time settings
            - Estimated weekdays or business days
            - Parcel tracking data This field is only updated (cleared)
              if provided in the update mask.

            This field is a member of `oneof`_ ``_shipping_improvements``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    item_updates: "AutomaticItemUpdates" = proto.Field(
        proto.MESSAGE,
        number=2,
        optional=True,
        message="AutomaticItemUpdates",
    )
    image_improvements: "AutomaticImageImprovements" = proto.Field(
        proto.MESSAGE,
        number=3,
        optional=True,
        message="AutomaticImageImprovements",
    )
    shipping_improvements: "AutomaticShippingImprovements" = proto.Field(
        proto.MESSAGE,
        number=4,
        optional=True,
        message="AutomaticShippingImprovements",
    )


class AutomaticItemUpdates(proto.Message):
    r"""Turning on `item
    updates <https://support.google.com/merchants/answer/3246284>`__
    allows Google to automatically update items for you. When item
    updates are on, Google uses the structured data markup on the
    website and advanced data extractors to update the price and
    availability of the items. When the item updates are off, items with
    mismatched data aren't shown.

    Attributes:
        account_item_updates_settings (google.shopping.merchant_accounts_v1.types.AutomaticItemUpdates.ItemUpdatesAccountLevelSettings):
            Optional. Determines which attributes of the
            items should be automatically updated. If this
            field is not present and provided in the update
            mask, then the settings will be deleted. If
            there are no settings for subaccount, they are
            inherited from aggregator.
        effective_allow_price_updates (bool):
            Output only. The effective value of allow_price_updates. If
            account_item_updates_settings is present, then this value is
            the same. Otherwise, it represents the inherited value of
            the parent account. The default value is true if no settings
            are present. Read-only.
        effective_allow_availability_updates (bool):
            Output only. The effective value of
            allow_availability_updates. If account_item_updates_settings
            is present, then this value is the same. Otherwise, it
            represents the inherited value of the parent account. The
            default value is true if no settings are present. Read-only.
        effective_allow_strict_availability_updates (bool):
            Output only. The effective value of
            allow_strict_availability_updates. If
            account_item_updates_settings is present, then this value is
            the same. Otherwise, it represents the inherited value of
            the parent account. The default value is true if no settings
            are present. Read-only.
        effective_allow_condition_updates (bool):
            Output only. The effective value of allow_condition_updates.
            If account_item_updates_settings is present, then this value
            is the same. Otherwise, it represents the inherited value of
            the parent account. The default value is true if no settings
            are present. Read-only.
    """

    class ItemUpdatesAccountLevelSettings(proto.Message):
        r"""Settings for the Automatic Item Updates.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            allow_price_updates (bool):
                If price updates are enabled, Google always
                updates the active price with the crawled
                information.

                This field is a member of `oneof`_ ``_allow_price_updates``.
            allow_availability_updates (bool):
                If availability updates are enabled, any previous
                availability values get overwritten if Google finds an
                out-of-stock annotation on the offer's page. If additionally
                ``allow_strict_availability_updates`` field is set to true,
                values get overwritten if Google finds an in-stock
                annotation on the offer’s page.

                This field is a member of `oneof`_ ``_allow_availability_updates``.
            allow_strict_availability_updates (bool):
                If ``allow_availability_updates`` is enabled, items are
                automatically updated in all your Shopping target countries.
                By default, availability updates will only be applied to
                items that are 'out of stock' on your website but 'in stock'
                on Shopping. Set this to true to also update items that are
                'in stock' on your website, but 'out of stock' on Google
                Shopping. In order for this field to have an effect, you
                must also set ``allow_availability_updates``.

                This field is a member of `oneof`_ ``_allow_strict_availability_updates``.
            allow_condition_updates (bool):
                If condition updates are enabled, Google
                always updates item condition with the condition
                detected from the details of your product.

                This field is a member of `oneof`_ ``_allow_condition_updates``.
        """

        allow_price_updates: bool = proto.Field(
            proto.BOOL,
            number=1,
            optional=True,
        )
        allow_availability_updates: bool = proto.Field(
            proto.BOOL,
            number=2,
            optional=True,
        )
        allow_strict_availability_updates: bool = proto.Field(
            proto.BOOL,
            number=3,
            optional=True,
        )
        allow_condition_updates: bool = proto.Field(
            proto.BOOL,
            number=4,
            optional=True,
        )

    account_item_updates_settings: ItemUpdatesAccountLevelSettings = proto.Field(
        proto.MESSAGE,
        number=1,
        message=ItemUpdatesAccountLevelSettings,
    )
    effective_allow_price_updates: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    effective_allow_availability_updates: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    effective_allow_strict_availability_updates: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    effective_allow_condition_updates: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class AutomaticImageImprovements(proto.Message):
    r"""This improvement will attempt to automatically correct submitted
    images if they don't meet the `image
    requirements <https://support.google.com/merchants/answer/6324350>`__,
    for example, removing overlays. If successful, the image will be
    replaced and approved. This improvement is only applied to images of
    disapproved offers. For more information see: `Automatic image
    improvements <https://support.google.com/merchants/answer/9242973>`__


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        account_image_improvements_settings (google.shopping.merchant_accounts_v1.types.AutomaticImageImprovements.ImageImprovementsAccountLevelSettings):
            Optional. Determines how the images should be
            automatically updated. If this field is not
            present and provided in the update mask, then
            the settings will be deleted. If there are no
            settings for subaccount, they are inherited from
            aggregator.

            This field is a member of `oneof`_ ``_account_image_improvements_settings``.
        effective_allow_automatic_image_improvements (bool):
            Output only. The effective value of
            allow_automatic_image_improvements. If
            account_image_improvements_settings is present, then this
            value is the same. Otherwise, it represents the inherited
            value of the parent account. Read-only.
    """

    class ImageImprovementsAccountLevelSettings(proto.Message):
        r"""Settings for the Automatic Image Improvements.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            allow_automatic_image_improvements (bool):
                Enables automatic image improvements.

                This field is a member of `oneof`_ ``_allow_automatic_image_improvements``.
        """

        allow_automatic_image_improvements: bool = proto.Field(
            proto.BOOL,
            number=1,
            optional=True,
        )

    account_image_improvements_settings: ImageImprovementsAccountLevelSettings = (
        proto.Field(
            proto.MESSAGE,
            number=1,
            optional=True,
            message=ImageImprovementsAccountLevelSettings,
        )
    )
    effective_allow_automatic_image_improvements: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class AutomaticShippingImprovements(proto.Message):
    r"""Not available for `advanced
    accounts <https://support.google.com/merchants/answer/188487>`__. By
    turning on `automatic shipping
    improvements <https://support.google.com/merchants/answer/10027038>`__,
    you are allowing Google to improve the accuracy of your delivery
    times shown to shoppers using Google. More accurate delivery times,
    especially when faster, typically lead to better conversion rates.
    Google will improve your estimated delivery times based on various
    factors:

    - Delivery address of an order
    - Current handling time and shipping time settings
    - Estimated weekdays or business days
    - Parcel tracking data


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        allow_shipping_improvements (bool):
            Enables automatic shipping improvements.

            This field is a member of `oneof`_ ``_allow_shipping_improvements``.
    """

    allow_shipping_improvements: bool = proto.Field(
        proto.BOOL,
        number=1,
        optional=True,
    )


class GetAutomaticImprovementsRequest(proto.Message):
    r"""Request message for the ``GetAutomaticImprovements`` method.

    Attributes:
        name (str):
            Required. The resource name of the automatic improvements.
            Format: ``accounts/{account}/automaticImprovements``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateAutomaticImprovementsRequest(proto.Message):
    r"""Request message for the ``UpdateAutomaticImprovements`` method.

    Attributes:
        automatic_improvements (google.shopping.merchant_accounts_v1.types.AutomaticImprovements):
            Required. The new version of the automatic
            imrovements.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. List of fields being updated. The following fields
            are supported (in both ``snake_case`` and
            ``lowerCamelCase``):

            - ``item_updates``
            - ``item_updates.account_level_settings``
            - ``image_improvements``
            - ``image_improvements.account_level_settings``
            - ``shipping_improvements``
            - ``shipping_improvements.allow_shipping_improvements``
    """

    automatic_improvements: "AutomaticImprovements" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="AutomaticImprovements",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
