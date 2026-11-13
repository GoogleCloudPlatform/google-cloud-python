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
import google.type.datetime_pb2 as datetime_pb2  # type: ignore
import google.type.decimal_pb2 as decimal_pb2  # type: ignore
import google.type.money_pb2 as money_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.commerceproducer.v1beta",
    manifest={
        "PrivateOffer",
        "PrivateOfferDocument",
    },
)


class PrivateOffer(proto.Message):
    r"""Message describing PrivateOffer resource.

    Note on OPTIONAL fields: To facilitate saving incomplete draft
    offers, most fields are categorized as OPTIONAL irrespective of
    whether they are necessary for a private offer to be valid. Many
    fields labeled OPTIONAL must be set to publish the offer.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        single_product_offer (google.cloud.commerceproducer_v1beta.types.PrivateOffer.SingleProductOffer):
            Optional. Configurations for the offer that
            is associated with a single product.

            This field is a member of `oneof`_ ``content``.
        name (str):
            Identifier. Name of the resource.
        state (google.cloud.commerceproducer_v1beta.types.PrivateOffer.State):
            Output only. The state of the private offer.
        publish_requirement_google_review (google.cloud.commerceproducer_v1beta.types.PrivateOffer.PublishRequirementGoogleReview):
            Output only. Information about the Google
            review process. Present only when the offer is
            determined to require review by Google.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The creation time.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last update time.
        publish_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the offer transitioned
            to PUBLISHED state.
        accept_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the offer transitioned
            to ACCEPTED state.
        cancel_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the offer transited to
            CANCELLED state.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the offer ended. This can only be
            set for offers with ``ENDED`` state.
        cancellation_note (str):
            Output only. Internal note supplied when the
            offer was cancelled. Present only for cancelled
            offers and only if a note was supplied.
        reseller_contact (google.cloud.commerceproducer_v1beta.types.PrivateOffer.ResellerContact):
            Output only. Information about the reseller
            contact. Present only for offers created by a
            reseller.
        internal_note (str):
            Optional. Unstructured text content that is
            not visible to the customer. Intended to be used
            by partners for storing notes about the private
            offer. Maximum length: 1500 characters.
        offer_deal_type (google.cloud.commerceproducer_v1beta.types.PrivateOffer.OfferDealType):
            Optional. The type of the deal transacted
            with the offer.
            The deal type is not visible to customers.

            Must be present to publish the offer.
        title (str):
            Optional. A title that describes the offer
            and helps your customers identify it. This title
            will be visible to the customer. Maximum length:

            256 characters. Must be present to publish the
            offer.
        customer_note (str):
            Optional. Unstructured text content that is
            visible to the customer. Maximum length: 120
            characters.
        partner_contact (google.cloud.commerceproducer_v1beta.types.PrivateOffer.PartnerContact):
            Optional. Information about the partner
            contact. Must be provided when publishing the
            offer.
        customer (google.cloud.commerceproducer_v1beta.types.PrivateOffer.Customer):
            Optional. Information identifying the
            intended recipient of the offer. Must be
            provided when publishing the offer.
        accept_deadline_time (google.type.datetime_pb2.DateTime):
            Optional. Deadline for acceptance of published offers. A
            published offer not accepted by this time will expire. Only
            day boundaries in the America/Los_Angeles time zone are
            supported. Must be present to publish the offer.

            When publishing an offer the deadline must be set to a time
            in the future not more than 3 months from the time of
            publishing. For example, if the offer is published on 03/05
            at 1PM, then the deadline must be at or before 06/05 12AM
            America/Los_Angeles time.

            The deadline must also be:

            - Before or equal to the scheduled start time of this offer
              (if ``term.scheduled_start_time`` is set and the term's
              start policy is ``SCHEDULED_START_TIME``).
            - Before or equal to the scheduled end time of this offer,
              if ``term.scheduled_end_time`` is set and the term's end
              policy is ``SCHEDULED_END_TIME``.
            - Before or equal to the upcoming installment start times on
              this offer.
            - Before or equal to the amended offer's end time, if the
              offer amends another private or standard offer.
            - Before or equal to the start time of the next pending
              installment of the amended offer, if amending a private
              offer with custom installments. For example, if the
              amended offer has installments on 01/01, 02/01, 03/01,
              04/01, and today is 02/15, then this offer's
              ``accept_deadline_time`` must be at or before 03/01.

            In addition, if the offer amends another private offer, but
            there is already an accepted upcoming amendment against that
            private offer, then this deadline must be before or equal to
            the start time of the accepted upcoming offer. For example,
            today is 02/15, and this offer (offer C) amends private
            offer A, and private offer B has already been accepted which
            also amends private offer A. Private offer B has a start
            time of 03/01. Then this deadline must be at or before
            03/01. Otherwise, on 03/01, private offer B would take
            effect, superseding offer A. This would mean offer C is no
            longer amending the currently active offer (Offer A), which
            is required for valid amendments.

            Once the offer is published, this field is still updatable
            to extend the deadline of the offer. However, the extension
            is still limited to be at most 3 months from the time of
            publishing.
        term (google.cloud.commerceproducer_v1beta.types.PrivateOffer.Term):
            Optional. Configuration for the offer term.
            Must be set when publishing the offer.
    """

    class State(proto.Enum):
        r"""State of an offer.

        Values:
            STATE_UNSPECIFIED (0):
                Default value. This value is unused.
            DRAFT (1):
                The default state after creation when the
                offer can be edited. In all other states, the
                contents of the offer cannot be edited.
            PUBLISHING (2):
                The offer is publishing.
                Publishing will complete when all publishing
                requirements are satisfied.
            PUBLISHED (3):
                The offer has been published and is available
                to the customer to accept.
            ACCEPTED (4):
                The offer has been accepted by the customer.
            CANCELLED (5):
                The offer was cancelled by the provider
                before it was transacted. Cancelled offers can
                no longer be accepted by the customer.
            EXPIRED (6):
                The offer expired without being accepted by
                the customer. Expired offers can no longer be
                accepted by the customer.
            ENDED (7):
                The offer has ended.

                Ended offers were accepted and active in the
                past, but have now reached the end of their term
                or have been terminated.
        """

        STATE_UNSPECIFIED = 0
        DRAFT = 1
        PUBLISHING = 2
        PUBLISHED = 3
        ACCEPTED = 4
        CANCELLED = 5
        EXPIRED = 6
        ENDED = 7

    class OfferDealType(proto.Enum):
        r"""The type of the deal transacted with the offer. The deal type
        of an offer is a factor in determining the offer's revenue
        share.

        Values:
            OFFER_DEAL_TYPE_UNSPECIFIED (0):
                Default value. This value is unused.
            CHANNEL_SHIFT (1):
                The offer corresponds to a preexisting
                commercial arrangement for a workload on Google
                Cloud that is being transferred to the Cloud
                Marketplace.
            MIGRATION (2):
                The offer corresponds to a preexisting
                commercial arrangement for a workload previously
                not on Google Cloud that is being transferred to
                Google Cloud.
            NATIVE_RENEWAL (3):
                The offer corresponds to a renewal of a deal
                initially transacted on the Google Cloud
                Marketplace.
            NEW (4):
                The offer corresponds to a new deal transacted on the Google
                Cloud Marketplace.

                This value is not allowed if the offer amends another
                private offer where the term has not ended, and the amended
                private offer has a deal type of ``MIGRATION``,
                ``CHANNEL_SHIFT`` or ``NATIVE_RENEWAL``.
        """

        OFFER_DEAL_TYPE_UNSPECIFIED = 0
        CHANNEL_SHIFT = 1
        MIGRATION = 2
        NATIVE_RENEWAL = 3
        NEW = 4

    class PublishRequirementGoogleReview(proto.Message):
        r"""Information about the Google review process.

        Attributes:
            review_approve_time (google.protobuf.timestamp_pb2.Timestamp):
                Output only. The approval time of the Google
                review process.
        """

        review_approve_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=2,
            message=timestamp_pb2.Timestamp,
        )

    class ResellerContact(proto.Message):
        r"""Contact information for a reseller.

        Attributes:
            contact (str):
                Output only. The name of the reseller contact
                for this offer.
            email (str):
                Output only. The email of the reseller
                contact for this offer.
        """

        contact: str = proto.Field(
            proto.STRING,
            number=1,
        )
        email: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class PartnerContact(proto.Message):
        r"""Contact information for the partner representative.

        Attributes:
            contact (str):
                Optional. Display text identifying the
                partner sales contact. Displayed to the
                customer. Must be provided when publishing the
                offer.
                Maximum length: 256 characters.
            email (str):
                Optional. The email address of the partner
                sales contact. Displayed to the customer.
                The format of the provided email address is
                validated when publishing the offer, but no
                verification is performed that the email address
                actually exists, accepts email, or is otherwise
                functional.
        """

        contact: str = proto.Field(
            proto.STRING,
            number=1,
        )
        email: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class Customer(proto.Message):
        r"""Information about the customer.

        Attributes:
            entity_title (str):
                Optional. A string identifying the customer's
                entity (for example, the customer's organization
                or company name). Must be provided when
                publishing the offer. Maximum length: 256
                characters.
            contact (str):
                Optional. A string identifying the customer
                contact. Must be provided when publishing the
                offer. Maximum length: 256 characters.
            email (str):
                Optional. Email of customer contact.
                If provided, it must be a well-formed email
                address.
            address (str):
                Output only. Legal address of the customer
                organization. This field can no longer be set,
                but it is preserved to return the data from
                existing offers where address is set.
            target_billing_account (str):
                Optional. The customer's billing account targeted by the
                offer. The private offer once published can be accepted by a
                billing administrator of the target billing account. If the
                customer accepts the offer and later moves the resulting
                order to a new billing account, this field will continue to
                reflect the original billing account to which the private
                offer was extended. Must be provided when publishing the
                offer.

                To publish this private offer:

                - The billing account must exist.
                - The billing account must not be in a free trial.
                - The billing account must comply with Marketplace Reselling
                  Policies.
                - Reseller parent billing accounts are prohibited. Reseller
                  subaccounts are prohibited unless the service is enabled
                  for reselling.

                Format: billingAccounts/012345-567890-ABCDEF
        """

        entity_title: str = proto.Field(
            proto.STRING,
            number=1,
        )
        contact: str = proto.Field(
            proto.STRING,
            number=2,
        )
        email: str = proto.Field(
            proto.STRING,
            number=3,
        )
        address: str = proto.Field(
            proto.STRING,
            number=4,
        )
        target_billing_account: str = proto.Field(
            proto.STRING,
            number=5,
        )

    class Term(proto.Message):
        r"""Configurations for the offer term and renewal options.
        Extending a private offer to a customer that covers a given term
        constitutes a guarantee to the customer that the product will
        remain available to them for the duration of the term.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            duration_months (int):
                Optional. Duration in months of the offer term. The offer
                will end on the same day of the month after this duration.
                If that date is not available, the offer will end on the
                last day of the month. For example, if the offer starts on
                01/31/2024 and the duration is 13 months, the offer will end
                on 02/28/2025. Must be set to publish the offer if the end
                policy is ``AFTER_DURATION`` or ``MATCH_AMENDED_OFFER``, and
                must be a positive value.

                The maximum possible offer duration, including all renewal
                terms, cannot exceed 7 years. For example, if
                ``duration_months`` is 9 and ``term.max_renewal_count`` is
                9, then the maximum possible offer duration is 90 months and
                exceeds the 7 year limit.

                This field is a member of `oneof`_ ``end_policy_data``.
            scheduled_end_time (google.type.datetime_pb2.DateTime):
                Optional. Specified end time of the offer. Must be set to
                publish the offer if the end policy is
                ``SCHEDULED_END_TIME``. When set, the time must be in the
                future and at a day boundary in the America/Los_Angeles time
                zone, and must be after ``term.scheduled_start_time`` if
                applicable.

                This field is a member of `oneof`_ ``end_policy_data``.
            max_renewal_count (int):
                Optional. The max number of renewals allowed, after the
                initial term ends. This field is only relevant to standard
                interval offers with interval of 'MONTHLY_PRORATED',
                'MONTHLY_NOT_PRORATED', 'QUARTERLY_NOT_PRORATED' or
                'YEARLY_NOT_PRORATED'. Other types of offers cannot be
                renewed.

                For example, if the initial term is 1 year and the max
                renewals is 3, the customer can renew the offer for up to 3
                additional years after the initial term ends. Customers
                control whether they renew the offer.

                Allowing a customer to renew an offer does not constitute a
                guarantee to the customer that the offered product will
                still be available to be renewed at the renewal date.

                An offer with a max renewal count of 0 cannot be renewed.
                Must be non-negative.

                This field is a member of `oneof`_ ``renewal``.
            unlimited_renewal (bool):
                Output only. Deprecated: This field can only be true on
                existing offers with standard interval of 'MONTHLY_POSTPAY'.
                As of May 2024, we no longer allow unlimited renewals.

                This field is a member of `oneof`_ ``renewal``.
            start_policy (google.cloud.commerceproducer_v1beta.types.PrivateOffer.Term.StartPolicy):
                Optional. Defines when the resulting order
                should start. Must be set when publishing the
                offer.
            scheduled_start_time (google.type.datetime_pb2.DateTime):
                Optional. The scheduled start time of the offer. Cannot
                exceed one year from the time of publish.

                If the start policy is ``SCHEDULED_START_TIME``, a future
                time at a day boundary in the America/Los_Angeles time zone
                must be provided when publishing the offer.

                If the offer amends another private or standard offer, then
                the scheduled start time must be:

                - Before or equal to the amended offer's end time if the
                  offer's end policy is not MATCH_AMENDED_OFFER. Otherwise,
                  it has to be strictly before the amended offer's end time.
                - Before or equal to the start time of the next pending
                  installment of the amended offer, if amending a private
                  offer with custom installments. For example, if the
                  amended offer has installments on 01/01, 02/01, 03/01,
                  04/01, and today is 02/15, then the new offer's
                  ``scheduled_start_time`` must be at or before 03/01.
            end_policy (google.cloud.commerceproducer_v1beta.types.PrivateOffer.Term.EndPolicy):
                Optional. Defines when an offer should end.
                Must be set when publishing the offer.
            effective_term_end_time (google.type.datetime_pb2.DateTime):
                Output only. The expected end time of the current offer
                term.

                At the end of each offer term, an offer associated with an
                active order will either renew or end. When an offer renews,
                a new term begins and this value changes to reflect the end
                time of the new term. When an offer ends this value is no
                longer set and instead ``end_time`` is set.

                When the term of an offer ends and the offer does not renew,
                the associated order also ends if the base standard offer
                has a subscription price model. Otherwise, the associated
                order does not end and remains active.

                Not included for PRIVATE_OFFER_VIEW_BASIC. Included for
                PRIVATE_OFFER_VIEW_FULL when the offer has not ended and
                either the offer has started or the value can be derived
                from other fields.

                For offers that have not started, this field is set when one
                of the following conditions is true.

                - The offer sets ``term.scheduled_end_time``.
                - The offer sets ``term.scheduled_start_time`` and
                  ``term.duration_months``, the offer's ``term.end_policy``
                  is not ``MATCH_AMENDED_OFFER``, and the offer does not
                  have standard_interval set to ``MONTHLY_POSTPAY``.
        """

        class StartPolicy(proto.Enum):
            r"""Defines when an offer should start.

            Values:
                START_POLICY_UNSPECIFIED (0):
                    Default value. This value is unused.
                IMMEDIATE (1):
                    The resulting order starts immediately upon the customer's
                    acceptance of the offer, if no partner approval is required,
                    or else immediately after the partner approves the purchase
                    if order approval is required. This enum value cannot be
                    combined with ``term.scheduled_start_time``.
                SCHEDULED_START_TIME (2):
                    The resulting order starts at the scheduled
                    start time.
            """

            START_POLICY_UNSPECIFIED = 0
            IMMEDIATE = 1
            SCHEDULED_START_TIME = 2

        class EndPolicy(proto.Enum):
            r"""Defines when an offer should end.

            Values:
                END_POLICY_UNSPECIFIED (0):
                    Default value. This value is unused.
                AFTER_DURATION (1):
                    Offer ends after the specified duration. If this is set,
                    then ``duration_months`` must be positive.
                SCHEDULED_END_TIME (2):
                    Offer ends at the schduled time.
                MATCH_AMENDED_OFFER (3):
                    Offer coterms to the amended offer - the offer ends at the
                    end of the amended offer's term

                    For example, if the amended offer starts on 01/15/24, and
                    has a duration of 6 months, then it ends on 07/15/24. If the
                    current offer coterms to the previous offer, and the current
                    offer starts on 05/06/24, then it will still end on
                    07/15/24. Assuming the current offer renews 3 times, then
                    the terms on the current offer will be:

                    1. 05/06/24 - 07/15/24 (First term, ends on 07/15 to coterm
                       with the amended offer)
                    2. 07/15/24 - 01/15/25 (First renewal term)
                    3. 01/15/25 - 07/15/25 (Second renewal term)
                    4. 07/15/25 - 01/15/26 (Third renewal term)

                    As a contrast, if the current offer does not coterm with the
                    amended offer (such as when ``end_policy`` is
                    ``AFTER_DURATION``), then the terms will be:

                    1. 05/06/24 - 11/06/24 (First term, ends on 11/06, no
                       coterming)
                    2. 11/06/24 - 05/06/25 (First renewal term)
                    3. 05/06/25 - 11/06/25 (Second renewal term)
                    4. 11/06/25 - 05/06/26 (Third renewal term)

                    If this is set, then the following conditions must be met:

                    - ``single_product_offer.amended_private_offer`` must be
                      set, and the amended private offer must not be ended.
                    - The proration policy must not change (e.g., you cannot
                      switch between ``MONTHLY_PRORATED`` and
                      ``MONTHLY_NOT_PRORATED``).
                    - The current offer must not have custom intervals (where
                      ``custom_interval_price`` is set).
                    - ``term.duration_months`` must match the amended private
                      offer's duration.
                    - The amended private offer must not have a standard
                      interval of ``MONTHLY_POSTPAY``.

                    This is currently not supported.
            """

            END_POLICY_UNSPECIFIED = 0
            AFTER_DURATION = 1
            SCHEDULED_END_TIME = 2
            MATCH_AMENDED_OFFER = 3

        duration_months: int = proto.Field(
            proto.INT32,
            number=4,
            oneof="end_policy_data",
        )
        scheduled_end_time: datetime_pb2.DateTime = proto.Field(
            proto.MESSAGE,
            number=5,
            oneof="end_policy_data",
            message=datetime_pb2.DateTime,
        )
        max_renewal_count: int = proto.Field(
            proto.INT32,
            number=6,
            oneof="renewal",
        )
        unlimited_renewal: bool = proto.Field(
            proto.BOOL,
            number=7,
            oneof="renewal",
        )
        start_policy: "PrivateOffer.Term.StartPolicy" = proto.Field(
            proto.ENUM,
            number=1,
            enum="PrivateOffer.Term.StartPolicy",
        )
        scheduled_start_time: datetime_pb2.DateTime = proto.Field(
            proto.MESSAGE,
            number=2,
            message=datetime_pb2.DateTime,
        )
        end_policy: "PrivateOffer.Term.EndPolicy" = proto.Field(
            proto.ENUM,
            number=3,
            enum="PrivateOffer.Term.EndPolicy",
        )
        effective_term_end_time: datetime_pb2.DateTime = proto.Field(
            proto.MESSAGE,
            number=8,
            message=datetime_pb2.DateTime,
        )

    class SingleProductOffer(proto.Message):
        r"""Configurations for the offer that is associated with a single
        product.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            amended_private_offer (str):
                Optional. An existing private offer that will be superseded
                by this offer. Unless the private offer is for a product
                type that supports `multiple active
                orders <https://cloud.google.com/marketplace/docs/partners/offers/multiple-offers>`__,
                an amendment private offer must be transacted if and only if
                the destination customer billing account already contains an
                active order for the same product. The offer to be
                superseded must be the offer associated with an active
                order.

                Amendments generally fall into one of two scenarios:

                1. **Active Order / Ended Offer**: The term of the amended
                   offer has ended but it is still associated with an active
                   order. The new offer must amend the ended private offer.
                2. **Active Order / Active Offer**: The term of the amended
                   offer is still active and the associated order is active.
                   Similar to above, the new offer must amend the currently
                   active offer (unless "multiple active orders" are
                   supported).

                If this is set, then the ``base_standard_offer`` parent
                service must match the parent service of the
                ``base_standard_offer`` in the ``amended_private_offer``.

                **Active Term Restrictions**: If the term of the amended
                private offer has *NOT* ended, then the following
                compatibility rules apply:

                - **Price Model Compatibility**:

                  - Flat Fee (with or without usage) offers can amend Flat
                    Fee offers.
                  - Usage-only or CUD offers can amend usage-only offers.
                  - Commitment-based offers must amend offers of the same
                    price model subtype (e.g., "additional usage at list
                    price" vs "all usage discounted").

                - **Billing Frequency Compatibility**: Determined by
                  ``standard_interval`` or ``custom_interval_price``.

                  - If the amended offer has a custom billing frequency, the
                    new offer must also have a custom frequency.
                  - If the amended offer has a standard frequency (Monthly,
                    Quarterly, or Yearly), the new offer must maintain the
                    same frequency or transition to a custom frequency.
                  - Switching between different standard frequencies (e.g.,
                    Monthly to Quarterly) is not supported.
                  - For Monthly frequency, switching between
                    ``MONTHLY_PRORATED`` and ``MONTHLY_NOT_PRORATED`` is
                    supported, unless the offer's ``term.end_policy`` is
                    ``MATCH_AMENDED_OFFER``.
                  - For usage-only offers, there are no billing frequency
                    restrictions.

                Other criteria for offer amendment are detailed elsewhere.

                This field is a member of `oneof`_ ``amended_offer``.
            amended_standard_offer (str):
                Optional. An existing standard offer that will be superseded
                by this offer. An amendment private offer must be transacted
                if the destination customer billing account already contains
                an active order for the same product, and otherwise cannot
                be transacted. The offer to be superseded must be the offer
                associated with the active order.

                If this is set, then the ``base_standard_offer`` must
                contain the same parent service as the parent service of the
                ``amended_standard_offer``. The price model of this offer
                must be compatible with the price model of the
                ``amended_standard_offer``:

                - Flat Fee, or Flat Fee with usage offers can amend Flat Fee
                  or Flat Fee with usage standard offers.
                - Usage-only offers, or CUD offers can amend usage-only
                  standard offers.

                Other criteria for offer amendment are detailed elsewhere.

                This field is a member of `oneof`_ ``amended_offer``.
            standard_interval_price (google.cloud.commerceproducer_v1beta.types.PrivateOffer.SingleProductOffer.StandardIntervalPrice):
                Optional. Price configurations for offers
                with standard intervals. A price must be set
                when publishing the offer.

                This field is a member of `oneof`_ ``price``.
            custom_interval_price (google.cloud.commerceproducer_v1beta.types.PrivateOffer.SingleProductOffer.CustomIntervalPrice):
                Optional. Price configurations for offers
                with custom intervals. Custom interval
                corresponds to "custom billing frequency", see
                https://docs.cloud.google.com/marketplace/docs/partners/offers/select-payment-schedule.
                A price must be set when publishing the offer.

                This field is a member of `oneof`_ ``price``.
            base_standard_offer (str):
                Optional. The StandardOffer this PrivateOffer is based on.
                Must be in the same project as the private offer, and must
                be effective at the time of publishing. Must be present to
                publish the offer.

                Format:
                projects/{project}/locations/{location}/services/{service}/standardOffers/{standard_offer}
            service_level (str):
                Output only. The service level (also known as
                the 'plan') of the base standard offer. The
                value is populated at publish time from the base
                standard offer.
            reseller_private_offer_plan_id (str):
                Output only. Present for offers created by a reseller from a
                reseller private offer plan (RPOP). When set, contains the
                ID of the originating RPOP. Not included for
                ``PRIVATE_OFFER_VIEW_BASIC``.
            features (MutableSequence[google.cloud.commerceproducer_v1beta.types.PrivateOffer.SingleProductOffer.Feature]):
                Optional. The custom product features to display for this
                offer. Feature ``display_name`` values must be unique to
                publish the offer. The set of features specified here should
                generally include all features included in the base service
                level, with optionally customized values, but is not
                required to match exactly and may include additional
                features.
            effective_installment_timeline (MutableSequence[google.cloud.commerceproducer_v1beta.types.PrivateOffer.SingleProductOffer.Installment]):
                Output only. The effective installment timeline of the
                offer. Not included for ``PRIVATE_OFFER_VIEW_BASIC``.
                Included for ``PRIVATE_OFFER_VIEW_FULL`` if all necessary
                information is available to generate the timeline, and if
                the offer has 'standard_interval_price' of
                'MONTHLY_PRORATED', 'MONTHLY_NOT_PRORATED',
                'QUARTERLY_NOT_PRORATED', or 'YEARLY_NOT_PRORATED'.
            contract_value (google.cloud.commerceproducer_v1beta.types.PrivateOffer.SingleProductOffer.ContractValue):
                Output only. Contract value of the offer. Not included for
                ``PRIVATE_OFFER_VIEW_BASIC``.
            revenue_share (google.cloud.commerceproducer_v1beta.types.PrivateOffer.SingleProductOffer.RevenueShare):
                Output only. Revenue share information for this Private
                Offer. Not included for ``PRIVATE_OFFER_VIEW_BASIC``.
            additional_contract_value (google.cloud.commerceproducer_v1beta.types.PrivateOffer.SingleProductOffer.AdditionalContractValue):
                Optional. Additional contract value that the
                customer is legally obligated to spend on the
                product over the duration of the offer.
        """

        class Feature(proto.Message):
            r"""Additional details used to describe customization of the
            service level.
            Features are used to distinguish service levels of the same
            product. When a product has a single service level, all details
            can be contained in the product documentation. When a product
            has multiple service levels, each service level can be assigned
            a distinct set of features to distinguish the key differences
            between the service levels.

            In addition to customizing pricing and other transaction
            details, a private offer may include customization of
            partner-managed product behavior. When this is the case, the
            details of the custom behavior are described using features.

            Attributes:
                display_name (str):
                    Optional. Human readable display text
                    characterizing the feature. Should be
                    sufficiently detailed to identify the feature,
                    allowing features to be correlated across
                    separate offers and service levels. Must be
                    non-empty to publish the offer.
                    The maximum allowed length is 128 characters.
                    Allows characters from the following Unicode
                    Property Classes:

                    Letters, Numbers, Punctuation, Symbols, and
                    Separators
                value (str):
                    Optional. Human readable display text reflecting the value
                    of the feature. Used for variable features not captured by
                    the display_name alone. The maximum allowed length is 3000
                    characters. Allows characters from the following Unicode
                    Property Classes: Letters, Numbers, Punctuation, Symbols,
                    and Separators
            """

            display_name: str = proto.Field(
                proto.STRING,
                number=1,
            )
            value: str = proto.Field(
                proto.STRING,
                number=2,
            )

        class PriceModel(proto.Message):
            r"""The price model of the private offer.

            Private offers are referred to as having different kinds of price
            models based on the combination of fields set in the price model.
            The following terminology is used in documentation and other
            reference material.

            - Usage-based: the price model does not set ``flat_fee``
            - Usage-only: the price model sets only ``usage``
            - CUD (committed use discount): the price model sets ``commitment``

              - Commitment discount with additional usage at list price: The
                price model sets ``commitment`` and not ``usage``.
              - Commitment with all usage discounted: The price model sets
                ``commitment`` and ``usage``.

            - Flat fee: the price model sets only ``flat_fee``
            - Flat fee with usage: the price model sets ``flat_fee`` and
              ``usage``

            See
            https://docs.cloud.google.com/marketplace/docs/partners/offers/select-pricing-model#CUD
            for the price models.

            This message has `oneof`_ fields (mutually exclusive fields).
            For each oneof, at most one member field can be set at the same time.
            Setting any member of the oneof automatically clears all other
            members.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                flat_fee (google.cloud.commerceproducer_v1beta.types.PrivateOffer.SingleProductOffer.PriceModel.FlatFee):
                    Optional. The price configurations for the
                    flat fee subscription. Must be unset when the
                    base standard offer's price model does not
                    include subscription SKUs.

                    This field is a member of `oneof`_ ``subscription``.
                commitment (google.cloud.commerceproducer_v1beta.types.PrivateOffer.SingleProductOffer.PriceModel.Commitment):
                    Optional. The price configurations for the
                    commitment based subscription. Must be unset
                    when the base standard offer's price model
                    includes subscription SKUs.

                    This field is a member of `oneof`_ ``subscription``.
                usage (google.cloud.commerceproducer_v1beta.types.PrivateOffer.SingleProductOffer.PriceModel.Usage):
                    Optional. The price configurations for the usage part. If
                    this field is set, the ``Commitment.discount_percent`` must
                    be unset. A private offer can apply a discount to all usage
                    or to a usage commitment, but not both. Must be unset when
                    the base standard offer's price model includes no usage
                    SKUs.
            """

            class SkuDiscount(proto.Message):
                r"""The discount for a specific SKU.

                This message has `oneof`_ fields (mutually exclusive fields).
                For each oneof, at most one member field can be set at the same time.
                Setting any member of the oneof automatically clears all other
                members.

                .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

                Attributes:
                    sku (str):
                        Optional. The name of a partner SKU from this
                        API.
                        Must refer to a SKU in the price model of the
                        base standard offer. Inclusion in the base price
                        model can occur either directly or indirectly
                        via inclusion in an included SkuGroup.

                        Currently, standard offer price models include
                        only partner SKUs in the same project as the
                        standard offer. This may change.

                        Format:

                        projects/{project}/locations/{location}/services/{service}/skus/{sku}

                        This field is a member of `oneof`_ ``target``.
                    cloud_billing_sku (str):
                        Optional. The name of a Google SKU from the
                        Cloud Billing API.
                        Used for partner products sold by Google, such
                        as Premium Operating System Images sold for use
                        in Compute Engine. This is not common. SKUs of
                        this type are not present on this API and can
                        instead be found on the Cloud Billing API or at
                        https://cloud.google.com/skus.

                        Must refer to a SKU in the price model of the
                        base standard offer. Google SKUs are always
                        referenced in standard offers via SkuGroups.

                        Format: services/{service}/skus/{sku}

                        This field is a member of `oneof`_ ``target``.
                    discount_percent (google.type.decimal_pb2.Decimal):
                        Optional. The discount percent for the SKU. For example,
                        ``10`` means a discount of 10%. If the original SKU price is
                        $100/hour then the discounted price will be $90/hour.

                        Must be between 0 and 100 inclusive, with precision up to 2
                        decimal places. If this field is set, then the allowed
                        pattern for 'value' is
                        ``^([0-9]{1,2}(\\.\\d{1,2})?|100(\\.0{1,2})?)$``.

                        Examples of valid values: "0", "100.0", "12.34", "40.0".
                        Example of invalid values: ".3", "-1", "100.1", "12.345",
                        "+12", and "". Must be present to publish the offer.

                        This field is a member of `oneof`_ ``discount``.
                """

                sku: str = proto.Field(
                    proto.STRING,
                    number=1,
                    oneof="target",
                )
                cloud_billing_sku: str = proto.Field(
                    proto.STRING,
                    number=3,
                    oneof="target",
                )
                discount_percent: decimal_pb2.Decimal = proto.Field(
                    proto.MESSAGE,
                    number=2,
                    oneof="discount",
                    message=decimal_pb2.Decimal,
                )

            class Usage(proto.Message):
                r"""The price for the usage SKUs.

                Attributes:
                    default_discount_percent (google.type.decimal_pb2.Decimal):
                        Optional. The default discount percent for usage SKUs. An
                        unset default discount percent is equivalent to 0 (no
                        discount).

                        Must be between 0 and 100 inclusive, with precision up to 2
                        decimal places. If this field is set, then the allowed
                        pattern for 'value' is
                        ``^([0-9]{1,2}(\\.\\d{1,2})?|100(\\.0{1,2})?)$``. Examples
                        of valid values: "0", "100.0", "12.34", "40.0". Example of
                        invalid values: ".3", "-1", "100.1", "12.345", "+12", "".
                    sku_discounts (MutableSequence[google.cloud.commerceproducer_v1beta.types.PrivateOffer.SingleProductOffer.PriceModel.SkuDiscount]):
                        Optional. The discounts for the specific SKUs that override
                        the ``default_discount_percent``.
                """

                default_discount_percent: decimal_pb2.Decimal = proto.Field(
                    proto.MESSAGE,
                    number=1,
                    message=decimal_pb2.Decimal,
                )
                sku_discounts: MutableSequence[
                    "PrivateOffer.SingleProductOffer.PriceModel.SkuDiscount"
                ] = proto.RepeatedField(
                    proto.MESSAGE,
                    number=2,
                    message="PrivateOffer.SingleProductOffer.PriceModel.SkuDiscount",
                )

            class FlatFee(proto.Message):
                r"""The price configurations for the flat fee subscriptions.

                Attributes:
                    flat_fee_override (google.type.money_pb2.Money):
                        Optional. Flat fee overriding the default
                        flat fee in the base standard offer. Value
                        cannot be negative. The currency must be "USD"
                        and precision is limited to cents. Must be
                        present to publish the offer, if the parent
                        message is set. The maximum allowed value is
                        1,000,000,000 USD.
                """

                flat_fee_override: money_pb2.Money = proto.Field(
                    proto.MESSAGE,
                    number=1,
                    message=money_pb2.Money,
                )

            class Commitment(proto.Message):
                r"""The price configurations for the commitment based
                subscriptions.

                Attributes:
                    commitment_amount (google.type.money_pb2.Money):
                        Optional. The commitment balance that the customer will
                        receive. Value cannot be negative. The currency must be
                        "USD" and precision is limited to cents. Must be present to
                        publish the offer, if the parent message is set. The maximum
                        allowed value is 1,000,000,000 USD.

                        If the current offer amends a private offer where the term
                        has not ended, and if the field
                        ``single_product_offer.standard_interval_price.price_model.commitment.commitment_amount``
                        is set on both the current offer and the amended private
                        offer, then the commitment amount must be equal or higher on
                        the current offer, compared to the amended private offer.
                    discount_percent (google.type.decimal_pb2.Decimal):
                        Optional. The discount percent on ``commitment_amount``.

                        For example, ``10`` means a discount of 10%. If the original
                        ``commitment_amount`` is $100 then the discounted amount
                        will be $90. The customer is charged $90 and receives $100
                        in credits.

                        All reported usage will be charged at the standard price. If
                        this field is set, the ``price_model.usage`` must be unset.
                        A private offer can apply a discount to all usage or to a
                        usage commitment, but not both.

                        Must be between 0 and 100 inclusive, with precision up to 2
                        decimal places. If this field is set, then the allowed
                        pattern for 'value' is
                        ``^([0-9]{1,2}(\\.\\d{1,2})?|100(\\.0{1,2})?)$``. Examples
                        of valid values: "0", "100.0", "12.34", "40.0". Example of
                        invalid values: ".3", "-1", "100.1", "12.345", "+12", "".

                        Must be present to publish the offer.
                    additional_credit (google.type.money_pb2.Money):
                        Optional. Additional credit granted to the customer.
                        Additional credits are only supported for custom interval
                        offers. Equivalent behavior can be achieved for standard
                        interval offers by varying the ``commitment_amount`` and
                        ``discount_percent``.

                        Value cannot be negative. The currency must be "USD" and
                        precision is limited to cents. The maximum allowed value is
                        1,000,000 USD.
                    discard_previous_credit_balance (bool):
                        Optional. Whether to discard the previous
                        credit balance when the associated installment
                        starts. If not set, the previous credit balance
                        will be rolled over to the current installment.

                        If there are no previous installments, then the
                        value of this field will not matter - since it
                        has no effect when no credits exist.
                """

                commitment_amount: money_pb2.Money = proto.Field(
                    proto.MESSAGE,
                    number=1,
                    message=money_pb2.Money,
                )
                discount_percent: decimal_pb2.Decimal = proto.Field(
                    proto.MESSAGE,
                    number=2,
                    message=decimal_pb2.Decimal,
                )
                additional_credit: money_pb2.Money = proto.Field(
                    proto.MESSAGE,
                    number=3,
                    message=money_pb2.Money,
                )
                discard_previous_credit_balance: bool = proto.Field(
                    proto.BOOL,
                    number=4,
                )

            flat_fee: "PrivateOffer.SingleProductOffer.PriceModel.FlatFee" = (
                proto.Field(
                    proto.MESSAGE,
                    number=2,
                    oneof="subscription",
                    message="PrivateOffer.SingleProductOffer.PriceModel.FlatFee",
                )
            )
            commitment: "PrivateOffer.SingleProductOffer.PriceModel.Commitment" = (
                proto.Field(
                    proto.MESSAGE,
                    number=3,
                    oneof="subscription",
                    message="PrivateOffer.SingleProductOffer.PriceModel.Commitment",
                )
            )
            usage: "PrivateOffer.SingleProductOffer.PriceModel.Usage" = proto.Field(
                proto.MESSAGE,
                number=1,
                message="PrivateOffer.SingleProductOffer.PriceModel.Usage",
            )

        class StandardIntervalPrice(proto.Message):
            r"""Price configurations for offers with standard intervals.

            Attributes:
                standard_interval (google.cloud.commerceproducer_v1beta.types.PrivateOffer.SingleProductOffer.StandardIntervalPrice.StandardInterval):
                    Optional. The standard interval of the offer.
                    Must be present to publish unless the price
                    model is usage-only.
                price_model (google.cloud.commerceproducer_v1beta.types.PrivateOffer.SingleProductOffer.PriceModel):
                    Optional. The price model of the offer.
                    Must be present to publish the offer.
            """

            class StandardInterval(proto.Enum):
                r"""The options for offers with standard intervals.

                Values:
                    STANDARD_INTERVAL_UNSPECIFIED (0):
                        The private offer does not have an interval. If this is set,
                        then the offer is "usage-only". Field
                        ``term.duration_months`` must be positive.
                    MONTHLY_POSTPAY (1):
                        The schedule of the monthly postpay offers.
                        This type of offer has "Monthly" billing
                        frequency (see
                        https://docs.cloud.google.com/marketplace/docs/partners/offers/select-payment-schedule).
                        No longer supported as of May 2024. Cannot be
                        used to publish new offers.
                    MONTHLY_PRORATED (2):
                        Monthly installments with proration. This type of offer has
                        "Monthly" billing frequency (see
                        https://docs.cloud.google.com/marketplace/docs/partners/offers/select-payment-schedule).
                        For example, if the offer starts on 04/15, and the offer
                        duration is 3 months, the following installments will be
                        created:

                        1: from 04/15 to 05/01, at the prorated price for April.
                        ========================================================

                        2: from 05/01 to 06/01, at the full monthly price for May.
                        ==========================================================

                        3: from 06/01 to 07/01, at the full monthly price for June.
                        ===========================================================

                        4: from 07/01 to 07/15, at the prorated price for July.
                        =======================================================

                        All dates represent the start of that day in the
                        America/Los_Angeles time zone.

                        If this is set:

                        - The ``PriceModel.subscription`` oneof must be set.
                        - Field ``term.duration_months`` must be positive.
                    MONTHLY_NOT_PRORATED (3):
                        Monthly installments without proration. This type of offer
                        has "Monthly" billing frequency (see
                        https://docs.cloud.google.com/marketplace/docs/partners/offers/select-payment-schedule).
                        For example, if the offer starts on 04/15, and the offer
                        duration is 3 months, the following installments will be
                        created:

                        1: from 04/15 to 05/15, at the full monthly price.
                        ==================================================

                        2: from 05/15 to 06/15, at the full monthly price.
                        ==================================================

                        3: from 06/15 to 07/15, at the full monthly price.
                        ==================================================

                        All dates represent the start of that day in the
                        America/Los_Angeles time zone.

                        If this is set:

                        - The ``PriceModel.subscription`` oneof must be set.
                        - Field ``term.duration_months`` must be positive.
                    QUARTERLY_NOT_PRORATED (4):
                        Quarterly installments which are not prorated. This type of
                        offer has "Quarterly" billing frequency (see
                        https://docs.cloud.google.com/marketplace/docs/partners/offers/select-payment-schedule).
                        For example, if the offer starts on 01/15, and the offer
                        duration is 3 quarters, the following installments will be
                        created:

                        1: from 01/15 to 04/15, at the full quarterly price.
                        ====================================================

                        2: from 04/15 to 07/15, at the full quarterly price.
                        ====================================================

                        3: from 07/15 to 10/15, at the full quarterly price.
                        ====================================================

                        All dates represent the start of that day in the
                        America/Los_Angeles time zone.

                        If this is set:

                        - The ``PriceModel.subscription`` oneof must be set.
                        - Field ``term.duration_months`` must be positive.
                    YEARLY_NOT_PRORATED (5):
                        Yearly installments which are not prorated. This type of
                        offer has "Yearly" billing frequency (see
                        https://docs.cloud.google.com/marketplace/docs/partners/offers/select-payment-schedule).
                        For example, if the offer starts on 01/15/2025, and the
                        offer duration is 3 years, the following installments will
                        be created:

                        1: from 01/15/2025 to 01/15/2026, at the full yearly price.
                        ===========================================================

                        2: from 01/15/2026 to 01/15/2027, at the full yearly price.
                        ===========================================================

                        3: from 01/15/2027 to 01/15/2028, at the full yearly price.
                        ===========================================================

                        All dates represent the start of that day in the
                        America/Los_Angeles time zone.

                        If this is set:

                        - The ``PriceModel.subscription`` oneof must be set.
                        - Field ``term.duration_months`` must be positive.
                """

                STANDARD_INTERVAL_UNSPECIFIED = 0
                MONTHLY_POSTPAY = 1
                MONTHLY_PRORATED = 2
                MONTHLY_NOT_PRORATED = 3
                QUARTERLY_NOT_PRORATED = 4
                YEARLY_NOT_PRORATED = 5

            standard_interval: "PrivateOffer.SingleProductOffer.StandardIntervalPrice.StandardInterval" = proto.Field(
                proto.ENUM,
                number=1,
                enum="PrivateOffer.SingleProductOffer.StandardIntervalPrice.StandardInterval",
            )
            price_model: "PrivateOffer.SingleProductOffer.PriceModel" = proto.Field(
                proto.MESSAGE,
                number=2,
                message="PrivateOffer.SingleProductOffer.PriceModel",
            )

        class Installment(proto.Message):
            r"""An installment of the offer.

            Attributes:
                start_time (google.type.datetime_pb2.DateTime):
                    Optional. The start time of the installment. Each
                    installment must have a unique start time with one
                    exception: When the ``term.start_policy`` of the offer's
                    term is ``IMMEDIATE``, the ``start_time`` of the first
                    installment must be unset. The actual start time is not
                    recorded in the offer and instead is determined by the time
                    the resulting order became active.

                    When the ``term.start_policy`` of the offer's term is
                    ``SCHEDULED_START_TIME``, then the first installment's
                    ``start_time`` must match ``term.scheduled_start_time``.

                    If the ``term.end_policy`` of the offer's term is
                    ``SCHEDULED_END_TIME``, then installment ``start_time`` must
                    be before ``term.scheduled_end_time``. If it's
                    ``AFTER_DURATION``, then installment ``start_time`` must be
                    before the time calculated by adding the
                    ``term.duration_months`` to the start time of the offer.

                    The ``start_time`` of the installments cannot be before the
                    ``accept_deadline_time`` of the offer.

                    Installment start times must be in strictly increasing
                    chronological order.
                price_model (google.cloud.commerceproducer_v1beta.types.PrivateOffer.SingleProductOffer.PriceModel):
                    Optional. The price model of the installment.
                    All installments must have the same form of
                    price model.
            """

            start_time: datetime_pb2.DateTime = proto.Field(
                proto.MESSAGE,
                number=1,
                message=datetime_pb2.DateTime,
            )
            price_model: "PrivateOffer.SingleProductOffer.PriceModel" = proto.Field(
                proto.MESSAGE,
                number=2,
                message="PrivateOffer.SingleProductOffer.PriceModel",
            )

        class CustomIntervalPrice(proto.Message):
            r"""Price configurations for offers with custom intervals.

            Attributes:
                installments (MutableSequence[google.cloud.commerceproducer_v1beta.types.PrivateOffer.SingleProductOffer.Installment]):
                    Optional. The installments that make up the
                    installment timeline. All installments must have
                    the same form of price model (e.g. all
                    commitment, or all flat fee). A subscription
                    must be present under the price model for every
                    installment.

                    Must contain at least one installment to publish
                    the offer.
            """

            installments: MutableSequence[
                "PrivateOffer.SingleProductOffer.Installment"
            ] = proto.RepeatedField(
                proto.MESSAGE,
                number=1,
                message="PrivateOffer.SingleProductOffer.Installment",
            )

        class ContractValue(proto.Message):
            r"""The contract value of the offer.

            Attributes:
                total_contract_value (google.type.money_pb2.Money):
                    Output only. The total contract value of the offer. This
                    will be set for all non-draft private offers, as long as
                    'PRIVATE_OFFER_VIEW_FULL' is requested. For DRAFT private
                    offers, this will be populated only when the end user's
                    billing account is set and when the pricing and term
                    configuration is sufficiently complete to allow for a
                    calculation.
            """

            total_contract_value: money_pb2.Money = proto.Field(
                proto.MESSAGE,
                number=1,
                message=money_pb2.Money,
            )

        class RevenueShare(proto.Message):
            r"""Revenue Share information for a Private Offer. For more details
            about the revenue share, including how the value is determined, see
            https://docs.cloud.google.com/marketplace/docs/partners/revenue-share-scenarios.

            Not included for ``PRIVATE_OFFER_VIEW_BASIC``, or for DRAFT private
            offers.

            For non-draft private offers, these fields are populated based on
            the following:

            - Offers published after April 20, 2025 will always have revenue
              share fields populated.
            - Offers published on or before April 20, 2025 will only have
              revenue share fields populated if they were associated with an
              active, unexpired order on that date.

            Attributes:
                current_term_vendor_net_revenue_percent (google.type.decimal_pb2.Decimal):
                    Output only. The revenue share currently in
                    effect.
                    The range of the value is between 0 and 100. For
                    example, 80 means the Vendor's current term
                    revenue share is 80%. The vendor will keep 80%
                    of the revenue.
                    .
                renewal_term_vendor_net_revenue_percent (google.type.decimal_pb2.Decimal):
                    Output only. The expected revenue share for
                    the renewal term. Not included if the offer does
                    not have renewal terms.

                    The range of the value is between 0 and 100. For
                    example, 80 means the Vendor's current term
                    revenue share is 80%. The vendor will keep 80%
                    of the revenue after renewal.
                    .
            """

            current_term_vendor_net_revenue_percent: decimal_pb2.Decimal = proto.Field(
                proto.MESSAGE,
                number=1,
                message=decimal_pb2.Decimal,
            )
            renewal_term_vendor_net_revenue_percent: decimal_pb2.Decimal = proto.Field(
                proto.MESSAGE,
                number=2,
                message=decimal_pb2.Decimal,
            )

        class AdditionalContractValue(proto.Message):
            r"""Additional contract value that represents a spend obligation
            or target contract value tracked out-of-band by the partner.

            Attributes:
                contract_value (google.type.money_pb2.Money):
                    Optional. The absolute, cumulative contract value of the
                    customer's spend obligation that is added on top of the
                    automatically billed fees from Google. This amount is not
                    automatically billed or invoiced by Google; instead, it is
                    tracked as a legal spend guarantee to be met via usage
                    reporting and manually trued-up by partners.

                    The overall total contract value of the offer is calculated
                    as the sum of Google-billed fees (from installments), plus
                    this additional contract value.

                    For amendments, this field must be set to the new cumulative
                    additional total.

                    For example:

                    - Initial Offer: 3 installments of $15 (total $45 billed by
                      Google) plus an ``additional_contract_value`` of $100
                      (billed by Partner, with true-ups happening at the end of
                      the offer's term). The overall total contract value of the
                      offer is $145 ($45 + $100).
                    - Amended Offer: 6 installments of $15 (total $90 billed by
                      Google) plus an ``additional_contract_value`` of $70
                      (billed by Partner, with true-ups happening at the end of
                      the offer's term). The overall total contract value of the
                      amended offer is $160 ($90 + $70).

                    Must be non-negative. The maximum allowed value is
                    1,000,000,000 USD.
                eligible_skus (MutableSequence[str]):
                    Optional. The resource names of the SKUs
                    whose tracked usage is eligible to contribute
                    toward satisfying this additional contract value
                    obligation.

                    This list explicitly separates core spend
                    obligations from exclusions like overage fees,
                    which do not count toward meeting the customer's
                    legal spend commitment.

                    Must be non-empty for the offer to be published.

                    Format:

                    projects/{project}/locations/{location}/services/{service}/skus/{sku}
            """

            contract_value: money_pb2.Money = proto.Field(
                proto.MESSAGE,
                number=1,
                message=money_pb2.Money,
            )
            eligible_skus: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=2,
            )

        amended_private_offer: str = proto.Field(
            proto.STRING,
            number=3,
            oneof="amended_offer",
        )
        amended_standard_offer: str = proto.Field(
            proto.STRING,
            number=4,
            oneof="amended_offer",
        )
        standard_interval_price: "PrivateOffer.SingleProductOffer.StandardIntervalPrice" = proto.Field(
            proto.MESSAGE,
            number=5,
            oneof="price",
            message="PrivateOffer.SingleProductOffer.StandardIntervalPrice",
        )
        custom_interval_price: "PrivateOffer.SingleProductOffer.CustomIntervalPrice" = (
            proto.Field(
                proto.MESSAGE,
                number=6,
                oneof="price",
                message="PrivateOffer.SingleProductOffer.CustomIntervalPrice",
            )
        )
        base_standard_offer: str = proto.Field(
            proto.STRING,
            number=1,
        )
        service_level: str = proto.Field(
            proto.STRING,
            number=2,
        )
        reseller_private_offer_plan_id: str = proto.Field(
            proto.STRING,
            number=10,
        )
        features: MutableSequence["PrivateOffer.SingleProductOffer.Feature"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=8,
                message="PrivateOffer.SingleProductOffer.Feature",
            )
        )
        effective_installment_timeline: MutableSequence[
            "PrivateOffer.SingleProductOffer.Installment"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=7,
            message="PrivateOffer.SingleProductOffer.Installment",
        )
        contract_value: "PrivateOffer.SingleProductOffer.ContractValue" = proto.Field(
            proto.MESSAGE,
            number=11,
            message="PrivateOffer.SingleProductOffer.ContractValue",
        )
        revenue_share: "PrivateOffer.SingleProductOffer.RevenueShare" = proto.Field(
            proto.MESSAGE,
            number=12,
            message="PrivateOffer.SingleProductOffer.RevenueShare",
        )
        additional_contract_value: "PrivateOffer.SingleProductOffer.AdditionalContractValue" = proto.Field(
            proto.MESSAGE,
            number=13,
            message="PrivateOffer.SingleProductOffer.AdditionalContractValue",
        )

    single_product_offer: SingleProductOffer = proto.Field(
        proto.MESSAGE,
        number=12,
        oneof="content",
        message=SingleProductOffer,
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=3,
        enum=State,
    )
    publish_requirement_google_review: PublishRequirementGoogleReview = proto.Field(
        proto.MESSAGE,
        number=4,
        message=PublishRequirementGoogleReview,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    publish_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    accept_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    cancel_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=22,
        message=timestamp_pb2.Timestamp,
    )
    cancellation_note: str = proto.Field(
        proto.STRING,
        number=11,
    )
    reseller_contact: ResellerContact = proto.Field(
        proto.MESSAGE,
        number=20,
        message=ResellerContact,
    )
    internal_note: str = proto.Field(
        proto.STRING,
        number=16,
    )
    offer_deal_type: OfferDealType = proto.Field(
        proto.ENUM,
        number=21,
        enum=OfferDealType,
    )
    title: str = proto.Field(
        proto.STRING,
        number=2,
    )
    customer_note: str = proto.Field(
        proto.STRING,
        number=17,
    )
    partner_contact: PartnerContact = proto.Field(
        proto.MESSAGE,
        number=14,
        message=PartnerContact,
    )
    customer: Customer = proto.Field(
        proto.MESSAGE,
        number=13,
        message=Customer,
    )
    accept_deadline_time: datetime_pb2.DateTime = proto.Field(
        proto.MESSAGE,
        number=5,
        message=datetime_pb2.DateTime,
    )
    term: Term = proto.Field(
        proto.MESSAGE,
        number=15,
        message=Term,
    )


