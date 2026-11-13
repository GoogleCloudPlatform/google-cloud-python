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

from google.ads.admanager_v1.types import audience_segment_enums, targeting

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "AudienceSegment",
    },
)


class AudienceSegment(proto.Message):
    r"""The ``AudienceSegment`` resource.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        non_rule_based_first_party_audience_segment (google.ads.admanager_v1.types.AudienceSegment.NonRuleBasedFirstPartyAudienceSegment):
            Optional. An ``AudienceSegment`` owned by the publisher
            network that does not contain a rule. Cookies are usually
            added to these segments through cookie upload.

            This field is a member of `oneof`_ ``sub_type``.
        rule_based_first_party_audience_segment (google.ads.admanager_v1.types.AudienceSegment.RuleBasedFirstPartyAudienceSegment):
            Optional. An ``AudienceSegment`` owned by the publisher
            network that contains a rule.

            This field is a member of `oneof`_ ``sub_type``.
        third_party_audience_segment (google.ads.admanager_v1.types.AudienceSegment.ThirdPartyAudienceSegment):
            Output only. An ``AudienceSegment`` owned by a data provider
            and licensed to the Ad Manager publisher network.

            This field is a member of `oneof`_ ``sub_type``.
        name (str):
            Identifier. The resource name of the ``AudienceSegment``.
            Format:
            ``networks/{network_code}/audienceSegments/{audience_segment_id}``
            The ``audience_segment_id`` is not always numerical and may
            have one of the following suffixes:

            - ``~direct`` for directly licensed third-party segments
            - ``~global`` for globally licensed third-party segments
        shared_id (int):
            Output only. The ID of the ``AudienceSegment``. Up to two
            resources may share this ID.
        display_name (str):
            Required. Display name of the ``AudienceSegment``. The
            attribute has a maximum length of 255 characters.

            This field is a member of `oneof`_ ``_display_name``.
        category_ids (MutableSequence[int]):
            Optional. Unordered list. IDs of the categories that this
            audience segment belongs to. See ``segment_categories`` for
            additional information about the categories.
        description (str):
            Optional. Description of the ``AudienceSegment``. This has a
            maximum length of 8192 characters.

            This field is a member of `oneof`_ ``_description``.
        status (google.ads.admanager_v1.types.AudienceSegmentStatusEnum.AudienceSegmentStatus):
            Output only. Non-empty default. Status of the
            ``AudienceSegment`` used to determine whether the segment is
            available for targeting. Defaults to ``ACTIVE`` if not set.

            This field is a member of `oneof`_ ``_status``.
        size (int):
            Output only. Number of unique identifiers in the
            ``AudienceSegment``.

            This field is a member of `oneof`_ ``_size``.
        mobile_web_size (int):
            Output only. Number of unique mobile web identifiers in the
            ``AudienceSegment``.

            This field is a member of `oneof`_ ``_mobile_web_size``.
        idfa_size (int):
            Output only. Number of unique Identifier for Advertisers
            (IDFA) identifiers in the ``AudienceSegment``.

            This field is a member of `oneof`_ ``_idfa_size``.
        ad_id_size (int):
            Output only. Number of unique AdID identifiers in the
            ``AudienceSegment``.

            This field is a member of `oneof`_ ``_ad_id_size``.
        ppid_size (int):
            Output only. Number of unique publisher-provided (PPID)
            identifiers in the ``AudienceSegment``.

            This field is a member of `oneof`_ ``_ppid_size``.
        data_provider_display_name (str):
            Output only. Display name of the owner data
            provider. For a first-party audience segment,
            this is the display name of the publisher
            network. Otherwise, this is the display name of
            the entity providing the audience segment.

            This field is a member of `oneof`_ ``_data_provider_display_name``.
        segment_type (google.ads.admanager_v1.types.AudienceSegmentTypeEnum.AudienceSegmentType):
            Output only. Non-empty default. Type of the
            ``AudienceSegment``. Every ``AudienceSegment`` is either
            ``FIRST_PARTY`` or ``THIRD_PARTY``.

            This field is a member of `oneof`_ ``_segment_type``.
    """

    class NonRuleBasedFirstPartyAudienceSegment(proto.Message):
        r"""An ``AudienceSegment`` owned by the publisher network that does not
        contain a rule. Cookies are usually added to these segments through
        cookie upload.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            membership_expiration_days (int):
                Required. Number of days after which a user's cookie will be
                removed from the ``AudienceSegment`` due to inactivity. The
                field can be between 1 and 540.

                This field is a member of `oneof`_ ``_membership_expiration_days``.
        """

        membership_expiration_days: int = proto.Field(
            proto.INT64,
            number=1,
            optional=True,
        )

    class RuleBasedFirstPartyAudienceSegment(proto.Message):
        r"""An ``AudienceSegment`` owned by the publisher network that contains
        a rule.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            page_views (int):
                Required. Number of times a user's cookie must match the
                ``rule`` before it's associated with the
                ``AudienceSegment``. This is used with ``recency_days`` to
                determine eligibility of the association. This attribute is
                between 1 and 12.

                This field is a member of `oneof`_ ``_page_views``.
            recency_days (int):
                Optional. Number of days within which a user's cookie must
                match the ``rule`` before it's associated with the
                ``AudienceSegment``. This is used with ``page_views`` to
                determine eligibility of the association. This attribute is
                required if ``page_views`` is greater than 1. When set, it
                can be between 1 and 30.

                This field is a member of `oneof`_ ``_recency_days``.
            membership_expiration_days (int):
                Required. Number of days after which a user's cookie will be
                removed from the ``AudienceSegment`` due to inactivity. The
                field can be between 1 and 540.

                This field is a member of `oneof`_ ``_membership_expiration_days``.
            rule (google.ads.admanager_v1.types.AudienceSegment.Rule):
                Required. The rule definition which determines the
                eligibility criteria for the ``AudienceSegment``.
        """

        page_views: int = proto.Field(
            proto.INT64,
            number=1,
            optional=True,
        )
        recency_days: int = proto.Field(
            proto.INT64,
            number=2,
            optional=True,
        )
        membership_expiration_days: int = proto.Field(
            proto.INT64,
            number=3,
            optional=True,
        )
        rule: "AudienceSegment.Rule" = proto.Field(
            proto.MESSAGE,
            number=4,
            message="AudienceSegment.Rule",
        )

    class ThirdPartyAudienceSegment(proto.Message):
        r"""An ``AudienceSegment`` owned by a data provider and licensed to the
        Ad Manager publisher network.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            approval_status (google.ads.admanager_v1.types.AudienceSegmentApprovalStatusEnum.AudienceSegmentApprovalStatus):
                Output only. Whether the publisher has
                approved or rejected the segment.

                This field is a member of `oneof`_ ``_approval_status``.
            cost (google.type.money_pb2.Money):
                Output only. The CPM cost for the given
                segment. This is assigned by the data provider.
                The CPM cost comes from the active pricing if it
                exists, otherwise it comes from the latest
                pricing.
            license_type (google.ads.admanager_v1.types.AudienceSegmentLicenseTypeEnum.AudienceSegmentLicenseType):
                Output only. The license type of the external
                segment.

                This field is a member of `oneof`_ ``_license_type``.
            start_time (google.protobuf.timestamp_pb2.Timestamp):
                Output only. Time which this segment becomes
                available for use. It is assigned by the data
                provider.
            end_time (google.protobuf.timestamp_pb2.Timestamp):
                Output only. Time which this segment ceases
                to be available. It is assigned by the data
                provider.
        """

        approval_status: audience_segment_enums.AudienceSegmentApprovalStatusEnum.AudienceSegmentApprovalStatus = proto.Field(
            proto.ENUM,
            number=1,
            optional=True,
            enum=audience_segment_enums.AudienceSegmentApprovalStatusEnum.AudienceSegmentApprovalStatus,
        )
        cost: money_pb2.Money = proto.Field(
            proto.MESSAGE,
            number=2,
            message=money_pb2.Money,
        )
        license_type: audience_segment_enums.AudienceSegmentLicenseTypeEnum.AudienceSegmentLicenseType = proto.Field(
            proto.ENUM,
            number=3,
            optional=True,
            enum=audience_segment_enums.AudienceSegmentLicenseTypeEnum.AudienceSegmentLicenseType,
        )
        start_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=4,
            message=timestamp_pb2.Timestamp,
        )
        end_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=5,
            message=timestamp_pb2.Timestamp,
        )

    class Rule(proto.Message):
        r"""Eligibility criteria for a user to be part of an
        ``AudienceSegment``.

        Attributes:
            inventory_targeting (google.ads.admanager_v1.types.InventoryTargeting):
                Required. Specification of inventory (i.e. ad
                units and placements) that are part of the rule
                of the RuleBasedFirstPartyAudienceSegment.
            custom_targeting (google.ads.admanager_v1.types.CustomTargeting):
                Optional. Specification of custom criteria that are part of
                the rule of the RuleBasedFirstPartyAudienceSegment. Once
                specified, the server may return a normalized but equivalent
                representation of the rule. There are up to 3 levels of
                custom criteria allowed. See
                [CustomTargeting][google.ads.admanager.v1.CustomTargeting]
                and its sub-messages for limitations.
        """

        inventory_targeting: targeting.InventoryTargeting = proto.Field(
            proto.MESSAGE,
            number=1,
            message=targeting.InventoryTargeting,
        )
        custom_targeting: targeting.CustomTargeting = proto.Field(
            proto.MESSAGE,
            number=2,
            message=targeting.CustomTargeting,
        )

    non_rule_based_first_party_audience_segment: NonRuleBasedFirstPartyAudienceSegment = proto.Field(
        proto.MESSAGE,
        number=13,
        oneof="sub_type",
        message=NonRuleBasedFirstPartyAudienceSegment,
    )
    rule_based_first_party_audience_segment: RuleBasedFirstPartyAudienceSegment = (
        proto.Field(
            proto.MESSAGE,
            number=14,
            oneof="sub_type",
            message=RuleBasedFirstPartyAudienceSegment,
        )
    )
    third_party_audience_segment: ThirdPartyAudienceSegment = proto.Field(
        proto.MESSAGE,
        number=16,
        oneof="sub_type",
        message=ThirdPartyAudienceSegment,
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    shared_id: int = proto.Field(
        proto.INT64,
        number=17,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    category_ids: MutableSequence[int] = proto.RepeatedField(
        proto.INT64,
        number=3,
    )
    description: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )
    status: audience_segment_enums.AudienceSegmentStatusEnum.AudienceSegmentStatus = (
        proto.Field(
            proto.ENUM,
            number=5,
            optional=True,
            enum=audience_segment_enums.AudienceSegmentStatusEnum.AudienceSegmentStatus,
        )
    )
    size: int = proto.Field(
        proto.INT64,
        number=6,
        optional=True,
    )
    mobile_web_size: int = proto.Field(
        proto.INT64,
        number=7,
        optional=True,
    )
    idfa_size: int = proto.Field(
        proto.INT64,
        number=8,
        optional=True,
    )
    ad_id_size: int = proto.Field(
        proto.INT64,
        number=9,
        optional=True,
    )
    ppid_size: int = proto.Field(
        proto.INT64,
        number=10,
        optional=True,
    )
    data_provider_display_name: str = proto.Field(
        proto.STRING,
        number=11,
        optional=True,
    )
    segment_type: audience_segment_enums.AudienceSegmentTypeEnum.AudienceSegmentType = (
        proto.Field(
            proto.ENUM,
            number=12,
            optional=True,
            enum=audience_segment_enums.AudienceSegmentTypeEnum.AudienceSegmentType,
        )
    )


__all__ = tuple(sorted(__protobuf__.manifest))
