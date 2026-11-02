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

from google.cloud.channel_v1.types import billing_accounts, common, repricing
from google.cloud.channel_v1.types import (
    channel_partner_links as gcc_channel_partner_links,
)
from google.cloud.channel_v1.types import customers as gcc_customers
from google.cloud.channel_v1.types import entitlement_changes as gcc_entitlement_changes
from google.cloud.channel_v1.types import entitlements as gcc_entitlements
from google.cloud.channel_v1.types import offers as gcc_offers
from google.cloud.channel_v1.types import products as gcc_products

__protobuf__ = proto.module(
    package="google.cloud.channel.v1",
    manifest={
        "CheckCloudIdentityAccountsExistRequest",
        "CloudIdentityCustomerAccount",
        "CheckCloudIdentityAccountsExistResponse",
        "ListCustomersRequest",
        "ListCustomersResponse",
        "GetCustomerRequest",
        "CreateCustomerRequest",
        "UpdateCustomerRequest",
        "DeleteCustomerRequest",
        "ImportCustomerRequest",
        "ProvisionCloudIdentityRequest",
        "ListEntitlementsRequest",
        "ListEntitlementsResponse",
        "ListTransferableSkusRequest",
        "ListTransferableSkusResponse",
        "ListTransferableOffersRequest",
        "ListTransferableOffersResponse",
        "TransferableOffer",
        "GetEntitlementRequest",
        "ListChannelPartnerLinksRequest",
        "ListChannelPartnerLinksResponse",
        "GetChannelPartnerLinkRequest",
        "CreateChannelPartnerLinkRequest",
        "UpdateChannelPartnerLinkRequest",
        "GetCustomerRepricingConfigRequest",
        "ListCustomerRepricingConfigsRequest",
        "ListCustomerRepricingConfigsResponse",
        "CreateCustomerRepricingConfigRequest",
        "UpdateCustomerRepricingConfigRequest",
        "DeleteCustomerRepricingConfigRequest",
        "GetChannelPartnerRepricingConfigRequest",
        "ListChannelPartnerRepricingConfigsRequest",
        "ListChannelPartnerRepricingConfigsResponse",
        "CreateChannelPartnerRepricingConfigRequest",
        "UpdateChannelPartnerRepricingConfigRequest",
        "DeleteChannelPartnerRepricingConfigRequest",
        "ListSkuGroupsRequest",
        "ListSkuGroupBillableSkusRequest",
        "ListSkuGroupsResponse",
        "ListSkuGroupBillableSkusResponse",
        "SkuGroup",
        "BillableSku",
        "CreateEntitlementRequest",
        "TransferEntitlementsRequest",
        "TransferEntitlementsResponse",
        "TransferEntitlementsToGoogleRequest",
        "ChangeParametersRequest",
        "ChangeRenewalSettingsRequest",
        "ChangeOfferRequest",
        "StartPaidServiceRequest",
        "CancelEntitlementRequest",
        "SuspendEntitlementRequest",
        "ActivateEntitlementRequest",
        "LookupOfferRequest",
        "ListProductsRequest",
        "ListProductsResponse",
        "ListSkusRequest",
        "ListSkusResponse",
        "ListOffersRequest",
        "ListOffersResponse",
        "ListPurchasableSkusRequest",
        "ListPurchasableSkusResponse",
        "PurchasableSku",
        "ListPurchasableOffersRequest",
        "ListPurchasableOffersResponse",
        "PurchasableOffer",
        "QueryEligibleBillingAccountsRequest",
        "QueryEligibleBillingAccountsResponse",
        "SkuPurchaseGroup",
        "BillingAccountPurchaseInfo",
        "RegisterSubscriberRequest",
        "RegisterSubscriberResponse",
        "UnregisterSubscriberRequest",
        "UnregisterSubscriberResponse",
        "ListSubscribersRequest",
        "ListSubscribersResponse",
        "ListEntitlementChangesRequest",
        "ListEntitlementChangesResponse",
    },
)


class CheckCloudIdentityAccountsExistRequest(proto.Message):
    r"""Request message for
    [CloudChannelService.CheckCloudIdentityAccountsExist][google.cloud.channel.v1.CloudChannelService.CheckCloudIdentityAccountsExist].

    Attributes:
        parent (str):
            Required. The reseller account's resource name. Parent uses
            the format: accounts/{account_id}
        domain (str):
            Required. Domain to fetch for Cloud Identity
            account customers, including domain and team
            customers. For team customers, please use the
            domain for their emails.
        primary_admin_email (str):
            Optional. Primary admin email to fetch for
            Cloud Identity account team customer.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    domain: str = proto.Field(
        proto.STRING,
        number=2,
    )
    primary_admin_email: str = proto.Field(
        proto.STRING,
        number=4,
    )


class CloudIdentityCustomerAccount(proto.Message):
    r"""Entity representing a Cloud Identity account that may be
    associated with a Channel Services API partner.

    Attributes:
        existing (bool):
            Returns true if a Cloud Identity account
            exists for a specific domain.
        owned (bool):
            Returns true if the Cloud Identity account is
            associated with a customer of the Channel
            Services partner (with active subscriptions or
            purchase consents).
        customer_name (str):
            If owned = true, the name of the customer that owns the
            Cloud Identity account. Customer_name uses the format:
            accounts/{account_id}/customers/{customer_id}
        customer_cloud_identity_id (str):
            If existing = true, the Cloud Identity ID of
            the customer.
        customer_type (google.cloud.channel_v1.types.CloudIdentityInfo.CustomerType):
            If existing = true, the type of the customer.
        channel_partner_cloud_identity_id (str):
            If existing = true, and is 2-tier customer,
            the channel partner of the customer.
    """

    existing: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    owned: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    customer_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    customer_cloud_identity_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    customer_type: common.CloudIdentityInfo.CustomerType = proto.Field(
        proto.ENUM,
        number=5,
        enum=common.CloudIdentityInfo.CustomerType,
    )
    channel_partner_cloud_identity_id: str = proto.Field(
        proto.STRING,
        number=6,
    )


class CheckCloudIdentityAccountsExistResponse(proto.Message):
    r"""Response message for
    [CloudChannelService.CheckCloudIdentityAccountsExist][google.cloud.channel.v1.CloudChannelService.CheckCloudIdentityAccountsExist].

    Attributes:
        cloud_identity_accounts (MutableSequence[google.cloud.channel_v1.types.CloudIdentityCustomerAccount]):
            The Cloud Identity accounts associated with
            the domain.
    """

    cloud_identity_accounts: MutableSequence["CloudIdentityCustomerAccount"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="CloudIdentityCustomerAccount",
        )
    )


class ListCustomersRequest(proto.Message):
    r"""Request message for
    [CloudChannelService.ListCustomers][google.cloud.channel.v1.CloudChannelService.ListCustomers]

    Attributes:
        parent (str):
            Required. The resource name of the reseller account to list
            customers from. Parent uses the format:
            accounts/{account_id}.
        page_size (int):
            Optional. The maximum number of customers to
            return. The service may return fewer than this
            value. If unspecified, returns at most 10
            customers. The maximum value is 50.
        page_token (str):
            Optional. A token identifying a page of results other than
            the first page. Obtained through
            [ListCustomersResponse.next_page_token][google.cloud.channel.v1.ListCustomersResponse.next_page_token]
            of the previous
            [CloudChannelService.ListCustomers][google.cloud.channel.v1.CloudChannelService.ListCustomers]
            call.
        filter (str):
            Optional. Filters applied to the
            [CloudChannelService.ListCustomers] results. See
            https://cloud.google.com/channel/docs/concepts/google-cloud/filter-customers
            for more information.
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
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListCustomersResponse(proto.Message):
    r"""Response message for
    [CloudChannelService.ListCustomers][google.cloud.channel.v1.CloudChannelService.ListCustomers].

    Attributes:
        customers (MutableSequence[google.cloud.channel_v1.types.Customer]):
            The customers belonging to a reseller or
            distributor.
        next_page_token (str):
            A token to retrieve the next page of results. Pass to
            [ListCustomersRequest.page_token][google.cloud.channel.v1.ListCustomersRequest.page_token]
            to obtain that page.
    """

    @property
    def raw_page(self):
        return self

    customers: MutableSequence[gcc_customers.Customer] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcc_customers.Customer,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetCustomerRequest(proto.Message):
    r"""Request message for
    [CloudChannelService.GetCustomer][google.cloud.channel.v1.CloudChannelService.GetCustomer].

    Attributes:
        name (str):
            Required. The resource name of the customer to retrieve.
            Name uses the format:
            accounts/{account_id}/customers/{customer_id}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateCustomerRequest(proto.Message):
    r"""Request message for
    [CloudChannelService.CreateCustomer][google.cloud.channel.v1.CloudChannelService.CreateCustomer]

    Attributes:
        parent (str):
            Required. The resource name of reseller account in which to
            create the customer. Parent uses the format:
            accounts/{account_id}
        customer (google.cloud.channel_v1.types.Customer):
            Required. The customer to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    customer: gcc_customers.Customer = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcc_customers.Customer,
    )


