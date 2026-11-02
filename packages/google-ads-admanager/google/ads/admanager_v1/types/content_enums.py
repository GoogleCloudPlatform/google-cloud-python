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
        "ContentStatusEnum",
        "ContentStatusSourceEnum",
        "DaiIngestStatusEnum",
        "DaiIngestErrorReasonEnum",
    },
)


class ContentStatusEnum(proto.Message):
    r"""Wrapper message for
    [ContentStatus][google.ads.admanager.v1.ContentStatusEnum.ContentStatus]

    """

    class ContentStatus(proto.Enum):
        r"""Describes the status of a [Content][google.ads.admanager.v1.Content]
        object.

        Values:
            CONTENT_STATUS_UNSPECIFIED (0):
                Default value. This value is unused.
            ACTIVE (1):
                Indicates the ``Content`` has been created and is eligible
                to have ads served against it.
            INACTIVE (2):
                Indicates the ``Content`` has been deactivated and cannot
                have ads served against it.
            ARCHIVED (3):
                Indicates the ``Content`` has been archived; user-visible.
            DELETED (4):
                Indicates the ``Content`` has been removed from an external
                CMS.
            DUPLICATED (5):
                Indicates the ``Content`` is a duplicate of another piece of
                content.
        """

        CONTENT_STATUS_UNSPECIFIED = 0
        ACTIVE = 1
        INACTIVE = 2
        ARCHIVED = 3
        DELETED = 4
        DUPLICATED = 5


class ContentStatusSourceEnum(proto.Message):
    r"""Wrapper message for
    [ContentStatusSource][google.ads.admanager.v1.ContentStatusSourceEnum.ContentStatusSource]

    """

    class ContentStatusSource(proto.Enum):
        r"""Describes who defined the status of the
        [Content][google.ads.admanager.v1.Content] object.

        Values:
            CONTENT_STATUS_SOURCE_UNSPECIFIED (0):
                Default value. This value is unused.
            CMS (1):
                Indicates that the status of the ``Content`` is defined by
                the CMS.
            USER (2):
                Indicates that the status of the ``Content`` is defined by
                the user.
        """

        CONTENT_STATUS_SOURCE_UNSPECIFIED = 0
        CMS = 1
        USER = 2


class DaiIngestStatusEnum(proto.Message):
    r"""Wrapper message for
    [DaiIngestStatus][google.ads.admanager.v1.DaiIngestStatusEnum.DaiIngestStatus]

    """

    class DaiIngestStatus(proto.Enum):
        r"""The status of the Dynamic Ad Insertion (DAI) ingestion process. Only
        [Content][google.ads.admanager.v1.Content] with a status of SUCCESS
        will be available for DAI.

        Values:
            DAI_INGEST_STATUS_UNSPECIFIED (0):
                Default value. This value is unused.
            SUCCESS (1):
                The ``Content`` was successfully ingested for DAI.
            WARNING (2):
                There was a non-fatal issue during the DAI
                ingestion process.
            INGESTED (3):
                The preconditioned ``Content`` was successfully ingested for
                DAI.
            INGESTED_WITH_WARNINGS (4):
                There was a non-fatal issue during the DAI ingestion process
                on preconditioned ``Content``.
            CONDITIONED (5):
                The unconditioned ``Content`` was successfully conditioned
                for DAI.
            CONDITIONED_WITH_WARNINGS (6):
                There was a non-fatal issue during the DAI conditioning
                process on originally unconditioned ``Content``.
            FAILURE (7):
                There was a non-fatal issue during the DAI ingestion process
                and the ``Content`` is not available for dynamic ad
                insertion.
        """

        DAI_INGEST_STATUS_UNSPECIFIED = 0
        SUCCESS = 1
        WARNING = 2
        INGESTED = 3
        INGESTED_WITH_WARNINGS = 4
        CONDITIONED = 5
        CONDITIONED_WITH_WARNINGS = 6
        FAILURE = 7


