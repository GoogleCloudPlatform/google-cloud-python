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
    package="google.ads.admanager.v1",
    manifest={
        "StitchingTypeEnum",
        "ReportingTypeEnum",
        "AdResponseTypeEnum",
        "BreakTypeEnum",
        "PrefetchStageTypeEnum",
        "CreativeIdTypeEnum",
        "SessionFindingSeverityEnum",
        "PodFindingTypeEnum",
        "SlateFindingTypeEnum",
        "AdBreakFindingTypeEnum",
        "TrackingPingFindingTypeEnum",
        "CreativeFindingTypeEnum",
        "AdRequestFindingTypeEnum",
    },
)


class StitchingTypeEnum(proto.Message):
    r"""Wrapper message for
    [StitchingType][google.ads.admanager.v1.StitchingTypeEnum.StitchingType]

    """

    class StitchingType(proto.Enum):
        r"""Indicates how ads are stitched into the session.

        Values:
            STITCHING_TYPE_UNSPECIFIED (0):
                Default value.
            STITCHED (1):
                DAI stitches ad pods into the session.
            POD_SERVING (2):
                Ready to stitch ad pods are provided by DAI
                and stitched by the publisher.
        """

        STITCHING_TYPE_UNSPECIFIED = 0
        STITCHED = 1
        POD_SERVING = 2


class ReportingTypeEnum(proto.Message):
    r"""Wrapper message for
    [ReportingType][google.ads.admanager.v1.ReportingTypeEnum.ReportingType]

    """

    class ReportingType(proto.Enum):
        r"""Indicates how ad tracking URLs are reported for the session.

        Values:
            REPORTING_TYPE_UNSPECIFIED (0):
                Default value.
            CLIENT (1):
                Tracking URLs are pinged on client side.
            SERVER (2):
                Tracking URLs are pinged on server side.
            CLIENT_INITIATED_SERVER_TRIGGERED (3):
                Tracking URLs are pinged on server side upon
                receiving ad media verification requests from
                client.
        """

        REPORTING_TYPE_UNSPECIFIED = 0
        CLIENT = 1
        SERVER = 2
        CLIENT_INITIATED_SERVER_TRIGGERED = 3


class AdResponseTypeEnum(proto.Message):
    r"""Wrapper message for
    [AdResponseType][google.ads.admanager.v1.AdResponseTypeEnum.AdResponseType]

    """

    class AdResponseType(proto.Enum):
        r"""The type of the ad response.

        Values:
            AD_RESPONSE_TYPE_UNSPECIFIED (0):
                Default value.
            VAST (1):
                The ad response is VAST (Video Ad Serving
                Template).
            VMAP (2):
                The ad response is VMAP (Video Multiple Ad
                Playlist).
        """

        AD_RESPONSE_TYPE_UNSPECIFIED = 0
        VAST = 1
        VMAP = 2


class BreakTypeEnum(proto.Message):
    r"""Wrapper message for
    [BreakType][google.ads.admanager.v1.BreakTypeEnum.BreakType]

    """

    class BreakType(proto.Enum):
        r"""Different break types that DAI supports for ad insertion.

        Values:
            BREAK_TYPE_UNSPECIFIED (0):
                Default value.
            PREROLL (1):
                Before content.
            MIDROLL (2):
                In the middle of content.
            POSTROLL (3):
                After content.
            AUXILIARY (4):
                Non-linear auxiliary ads run concurrently
                with the content (e.g., Pause Ads).
        """

        BREAK_TYPE_UNSPECIFIED = 0
        PREROLL = 1
        MIDROLL = 2
        POSTROLL = 3
        AUXILIARY = 4


class PrefetchStageTypeEnum(proto.Message):
    r"""Wrapper message for
    [PrefetchStageType][google.ads.admanager.v1.PrefetchStageTypeEnum.PrefetchStageType]

    """

    class PrefetchStageType(proto.Enum):
        r"""Indicates the prefetch stage for an ad pod.

        Values:
            PREFETCH_STAGE_TYPE_UNSPECIFIED (0):
                Default value.
            ONE (1):
                Prefetch stage 1.
            TWO (2):
                Prefetch stage 2.
            DISABLED (3):
                Prefetch is disabled for this ad pod.
        """

        PREFETCH_STAGE_TYPE_UNSPECIFIED = 0
        ONE = 1
        TWO = 2
        DISABLED = 3


