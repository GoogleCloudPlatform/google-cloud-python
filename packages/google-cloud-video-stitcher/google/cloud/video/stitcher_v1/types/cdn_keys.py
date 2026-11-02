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
    package="google.cloud.video.stitcher.v1",
    manifest={
        "CdnKey",
        "GoogleCdnKey",
        "AkamaiCdnKey",
        "MediaCdnKey",
    },
)


class CdnKey(proto.Message):
    r"""Configuration for a CDN key. Used by the Video Stitcher
    to sign URIs for fetching video manifests and signing media
    segments for playback.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        google_cdn_key (google.cloud.video.stitcher_v1.types.GoogleCdnKey):
            The configuration for a Google Cloud CDN key.

            This field is a member of `oneof`_ ``cdn_key_config``.
        akamai_cdn_key (google.cloud.video.stitcher_v1.types.AkamaiCdnKey):
            The configuration for an Akamai CDN key.

            This field is a member of `oneof`_ ``cdn_key_config``.
        media_cdn_key (google.cloud.video.stitcher_v1.types.MediaCdnKey):
            The configuration for a Media CDN key.

            This field is a member of `oneof`_ ``cdn_key_config``.
        name (str):
            The resource name of the CDN key, in the form of
            ``projects/{project}/locations/{location}/cdnKeys/{id}``.
            The name is ignored when creating a CDN key.
        hostname (str):
            The hostname this key applies to.
    """

    google_cdn_key: "GoogleCdnKey" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="cdn_key_config",
        message="GoogleCdnKey",
    )
    akamai_cdn_key: "AkamaiCdnKey" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="cdn_key_config",
        message="AkamaiCdnKey",
    )
    media_cdn_key: "MediaCdnKey" = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="cdn_key_config",
        message="MediaCdnKey",
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    hostname: str = proto.Field(
        proto.STRING,
        number=4,
    )


class GoogleCdnKey(proto.Message):
    r"""Configuration for a Google Cloud CDN key.

    Attributes:
        private_key (bytes):
            Input only. Secret for this Google Cloud CDN
            key.
        key_name (str):
            The public name of the Google Cloud CDN key.
    """

    private_key: bytes = proto.Field(
        proto.BYTES,
        number=1,
    )
    key_name: str = proto.Field(
        proto.STRING,
        number=2,
    )


class AkamaiCdnKey(proto.Message):
    r"""Configuration for an Akamai CDN key.

    Attributes:
        token_key (bytes):
            Input only. Token key for the Akamai CDN edge
            configuration.
    """

    token_key: bytes = proto.Field(
        proto.BYTES,
        number=1,
    )


class MediaCdnKey(proto.Message):
    r"""Configuration for a Media CDN key.

    Attributes:
        private_key (bytes):
            Input only. 64-byte ed25519 private key for
            this Media CDN key.
        key_name (str):
            The keyset name of the Media CDN key.
        token_config (google.cloud.video.stitcher_v1.types.MediaCdnKey.TokenConfig):
            Optional. If set, the URL will be signed
            using the Media CDN token. Otherwise, the URL
            would be signed using the standard Media CDN
            signature.
    """

    class TokenConfig(proto.Message):
        r"""Configuration for a Media CDN token.

        Attributes:
            query_parameter (str):
                Optional. The query parameter in which to find the token.

                The name must be 1-64 characters long and match the regular
                expression ``[a-zA-Z]([a-zA-Z0-9_-])*`` which means the
                first character must be a letter, and all following
                characters must be a dash, underscore, letter or digit.

                Defaults to ``edge-cache-token``.
        """

        query_parameter: str = proto.Field(
            proto.STRING,
            number=1,
        )

    private_key: bytes = proto.Field(
        proto.BYTES,
        number=1,
    )
    key_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    token_config: TokenConfig = proto.Field(
        proto.MESSAGE,
        number=3,
        message=TokenConfig,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
