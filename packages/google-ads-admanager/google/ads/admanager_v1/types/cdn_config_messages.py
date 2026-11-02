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

from google.ads.admanager_v1.types import (
    cdn_config_status_enum,
    cdn_config_type_enum,
    cdn_security_policy_enum,
    cdn_security_policy_origin_forwarding_enum,
)

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "CdnConfig",
        "CdnSecurityPolicy",
        "AdMediaDeliveryConfig",
        "SourceContentConfig",
        "MediaLocation",
    },
)


class CdnConfig(proto.Message):
    r"""A CdnConfig encapsulates information about where and how to
    ingest and deliver content enabled for DAI (Dynamic Ad
    Insertion).


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the ``CdnConfig``. Format:
            ``networks/{network_code}/cdnConfigs/{cdn_config_id}``
        display_name (str):
            Required. The name of the CdnConfig. This
            value is required to create a CDN config and has
            a maximum length of 255 characters.

            This field is a member of `oneof`_ ``_display_name``.
        cdn_config_type (google.ads.admanager_v1.types.CdnConfigTypeEnum.CdnConfigType):
            Required. The type of CDN config represented
            by this CdnConfig.

            This field is a member of `oneof`_ ``_cdn_config_type``.
        source_content_config (google.ads.admanager_v1.types.SourceContentConfig):
            Optional. Parameters about this CDN config as
            a source of content. This facilitates fetching
            the original content for conditioning and
            delivering the original content as part of a
            modified stream.
        ad_media_delivery_config (google.ads.admanager_v1.types.AdMediaDeliveryConfig):
            Optional. Config of CDN to deliver ad media.
        cdn_config_status (google.ads.admanager_v1.types.CdnConfigStatusEnum.CdnConfigStatus):
            Output only. The status of the CDN config.

            This field is a member of `oneof`_ ``_cdn_config_status``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    cdn_config_type: cdn_config_type_enum.CdnConfigTypeEnum.CdnConfigType = proto.Field(
        proto.ENUM,
        number=3,
        optional=True,
        enum=cdn_config_type_enum.CdnConfigTypeEnum.CdnConfigType,
    )
    source_content_config: "SourceContentConfig" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="SourceContentConfig",
    )
    ad_media_delivery_config: "AdMediaDeliveryConfig" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="AdMediaDeliveryConfig",
    )
    cdn_config_status: cdn_config_status_enum.CdnConfigStatusEnum.CdnConfigStatus = (
        proto.Field(
            proto.ENUM,
            number=7,
            optional=True,
            enum=cdn_config_status_enum.CdnConfigStatusEnum.CdnConfigStatus,
        )
    )


class CdnSecurityPolicy(proto.Message):
    r"""A set of security requirements to authenticate against in
    order to access video content. Different locations (e.g.
    different CDNs) can have different security policies.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        security_policy_type (google.ads.admanager_v1.types.CdnSecurityPolicyTypeEnum.CdnSecurityPolicyType):
            Required. Type of security policy. This
            determines which other fields should be
            populated. This value is required for a valid
            security policy.

            This field is a member of `oneof`_ ``_security_policy_type``.
        token_authentication_key (str):
            Optional. Shared security key used to generate the Akamai
            HMAC token for authenticating requests. Only applicable when
            the value of ``CdnSecurityPolicyType`` is equal to
            ``CdnSecurityPolicyType.AKAMAI`` and will be set to null
            otherwise. Required when the ``CdnConfig.cdnConfigType`` is
            equal to ``CdnConfigType.LIVE_STREAM_SOURCE_CONTENT`` and
            this ``CdnSecurityPolicy`` is being configured for
            ``SourceContentConfig.ingestSettings``.

            This field is a member of `oneof`_ ``_token_authentication_key``.
        server_side_url_signing_disabled (bool):
            Optional. Whether the segment URLs should be
            signed using the #tokenAuthenticationKey on the
            server. This is only applicable for delivery
            media locations that have token authentication
            enabled.

            This field is a member of `oneof`_ ``_server_side_url_signing_disabled``.
        origin_forwarding_type (google.ads.admanager_v1.types.CdnSecurityPolicyOriginForwardingEnum.CdnSecurityPolicyOriginForwarding):
            Optional. The type of origin forwarding used to support
            Akamai authentication policies for the parent playlist. Not
            applicable to ingest locations, and is only applicable to
            delivery media locations with the ``securityPolicyType`` set
            to ``CdnSecurityPolicyType.AKAMAI``. If set elsewhere it
            will be reset to null.

            This field is a member of `oneof`_ ``_origin_forwarding_type``.
        origin_path_prefix (str):
            Optional. The origin path prefix provided by the publisher
            for the parent playlist. Only applicable for delivery media
            locations with the value of ``originForwardingType`` set to
            ``CdnSecurityPolicyOriginForwarding.CONVENTIONAL``, and will
            be set to null otherwise.

            This field is a member of `oneof`_ ``_origin_path_prefix``.
        media_playlist_origin_forwarding_type (google.ads.admanager_v1.types.CdnSecurityPolicyOriginForwardingEnum.CdnSecurityPolicyOriginForwarding):
            Optional. The type of origin forwarding used to support
            Akamai authentication policies for media playlists. This
            setting can only be used with CDN configs with a
            ``cdnConfigType`` of
            ``CdnConfigType.LIVE_STREAM_SOURCE_CONTENT``, is not
            applicable to ingest locations, and is only applicable to
            delivery media locations with the ``CdnSecurityPolicyType``
            set to ``CdnSecurityPolicyType.AKAMAI``. Valid options are
            ``CdnSecurityPolicyOriginForwarding.NONE`` or
            ``CdnSecurityPolicyOriginForwarding.ORIGIN_PATH``. This
            setting can only be used with CDN configs with a
            ``cdnConfigType`` of
            ``CdnConfigType.LIVE_STREAM_SOURCE_CONTENT``.

            This field is a member of `oneof`_ ``_media_playlist_origin_forwarding_type``.
        media_playlist_origin_path_prefix (str):
            Optional. The origin path prefix provided by the publisher
            for the media playlists. Only applicable for delivery media
            locations with the value of
            ``mediaPlaylistOriginForwardingType`` set to
            ``CdnSecurityPolicyOriginForwarding.CONVENTIONAL``, and will
            be set to null otherwise.

            This field is a member of `oneof`_ ``_media_playlist_origin_path_prefix``.
        keyset (str):
            Optional. The name of the EdgeCacheKeyset on
            the Media CDN config that will be used to
            validate signed requests from DAI to ingest
            content.

            This field is a member of `oneof`_ ``_keyset``.
        signed_request_expiration_ttl (google.protobuf.duration_pb2.Duration):
            Optional. The duration for which a request signed with a
            short token will be valid. Only required if
            ``signedRequestMaximumExpirationTtl`` has been set in the
            Media CDN config.

            This field is a member of `oneof`_ ``_signed_request_expiration_ttl``.
    """

    security_policy_type: cdn_security_policy_enum.CdnSecurityPolicyTypeEnum.CdnSecurityPolicyType = proto.Field(
        proto.ENUM,
        number=1,
        optional=True,
        enum=cdn_security_policy_enum.CdnSecurityPolicyTypeEnum.CdnSecurityPolicyType,
    )
    token_authentication_key: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    server_side_url_signing_disabled: bool = proto.Field(
        proto.BOOL,
        number=3,
        optional=True,
    )
    origin_forwarding_type: cdn_security_policy_origin_forwarding_enum.CdnSecurityPolicyOriginForwardingEnum.CdnSecurityPolicyOriginForwarding = proto.Field(
        proto.ENUM,
        number=5,
        optional=True,
        enum=cdn_security_policy_origin_forwarding_enum.CdnSecurityPolicyOriginForwardingEnum.CdnSecurityPolicyOriginForwarding,
    )
    origin_path_prefix: str = proto.Field(
        proto.STRING,
        number=6,
        optional=True,
    )
    media_playlist_origin_forwarding_type: cdn_security_policy_origin_forwarding_enum.CdnSecurityPolicyOriginForwardingEnum.CdnSecurityPolicyOriginForwarding = proto.Field(
        proto.ENUM,
        number=7,
        optional=True,
        enum=cdn_security_policy_origin_forwarding_enum.CdnSecurityPolicyOriginForwardingEnum.CdnSecurityPolicyOriginForwarding,
    )
    media_playlist_origin_path_prefix: str = proto.Field(
        proto.STRING,
        number=8,
        optional=True,
    )
    keyset: str = proto.Field(
        proto.STRING,
        number=10,
        optional=True,
    )
    signed_request_expiration_ttl: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=11,
        optional=True,
        message=duration_pb2.Duration,
    )


class AdMediaDeliveryConfig(proto.Message):
    r"""Parameters about this CDN config of a CDN used for delivering
    ad media.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        override_default_delivery_settings (bool):
            Optional. Whether to override the default delivery CDN. If
            false, ``deliverySettings`` must be null.

            This field is a member of `oneof`_ ``_override_default_delivery_settings``.
        delivery_settings (google.ads.admanager_v1.types.MediaLocation):
            Optional. Config for the delivery location that will
            override the default. From MediaLocationDto, the URL prefix
            field represents the hostname of the external CDN and the
            security policy will be ignored. Null if
            ``overrideDefaultDeliverySettings`` is false.
        additional_delivery_settings (MutableSequence[google.ads.admanager_v1.types.MediaLocation]):
            Optional. List of additional delivery locations. From
            MediaLocationDto, the URL prefix field represents the
            hostname of the external CDN and the security policy will be
            ignored. In your stream create request, you can set the
            value of the ``dai-dlid`` parameter to the name of the
            MediaLocation you want to use.
    """

    override_default_delivery_settings: bool = proto.Field(
        proto.BOOL,
        number=4,
        optional=True,
    )
    delivery_settings: "MediaLocation" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="MediaLocation",
    )
    additional_delivery_settings: MutableSequence["MediaLocation"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message="MediaLocation",
        )
    )


class SourceContentConfig(proto.Message):
    r"""Parameters about this CDN config as a source of content. This
    facilitates fetching the original content for conditioning and
    delivering the original content as part of a modified stream.

    Attributes:
        ingest_settings (google.ads.admanager_v1.types.MediaLocation):
            Required. Config for how DAI should ingest
            media. At ingest time, we match the URL prefix
            of media in a stream's playlist with an ingest
            location and use the authentication credentials
            from the corresponding ingest settings to
            download the media. This value is required for a
            valid source content config.
        default_delivery_settings (google.ads.admanager_v1.types.MediaLocation):
            Required. Default config for how DAI should
            deliver the non-modified media segments. At
            delivery time, we replace the ingest location's
            URL prefix with the delivery location's URL
            prefix and use the security policy from the
            delivery settings to determine how DAI needs to
            deliver the media so that users can access it.
            This value is required for a valid source
            content config.
    """

    ingest_settings: "MediaLocation" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="MediaLocation",
    )
    default_delivery_settings: "MediaLocation" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="MediaLocation",
    )


class MediaLocation(proto.Message):
    r"""Config that associates a media location with a security
    policy and the authentication credentials needed to access the
    content.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        display_name (str):
            Output only. The name of the media location.
            This value is read-only and is assigned by
            Google.

            This field is a member of `oneof`_ ``_display_name``.
        url_prefix (str):
            Required. The URL prefix of the media
            location. This value is required for a valid
            media location.

            This field is a member of `oneof`_ ``_url_prefix``.
        security_policy (google.ads.admanager_v1.types.CdnSecurityPolicy):
            Optional. The security policy and
            authentication credentials needed to access the
            content in this media location. Optional; if
            omitted, no security policy will be applied
            (indicating a public/unprotected location). Must
            NOT be configured for ad media delivery
            locations (doing so will trigger a validation
            error).
    """

    display_name: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    url_prefix: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    security_policy: "CdnSecurityPolicy" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="CdnSecurityPolicy",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