class CreativeIdTypeEnum(proto.Message):
    r"""Wrapper message for
    [CreativeIdType][google.ads.admanager.v1.CreativeIdTypeEnum.CreativeIdType]

    """

    class CreativeIdType(proto.Enum):
        r"""The ID types in a VAST response to uniquely identify a
        creative.

        Values:
            CREATIVE_ID_TYPE_UNSPECIFIED (0):
                Default value.
            AD_ID (1):
                An ad server-defined ID string for the ad.
            CREATIVE_ID (2):
                An ad server-defined ID for the creative.
            CREATIVE_AD_ID (3):
                Identifies the ad with which the creative is
                served. This is an optional attribute of
                Creative element in the VAST specification.
            MEDIA_URI_HASH (4):
                A media URI was used to generate a hash
                value, hopefully unique to this creative.
            UNIVERSAL_AD_ID (5):
                Universal Ad ID of the creative as defined in the VAST 4.0
                spec:
                http://www.iab.com/wp-content/uploads/2016/04/VAST4.0_Updated_April_2016.pdf
                Section 3.7.1 The ID string format is "\|".
            MEDIA_URI_PATH (6):
                ID value is the path of the URL of the
                highest bitrate mediafile found in the response.
            CREATIVE_AD_ID_WITH_FALLBACK (8):
                ID value is the VAST/Ad/Inline/Creative ``adId`` attribute.
                If absent, the value will fallback to the
                VAST/Ad/Inline/Creative ``id`` attribute. If that is also
                absent, the value will again fallback to the VAST/Ad ``id``
                attribute.
            MEDIA_URI (9):
                ID value is the URL of the highest bitrate
                mediafile found in the response.
            CANONICALIZED_MEDIA_URI (11):
                ID value is a projection of the URL of the
                highest bitrate mediafile found in the response.
            GOOGLE_VIDEO_REGISTRY_ID (10):
                ID value is the Google Video Registry ID.
        """

        CREATIVE_ID_TYPE_UNSPECIFIED = 0
        AD_ID = 1
        CREATIVE_ID = 2
        CREATIVE_AD_ID = 3
        MEDIA_URI_HASH = 4
        UNIVERSAL_AD_ID = 5
        MEDIA_URI_PATH = 6
        CREATIVE_AD_ID_WITH_FALLBACK = 8
        MEDIA_URI = 9
        CANONICALIZED_MEDIA_URI = 11
        GOOGLE_VIDEO_REGISTRY_ID = 10


class SessionFindingSeverityEnum(proto.Message):
    r"""Wrapper message for
    [SessionFindingSeverity][google.ads.admanager.v1.SessionFindingSeverityEnum.SessionFindingSeverity]

    """

    class SessionFindingSeverity(proto.Enum):
        r"""Severity levels for a finding.

        Values:
            SESSION_FINDING_SEVERITY_UNSPECIFIED (0):
                Default value.
            INFO (1):
                The finding is informational.
            WARNING (2):
                The finding is a warning.
            ERROR (3):
                The finding is an error.
        """

        SESSION_FINDING_SEVERITY_UNSPECIFIED = 0
        INFO = 1
        WARNING = 2
        ERROR = 3


class PodFindingTypeEnum(proto.Message):
    r"""Wrapper message for
    [PodFindingType][google.ads.admanager.v1.PodFindingTypeEnum.PodFindingType]

    """

    class PodFindingType(proto.Enum):
        r"""Types of findings that can occur while decisioning an ad pod.

        Values:
            POD_FINDING_TYPE_UNSPECIFIED (0):
                Default value.
            INTERNAL_ERROR (1):
                Internal DAI error.
            AD_POD_DROPPED_EMPTY_ADS (2):
                Ad pod doesn't contain ad(s) available for
                insertion.
            AD_POD_DROPPED_INCOMPATIBLE_TIMEOFFSET (3):
                Ad pod was dropped because the request is
                incompatible with the time offset returned by
                the VMAP.
            AD_POD_DROPPED_UNSUPPORTED_TYPE (4):
                Ad pod was dropped because it was an
                unsupported type for this session.
        """

        POD_FINDING_TYPE_UNSPECIFIED = 0
        INTERNAL_ERROR = 1
        AD_POD_DROPPED_EMPTY_ADS = 2
        AD_POD_DROPPED_INCOMPATIBLE_TIMEOFFSET = 3
        AD_POD_DROPPED_UNSUPPORTED_TYPE = 4


