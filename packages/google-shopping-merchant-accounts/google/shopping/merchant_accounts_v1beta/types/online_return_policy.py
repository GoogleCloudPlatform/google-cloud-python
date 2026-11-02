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
import google.type.date_pb2 as date_pb2  # type: ignore
import proto  # type: ignore
from google.shopping.type.types import types

__protobuf__ = proto.module(
    package="google.shopping.merchant.accounts.v1beta",
    manifest={
        "GetOnlineReturnPolicyRequest",
        "CreateOnlineReturnPolicyRequest",
        "UpdateOnlineReturnPolicyRequest",
        "DeleteOnlineReturnPolicyRequest",
        "ListOnlineReturnPoliciesRequest",
        "ListOnlineReturnPoliciesResponse",
        "OnlineReturnPolicy",
    },
)


class GetOnlineReturnPolicyRequest(proto.Message):
    r"""Request message for the ``GetOnlineReturnPolicy`` method.

    Attributes:
        name (str):
            Required. The name of the return policy to retrieve. Format:
            ``accounts/{account}/onlineReturnPolicies/{return_policy}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateOnlineReturnPolicyRequest(proto.Message):
    r"""Request message for the ``CreateOnlineReturnPolicy`` method.

    Attributes:
        parent (str):
            Required. The merchant account for which the return policy
            will be created. Format: ``accounts/{account}``
        online_return_policy (google.shopping.merchant_accounts_v1beta.types.OnlineReturnPolicy):
            Required. The return policy object to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    online_return_policy: "OnlineReturnPolicy" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="OnlineReturnPolicy",
    )


