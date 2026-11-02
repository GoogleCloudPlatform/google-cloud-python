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

import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.video.stitcher_v1.types import fetch_options

__protobuf__ = proto.module(
    package="google.cloud.video.stitcher.v1",
    manifest={
        "AdTracking",
        "LiveConfig",
        "PrefetchConfig",
        "GamLiveConfig",
    },
)


class AdTracking(proto.Enum):
    r"""Determines the ad tracking policy.

    Values:
        AD_TRACKING_UNSPECIFIED (0):
            The ad tracking policy is not specified.
        CLIENT (1):
            Client-side ad tracking is specified. The
            client player is expected to trigger playback
            and activity events itself.
        SERVER (2):
            The Video Stitcher API will trigger playback
            events on behalf of the client player.
    """

    AD_TRACKING_UNSPECIFIED = 0
    CLIENT = 1
    SERVER = 2


class LiveConfig(proto.Message):
    r"""Metadata for used to register live configs.

    Attributes:
        name (str):
            Output only. The resource name of the live config, in the
            form of
            ``projects/{project}/locations/{location}/liveConfigs/{id}``.
        source_uri (str):
            Required. Source URI for the live stream
            manifest.
        ad_tag_uri (str):
            The default ad tag associated with this live
            stream config.
        gam_live_config (google.cloud.video.stitcher_v1.types.GamLiveConfig):
            Additional metadata used to register a live
            stream with Google Ad Manager (GAM)
        state (google.cloud.video.stitcher_v1.types.LiveConfig.State):
            Output only. State of the live config.
        ad_tracking (google.cloud.video.stitcher_v1.types.AdTracking):
            Required. Determines how the ads are tracked.
        default_slate (str):
            This must refer to a slate in the same project. If Google Ad
            Manager (GAM) is used for ads, this string sets the value of
            ``slateCreativeId`` in
            https://developers.google.com/ad-manager/api/reference/v202211/LiveStreamEventService.LiveStreamEvent#slateCreativeId
        stitching_policy (google.cloud.video.stitcher_v1.types.LiveConfig.StitchingPolicy):
            Defines the stitcher behavior in case an ad does not align
            exactly with the ad break boundaries. If not specified, the
            default is ``CUT_CURRENT``.
        prefetch_config (google.cloud.video.stitcher_v1.types.PrefetchConfig):
            The configuration for prefetching ads.
        source_fetch_options (google.cloud.video.stitcher_v1.types.FetchOptions):
            Options for fetching source manifests and
            segments.
    """

    class State(proto.Enum):
        r"""State of the live config.

        Values:
            STATE_UNSPECIFIED (0):
                State is not specified.
            CREATING (1):
                Live config is being created.
            READY (2):
                Live config is ready for use.
            DELETING (3):
                Live config is queued up for deletion.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        READY = 2
        DELETING = 3

    class StitchingPolicy(proto.Enum):
        r"""Defines the ad stitching behavior in case the ad duration does not
        align exactly with the ad break boundaries. If not specified, the
        default is ``CUT_CURRENT``.

        Values:
            STITCHING_POLICY_UNSPECIFIED (0):
                Stitching policy is not specified.
            CUT_CURRENT (1):
                Cuts an ad short and returns to content in
                the middle of the ad.
            COMPLETE_AD (2):
                Finishes stitching the current ad before
                returning to content.
        """

        STITCHING_POLICY_UNSPECIFIED = 0
        CUT_CURRENT = 1
        COMPLETE_AD = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    source_uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    ad_tag_uri: str = proto.Field(
        proto.STRING,
        number=3,
    )
    gam_live_config: "GamLiveConfig" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="GamLiveConfig",
    )
    state: State = proto.Field(
        proto.ENUM,
        number=5,
        enum=State,
    )
    ad_tracking: "AdTracking" = proto.Field(
        proto.ENUM,
        number=6,
        enum="AdTracking",
    )
    default_slate: str = proto.Field(
        proto.STRING,
        number=7,
    )
    stitching_policy: StitchingPolicy = proto.Field(
        proto.ENUM,
        number=8,
        enum=StitchingPolicy,
    )
    prefetch_config: "PrefetchConfig" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="PrefetchConfig",
    )
    source_fetch_options: fetch_options.FetchOptions = proto.Field(
        proto.MESSAGE,
        number=16,
        message=fetch_options.FetchOptions,
    )


class PrefetchConfig(proto.Message):
    r"""The configuration for prefetch ads.

    Attributes:
        enabled (bool):
            Required. Indicates whether the option to
            prefetch ad requests is enabled.
        initial_ad_request_duration (google.protobuf.duration_pb2.Duration):
            The duration in seconds of the part of the
            break to be prefetched. This field is only
            relevant if prefetch is enabled. You should set
            this duration to as long as possible to increase
            the benefits of prefetching, but not longer than
            the shortest ad break expected. For example, for
            a live event with 30s and 60s ad breaks, the
            initial duration should be set to 30s.
    """

    enabled: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    initial_ad_request_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=2,
        message=duration_pb2.Duration,
    )


class GamLiveConfig(proto.Message):
    r"""Metadata used to register a live stream with Google Ad
    Manager (GAM)

    Attributes:
        network_code (str):
            Required. Ad Manager network code to
            associate with the live config.
        asset_key (str):
            Output only. The asset key identifier
            generated for the live config.
        custom_asset_key (str):
            Output only. The custom asset key identifier
            generated for the live config.
    """

    network_code: str = proto.Field(
        proto.STRING,
        number=1,
    )
    asset_key: str = proto.Field(
        proto.STRING,
        number=2,
    )
    custom_asset_key: str = proto.Field(
        proto.STRING,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
