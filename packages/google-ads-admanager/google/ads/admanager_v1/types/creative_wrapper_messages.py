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

from google.ads.admanager_v1.types import creative_wrapper_enums, video_tracking_url
from google.ads.admanager_v1.types import (
    third_party_data_declaration as gaa_third_party_data_declaration,
)

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "CreativeWrapper",
    },
)


class CreativeWrapper(proto.Message):
    r"""A ``CreativeWrapper`` allows the wrapping of HTML snippets to be
    served along with Creative objects.

    ``CreativeWrapper`` must be associated with a
    [LabelType.CREATIVE_WRAPPER][google.ads.admanager.v1.LabelTypeEnum.LabelType.CREATIVE_WRAPPER]
    label and applied to ad units by
    [AdUnit.appliedLabels][google.ads.admanager.v1.AdUnit.applied_labels].


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the ``CreativeWrapper``.
            Format:
            ``networks/{network_code}/creativeWrappers/{creative_wrapper_id}``
        label (str):
            Required. Immutable. The resource name of the
            [Label][google.ads.admanager.v1.Label].
            Format:``networks/{network_code}/label/{label_id}``
        creative_wrapper_type (google.ads.admanager_v1.types.CreativeWrapperTypeEnum.CreativeWrapperType):
            Required. The ``creative_wrapper_type``. If the
            ``creative_wrapper_type`` is
            [CreativeWrapperType.VIDEO_TRACKING_URL][google.ads.admanager.v1.CreativeWrapperTypeEnum.CreativeWrapperType.VIDEO_TRACKING_URL],
            the ``video_tracking_urls`` field must be set. If the
            ``creative_wrapper_type`` is
            [CreativeWrapperType.HTML][google.ads.admanager.v1.CreativeWrapperTypeEnum.CreativeWrapperType.HTML],
            either the header or footer field must be set.

            This field is a member of `oneof`_ ``_creative_wrapper_type``.
        header_creative (str):
            Output only. The resource name of the
            [Creative][google.ads.admanager.v1.Creative]. Format:
            ``networks/{network_code}/creative/{creative_id}``

            This field is a member of `oneof`_ ``_header_creative``.
        footer_creative (str):
            Output only. The resource name of the
            [Creative][google.ads.admanager.v1.Creative]. Format:
            ``networks/{network_code}/creative/{creative_id}``

            This field is a member of `oneof`_ ``_footer_creative``.
        html_header (str):
            Optional. The header HTML snippet that this
            ``CreativeWrapper`` delivers.

            This field is a member of `oneof`_ ``_html_header``.
        html_footer (str):
            Optional. The footer HTML snippet that this
            ``CreativeWrapper`` delivers.

            This field is a member of `oneof`_ ``_html_footer``.
        amp_header (str):
            Optional. The header AMP snippet that this
            ``CreativeWrapper`` delivers.

            This field is a member of `oneof`_ ``_amp_header``.
        amp_footer (str):
            Optional. The footer AMP snippet that this
            ``CreativeWrapper`` delivers.

            This field is a member of `oneof`_ ``_amp_footer``.
        video_tracking_urls (MutableSequence[google.ads.admanager_v1.types.VideoTrackingUrl]):
            Optional. The video tracking URLs that this
            ``CreativeWrapper`` delivers. This field is required if the
            ``creative_wrapper_type`` is
            [CreativeWrapperType.VIDEO_TRACKING_URL][google.ads.admanager.v1.CreativeWrapperTypeEnum.CreativeWrapperType.VIDEO_TRACKING_URL]
            and ignored otherwise.
        third_party_data_declaration (google.ads.admanager_v1.types.ThirdPartyDataDeclaration):
            Optional. The ``ThirdPartyDataDeclaration`` for this
            creative wrapper.

            The third party companies that are associated with this
            ``CreativeWrapper`` and are present in the ``html_header``
            or ``html_footer``. This field is only applicable when the
            ``creative_wrapper_type`` is
            [CreativeWrapperType.HTML][google.ads.admanager.v1.CreativeWrapperTypeEnum.CreativeWrapperType.HTML].

            This field is a member of `oneof`_ ``_third_party_data_declaration``.
        ordering (google.ads.admanager_v1.types.CreativeWrapperOrderingEnum.CreativeWrapperOrdering):
            Optional. If there are multiple wrappers for a
            [Creative][google.ads.admanager.v1.Creative], then ordering
            defines the order in which the HTML snippets are rendered.

            This field is a member of `oneof`_ ``_ordering``.
        status (google.ads.admanager_v1.types.CreativeWrapperStatusEnum.CreativeWrapperStatus):
            Output only. The status of the ``CreativeWrapper``.

            This field is a member of `oneof`_ ``_status``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    label: str = proto.Field(
        proto.STRING,
        number=4,
    )
    creative_wrapper_type: creative_wrapper_enums.CreativeWrapperTypeEnum.CreativeWrapperType = proto.Field(
        proto.ENUM,
        number=5,
        optional=True,
        enum=creative_wrapper_enums.CreativeWrapperTypeEnum.CreativeWrapperType,
    )
    header_creative: str = proto.Field(
        proto.STRING,
        number=7,
        optional=True,
    )
    footer_creative: str = proto.Field(
        proto.STRING,
        number=9,
        optional=True,
    )
    html_header: str = proto.Field(
        proto.STRING,
        number=11,
        optional=True,
    )
    html_footer: str = proto.Field(
        proto.STRING,
        number=12,
        optional=True,
    )
    amp_header: str = proto.Field(
        proto.STRING,
        number=13,
        optional=True,
    )
    amp_footer: str = proto.Field(
        proto.STRING,
        number=14,
        optional=True,
    )
    video_tracking_urls: MutableSequence[video_tracking_url.VideoTrackingUrl] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=15,
            message=video_tracking_url.VideoTrackingUrl,
        )
    )
    third_party_data_declaration: gaa_third_party_data_declaration.ThirdPartyDataDeclaration = proto.Field(
        proto.MESSAGE,
        number=16,
        optional=True,
        message=gaa_third_party_data_declaration.ThirdPartyDataDeclaration,
    )
    ordering: creative_wrapper_enums.CreativeWrapperOrderingEnum.CreativeWrapperOrdering = proto.Field(
        proto.ENUM,
        number=20,
        optional=True,
        enum=creative_wrapper_enums.CreativeWrapperOrderingEnum.CreativeWrapperOrdering,
    )
    status: creative_wrapper_enums.CreativeWrapperStatusEnum.CreativeWrapperStatus = (
        proto.Field(
            proto.ENUM,
            number=21,
            optional=True,
            enum=creative_wrapper_enums.CreativeWrapperStatusEnum.CreativeWrapperStatus,
        )
    )


__all__ = tuple(sorted(__protobuf__.manifest))
