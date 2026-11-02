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
    package="google.cloud.channel.v1",
    manifest={
        "CustomerEvent",
        "EntitlementEvent",
        "SubscriberEvent",
    },
)


class CustomerEvent(proto.Message):
    r"""Represents Pub/Sub message content describing customer
    update.

    Attributes:
        customer (str):
            Resource name of the customer. Format:
            accounts/{account_id}/customers/{customer_id}
        event_type (google.cloud.channel_v1.types.CustomerEvent.Type):
            Type of event which happened for the
            customer.
    """

    class Type(proto.Enum):
        r"""Type of customer event.

        Values:
            TYPE_UNSPECIFIED (0):
                Not used.
            PRIMARY_DOMAIN_CHANGED (1):
                Primary domain for customer was changed.
            PRIMARY_DOMAIN_VERIFIED (2):
                Primary domain of the customer has been
                verified.
        """

        TYPE_UNSPECIFIED = 0
        PRIMARY_DOMAIN_CHANGED = 1
        PRIMARY_DOMAIN_VERIFIED = 2

    customer: str = proto.Field(
        proto.STRING,
        number=1,
    )
    event_type: Type = proto.Field(
        proto.ENUM,
        number=2,
        enum=Type,
    )


class EntitlementEvent(proto.Message):
    r"""Represents Pub/Sub message content describing entitlement
    update.

    Attributes:
        entitlement (str):
            Resource name of an entitlement of the form:
            accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id}
        event_type (google.cloud.channel_v1.types.EntitlementEvent.Type):
            Type of event which happened for the
            entitlement.
    """

    class Type(proto.Enum):
        r"""Type of entitlement event.

        Values:
            TYPE_UNSPECIFIED (0):
                Not used.
            CREATED (1):
                A new entitlement was created.
            PRICE_PLAN_SWITCHED (3):
                The offer type associated with an entitlement
                was changed. This is not triggered if an
                entitlement converts from a commit offer to a
                flexible offer as part of a renewal.
            COMMITMENT_CHANGED (4):
                Annual commitment for a commit plan was
                changed.
            RENEWED (5):
                An annual entitlement was renewed.
            SUSPENDED (6):
                Entitlement was suspended.
            ACTIVATED (7):
                Entitlement was unsuspended.
            CANCELLED (8):
                Entitlement was cancelled.
            SKU_CHANGED (9):
                Entitlement was upgraded or downgraded (e.g.
                from Google Workspace Business Standard to
                Google Workspace Business Plus).
            RENEWAL_SETTING_CHANGED (10):
                The renewal settings of an entitlement has
                changed.
            PAID_SERVICE_STARTED (11):
                Paid service has started on trial
                entitlement.
            LICENSE_ASSIGNMENT_CHANGED (12):
                License was assigned to or revoked from a
                user.
            LICENSE_CAP_CHANGED (13):
                License cap was changed for the entitlement.
        """

        TYPE_UNSPECIFIED = 0
        CREATED = 1
        PRICE_PLAN_SWITCHED = 3
        COMMITMENT_CHANGED = 4
        RENEWED = 5
        SUSPENDED = 6
        ACTIVATED = 7
        CANCELLED = 8
        SKU_CHANGED = 9
        RENEWAL_SETTING_CHANGED = 10
        PAID_SERVICE_STARTED = 11
        LICENSE_ASSIGNMENT_CHANGED = 12
        LICENSE_CAP_CHANGED = 13

    entitlement: str = proto.Field(
        proto.STRING,
        number=1,
    )
    event_type: Type = proto.Field(
        proto.ENUM,
        number=2,
        enum=Type,
    )


class SubscriberEvent(proto.Message):
    r"""Represents information which resellers will get as part of
    notification from Pub/Sub.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        customer_event (google.cloud.channel_v1.types.CustomerEvent):
            Customer event sent as part of Pub/Sub event
            to partners.

            This field is a member of `oneof`_ ``event``.
        entitlement_event (google.cloud.channel_v1.types.EntitlementEvent):
            Entitlement event sent as part of Pub/Sub
            event to partners.

            This field is a member of `oneof`_ ``event``.
    """

    customer_event: "CustomerEvent" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="event",
        message="CustomerEvent",
    )
    entitlement_event: "EntitlementEvent" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="event",
        message="EntitlementEvent",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
