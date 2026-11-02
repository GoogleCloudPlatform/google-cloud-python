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

from google.cloud.channel_v1.types import common, offers, products

__protobuf__ = proto.module(
    package="google.cloud.channel.v1",
    manifest={
        "Entitlement",
        "Parameter",
        "AssociationInfo",
        "ProvisionedService",
        "CommitmentSettings",
        "RenewalSettings",
        "TrialSettings",
        "TransferableSku",
        "TransferEligibility",
    },
)


class Entitlement(proto.Message):
    r"""An entitlement is a representation of a customer's ability to
    use a service.

    Attributes:
        name (str):
            Output only. Resource name of an entitlement in the form:
            accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id}.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which the
            entitlement is created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which the
            entitlement is updated.
        offer (str):
            Required. The offer resource name for which the entitlement
            is to be created. Takes the form:
            accounts/{account_id}/offers/{offer_id}.
        commitment_settings (google.cloud.channel_v1.types.CommitmentSettings):
            Commitment settings for a commitment-based
            Offer. Required for commitment based offers.
        provisioning_state (google.cloud.channel_v1.types.Entitlement.ProvisioningState):
            Output only. Current provisioning state of
            the entitlement.
        provisioned_service (google.cloud.channel_v1.types.ProvisionedService):
            Output only. Service provisioning details for
            the entitlement.
        suspension_reasons (MutableSequence[google.cloud.channel_v1.types.Entitlement.SuspensionReason]):
            Output only. Enumerable of all current
            suspension reasons for an entitlement.
        purchase_order_id (str):
            Optional. This purchase order (PO)
            information is for resellers to use for their
            company tracking usage. If a purchaseOrderId
            value is given, it appears in the API responses
            and shows up in the invoice. The property
            accepts up to 80 plain text characters. This is
            only supported for Google Workspace
            entitlements.
        trial_settings (google.cloud.channel_v1.types.TrialSettings):
            Output only. Settings for trial offers.
        association_info (google.cloud.channel_v1.types.AssociationInfo):
            Association information to other
            entitlements.
        parameters (MutableSequence[google.cloud.channel_v1.types.Parameter]):
            Extended entitlement parameters. When creating an
            entitlement, valid parameter names and values are defined in
            the
            [Offer.parameter_definitions][google.cloud.channel.v1.Offer.parameter_definitions].

            For Google Workspace, the following Parameters may be
            accepted as input:

            - max_units: The maximum assignable units for a flexible
              offer

            OR

            - num_units: The total commitment for commitment-based
              offers

            The response may additionally include the following
            output-only Parameters:

            - assigned_units: The number of licenses assigned to users.

            For Google Cloud billing subaccounts, the following
            Parameter may be accepted as input:

            - display_name: The display name of the billing subaccount.
        billing_account (str):
            Optional. The billing account resource name
            that is used to pay for this entitlement.
        price_reference_id (str):
            Optional. Price reference ID for the offer.
            Only for offers that require additional price
            information. Used to guarantee that the pricing
            is consistent between quoting the offer and
            placing the order.
    """

    class ProvisioningState(proto.Enum):
        r"""Indicates the current provisioning state of the entitlement.

        Values:
            PROVISIONING_STATE_UNSPECIFIED (0):
                Not used.
            ACTIVE (1):
                The entitlement is currently active.
            SUSPENDED (5):
                The entitlement is currently suspended.
        """

        PROVISIONING_STATE_UNSPECIFIED = 0
        ACTIVE = 1
        SUSPENDED = 5

    class SuspensionReason(proto.Enum):
        r"""Suspension reason for an entitlement if
        [provisioning_state][google.cloud.channel.v1.Entitlement.provisioning_state]
        = SUSPENDED.

        Values:
            SUSPENSION_REASON_UNSPECIFIED (0):
                Not used.
            RESELLER_INITIATED (1):
                Entitlement was manually suspended by the
                Reseller.
            TRIAL_ENDED (2):
                Trial ended.
            RENEWAL_WITH_TYPE_CANCEL (3):
                Entitlement renewal was canceled.
            PENDING_TOS_ACCEPTANCE (4):
                Entitlement was automatically suspended on
                creation for pending ToS acceptance on customer.
            OTHER (100):
                Other reasons (internal reasons, abuse,
                etc.).
        """

        SUSPENSION_REASON_UNSPECIFIED = 0
        RESELLER_INITIATED = 1
        TRIAL_ENDED = 2
        RENEWAL_WITH_TYPE_CANCEL = 3
        PENDING_TOS_ACCEPTANCE = 4
        OTHER = 100

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    offer: str = proto.Field(
        proto.STRING,
        number=8,
    )
    commitment_settings: "CommitmentSettings" = proto.Field(
        proto.MESSAGE,
        number=12,
        message="CommitmentSettings",
    )
    provisioning_state: ProvisioningState = proto.Field(
        proto.ENUM,
        number=13,
        enum=ProvisioningState,
    )
    provisioned_service: "ProvisionedService" = proto.Field(
        proto.MESSAGE,
        number=16,
        message="ProvisionedService",
    )
    suspension_reasons: MutableSequence[SuspensionReason] = proto.RepeatedField(
        proto.ENUM,
        number=18,
        enum=SuspensionReason,
    )
    purchase_order_id: str = proto.Field(
        proto.STRING,
        number=19,
    )
    trial_settings: "TrialSettings" = proto.Field(
        proto.MESSAGE,
        number=21,
        message="TrialSettings",
    )
    association_info: "AssociationInfo" = proto.Field(
        proto.MESSAGE,
        number=23,
        message="AssociationInfo",
    )
    parameters: MutableSequence["Parameter"] = proto.RepeatedField(
        proto.MESSAGE,
        number=26,
        message="Parameter",
    )
    billing_account: str = proto.Field(
        proto.STRING,
        number=28,
    )
    price_reference_id: str = proto.Field(
        proto.STRING,
        number=29,
    )


