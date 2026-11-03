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

from google.ads.admanager_v1.types import dai_encoding_profile_enums, size

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "DaiEncodingProfile",
        "AudioSettings",
        "VideoSettings",
    },
)


class DaiEncodingProfile(proto.Message):
    r"""A DaiEncodingProfile contains data about a publisher's
    encoding profiles. Ad Manager Dynamic Ad Insertion (DAI) uses
    the profile information about the content to select an
    appropriate ad transcode to play for the particular video.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the ``DaiEncodingProfile``.
            Format:
            ``networks/{network_code}/daiEncodingProfiles/{dai_encoding_profile_id}``
        display_name (str):
            Required. The name of the DaiEncodingProfile. It may be at
            most 64 characters. The name field can contain alphanumeric
            characters and symbols other than the following: ", ', =, !,
            +, #, , ~, ;, ^, (, ), <, >, [, ], the white space
            character.

            This field is a member of `oneof`_ ``_display_name``.
        status (google.ads.admanager_v1.types.DaiEncodingProfileStatusEnum.DaiEncodingProfileStatus):
            Output only. The status of this DaiEncodingProfile.

            DAI encoding profiles are created in the
            [DaiEncodingProfileStatusEnum.DaiEncodingProfileStatus.ACTIVE][google.ads.admanager.v1.DaiEncodingProfileStatusEnum.DaiEncodingProfileStatus.ACTIVE]
            state by default.

            Only active profiles will be allowed to be associated with
            live streams.

            This field is a member of `oneof`_ ``_status``.
        variant_type (google.ads.admanager_v1.types.DaiEncodingProfileVariantTypeEnum.DaiEncodingProfileVariantType):
            Required. The variant playlist type that this
            DaiEncodingProfile represents.

            This field is a member of `oneof`_ ``_variant_type``.
        container_type (google.ads.admanager_v1.types.ContainerTypeEnum.ContainerType):
            Required. The digital container type of the
            underlying media. This is required for MEDIA and
            IFRAME variant types.

            This field is a member of `oneof`_ ``_container_type``.
        video_settings (google.ads.admanager_v1.types.VideoSettings):
            Optional. Information about the video media,
            if present. This field will only be set if the
            media contains video, or is an IFRAME variant
            type.
        audio_settings (google.ads.admanager_v1.types.AudioSettings):
            Optional. Information about the audio media,
            if present. This field will only be set if the
            media contains audio. Only MEDIA and IFRAME
            variant types can set audio.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    status: dai_encoding_profile_enums.DaiEncodingProfileStatusEnum.DaiEncodingProfileStatus = proto.Field(
        proto.ENUM,
        number=4,
        optional=True,
        enum=dai_encoding_profile_enums.DaiEncodingProfileStatusEnum.DaiEncodingProfileStatus,
    )
    variant_type: dai_encoding_profile_enums.DaiEncodingProfileVariantTypeEnum.DaiEncodingProfileVariantType = proto.Field(
        proto.ENUM,
        number=5,
        optional=True,
        enum=dai_encoding_profile_enums.DaiEncodingProfileVariantTypeEnum.DaiEncodingProfileVariantType,
    )
    container_type: dai_encoding_profile_enums.ContainerTypeEnum.ContainerType = (
        proto.Field(
            proto.ENUM,
            number=6,
            optional=True,
            enum=dai_encoding_profile_enums.ContainerTypeEnum.ContainerType,
        )
    )
    video_settings: "VideoSettings" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="VideoSettings",
    )
    audio_settings: "AudioSettings" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="AudioSettings",
    )


class AudioSettings(proto.Message):
    r"""Information about the audio settings of an encoding profile.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        codec (str):
            Required. The RFC6381 codec string of the
            audio.

            This field is a member of `oneof`_ ``_codec``.
        bitrate (int):
            Required. The bitrate of the audio, in bits
            per second. This value must be between 8kbps and
            250 Mbps.

            This field is a member of `oneof`_ ``_bitrate``.
        channels (int):
            Required. The number of audio channels,
            including low frequency channels. This value has
            a maximum of 8.

            This field is a member of `oneof`_ ``_channels``.
        sample_rate_hertz (int):
            Required. The audio sample rate in hertz.
            Must be between 44kHz and 100kHz.

            This field is a member of `oneof`_ ``_sample_rate_hertz``.
    """

    codec: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    bitrate: int = proto.Field(
        proto.INT64,
        number=2,
        optional=True,
    )
    channels: int = proto.Field(
        proto.INT64,
        number=3,
        optional=True,
    )
    sample_rate_hertz: int = proto.Field(
        proto.INT64,
        number=4,
        optional=True,
    )


class VideoSettings(proto.Message):
    r"""Information about the video settings of an encoding profile.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        codec (str):
            Required. The RFC6381 codec string of the
            video.

            This field is a member of `oneof`_ ``_codec``.
        bitrate (int):
            Required. The bitrate of the video, in bits
            per second. This value must be between 32kbps
            and 250 Mbps.

            This field is a member of `oneof`_ ``_bitrate``.
        frames_per_second (float):
            Required. The frames per second of the video.
            This value will be truncated to three decimal
            places.

            This field is a member of `oneof`_ ``_frames_per_second``.
        resolution (google.ads.admanager_v1.types.Size):
            Required. The resolution of the video, in
            pixels.

            This field is a member of `oneof`_ ``_resolution``.
    """

    codec: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    bitrate: int = proto.Field(
        proto.INT64,
        number=2,
        optional=True,
    )
    frames_per_second: float = proto.Field(
        proto.DOUBLE,
        number=3,
        optional=True,
    )
    resolution: size.Size = proto.Field(
        proto.MESSAGE,
        number=4,
        optional=True,
        message=size.Size,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
