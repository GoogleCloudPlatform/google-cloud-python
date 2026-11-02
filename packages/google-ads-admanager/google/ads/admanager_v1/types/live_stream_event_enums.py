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
        "SlateStatusEnum",
        "LiveStreamEventStatusEnum",
        "AdBreakMarkupTypeEnum",
        "LiveStreamEventStreamingFormatEnum",
        "DynamicAdInsertionTypeEnum",
        "HlsSettingsPlaylistTypeEnum",
        "HlsMasterPlaylistRefreshTypeEnum",
        "AdBreakFillTypeEnum",
    },
)


class SlateStatusEnum(proto.Message):
    r"""Wrapper message for
    [SlateStatus][google.ads.admanager.v1.SlateStatusEnum.SlateStatus]

    """

    class SlateStatus(proto.Enum):
        r"""Describes the status of a Slate object.

        Values:
            SLATE_STATUS_UNSPECIFIED (0):
                Default value. This value is unused.
            ACTIVE (1):
                Indicates the Slate has been created and is
                eligible for streaming.
            ARCHIVED (2):
                Indicates the Slate has been archived.
        """

        SLATE_STATUS_UNSPECIFIED = 0
        ACTIVE = 1
        ARCHIVED = 2


class LiveStreamEventStatusEnum(proto.Message):
    r"""Wrapper message for
    [LiveStreamEventStatus][google.ads.admanager.v1.LiveStreamEventStatusEnum.LiveStreamEventStatus]

    """

    class LiveStreamEventStatus(proto.Enum):
        r"""Describes the status of a LiveStreamEvent object.

        Values:
            LIVE_STREAM_EVENT_STATUS_UNSPECIFIED (0):
                Default value. This value is unused.
            ACTIVE (1):
                Indicates the LiveStreamEvent has been
                created and is eligible for streaming.
            ADS_PAUSED (2):
                Indicates that the stream is still being
                served, but ad insertion should be paused
                temporarily.
            ARCHIVED (3):
                Indicates the LiveStreamEvent has been
                archived.
            PAUSED (4):
                Indicates the LiveStreamEvent has been
                paused. This can be made #ACTIVE at later time.
        """

        LIVE_STREAM_EVENT_STATUS_UNSPECIFIED = 0
        ACTIVE = 1
        ADS_PAUSED = 2
        ARCHIVED = 3
        PAUSED = 4


class AdBreakMarkupTypeEnum(proto.Message):
    r"""Wrapper message for
    [AdBreakMarkupType][google.ads.admanager.v1.AdBreakMarkupTypeEnum.AdBreakMarkupType]

    """

    class AdBreakMarkupType(proto.Enum):
        r"""Describes the SCTE ad break markups for a LiveStreamEvent.

        Values:
            AD_BREAK_MARKUP_TYPE_UNSPECIFIED (0):
                Default value. This value is unused.
            HLS_DATERANGE_SPLICE (1):
                The DATERANGE ad break marker type. This mark
                up type is only applicable for HLS live streams.
            HLS_EXT_CUE (2):
                The CUE-OUT/CUE-IN ad break marker type. This
                mark up type is only applicable for HLS live
                streams.
            HLS_PRIMETIME_SPLICE (3):
                The CUE (Adobe/Azure Prime Time) ad break
                marker type. This mark up type is only
                applicable for HLS live streams.
            SCTE35_BINARY_BREAK_START_END (4):
                The SCTE35 Binary Time Signal: Break
                Start/End ad break marker type. This mark up
                type is only applicable for HLS and DASH live
                streams.
            SCTE35_BINARY_PROVIDER_AD_START_END (5):
                The SCTE35 Binary Time Signal: Provider Ad
                Start/End ad break marker type. This mark up
                type is only applicable for HLS and DASH live
                streams.
            SCTE35_BINARY_PROVIDER_PLACEMENT_OP_START_END (6):
                The SCTE35 Binary Time Signal: Provider
                Placement Opportunity Start/End ad break marker
                type. This mark up type is only applicable for
                HLS and DASH live streams.
            SCTE35_BINARY_SPLICE_INSERT (7):
                The SCTE35 Binary Splice Insert ad break
                marker type. This mark up type is only
                applicable for HLS and DASH live streams.
            SCTE35_XML_SPLICE_INSERT (11):
                The SCTE35 XML Splice In/Out ad break marker
                type. This markup type is only applicable for
                DASH live streams.
        """

        AD_BREAK_MARKUP_TYPE_UNSPECIFIED = 0
        HLS_DATERANGE_SPLICE = 1
        HLS_EXT_CUE = 2
        HLS_PRIMETIME_SPLICE = 3
        SCTE35_BINARY_BREAK_START_END = 4
        SCTE35_BINARY_PROVIDER_AD_START_END = 5
        SCTE35_BINARY_PROVIDER_PLACEMENT_OP_START_END = 6
        SCTE35_BINARY_SPLICE_INSERT = 7
        SCTE35_XML_SPLICE_INSERT = 11