class UpdateCustomerRequest(proto.Message):
    r"""Request message for
    [CloudChannelService.UpdateCustomer][google.cloud.channel.v1.CloudChannelService.UpdateCustomer].

    Attributes:
        customer (google.cloud.channel_v1.types.Customer):
            Required. New contents of the customer.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The update mask that applies to the resource.
            Optional.
    """

    customer: gcc_customers.Customer = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcc_customers.Customer,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=3,
        message=field_mask_pb2.FieldMask,
    )


class DeleteCustomerRequest(proto.Message):
    r"""Request message for
    [CloudChannelService.DeleteCustomer][google.cloud.channel.v1.CloudChannelService.DeleteCustomer].

    Attributes:
        name (str):
            Required. The resource name of the customer
            to delete.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ImportCustomerRequest(proto.Message):
    r"""Request message for
    [CloudChannelService.ImportCustomer][google.cloud.channel.v1.CloudChannelService.ImportCustomer]

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        domain (str):
            Required. Customer domain.

            This field is a member of `oneof`_ ``customer_identity``.
        cloud_identity_id (str):
            Required. Customer's Cloud Identity ID

            This field is a member of `oneof`_ ``customer_identity``.
        primary_admin_email (str):
            Required. Customer's primary admin email.

            This field is a member of `oneof`_ ``customer_identity``.
        parent (str):
            Required. The resource name of the reseller's account.
            Parent takes the format: accounts/{account_id} or
            accounts/{account_id}/channelPartnerLinks/{channel_partner_id}
        auth_token (str):
            Optional. The super admin of the resold
            customer generates this token to authorize a
            reseller to access their Cloud Identity and
            purchase entitlements on their behalf. You can
            omit this token after authorization. See
            https://support.google.com/a/answer/7643790 for
            more details.
        overwrite_if_exists (bool):
            Required. Choose to overwrite an existing
            customer if found. This must be set to true if
            there is an existing customer with a conflicting
            region code or domain.
        channel_partner_id (str):
            Optional. Cloud Identity ID of a channel
            partner who will be the direct reseller for the
            customer's order. This field is required for
            2-tier transfer scenarios and can be provided
            via the request Parent binding as well.
        customer (str):
            Optional. Specifies the customer that will receive imported
            Cloud Identity information. Format:
            accounts/{account_id}/customers/{customer_id}
    """

    domain: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="customer_identity",
    )
    cloud_identity_id: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="customer_identity",
    )
    primary_admin_email: str = proto.Field(
        proto.STRING,
        number=8,
        oneof="customer_identity",
    )
    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    auth_token: str = proto.Field(
        proto.STRING,
        number=4,
    )
    overwrite_if_exists: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    channel_partner_id: str = proto.Field(
        proto.STRING,
        number=6,
    )
    customer: str = proto.Field(
        proto.STRING,
        number=7,
    )


class ProvisionCloudIdentityRequest(proto.Message):
    r"""Request message for
    [CloudChannelService.ProvisionCloudIdentity][google.cloud.channel.v1.CloudChannelService.ProvisionCloudIdentity]

    Attributes:
        customer (str):
            Required. Resource name of the customer. Format:
            accounts/{account_id}/customers/{customer_id}
        cloud_identity_info (google.cloud.channel_v1.types.CloudIdentityInfo):
            CloudIdentity-specific customer information.
        user (google.cloud.channel_v1.types.AdminUser):
            Admin user information.
        validate_only (bool):
            Validate the request and preview the review,
            but do not post it.
    """

    customer: str = proto.Field(
        proto.STRING,
        number=1,
    )
    cloud_identity_info: common.CloudIdentityInfo = proto.Field(
        proto.MESSAGE,
        number=2,
        message=common.CloudIdentityInfo,
    )
    user: common.AdminUser = proto.Field(
        proto.MESSAGE,
        number=3,
        message=common.AdminUser,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class ListEntitlementsRequest(proto.Message):
    r"""Request message for
    [CloudChannelService.ListEntitlements][google.cloud.channel.v1.CloudChannelService.ListEntitlements]

    Attributes:
        parent (str):
            Required. The resource name of the reseller's customer
            account to list entitlements for. Parent uses the format:
            accounts/{account_id}/customers/{customer_id}
        page_size (int):
            Optional. Requested page size. Server might
            return fewer results than requested. If
            unspecified, return at most 50 entitlements. The
            maximum value is 100; the server will coerce
            values above 100.
        page_token (str):
            Optional. A token for a page of results other than the first
            page. Obtained using
            [ListEntitlementsResponse.next_page_token][google.cloud.channel.v1.ListEntitlementsResponse.next_page_token]
            of the previous
            [CloudChannelService.ListEntitlements][google.cloud.channel.v1.CloudChannelService.ListEntitlements]
            call.
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


class ListEntitlementsResponse(proto.Message):
    r"""Response message for
    [CloudChannelService.ListEntitlements][google.cloud.channel.v1.CloudChannelService.ListEntitlements].

    Attributes:
        entitlements (MutableSequence[google.cloud.channel_v1.types.Entitlement]):
            The reseller customer's entitlements.
        next_page_token (str):
            A token to list the next page of results. Pass to
            [ListEntitlementsRequest.page_token][google.cloud.channel.v1.ListEntitlementsRequest.page_token]
            to obtain that page.
    """

    @property
    def raw_page(self):
        return self

    entitlements: MutableSequence[gcc_entitlements.Entitlement] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcc_entitlements.Entitlement,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListTransferableSkusRequest(proto.Message):
    r"""Request message for
    [CloudChannelService.ListTransferableSkus][google.cloud.channel.v1.CloudChannelService.ListTransferableSkus]

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        cloud_identity_id (str):
            Customer's Cloud Identity ID

            This field is a member of `oneof`_ ``transferred_customer_identity``.
        customer_name (str):
            A reseller is required to create a customer and use the
            resource name of the created customer here. Customer_name
            uses the format:
            accounts/{account_id}/customers/{customer_id}

            This field is a member of `oneof`_ ``transferred_customer_identity``.
        parent (str):
            Required. The reseller account's resource name. Parent uses
            the format: accounts/{account_id}
        page_size (int):
            The requested page size. Server might return
            fewer results than requested. If unspecified,
            returns at most 100 SKUs. The maximum value is
            1000; the server will coerce values above 1000.
            Optional.
        page_token (str):
            A token for a page of results other than the first page.
            Obtained using
            [ListTransferableSkusResponse.next_page_token][google.cloud.channel.v1.ListTransferableSkusResponse.next_page_token]
            of the previous
            [CloudChannelService.ListTransferableSkus][google.cloud.channel.v1.CloudChannelService.ListTransferableSkus]
            call. Optional.
        auth_token (str):
            Optional. The super admin of the resold
            customer generates this token to authorize a
            reseller to access their Cloud Identity and
            purchase entitlements on their behalf. You can
            omit this token after authorization. See
            https://support.google.com/a/answer/7643790 for
            more details.
        language_code (str):
            The BCP-47 language code. For example,
            "en-US". The response will localize in the
            corresponding language code, if specified. The
            default value is "en-US".
            Optional.
    """

    cloud_identity_id: str = proto.Field(
        proto.STRING,
        number=4,
        oneof="transferred_customer_identity",
    )
    customer_name: str = proto.Field(
        proto.STRING,
        number=7,
        oneof="transferred_customer_identity",
    )
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
    auth_token: str = proto.Field(
        proto.STRING,
        number=5,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=6,
    )