class SlateFindingTypeEnum(proto.Message):
    r"""Wrapper message for
    [SlateFindingType][google.ads.admanager.v1.SlateFindingTypeEnum.SlateFindingType]

    """

    class SlateFindingType(proto.Enum):
        r"""A finding that occurred regarding the slate creative.

        Values:
            SLATE_FINDING_TYPE_UNSPECIFIED (0):
                Default value.
            INTERNAL_ERROR (1):
                Internal DAI error.
            SLATE_STATUS_SKIPPED (2):
                Slate was skipped for this ad break and
                underlying content was stitched instead because
                slate was disabled for underfill or empty break.
            SLATE_STATUS_DROPPED_UNKNOWN (3):
                Slate was not inserted into this ad break due
                to an unknown reason.
            SLATE_STATUS_MINIMUM_INSERTED (4):
                The minimum amount of slate was inserted into
                an underfilled ad break to cover the gap between
                the end of the ads and the next segment start of
                the trimmed underlying linear content.
        """

        SLATE_FINDING_TYPE_UNSPECIFIED = 0
        INTERNAL_ERROR = 1
        SLATE_STATUS_SKIPPED = 2
        SLATE_STATUS_DROPPED_UNKNOWN = 3
        SLATE_STATUS_MINIMUM_INSERTED = 4


class AdBreakFindingTypeEnum(proto.Message):
    r"""Wrapper message for
    [AdBreakFindingType][google.ads.admanager.v1.AdBreakFindingTypeEnum.AdBreakFindingType]

    """

    class AdBreakFindingType(proto.Enum):
        r"""A finding that occurred while serving an ad break for a
        session.

        Values:
            AD_BREAK_FINDING_TYPE_UNSPECIFIED (0):
                Default value.
            INTERNAL_ERROR (1):
                Internal DAI error.
            AD_POD_DROPPED_TOO_MANY_AD_PODS (2):
                Ad pod was dropped, the number of ad breaks
                is less than the number of decisioned ad pods.
            EXCEEDS_MAX_FILLER (3):
                Ad pod doesn't contain enough ads - requires
                more filler than specified.
            ADS_STATUS_DROPPED_FOR_PREROLL (4):
                The midroll ad break was skipped due to
                overlapping with preroll.
            ADS_STATUS_ALL_ADS_MISSING_ASSETS (5):
                Ad pod was dropped due to all of the ads in
                the pod missing their assets, probably due to
                the assets not yet being transcoded.
            ADS_STATUS_OUT_OF_WINDOW (6):
                Ad pod is outside of the window at session
                creation time so ad pod was skipped and
                underlying content was stitched instead.
            ADS_STATUS_DISABLED (7):
                Ads are disabled for this session.
            ADS_STATUS_STORAGE_ERROR (8):
                Decisioned ad pod couldn't be fetched from
                storage.
            ADS_STATUS_EXPIRED (9):
                Ad pod expired because the ad request
                couldn't finish before the deadline.
            ADS_STATUS_HOLIDAY (10):
                Ad pod occurred within the configured ad
                holiday.
            ADS_STATUS_DROPPED_SLATE_UNAVAILABLE (11):
                Ad pod was dropped because slate was
                unavailable and underlying content was stitched
                instead.
            ADS_STATUS_NO_ADS_AVAILABLE_BEFORE_DEADLINE (12):
                Ad pod was dropped because there were no ads
                available before the deadline.
            ADS_STATUS_INVALID_POD_REQUEST (13):
                Ad pod was dropped due to an invalid pod
                request.
            ADS_STATUS_DROPPED_FOR_MIDROLL (14):
                The requested pre-roll break would overlap
                with a mid-roll ad break.
            ADS_STATUS_DROPPED_BREAK_DURATION_TOO_SHORT (15):
                The duration of the ad break was too short to
                request ads.
            ADS_STATUS_DROPPED_STREAM_CREATED_AFTER_BREAK (16):
                Session created after the ad break ended.
            ADS_STATUS_DROPPED_MEDIA_ANALYSIS_UNAVAILABLE (17):
                Information about the content stream that is
                required to stitch the ads is missing or
                unavailable.
            ADS_STATUS_UNKNOWN (18):
                The serving or insertion status of the ad
                break is unknown.
            UNSERVED_BREAK (19):
                Ad break was not served.
            PREROLL_AUDIO_VIDEO_MISALIGNMENT (20):
                The content segment boundary at the end of
                the preroll has misaligned video and audio
                segments.
        """

        AD_BREAK_FINDING_TYPE_UNSPECIFIED = 0
        INTERNAL_ERROR = 1
        AD_POD_DROPPED_TOO_MANY_AD_PODS = 2
        EXCEEDS_MAX_FILLER = 3
        ADS_STATUS_DROPPED_FOR_PREROLL = 4
        ADS_STATUS_ALL_ADS_MISSING_ASSETS = 5
        ADS_STATUS_OUT_OF_WINDOW = 6
        ADS_STATUS_DISABLED = 7
        ADS_STATUS_STORAGE_ERROR = 8
        ADS_STATUS_EXPIRED = 9
        ADS_STATUS_HOLIDAY = 10
        ADS_STATUS_DROPPED_SLATE_UNAVAILABLE = 11
        ADS_STATUS_NO_ADS_AVAILABLE_BEFORE_DEADLINE = 12
        ADS_STATUS_INVALID_POD_REQUEST = 13
        ADS_STATUS_DROPPED_FOR_MIDROLL = 14
        ADS_STATUS_DROPPED_BREAK_DURATION_TOO_SHORT = 15
        ADS_STATUS_DROPPED_STREAM_CREATED_AFTER_BREAK = 16
        ADS_STATUS_DROPPED_MEDIA_ANALYSIS_UNAVAILABLE = 17
        ADS_STATUS_UNKNOWN = 18
        UNSERVED_BREAK = 19
        PREROLL_AUDIO_VIDEO_MISALIGNMENT = 20