class Parameter(proto.Message):
    r"""Definition for extended entitlement parameters.

    Attributes:
        name (str):
            Name of the parameter.
        value (google.cloud.channel_v1.types.Value):
            Value of the parameter.
        editable (bool):
            Output only. Specifies whether this parameter is allowed to
            be changed. For example, for a Google Workspace Business
            Starter entitlement in commitment plan, num_units is
            editable when entitlement is active.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    value: common.Value = proto.Field(
        proto.MESSAGE,
        number=2,
        message=common.Value,
    )
    editable: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class AssociationInfo(proto.Message):
    r"""Association links that an entitlement has to other
    entitlements.

    Attributes:
        base_entitlement (str):
            The name of the base entitlement, for which
            this entitlement is an add-on.
    """

    base_entitlement: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ProvisionedService(proto.Message):
    r"""Service provisioned for an entitlement.

    Attributes:
        provisioning_id (str):
            Output only. Provisioning ID of the
            entitlement. For Google Workspace, this is the
            underlying Subscription ID. For Google Cloud,
            this is the Billing Account ID of the billing
            subaccount.
        product_id (str):
            Output only. The product pertaining to the
            provisioning resource as specified in the Offer.
        sku_id (str):
            Output only. The SKU pertaining to the
            provisioning resource as specified in the Offer.
    """

    provisioning_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    product_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    sku_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class CommitmentSettings(proto.Message):
    r"""Commitment settings for commitment-based offers.

    Attributes:
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Commitment start timestamp.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Commitment end timestamp.
        renewal_settings (google.cloud.channel_v1.types.RenewalSettings):
            Optional. Renewal settings applicable for a
            commitment-based Offer.
    """

    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    renewal_settings: "RenewalSettings" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="RenewalSettings",
    )


class RenewalSettings(proto.Message):
    r"""Renewal settings for renewable Offers.

    Attributes:
        enable_renewal (bool):
            If false, the plan will be completed at the
            end date.
        resize_unit_count (bool):
            If true and enable_renewal = true, the unit (for example
            seats or licenses) will be set to the number of active units
            at renewal time.
        payment_plan (google.cloud.channel_v1.types.PaymentPlan):
            Describes how a reseller will be billed.
        payment_cycle (google.cloud.channel_v1.types.Period):
            Describes how frequently the reseller will be
            billed, such as once per month.
    """

    enable_renewal: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    resize_unit_count: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    payment_plan: offers.PaymentPlan = proto.Field(
        proto.ENUM,
        number=5,
        enum=offers.PaymentPlan,
    )
    payment_cycle: offers.Period = proto.Field(
        proto.MESSAGE,
        number=6,
        message=offers.Period,
    )


class TrialSettings(proto.Message):
    r"""Settings for trial offers.

    Attributes:
        trial (bool):
            Determines if the entitlement is in a trial or not:

            - ``true`` - The entitlement is in trial.
            - ``false`` - The entitlement is not in trial.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Date when the trial ends. The value is in milliseconds using
            the UNIX Epoch format. See an example `Epoch
            converter <https://www.epochconverter.com>`__.
    """

    trial: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )


class TransferableSku(proto.Message):
    r"""TransferableSku represents information a reseller needs to
    view existing provisioned services for a customer that they do
    not own. Read-only.

    Attributes:
        transfer_eligibility (google.cloud.channel_v1.types.TransferEligibility):
            Describes the transfer eligibility of a SKU.
        sku (google.cloud.channel_v1.types.Sku):
            The SKU pertaining to the provisioning
            resource as specified in the Offer.
        legacy_sku (google.cloud.channel_v1.types.Sku):
            Optional. The customer to transfer has an
            entitlement with the populated legacy SKU.
    """

    transfer_eligibility: "TransferEligibility" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="TransferEligibility",
    )
    sku: products.Sku = proto.Field(
        proto.MESSAGE,
        number=11,
        message=products.Sku,
    )
    legacy_sku: products.Sku = proto.Field(
        proto.MESSAGE,
        number=12,
        message=products.Sku,
    )


class TransferEligibility(proto.Message):
    r"""Specifies transfer eligibility of a SKU.

    Attributes:
        is_eligible (bool):
            Whether reseller is eligible to transfer the
            SKU.
        description (str):
            Localized description if reseller is not
            eligible to transfer the SKU.
        ineligibility_reason (google.cloud.channel_v1.types.TransferEligibility.Reason):
            Specified the reason for ineligibility.
    """

    class Reason(proto.Enum):
        r"""Reason of ineligibility.

        Values:
            REASON_UNSPECIFIED (0):
                Not used.
            PENDING_TOS_ACCEPTANCE (1):
                Reseller needs to accept TOS before
                transferring the SKU.
            SKU_NOT_ELIGIBLE (2):
                Reseller not eligible to sell the SKU.
            SKU_SUSPENDED (3):
                SKU subscription is suspended
            CHANNEL_PARTNER_NOT_AUTHORIZED_FOR_SKU (4):
                The reseller is not authorized to transact on
                this Product. See
                https://support.google.com/channelservices/answer/9759265
        """

        REASON_UNSPECIFIED = 0
        PENDING_TOS_ACCEPTANCE = 1
        SKU_NOT_ELIGIBLE = 2
        SKU_SUSPENDED = 3
        CHANNEL_PARTNER_NOT_AUTHORIZED_FOR_SKU = 4

    is_eligible: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    ineligibility_reason: Reason = proto.Field(
        proto.ENUM,
        number=3,
        enum=Reason,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