class ListTransferableSkusResponse(proto.Message):
    r"""Response message for
    [CloudChannelService.ListTransferableSkus][google.cloud.channel.v1.CloudChannelService.ListTransferableSkus].

    Attributes:
        transferable_skus (MutableSequence[google.cloud.channel_v1.types.TransferableSku]):
            Information about existing SKUs for a
            customer that needs a transfer.
        next_page_token (str):
            A token to retrieve the next page of results. Pass to
            [ListTransferableSkusRequest.page_token][google.cloud.channel.v1.ListTransferableSkusRequest.page_token]
            to obtain that page.
    """

    @property
    def raw_page(self):
        return self

    transferable_skus: MutableSequence[gcc_entitlements.TransferableSku] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=gcc_entitlements.TransferableSku,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListTransferableOffersRequest(proto.Message):
    r"""Request message for
    [CloudChannelService.ListTransferableOffers][google.cloud.channel.v1.CloudChannelService.ListTransferableOffers]

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        cloud_identity_id (str):
            Customer's Cloud Identity ID

            This field is a member of `oneof`_ ``transferred_customer_identity``.
        customer_name (str):
            A reseller should create a customer and use
            the resource name of that customer here.

            This field is a member of `oneof`_ ``transferred_customer_identity``.
        parent (str):
            Required. The resource name of the reseller's
            account.
        page_size (int):
            Requested page size. Server might return
            fewer results than requested. If unspecified,
            returns at most 100 offers. The maximum value is
            1000; the server will coerce values above 1000.
        page_token (str):
            A token for a page of results other than the first page.
            Obtained using
            [ListTransferableOffersResponse.next_page_token][google.cloud.channel.v1.ListTransferableOffersResponse.next_page_token]
            of the previous
            [CloudChannelService.ListTransferableOffers][google.cloud.channel.v1.CloudChannelService.ListTransferableOffers]
            call.
        sku (str):
            Required. The SKU to look up Offers for.
        language_code (str):
            Optional. The BCP-47 language code. For
            example, "en-US". The response will localize in
            the corresponding language code, if specified.
            The default value is "en-US".
        billing_account (str):
            Optional. The Billing Account to look up Offers for. Format:
            accounts/{account_id}/billingAccounts/{billing_account_id}.

            This field is only relevant for multi-currency accounts. It
            should be left empty for single currency accounts.
    """

    cloud_identity_id: str = proto.Field(
        proto.STRING,
        number=4,
        oneof="transferred_customer_identity",
    )
    customer_name: str = proto.Field(
        proto.STRING,
        number=5,
        oneof="transferred_customer_identity",
    )
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
    sku: str = proto.Field(
        proto.STRING,
        number=6,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=7,
    )
    billing_account: str = proto.Field(
        proto.STRING,
        number=8,
    )


class ListTransferableOffersResponse(proto.Message):
    r"""Response message for
    [CloudChannelService.ListTransferableOffers][google.cloud.channel.v1.CloudChannelService.ListTransferableOffers].

    Attributes:
        transferable_offers (MutableSequence[google.cloud.channel_v1.types.TransferableOffer]):
            Information about Offers for a customer that
            can be used for transfer.
        next_page_token (str):
            A token to retrieve the next page of results. Pass to
            [ListTransferableOffersRequest.page_token][google.cloud.channel.v1.ListTransferableOffersRequest.page_token]
            to obtain that page.
    """

    @property
    def raw_page(self):
        return self

    transferable_offers: MutableSequence["TransferableOffer"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="TransferableOffer",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class TransferableOffer(proto.Message):
    r"""TransferableOffer represents an Offer that can be used in
    Transfer. Read-only.

    Attributes:
        offer (google.cloud.channel_v1.types.Offer):
            Offer with parameter constraints updated to
            allow the Transfer.
        price_reference_id (str):
            Optional. Price reference ID for the offer.
            Only for offers that require additional price
            information. Used to guarantee that the pricing
            is consistent between quoting the offer and
            placing the order.
    """

    offer: gcc_offers.Offer = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcc_offers.Offer,
    )
    price_reference_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetEntitlementRequest(proto.Message):
    r"""Request message for
    [CloudChannelService.GetEntitlement][google.cloud.channel.v1.CloudChannelService.GetEntitlement].

    Attributes:
        name (str):
            Required. The resource name of the entitlement to retrieve.
            Name uses the format:
            accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListChannelPartnerLinksRequest(proto.Message):
    r"""Request message for
    [CloudChannelService.ListChannelPartnerLinks][google.cloud.channel.v1.CloudChannelService.ListChannelPartnerLinks]

    Attributes:
        parent (str):
            Required. The resource name of the reseller account for
            listing channel partner links. Parent uses the format:
            accounts/{account_id}
        page_size (int):
            Optional. Requested page size. Server might
            return fewer results than requested. If
            unspecified, server will pick a default size
            (25). The maximum value is 200; the server will
            coerce values above 200.
        page_token (str):
            Optional. A token for a page of results other than the first
            page. Obtained using
            [ListChannelPartnerLinksResponse.next_page_token][google.cloud.channel.v1.ListChannelPartnerLinksResponse.next_page_token]
            of the previous
            [CloudChannelService.ListChannelPartnerLinks][google.cloud.channel.v1.CloudChannelService.ListChannelPartnerLinks]
            call.
        view (google.cloud.channel_v1.types.ChannelPartnerLinkView):
            Optional. The level of granularity the
            ChannelPartnerLink will display.
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
    view: gcc_channel_partner_links.ChannelPartnerLinkView = proto.Field(
        proto.ENUM,
        number=4,
        enum=gcc_channel_partner_links.ChannelPartnerLinkView,
    )


class ListChannelPartnerLinksResponse(proto.Message):
    r"""Response message for
    [CloudChannelService.ListChannelPartnerLinks][google.cloud.channel.v1.CloudChannelService.ListChannelPartnerLinks].

    Attributes:
        channel_partner_links (MutableSequence[google.cloud.channel_v1.types.ChannelPartnerLink]):
            The Channel partner links for a reseller.
        next_page_token (str):
            A token to retrieve the next page of results. Pass to
            [ListChannelPartnerLinksRequest.page_token][google.cloud.channel.v1.ListChannelPartnerLinksRequest.page_token]
            to obtain that page.
    """

    @property
    def raw_page(self):
        return self

    channel_partner_links: MutableSequence[
        gcc_channel_partner_links.ChannelPartnerLink
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcc_channel_partner_links.ChannelPartnerLink,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetChannelPartnerLinkRequest(proto.Message):
    r"""Request message for
    [CloudChannelService.GetChannelPartnerLink][google.cloud.channel.v1.CloudChannelService.GetChannelPartnerLink].

    Attributes:
        name (str):
            Required. The resource name of the channel partner link to
            retrieve. Name uses the format:
            accounts/{account_id}/channelPartnerLinks/{id} where {id} is
            the Cloud Identity ID of the partner.
        view (google.cloud.channel_v1.types.ChannelPartnerLinkView):
            Optional. The level of granularity the
            ChannelPartnerLink will display.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    view: gcc_channel_partner_links.ChannelPartnerLinkView = proto.Field(
        proto.ENUM,
        number=2,
        enum=gcc_channel_partner_links.ChannelPartnerLinkView,
    )


class CreateChannelPartnerLinkRequest(proto.Message):
    r"""Request message for
    [CloudChannelService.CreateChannelPartnerLink][google.cloud.channel.v1.CloudChannelService.CreateChannelPartnerLink]

    Attributes:
        parent (str):
            Required. Create a channel partner link for the provided
            reseller account's resource name. Parent uses the format:
            accounts/{account_id}
        channel_partner_link (google.cloud.channel_v1.types.ChannelPartnerLink):
            Required. The channel partner link to create. Either
            channel_partner_link.reseller_cloud_identity_id or domain
            can be used to create a link.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    channel_partner_link: gcc_channel_partner_links.ChannelPartnerLink = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcc_channel_partner_links.ChannelPartnerLink,
    )