class TrackingPingFindingTypeEnum(proto.Message):
    r"""Wrapper message for
    [TrackingPingFindingType][google.ads.admanager.v1.TrackingPingFindingTypeEnum.TrackingPingFindingType]

    """

    class TrackingPingFindingType(proto.Enum):
        r"""A finding that occurred while pinging tracking URLs for a
        session.

        Values:
            TRACKING_PING_FINDING_TYPE_UNSPECIFIED (0):
                Default value.
            INTERNAL_ERROR (1):
                Internal DAI error.
            FAILED_PING (2):
                Failed to ping a URL.
        """

        TRACKING_PING_FINDING_TYPE_UNSPECIFIED = 0
        INTERNAL_ERROR = 1
        FAILED_PING = 2


class CreativeFindingTypeEnum(proto.Message):
    r"""Wrapper message for
    [CreativeFindingType][google.ads.admanager.v1.CreativeFindingTypeEnum.CreativeFindingType]

    """

    class CreativeFindingType(proto.Enum):
        r"""A finding that occurred while looking up creative
        information.

        Values:
            CREATIVE_FINDING_TYPE_UNSPECIFIED (0):
                Default value.
            UNIDENTIFIED_AD_CREATIVE (1):
                Ad was dropped because the VAST document
                returned did not contain enough information to
                successfully identify the creative media.
            UNKNOWN_AD_CREATIVE (2):
                Ad was dropped because the system has no
                knowledge of the creative media to insert into
                the DAI session. Creative will be reactively
                loaded into the system for subsequent use.
            AD_CREATIVE_LOOKUP_FAILED (3):
                Error occurred when performing lookup on the
                ad creative for insertion into the DAI session.
            DISABLED_AD_CREATIVE (4):
                Creative has been disabled from serving.
            FAILED_AD_CREATIVE (5):
                Ad creative is known but failed to acquire /
                transcode for serving.
            AD_CREATIVE_ENCODING_MATCH_FAILURE (6):
                Ad creative does not have suitable encodings
                available to be successfully stitched into a DAI
                session.
            MISMATCHED_FRAME_COUNT (7):
                Incorrect number of frames available for
                creative when exact frame count is required for
                a specific duration.
            MISSING_TRANSCODES (8):
                Ad creative doesn't have any encodings
                available.
            AD_DROPPED_TO_FIT_BREAK (9):
                Ad creative is dropped due to pod trimming to
                fit the break.
        """

        CREATIVE_FINDING_TYPE_UNSPECIFIED = 0
        UNIDENTIFIED_AD_CREATIVE = 1
        UNKNOWN_AD_CREATIVE = 2
        AD_CREATIVE_LOOKUP_FAILED = 3
        DISABLED_AD_CREATIVE = 4
        FAILED_AD_CREATIVE = 5
        AD_CREATIVE_ENCODING_MATCH_FAILURE = 6
        MISMATCHED_FRAME_COUNT = 7
        MISSING_TRANSCODES = 8
        AD_DROPPED_TO_FIT_BREAK = 9


