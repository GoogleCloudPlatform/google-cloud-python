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

from google.ads.datamanager_v1.types import device_info as gad_device_info
from google.ads.datamanager_v1.types import user_data as gad_user_data
from google.ads.datamanager_v1.types import viewability_info as gad_viewability_info

__protobuf__ = proto.module(
    package="google.ads.datamanager.v1",
    manifest={
        "AdType",
        "AdFormat",
        "AdPlacement",
        "TargetingType",
        "PlatformType",
        "Platform",
        "AttributionHint",
        "AdEvent",
    },
)


class AdType(proto.Enum):
    r"""The type of the ad served.

    Values:
        AD_TYPE_UNSPECIFIED (0):
            Unspecified ad type.
        AD_TYPE_DISPLAY (1):
            Display ad.
        AD_TYPE_TEXT (2):
            Text ad.
        AD_TYPE_IMAGE (3):
            Image ad.
        AD_TYPE_RICH_MEDIA (4):
            Rich media ad.
        AD_TYPE_HTML (5):
            HTML ad.
        AD_TYPE_AUDIO (6):
            Audio ad.
        AD_TYPE_VIDEO (7):
            Video ad.
    """

    AD_TYPE_UNSPECIFIED = 0
    AD_TYPE_DISPLAY = 1
    AD_TYPE_TEXT = 2
    AD_TYPE_IMAGE = 3
    AD_TYPE_RICH_MEDIA = 4
    AD_TYPE_HTML = 5
    AD_TYPE_AUDIO = 6
    AD_TYPE_VIDEO = 7


class AdFormat(proto.Enum):
    r"""The format of the ad served.

    Values:
        AD_FORMAT_UNSPECIFIED (0):
            Unspecified ad format.
        AD_FORMAT_AR (1):
            AR ad.
        AD_FORMAT_AUDIO (2):
            Audio ad.
        AD_FORMAT_BANNER (3):
            Banner ad.
        AD_FORMAT_BUMPER (4):
            Bumper ad.
        AD_FORMAT_CAROUSEL (5):
            Carousel ad.
        AD_FORMAT_COLLECTION (6):
            Collection ad.
        AD_FORMAT_IMAGE (7):
            Image ad.
        AD_FORMAT_INTERACTIVE (8):
            Interactive ad.
        AD_FORMAT_INTERSTITIAL (9):
            Interstitial ad.
        AD_FORMAT_IN_FEED (10):
            In-feed ad.
        AD_FORMAT_IN_STREAM (11):
            In-stream ad.
        AD_FORMAT_IN_STREAM_SKIPPABLE (12):
            In-stream skippable ad.
        AD_FORMAT_IN_STREAM_NON_SKIPPABLE (13):
            In-stream non-skippable ad.
        AD_FORMAT_NATIVE (14):
            Native ad.
        AD_FORMAT_SHORTS (15):
            Shorts ad.
        AD_FORMAT_STORY (16):
            Story ad.
        AD_FORMAT_SPONSORED (17):
            Sponsored ad.
        AD_FORMAT_VIDEO (18):
            Video ad.
    """

    AD_FORMAT_UNSPECIFIED = 0
    AD_FORMAT_AR = 1
    AD_FORMAT_AUDIO = 2
    AD_FORMAT_BANNER = 3
    AD_FORMAT_BUMPER = 4
    AD_FORMAT_CAROUSEL = 5
    AD_FORMAT_COLLECTION = 6
    AD_FORMAT_IMAGE = 7
    AD_FORMAT_INTERACTIVE = 8
    AD_FORMAT_INTERSTITIAL = 9
    AD_FORMAT_IN_FEED = 10
    AD_FORMAT_IN_STREAM = 11
    AD_FORMAT_IN_STREAM_SKIPPABLE = 12
    AD_FORMAT_IN_STREAM_NON_SKIPPABLE = 13
    AD_FORMAT_NATIVE = 14
    AD_FORMAT_SHORTS = 15
    AD_FORMAT_STORY = 16
    AD_FORMAT_SPONSORED = 17
    AD_FORMAT_VIDEO = 18


