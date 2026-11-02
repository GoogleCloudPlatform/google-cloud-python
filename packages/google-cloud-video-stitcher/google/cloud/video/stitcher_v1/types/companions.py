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

from google.cloud.video.stitcher_v1.types import events as gcvs_events

__protobuf__ = proto.module(
    package="google.cloud.video.stitcher.v1",
    manifest={
        "CompanionAds",
        "Companion",
        "HtmlAdResource",
        "IframeAdResource",
        "StaticAdResource",
    },
)


class CompanionAds(proto.Message):
    r"""Metadata for companion ads.

    Attributes:
        display_requirement (google.cloud.video.stitcher_v1.types.CompanionAds.DisplayRequirement):
            Indicates how many of the companions should
            be displayed with the ad.
        companions (MutableSequence[google.cloud.video.stitcher_v1.types.Companion]):
            List of companion ads.
    """

    class DisplayRequirement(proto.Enum):
        r"""Indicates how many of the companions should be displayed with
        the ad.

        Values:
            DISPLAY_REQUIREMENT_UNSPECIFIED (0):
                Required companions are not specified. The
                default is ALL.
            ALL (1):
                All companions are required to be displayed.
            ANY (2):
                At least one of companions needs to be
                displayed.
            NONE (3):
                All companions are optional for display.
        """

        DISPLAY_REQUIREMENT_UNSPECIFIED = 0
        ALL = 1
        ANY = 2
        NONE = 3

    display_requirement: DisplayRequirement = proto.Field(
        proto.ENUM,
        number=1,
        enum=DisplayRequirement,
    )
    companions: MutableSequence["Companion"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="Companion",
    )


class Companion(proto.Message):
    r"""Metadata for a companion.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        iframe_ad_resource (google.cloud.video.stitcher_v1.types.IframeAdResource):
            The IFrame ad resource associated with the
            companion ad.

            This field is a member of `oneof`_ ``ad_resource``.
        static_ad_resource (google.cloud.video.stitcher_v1.types.StaticAdResource):
            The static ad resource associated with the
            companion ad.

            This field is a member of `oneof`_ ``ad_resource``.
        html_ad_resource (google.cloud.video.stitcher_v1.types.HtmlAdResource):
            The HTML ad resource associated with the
            companion ad.

            This field is a member of `oneof`_ ``ad_resource``.
        api_framework (str):
            The API necessary to communicate with the
            creative if available.
        height_px (int):
            The pixel height of the placement slot for
            the intended creative.
        width_px (int):
            The pixel width of the placement slot for the
            intended creative.
        asset_height_px (int):
            The pixel height of the creative.
        expanded_height_px (int):
            The maximum pixel height of the creative in
            its expanded state.
        asset_width_px (int):
            The pixel width of the creative.
        expanded_width_px (int):
            The maximum pixel width of the creative in
            its expanded state.
        ad_slot_id (str):
            The ID used to identify the desired placement
            on a publisher's page. Values to be used should
            be discussed between publishers and advertisers.
        events (MutableSequence[google.cloud.video.stitcher_v1.types.Event]):
            The list of tracking events for the
            companion.
    """

    iframe_ad_resource: "IframeAdResource" = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="ad_resource",
        message="IframeAdResource",
    )
    static_ad_resource: "StaticAdResource" = proto.Field(
        proto.MESSAGE,
        number=11,
        oneof="ad_resource",
        message="StaticAdResource",
    )
    html_ad_resource: "HtmlAdResource" = proto.Field(
        proto.MESSAGE,
        number=12,
        oneof="ad_resource",
        message="HtmlAdResource",
    )
    api_framework: str = proto.Field(
        proto.STRING,
        number=1,
    )
    height_px: int = proto.Field(
        proto.INT32,
        number=2,
    )
    width_px: int = proto.Field(
        proto.INT32,
        number=3,
    )
    asset_height_px: int = proto.Field(
        proto.INT32,
        number=4,
    )
    expanded_height_px: int = proto.Field(
        proto.INT32,
        number=5,
    )
    asset_width_px: int = proto.Field(
        proto.INT32,
        number=6,
    )
    expanded_width_px: int = proto.Field(
        proto.INT32,
        number=7,
    )
    ad_slot_id: str = proto.Field(
        proto.STRING,
        number=8,
    )
    events: MutableSequence[gcvs_events.Event] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message=gcvs_events.Event,
    )


class HtmlAdResource(proto.Message):
    r"""Metadata for an HTML ad resource.

    Attributes:
        html_source (str):
            The HTML to display for the ad resource.
    """

    html_source: str = proto.Field(
        proto.STRING,
        number=1,
    )


class IframeAdResource(proto.Message):
    r"""Metadata for an IFrame ad resource.

    Attributes:
        uri (str):
            URI source for an IFrame to display for the
            ad resource.
    """

    uri: str = proto.Field(
        proto.STRING,
        number=1,
    )


class StaticAdResource(proto.Message):
    r"""Metadata for a static ad resource.

    Attributes:
        uri (str):
            URI to the static file for the ad resource.
        creative_type (str):
            Describes the MIME type of the ad resource.
    """

    uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    creative_type: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