class UpdateChannelPartnerLinkRequest(proto.Message):
    r"""Request message for
    [CloudChannelService.UpdateChannelPartnerLink][google.cloud.channel.v1.CloudChannelService.UpdateChannelPartnerLink]

    Attributes:
        name (str):
            Required. The resource name of the channel partner link to
            cancel. Name uses the format:
            accounts/{account_id}/channelPartnerLinks/{id} where {id} is
            the Cloud Identity ID of the partner.
        channel_partner_link (google.cloud.channel_v1.types.ChannelPartnerLink):
            Required. The channel partner link to update. Only
            channel_partner_link.link_state is allowed for updates.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The update mask that applies to the resource. The
            only allowable value for an update mask is
            channel_partner_link.link_state.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    channel_partner_link: gcc_channel_partner_links.ChannelPartnerLink = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcc_channel_partner_links.ChannelPartnerLink,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=3,
        message=field_mask_pb2.FieldMask,
    )


class GetCustomerRepricingConfigRequest(proto.Message):
    r"""Request message for
    [CloudChannelService.GetCustomerRepricingConfig][google.cloud.channel.v1.CloudChannelService.GetCustomerRepricingConfig].

    Attributes:
        name (str):
            Required. The resource name of the CustomerRepricingConfig.
            Format:
            accounts/{account_id}/customers/{customer_id}/customerRepricingConfigs/{id}.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListCustomerRepricingConfigsRequest(proto.Message):
    r"""Request message for
    [CloudChannelService.ListCustomerRepricingConfigs][google.cloud.channel.v1.CloudChannelService.ListCustomerRepricingConfigs].

    Attributes:
        parent (str):
            Required. The resource name of the customer. Parent uses the
            format: accounts/{account_id}/customers/{customer_id}.
            Supports accounts/{account_id}/customers/- to retrieve
            configs for all customers.
        page_size (int):
            Optional. The maximum number of repricing
            configs to return. The service may return fewer
            than this value. If unspecified, returns a
            maximum of 50 rules. The maximum value is 100;
            values above 100 will be coerced to 100.
        page_token (str):
            Optional. A token identifying a page of results beyond the
            first page. Obtained through
            [ListCustomerRepricingConfigsResponse.next_page_token][google.cloud.channel.v1.ListCustomerRepricingConfigsResponse.next_page_token]
            of the previous
            [CloudChannelService.ListCustomerRepricingConfigs][google.cloud.channel.v1.CloudChannelService.ListCustomerRepricingConfigs]
            call.
        filter (str):
            Optional. A filter for
            [CloudChannelService.ListCustomerRepricingConfigs] results
            (customer only). You can use this filter when you support a
            BatchGet-like query. To use the filter, you must set
            ``parent=accounts/{account_id}/customers/-``.

            Example: customer = accounts/account_id/customers/c1 OR
            customer = accounts/account_id/customers/c2.
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
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListCustomerRepricingConfigsResponse(proto.Message):
    r"""Response message for
    [CloudChannelService.ListCustomerRepricingConfigs][google.cloud.channel.v1.CloudChannelService.ListCustomerRepricingConfigs].

    Attributes:
        customer_repricing_configs (MutableSequence[google.cloud.channel_v1.types.CustomerRepricingConfig]):
            The repricing configs for this channel
            partner.
        next_page_token (str):
            A token to retrieve the next page of results. Pass to
            [ListCustomerRepricingConfigsRequest.page_token][google.cloud.channel.v1.ListCustomerRepricingConfigsRequest.page_token]
            to obtain that page.
    """

    @property
    def raw_page(self):
        return self

    customer_repricing_configs: MutableSequence[repricing.CustomerRepricingConfig] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=repricing.CustomerRepricingConfig,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateCustomerRepricingConfigRequest(proto.Message):
    r"""Request message for
    [CloudChannelService.CreateCustomerRepricingConfig][google.cloud.channel.v1.CloudChannelService.CreateCustomerRepricingConfig].

    Attributes:
        parent (str):
            Required. The resource name of the customer that will
            receive this repricing config. Parent uses the format:
            accounts/{account_id}/customers/{customer_id}
        customer_repricing_config (google.cloud.channel_v1.types.CustomerRepricingConfig):
            Required. The CustomerRepricingConfig object
            to update.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    customer_repricing_config: repricing.CustomerRepricingConfig = proto.Field(
        proto.MESSAGE,
        number=2,
        message=repricing.CustomerRepricingConfig,
    )


class UpdateCustomerRepricingConfigRequest(proto.Message):
    r"""Request message for
    [CloudChannelService.UpdateCustomerRepricingConfig][google.cloud.channel.v1.CloudChannelService.UpdateCustomerRepricingConfig].

    Attributes:
        customer_repricing_config (google.cloud.channel_v1.types.CustomerRepricingConfig):
            Required. The CustomerRepricingConfig object
            to update.
    """

    customer_repricing_config: repricing.CustomerRepricingConfig = proto.Field(
        proto.MESSAGE,
        number=1,
        message=repricing.CustomerRepricingConfig,
    )


class DeleteCustomerRepricingConfigRequest(proto.Message):
    r"""Request message for
    [CloudChannelService.DeleteCustomerRepricingConfig][google.cloud.channel.v1.CloudChannelService.DeleteCustomerRepricingConfig].

    Attributes:
        name (str):
            Required. The resource name of the customer repricing config
            rule to delete. Format:
            accounts/{account_id}/customers/{customer_id}/customerRepricingConfigs/{id}.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetChannelPartnerRepricingConfigRequest(proto.Message):
    r"""Request message for
    [CloudChannelService.GetChannelPartnerRepricingConfig][google.cloud.channel.v1.CloudChannelService.GetChannelPartnerRepricingConfig]

    Attributes:
        name (str):
            Required. The resource name of the
            ChannelPartnerRepricingConfig Format:
            accounts/{account_id}/channelPartnerLinks/{channel_partner_id}/channelPartnerRepricingConfigs/{id}.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListChannelPartnerRepricingConfigsRequest(proto.Message):
    r"""Request message for
    [CloudChannelService.ListChannelPartnerRepricingConfigs][google.cloud.channel.v1.CloudChannelService.ListChannelPartnerRepricingConfigs].

    Attributes:
        parent (str):
            Required. The resource name of the account's
            [ChannelPartnerLink][google.cloud.channel.v1.ChannelPartnerLink].
            Parent uses the format:
            accounts/{account_id}/channelPartnerLinks/{channel_partner_id}.
            Supports accounts/{account_id}/channelPartnerLinks/- to
            retrieve configs for all channel partners.
        page_size (int):
            Optional. The maximum number of repricing
            configs to return. The service may return fewer
            than this value. If unspecified, returns a
            maximum of 50 rules. The maximum value is 100;
            values above 100 will be coerced to 100.
        page_token (str):
            Optional. A token identifying a page of results beyond the
            first page. Obtained through
            [ListChannelPartnerRepricingConfigsResponse.next_page_token][google.cloud.channel.v1.ListChannelPartnerRepricingConfigsResponse.next_page_token]
            of the previous
            [CloudChannelService.ListChannelPartnerRepricingConfigs][google.cloud.channel.v1.CloudChannelService.ListChannelPartnerRepricingConfigs]
            call.
        filter (str):
            Optional. A filter for
            [CloudChannelService.ListChannelPartnerRepricingConfigs]
            results (channel_partner_link only). You can use this filter
            when you support a BatchGet-like query. To use the filter,
            you must set
            ``parent=accounts/{account_id}/channelPartnerLinks/-``.

            Example:
            ``channel_partner_link = accounts/account_id/channelPartnerLinks/c1``
            OR
            ``channel_partner_link = accounts/account_id/channelPartnerLinks/c2``.
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
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListChannelPartnerRepricingConfigsResponse(proto.Message):
    r"""Response message for
    [CloudChannelService.ListChannelPartnerRepricingConfigs][google.cloud.channel.v1.CloudChannelService.ListChannelPartnerRepricingConfigs].

    Attributes:
        channel_partner_repricing_configs (MutableSequence[google.cloud.channel_v1.types.ChannelPartnerRepricingConfig]):
            The repricing configs for this channel
            partner.
        next_page_token (str):
            A token to retrieve the next page of results. Pass to
            [ListChannelPartnerRepricingConfigsRequest.page_token][google.cloud.channel.v1.ListChannelPartnerRepricingConfigsRequest.page_token]
            to obtain that page.
    """

    @property
    def raw_page(self):
        return self

    channel_partner_repricing_configs: MutableSequence[
        repricing.ChannelPartnerRepricingConfig
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=repricing.ChannelPartnerRepricingConfig,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateChannelPartnerRepricingConfigRequest(proto.Message):
    r"""Request message for
    [CloudChannelService.CreateChannelPartnerRepricingConfig][google.cloud.channel.v1.CloudChannelService.CreateChannelPartnerRepricingConfig].

    Attributes:
        parent (str):
            Required. The resource name of the ChannelPartner that will
            receive the repricing config. Parent uses the format:
            accounts/{account_id}/channelPartnerLinks/{channel_partner_id}
        channel_partner_repricing_config (google.cloud.channel_v1.types.ChannelPartnerRepricingConfig):
            Required. The ChannelPartnerRepricingConfig
            object to update.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    channel_partner_repricing_config: repricing.ChannelPartnerRepricingConfig = (
        proto.Field(
            proto.MESSAGE,
            number=2,
            message=repricing.ChannelPartnerRepricingConfig,
        )
    )


class UpdateChannelPartnerRepricingConfigRequest(proto.Message):
    r"""Request message for
    [CloudChannelService.UpdateChannelPartnerRepricingConfig][google.cloud.channel.v1.CloudChannelService.UpdateChannelPartnerRepricingConfig].

    Attributes:
        channel_partner_repricing_config (google.cloud.channel_v1.types.ChannelPartnerRepricingConfig):
            Required. The ChannelPartnerRepricingConfig
            object to update.
    """

    channel_partner_repricing_config: repricing.ChannelPartnerRepricingConfig = (
        proto.Field(
            proto.MESSAGE,
            number=1,
            message=repricing.ChannelPartnerRepricingConfig,
        )
    )