class DaiIngestErrorReasonEnum(proto.Message):
    r"""Wrapper message for
    [DaiIngestErrorReason][google.ads.admanager.v1.DaiIngestErrorReasonEnum.DaiIngestErrorReason]

    """

    class DaiIngestErrorReason(proto.Enum):
        r"""Represents an error associated with a Dynamic Ad Insertion (DAI)
        [Content's][google.ads.admanager.v1.Content] status.

        Values:
            DAI_INGEST_ERROR_REASON_UNSPECIFIED (0):
                Default value. This value is unused.
            INVALID_INGEST_URL (1):
                The ingest URL provided in the publisher's ``Content``
                source feed is invalid. The trigger for this error is the
                ingest URL specified in the publisher's feed.
            INVALID_CLOSED_CAPTION_URL (2):
                The closed caption URL provided in the publisher's
                ``Content`` source feed is invalid.
            MISSING_CLOSED_CAPTION_URL (3):
                There is no closed caption URL for a ``Content`` in the
                publisher's ``Content`` source feed. There is no trigger for
                this error.
            COULD_NOT_FETCH_HLS (4):
                There was an error while trying to fetch the
                HLS from the specified ingest URL. The trigger
                for this error is the ingest URL specified in
                the publisher's feed.
            COULD_NOT_FETCH_SUBTITLES (5):
                There was an error while trying to fetch the
                subtitles from the specified closed caption url.
                The trigger for this error is the closed caption
                URL specified in the publisher's feed.
            MISSING_SUBTITLE_LANGUAGE (6):
                One of the subtitles from the closed caption
                URL is missing a language. The trigger for this
                error is the closed caption URL that does not
                have a language associated with it.
            COULD_NOT_FETCH_MEDIA (7):
                Error fetching the media files from the URLs
                specified in the master HLS playlist. The
                trigger for this error is a media playlist URL
                within the publisher's HLS playlist that could
                not be fetched.
            MALFORMED_MEDIA_BYTES (8):
                The media from the publisher's CDN is
                malformed and cannot be conditioned. The trigger
                for this error is a media playlist URL within
                the publisher's HLS playlist that is malformed.
            CHAPTER_TIME_OUT_OF_BOUNDS (9):
                A chapter time for the ``Content`` is outside of the range
                of the ``Content``'s duration. The trigger for this error is
                the chapter time (a parsable long representing the time in
                ms) that is out of bounds.
            INTERNAL_ERROR (10):
                An internal error occurred. There is no
                trigger for this error.
            CONTENT_HAS_CHAPTER_TIMES_BUT_NO_MIDROLL_SETTINGS (11):
                The ``Content`` has chapter times but the ``Content``'s
                source has no CDN settings for midrolls. There is no trigger
                for this error.
            MALFORMED_MEDIA_PLAYLIST (12):
                There is bad/missing/malformed data in a
                media playlist. The trigger for this error is
                the URL that points to the malformed media
                playlist.
            MIXED_AD_BREAK_TAGS (13):
                Multiple ways of denoting ad breaks were
                detected in a media playlist (e.g. placement
                opportunity tags, cue markers, etc.)
            AD_BREAK_TAGS_INCONSISTENT_ACROSS_VARIANTS (14):
                The ad break tags in the preconditioned ``Content`` are not
                in the same locations across all variant playlists.
            MALFORMED_SUBTITLES (15):
                There is bad/missing/malformed data in a
                subtitles file. The trigger for this error is
                the URL that points to the malformed subtitles.
            SUBTITLES_TOO_LARGE (16):
                The subtitles sent to DAI are too large. The
                trigger for this error is the URL that points to
                the master playlist.
            PLAYLIST_ITEM_URL_DOES_NOT_MATCH_INGEST_COMMON_PATH (17):
                A playlist item has a URL that does not begin
                with the ingest common path provided in the DAI
                settings. The trigger for this error is the
                playlist item URL.
            COULD_NOT_UPLOAD_SPLIT_MEDIA_AUTHENTICATION_FAILED (18):
                Uploading split media segments failed due to
                an authentication error.
            COULD_NOT_UPLOAD_SPLIT_MEDIA_CONNECTION_FAILED (19):
                Uploading spit media segments failed due to a
                connection error.
            COULD_NOT_UPLOAD_SPLIT_MEDIA_WRITE_FAILED (20):
                Uploading split media segments failed due to
                a write error.
            PLAYLISTS_HAVE_DIFFERENT_NUMBER_OF_DISCONTINUITIES (21):
                Variants in a playlist do not have the same
                number of discontinuities. The trigger for this
                error is the master playlist URI.
            PLAYLIST_HAS_NO_STARTING_PTS_VALUE (22):
                The playlist does not have a starting PTS
                value. The trigger for this error is the master
                playlist URI.
            PLAYLIST_DISCONTINUITY_PTS_VALUES_DIFFER_TOO_MUCH (23):
                The PTS at a discontinuity varies too much
                between the different variants. The trigger for
                this error is the master playlist URI.
            SEGMENT_HAS_NO_PTS (24):
                A media segment has no PTS. The trigger for
                this error is the segment data URI.
            SUBTITLE_LANGUAGE_DOES_NOT_MATCH_LANGUAGE_IN_FEED (25):
                The language in the subtitles file does not
                match the language specified in the feed. The
                trigger for this error is the feed language and
                the parsed language separated by a semi-colon,
                e.g. "en;sp".
            CANNOT_DETERMINE_CORRECT_SUBTITLES_FOR_LANGUAGE (26):
                There are multiple subtitles files at the
                closed caption URI, and none of them match the
                language defined in the feed.
            NO_CDN_CONFIG_FOUND (27):
                No CDN configuration found for the ``Content``. The trigger
                for this error is the ``Content``'s master playlist URI.
            CONTENT_HAS_MIDROLLS_BUT_NO_SPLIT_CONTENT_CONFIG (28):
                The ``Content`` has midrolls but there was no split
                ``Content`` config on the CDN configuration for that
                ``Content`` so the ``Content`` was not conditioned. There is
                no trigger for this error.
            CONTENT_HAS_MIDROLLS_BUT_SOURCE_HAS_MIDROLLS_DISABLED (29):
                The ``Content`` has midrolls but the source the ``Content``
                was ingested from has mid-rolls disabled, so the ``Content``
                was not conditioned. There is no trigger for this error.
            ADTS_PARSE_ERROR (30):
                Error parsing ADTS while splitting the ``Content``. The
                trigger for this error is the variant URL and the cue-point
                separated by a semi-colon, e.g. "www.variant2.com;5000".
            AAC_SPLIT_ERROR (31):
                Error splitting an AAC segment. The trigger
                for this error is the variant URL and the
                cue-point separated by a semi-colon, e.g.
                "www.variant2.com;5000".
            AAC_PARSE_ERROR (32):
                Error parsing an AAC file while splitting the ``Content``.
                The trigger for this error is the variant URL and the
                cue-point separated by a semi-colon, e.g.
                "www.variant2.com;5000".
            TS_PARSE_ERROR (33):
                Error parsing a TS file while splitting the ``Content``. The
                trigger for this error is the variant URL and the cue-point
                separated by a semi-colon, e.g. "www.variant2.com;5000".
            TS_SPLIT_ERROR (34):
                Error splitting a TS file while splitting the ``Content``.
                The trigger for this error is the variant URL and the
                cue-point separated by a semi-colon, e.g.
                "www.variant2.com;5000".
            UNSUPPORTED_CONTAINER_FORMAT (35):
                Encountered an unsupported container format while splitting
                the ``Content``. The trigger for this error is the variant
                URL and the cue-point separated by a semi-colon, e.g.
                "www.variant2.com;5000".
            MULTIPLE_ELEMENTARY_STREAMS_OF_SAME_MEDIA_TYPE_IN_TS (36):
                Encountered multiple elementary streams of
                the same media type (audio, video) within a
                transport stream. The trigger for this error is
                the variant URL and the cue-point separated by a
                semi-colon, e.g. "www.variant2.com;5000".
            UNSUPPORTED_TS_MEDIA_FORMAT (37):
                Encountered an unsupported TS media format while splitting
                the ``Content``. The trigger for this error is the variant
                URL and the cue-point separated by a semi-colon, e.g.
                "www.variant2.com;5000".
            NO_IFRAMES_NEAR_CUE_POINT (38):
                Error splitting because there were no
                i-frames near the target split point. The
                trigger for this error is the variant URL and
                the cue-point separated by a semi-colon, e.g.
                "www.variant2.com;5000".
            AC3_SPLIT_ERROR (39):
                Error splitting an AC-3 segment. The trigger
                for this error is the variant URL and the
                cue-point separated by a semi-colon, e.g.
                "www.variant2.com;5000".
            AC3_PARSE_ERROR (40):
                Error parsing an AC-3 file while splitting the ``Content``.
                The trigger for this error is the variant URL and the
                cue-point separated by a semi-colon, e.g.
                "www.variant2.com;5000".
            EAC3_SPLIT_ERROR (41):
                Error splitting an E-AC-3 segment. The
                trigger for this error is the variant URL and
                the cue-point separated by a semi-colon, e.g.
                "www.variant2.com;5000".
            INVALID_ENCRYPTION_KEY (42):
                Error caused by an invalid encryption key.
                The trigger for this error is a media playlist
                URL within the publisher's HLS playlist that has
                the invalid encryption key.
            EAC3_PARSE_ERROR (43):
                Error parsing an E-AC-3 file while splitting the
                ``Content``. The trigger for this error is the variant URL
                and the cue-point separated by a semi-colon, e.g.
                "www.variant2.com;5000".
            CUE_POINT_COUNT_DOES_NOT_MATCH_PTS_COUNT (44):
                Error caused by the number of PTS being a
                different value than the number of cue points +
                1.
            DISCONTINUITY_COUNT_DOES_NOT_MATCH_PTS_COUNT (45):
                Error caused by the number of PTS being a
                different value than the number of discontinuity
                tags + 1.
            DASH_CUE_POINT_EVENT_MISMATCH (46):
                The DASH ``Content`` has cue points but they do not match
                the Event durations from the DASH manifest EventStream, if
                present.
            DASH_MANIFEST_CONDITIONING_FAILED (47):
                The DASH manifest cannot be conditioned for
                midrolls.
            DASH_MANIFEST_CONDITIONING_SEGMENT_BOUNDARY_ERROR (48):
                The DASH manifest cannot be conditioned for
                midrolls because one or more of the cue points
                do not lie on a media segment boundary.
            CLOSED_CAPTION_LANGUAGE_VALUE_INVALID (49):
                The subtitle language code should not contain
                "$$$$$".
            CLOSED_CAPTION_NAME_VALUE_INVALID (50):
                The subtitle name should not contain "$$$$$".
            CLOSED_CAPTION_CHARACTERISTICS_VALUE_UNEXPECTED (51):
                The common subtitle characteristics values
                listed in the HLS spec are:
                1)"public.accessibility.transcribes-spoken-dialog",
                2)"public.accessibility.describes-music-and-sound",
                3)"public.easy-to-read";
            CLOSED_CAPTIONS_WITH_DUPLICATE_KEYS (52):
                Closed captions for a ``Content`` should be unique by
                'language + name'.
            SUBTITLES_PRESENT_IN_FEED_AND_MANIFEST (53):
                Subtitles are defined in the ``Content`` source feed as well
                as inside the stream manifest. Only feed subtitles will be
                ingested.
            INVALID_MEDIA_PROFILE (54):
                The media profile is invalid due to missing
                data.
            CHAPTER_PTS_MISMATCH (55):
                Error caused when the PTS values do not align
                across chapters.
            CHAPTER_RENDITION_ERROR (56):
                Error occurred while chaptering renditions in the
                ``Content``.
            INVALID_TRANSCODING_REQUEST (57):
                Error during notification processing: invalid
                transcoding request.
            TRANSCODE_FAILED (58):
                Error during notification processing:
                transcode failed.
            PLAYLIST_GENERATION_FAILED (59):
                Error during playlist generation.
            COULD_NOT_FETCH_DASH (60):
                Error during DASH ingest: could not fetch
                DASH manifest.
            MALFORMED_DASH (61):
                Error during DASH ingest: malformed DASH
                manifest.
            DASH_CONDITIONING_NOT_SUPPORTED (62):
                Error during DASH ingest: DASH conditioning
                not supported.
        """

        DAI_INGEST_ERROR_REASON_UNSPECIFIED = 0
        INVALID_INGEST_URL = 1
        INVALID_CLOSED_CAPTION_URL = 2
        MISSING_CLOSED_CAPTION_URL = 3
        COULD_NOT_FETCH_HLS = 4
        COULD_NOT_FETCH_SUBTITLES = 5
        MISSING_SUBTITLE_LANGUAGE = 6
        COULD_NOT_FETCH_MEDIA = 7
        MALFORMED_MEDIA_BYTES = 8
        CHAPTER_TIME_OUT_OF_BOUNDS = 9
        INTERNAL_ERROR = 10
        CONTENT_HAS_CHAPTER_TIMES_BUT_NO_MIDROLL_SETTINGS = 11
        MALFORMED_MEDIA_PLAYLIST = 12
        MIXED_AD_BREAK_TAGS = 13
        AD_BREAK_TAGS_INCONSISTENT_ACROSS_VARIANTS = 14
        MALFORMED_SUBTITLES = 15
        SUBTITLES_TOO_LARGE = 16
        PLAYLIST_ITEM_URL_DOES_NOT_MATCH_INGEST_COMMON_PATH = 17
        COULD_NOT_UPLOAD_SPLIT_MEDIA_AUTHENTICATION_FAILED = 18
        COULD_NOT_UPLOAD_SPLIT_MEDIA_CONNECTION_FAILED = 19
        COULD_NOT_UPLOAD_SPLIT_MEDIA_WRITE_FAILED = 20
        PLAYLISTS_HAVE_DIFFERENT_NUMBER_OF_DISCONTINUITIES = 21
        PLAYLIST_HAS_NO_STARTING_PTS_VALUE = 22
        PLAYLIST_DISCONTINUITY_PTS_VALUES_DIFFER_TOO_MUCH = 23
        SEGMENT_HAS_NO_PTS = 24
        SUBTITLE_LANGUAGE_DOES_NOT_MATCH_LANGUAGE_IN_FEED = 25
        CANNOT_DETERMINE_CORRECT_SUBTITLES_FOR_LANGUAGE = 26
        NO_CDN_CONFIG_FOUND = 27
        CONTENT_HAS_MIDROLLS_BUT_NO_SPLIT_CONTENT_CONFIG = 28
        CONTENT_HAS_MIDROLLS_BUT_SOURCE_HAS_MIDROLLS_DISABLED = 29
        ADTS_PARSE_ERROR = 30
        AAC_SPLIT_ERROR = 31
        AAC_PARSE_ERROR = 32
        TS_PARSE_ERROR = 33
        TS_SPLIT_ERROR = 34
        UNSUPPORTED_CONTAINER_FORMAT = 35
        MULTIPLE_ELEMENTARY_STREAMS_OF_SAME_MEDIA_TYPE_IN_TS = 36
        UNSUPPORTED_TS_MEDIA_FORMAT = 37
        NO_IFRAMES_NEAR_CUE_POINT = 38
        AC3_SPLIT_ERROR = 39
        AC3_PARSE_ERROR = 40
        EAC3_SPLIT_ERROR = 41
        INVALID_ENCRYPTION_KEY = 42
        EAC3_PARSE_ERROR = 43
        CUE_POINT_COUNT_DOES_NOT_MATCH_PTS_COUNT = 44
        DISCONTINUITY_COUNT_DOES_NOT_MATCH_PTS_COUNT = 45
        DASH_CUE_POINT_EVENT_MISMATCH = 46
        DASH_MANIFEST_CONDITIONING_FAILED = 47
        DASH_MANIFEST_CONDITIONING_SEGMENT_BOUNDARY_ERROR = 48
        CLOSED_CAPTION_LANGUAGE_VALUE_INVALID = 49
        CLOSED_CAPTION_NAME_VALUE_INVALID = 50
        CLOSED_CAPTION_CHARACTERISTICS_VALUE_UNEXPECTED = 51
        CLOSED_CAPTIONS_WITH_DUPLICATE_KEYS = 52
        SUBTITLES_PRESENT_IN_FEED_AND_MANIFEST = 53
        INVALID_MEDIA_PROFILE = 54
        CHAPTER_PTS_MISMATCH = 55
        CHAPTER_RENDITION_ERROR = 56
        INVALID_TRANSCODING_REQUEST = 57
        TRANSCODE_FAILED = 58
        PLAYLIST_GENERATION_FAILED = 59
        COULD_NOT_FETCH_DASH = 60
        MALFORMED_DASH = 61
        DASH_CONDITIONING_NOT_SUPPORTED = 62


__all__ = tuple(sorted(__protobuf__.manifest))
