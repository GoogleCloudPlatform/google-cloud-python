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

from google.cloud.video.stitcher_v1.types import fetch_options

__protobuf__ = proto.module(
    package="google.cloud.video.stitcher.v1",
    manifest={
        "VodConfig",
        "GamVodConfig",
    },
)


class VodConfig(proto.Message):
    r"""Metadata used to register VOD configs.

    Attributes:
        name (str):
            Output only. The resource name of the VOD config, in the
            form of
            ``projects/{project}/locations/{location}/vodConfigs/{id}``.
        source_uri (str):
            Required. Source URI for the VOD stream
            manifest.
        ad_tag_uri (str):
            Required. The default ad tag associated with
            this VOD config.
        gam_vod_config (google.cloud.video.stitcher_v1.types.GamVodConfig):
            Optional. Google Ad Manager (GAM) metadata.
        state (google.cloud.video.stitcher_v1.types.VodConfig.State):
            Output only. State of the VOD config.
        source_fetch_options (google.cloud.video.stitcher_v1.types.FetchOptions):
            Options for fetching source manifests and
            segments.
    """

    class State(proto.Enum):
        r"""State of the VOD config.

        Values:
            STATE_UNSPECIFIED (0):
                State is not specified.
            CREATING (1):
                VOD config is being created.
            READY (2):
                VOD config is ready for use.
            DELETING (3):
                VOD config is queued up for deletion.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        READY = 2
        DELETING = 3

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
    gam_vod_config: "GamVodConfig" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="GamVodConfig",
    )
    state: State = proto.Field(
        proto.ENUM,
        number=5,
        enum=State,
    )
    source_fetch_options: fetch_options.FetchOptions = proto.Field(
        proto.MESSAGE,
        number=8,
        message=fetch_options.FetchOptions,
    )


class GamVodConfig(proto.Message):
    r"""Metadata used for GAM ad decisioning.

    Attributes:
        network_code (str):
            Required. Ad Manager network code to
            associate with the VOD config.
    """

    network_code: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