class DeleteChannelPartnerRepricingConfigRequest(proto.Message):
    r"""Request message for DeleteChannelPartnerRepricingConfig.

    Attributes:
        name (str):
            Required. The resource name of the channel
            partner repricing config rule to delete.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListSkuGroupsRequest(proto.Message):
    r"""Request message for ListSkuGroups.

    Attributes:
        parent (str):
            Required. The resource name of the account
            from which to list SKU groups. Parent uses the
            format: accounts/{account}.
        page_size (int):
            Optional. The maximum number of SKU groups to
            return. The service may return fewer than this
            value. If unspecified, returns a maximum of 1000
            SKU groups. The maximum value is 1000; values
            above 1000 will be coerced to 1000.
        page_token (str):
            Optional. A token identifying a page of results beyond the
            first page. Obtained through
            [ListSkuGroupsResponse.next_page_token][google.cloud.channel.v1.ListSkuGroupsResponse.next_page_token]
            of the previous
            [CloudChannelService.ListSkuGroups][google.cloud.channel.v1.CloudChannelService.ListSkuGroups]
            call.
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


class ListSkuGroupBillableSkusRequest(proto.Message):
    r"""Request message for ListSkuGroupBillableSkus.

    Attributes:
        parent (str):
            Required. Resource name of the SKU group. Format:
            accounts/{account}/skuGroups/{sku_group}.
        page_size (int):
            Optional. The maximum number of SKUs to
            return. The service may return fewer than this
            value. If unspecified, returns a maximum of
            100000 SKUs. The maximum value is 100000; values
            above 100000 will be coerced to 100000.
        page_token (str):
            Optional. A token identifying a page of results beyond the
            first page. Obtained through
            [ListSkuGroupBillableSkusResponse.next_page_token][google.cloud.channel.v1.ListSkuGroupBillableSkusResponse.next_page_token]
            of the previous
            [CloudChannelService.ListSkuGroupBillableSkus][google.cloud.channel.v1.CloudChannelService.ListSkuGroupBillableSkus]
            call.
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


class ListSkuGroupsResponse(proto.Message):
    r"""Response message for ListSkuGroups.

    Attributes:
        sku_groups (MutableSequence[google.cloud.channel_v1.types.SkuGroup]):
            The list of SKU groups requested.
        next_page_token (str):
            A token to retrieve the next page of results. Pass to
            [ListSkuGroupsRequest.page_token][google.cloud.channel.v1.ListSkuGroupsRequest.page_token]
            to obtain that page.
    """

    @property
    def raw_page(self):
        return self

    sku_groups: MutableSequence["SkuGroup"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="SkuGroup",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListSkuGroupBillableSkusResponse(proto.Message):
    r"""Response message for ListSkuGroupBillableSkus.

    Attributes:
        billable_skus (MutableSequence[google.cloud.channel_v1.types.BillableSku]):
            The list of billable SKUs in the requested
            SKU group.
        next_page_token (str):
            A token to retrieve the next page of results. Pass to
            [ListSkuGroupBillableSkusRequest.page_token][google.cloud.channel.v1.ListSkuGroupBillableSkusRequest.page_token]
            to obtain that page.
    """

    @property
    def raw_page(self):
        return self

    billable_skus: MutableSequence["BillableSku"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="BillableSku",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class SkuGroup(proto.Message):
    r"""Represents the SKU group information.

    Attributes:
        name (str):
            Resource name of SKU group. Format:
            accounts/{account}/skuGroups/{sku_group}. Example:
            "accounts/C01234/skuGroups/3d50fd57-3157-4577-a5a9-a219b8490041".
        display_name (str):
            Unique human readable identifier for the SKU
            group.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )


class BillableSku(proto.Message):
    r"""Represents the Billable SKU information.

    Attributes:
        sku (str):
            Resource name of Billable SKU. Format:

            billableSkus/{sku}.
            Example:

            billableSkus/6E1B-6634-470F".
        sku_display_name (str):
            Unique human readable name for the SKU.
        service (str):
            Resource name of Service which contains
            Repricing SKU. Format: services/{service}.
            Example:

            "services/B7D9-FDCB-15D8".
        service_display_name (str):
            Unique human readable name for the Service.
    """

    sku: str = proto.Field(
        proto.STRING,
        number=1,
    )
    sku_display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    service: str = proto.Field(
        proto.STRING,
        number=3,
    )
    service_display_name: str = proto.Field(
        proto.STRING,
        number=4,
    )


class CreateEntitlementRequest(proto.Message):
    r"""Request message for
    [CloudChannelService.CreateEntitlement][google.cloud.channel.v1.CloudChannelService.CreateEntitlement]

    Attributes:
        parent (str):
            Required. The resource name of the reseller's customer
            account in which to create the entitlement. Parent uses the
            format: accounts/{account_id}/customers/{customer_id}
        entitlement (google.cloud.channel_v1.types.Entitlement):
            Required. The entitlement to create.
        request_id (str):
            Optional. You can specify an optional unique request ID, and
            if you need to retry your request, the server will know to
            ignore the request if it's complete.

            For example, you make an initial request and the request
            times out. If you make the request again with the same
            request ID, the server can check if it received the original
            operation with the same request ID. If it did, it will
            ignore the second request.

            The request ID must be a valid
            `UUID <https://tools.ietf.org/html/rfc4122>`__ with the
            exception that zero UUID is not supported
            (``00000000-0000-0000-0000-000000000000``).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    entitlement: gcc_entitlements.Entitlement = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcc_entitlements.Entitlement,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=5,
    )


class TransferEntitlementsRequest(proto.Message):
    r"""Request message for
    [CloudChannelService.TransferEntitlements][google.cloud.channel.v1.CloudChannelService.TransferEntitlements].

    Attributes:
        parent (str):
            Required. The resource name of the reseller's customer
            account that will receive transferred entitlements. Parent
            uses the format:
            accounts/{account_id}/customers/{customer_id}
        entitlements (MutableSequence[google.cloud.channel_v1.types.Entitlement]):
            Required. The new entitlements to create or
            transfer.
        auth_token (str):
            The super admin of the resold customer
            generates this token to authorize a reseller to
            access their Cloud Identity and purchase
            entitlements on their behalf. You can omit this
            token after authorization. See
            https://support.google.com/a/answer/7643790 for
            more details.
        request_id (str):
            Optional. You can specify an optional unique request ID, and
            if you need to retry your request, the server will know to
            ignore the request if it's complete.

            For example, you make an initial request and the request
            times out. If you make the request again with the same
            request ID, the server can check if it received the original
            operation with the same request ID. If it did, it will
            ignore the second request.

            The request ID must be a valid
            `UUID <https://tools.ietf.org/html/rfc4122>`__ with the
            exception that zero UUID is not supported
            (``00000000-0000-0000-0000-000000000000``).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    entitlements: MutableSequence[gcc_entitlements.Entitlement] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=gcc_entitlements.Entitlement,
    )
    auth_token: str = proto.Field(
        proto.STRING,
        number=4,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=6,
    )


class TransferEntitlementsResponse(proto.Message):
    r"""Response message for
    [CloudChannelService.TransferEntitlements][google.cloud.channel.v1.CloudChannelService.TransferEntitlements].
    This is put in the response field of google.longrunning.Operation.

    Attributes:
        entitlements (MutableSequence[google.cloud.channel_v1.types.Entitlement]):
            The transferred entitlements.
    """

    entitlements: MutableSequence[gcc_entitlements.Entitlement] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcc_entitlements.Entitlement,
    )