class AdPlacement(proto.Enum):
    r"""The placement of the ad served.

    Values:
        AD_PLACEMENT_UNSPECIFIED (0):
            Unspecified ad placement.
        AD_PLACEMENT_DISCOVER (1):
            Discover placement.
        AD_PLACEMENT_FEED (2):
            Feed placement.
        AD_PLACEMENT_FOOTER (3):
            Footer placement.
        AD_PLACEMENT_HEADER (4):
            Header placement.
        AD_PLACEMENT_HOME (5):
            Home placement.
        AD_PLACEMENT_IN_CONTENT (6):
            In-content placement.
        AD_PLACEMENT_PROMOTED (7):
            Promoted placement.
        AD_PLACEMENT_SEARCH (8):
            Search placement.
        AD_PLACEMENT_STORY (9):
            Story placement.
    """

    AD_PLACEMENT_UNSPECIFIED = 0
    AD_PLACEMENT_DISCOVER = 1
    AD_PLACEMENT_FEED = 2
    AD_PLACEMENT_FOOTER = 3
    AD_PLACEMENT_HEADER = 4
    AD_PLACEMENT_HOME = 5
    AD_PLACEMENT_IN_CONTENT = 6
    AD_PLACEMENT_PROMOTED = 7
    AD_PLACEMENT_SEARCH = 8
    AD_PLACEMENT_STORY = 9


class TargetingType(proto.Enum):
    r"""The type of targeting used to serve the ad.

    Values:
        TARGETING_TYPE_UNSPECIFIED (0):
            Unspecified targeting type.
        TARGETING_TYPE_AUDIENCE (1):
            Audience targeting.
        TARGETING_TYPE_CONTEXTUAL (2):
            Contextual targeting.
        TARGETING_TYPE_DEMOGRAPHIC (3):
            Demographic targeting.
        TARGETING_TYPE_DEVICE (4):
            Device targeting.
        TARGETING_TYPE_GEO (5):
            Geo targeting.
        TARGETING_TYPE_INTEREST (6):
            Interest targeting.
        TARGETING_TYPE_PURCHASE_INTENT (7):
            Purchase intent targeting.
        TARGETING_TYPE_REMARKETING (8):
            Remarketing targeting.
    """

    TARGETING_TYPE_UNSPECIFIED = 0
    TARGETING_TYPE_AUDIENCE = 1
    TARGETING_TYPE_CONTEXTUAL = 2
    TARGETING_TYPE_DEMOGRAPHIC = 3
    TARGETING_TYPE_DEVICE = 4
    TARGETING_TYPE_GEO = 5
    TARGETING_TYPE_INTEREST = 6
    TARGETING_TYPE_PURCHASE_INTENT = 7
    TARGETING_TYPE_REMARKETING = 8


class PlatformType(proto.Enum):
    r"""The type of the platform on which the ad was served.

    Values:
        PLATFORM_TYPE_UNSPECIFIED (0):
            Unspecified platform type.
        PLATFORM_TYPE_MOBILE (1):
            Mobile platform.
        PLATFORM_TYPE_DESKTOP (2):
            Desktop platform.
        PLATFORM_TYPE_CTV (3):
            CTV platform.
        PLATFORM_TYPE_PHONE (4):
            Phone platform.
        PLATFORM_TYPE_TABLET (5):
            Tablet platform.
    """

    PLATFORM_TYPE_UNSPECIFIED = 0
    PLATFORM_TYPE_MOBILE = 1
    PLATFORM_TYPE_DESKTOP = 2
    PLATFORM_TYPE_CTV = 3
    PLATFORM_TYPE_PHONE = 4
    PLATFORM_TYPE_TABLET = 5


class Platform(proto.Enum):
    r"""Further detail of the platform on which the ad was served.

    Values:
        PLATFORM_UNSPECIFIED (0):
            Unspecified platform.
        PLATFORM_IOS (1):
            iOS platform.
        PLATFORM_ANDROID (2):
            Android platform.
        PLATFORM_WEB (3):
            Web platform.
    """

    PLATFORM_UNSPECIFIED = 0
    PLATFORM_IOS = 1
    PLATFORM_ANDROID = 2
    PLATFORM_WEB = 3


class AttributionHint(proto.Enum):
    r"""The partner-assumed attribution status for this ad event.

    Values:
        ATTRIBUTION_HINT_UNSPECIFIED (0):
            Unknown attribution status.
        ATTRIBUTION_HINT_CONVERTED (1):
            Converted status.
        ATTRIBUTION_HINT_NOT_CONVERTED (2):
            Not converted status.
    """

    ATTRIBUTION_HINT_UNSPECIFIED = 0
    ATTRIBUTION_HINT_CONVERTED = 1
    ATTRIBUTION_HINT_NOT_CONVERTED = 2


