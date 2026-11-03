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

import google.rpc.status_pb2 as status_pb2  # type: ignore
import google.type.interval_pb2 as interval_pb2  # type: ignore
import proto  # type: ignore

from google.ads.admanager_v1.types import (
    ad_review_center_ad_enums,
    ad_review_center_ad_messages,
)

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "SearchAdReviewCenterAdsRequest",
        "SearchAdReviewCenterAdsResponse",
        "BatchAllowAdReviewCenterAdsRequest",
        "BatchAllowAdReviewCenterAdsResponse",
        "BatchBlockAdReviewCenterAdsRequest",
        "BatchBlockAdReviewCenterAdsResponse",
        "BatchAdReviewCenterAdsOperationMetadata",
        "FetchAdReviewCenterCustomLabelsRequest",
        "FetchAdReviewCenterCustomLabelsResponse",
        "BatchApplyAdReviewCenterCustomLabelsRequest",
        "BatchApplyAdReviewCenterCustomLabelsResponse",
    },
)


class SearchAdReviewCenterAdsRequest(proto.Message):
    r"""Request object for ``SearchAdReviewCenterAds`` method.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        status (google.ads.admanager_v1.types.AdReviewCenterAdStatusEnum.AdReviewCenterAdStatus):
            Optional. Only return ads with the given status. Use this
            filter for web properties where `Manual Creative Review
            (MCR) <https://support.google.com/admanager/answer/2913553>`__
            is not enabled.

            This field is a member of `oneof`_ ``ad_review_status``.
        manual_review_status (google.ads.admanager_v1.types.ManualAdReviewCenterAdStatusEnum.ManualAdReviewCenterAdStatus):
            Optional. Only return ads with the given manual review
            status. Use this filter for web properties where `Manual
            Creative Review
            (MCR) <https://support.google.com/admanager/answer/2913553>`__
            is enabled.

            This field is a member of `oneof`_ ``ad_review_status``.
        parent (str):
            Required. The parent, which owns this collection of
            AdReviewCenterAds. Format:
            networks/{network_code}/webProperties/{web_property_code}

            Since a network can only have a single web property of each
            ``ExchangeSyndicationProduct``, you can use the
            ``ExchangeSyndicationProduct`` as an alias for the web
            property code:

            ``networks/{network_code}/webProperties/display``

            ``networks/{network_code}/webProperties/videoAndAudio``

            ``networks/{network_code}/webProperties/mobileApp``

            ``networks/{network_code}/webProperties/games``
        page_size (int):
            Optional. The maximum number of
            AdReviewCenterAds to return. The service may
            return fewer than this value. If unspecified, at
            most 50 AdReviewCenterAds will be returned. The
            maximum value is 1000; values greater than 1000
            will be coerced to 1000.
        page_token (str):
            Optional. The page token to fetch the next
            page of AdReviewCenterAds. This is the value
            returned from a previous Search request, or
            empty.
        ad_review_center_ad_id (MutableSequence[str]):
            Optional. Only return ads with the given
            AdReviewCenterAd IDs. If provided, no other
            filter can be set (other than page size and page
            token).
        date_time_range (google.type.interval_pb2.Interval):
            Optional. If provided, only return ads that
            served within the given date range (inclusive).
            The date range must be within the last 30 days.
            If not provided, the date range will be the last
            30 days.
        search_text (MutableSequence[str]):
            Optional. If provided, restrict the search to
            AdReviewCenterAds associated with the text (including any
            text on the ad or in the destination URL). If more than one
            value is provided, the search will combine them in a logical
            AND. For example, ['car', 'blue'] will match ads that
            contain both "car" and "blue", but not an ad that only
            contains "car".
        buyer_account_id (MutableSequence[int]):
            Optional. If provided, restrict the search to creatives
            belonging to one of the given Adx buyer account IDs. Only
            applicable to RTB creatives. Adx buyer account IDs can be
            found using the ``ProgrammaticBuyerService``.
        ad_response_id (MutableSequence[str]):
            Optional. If provided, only return ads with
            the given ad response IDs. This filter is
            exclusive and cannot be combined with any other
            filters. Maximum of 10 IDs can be specified.
        advertiser_display_names (MutableSequence[str]):
            Optional. If provided, restrict the search to
            creatives with the given advertiser names.
        language_codes (MutableSequence[str]):
            Optional. If provided, restrict the search to
            creatives serving in the given language codes.
        region_codes (MutableSequence[str]):
            Optional. If provided, restrict the search to
            creatives serving in the given region codes.
        ad_types (MutableSequence[google.ads.admanager_v1.types.ArcCreativeFormatEnum.ArcCreativeFormat]):
            Optional. If provided, restrict the search to
            creatives with the given ad types.
        advertiser_apps (MutableSequence[str]):
            Optional. If provided, restrict the search to
            creatives promoting the given app.
        publisher_domains (MutableSequence[str]):
            Optional. If provided, restrict the search to
            creatives belonging to the given publisher
            domain.
        new_in_last_days (int):
            Optional. If provided, restrict the search to
            creatives which appeared for the first time
            within the past X days. Must be within the last
            30 days (1 to 30, inclusive).

            This field is a member of `oneof`_ ``_new_in_last_days``.
        label_ids (MutableSequence[str]):
            Optional. If provided, restrict the search to
            creatives associated with the given custom label
            IDs.
    """

    status: ad_review_center_ad_enums.AdReviewCenterAdStatusEnum.AdReviewCenterAdStatus = proto.Field(
        proto.ENUM,
        number=4,
        oneof="ad_review_status",
        enum=ad_review_center_ad_enums.AdReviewCenterAdStatusEnum.AdReviewCenterAdStatus,
    )
    manual_review_status: ad_review_center_ad_enums.ManualAdReviewCenterAdStatusEnum.ManualAdReviewCenterAdStatus = proto.Field(
        proto.ENUM,
        number=9,
        oneof="ad_review_status",
        enum=ad_review_center_ad_enums.ManualAdReviewCenterAdStatusEnum.ManualAdReviewCenterAdStatus,
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
    ad_review_center_ad_id: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    date_time_range: interval_pb2.Interval = proto.Field(
        proto.MESSAGE,
        number=6,
        message=interval_pb2.Interval,
    )
    search_text: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )
    buyer_account_id: MutableSequence[int] = proto.RepeatedField(
        proto.INT64,
        number=8,
    )
    ad_response_id: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=10,
    )
    advertiser_display_names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=11,
    )
    language_codes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=12,
    )
    region_codes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=13,
    )
    ad_types: MutableSequence[
        ad_review_center_ad_enums.ArcCreativeFormatEnum.ArcCreativeFormat
    ] = proto.RepeatedField(
        proto.ENUM,
        number=14,
        enum=ad_review_center_ad_enums.ArcCreativeFormatEnum.ArcCreativeFormat,
    )
    advertiser_apps: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=15,
    )
    publisher_domains: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=16,
    )
    new_in_last_days: int = proto.Field(
        proto.INT32,
        number=17,
        optional=True,
    )
    label_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=18,
    )