class PrivateOfferDocument(proto.Message):
    r"""Message describing the PrivateOfferDocument resource. Used to attach
    documents to a private offer in state DRAFT. Once a private offer is
    no longer in state DRAFT, the set of child documents is immutable.
    Existing documents cannot be updated or deleted, and new documents
    cannot be added.

    A private offer may have at most one document of each type, and may
    not have both a standard EULA and a custom EULA.

    Which document types are required, optional, or not permitted
    depends on the service the offer is for, and is returned in
    ``Service.document_requirement``.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        inline_content (bytes):
            Optional. Byte content of an unstructured
            document. Max size: 4MB

            This field is a member of `oneof`_ ``content``.
        name (str):
            Identifier. Name of the resource.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The creation time of the
            resource.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last update time of the
            resource.
        document_type (google.cloud.commerceproducer_v1beta.types.PrivateOfferDocument.DocumentType):
            Required. The classification type of the
            document. Used to distinguish between different
            types of documents that may be attached to a
            private offer for different business purposes.
        mime_type (str):
            Optional. The MIME type of the document.
            Used to distinguish between different document
            formats. Supported formats (which may be
            expanded in the future)

            - 'application/pdf'
    """

    class DocumentType(proto.Enum):
        r"""Supported types of documents.
        Additional document types may be added in future. Further
        editions of the Google Cloud Marketplace Standard EULA may be
        published in future, which may result in changes to the subset
        of Standard EULA versions permitted to be used in new offers.

        Values:
            DOCUMENT_TYPE_UNSPECIFIED (0):
                The default / unset value. Do not use.
            CUSTOM_END_USER_LICENSE_AGREEMENT (1):
                The document is a custom EULA used in place of the standard
                product EULA. A private offer may not have more than one
                custom EULA document, and may not have both a custom EULA
                and a standard EULA.

                If this enum value is set, then mime_type and inline_content
                must be set.
            STATEMENT_OF_WORK (2):
                The document is the statement of work described by the
                `Cloud Marketplace Product Specific
                Terms <https://cloud.google.com/terms/marketplace-product-terms>`__.
                A private offer may not have more than one statement of work
                document.

                Whether this document type is required, optional, or not
                permitted depends on the service; see
                ``Service.document_requirement``.

                The mime_type and inline_content fields must be set.
            STANDARD_END_USER_LICENSE_AGREEMENT_V1 (3):
                The document is the Marketplace standard EULA, with the
                following link:
                https://cloud.google.com/terms/marketplace/eula-standard-v1-12102020.

                This edition has been superseded by
                STANDARD_END_USER_LICENSE_AGREEMENT_V2. Offers created
                before that edition was published may have this document
                type, but it is not permitted on any service for new offers.
            STANDARD_END_USER_LICENSE_AGREEMENT_V2 (4):
                The document is the Marketplace standard EULA, with the
                following link:
                https://cloud.google.com/terms/marketplace/eula-standard-v2-01272021

                New offers using Standard EULAs should set this enum value.
                A private offer may not have more than one standard EULA
                document, and may not have both a standard EULA and a custom
                EULA.

                Whether this document type is required, optional, or not
                permitted depends on the service; see
                ``Service.document_requirement``.

                The mime_type and inline_content fields must not be set.
        """

        DOCUMENT_TYPE_UNSPECIFIED = 0
        CUSTOM_END_USER_LICENSE_AGREEMENT = 1
        STATEMENT_OF_WORK = 2
        STANDARD_END_USER_LICENSE_AGREEMENT_V1 = 3
        STANDARD_END_USER_LICENSE_AGREEMENT_V2 = 4

    inline_content: bytes = proto.Field(
        proto.BYTES,
        number=6,
        oneof="content",
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
    document_type: DocumentType = proto.Field(
        proto.ENUM,
        number=4,
        enum=DocumentType,
    )
    mime_type: str = proto.Field(
        proto.STRING,
        number=5,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