class TransferEntitlementsToGoogleRequest(proto.Message):
    r"""Request message for
    [CloudChannelService.TransferEntitlementsToGoogle][google.cloud.channel.v1.CloudChannelService.TransferEntitlementsToGoogle].

    Attributes:
        parent (str):
            Required. The resource name of the reseller's customer
            account where the entitlements transfer from. Parent uses
            the format: accounts/{account_id}/customers/{customer_id}
        entitlements (MutableSequence[google.cloud.channel_v1.types.Entitlement]):
            Required. The entitlements to transfer to
            Google.
        request_id (str):
            Optional. You can specify an optional unique request ID, and
            if you need to retry your request, the server will know to
            ignore the request if it's complete.

            For example, you make an initial request and the request
            times out. If you make the request again with the same
            request ID, the server can check if it received the original
            operation with the same request ID. If it did, it will
            ignore the second request.

            The request ID must be a valid
            `UUID <https://tools.ietf.org/html/rfc4122>`__ with the
            exception that zero UUID is not supported
            (``00000000-0000-0000-0000-000000000000``).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    entitlements: MutableSequence[gcc_entitlements.Entitlement] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=gcc_entitlements.Entitlement,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ChangeParametersRequest(proto.Message):
    r"""Request message for
    [CloudChannelService.ChangeParameters][google.cloud.channel.v1.CloudChannelService.ChangeParameters].

    Attributes:
        name (str):
            Required. The name of the entitlement to update. Name uses
            the format:
            accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id}
        parameters (MutableSequence[google.cloud.channel_v1.types.Parameter]):
            Required. Entitlement parameters to update. You can only
            change editable parameters.

            To view the available Parameters for a request, refer to the
            [Offer.parameter_definitions][google.cloud.channel.v1.Offer.parameter_definitions]
            from the desired offer.
        request_id (str):
            Optional. You can specify an optional unique request ID, and
            if you need to retry your request, the server will know to
            ignore the request if it's complete.

            For example, you make an initial request and the request
            times out. If you make the request again with the same
            request ID, the server can check if it received the original
            operation with the same request ID. If it did, it will
            ignore the second request.

            The request ID must be a valid
            `UUID <https://tools.ietf.org/html/rfc4122>`__ with the
            exception that zero UUID is not supported
            (``00000000-0000-0000-0000-000000000000``).
        purchase_order_id (str):
            Optional. Purchase order ID provided by the
            reseller.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    parameters: MutableSequence[gcc_entitlements.Parameter] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=gcc_entitlements.Parameter,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    purchase_order_id: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ChangeRenewalSettingsRequest(proto.Message):
    r"""Request message for
    [CloudChannelService.ChangeRenewalSettings][google.cloud.channel.v1.CloudChannelService.ChangeRenewalSettings].

    Attributes:
        name (str):
            Required. The name of the entitlement to update. Name uses
            the format:
            accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id}
        renewal_settings (google.cloud.channel_v1.types.RenewalSettings):
            Required. New renewal settings.
        request_id (str):
            Optional. You can specify an optional unique request ID, and
            if you need to retry your request, the server will know to
            ignore the request if it's complete.

            For example, you make an initial request and the request
            times out. If you make the request again with the same
            request ID, the server can check if it received the original
            operation with the same request ID. If it did, it will
            ignore the second request.

            The request ID must be a valid
            `UUID <https://tools.ietf.org/html/rfc4122>`__ with the
            exception that zero UUID is not supported
            (``00000000-0000-0000-0000-000000000000``).
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    renewal_settings: gcc_entitlements.RenewalSettings = proto.Field(
        proto.MESSAGE,
        number=4,
        message=gcc_entitlements.RenewalSettings,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ChangeOfferRequest(proto.Message):
    r"""Request message for
    [CloudChannelService.ChangeOffer][google.cloud.channel.v1.CloudChannelService.ChangeOffer].

    Attributes:
        name (str):
            Required. The resource name of the entitlement to update.
            Name uses the format:
            accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id}
        offer (str):
            Required. New Offer. Format:
            accounts/{account_id}/offers/{offer_id}.
        parameters (MutableSequence[google.cloud.channel_v1.types.Parameter]):
            Optional. Parameters needed to purchase the Offer. To view
            the available Parameters refer to the
            [Offer.parameter_definitions][google.cloud.channel.v1.Offer.parameter_definitions]
            from the desired offer.
        purchase_order_id (str):
            Optional. Purchase order id provided by the
            reseller.
        request_id (str):
            Optional. You can specify an optional unique request ID, and
            if you need to retry your request, the server will know to
            ignore the request if it's complete.

            For example, you make an initial request and the request
            times out. If you make the request again with the same
            request ID, the server can check if it received the original
            operation with the same request ID. If it did, it will
            ignore the second request.

            The request ID must be a valid
            `UUID <https://tools.ietf.org/html/rfc4122>`__ with the
            exception that zero UUID is not supported
            (``00000000-0000-0000-0000-000000000000``).
        billing_account (str):
            Optional. The billing account resource name
            that is used to pay for this entitlement when
            setting up billing on a trial subscription.

            This field is only relevant for multi-currency
            accounts. It should be left empty for single
            currency accounts.
        price_reference_id (str):
            Optional. Price reference ID for the offer.
            Only for offers that require additional price
            information. Used to guarantee that the pricing
            is consistent between quoting the offer and
            placing the order.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    offer: str = proto.Field(
        proto.STRING,
        number=2,
    )
    parameters: MutableSequence[gcc_entitlements.Parameter] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=gcc_entitlements.Parameter,
    )
    purchase_order_id: str = proto.Field(
        proto.STRING,
        number=5,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=6,
    )
    billing_account: str = proto.Field(
        proto.STRING,
        number=7,
    )
    price_reference_id: str = proto.Field(
        proto.STRING,
        number=8,
    )


class StartPaidServiceRequest(proto.Message):
    r"""Request message for
    [CloudChannelService.StartPaidService][google.cloud.channel.v1.CloudChannelService.StartPaidService].

    Attributes:
        name (str):
            Required. The name of the entitlement to start a paid
            service for. Name uses the format:
            accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id}
        request_id (str):
            Optional. You can specify an optional unique request ID, and
            if you need to retry your request, the server will know to
            ignore the request if it's complete.

            For example, you make an initial request and the request
            times out. If you make the request again with the same
            request ID, the server can check if it received the original
            operation with the same request ID. If it did, it will
            ignore the second request.

            The request ID must be a valid
            `UUID <https://tools.ietf.org/html/rfc4122>`__ with the
            exception that zero UUID is not supported
            (``00000000-0000-0000-0000-000000000000``).
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class CancelEntitlementRequest(proto.Message):
    r"""Request message for
    [CloudChannelService.CancelEntitlement][google.cloud.channel.v1.CloudChannelService.CancelEntitlement].

    Attributes:
        name (str):
            Required. The resource name of the entitlement to cancel.
            Name uses the format:
            accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id}
        request_id (str):
            Optional. You can specify an optional unique request ID, and
            if you need to retry your request, the server will know to
            ignore the request if it's complete.

            For example, you make an initial request and the request
            times out. If you make the request again with the same
            request ID, the server can check if it received the original
            operation with the same request ID. If it did, it will
            ignore the second request.

            The request ID must be a valid
            `UUID <https://tools.ietf.org/html/rfc4122>`__ with the
            exception that zero UUID is not supported
            (``00000000-0000-0000-0000-000000000000``).
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SuspendEntitlementRequest(proto.Message):
    r"""Request message for
    [CloudChannelService.SuspendEntitlement][google.cloud.channel.v1.CloudChannelService.SuspendEntitlement].

    Attributes:
        name (str):
            Required. The resource name of the entitlement to suspend.
            Name uses the format:
            accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id}
        request_id (str):
            Optional. You can specify an optional unique request ID, and
            if you need to retry your request, the server will know to
            ignore the request if it's complete.

            For example, you make an initial request and the request
            times out. If you make the request again with the same
            request ID, the server can check if it received the original
            operation with the same request ID. If it did, it will
            ignore the second request.

            The request ID must be a valid
            `UUID <https://tools.ietf.org/html/rfc4122>`__ with the
            exception that zero UUID is not supported
            (``00000000-0000-0000-0000-000000000000``).
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ActivateEntitlementRequest(proto.Message):
    r"""Request message for
    [CloudChannelService.ActivateEntitlement][google.cloud.channel.v1.CloudChannelService.ActivateEntitlement].

    Attributes:
        name (str):
            Required. The resource name of the entitlement to activate.
            Name uses the format:
            accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id}
        request_id (str):
            Optional. You can specify an optional unique request ID, and
            if you need to retry your request, the server will know to
            ignore the request if it's complete.

            For example, you make an initial request and the request
            times out. If you make the request again with the same
            request ID, the server can check if it received the original
            operation with the same request ID. If it did, it will
            ignore the second request.

            The request ID must be a valid
            `UUID <https://tools.ietf.org/html/rfc4122>`__ with the
            exception that zero UUID is not supported
            (``00000000-0000-0000-0000-000000000000``).
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class LookupOfferRequest(proto.Message):
    r"""Request message for LookupOffer.

    Attributes:
        entitlement (str):
            Required. The resource name of the entitlement to retrieve
            the Offer. Entitlement uses the format:
            accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id}
    """

    entitlement: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListProductsRequest(proto.Message):
    r"""Request message for ListProducts.

    Attributes:
        account (str):
            Required. The resource name of the reseller account. Format:
            accounts/{account_id}.
        page_size (int):
            Optional. Requested page size. Server might
            return fewer results than requested. If
            unspecified, returns at most 100 Products. The
            maximum value is 1000; the server will coerce
            values above 1000.
        page_token (str):
            Optional. A token for a page of results other
            than the first page.
        language_code (str):
            Optional. The BCP-47 language code. For
            example, "en-US". The response will localize in
            the corresponding language code, if specified.
            The default value is "en-US".
    """

    account: str = proto.Field(
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
    language_code: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListProductsResponse(proto.Message):
    r"""Response message for ListProducts.

    Attributes:
        products (MutableSequence[google.cloud.channel_v1.types.Product]):
            List of Products requested.
        next_page_token (str):
            A token to retrieve the next page of results.
    """

    @property
    def raw_page(self):
        return self

    products: MutableSequence[gcc_products.Product] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcc_products.Product,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListSkusRequest(proto.Message):
    r"""Request message for ListSkus.

    Attributes:
        parent (str):
            Required. The resource name of the Product to list SKUs for.
            Parent uses the format: products/{product_id}. Supports
            products/- to retrieve SKUs for all products.
        account (str):
            Required. Resource name of the reseller. Format:
            accounts/{account_id}.
        page_size (int):
            Optional. Requested page size. Server might
            return fewer results than requested. If
            unspecified, returns at most 100 SKUs. The
            maximum value is 1000; the server will coerce
            values above 1000.
        page_token (str):
            Optional. A token for a page of results other
            than the first page. Optional.
        language_code (str):
            Optional. The BCP-47 language code. For
            example, "en-US". The response will localize in
            the corresponding language code, if specified.
            The default value is "en-US".
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    account: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListSkusResponse(proto.Message):
    r"""Response message for ListSkus.

    Attributes:
        skus (MutableSequence[google.cloud.channel_v1.types.Sku]):
            The list of SKUs requested.
        next_page_token (str):
            A token to retrieve the next page of results.
    """

    @property
    def raw_page(self):
        return self

    skus: MutableSequence[gcc_products.Sku] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcc_products.Sku,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListOffersRequest(proto.Message):
    r"""Request message for ListOffers.

    Attributes:
        parent (str):
            Required. The resource name of the reseller account from
            which to list Offers. Parent uses the format:
            accounts/{account_id}.
        page_size (int):
            Optional. Requested page size. Server might
            return fewer results than requested. If
            unspecified, returns at most 500 Offers. The
            maximum value is 1000; the server will coerce
            values above 1000.
        page_token (str):
            Optional. A token for a page of results other
            than the first page.
        filter (str):
            Optional. The expression to filter results by
            name (name of the Offer), sku.name (name of the
            SKU), or sku.product.name (name of the Product).
            Example 1: sku.product.name=products/p1 AND
            sku.name!=products/p1/skus/s1 Example 2:
            name=accounts/a1/offers/o1
        language_code (str):
            Optional. The BCP-47 language code. For
            example, "en-US". The response will localize in
            the corresponding language code, if specified.
            The default value is "en-US".
        show_future_offers (bool):
            Optional. A boolean flag that determines if a response
            returns future offers 30 days from now. If the
            show_future_offers is true, the response will only contain
            offers that are scheduled to be available 30 days from now.
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
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=5,
    )
    show_future_offers: bool = proto.Field(
        proto.BOOL,
        number=7,
    )


