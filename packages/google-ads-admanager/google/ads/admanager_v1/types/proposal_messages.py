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
import google.type.money_pb2 as money_pb2  # type: ignore
import proto  # type: ignore

from google.ads.admanager_v1.types import (
    applied_label,
    creative_placeholder,
    custom_field_value,
    proposal_enums,
    proposal_environment_type_enum,
    proposal_negotiation_status_enum,
    supply_path_type_enum,
)
from google.ads.admanager_v1.types import targeting as gaa_targeting

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "Proposal",
        "BuyerRfp",
        "ProposalCompanyAssociation",
        "ProposalMarketplaceInfo",
        "MarketplaceComment",
    },
)


class Proposal(proto.Message):
    r"""A Proposal represents an agreement between an interactive
    advertising seller and a buyer that specifies the details of an
    advertising campaign.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the Proposal. Format:
            ``networks/{network_code}/proposals/{proposal_id}``
        order (str):
            Output only. The resource name of the corresponding Order.
            This will not be set if the Proposal has not been pushed to
            Ad Manager. Format:
            ``networks/{network_code}/orders/{order_id}``

            This field is a member of `oneof`_ ``_order``.
        display_name (str):
            Required. The display name of the Proposal. This value has a
            maximum length of 255 characters. This value is copied to
            [Order.displayName][google.ads.admanager.v1.Order.display_name]
            when the proposal turns into an order.

            This field is a member of `oneof`_ ``_display_name``.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which the
            [Order][google.ads.admanager.v1.Order] and
            [LineItems][google.ads.admanager.v1.LineItem] associated
            with the Proposal are eligible to begin serving. This
            attribute is derived from the [ProposalLineItem][] with the
            earliest [startTime][ProposalLineItem.start_time]. This
            attribute will be empty if this Proposal has no associated
            [ProposalLineItems][ProposalLineItem] or if none of its
            [ProposalLineItems][ProposalLineItem] have a start time.

            This field is a member of `oneof`_ ``_start_time``.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which the
            [Order][google.ads.admanager.v1.Order] and
            [LineItems][google.ads.admanager.v1.LineItem] associated
            with the Proposal stop serving. This attribute is derived
            from the [ProposalLineItem][] with the latest
            [endTime][ProposalLineItem.end_time]. This attribute will be
            empty if this Proposal has no associated
            [ProposalLineItems][ProposalLineItem] or if none of its
            [ProposalLineItems][ProposalLineItem] have an end time.

            This field is a member of `oneof`_ ``_end_time``.
        archived (bool):
            Output only. Whether the Proposal is archived
            or not.

            This field is a member of `oneof`_ ``_archived``.
        advertiser (str):
            Required. The resource name of the
            [Company][google.ads.admanager.v1.Company] of type
            [ADVERTISER][google.ads.admanager.v1.CompanyTypeEnum.CompanyType.ADVERTISER]
            to which this Proposal belongs. This attribute is required
            when the proposal turns into an order, and will be copied to
            [Order.advertiser][google.ads.admanager.v1.Order.advertiser].
            This attribute becomes read-only once the Proposal has been
            pushed. Format:
            ``networks/{network_code}/companies/{company_id}``

            This field is a member of `oneof`_ ``_advertiser``.
        agencies (MutableSequence[google.ads.admanager_v1.types.ProposalCompanyAssociation]):
            Optional. List of agencies and the set of
            [Contacts][google.ads.admanager.v1.Contact] associated with
            each agency. A Proposal can have at most one
            [Company][google.ads.admanager.v1.Company] with
            [PRIMARY_AGENCY][google.ads.admanager.v1.ProposalCompanyAssociationTypeEnum.ProposalCompanyAssociationType.PRIMARY_AGENCY]
            type, but a [Company][google.ads.admanager.v1.Company] can
            appear more than once with different
            [ProposalCompanyAssociationType][google.ads.admanager.v1.ProposalCompanyAssociationTypeEnum.ProposalCompanyAssociationType]
            values. If a primary agency exists, its
            [ProposalCompanyAssociation.company][google.ads.admanager.v1.ProposalCompanyAssociation.company]
            will be copied to
            [Order.agency][google.ads.admanager.v1.Order.agency] when
            the proposal turns into an order.
        notes (str):
            Optional. Provides any additional notes that
            may annotate the Proposal. This attribute has a
            maximum length of 65,535 characters.

            This field is a member of `oneof`_ ``_notes``.
        primary_salesperson (str):
            Optional. The resource name of the
            [User][google.ads.admanager.v1.User] representing the
            primary salesperson who brokered the transaction with the
            [advertiser][google.ads.admanager.v1.Proposal.advertiser].
            This attribute is required when the proposal turns into an
            order. Format: ``networks/{network_code}/users/{user_id}``

            This field is a member of `oneof`_ ``_primary_salesperson``.
        sales_planner_users (MutableSequence[str]):
            Optional. The resource names of the
            [Users][google.ads.admanager.v1.User] representing the sales
            planners of the Proposal. A Proposal can have at most 8
            sales planners. Format:
            ``networks/{network_code}/users/{user_id}``
        trafficker (str):
            Optional. The resource name of the
            [User][google.ads.admanager.v1.User] who is the primary
            trafficker and is responsible for trafficking the Proposal.
            This attribute is required when the proposal turns into an
            order, and will be copied to
            [Order.trafficker][google.ads.admanager.v1.Order.trafficker].
            Format: ``networks/{network_code}/users/{user_id}``

            This field is a member of `oneof`_ ``_trafficker``.
        seller_contact_users (MutableSequence[str]):
            Optional. The resource names of the
            [Users][google.ads.admanager.v1.User] who are the seller's
            contacts. Format:
            ``networks/{network_code}/users/{user_id}``
        applied_teams (MutableSequence[str]):
            Optional. The resource names of the teams directly applied
            to the Proposal. Format:
            ``networks/{network_code}/teams/{team_id}``
        custom_field_values (MutableSequence[google.ads.admanager_v1.types.CustomFieldValue]):
            Optional. The values of the custom fields
            associated with the Proposal.
        applied_labels (MutableSequence[google.ads.admanager_v1.types.AppliedLabel]):
            Optional. The set of labels applied directly
            to the Proposal.
        effective_applied_labels (MutableSequence[google.ads.admanager_v1.types.AppliedLabel]):
            Output only. The set of labels applied to the
            Proposal including inherited values. Only labels
            that directly affect the entity are listed here.
            If they are negated, only the negated version is
            visible.
        currency_code (str):
            Optional. The currency code of this Proposal.
            If not directly set, the currency code will be
            the network's currency code.
        sold (bool):
            Output only. Indicates whether the proposal has been sold,
            i.e., corresponds to whether the status of an Order is
            [APPROVED][google.ads.admanager.v1.OrderStatusEnum.OrderStatus.APPROVED]
            or
            [PAUSED][google.ads.admanager.v1.OrderStatusEnum.OrderStatus.PAUSED].

            This field is a member of `oneof`_ ``_sold``.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time this Proposal was last
            modified.

            This field is a member of `oneof`_ ``_update_time``.
        marketplace_info (google.ads.admanager_v1.types.ProposalMarketplaceInfo):
            Optional. The marketplace info of this
            Proposal if it has a corresponding Order in
            Marketplace.
        buyer_rfp (google.ads.admanager_v1.types.BuyerRfp):
            Output only. The buyer RFP associated with
            this Proposal. This field will be unset if the
            proposal is not initiated from an RFP.
        delivery_pausing_enabled (bool):
            Optional. Non-empty default. Whether delivery of the
            Proposal can be paused. Defaults to ``true``. If ``false``,
            the buyer and the seller agree that the Proposal should not
            be paused.

            This field is a member of `oneof`_ ``_delivery_pausing_enabled``.
        supply_path (google.ads.admanager_v1.types.SupplyPathTypeEnum.SupplyPathType):
            Optional. Non-empty default. The supply path type of this
            Proposal. If no value is provided on creation, defaults to
            [DEMAND_SIDE_PLATFORM][google.ads.admanager.v1.SupplyPathTypeEnum.SupplyPathType.DEMAND_SIDE_PLATFORM].

            This field is a member of `oneof`_ ``_supply_path``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    order: str = proto.Field(
        proto.STRING,
        number=41,
        optional=True,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=5,
        optional=True,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        optional=True,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        optional=True,
        message=timestamp_pb2.Timestamp,
    )
    archived: bool = proto.Field(
        proto.BOOL,
        number=50,
        optional=True,
    )
    advertiser: str = proto.Field(
        proto.STRING,
        number=57,
        optional=True,
    )
    agencies: MutableSequence["ProposalCompanyAssociation"] = proto.RepeatedField(
        proto.MESSAGE,
        number=11,
        message="ProposalCompanyAssociation",
    )
    notes: str = proto.Field(
        proto.STRING,
        number=12,
        optional=True,
    )
    primary_salesperson: str = proto.Field(
        proto.STRING,
        number=14,
        optional=True,
    )
    sales_planner_users: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=16,
    )
    trafficker: str = proto.Field(
        proto.STRING,
        number=18,
        optional=True,
    )
    seller_contact_users: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=20,
    )
    applied_teams: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=24,
    )
    custom_field_values: MutableSequence[custom_field_value.CustomFieldValue] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=25,
            message=custom_field_value.CustomFieldValue,
        )
    )
    applied_labels: MutableSequence[applied_label.AppliedLabel] = proto.RepeatedField(
        proto.MESSAGE,
        number=26,
        message=applied_label.AppliedLabel,
    )
    effective_applied_labels: MutableSequence[applied_label.AppliedLabel] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=27,
            message=applied_label.AppliedLabel,
        )
    )
    currency_code: str = proto.Field(
        proto.STRING,
        number=29,
    )
    sold: bool = proto.Field(
        proto.BOOL,
        number=30,
        optional=True,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=34,
        optional=True,
        message=timestamp_pb2.Timestamp,
    )
    marketplace_info: "ProposalMarketplaceInfo" = proto.Field(
        proto.MESSAGE,
        number=36,
        message="ProposalMarketplaceInfo",
    )
    buyer_rfp: "BuyerRfp" = proto.Field(
        proto.MESSAGE,
        number=38,
        message="BuyerRfp",
    )
    delivery_pausing_enabled: bool = proto.Field(
        proto.BOOL,
        number=40,
        optional=True,
    )
    supply_path: supply_path_type_enum.SupplyPathTypeEnum.SupplyPathType = proto.Field(
        proto.ENUM,
        number=42,
        optional=True,
        enum=supply_path_type_enum.SupplyPathTypeEnum.SupplyPathType,
    )


class BuyerRfp(proto.Message):
    r"""Represents the buyer RFP information associated with a
    Proposal describing the requirements from the buyer.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        cost_per_unit (google.type.money_pb2.Money):
            Output only. CPM for the Proposal in question. Given that
            this field belongs to a request for proposal (for which
            initially a Proposal does not yet exist), this field should
            serve as guidance for publishers to create a Proposal with
            [LineItems][google.ads.admanager.v1.LineItem] reflecting
            this CPM.
        units (int):
            Output only. The number of impressions per
            day that a buyer wishes to see in the Proposal
            derived from the request for proposal in
            question.

            This field is a member of `oneof`_ ``_units``.
        budget (google.type.money_pb2.Money):
            Output only. Total amount of money available
            to spend on this deal. In the case of a
            Preferred Deal, the budget is equal to the
            maximum amount of money a buyer is willing to
            spend on a given Proposal, even though the
            budget might not be spent entirely, as
            impressions are not guaranteed.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which the proposed
            deal should start serving.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which the proposed
            deal should end serving.
        description (str):
            Output only. A description of the proposed
            deal. This can be used for the buyer to tell the
            publisher more detailed information about the
            deal in question.

            This field is a member of `oneof`_ ``_description``.
        creative_placeholders (MutableSequence[google.ads.admanager_v1.types.CreativePlaceholder]):
            Output only. A list of inventory sizes in
            which creatives will eventually be served.
        targeting (google.ads.admanager_v1.types.Targeting):
            Output only. Targeting information for the
            proposal in question. Currently this field only
            contains GeoTargeting information.
        additional_terms (str):
            Output only. Additional terms of the deal in
            question. This field can be used to state more
            specific targeting information for the deal, as
            well as any additional information regarding
            this deal. Given that this field belongs to a
            request for proposal (for which initially a
            Proposal does not yet exist), this field can be
            populated by buyers to specify additional
            information that they wish publishers to
            incorporate into the Proposal derived from this
            request for proposal.

            This field is a member of `oneof`_ ``_additional_terms``.
        ad_exchange_environment (google.ads.admanager_v1.types.ProposalEnvironmentTypeEnum.ProposalEnvironmentType):
            Output only. Identifies the format of the inventory or
            "channel" through which the ad serves. Environments
            currently supported include
            [DISPLAY][google.ads.admanager.v1.ProposalEnvironmentTypeEnum.ProposalEnvironmentType.DISPLAY],
            [VIDEO][google.ads.admanager.v1.ProposalEnvironmentTypeEnum.ProposalEnvironmentType.VIDEO],
            and
            [MOBILE][google.ads.admanager.v1.ProposalEnvironmentTypeEnum.ProposalEnvironmentType.MOBILE].

            This field is a member of `oneof`_ ``_ad_exchange_environment``.
        rfp_type (google.ads.admanager_v1.types.BuyerRfpTypeEnum.BuyerRfpType):
            Output only. Deal type; either Programmatic
            Guaranteed or Preferred Deal. This field
            corresponds to the type of Proposal that a buyer
            wishes to negotiate with a seller.

            This field is a member of `oneof`_ ``_rfp_type``.
    """

    cost_per_unit: money_pb2.Money = proto.Field(
        proto.MESSAGE,
        number=1,
        message=money_pb2.Money,
    )
    units: int = proto.Field(
        proto.INT64,
        number=2,
        optional=True,
    )
    budget: money_pb2.Money = proto.Field(
        proto.MESSAGE,
        number=3,
        message=money_pb2.Money,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    description: str = proto.Field(
        proto.STRING,
        number=9,
        optional=True,
    )
    creative_placeholders: MutableSequence[creative_placeholder.CreativePlaceholder] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=10,
            message=creative_placeholder.CreativePlaceholder,
        )
    )
    targeting: gaa_targeting.Targeting = proto.Field(
        proto.MESSAGE,
        number=11,
        message=gaa_targeting.Targeting,
    )
    additional_terms: str = proto.Field(
        proto.STRING,
        number=12,
        optional=True,
    )
    ad_exchange_environment: proposal_environment_type_enum.ProposalEnvironmentTypeEnum.ProposalEnvironmentType = proto.Field(
        proto.ENUM,
        number=13,
        optional=True,
        enum=proposal_environment_type_enum.ProposalEnvironmentTypeEnum.ProposalEnvironmentType,
    )
    rfp_type: proposal_enums.BuyerRfpTypeEnum.BuyerRfpType = proto.Field(
        proto.ENUM,
        number=14,
        optional=True,
        enum=proposal_enums.BuyerRfpTypeEnum.BuyerRfpType,
    )


class ProposalCompanyAssociation(proto.Message):
    r"""A ProposalCompanyAssociation represents a
    [Company][google.ads.admanager.v1.Company] associated with the
    Proposal and a set of [Contacts][google.ads.admanager.v1.Contact]
    belonging to the company.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        company (str):
            Required. The resource name of the
            [Company][google.ads.admanager.v1.Company] associated with
            the Proposal. Format:
            ``networks/{network_code}/companies/{company_id}``

            This field is a member of `oneof`_ ``_company``.
        type_ (google.ads.admanager_v1.types.ProposalCompanyAssociationTypeEnum.ProposalCompanyAssociationType):
            Required. The association type between the
            [Company][google.ads.admanager.v1.Company] and the Proposal.

            This field is a member of `oneof`_ ``_type``.
        seller_contacts (MutableSequence[str]):
            Optional. The resource names of the
            [Contacts][google.ads.admanager.v1.Contact] associated with
            the [Company][google.ads.admanager.v1.Company]. Format:
            ``networks/{network_code}/contacts/{contact_id}``
    """

    company: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    type_: proposal_enums.ProposalCompanyAssociationTypeEnum.ProposalCompanyAssociationType = proto.Field(
        proto.ENUM,
        number=3,
        optional=True,
        enum=proposal_enums.ProposalCompanyAssociationTypeEnum.ProposalCompanyAssociationType,
    )
    seller_contacts: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )


class ProposalMarketplaceInfo(proto.Message):
    r"""Marketplace info for a Proposal with a corresponding order in
    Marketplace.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        marketplace_order_id (str):
            Output only. The marketplace ID of this
            Proposal. This is a shared ID between Ad Manager
            and the buy-side platform. This value is null if
            the Proposal has not been sent to the buyer.

            This field is a member of `oneof`_ ``_marketplace_order_id``.
        draft_proposal (bool):
            Output only. Whether the non-free-editable fields of a
            Proposal are opened for edit. A Proposal that is open for
            edit will not receive buyer updates from Marketplace. If the
            buyer updates the Proposal while this is open for local
            editing, Google will set
            [newVersionFromBuyer][google.ads.admanager.v1.ProposalMarketplaceInfo.new_version_from_buyer]
            to ``true``. You will then need to call
            [ProposalService.BatchDiscardDraftProposals][google.ads.admanager.v1.ProposalService.BatchDiscardDraftProposals]
            to revert your edits to get the buyer's latest changes.

            This field is a member of `oneof`_ ``_draft_proposal``.
        negotiation_status (google.ads.admanager_v1.types.ProposalNegotiationStatusEnum.ProposalNegotiationStatus):
            Output only. The negotiation status of the
            Proposal.

            This field is a member of `oneof`_ ``_negotiation_status``.
        marketplace_comment (str):
            Optional. The comment on the Proposal to be
            sent to the buyer.

            This field is a member of `oneof`_ ``_marketplace_comment``.
        new_version_from_buyer (bool):
            Output only. Indicates that the buyer has made updates to
            the Proposal on Marketplace. This attribute is only
            meaningful if the Proposal is open for edit (i.e.,
            [draftProposal][google.ads.admanager.v1.ProposalMarketplaceInfo.draft_proposal]
            is ``true``).

            This field is a member of `oneof`_ ``_new_version_from_buyer``.
        buyer_account_id (int):
            Required. The account ID of the buyer that
            this Proposal is being negotiated with.

            This field is a member of `oneof`_ ``_buyer_account_id``.
        partner_client_id (str):
            Output only. The ID used to represent the
            Display & Video 360 client buyer partner ID (if
            Display & Video 360) or the Authorized Buyers
            client buyer account ID.

            This field is a member of `oneof`_ ``_partner_client_id``.
    """

    marketplace_order_id: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    draft_proposal: bool = proto.Field(
        proto.BOOL,
        number=3,
        optional=True,
    )
    negotiation_status: proposal_negotiation_status_enum.ProposalNegotiationStatusEnum.ProposalNegotiationStatus = proto.Field(
        proto.ENUM,
        number=4,
        optional=True,
        enum=proposal_negotiation_status_enum.ProposalNegotiationStatusEnum.ProposalNegotiationStatus,
    )
    marketplace_comment: str = proto.Field(
        proto.STRING,
        number=5,
        optional=True,
    )
    new_version_from_buyer: bool = proto.Field(
        proto.BOOL,
        number=7,
        optional=True,
    )
    buyer_account_id: int = proto.Field(
        proto.INT64,
        number=9,
        optional=True,
    )
    partner_client_id: str = proto.Field(
        proto.STRING,
        number=10,
        optional=True,
    )


class MarketplaceComment(proto.Message):
    r"""Comment associated with a programmatic Proposal that has been
    sent to Marketplace.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        proposal (str):
            Output only. The resource name of the ``Proposal`` the
            comment belongs to. Format:
            ``networks/{network_code}/proposals/{proposal}``

            This field is a member of `oneof`_ ``_proposal``.
        comment (str):
            Output only. The comment made on the
            Proposal.

            This field is a member of `oneof`_ ``_comment``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which the comment
            was created.
        commenter_role (google.ads.admanager_v1.types.MarketplaceComment.CommenterRole):
            Output only. The role of the user who created
            the comment.

            This field is a member of `oneof`_ ``_commenter_role``.
    """

    class CommenterRole(proto.Enum):
        r"""Role of the user who created the comment.

        Values:
            COMMENTER_ROLE_UNSPECIFIED (0):
                Default value. This value is unused.
            BUYER (1):
                The comment was created by the buyer.
            SELLER (2):
                The comment was created by the seller.
        """

        COMMENTER_ROLE_UNSPECIFIED = 0
        BUYER = 1
        SELLER = 2

    proposal: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    comment: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    commenter_role: CommenterRole = proto.Field(
        proto.ENUM,
        number=4,
        optional=True,
        enum=CommenterRole,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
