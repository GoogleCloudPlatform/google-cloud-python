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
import google.api_core as api_core

from google.cloud.video.live_stream_v1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.video.live_stream_v1.services.livestream_service",
    "google.cloud.video.live_stream_v1.types.outputs",
    "google.cloud.video.live_stream_v1.types.resources",
    "google.cloud.video.live_stream_v1.types.service",
}


from .services.livestream_service import (
    LivestreamServiceAsyncClient,
    LivestreamServiceClient,
)
from .types.outputs import (
    AudioStream,
    Distribution,
    DistributionStream,
    ElementaryStream,
    Manifest,
    MuxStream,
    PreprocessingConfig,
    RtmpPushOutputEndpoint,
    SegmentSettings,
    SpriteSheet,
    SrtPushOutputEndpoint,
    TextStream,
    TimecodeConfig,
    VideoStream,
)
from .types.resources import (
    Asset,
    AudioFormat,
    AudioStreamProperty,
    AutoTranscriptionConfig,
    Channel,
    Clip,
    DvrSession,
    Encryption,
    EncryptionUpdate,
    Event,
    Input,
    InputAttachment,
    InputConfig,
    InputStreamProperty,
    LogConfig,
    NormalizedCoordinate,
    NormalizedResolution,
    Pool,
    RetentionConfig,
    StaticOverlay,
    TimeInterval,
    VideoFormat,
    VideoStreamProperty,
)
from .types.service import (
    ChannelOperationResponse,
    CreateAssetRequest,
    CreateChannelRequest,
    CreateClipRequest,
    CreateDvrSessionRequest,
    CreateEventRequest,
    CreateInputRequest,
    DeleteAssetRequest,
    DeleteChannelRequest,
    DeleteClipRequest,
    DeleteDvrSessionRequest,
    DeleteEventRequest,
    DeleteInputRequest,
    GetAssetRequest,
    GetChannelRequest,
    GetClipRequest,
    GetDvrSessionRequest,
    GetEventRequest,
    GetInputRequest,
    GetPoolRequest,
    ListAssetsRequest,
    ListAssetsResponse,
    ListChannelsRequest,
    ListChannelsResponse,
    ListClipsRequest,
    ListClipsResponse,
    ListDvrSessionsRequest,
    ListDvrSessionsResponse,
    ListEventsRequest,
    ListEventsResponse,
    ListInputsRequest,
    ListInputsResponse,
    OperationMetadata,
    PreviewInputRequest,
    PreviewInputResponse,
    StartChannelRequest,
    StartDistributionRequest,
    StopChannelRequest,
    StopDistributionRequest,
    UpdateChannelRequest,
    UpdateDvrSessionRequest,
    UpdateInputRequest,
    UpdatePoolRequest,
)

__all__ = (
    "LivestreamServiceAsyncClient",
    "Asset",
    "AudioFormat",
    "AudioStream",
    "AudioStreamProperty",
    "AutoTranscriptionConfig",
    "Channel",
    "ChannelOperationResponse",
    "Clip",
    "CreateAssetRequest",
    "CreateChannelRequest",
    "CreateClipRequest",
    "CreateDvrSessionRequest",
    "CreateEventRequest",
    "CreateInputRequest",
    "DeleteAssetRequest",
    "DeleteChannelRequest",
    "DeleteClipRequest",
    "DeleteDvrSessionRequest",
    "DeleteEventRequest",
    "DeleteInputRequest",
    "Distribution",
    "DistributionStream",
    "DvrSession",
    "ElementaryStream",
    "Encryption",
    "EncryptionUpdate",
    "Event",
    "GetAssetRequest",
    "GetChannelRequest",
    "GetClipRequest",
    "GetDvrSessionRequest",
    "GetEventRequest",
    "GetInputRequest",
    "GetPoolRequest",
    "Input",
    "InputAttachment",
    "InputConfig",
    "InputStreamProperty",
    "ListAssetsRequest",
    "ListAssetsResponse",
    "ListChannelsRequest",
    "ListChannelsResponse",
    "ListClipsRequest",
    "ListClipsResponse",
    "ListDvrSessionsRequest",
    "ListDvrSessionsResponse",
    "ListEventsRequest",
    "ListEventsResponse",
    "ListInputsRequest",
    "ListInputsResponse",
    "LivestreamServiceClient",
    "LogConfig",
    "Manifest",
    "MuxStream",
    "NormalizedCoordinate",
    "NormalizedResolution",
    "OperationMetadata",
    "Pool",
    "PreprocessingConfig",
    "PreviewInputRequest",
    "PreviewInputResponse",
    "RetentionConfig",
    "RtmpPushOutputEndpoint",
    "SegmentSettings",
    "SpriteSheet",
    "SrtPushOutputEndpoint",
    "StartChannelRequest",
    "StartDistributionRequest",
    "StaticOverlay",
    "StopChannelRequest",
    "StopDistributionRequest",
    "TextStream",
    "TimeInterval",
    "TimecodeConfig",
    "UpdateChannelRequest",
    "UpdateDvrSessionRequest",
    "UpdateInputRequest",
    "UpdatePoolRequest",
    "VideoFormat",
    "VideoStream",
    "VideoStreamProperty",
)

api_core.check_python_version("google.cloud.video.live_stream_v1")
api_core.check_dependency_versions("google.cloud.video.live_stream_v1")