class AdEvent(proto.Message):
    r"""An ad event.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        advertiser_id (str):
            Required. The ID of the advertiser for the ad
            event.
            This must match the ID sent in the linking flow.
        event_type (google.ads.datamanager_v1.types.AdEvent.EventType):
            Required. The type of the event.
        event_subtype (google.ads.datamanager_v1.types.AdEvent.EventSubtype):
            Enum value for event subtype.

            This field is a member of `oneof`_ ``event_subtype_oneof``.
        event_subtype_string (str):
            String value for event subtype.

            This field is a member of `oneof`_ ``event_subtype_oneof``.
        timestamp (google.protobuf.timestamp_pb2.Timestamp):
            Required. The time the event occurred.
        event_id (str):
            Optional. An ID created and managed by the
            caller that uniquely identifies this event.

            Required if you want to deduplicate ad events
            that are included in multiple requests.
            Otherwise, this field is optional.
        user_data (google.ads.datamanager_v1.types.UserData):
            Optional. Multiple pieces of user-provided
            data, representing the user the event is
            associated with.

            It is possible to provide multiple instances of
            the same type of data (e.g. email address). The
            more data provided, the more likely a match will
            be found.
        device_info (google.ads.datamanager_v1.types.DeviceInfo):
            Required. Information gathered about the
            device being used when the ad event happened.
        ip_address (str):
            Optional. IP address used for measurement. This must be same
            value as
            [DeviceInfo.ip_address][google.ads.datamanager.v1.DeviceInfo.ip_address].
            Keep it blank if you do not want to share IP for
            measurement.
        mobile_device_id (str):
            Optional. The device ID of the device that
            the ad was served to.
        campaign_id (str):
            Required. The ID of the associated campaign.
        campaign_name (str):
            Required. The name of the associated
            campaign.
        ad_group_id (str):
            Optional. The ID of the associated ad group.
        ad_id (str):
            Optional. The ID of the associated ad within
            the group.
        ad_type (google.ads.datamanager_v1.types.AdType):
            Enum value for ad type.

            This field is a member of `oneof`_ ``ad_type_oneof``.
        ad_type_string (str):
            String value for ad type.

            This field is a member of `oneof`_ ``ad_type_oneof``.
        ad_format (google.ads.datamanager_v1.types.AdFormat):
            Enum value for ad format.

            This field is a member of `oneof`_ ``ad_format_oneof``.
        ad_format_string (str):
            String value for ad format.

            This field is a member of `oneof`_ ``ad_format_oneof``.
        ad_placement (google.ads.datamanager_v1.types.AdPlacement):
            Enum value for ad placement.

            This field is a member of `oneof`_ ``ad_placement_oneof``.
        ad_placement_string (str):
            String value for ad placement.

            This field is a member of `oneof`_ ``ad_placement_oneof``.
        ad_height (int):
            Optional. The height of the ad in pixels.
        ad_width (int):
            Optional. The width of the ad in pixels.
        region_code (str):
            Optional. The ISO 3166-2 country plus
            subdivision.
        source (str):
            Required. The platform source of the ad, akin
            to the Google Analytics source.
        medium (str):
            Required. The medium of the ad, akin to the
            Google Analytics medium.
        targeting_type (google.ads.datamanager_v1.types.TargetingType):
            Enum value for targeting type.

            This field is a member of `oneof`_ ``targeting_type_oneof``.
        targeting_type_string (str):
            String value for targeting type.

            This field is a member of `oneof`_ ``targeting_type_oneof``.
        platform_type (google.ads.datamanager_v1.types.PlatformType):
            Enum value for platform type.

            This field is a member of `oneof`_ ``platform_type_oneof``.
        platform_type_string (str):
            String value for platform type.

            This field is a member of `oneof`_ ``platform_type_oneof``.
        platform (google.ads.datamanager_v1.types.Platform):
            Enum value for platform.

            This field is a member of `oneof`_ ``platform_oneof``.
        platform_string (str):
            String value for platform.

            This field is a member of `oneof`_ ``platform_oneof``.
        attribution_hint (google.ads.datamanager_v1.types.AttributionHint):
            Optional. The partner-assumed attribution
            status for this ad event.
            This acts only as a signal for how the partner
            assumed attribution played out, and does not
            force an end result in final reports.
        viewability_info (google.ads.datamanager_v1.types.ViewabilityInfo):
            Required. Details of the viewability of the
            ad served.
        measurement_allowed (bool):
            Optional. Represents if the row is allowed to
            be used for measurement purposes, as governed by
            applicable privacy laws within regional
            jurisdiction.

            This field is a member of `oneof`_ ``_measurement_allowed``.
    """

    class EventType(proto.Enum):
        r"""The type of the event.

        Values:
            EVENT_TYPE_UNSPECIFIED (0):
                Unspecified event type.
            EVENT_TYPE_VIEW (1):
                View event.
            EVENT_TYPE_CLICK (2):
                Click event.
        """

        EVENT_TYPE_UNSPECIFIED = 0
        EVENT_TYPE_VIEW = 1
        EVENT_TYPE_CLICK = 2

    class EventSubtype(proto.Enum):
        r"""Additional classification about the type of ad event.

        Values:
            EVENT_SUBTYPE_UNSPECIFIED (0):
                Unspecified event subtype.
            EVENT_SUBTYPE_IMPRESSION (1):
                Impression event.
            EVENT_SUBTYPE_ENGAGED_VIEW (2):
                Engaged view event.
            EVENT_SUBTYPE_ONSITE_CLICK (3):
                Onsite click event.
            EVENT_SUBTYPE_OUTBOUND_CLICK (4):
                Outbound click event.
        """

        EVENT_SUBTYPE_UNSPECIFIED = 0
        EVENT_SUBTYPE_IMPRESSION = 1
        EVENT_SUBTYPE_ENGAGED_VIEW = 2
        EVENT_SUBTYPE_ONSITE_CLICK = 3
        EVENT_SUBTYPE_OUTBOUND_CLICK = 4

    advertiser_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    event_type: EventType = proto.Field(
        proto.ENUM,
        number=2,
        enum=EventType,
    )
    event_subtype: EventSubtype = proto.Field(
        proto.ENUM,
        number=3,
        oneof="event_subtype_oneof",
        enum=EventSubtype,
    )
    event_subtype_string: str = proto.Field(
        proto.STRING,
        number=4,
        oneof="event_subtype_oneof",
    )
    timestamp: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    event_id: str = proto.Field(
        proto.STRING,
        number=6,
    )
    user_data: gad_user_data.UserData = proto.Field(
        proto.MESSAGE,
        number=7,
        message=gad_user_data.UserData,
    )
    device_info: gad_device_info.DeviceInfo = proto.Field(
        proto.MESSAGE,
        number=8,
        message=gad_device_info.DeviceInfo,
    )
    ip_address: str = proto.Field(
        proto.STRING,
        number=34,
    )
    mobile_device_id: str = proto.Field(
        proto.STRING,
        number=9,
    )
    campaign_id: str = proto.Field(
        proto.STRING,
        number=10,
    )
    campaign_name: str = proto.Field(
        proto.STRING,
        number=11,
    )
    ad_group_id: str = proto.Field(
        proto.STRING,
        number=12,
    )
    ad_id: str = proto.Field(
        proto.STRING,
        number=13,
    )
    ad_type: "AdType" = proto.Field(
        proto.ENUM,
        number=14,
        oneof="ad_type_oneof",
        enum="AdType",
    )
    ad_type_string: str = proto.Field(
        proto.STRING,
        number=15,
        oneof="ad_type_oneof",
    )
    ad_format: "AdFormat" = proto.Field(
        proto.ENUM,
        number=16,
        oneof="ad_format_oneof",
        enum="AdFormat",
    )
    ad_format_string: str = proto.Field(
        proto.STRING,
        number=17,
        oneof="ad_format_oneof",
    )
    ad_placement: "AdPlacement" = proto.Field(
        proto.ENUM,
        number=18,
        oneof="ad_placement_oneof",
        enum="AdPlacement",
    )
    ad_placement_string: str = proto.Field(
        proto.STRING,
        number=19,
        oneof="ad_placement_oneof",
    )
    ad_height: int = proto.Field(
        proto.INT32,
        number=20,
    )
    ad_width: int = proto.Field(
        proto.INT32,
        number=21,
    )
    region_code: str = proto.Field(
        proto.STRING,
        number=22,
    )
    source: str = proto.Field(
        proto.STRING,
        number=23,
    )
    medium: str = proto.Field(
        proto.STRING,
        number=24,
    )
    targeting_type: "TargetingType" = proto.Field(
        proto.ENUM,
        number=25,
        oneof="targeting_type_oneof",
        enum="TargetingType",
    )
    targeting_type_string: str = proto.Field(
        proto.STRING,
        number=26,
        oneof="targeting_type_oneof",
    )
    platform_type: "PlatformType" = proto.Field(
        proto.ENUM,
        number=27,
        oneof="platform_type_oneof",
        enum="PlatformType",
    )
    platform_type_string: str = proto.Field(
        proto.STRING,
        number=28,
        oneof="platform_type_oneof",
    )
    platform: "Platform" = proto.Field(
        proto.ENUM,
        number=29,
        oneof="platform_oneof",
        enum="Platform",
    )
    platform_string: str = proto.Field(
        proto.STRING,
        number=30,
        oneof="platform_oneof",
    )
    attribution_hint: "AttributionHint" = proto.Field(
        proto.ENUM,
        number=31,
        enum="AttributionHint",
    )
    viewability_info: gad_viewability_info.ViewabilityInfo = proto.Field(
        proto.MESSAGE,
        number=32,
        message=gad_viewability_info.ViewabilityInfo,
    )
    measurement_allowed: bool = proto.Field(
        proto.BOOL,
        number=33,
        optional=True,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
