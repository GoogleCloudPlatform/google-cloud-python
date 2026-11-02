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
from google.cloud.video.stitcher import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.video.stitcher_v1.services.video_stitcher_service.async_client import (
    VideoStitcherServiceAsyncClient,
)
from google.cloud.video.stitcher_v1.services.video_stitcher_service.client import (
    VideoStitcherServiceClient,
)
from google.cloud.video.stitcher_v1.types.ad_tag_details import (
    AdRequest,
    LiveAdTagDetail,
    RequestMetadata,
    ResponseMetadata,
    VodAdTagDetail,
)
from google.cloud.video.stitcher_v1.types.cdn_keys import (
    AkamaiCdnKey,
    CdnKey,
    GoogleCdnKey,
    MediaCdnKey,
)
from google.cloud.video.stitcher_v1.types.companions import (
    Companion,
    CompanionAds,
    HtmlAdResource,
    IframeAdResource,
    StaticAdResource,
)
from google.cloud.video.stitcher_v1.types.events import Event, ProgressEvent
from google.cloud.video.stitcher_v1.types.fetch_options import FetchOptions
from google.cloud.video.stitcher_v1.types.live_configs import (
    AdTracking,
    GamLiveConfig,
    LiveConfig,
    PrefetchConfig,
)
from google.cloud.video.stitcher_v1.types.sessions import (
    Interstitials,
    LiveSession,
    ManifestOptions,
    RenditionFilter,
    VodSession,
    VodSessionAd,
    VodSessionAdBreak,
    VodSessionContent,
)
from google.cloud.video.stitcher_v1.types.slates import Slate
from google.cloud.video.stitcher_v1.types.stitch_details import (
    AdStitchDetail,
    VodStitchDetail,
)
from google.cloud.video.stitcher_v1.types.video_stitcher_service import (
    CreateCdnKeyRequest,
    CreateLiveConfigRequest,
    CreateLiveSessionRequest,
    CreateSlateRequest,
    CreateVodConfigRequest,
    CreateVodSessionRequest,
    DeleteCdnKeyRequest,
    DeleteLiveConfigRequest,
    DeleteSlateRequest,
    DeleteVodConfigRequest,
    GetCdnKeyRequest,
    GetLiveAdTagDetailRequest,
    GetLiveConfigRequest,
    GetLiveSessionRequest,
    GetSlateRequest,
    GetVodAdTagDetailRequest,
    GetVodConfigRequest,
    GetVodSessionRequest,
    GetVodStitchDetailRequest,
    ListCdnKeysRequest,
    ListCdnKeysResponse,
    ListLiveAdTagDetailsRequest,
    ListLiveAdTagDetailsResponse,
    ListLiveConfigsRequest,
    ListLiveConfigsResponse,
    ListSlatesRequest,
    ListSlatesResponse,
    ListVodAdTagDetailsRequest,
    ListVodAdTagDetailsResponse,
    ListVodConfigsRequest,
    ListVodConfigsResponse,
    ListVodStitchDetailsRequest,
    ListVodStitchDetailsResponse,
    OperationMetadata,
    UpdateCdnKeyRequest,
    UpdateLiveConfigRequest,
    UpdateSlateRequest,
    UpdateVodConfigRequest,
)
from google.cloud.video.stitcher_v1.types.vod_configs import GamVodConfig, VodConfig

__all__ = (
    "VideoStitcherServiceClient",
    "VideoStitcherServiceAsyncClient",
    "AdRequest",
    "LiveAdTagDetail",
    "RequestMetadata",
    "ResponseMetadata",
    "VodAdTagDetail",
    "AkamaiCdnKey",
    "CdnKey",
    "GoogleCdnKey",
    "MediaCdnKey",
    "Companion",
    "CompanionAds",
    "HtmlAdResource",
    "IframeAdResource",
    "StaticAdResource",
    "Event",
    "ProgressEvent",
    "FetchOptions",
    "GamLiveConfig",
    "LiveConfig",
    "PrefetchConfig",
    "AdTracking",
    "Interstitials",
    "LiveSession",
    "ManifestOptions",
    "RenditionFilter",
    "VodSession",
    "VodSessionAd",
    "VodSessionAdBreak",
    "VodSessionContent",
    "Slate",
    "AdStitchDetail",
    "VodStitchDetail",
    "CreateCdnKeyRequest",
    "CreateLiveConfigRequest",
    "CreateLiveSessionRequest",
    "CreateSlateRequest",
    "CreateVodConfigRequest",
    "CreateVodSessionRequest",
    "DeleteCdnKeyRequest",
    "DeleteLiveConfigRequest",
    "DeleteSlateRequest",
    "DeleteVodConfigRequest",
    "GetCdnKeyRequest",
    "GetLiveAdTagDetailRequest",
    "GetLiveConfigRequest",
    "GetLiveSessionRequest",
    "GetSlateRequest",
    "GetVodAdTagDetailRequest",
    "GetVodConfigRequest",
    "GetVodSessionRequest",
    "GetVodStitchDetailRequest",
    "ListCdnKeysRequest",
    "ListCdnKeysResponse",
    "ListLiveAdTagDetailsRequest",
    "ListLiveAdTagDetailsResponse",
    "ListLiveConfigsRequest",
    "ListLiveConfigsResponse",
    "ListSlatesRequest",
    "ListSlatesResponse",
    "ListVodAdTagDetailsRequest",
    "ListVodAdTagDetailsResponse",
    "ListVodConfigsRequest",
    "ListVodConfigsResponse",
    "ListVodStitchDetailsRequest",
    "ListVodStitchDetailsResponse",
    "OperationMetadata",
    "UpdateCdnKeyRequest",
    "UpdateLiveConfigRequest",
    "UpdateSlateRequest",
    "UpdateVodConfigRequest",
    "GamVodConfig",
    "VodConfig",
)