class SearchAdReviewCenterAdsResponse(proto.Message):
    r"""Response object for ``SearchAdReviewCenterAds`` method.

    Attributes:
        ad_review_center_ads (MutableSequence[google.ads.admanager_v1.types.AdReviewCenterAd]):
            The AdReviewCenterAds that match the search
            request.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    ad_review_center_ads: MutableSequence[
        ad_review_center_ad_messages.AdReviewCenterAd
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=ad_review_center_ad_messages.AdReviewCenterAd,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class BatchAllowAdReviewCenterAdsRequest(proto.Message):
    r"""Request object for ``BatchAllowAdReviewCenterAds`` method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of
            AdReviewCenterAds. Format:
            networks/{network_code}/webProperties/{web_property_code}

            Since a network can only have a single web property of each
            ``ExchangeSyndicationProduct``, you can use the
            ``ExchangeSyndicationProduct`` as an alias for the web
            property code:

            ``networks/{network_code}/webProperties/display``

            ``networks/{network_code}/webProperties/videoAndAudio``

            ``networks/{network_code}/webProperties/mobileApp``

            ``networks/{network_code}/webProperties/games``
        names (MutableSequence[str]):
            Required. The resource names of the ``AdReviewCenterAd``\ s
            to allow. Format:
            ``networks/{network_code}/webProperties/{web_property_code}/adReviewCenterAds/{ad_review_center_ad_id}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchAllowAdReviewCenterAdsResponse(proto.Message):
    r"""Response object for ``BatchAllowAdReviewCenterAds`` method."""