class ListOffersResponse(proto.Message):
    r"""Response message for ListOffers.

    Attributes:
        offers (MutableSequence[google.cloud.channel_v1.types.Offer]):
            The list of Offers requested.

            The pricing information for each Offer only
            includes the base price. Effective prices and
            discounts aren't populated.
        next_page_token (str):
            A token to retrieve the next page of results.
    """

    @property
    def raw_page(self):
        return self

    offers: MutableSequence[gcc_offers.Offer] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcc_offers.Offer,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListPurchasableSkusRequest(proto.Message):
    r"""Request message for ListPurchasableSkus.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        create_entitlement_purchase (google.cloud.channel_v1.types.ListPurchasableSkusRequest.CreateEntitlementPurchase):
            List SKUs for CreateEntitlement purchase.

            This field is a member of `oneof`_ ``purchase_option``.
        change_offer_purchase (google.cloud.channel_v1.types.ListPurchasableSkusRequest.ChangeOfferPurchase):
            List SKUs for ChangeOffer purchase with a new
            SKU.

            This field is a member of `oneof`_ ``purchase_option``.
        customer (str):
            Required. The resource name of the customer to list SKUs
            for. Format: accounts/{account_id}/customers/{customer_id}.
        page_size (int):
            Optional. Requested page size. Server might
            return fewer results than requested. If
            unspecified, returns at most 100 SKUs. The
            maximum value is 1000; the server will coerce
            values above 1000.
        page_token (str):
            Optional. A token for a page of results other
            than the first page.
        language_code (str):
            Optional. The BCP-47 language code. For
            example, "en-US". The response will localize in
            the corresponding language code, if specified.
            The default value is "en-US".
    """

    class CreateEntitlementPurchase(proto.Message):
        r"""List SKUs for a new entitlement. Make the purchase using
        [CloudChannelService.CreateEntitlement][google.cloud.channel.v1.CloudChannelService.CreateEntitlement].

        Attributes:
            product (str):
                Required. List SKUs belonging to this Product. Format:
                products/{product_id}. Supports products/- to retrieve SKUs
                for all products.
        """

        product: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class ChangeOfferPurchase(proto.Message):
        r"""List SKUs for upgrading or downgrading an entitlement. Make the
        purchase using
        [CloudChannelService.ChangeOffer][google.cloud.channel.v1.CloudChannelService.ChangeOffer].

        Attributes:
            entitlement (str):
                Required. Resource name of the entitlement. Format:
                accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id}
            change_type (google.cloud.channel_v1.types.ListPurchasableSkusRequest.ChangeOfferPurchase.ChangeType):
                Required. Change Type for the entitlement.
        """

        class ChangeType(proto.Enum):
            r"""Change Type enum.

            Values:
                CHANGE_TYPE_UNSPECIFIED (0):
                    Not used.
                UPGRADE (1):
                    SKU is an upgrade on the current entitlement.
                DOWNGRADE (2):
                    SKU is a downgrade on the current
                    entitlement.
            """

            CHANGE_TYPE_UNSPECIFIED = 0
            UPGRADE = 1
            DOWNGRADE = 2

        entitlement: str = proto.Field(
            proto.STRING,
            number=1,
        )
        change_type: "ListPurchasableSkusRequest.ChangeOfferPurchase.ChangeType" = (
            proto.Field(
                proto.ENUM,
                number=2,
                enum="ListPurchasableSkusRequest.ChangeOfferPurchase.ChangeType",
            )
        )

    create_entitlement_purchase: CreateEntitlementPurchase = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="purchase_option",
        message=CreateEntitlementPurchase,
    )
    change_offer_purchase: ChangeOfferPurchase = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="purchase_option",
        message=ChangeOfferPurchase,
    )
    customer: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=4,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=5,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=6,
    )


class ListPurchasableSkusResponse(proto.Message):
    r"""Response message for ListPurchasableSkus.

    Attributes:
        purchasable_skus (MutableSequence[google.cloud.channel_v1.types.PurchasableSku]):
            The list of SKUs requested.
        next_page_token (str):
            A token to retrieve the next page of results.
    """

    @property
    def raw_page(self):
        return self

    purchasable_skus: MutableSequence["PurchasableSku"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="PurchasableSku",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class PurchasableSku(proto.Message):
    r"""SKU that you can purchase. This is used in ListPurchasableSku
    API response.

    Attributes:
        sku (google.cloud.channel_v1.types.Sku):
            SKU
    """

    sku: gcc_products.Sku = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcc_products.Sku,
    )


class ListPurchasableOffersRequest(proto.Message):
    r"""Request message for ListPurchasableOffers.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        create_entitlement_purchase (google.cloud.channel_v1.types.ListPurchasableOffersRequest.CreateEntitlementPurchase):
            List Offers for CreateEntitlement purchase.

            This field is a member of `oneof`_ ``purchase_option``.
        change_offer_purchase (google.cloud.channel_v1.types.ListPurchasableOffersRequest.ChangeOfferPurchase):
            List Offers for ChangeOffer purchase.

            This field is a member of `oneof`_ ``purchase_option``.
        customer (str):
            Required. The resource name of the customer to list Offers
            for. Format: accounts/{account_id}/customers/{customer_id}.
        page_size (int):
            Optional. Requested page size. Server might
            return fewer results than requested. If
            unspecified, returns at most 100 Offers. The
            maximum value is 1000; the server will coerce
            values above 1000.
        page_token (str):
            Optional. A token for a page of results other
            than the first page.
        language_code (str):
            Optional. The BCP-47 language code. For
            example, "en-US". The response will localize in
            the corresponding language code, if specified.
            The default value is "en-US".
    """

    class CreateEntitlementPurchase(proto.Message):
        r"""List Offers for CreateEntitlement purchase.

        Attributes:
            sku (str):
                Required. SKU that the result should be restricted to.
                Format: products/{product_id}/skus/{sku_id}.
            billing_account (str):
                Optional. Billing account that the result should be
                restricted to. Format:
                accounts/{account_id}/billingAccounts/{billing_account_id}.
        """

        sku: str = proto.Field(
            proto.STRING,
            number=1,
        )
        billing_account: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class ChangeOfferPurchase(proto.Message):
        r"""List Offers for ChangeOffer purchase.

        Attributes:
            entitlement (str):
                Required. Resource name of the entitlement. Format:
                accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id}
            new_sku (str):
                Optional. Resource name of the new target SKU. Provide this
                SKU when upgrading or downgrading an entitlement. Format:
                products/{product_id}/skus/{sku_id}
            billing_account (str):
                Optional. Resource name of the new target Billing Account.
                Provide this Billing Account when setting up billing for a
                trial subscription. Format:
                accounts/{account_id}/billingAccounts/{billing_account_id}.

                This field is only relevant for multi-currency accounts. It
                should be left empty for single currency accounts.
        """

        entitlement: str = proto.Field(
            proto.STRING,
            number=1,
        )
        new_sku: str = proto.Field(
            proto.STRING,
            number=2,
        )
        billing_account: str = proto.Field(
            proto.STRING,
            number=3,
        )

    create_entitlement_purchase: CreateEntitlementPurchase = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="purchase_option",
        message=CreateEntitlementPurchase,
    )
    change_offer_purchase: ChangeOfferPurchase = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="purchase_option",
        message=ChangeOfferPurchase,
    )
    customer: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=4,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=5,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=6,
    )