class UpdateOnlineReturnPolicyRequest(proto.Message):
    r"""Request message for the ``UpdateOnlineReturnPolicy`` method. The
    method supports field masks and when the mask is provided, only the
    fields specified in the mask are updated.

    Attributes:
        online_return_policy (google.shopping.merchant_accounts_v1beta.types.OnlineReturnPolicy):
            Required. The online return policy to update. The online
            return policy's ``name`` field is used to identify the
            online return policy to be updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. List of fields being updated.

            The following fields are supported (in both ``snake_case``
            and ``lowerCamelCase``):

            - ``accept_defective_only``
            - ``accept_exchange``
            - ``item_conditions``
            - ``policy``
            - ``process_refund_days``
            - ``restocking_fee``
            - ``return_methods``
            - ``return_policy_uri``
            - ``return_shipping_fee``
    """

    online_return_policy: "OnlineReturnPolicy" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="OnlineReturnPolicy",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteOnlineReturnPolicyRequest(proto.Message):
    r"""Request message for the ``DeleteOnlineReturnPolicy`` method.

    Attributes:
        name (str):
            Required. The name of the return policy to delete. Format:
            ``accounts/{account}/onlineReturnPolicies/{return_policy}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListOnlineReturnPoliciesRequest(proto.Message):
    r"""Request message for the ``ListOnlineReturnPolicies`` method.

    Attributes:
        parent (str):
            Required. The merchant account for which to list return
            policies. Format: ``accounts/{account}``
        page_size (int):
            Optional. The maximum number of ``OnlineReturnPolicy``
            resources to return. The service returns fewer than this
            value if the number of return policies for the given
            merchant is less that than the ``pageSize``. The default
            value is 10. The maximum value is 100; If a value higher
            than the maximum is specified, then the ``pageSize`` will
            default to the maximum
        page_token (str):
            Optional. A page token, received from a previous
            ``ListOnlineReturnPolicies`` call. Provide the page token to
            retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``ListOnlineReturnPolicies`` must match the call that
            provided the page token. The token returned as
            [nextPageToken][google.shopping.merchant.accounts.v1beta.ListOnlineReturnPoliciesResponse.next_page_token]
            in the response to the previous request.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListOnlineReturnPoliciesResponse(proto.Message):
    r"""Response message for the ``ListOnlineReturnPolicies`` method.

    Attributes:
        online_return_policies (MutableSequence[google.shopping.merchant_accounts_v1beta.types.OnlineReturnPolicy]):
            The retrieved return policies.
        next_page_token (str):
            A token, which can be sent as ``pageToken`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    online_return_policies: MutableSequence["OnlineReturnPolicy"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="OnlineReturnPolicy",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class OnlineReturnPolicy(proto.Message):
    r"""`Online return
    policy <https://support.google.com/merchants/answer/10220642>`__
    object. This is currently used to represent return policies for ads
    and free listings programs.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The name of the ``OnlineReturnPolicy`` resource.
            Format:
            ``accounts/{account}/onlineReturnPolicies/{return_policy}``
        return_policy_id (str):
            Output only. Return policy ID generated by
            Google.
        label (str):
            Required. Immutable. This field represents the unique
            user-defined label of the return policy. It is important to
            note that the same label cannot be used in different return
            policies for the same country. Unless a product specifies a
            specific label attribute, policies will be automatically
            labeled as 'default'. To assign a custom return policy to
            certain product groups, follow the instructions provided in
            the [Return policy label]
            (https://support.google.com/merchants/answer/9445425). The
            label can contain up to 50 characters.
        countries (MutableSequence[str]):
            Required. Immutable. The countries of sale
            where the return policy applies. The values must
            be a valid 2 letter ISO 3166 code.
        policy (google.shopping.merchant_accounts_v1beta.types.OnlineReturnPolicy.Policy):
            Optional. The return policy.
        seasonal_overrides (MutableSequence[google.shopping.merchant_accounts_v1beta.types.OnlineReturnPolicy.SeasonalOverride]):
            Optional. Overrides to the general policy for
            orders placed during a specific set of time
            intervals.
        restocking_fee (google.shopping.merchant_accounts_v1beta.types.OnlineReturnPolicy.RestockingFee):
            Optional. The restocking fee that applies to
            all return reason categories. This would be
            treated as a free restocking fee if the value is
            not set.
        return_methods (MutableSequence[google.shopping.merchant_accounts_v1beta.types.OnlineReturnPolicy.ReturnMethod]):
            Optional. The return methods of how customers
            can return an item. This value is required to
            not be empty unless the type of return policy is
            noReturns.
        item_conditions (MutableSequence[google.shopping.merchant_accounts_v1beta.types.OnlineReturnPolicy.ItemCondition]):
            Optional. The item conditions accepted for
            returns must not be empty unless the type of
            return policy is 'noReturns'.
        return_shipping_fee (google.shopping.merchant_accounts_v1beta.types.OnlineReturnPolicy.ReturnShippingFee):
            Optional. The return shipping fee. Should be
            set only when customer need to download and
            print the return label.
        return_policy_uri (str):
            Required. The return policy uri. This can
            used by Google to do a sanity check for the
            policy. It must be a valid URL.
        accept_defective_only (bool):
            Optional. This field specifies if merchant
            only accepts defective products for returns.

            This field is a member of `oneof`_ ``_accept_defective_only``.
        process_refund_days (int):
            Optional. The field specifies the number of
            days it takes for merchants to process refunds.

            This field is a member of `oneof`_ ``_process_refund_days``.
        accept_exchange (bool):
            Optional. This field specifies if merchant
            allows customers to exchange products.

            This field is a member of `oneof`_ ``_accept_exchange``.
        return_label_source (google.shopping.merchant_accounts_v1beta.types.OnlineReturnPolicy.ReturnLabelSource):
            Optional. The field specifies the return
            label source.

            This field is a member of `oneof`_ ``_return_label_source``.
    """

    class ReturnMethod(proto.Enum):
        r"""The available return methods.

        Values:
            RETURN_METHOD_UNSPECIFIED (0):
                Default value. This value is unused.
            BY_MAIL (1):
                Return by mail.
            IN_STORE (2):
                Return in store.
            AT_A_KIOSK (3):
                Return at a kiosk.
        """

        RETURN_METHOD_UNSPECIFIED = 0
        BY_MAIL = 1
        IN_STORE = 2
        AT_A_KIOSK = 3

    class ItemCondition(proto.Enum):
        r"""The available item conditions.

        Values:
            ITEM_CONDITION_UNSPECIFIED (0):
                Default value. This value is unused.
            NEW (1):
                New.
            USED (2):
                Used.
        """

        ITEM_CONDITION_UNSPECIFIED = 0
        NEW = 1
        USED = 2

    class ReturnLabelSource(proto.Enum):
        r"""The available return label sources.

        Values:
            RETURN_LABEL_SOURCE_UNSPECIFIED (0):
                Default value. This value is unused.
            DOWNLOAD_AND_PRINT (1):
                Download and print.
            IN_THE_PACKAGE (2):
                Label include in the package.
            CUSTOMER_RESPONSIBILITY (3):
                Customer to provide.
        """

        RETURN_LABEL_SOURCE_UNSPECIFIED = 0
        DOWNLOAD_AND_PRINT = 1
        IN_THE_PACKAGE = 2
        CUSTOMER_RESPONSIBILITY = 3

    class ReturnShippingFee(proto.Message):
        r"""The return shipping fee. This can either be a fixed fee or a
        boolean to indicate that the customer pays the actual shipping
        cost.

        Attributes:
            type_ (google.shopping.merchant_accounts_v1beta.types.OnlineReturnPolicy.ReturnShippingFee.Type):
                Required. Type of return shipping fee.
            fixed_fee (google.shopping.type.types.Price):
                Fixed return shipping fee amount. This value is only
                applicable when type is ``FIXED``. We will treat the return
                shipping fee as free if type is ``FIXED`` and this value is
                not set.
        """

        class Type(proto.Enum):
            r"""Return shipping fee types.

            Values:
                TYPE_UNSPECIFIED (0):
                    Default value. This value is unused.
                FIXED (1):
                    The return shipping fee is a fixed value.
                CUSTOMER_PAYING_ACTUAL_FEE (2):
                    Customers will pay the actual return shipping
                    fee.
            """

            TYPE_UNSPECIFIED = 0
            FIXED = 1
            CUSTOMER_PAYING_ACTUAL_FEE = 2

        type_: "OnlineReturnPolicy.ReturnShippingFee.Type" = proto.Field(
            proto.ENUM,
            number=1,
            enum="OnlineReturnPolicy.ReturnShippingFee.Type",
        )
        fixed_fee: types.Price = proto.Field(
            proto.MESSAGE,
            number=2,
            message=types.Price,
        )

    class RestockingFee(proto.Message):
        r"""The restocking fee. This can be a flat fee or a micro
        percent.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            fixed_fee (google.shopping.type.types.Price):
                Fixed restocking fee.

                This field is a member of `oneof`_ ``type``.
            micro_percent (int):
                Percent of total price in micros. 15,000,000
                means 15% of the total price would be charged.

                This field is a member of `oneof`_ ``type``.
        """

        fixed_fee: types.Price = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="type",
            message=types.Price,
        )
        micro_percent: int = proto.Field(
            proto.INT32,
            number=2,
            oneof="type",
        )

    class Policy(proto.Message):
        r"""The available policies.

        Attributes:
            type_ (google.shopping.merchant_accounts_v1beta.types.OnlineReturnPolicy.Policy.Type):
                Policy type.
            days (int):
                The number of days items can be returned after delivery,
                where one day is defined as 24 hours after the delivery
                timestamp. Required for ``NUMBER_OF_DAYS_AFTER_DELIVERY``
                returns.
        """

        class Type(proto.Enum):
            r"""Return policy types.

            Values:
                TYPE_UNSPECIFIED (0):
                    Default value. This value is unused.
                NUMBER_OF_DAYS_AFTER_DELIVERY (1):
                    The number of days within which a return is
                    valid after delivery.
                NO_RETURNS (2):
                    No returns.
                LIFETIME_RETURNS (3):
                    Life time returns.
            """

            TYPE_UNSPECIFIED = 0
            NUMBER_OF_DAYS_AFTER_DELIVERY = 1
            NO_RETURNS = 2
            LIFETIME_RETURNS = 3

        type_: "OnlineReturnPolicy.Policy.Type" = proto.Field(
            proto.ENUM,
            number=1,
            enum="OnlineReturnPolicy.Policy.Type",
        )
        days: int = proto.Field(
            proto.INT64,
            number=2,
        )

    class SeasonalOverride(proto.Message):
        r"""

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            return_days (int):
                Number of days (from the delivery date) that
                the product can be returned.

                This field is a member of `oneof`_ ``return_window``.
            return_until_date (google.type.date_pb2.Date):
                Fixed end date until which the product can be
                returned.

                This field is a member of `oneof`_ ``return_window``.
            label (str):
                Required. Display name of this seasonal
                override in Merchant Center.
            start_date (google.type.date_pb2.Date):
                Required. Defines the date range when this seasonal override
                applies. Both start_date and end_date are inclusive. The
                dates of the seasonal overrides should not overlap.
            end_date (google.type.date_pb2.Date):
                Required. seasonal override end date
                (inclusive).
        """

        return_days: int = proto.Field(
            proto.INT32,
            number=5,
            oneof="return_window",
        )
        return_until_date: date_pb2.Date = proto.Field(
            proto.MESSAGE,
            number=6,
            oneof="return_window",
            message=date_pb2.Date,
        )
        label: str = proto.Field(
            proto.STRING,
            number=1,
        )
        start_date: date_pb2.Date = proto.Field(
            proto.MESSAGE,
            number=2,
            message=date_pb2.Date,
        )
        end_date: date_pb2.Date = proto.Field(
            proto.MESSAGE,
            number=3,
            message=date_pb2.Date,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    return_policy_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    label: str = proto.Field(
        proto.STRING,
        number=3,
    )
    countries: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    policy: Policy = proto.Field(
        proto.MESSAGE,
        number=5,
        message=Policy,
    )
    seasonal_overrides: MutableSequence[SeasonalOverride] = proto.RepeatedField(
        proto.MESSAGE,
        number=14,
        message=SeasonalOverride,
    )
    restocking_fee: RestockingFee = proto.Field(
        proto.MESSAGE,
        number=6,
        message=RestockingFee,
    )
    return_methods: MutableSequence[ReturnMethod] = proto.RepeatedField(
        proto.ENUM,
        number=7,
        enum=ReturnMethod,
    )
    item_conditions: MutableSequence[ItemCondition] = proto.RepeatedField(
        proto.ENUM,
        number=8,
        enum=ItemCondition,
    )
    return_shipping_fee: ReturnShippingFee = proto.Field(
        proto.MESSAGE,
        number=9,
        message=ReturnShippingFee,
    )
    return_policy_uri: str = proto.Field(
        proto.STRING,
        number=10,
    )
    accept_defective_only: bool = proto.Field(
        proto.BOOL,
        number=11,
        optional=True,
    )
    process_refund_days: int = proto.Field(
        proto.INT32,
        number=12,
        optional=True,
    )
    accept_exchange: bool = proto.Field(
        proto.BOOL,
        number=13,
        optional=True,
    )
    return_label_source: ReturnLabelSource = proto.Field(
        proto.ENUM,
        number=15,
        optional=True,
        enum=ReturnLabelSource,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