class BatchBlockAdReviewCenterAdsRequest(proto.Message):
    r"""Request object for ``BatchBlockAdReviewCenterAds`` method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of
            AdReviewCenterAds. Format:
            networks/{network_code}/webProperties/{web_property_code}

            Since a network can only have a single web property of each
            ``ExchangeSyndicationProduct``, you can use the
            ``ExchangeSyndicationProduct`` as an alias for the web
            property code:

            ``networks/{network_code}/webProperties/display``

            ``networks/{network_code}/webProperties/videoAndAudio``

            ``networks/{network_code}/webProperties/mobileApp``

            ``networks/{network_code}/webProperties/games``
        names (MutableSequence[str]):
            Required. The resource names of the ``AdReviewCenterAd``\ s
            to block. Format:
            ``networks/{network_code}/webProperties/{web_property_code}/adReviewCenterAds/{ad_review_center_ad_id}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchBlockAdReviewCenterAdsResponse(proto.Message):
    r"""Response object for ``BatchBlockAdReviewCenterAds`` method."""


class BatchAdReviewCenterAdsOperationMetadata(proto.Message):
    r"""Metadata object for ``BatchAllowAdReviewCenterAds`` and
    ``BatchBlockAdReviewCenterAds`` methods.

    Attributes:
        failed_requests (MutableMapping[int, google.rpc.status_pb2.Status]):
            The status of each failed request, keyed by
            the index of the corresponding request in the
            batch request.
    """

    failed_requests: MutableMapping[int, status_pb2.Status] = proto.MapField(
        proto.INT32,
        proto.MESSAGE,
        number=1,
        message=status_pb2.Status,
    )


class FetchAdReviewCenterCustomLabelsRequest(proto.Message):
    r"""Request object for ``FetchAdReviewCenterCustomLabels`` method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of
            AdReviewCenterAds custom labels. Format:
            networks/{network_code}/webProperties/{web_property_code}

            Since a network can only have a single web property of each
            ``ExchangeSyndicationProduct``, you can use the
            ``ExchangeSyndicationProduct`` as an alias for the web
            property code:

            ``networks/{network_code}/webProperties/display``

            ``networks/{network_code}/webProperties/videoAndAudio``

            ``networks/{network_code}/webProperties/mobileApp``

            ``networks/{network_code}/webProperties/games``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )


class FetchAdReviewCenterCustomLabelsResponse(proto.Message):
    r"""Response object for ``FetchAdReviewCenterCustomLabels`` method.

    Attributes:
        custom_labels (MutableSequence[google.ads.admanager_v1.types.FetchAdReviewCenterCustomLabelsResponse.CustomLabel]):
            Output only. The list of custom labels.
    """

    class CustomLabel(proto.Message):
        r"""A custom label for an Ad Review Center ad. Custom labels can
        help you filter and find creatives with the associated label.
        For more information, see
        https://support.google.com/admanager/answer/13812863.

        Attributes:
            label_id (str):
                Output only. The unique identifier of the
                custom label.
            display_name (str):
                Output only. The user-defined display name of
                the custom label.
        """

        label_id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        display_name: str = proto.Field(
            proto.STRING,
            number=2,
        )

    custom_labels: MutableSequence[CustomLabel] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=CustomLabel,
    )


class BatchApplyAdReviewCenterCustomLabelsRequest(proto.Message):
    r"""Request object for ``BatchApplyAdReviewCenterCustomLabels`` method.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of
            AdReviewCenterAds. Format:
            networks/{network_code}/webProperties/{web_property_code}

            Since a network can only have a single web property of each
            ``ExchangeSyndicationProduct``, you can use the
            ``ExchangeSyndicationProduct`` as an alias for the web
            property code:

            ``networks/{network_code}/webProperties/display``

            ``networks/{network_code}/webProperties/videoAndAudio``

            ``networks/{network_code}/webProperties/mobileApp``

            ``networks/{network_code}/webProperties/games``
        add_labels (google.ads.admanager_v1.types.BatchApplyAdReviewCenterCustomLabelsRequest.BatchLabelAction):
            Optional. Labels to add to the specified ads.

            This field is a member of `oneof`_ ``_add_labels``.
        remove_labels (google.ads.admanager_v1.types.BatchApplyAdReviewCenterCustomLabelsRequest.BatchLabelAction):
            Optional. Labels to remove from the specified
            ads.

            This field is a member of `oneof`_ ``_remove_labels``.
    """

    class BatchLabelAction(proto.Message):
        r"""Actions to perform on custom labels for batch updates.

        Attributes:
            names (MutableSequence[str]):
                Required. The resource names of the ``AdReviewCenterAd``\ s
                to update. Format:
                ``networks/{network_code}/webProperties/{web_property_code}/adReviewCenterAds/{ad_review_center_ad_id}``
            label_ids (MutableSequence[str]):
                Required. The
                [labelId][google.ads.admanager.v1.FetchAdReviewCenterCustomLabelsResponse.CustomLabel.label_id]
                to add or remove.
        """

        names: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )
        label_ids: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    add_labels: BatchLabelAction = proto.Field(
        proto.MESSAGE,
        number=2,
        optional=True,
        message=BatchLabelAction,
    )
    remove_labels: BatchLabelAction = proto.Field(
        proto.MESSAGE,
        number=3,
        optional=True,
        message=BatchLabelAction,
    )


class BatchApplyAdReviewCenterCustomLabelsResponse(proto.Message):
    r"""Response object for ``BatchApplyAdReviewCenterCustomLabels`` method."""


__all__ = tuple(sorted(__protobuf__.manifest))