class ListPurchasableOffersResponse(proto.Message):
    r"""Response message for ListPurchasableOffers.

    Attributes:
        purchasable_offers (MutableSequence[google.cloud.channel_v1.types.PurchasableOffer]):
            The list of Offers requested.
        next_page_token (str):
            A token to retrieve the next page of results.
    """

    @property
    def raw_page(self):
        return self

    purchasable_offers: MutableSequence["PurchasableOffer"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="PurchasableOffer",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class PurchasableOffer(proto.Message):
    r"""Offer that you can purchase for a customer. This is used in
    the ListPurchasableOffer API response.

    Attributes:
        offer (google.cloud.channel_v1.types.Offer):
            Offer.
        price_reference_id (str):
            Optional. Price reference ID for the offer.
            Only for offers that require additional price
            information. Used to guarantee that the pricing
            is consistent between quoting the offer and
            placing the order.
    """

    offer: gcc_offers.Offer = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcc_offers.Offer,
    )
    price_reference_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class QueryEligibleBillingAccountsRequest(proto.Message):
    r"""Request message for QueryEligibleBillingAccounts.

    Attributes:
        customer (str):
            Required. The resource name of the customer to list eligible
            billing accounts for. Format:
            accounts/{account_id}/customers/{customer_id}.
        skus (MutableSequence[str]):
            Required. List of SKUs to list eligible billing accounts
            for. At least one SKU is required. Format:
            products/{product_id}/skus/{sku_id}.
    """

    customer: str = proto.Field(
        proto.STRING,
        number=1,
    )
    skus: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class QueryEligibleBillingAccountsResponse(proto.Message):
    r"""Response message for QueryEligibleBillingAccounts.

    Attributes:
        sku_purchase_groups (MutableSequence[google.cloud.channel_v1.types.SkuPurchaseGroup]):
            List of SKU purchase groups where each group represents a
            set of SKUs that must be purchased using the same billing
            account. Each SKU from
            [QueryEligibleBillingAccountsRequest.skus] will appear in
            exactly one SKU group.
    """

    sku_purchase_groups: MutableSequence["SkuPurchaseGroup"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="SkuPurchaseGroup",
    )


class SkuPurchaseGroup(proto.Message):
    r"""Represents a set of SKUs that must be purchased using the
    same billing account.

    Attributes:
        skus (MutableSequence[str]):
            Resource names of the SKUs included in this group. Format:
            products/{product_id}/skus/{sku_id}.
        billing_account_purchase_infos (MutableSequence[google.cloud.channel_v1.types.BillingAccountPurchaseInfo]):
            List of billing accounts that are eligible to
            purhcase these SKUs.
    """

    skus: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    billing_account_purchase_infos: MutableSequence["BillingAccountPurchaseInfo"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="BillingAccountPurchaseInfo",
        )
    )


class BillingAccountPurchaseInfo(proto.Message):
    r"""Represents a billing account that can be used to make a
    purchase.

    Attributes:
        billing_account (google.cloud.channel_v1.types.BillingAccount):
            The billing account resource.
    """

    billing_account: billing_accounts.BillingAccount = proto.Field(
        proto.MESSAGE,
        number=1,
        message=billing_accounts.BillingAccount,
    )


class RegisterSubscriberRequest(proto.Message):
    r"""Request Message for RegisterSubscriber.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        account (str):
            Optional. Resource name of the account.
            Required if integrator is not provided.
            Otherwise, leave this field empty/unset.
        service_account (str):
            Required. Service account that provides
            subscriber access to the registered topic.
        integrator (str):
            Optional. Resource name of the integrator.
            Required if account is not provided. Otherwise,
            leave this field empty/unset.

            This field is a member of `oneof`_ ``_integrator``.
    """

    account: str = proto.Field(
        proto.STRING,
        number=1,
    )
    service_account: str = proto.Field(
        proto.STRING,
        number=2,
    )
    integrator: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )


class RegisterSubscriberResponse(proto.Message):
    r"""Response Message for RegisterSubscriber.

    Attributes:
        topic (str):
            Name of the topic the subscriber will listen
            to.
    """

    topic: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UnregisterSubscriberRequest(proto.Message):
    r"""Request Message for UnregisterSubscriber.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        account (str):
            Optional. Resource name of the account.
            Required if integrator is not provided.
            Otherwise, leave this field empty/unset.
        service_account (str):
            Required. Service account to unregister from
            subscriber access to the topic.
        integrator (str):
            Optional. Resource name of the integrator.
            Required if account is not provided. Otherwise,
            leave this field empty/unset.

            This field is a member of `oneof`_ ``_integrator``.
    """

    account: str = proto.Field(
        proto.STRING,
        number=1,
    )
    service_account: str = proto.Field(
        proto.STRING,
        number=2,
    )
    integrator: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )


class UnregisterSubscriberResponse(proto.Message):
    r"""Response Message for UnregisterSubscriber.

    Attributes:
        topic (str):
            Name of the topic the service account
            subscriber access was removed from.
    """

    topic: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListSubscribersRequest(proto.Message):
    r"""Request Message for ListSubscribers.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        account (str):
            Optional. Resource name of the account.
            Required if integrator is not provided.
            Otherwise, leave this field empty/unset.
        page_size (int):
            Optional. The maximum number of service
            accounts to return. The service may return fewer
            than this value. If unspecified, returns at most
            100 service accounts. The maximum value is 1000;
            the server will coerce values above 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListSubscribers`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListSubscribers`` must match the call that provided the
            page token.
        integrator (str):
            Optional. Resource name of the integrator.
            Required if account is not provided. Otherwise,
            leave this field empty/unset.

            This field is a member of `oneof`_ ``_integrator``.
    """

    account: str = proto.Field(
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
    integrator: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )


class ListSubscribersResponse(proto.Message):
    r"""Response Message for ListSubscribers.

    Attributes:
        topic (str):
            Name of the topic registered with the
            reseller.
        service_accounts (MutableSequence[str]):
            List of service accounts which have
            subscriber access to the topic.
        next_page_token (str):
            A token that can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    topic: str = proto.Field(
        proto.STRING,
        number=1,
    )
    service_accounts: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListEntitlementChangesRequest(proto.Message):
    r"""Request message for
    [CloudChannelService.ListEntitlementChanges][google.cloud.channel.v1.CloudChannelService.ListEntitlementChanges]

    Attributes:
        parent (str):
            Required. The resource name of the entitlement for which to
            list entitlement changes. The ``-`` wildcard may be used to
            match entitlements across a customer. Formats:

            - accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id}
            - accounts/{account_id}/customers/{customer_id}/entitlements/-
        page_size (int):
            Optional. The maximum number of entitlement
            changes to return. The service may return fewer
            than this value. If unspecified, returns at most
            10 entitlement changes. The maximum value is 50;
            the server will coerce values above 50.
        page_token (str):
            Optional. A page token, received from a previous
            [CloudChannelService.ListEntitlementChanges][google.cloud.channel.v1.CloudChannelService.ListEntitlementChanges]
            call. Provide this to retrieve the subsequent page.

            When paginating, all other parameters provided to
            [CloudChannelService.ListEntitlementChanges][google.cloud.channel.v1.CloudChannelService.ListEntitlementChanges]
            must match the call that provided the page token.
        filter (str):
            Optional. Filters applied to the list
            results.
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
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListEntitlementChangesResponse(proto.Message):
    r"""Response message for
    [CloudChannelService.ListEntitlementChanges][google.cloud.channel.v1.CloudChannelService.ListEntitlementChanges]

    Attributes:
        entitlement_changes (MutableSequence[google.cloud.channel_v1.types.EntitlementChange]):
            The list of entitlement changes.
        next_page_token (str):
            A token to list the next page of results.
    """

    @property
    def raw_page(self):
        return self

    entitlement_changes: MutableSequence[gcc_entitlement_changes.EntitlementChange] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=gcc_entitlement_changes.EntitlementChange,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