class LiveStreamEventStreamingFormatEnum(proto.Message):
    r"""Wrapper message for
    [LiveStreamEventStreamingFormat][google.ads.admanager.v1.LiveStreamEventStreamingFormatEnum.LiveStreamEventStreamingFormat]

    """

    class LiveStreamEventStreamingFormat(proto.Enum):
        r"""The LiveStreamEvent streaming format.

        Values:
            LIVE_STREAM_EVENT_STREAMING_FORMAT_UNSPECIFIED (0):
                Default value. This value is unused.
            DASH (1):
                The format of the live stream media is
                MPEG-DASH.
            HLS (2):
                The format of the live stream media is HTTP
                Live Streaming.
        """

        LIVE_STREAM_EVENT_STREAMING_FORMAT_UNSPECIFIED = 0
        DASH = 1
        HLS = 2


class DynamicAdInsertionTypeEnum(proto.Message):
    r"""Wrapper message for
    [DynamicAdInsertionType][google.ads.admanager.v1.DynamicAdInsertionTypeEnum.DynamicAdInsertionType]

    """

    class DynamicAdInsertionType(proto.Enum):
        r"""Describes how the live stream will have ads dynamically
        inserted into playlists.

        Values:
            DYNAMIC_AD_INSERTION_TYPE_UNSPECIFIED (0):
                Default value. This value is unused.
            LINEAR (1):
                Content manifest is served by Google DAI.
                Content and ads are stitched together into a
                unique video manifest per user.
            POD_SERVING_MANIFEST (2):
                Ads manifest is served by Google DAI,
                containing unique ad pod segments for the video
                player to switch to from the content stream, or
                for the partner to stitch directly into the user
                content manifest.
            POD_SERVING_REDIRECT (3):
                Content manifest is served by the partner,
                embedding Google DAI ad segment URLs which
                redirect to unique Google DAI ad segments per
                user.
        """

        DYNAMIC_AD_INSERTION_TYPE_UNSPECIFIED = 0
        LINEAR = 1
        POD_SERVING_MANIFEST = 2
        POD_SERVING_REDIRECT = 3


class HlsSettingsPlaylistTypeEnum(proto.Message):
    r"""Wrapper message for
    [HlsSettingsPlaylistType][google.ads.admanager.v1.HlsSettingsPlaylistTypeEnum.HlsSettingsPlaylistType]

    """

    class HlsSettingsPlaylistType(proto.Enum):
        r"""Describes the type of the playlist associated with this live
        stream. This is analogous to the EXT-X-PLAYLIST-TYPE HLS tag.
        Use HlsSettingsPlaylistType.EVENT for streams with the value
        "#EXT-X-PLAYLIST-TYPE:EVENT" and use
        HlsSettingsPlaylistType.LIVE for streams without the tag.

        Values:
            HLS_SETTINGS_PLAYLIST_TYPE_UNSPECIFIED (0):
                Default value. This value is unused.
            EVENT (1):
                The playlist is an event, which means that
                media segments can only be added to the end of
                the playlist. This allows viewers to scrub back
                to the beginning of the playlist.
            LIVE (2):
                The playlist is a live stream and there are
                no restrictions on whether media segments can be
                removed from the beginning of the playlist.
        """

        HLS_SETTINGS_PLAYLIST_TYPE_UNSPECIFIED = 0
        EVENT = 1
        LIVE = 2


class HlsMasterPlaylistRefreshTypeEnum(proto.Message):
    r"""Wrapper message for
    [HlsMasterPlaylistRefreshType][google.ads.admanager.v1.HlsMasterPlaylistRefreshTypeEnum.HlsMasterPlaylistRefreshType]

    """

    class HlsMasterPlaylistRefreshType(proto.Enum):
        r"""Enumerates the different ways an HLS master playlist on a
        live stream will can be refreshed.

        Values:
            HLS_MASTER_PLAYLIST_REFRESH_TYPE_UNSPECIFIED (0):
                Default value. This value is unused.
            AUTOMATIC (1):
                The master playlist will automatically be
                refreshed.
            MANUAL (2):
                The master playlist will only be refreshed
                when requested.
        """

        HLS_MASTER_PLAYLIST_REFRESH_TYPE_UNSPECIFIED = 0
        AUTOMATIC = 1
        MANUAL = 2


class AdBreakFillTypeEnum(proto.Message):
    r"""Wrapper message for
    [AdBreakFillType][google.ads.admanager.v1.AdBreakFillTypeEnum.AdBreakFillType]

    """

    class AdBreakFillType(proto.Enum):
        r"""Describes what should be used to fill an empty or underfilled
        ad break during a live stream.

        Values:
            AD_BREAK_FILL_TYPE_UNSPECIFIED (0):
                Default value. This value is unused.
            MINIMIZE_SLATE (1):
                Ad break should be filled with mostly
                underlying content. When ad content can't be
                aligned with underlying content during
                transition, the gap will be bridged with slate
                to maintain the timeline.
            SLATE (2):
                Ad break should be filled with slate.
            UNDERLYING_CONTENT (3):
                Ad break should be filled with underlying
                content.
        """

        AD_BREAK_FILL_TYPE_UNSPECIFIED = 0
        MINIMIZE_SLATE = 1
        SLATE = 2
        UNDERLYING_CONTENT = 3


__all__ = tuple(sorted(__protobuf__.manifest))