class AdRequestFindingTypeEnum(proto.Message):
    r"""Wrapper message for
    [AdRequestFindingType][google.ads.admanager.v1.AdRequestFindingTypeEnum.AdRequestFindingType]

    """

    class AdRequestFindingType(proto.Enum):
        r"""A finding that occurred while making an ad request.

        Values:
            AD_REQUEST_FINDING_TYPE_UNSPECIFIED (0):
                Default value.
            INTERNAL_ERROR (1):
                Internal DAI error.
            AD_REQUEST_ERROR (2):
                An error while making an ad request.
            VAST_PARSE_ERROR (3):
                Generic VAST parsing error.
            UNSUPPORTED_AD_SYSTEM (4):
                AdSystem reported in VAST is not supported.
            CANNOT_FIND_UNIQUE_TRANSCODE_ID (5):
                Ad element does not contain enough
                information to generate a unique transcode ID.
            MISSING_INLINE_ELEMENTS (7):
                No InLine elements found in the Ad.
            MAX_WRAPPER_DEPTH_REACHED (8):
                Reached the maximum number of VAST redirects.
            AD_TAG_PARSE_ERROR (9):
                Error while parsing ad tag.
            VMAP_PARSE_ERROR (10):
                Generic VMAP parsing error.
            INVALID_VMAP_RESPONSE (11):
                Invalid VMAP data (Able to parse VMAP but XML
                attributes have invalid data).
            NO_AD_BREAKS_IN_VMAP (12):
                VMAP response contains no ad breaks.
            CUSTOM_AD_SOURCE_IN_VMAP (13):
                VMAP contains custom ad source which is not
                supported.
            AD_BREAK_TYPE_NOT_SUPPORTED (14):
                VMAP contains an adbreak that is not
                supported.
            NEITHER_AD_SOURCE_NOR_TRACKING (15):
                VMAP contains an adbreak that has neither ad
                source nor tracking events.
            SKIPPABLE_AD_NOT_SUPPORTED (16):
                Client doesn't support skippable ads. The ad
                was a skippable ad.
            AD_REQUEST_TIMEOUT (17):
                The request has timed out.
            DUPLICATE_AD_TAG (18):
                The same ad tag was already used in the same
                pod.
            FOLLOW_REDIRECTS_IS_FALSE (19):
                VMAP AdSource followRedirects is set as
                false.
            UNSUPPORTED_VAST_VERSION (20):
                VAST version is not supported.
            NO_VALID_MEDIAFILES_FOUND (21):
                No media files were found in the VAST ad.
        """

        AD_REQUEST_FINDING_TYPE_UNSPECIFIED = 0
        INTERNAL_ERROR = 1
        AD_REQUEST_ERROR = 2
        VAST_PARSE_ERROR = 3
        UNSUPPORTED_AD_SYSTEM = 4
        CANNOT_FIND_UNIQUE_TRANSCODE_ID = 5
        MISSING_INLINE_ELEMENTS = 7
        MAX_WRAPPER_DEPTH_REACHED = 8
        AD_TAG_PARSE_ERROR = 9
        VMAP_PARSE_ERROR = 10
        INVALID_VMAP_RESPONSE = 11
        NO_AD_BREAKS_IN_VMAP = 12
        CUSTOM_AD_SOURCE_IN_VMAP = 13
        AD_BREAK_TYPE_NOT_SUPPORTED = 14
        NEITHER_AD_SOURCE_NOR_TRACKING = 15
        SKIPPABLE_AD_NOT_SUPPORTED = 16
        AD_REQUEST_TIMEOUT = 17
        DUPLICATE_AD_TAG = 18
        FOLLOW_REDIRECTS_IS_FALSE = 19
        UNSUPPORTED_VAST_VERSION = 20
        NO_VALID_MEDIAFILES_FOUND = 21


__all__ = tuple(sorted(__protobuf__.manifest))
