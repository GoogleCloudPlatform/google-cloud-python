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

from google.cloud.channel_v1.types import entitlements

__protobuf__ = proto.module(
    package="google.cloud.channel.v1",
    manifest={
        "EntitlementChange",
    },
)


class EntitlementChange(proto.Message):
    r"""Change event entry for Entitlement order history

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        suspension_reason (google.cloud.channel_v1.types.Entitlement.SuspensionReason):
            Suspension reason for the Entitlement.

            This field is a member of `oneof`_ ``change_reason``.
        cancellation_reason (google.cloud.channel_v1.types.EntitlementChange.CancellationReason):
            Cancellation reason for the Entitlement.

            This field is a member of `oneof`_ ``change_reason``.
        activation_reason (google.cloud.channel_v1.types.EntitlementChange.ActivationReason):
            The Entitlement's activation reason

            This field is a member of `oneof`_ ``change_reason``.
        other_change_reason (str):
            e.g. purchase_number change reason, entered by CRS.

            This field is a member of `oneof`_ ``change_reason``.
        entitlement (str):
            Required. Resource name of an entitlement in the form:
            accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id}
        offer (str):
            Required. Resource name of the Offer at the time of change.
            Takes the form: accounts/{account_id}/offers/{offer_id}.
        provisioned_service (google.cloud.channel_v1.types.ProvisionedService):
            Service provisioned for an Entitlement.
        change_type (google.cloud.channel_v1.types.EntitlementChange.ChangeType):
            The change action type.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            The submitted time of the change.
        operator_type (google.cloud.channel_v1.types.EntitlementChange.OperatorType):
            Operator type responsible for the change.
        parameters (MutableSequence[google.cloud.channel_v1.types.Parameter]):
            Extended parameters, such as: purchase_order_number,
            gcp_details; internal_correlation_id,
            long_running_operation_id, order_id; etc.
        operator (str):
            Human-readable identifier that shows what operator made a
            change. When the operator_type is RESELLER, this is the
            user's email address. For all other operator types, this is
            empty.
    """

    class ChangeType(proto.Enum):
        r"""Specifies the type of change action

        Values:
            CHANGE_TYPE_UNSPECIFIED (0):
                Not used.
            CREATED (1):
                New Entitlement was created.
            PRICE_PLAN_SWITCHED (3):
                Price plan associated with an Entitlement was
                changed.
            COMMITMENT_CHANGED (4):
                Number of seats committed for a commitment
                Entitlement was changed.
            RENEWED (5):
                An annual Entitlement was renewed.
            SUSPENDED (6):
                Entitlement was suspended.
            ACTIVATED (7):
                Entitlement was activated.
            CANCELLED (8):
                Entitlement was cancelled.
            SKU_CHANGED (9):
                Entitlement was upgraded or downgraded for
                ex. from Google Workspace Business Standard to
                Google Workspace Business Plus.
            RENEWAL_SETTING_CHANGED (10):
                The settings for renewal of an Entitlement
                have changed.
            PAID_SUBSCRIPTION_STARTED (11):
                Use for Google Workspace subscription.
                Either a trial was converted to a paid
                subscription or a new subscription with no trial
                is created.
            LICENSE_CAP_CHANGED (12):
                License cap was changed for the entitlement.
            SUSPENSION_DETAILS_CHANGED (13):
                The suspension details have changed (but it
                is still suspended).
            TRIAL_END_DATE_EXTENDED (14):
                The trial end date was extended.
            TRIAL_STARTED (15):
                Entitlement started trial.
        """

        CHANGE_TYPE_UNSPECIFIED = 0
        CREATED = 1
        PRICE_PLAN_SWITCHED = 3
        COMMITMENT_CHANGED = 4
        RENEWED = 5
        SUSPENDED = 6
        ACTIVATED = 7
        CANCELLED = 8
        SKU_CHANGED = 9
        RENEWAL_SETTING_CHANGED = 10
        PAID_SUBSCRIPTION_STARTED = 11
        LICENSE_CAP_CHANGED = 12
        SUSPENSION_DETAILS_CHANGED = 13
        TRIAL_END_DATE_EXTENDED = 14
        TRIAL_STARTED = 15

    class OperatorType(proto.Enum):
        r"""Specifies the type of operator responsible for the change

        Values:
            OPERATOR_TYPE_UNSPECIFIED (0):
                Not used.
            CUSTOMER_SERVICE_REPRESENTATIVE (1):
                Customer service representative.
            SYSTEM (2):
                System auto job.
            CUSTOMER (3):
                Customer user.
            RESELLER (4):
                Reseller user.
        """

        OPERATOR_TYPE_UNSPECIFIED = 0
        CUSTOMER_SERVICE_REPRESENTATIVE = 1
        SYSTEM = 2
        CUSTOMER = 3
        RESELLER = 4

    class CancellationReason(proto.Enum):
        r"""Cancellation reason for the entitlement

        Values:
            CANCELLATION_REASON_UNSPECIFIED (0):
                Not used.
            SERVICE_TERMINATED (1):
                Reseller triggered a cancellation of the
                service.
            RELATIONSHIP_ENDED (2):
                Relationship between the reseller and
                customer has ended due to a transfer.
            PARTIAL_TRANSFER (3):
                Entitlement transferred away from reseller
                while still keeping other entitlement(s) with
                the reseller.
        """

        CANCELLATION_REASON_UNSPECIFIED = 0
        SERVICE_TERMINATED = 1
        RELATIONSHIP_ENDED = 2
        PARTIAL_TRANSFER = 3

    class ActivationReason(proto.Enum):
        r"""The Entitlement's activation reason

        Values:
            ACTIVATION_REASON_UNSPECIFIED (0):
                Not used.
            RESELLER_REVOKED_SUSPENSION (1):
                Reseller reactivated a suspended Entitlement.
            CUSTOMER_ACCEPTED_PENDING_TOS (2):
                Customer accepted pending terms of service.
            RENEWAL_SETTINGS_CHANGED (3):
                Reseller updated the renewal settings on an
                entitlement that was suspended due to
                cancellation, and this update reactivated the
                entitlement.
            OTHER_ACTIVATION_REASON (100):
                Other reasons (Activated temporarily for
                cancellation, added a payment plan to a trial
                entitlement, etc.)
        """

        ACTIVATION_REASON_UNSPECIFIED = 0
        RESELLER_REVOKED_SUSPENSION = 1
        CUSTOMER_ACCEPTED_PENDING_TOS = 2
        RENEWAL_SETTINGS_CHANGED = 3
        OTHER_ACTIVATION_REASON = 100

    suspension_reason: entitlements.Entitlement.SuspensionReason = proto.Field(
        proto.ENUM,
        number=9,
        oneof="change_reason",
        enum=entitlements.Entitlement.SuspensionReason,
    )
    cancellation_reason: CancellationReason = proto.Field(
        proto.ENUM,
        number=10,
        oneof="change_reason",
        enum=CancellationReason,
    )
    activation_reason: ActivationReason = proto.Field(
        proto.ENUM,
        number=11,
        oneof="change_reason",
        enum=ActivationReason,
    )
    other_change_reason: str = proto.Field(
        proto.STRING,
        number=100,
        oneof="change_reason",
    )
    entitlement: str = proto.Field(
        proto.STRING,
        number=1,
    )
    offer: str = proto.Field(
        proto.STRING,
        number=2,
    )
    provisioned_service: entitlements.ProvisionedService = proto.Field(
        proto.MESSAGE,
        number=3,
        message=entitlements.ProvisionedService,
    )
    change_type: ChangeType = proto.Field(
        proto.ENUM,
        number=4,
        enum=ChangeType,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    operator_type: OperatorType = proto.Field(
        proto.ENUM,
        number=6,
        enum=OperatorType,
    )
    parameters: MutableSequence[entitlements.Parameter] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message=entitlements.Parameter,
    )
    operator: str = proto.Field(
        proto.STRING,
        number=12,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
