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
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

from google.ads.admanager_v1.types import (
    applied_label,
    creative_asset,
    creative_enums,
    creative_placeholder,
    creative_third_party_data_declaration_status_enum,
    custom_creative_asset,
    custom_field_value,
    delivery_enums,
    rich_media_studio_creative_billing_attribute_enum,
    rich_media_studio_creative_format_enum,
    rich_media_studio_messages,
    skippable_ad_type_enum,
    vast_redirect_type_enum,
    video_tracking_url,
)
from google.ads.admanager_v1.types import size as gaa_size
from google.ads.admanager_v1.types import (
    third_party_data_declaration as gaa_third_party_data_declaration,
)

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "Creative",
        "AdExchangeCreativeDetails",
        "AdSenseCreativeDetails",
        "AspectRatioImageCreativeDetails",
        "AudioCreativeDetails",
        "AudioRedirectCreativeDetails",
        "ClickTrackingCreativeDetails",
        "CustomCreativeDetails",
        "Html5CreativeDetails",
        "ImageCreativeDetails",
        "ImageOverlayCreativeDetails",
        "ImageRedirectCreativeDetails",
        "ImageRedirectOverlayCreativeDetails",
        "InternalRedirectCreativeDetails",
        "LegacyDfpCreativeDetails",
        "ProgrammaticCreativeDetails",
        "RichMediaStudioCreativeDetails",
        "SetTopBoxCreativeDetails",
        "TemplateCreativeDetails",
        "ThirdPartyCreativeDetails",
        "VastRedirectCreativeDetails",
        "VideoCreativeDetails",
        "VideoRedirectCreativeDetails",
        "VastInfo",
        "BuyerPlacementConfig",
    },
)


class Creative(proto.Message):
    r"""The Creative resource.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        ad_exchange_creative (google.ads.admanager_v1.types.AdExchangeCreativeDetails):
            Optional. An Ad Exchange dynamic allocation
            creative.

            This field is a member of `oneof`_ ``details``.
        ad_sense_creative (google.ads.admanager_v1.types.AdSenseCreativeDetails):
            Optional. An AdSense dynamic allocation
            creative.

            This field is a member of `oneof`_ ``details``.
        aspect_ratio_image_creative (google.ads.admanager_v1.types.AspectRatioImageCreativeDetails):
            Optional. A Creative intended for mobile
            platforms that displays an image, whose size is
            defined as an aspect ratio. It can have multiple
            images whose dimensions conform to that aspect
            ratio.

            This field is a member of `oneof`_ ``details``.
        audio_creative (google.ads.admanager_v1.types.AudioCreativeDetails):
            Optional. A Creative that contains Ad Manager
            hosted audio ads and is served via VAST XML.

            This field is a member of `oneof`_ ``details``.
        audio_redirect_creative (google.ads.admanager_v1.types.AudioRedirectCreativeDetails):
            Optional. A Creative that contains externally
            hosted audio ads and is served via VAST XML.

            This field is a member of `oneof`_ ``details``.
        click_tracking_creative (google.ads.admanager_v1.types.ClickTrackingCreativeDetails):
            Optional. A creative that is used for
            tracking clicks on ads that are served directly
            from the customers' web servers or media
            servers. NOTE:

            The size attribute is not used for click
            tracking creative and it will not be persisted
            upon save.

            This field is a member of `oneof`_ ``details``.
        custom_creative (google.ads.admanager_v1.types.CustomCreativeDetails):
            Optional. A Creative that contains a custom
            HTML snippet and file assets.

            This field is a member of `oneof`_ ``details``.
        html5_creative (google.ads.admanager_v1.types.Html5CreativeDetails):
            Optional. A Creative that contains a zipped
            HTML5 bundle asset, a list of third party
            impression trackers, and a third party click
            tracker.

            This field is a member of `oneof`_ ``details``.
        image_creative (google.ads.admanager_v1.types.ImageCreativeDetails):
            Optional. A Creative that displays an image.

            This field is a member of `oneof`_ ``details``.
        image_overlay_creative (google.ads.admanager_v1.types.ImageOverlayCreativeDetails):
            Optional. An overlay Creative that displays
            an image and is served via VAST 2.0 XML.
            Overlays cover part of the video content they
            are displayed on top of.

            This field is a member of `oneof`_ ``details``.
        image_redirect_creative (google.ads.admanager_v1.types.ImageRedirectCreativeDetails):
            Optional. A Creative that loads an image
            asset from a specified URL.

            This field is a member of `oneof`_ ``details``.
        image_redirect_overlay_creative (google.ads.admanager_v1.types.ImageRedirectOverlayCreativeDetails):
            Optional. An overlay Creative that loads an
            image asset from a specified URL and is served
            via VAST XML. Overlays cover part of the video
            content they are displayed on top of. This
            creative is read only.

            This field is a member of `oneof`_ ``details``.
        internal_redirect_creative (google.ads.admanager_v1.types.InternalRedirectCreativeDetails):
            Optional. A Creative hosted by Campaign
            Manager 360.
            Similar to third-party creatives, a Campaign
            Manager 360 tag is used to retrieve a creative
            asset. However, Campaign Manager 360 tags are
            not sent to the user's browser. Instead, they
            are processed internally within the Google
            Marketing Platform system.

            This field is a member of `oneof`_ ``details``.
        legacy_dfp_creative (google.ads.admanager_v1.types.LegacyDfpCreativeDetails):
            Optional. A Creative that isn't supported by
            Google DFP, but was migrated from DART.
            Creatives of this type cannot be created or
            modified.

            This field is a member of `oneof`_ ``details``.
        programmatic_creative (google.ads.admanager_v1.types.ProgrammaticCreativeDetails):
            Optional. A Creative used for programmatic
            trafficking. This creative will be auto-created
            with the right approval from the buyer. This
            creative cannot be created through the API. This
            creative can be updated.

            This field is a member of `oneof`_ ``details``.
        rich_media_studio_creative (google.ads.admanager_v1.types.RichMediaStudioCreativeDetails):
            Optional. A Creative that is created by a
            Rich Media Studio. You cannot create this
            creative, but you can update some fields of this
            creative.

            This field is a member of `oneof`_ ``details``.
        set_top_box_creative (google.ads.admanager_v1.types.SetTopBoxCreativeDetails):
            Optional. A Creative that will be served into
            cable set-top boxes. There are no assets for
            this creative type, as they are hosted by
            external cable systems.

            This field is a member of `oneof`_ ``details``.
        template_creative (google.ads.admanager_v1.types.TemplateCreativeDetails):
            Optional. A Creative that is created by the
            specified creative template.

            This field is a member of `oneof`_ ``details``.
        third_party_creative (google.ads.admanager_v1.types.ThirdPartyCreativeDetails):
            Optional. A Creative that is served by a
            3rd-party vendor.

            This field is a member of `oneof`_ ``details``.
        vast_redirect_creative (google.ads.admanager_v1.types.VastRedirectCreativeDetails):
            Optional. A Creative that points to an
            externally hosted VAST ad and is served via VAST
            XML as a VAST Wrapper.

            This field is a member of `oneof`_ ``details``.
        video_creative (google.ads.admanager_v1.types.VideoCreativeDetails):
            Optional. A Creative that contains Ad Manager
            hosted video ads and is served via VAST XML.

            This field is a member of `oneof`_ ``details``.
        video_redirect_creative (google.ads.admanager_v1.types.VideoRedirectCreativeDetails):
            Optional. A Creative that contains externally
            hosted video ads and is served via VAST XML.

            This field is a member of `oneof`_ ``details``.
        name (str):
            Identifier. The resource name of the Creative. Format:
            ``networks/{network_code}/creatives/{creative_id}``
        display_name (str):
            Required. Display name of the ``Creative``. This attribute
            has a maximum length of 255 characters.

            This field is a member of `oneof`_ ``_display_name``.
        advertiser (str):
            Required. The resource name of the Company, which is of type
            Company.Type.ADVERTISER, to which this Creative belongs.
            Format: "networks/{network_code}/companies/{company_id}".

            This field is a member of `oneof`_ ``_advertiser``.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The instant this Creative was
            last modified.
        custom_field_values (MutableSequence[google.ads.admanager_v1.types.CustomFieldValue]):
            Optional. The values of the custom fields
            associated with this creative.
        preview_url (str):
            Output only. The URL of the creative for
            previewing the media.

            This field is a member of `oneof`_ ``_preview_url``.
        size (google.ads.admanager_v1.types.Size):
            Required. Immutable. The Size of the
            creative.
        third_party_data_declaration (google.ads.admanager_v1.types.ThirdPartyDataDeclaration):
            Optional. The third party companies
            associated with this creative. This is distinct
            from any associated companies that Google may
            detect programmatically.
        third_party_data_declaration_status (google.ads.admanager_v1.types.CreativeThirdPartyDataDeclarationStatusEnum.CreativeThirdPartyDataDeclarationStatus):
            Output only. The status of the publisher's
            ``ThirdPartyDataDeclaration``, when compared with the set of
            third party companies detected via automated scanning.

            For example, if automated scanning detects more companies
            than have been declared, this status will be
            [CreativeThirdPartyDataDeclarationStatus.INCOMPLETE][google.ads.admanager.v1.CreativeThirdPartyDataDeclarationStatusEnum.CreativeThirdPartyDataDeclarationStatus.INCOMPLETE].

            This field is a member of `oneof`_ ``_third_party_data_declaration_status``.
        self_declared_european_union_political_content (bool):
            Optional. Whether this creative contains
            self-declared European Union political content.

            This field is a member of `oneof`_ ``_self_declared_european_union_political_content``.
        ad_badging_enabled (bool):
            Optional. Non-empty default. Whether the
            creative has ad badging enabled.
            Defaults to false for VastRedirectCreative,
            ThirdPartyCreative, AudioRedirectCreative,
            ProgrammaticCreative, LegacyDfpMobileCreative,
            FlashOverlayCreative,
            GraphicalInterstitialCreative,
            LegacyDfpCreative, MobileAdNetworkCreative,
            MobileVideoInterstitialCreative,
            SdkMediationCreative, and FlashCreative types.

            Defaults to true for all other creative types.

            This field is a member of `oneof`_ ``_ad_badging_enabled``.
        applied_labels (MutableSequence[google.ads.admanager_v1.types.AppliedLabel]):
            Optional. The set of labels applied directly
            to this creative.
        buyer_placement_config (google.ads.admanager_v1.types.BuyerPlacementConfig):
            Optional. The buyer placement configuration
            for this creative.
    """

    ad_exchange_creative: "AdExchangeCreativeDetails" = proto.Field(
        proto.MESSAGE,
        number=20,
        oneof="details",
        message="AdExchangeCreativeDetails",
    )
    ad_sense_creative: "AdSenseCreativeDetails" = proto.Field(
        proto.MESSAGE,
        number=22,
        oneof="details",
        message="AdSenseCreativeDetails",
    )
    aspect_ratio_image_creative: "AspectRatioImageCreativeDetails" = proto.Field(
        proto.MESSAGE,
        number=23,
        oneof="details",
        message="AspectRatioImageCreativeDetails",
    )
    audio_creative: "AudioCreativeDetails" = proto.Field(
        proto.MESSAGE,
        number=24,
        oneof="details",
        message="AudioCreativeDetails",
    )
    audio_redirect_creative: "AudioRedirectCreativeDetails" = proto.Field(
        proto.MESSAGE,
        number=25,
        oneof="details",
        message="AudioRedirectCreativeDetails",
    )
    click_tracking_creative: "ClickTrackingCreativeDetails" = proto.Field(
        proto.MESSAGE,
        number=26,
        oneof="details",
        message="ClickTrackingCreativeDetails",
    )
    custom_creative: "CustomCreativeDetails" = proto.Field(
        proto.MESSAGE,
        number=18,
        oneof="details",
        message="CustomCreativeDetails",
    )
    html5_creative: "Html5CreativeDetails" = proto.Field(
        proto.MESSAGE,
        number=33,
        oneof="details",
        message="Html5CreativeDetails",
    )
    image_creative: "ImageCreativeDetails" = proto.Field(
        proto.MESSAGE,
        number=19,
        oneof="details",
        message="ImageCreativeDetails",
    )
    image_overlay_creative: "ImageOverlayCreativeDetails" = proto.Field(
        proto.MESSAGE,
        number=35,
        oneof="details",
        message="ImageOverlayCreativeDetails",
    )
    image_redirect_creative: "ImageRedirectCreativeDetails" = proto.Field(
        proto.MESSAGE,
        number=36,
        oneof="details",
        message="ImageRedirectCreativeDetails",
    )
    image_redirect_overlay_creative: "ImageRedirectOverlayCreativeDetails" = (
        proto.Field(
            proto.MESSAGE,
            number=37,
            oneof="details",
            message="ImageRedirectOverlayCreativeDetails",
        )
    )
    internal_redirect_creative: "InternalRedirectCreativeDetails" = proto.Field(
        proto.MESSAGE,
        number=38,
        oneof="details",
        message="InternalRedirectCreativeDetails",
    )
    legacy_dfp_creative: "LegacyDfpCreativeDetails" = proto.Field(
        proto.MESSAGE,
        number=39,
        oneof="details",
        message="LegacyDfpCreativeDetails",
    )
    programmatic_creative: "ProgrammaticCreativeDetails" = proto.Field(
        proto.MESSAGE,
        number=42,
        oneof="details",
        message="ProgrammaticCreativeDetails",
    )
    rich_media_studio_creative: "RichMediaStudioCreativeDetails" = proto.Field(
        proto.MESSAGE,
        number=43,
        oneof="details",
        message="RichMediaStudioCreativeDetails",
    )
    set_top_box_creative: "SetTopBoxCreativeDetails" = proto.Field(
        proto.MESSAGE,
        number=46,
        oneof="details",
        message="SetTopBoxCreativeDetails",
    )
    template_creative: "TemplateCreativeDetails" = proto.Field(
        proto.MESSAGE,
        number=47,
        oneof="details",
        message="TemplateCreativeDetails",
    )
    third_party_creative: "ThirdPartyCreativeDetails" = proto.Field(
        proto.MESSAGE,
        number=48,
        oneof="details",
        message="ThirdPartyCreativeDetails",
    )
    vast_redirect_creative: "VastRedirectCreativeDetails" = proto.Field(
        proto.MESSAGE,
        number=49,
        oneof="details",
        message="VastRedirectCreativeDetails",
    )
    video_creative: "VideoCreativeDetails" = proto.Field(
        proto.MESSAGE,
        number=51,
        oneof="details",
        message="VideoCreativeDetails",
    )
    video_redirect_creative: "VideoRedirectCreativeDetails" = proto.Field(
        proto.MESSAGE,
        number=53,
        oneof="details",
        message="VideoRedirectCreativeDetails",
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=8,
        optional=True,
    )
    advertiser: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    custom_field_values: MutableSequence[custom_field_value.CustomFieldValue] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=76,
            message=custom_field_value.CustomFieldValue,
        )
    )
    preview_url: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )
    size: gaa_size.Size = proto.Field(
        proto.MESSAGE,
        number=5,
        message=gaa_size.Size,
    )
    third_party_data_declaration: gaa_third_party_data_declaration.ThirdPartyDataDeclaration = proto.Field(
        proto.MESSAGE,
        number=59,
        message=gaa_third_party_data_declaration.ThirdPartyDataDeclaration,
    )
    third_party_data_declaration_status: creative_third_party_data_declaration_status_enum.CreativeThirdPartyDataDeclarationStatusEnum.CreativeThirdPartyDataDeclarationStatus = proto.Field(
        proto.ENUM,
        number=60,
        optional=True,
        enum=creative_third_party_data_declaration_status_enum.CreativeThirdPartyDataDeclarationStatusEnum.CreativeThirdPartyDataDeclarationStatus,
    )
    self_declared_european_union_political_content: bool = proto.Field(
        proto.BOOL,
        number=13,
        optional=True,
    )
    ad_badging_enabled: bool = proto.Field(
        proto.BOOL,
        number=17,
        optional=True,
    )
    applied_labels: MutableSequence[applied_label.AppliedLabel] = proto.RepeatedField(
        proto.MESSAGE,
        number=56,
        message=applied_label.AppliedLabel,
    )
    buyer_placement_config: "BuyerPlacementConfig" = proto.Field(
        proto.MESSAGE,
        number=81,
        message="BuyerPlacementConfig",
    )


class AdExchangeCreativeDetails(proto.Message):
    r"""An Ad Exchange dynamic allocation creative.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        native_eligible (bool):
            Optional. Whether this creative is eligible
            for native ad-serving. This value is optional
            and defaults to false.

            This field is a member of `oneof`_ ``_native_eligible``.
        interstitial (bool):
            Optional. True if this creative is
            interstitial. An interstitial creative will not
            consider an impression served until it is fully
            rendered in the browser.

            This field is a member of `oneof`_ ``_interstitial``.
        allows_all_requested_sizes (bool):
            Optional. True if this creative is eligible
            for all requested sizes.

            This field is a member of `oneof`_ ``_allows_all_requested_sizes``.
        slot_id (str):
            Output only. The ID of ad slot (inventory)
            that an advertiser might want to target.

            This field is a member of `oneof`_ ``_slot_id``.
        backfill_snippet (str):
            Optional. The code snippet (ad tag) from Ad
            Exchange or AdSense to traffic the dynamic
            allocation creative. Only valid Ad Exchange or
            AdSense parameters will be considered. Any
            extraneous HTML or JavaScript will be ignored.

            This field is a member of `oneof`_ ``_backfill_snippet``.
    """

    native_eligible: bool = proto.Field(
        proto.BOOL,
        number=1,
        optional=True,
    )
    interstitial: bool = proto.Field(
        proto.BOOL,
        number=2,
        optional=True,
    )
    allows_all_requested_sizes: bool = proto.Field(
        proto.BOOL,
        number=3,
        optional=True,
    )
    slot_id: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )
    backfill_snippet: str = proto.Field(
        proto.STRING,
        number=5,
        optional=True,
    )


class AdSenseCreativeDetails(proto.Message):
    r"""An AdSense dynamic allocation creative.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        slot_id (str):
            Output only. The ID of ad slot (inventory)
            that an advertiser might want to target.

            This field is a member of `oneof`_ ``_slot_id``.
        backfill_snippet (str):
            Optional. The code snippet (ad tag) from Ad
            Exchange or AdSense to traffic the dynamic
            allocation creative. Only valid Ad Exchange or
            AdSense parameters will be considered. Any
            extraneous HTML or JavaScript will be ignored.

            This field is a member of `oneof`_ ``_backfill_snippet``.
    """

    slot_id: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    backfill_snippet: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )


class AspectRatioImageCreativeDetails(proto.Message):
    r"""A Creative intended for mobile platforms that displays an
    image, whose size is defined as an aspect ratio. It can have
    multiple images whose dimensions conform to that aspect ratio.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        alt_text (str):
            Optional. The text that is served along with
            the image creative, primarily for accessibility.
            If no suitable image size is available for the
            device, this text replaces the image completely.
            This field is optional and has a maximum length
            of 500 characters.

            This field is a member of `oneof`_ ``_alt_text``.
        destination_url (str):
            Optional. The URL that the user is directed to if they click
            on the creative. This attribute is required unless the
            ``destinationUrlType`` is ``NONE``, and has a maximum length
            of 1024 characters.

            This field is a member of `oneof`_ ``_destination_url``.
        destination_url_type (google.ads.admanager_v1.types.CreativeDestinationUrlTypeEnum.CreativeDestinationUrlType):
            Optional. The action that should be performed if the user
            clicks on the creative. This attribute defaults to
            ``CLICK_TO_WEB``.

            This field is a member of `oneof`_ ``_destination_url_type``.
        image_assets (MutableSequence[google.ads.admanager_v1.types.CreativeAsset]):
            Required. The images associated with this
            creative. The ad server will choose one based on
            the capabilities of the device. Each asset
            should have a size which is of the same aspect
            ratio as the Creative.size. This attribute is
            required and must have at least one asset.
        third_party_impression_tracking_urls (MutableSequence[str]):
            Optional. Third party impression tracking
            URLs to ping when this creative is displayed.
    """

    alt_text: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    destination_url: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    destination_url_type: creative_enums.CreativeDestinationUrlTypeEnum.CreativeDestinationUrlType = proto.Field(
        proto.ENUM,
        number=3,
        optional=True,
        enum=creative_enums.CreativeDestinationUrlTypeEnum.CreativeDestinationUrlType,
    )
    image_assets: MutableSequence[creative_asset.CreativeAsset] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=creative_asset.CreativeAsset,
    )
    third_party_impression_tracking_urls: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )


class AudioCreativeDetails(proto.Message):
    r"""A Creative that contains Ad Manager hosted audio ads and is
    served via VAST XML.

    Attributes:
        vast_info (google.ads.admanager_v1.types.VastInfo):
            Optional. Fields common to Video Ad Serving
            Template (VAST) creatives
    """

    vast_info: "VastInfo" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="VastInfo",
    )


class AudioRedirectCreativeDetails(proto.Message):
    r"""A Creative that contains externally hosted audio ads and is
    served via VAST XML.

    Attributes:
        vast_info (google.ads.admanager_v1.types.VastInfo):
            Optional. Fields common to Video Ad Serving
            Template (VAST) creatives
    """

    vast_info: "VastInfo" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="VastInfo",
    )


class ClickTrackingCreativeDetails(proto.Message):
    r"""A creative that is used for tracking clicks on ads that are
    served directly from the customers' web servers or media
    servers. NOTE: The size attribute is not used for click tracking
    creative and it will not be persisted upon save.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        click_tracking_url (str):
            Optional. The click tracking URL.

            This field is a member of `oneof`_ ``_click_tracking_url``.
    """

    click_tracking_url: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )


class CustomCreativeDetails(proto.Message):
    r"""A Creative that contains a custom HTML snippet and file
    assets.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        html_snippet (str):
            Required. The HTML snippet that this creative
            delivers.

            This field is a member of `oneof`_ ``_html_snippet``.
        amp_html_snippet (str):
            The AMP HTML snippet that this creative
            delivers.

            This field is a member of `oneof`_ ``_amp_html_snippet``.
        interstitial (bool):
            Whether this custom creative is an
            interstitial. An interstitial creative will not
            consider an impression served until it is fully
            rendered in the browser.

            This field is a member of `oneof`_ ``_interstitial``.
        destination_url (str):
            Optional. The URL that the user is directed to if they click
            on the creative. This attribute is required unless the
            ``destinationUrlType`` is ``NONE``, and has a maximum length
            of 1024 characters.

            This field is a member of `oneof`_ ``_destination_url``.
        destination_url_type (google.ads.admanager_v1.types.CreativeDestinationUrlTypeEnum.CreativeDestinationUrlType):
            Optional. The action that should be performed if the user
            clicks on the creative. This attribute defaults to
            ``CLICK_TO_WEB``.

            This field is a member of `oneof`_ ``_destination_url_type``.
        safe_frame_compatible (bool):
            Input only. Whether the creative is
            compatible for SafeFrame rendering.

            This field is a member of `oneof`_ ``_safe_frame_compatible``.
        effective_safe_frame_compatible (bool):
            Output only. The effective value of whether
            the creative is compatible for SafeFrame
            rendering, as decided by the service.

            This field is a member of `oneof`_ ``_effective_safe_frame_compatible``.
        third_party_impression_tracking_urls (MutableSequence[str]):
            Optional. Impression tracking URLs to ping
            when this creative is displayed.
        locked_orientation (google.ads.admanager_v1.types.CreativeLockedOrientationEnum.CreativeLockedOrientation):
            Optional. A locked orientation for this
            creative to be displayed in.

            This field is a member of `oneof`_ ``_locked_orientation``.
        custom_creative_assets (MutableSequence[google.ads.admanager_v1.types.CustomCreativeAsset]):
            Optional. File assets that are associated
            with this creative, and can be referenced in the
            snippet.
    """

    html_snippet: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    amp_html_snippet: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    interstitial: bool = proto.Field(
        proto.BOOL,
        number=3,
        optional=True,
    )
    destination_url: str = proto.Field(
        proto.STRING,
        number=12,
        optional=True,
    )
    destination_url_type: creative_enums.CreativeDestinationUrlTypeEnum.CreativeDestinationUrlType = proto.Field(
        proto.ENUM,
        number=13,
        optional=True,
        enum=creative_enums.CreativeDestinationUrlTypeEnum.CreativeDestinationUrlType,
    )
    safe_frame_compatible: bool = proto.Field(
        proto.BOOL,
        number=5,
        optional=True,
    )
    effective_safe_frame_compatible: bool = proto.Field(
        proto.BOOL,
        number=6,
        optional=True,
    )
    third_party_impression_tracking_urls: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )
    locked_orientation: creative_enums.CreativeLockedOrientationEnum.CreativeLockedOrientation = proto.Field(
        proto.ENUM,
        number=8,
        optional=True,
        enum=creative_enums.CreativeLockedOrientationEnum.CreativeLockedOrientation,
    )
    custom_creative_assets: MutableSequence[
        custom_creative_asset.CustomCreativeAsset
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=14,
        message=custom_creative_asset.CustomCreativeAsset,
    )


class Html5CreativeDetails(proto.Message):
    r"""A Creative that contains a zipped HTML5 bundle asset, a list
    of third party impression trackers, and a third party click
    tracker.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        locked_orientation (google.ads.admanager_v1.types.CreativeLockedOrientationEnum.CreativeLockedOrientation):
            Optional. A locked orientation for this
            creative to be displayed in.

            This field is a member of `oneof`_ ``_locked_orientation``.
        override_size (bool):
            Optional. Allows the creative size to differ
            from the actual HTML5 asset size.

            This field is a member of `oneof`_ ``_override_size``.
        third_party_impression_tracking_urls (MutableSequence[str]):
            Optional. Impression tracking URLs to ping
            when this creative is displayed.
        third_party_click_tracking_url (str):
            Optional. A click tracking URL to ping when
            this creative is clicked.

            This field is a member of `oneof`_ ``_third_party_click_tracking_url``.
        safe_frame_compatible (bool):
            Optional. Whether the creative is compatible
            for SafeFrame rendering.

            This field is a member of `oneof`_ ``_safe_frame_compatible``.
        html5_asset (google.ads.admanager_v1.types.CreativeAsset):
            Required. The HTML5 asset. To preview the HTML5 asset, use
            the ``CreativeAsset.asset_url``. In this field, the
            ``CreativeAsset.asset_byte_array`` must be a zip bundle and
            the ``CreativeAsset.file_name`` must have a zip extension.

            This field is a member of `oneof`_ ``_html5_asset``.
    """

    locked_orientation: creative_enums.CreativeLockedOrientationEnum.CreativeLockedOrientation = proto.Field(
        proto.ENUM,
        number=1,
        optional=True,
        enum=creative_enums.CreativeLockedOrientationEnum.CreativeLockedOrientation,
    )
    override_size: bool = proto.Field(
        proto.BOOL,
        number=2,
        optional=True,
    )
    third_party_impression_tracking_urls: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    third_party_click_tracking_url: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )
    safe_frame_compatible: bool = proto.Field(
        proto.BOOL,
        number=7,
        optional=True,
    )
    html5_asset: creative_asset.CreativeAsset = proto.Field(
        proto.MESSAGE,
        number=8,
        optional=True,
        message=creative_asset.CreativeAsset,
    )


class ImageCreativeDetails(proto.Message):
    r"""A Creative that displays an image.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        alt_text (str):
            Alternative text to be rendered along with
            the creative used mainly for accessibility. This
            field has a maximum length of 500 characters.

            This field is a member of `oneof`_ ``_alt_text``.
        destination_url (str):
            Optional. The URL that the user is directed to if they click
            on the creative. This attribute is required unless the
            ``destinationUrlType`` is ``NONE``, and has a maximum length
            of 1024 characters.

            This field is a member of `oneof`_ ``_destination_url``.
        destination_url_type (google.ads.admanager_v1.types.CreativeDestinationUrlTypeEnum.CreativeDestinationUrlType):
            Optional. The action that should be performed if the user
            clicks on the creative. This attribute defaults to
            ``CLICK_TO_WEB``.

            This field is a member of `oneof`_ ``_destination_url_type``.
        third_party_impression_tracking_urls (MutableSequence[str]):
            Optional. Impression tracking URLs to ping
            when this creative is displayed.
        amp_destination_url (str):
            Optional. The AMP destination URL for this creative. This
            must be a valid URL, including the ``http://`` or
            ``https://`` scheme.

            This field is a member of `oneof`_ ``_amp_destination_url``.
        locked_orientation (google.ads.admanager_v1.types.CreativeLockedOrientationEnum.CreativeLockedOrientation):
            Optional. A locked orientation for this
            creative to be displayed in.

            This field is a member of `oneof`_ ``_locked_orientation``.
        primary_image_asset (google.ads.admanager_v1.types.CreativeAsset):
            The primary image asset associated with this
            creative. This attribute is required.
        secondary_image_assets (MutableSequence[google.ads.admanager_v1.types.CreativeAsset]):
            Secondary image assets associated with this
            creative. This attribute is optional.

            Secondary image assets can be used to store
            different resolution versions of the primary
            asset for use on non-standard density screens.
        override_size (bool):
            Optional. Allows the creative size to differ
            from the actual image asset size.

            This field is a member of `oneof`_ ``_override_size``.
    """

    alt_text: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    destination_url: str = proto.Field(
        proto.STRING,
        number=8,
        optional=True,
    )
    destination_url_type: creative_enums.CreativeDestinationUrlTypeEnum.CreativeDestinationUrlType = proto.Field(
        proto.ENUM,
        number=9,
        optional=True,
        enum=creative_enums.CreativeDestinationUrlTypeEnum.CreativeDestinationUrlType,
    )
    third_party_impression_tracking_urls: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    amp_destination_url: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )
    locked_orientation: creative_enums.CreativeLockedOrientationEnum.CreativeLockedOrientation = proto.Field(
        proto.ENUM,
        number=5,
        optional=True,
        enum=creative_enums.CreativeLockedOrientationEnum.CreativeLockedOrientation,
    )
    primary_image_asset: creative_asset.CreativeAsset = proto.Field(
        proto.MESSAGE,
        number=6,
        message=creative_asset.CreativeAsset,
    )
    secondary_image_assets: MutableSequence[creative_asset.CreativeAsset] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=7,
            message=creative_asset.CreativeAsset,
        )
    )
    override_size: bool = proto.Field(
        proto.BOOL,
        number=10,
        optional=True,
    )


class ImageOverlayCreativeDetails(proto.Message):
    r"""An overlay Creative that displays an image and is served via
    VAST 2.0 XML. Overlays cover part of the video content they are
    displayed on top of.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        locked_orientation (google.ads.admanager_v1.types.CreativeLockedOrientationEnum.CreativeLockedOrientation):
            Optional. A locked orientation for this
            creative to be displayed in.

            This field is a member of `oneof`_ ``_locked_orientation``.
        destination_url (str):
            Optional. The URL that the user is directed to if they click
            on the creative. This attribute is required unless the
            ``destinationUrlType`` is ``NONE``, and has a maximum length
            of 1024 characters.

            This field is a member of `oneof`_ ``_destination_url``.
        destination_url_type (google.ads.admanager_v1.types.CreativeDestinationUrlTypeEnum.CreativeDestinationUrlType):
            Optional. The action that should be performed if the user
            clicks on the creative. This attribute defaults to
            ``CLICK_TO_WEB``.

            This field is a member of `oneof`_ ``_destination_url_type``.
        override_size (bool):
            Optional. Allows the creative size to differ
            from the actual image asset size.

            This field is a member of `oneof`_ ``_override_size``.
        primary_image_asset (google.ads.admanager_v1.types.CreativeAsset):
            Required. The primary image asset associated
            with this creative.
        creative_set_display_name (str):
            Output only. The display name of the creative
            set.

            This field is a member of `oneof`_ ``_creative_set_display_name``.
        creative_set (str):
            Output only. The resource name of the creative set. Format:
            "networks/{network_code}/creativeSets/{creative_set_id}".

            This field is a member of `oneof`_ ``_creative_set``.
        companion_creatives (MutableSequence[str]):
            Output only. The resource names of the companion creatives
            that are associated with this creative. Format:
            "networks/{network_code}/creatives/{creative_id}".
        tracking_urls (MutableSequence[google.ads.admanager_v1.types.VideoTrackingUrl]):
            Optional. URLs that will be pinged when
            conversion events happen.
        custom_parameters (str):
            Optional. A comma separated key=value list of parameters
            that will be supplied to the creative, written into the VAST
            ``AdParameters`` node.

            This field is a member of `oneof`_ ``_custom_parameters``.
        duration (google.protobuf.duration_pb2.Duration):
            Optional. Minimum suggested duration.
        expected_companions (MutableSequence[google.ads.admanager_v1.types.CreativePlaceholder]):
            Optional. ``CreativePlaceholder`` objects a creative set
            should fulfill.
        expected_companion_delivery_option (google.ads.admanager_v1.types.CompanionDeliveryOptionEnum.CompanionDeliveryOption):
            Output only. The companion delivery option
            this set will be served with.

            This field is a member of `oneof`_ ``_expected_companion_delivery_option``.
        vast_preview_url (str):
            Output only. An ad tag URL that will return a
            preview of the VAST XML response specific to
            this creative.

            This field is a member of `oneof`_ ``_vast_preview_url``.
    """

    locked_orientation: creative_enums.CreativeLockedOrientationEnum.CreativeLockedOrientation = proto.Field(
        proto.ENUM,
        number=1,
        optional=True,
        enum=creative_enums.CreativeLockedOrientationEnum.CreativeLockedOrientation,
    )
    destination_url: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    destination_url_type: creative_enums.CreativeDestinationUrlTypeEnum.CreativeDestinationUrlType = proto.Field(
        proto.ENUM,
        number=4,
        optional=True,
        enum=creative_enums.CreativeDestinationUrlTypeEnum.CreativeDestinationUrlType,
    )
    override_size: bool = proto.Field(
        proto.BOOL,
        number=5,
        optional=True,
    )
    primary_image_asset: creative_asset.CreativeAsset = proto.Field(
        proto.MESSAGE,
        number=6,
        message=creative_asset.CreativeAsset,
    )
    creative_set_display_name: str = proto.Field(
        proto.STRING,
        number=7,
        optional=True,
    )
    creative_set: str = proto.Field(
        proto.STRING,
        number=8,
        optional=True,
    )
    companion_creatives: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=9,
    )
    tracking_urls: MutableSequence[video_tracking_url.VideoTrackingUrl] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=10,
            message=video_tracking_url.VideoTrackingUrl,
        )
    )
    custom_parameters: str = proto.Field(
        proto.STRING,
        number=11,
        optional=True,
    )
    duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=12,
        message=duration_pb2.Duration,
    )
    expected_companions: MutableSequence[creative_placeholder.CreativePlaceholder] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=13,
            message=creative_placeholder.CreativePlaceholder,
        )
    )
    expected_companion_delivery_option: delivery_enums.CompanionDeliveryOptionEnum.CompanionDeliveryOption = proto.Field(
        proto.ENUM,
        number=14,
        optional=True,
        enum=delivery_enums.CompanionDeliveryOptionEnum.CompanionDeliveryOption,
    )
    vast_preview_url: str = proto.Field(
        proto.STRING,
        number=16,
        optional=True,
    )


class ImageRedirectCreativeDetails(proto.Message):
    r"""A Creative that loads an image asset from a specified URL.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        destination_url (str):
            Optional. The URL that the user is directed to if they click
            on the creative. This attribute is required unless the
            ``destinationUrlType`` is ``NONE``, and has a maximum length
            of 1024 characters.

            This field is a member of `oneof`_ ``_destination_url``.
        destination_url_type (google.ads.admanager_v1.types.CreativeDestinationUrlTypeEnum.CreativeDestinationUrlType):
            Optional. The action that should be performed if the user
            clicks on the creative. This attribute defaults to
            ``CLICK_TO_WEB``.

            This field is a member of `oneof`_ ``_destination_url_type``.
        alt_text (str):
            Optional. Alternative text to be rendered
            along with the creative used mainly for
            accessibility. This field has a maximum length
            of 500 characters.

            This field is a member of `oneof`_ ``_alt_text``.
        image_url (str):
            Required. The URL where the actual asset
            resides. This field has a maximum length of 1024
            characters.

            This field is a member of `oneof`_ ``_image_url``.
        third_party_impression_tracking_urls (MutableSequence[str]):
            Optional. Impression tracking URLs to ping
            when this creative is displayed. Each string has
            a maximum length of 1024 characters.
    """

    destination_url: str = proto.Field(
        proto.STRING,
        number=5,
        optional=True,
    )
    destination_url_type: creative_enums.CreativeDestinationUrlTypeEnum.CreativeDestinationUrlType = proto.Field(
        proto.ENUM,
        number=6,
        optional=True,
        enum=creative_enums.CreativeDestinationUrlTypeEnum.CreativeDestinationUrlType,
    )
    alt_text: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    image_url: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    third_party_impression_tracking_urls: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )


class ImageRedirectOverlayCreativeDetails(proto.Message):
    r"""An overlay Creative that loads an image asset from a
    specified URL and is served via VAST XML. Overlays cover part of
    the video content they are displayed on top of. This creative is
    read only.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        destination_url (str):
            Optional. The URL that the user is directed to if they click
            on the creative. This attribute is required unless the
            ``destinationUrlType`` is ``NONE``, and has a maximum length
            of 1024 characters.

            This field is a member of `oneof`_ ``_destination_url``.
        destination_url_type (google.ads.admanager_v1.types.CreativeDestinationUrlTypeEnum.CreativeDestinationUrlType):
            Optional. The action that should be performed if the user
            clicks on the creative. This attribute defaults to
            ``CLICK_TO_WEB``.

            This field is a member of `oneof`_ ``_destination_url_type``.
        image_url (str):
            Required. The URL where the actual image
            asset resides. This attribute is required and
            has a maximum length of 1024 characters.

            This field is a member of `oneof`_ ``_image_url``.
        asset_size (google.ads.admanager_v1.types.Size):
            Optional. The size of the image asset. Note
            that this may differ from the creative size if
            the asset is not expected to fill the entire
            video player.

            This field is a member of `oneof`_ ``_asset_size``.
        duration (google.protobuf.duration_pb2.Duration):
            Optional. Minimum suggested duration.

            This field is a member of `oneof`_ ``_duration``.
        tracking_urls (MutableSequence[google.ads.admanager_v1.types.VideoTrackingUrl]):
            Optional. URLs that will be pinged when
            conversion events happen.
        custom_parameters (str):
            Optional. A comma separated key=value list of parameters
            that will be supplied to the creative, written into the VAST
            ``AdParameters`` node.

            This field is a member of `oneof`_ ``_custom_parameters``.
        expected_companions (MutableSequence[google.ads.admanager_v1.types.CreativePlaceholder]):
            Optional. ``CreativePlaceholder`` objects a creative set
            should fulfill.
        expected_companion_delivery_option (google.ads.admanager_v1.types.CompanionDeliveryOptionEnum.CompanionDeliveryOption):
            Output only. The companion delivery option
            this set will be served with.

            This field is a member of `oneof`_ ``_expected_companion_delivery_option``.
        vast_preview_url (str):
            Output only. An ad tag URL that will return a
            preview of the VAST XML response specific to
            this creative.

            This field is a member of `oneof`_ ``_vast_preview_url``.
        creative_set_display_name (str):
            Output only. The display name of the creative
            set.

            This field is a member of `oneof`_ ``_creative_set_display_name``.
        creative_set (str):
            Output only. The resource name of the creative set. Format:
            "networks/{network_code}/creativeSets/{creative_set_id}".

            This field is a member of `oneof`_ ``_creative_set``.
        companion_creatives (MutableSequence[str]):
            Optional. The companion creatives that are associated with
            this creative. Format:
            "networks/{network_code}/creatives/{creative_id}".
    """

    destination_url: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    destination_url_type: creative_enums.CreativeDestinationUrlTypeEnum.CreativeDestinationUrlType = proto.Field(
        proto.ENUM,
        number=3,
        optional=True,
        enum=creative_enums.CreativeDestinationUrlTypeEnum.CreativeDestinationUrlType,
    )
    image_url: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    asset_size: gaa_size.Size = proto.Field(
        proto.MESSAGE,
        number=7,
        optional=True,
        message=gaa_size.Size,
    )
    duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=8,
        optional=True,
        message=duration_pb2.Duration,
    )
    tracking_urls: MutableSequence[video_tracking_url.VideoTrackingUrl] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=9,
            message=video_tracking_url.VideoTrackingUrl,
        )
    )
    custom_parameters: str = proto.Field(
        proto.STRING,
        number=10,
        optional=True,
    )
    expected_companions: MutableSequence[creative_placeholder.CreativePlaceholder] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=11,
            message=creative_placeholder.CreativePlaceholder,
        )
    )
    expected_companion_delivery_option: delivery_enums.CompanionDeliveryOptionEnum.CompanionDeliveryOption = proto.Field(
        proto.ENUM,
        number=12,
        optional=True,
        enum=delivery_enums.CompanionDeliveryOptionEnum.CompanionDeliveryOption,
    )
    vast_preview_url: str = proto.Field(
        proto.STRING,
        number=14,
        optional=True,
    )
    creative_set_display_name: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )
    creative_set: str = proto.Field(
        proto.STRING,
        number=5,
        optional=True,
    )
    companion_creatives: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )


class InternalRedirectCreativeDetails(proto.Message):
    r"""A Creative hosted by Campaign Manager 360.

    Similar to third-party creatives, a Campaign Manager 360 tag is
    used to retrieve a creative asset. However, Campaign Manager 360
    tags are not sent to the user's browser. Instead, they are
    processed internally within the Google Marketing Platform
    system.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        locked_orientation (google.ads.admanager_v1.types.CreativeLockedOrientationEnum.CreativeLockedOrientation):
            Optional. A locked orientation for this
            creative to be displayed in.

            This field is a member of `oneof`_ ``_locked_orientation``.
        asset_size (google.ads.admanager_v1.types.Size):
            Output only. The asset size of an internal redirect
            creative. Note that this may differ from ``size`` if users
            set ``override_size`` to true.

            This field is a member of `oneof`_ ``_asset_size``.
        internal_redirect_url (str):
            Required. The internal redirect URL of the
            Campaign Manager 360 hosted creative. This
            attribute has a maximum length of 1024
            characters.

            This field is a member of `oneof`_ ``_internal_redirect_url``.
        override_size (bool):
            Optional. Allows the creative size to differ
            from the actual size specified in the internal
            redirect's url.

            This field is a member of `oneof`_ ``_override_size``.
        interstitial (bool):
            Optional. Whether this creative is
            interstitial.

            This field is a member of `oneof`_ ``_interstitial``.
        ssl_scan_result (google.ads.admanager_v1.types.CreativeSslScanResultEnum.CreativeSslScanResult):
            Output only. The SSL compatibility scan
            result of this creative.

            This field is a member of `oneof`_ ``_ssl_scan_result``.
        ssl_manual_override (google.ads.admanager_v1.types.CreativeSslOverrideEnum.CreativeSslOverride):
            Optional. The manual override for the SSL
            compatibility of this creative.

            This field is a member of `oneof`_ ``_ssl_manual_override``.
        third_party_impression_tracking_urls (MutableSequence[str]):
            Optional. Impression tracking URLs to ping
            when this creative is displayed.
    """

    locked_orientation: creative_enums.CreativeLockedOrientationEnum.CreativeLockedOrientation = proto.Field(
        proto.ENUM,
        number=1,
        optional=True,
        enum=creative_enums.CreativeLockedOrientationEnum.CreativeLockedOrientation,
    )
    asset_size: gaa_size.Size = proto.Field(
        proto.MESSAGE,
        number=5,
        optional=True,
        message=gaa_size.Size,
    )
    internal_redirect_url: str = proto.Field(
        proto.STRING,
        number=6,
        optional=True,
    )
    override_size: bool = proto.Field(
        proto.BOOL,
        number=7,
        optional=True,
    )
    interstitial: bool = proto.Field(
        proto.BOOL,
        number=2,
        optional=True,
    )
    ssl_scan_result: creative_enums.CreativeSslScanResultEnum.CreativeSslScanResult = (
        proto.Field(
            proto.ENUM,
            number=3,
            optional=True,
            enum=creative_enums.CreativeSslScanResultEnum.CreativeSslScanResult,
        )
    )
    ssl_manual_override: creative_enums.CreativeSslOverrideEnum.CreativeSslOverride = (
        proto.Field(
            proto.ENUM,
            number=4,
            optional=True,
            enum=creative_enums.CreativeSslOverrideEnum.CreativeSslOverride,
        )
    )
    third_party_impression_tracking_urls: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=8,
    )


class LegacyDfpCreativeDetails(proto.Message):
    r"""A Creative that isn't supported by Google DFP, but was
    migrated from DART. Creatives of this type cannot be created or
    modified.

    """


class ProgrammaticCreativeDetails(proto.Message):
    r"""A Creative used for programmatic trafficking. This creative
    will be auto-created with the right approval from the buyer.
    This creative cannot be created through the API. This creative
    can be updated.

    """


class RichMediaStudioCreativeDetails(proto.Message):
    r"""A Creative that is created by a Rich Media Studio. You cannot
    create this creative, but you can update some fields of this
    creative.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        locked_orientation (google.ads.admanager_v1.types.CreativeLockedOrientationEnum.CreativeLockedOrientation):
            Optional. A locked orientation for this
            creative to be displayed in.

            This field is a member of `oneof`_ ``_locked_orientation``.
        studio_creative_id (int):
            Output only. The creative ID as known by Rich
            Media Studio creative.

            This field is a member of `oneof`_ ``_studio_creative_id``.
        creative_format (google.ads.admanager_v1.types.RichMediaStudioCreativeFormatEnum.RichMediaStudioCreativeFormat):
            Optional. The creative format of the Rich
            Media Studio creative.

            This field is a member of `oneof`_ ``_creative_format``.
        total_file_size (int):
            Output only. The total size of all assets in
            bytes.

            This field is a member of `oneof`_ ``_total_file_size``.
        ad_tag_keys (MutableSequence[str]):
            Optional. Ad tag keys.
        custom_key_values (MutableSequence[str]):
            Optional. Custom key values.
        survey_url (str):
            Optional. The survey URL for this creative.

            This field is a member of `oneof`_ ``_survey_url``.
        all_impressions_url (str):
            Optional. The tracking URL to be triggered
            when an ad starts to play, whether Rich Media or
            backup content is displayed. Behaves like the
            /imp URL that DART used to track impressions.
            This URL can't exceed 1024 characters and must
            start with http:// or https://.

            This field is a member of `oneof`_ ``_all_impressions_url``.
        rich_media_impressions_url (str):
            Optional. The tracking URL to be triggered
            when any rich media artwork is displayed in an
            ad. Behaves like the /imp URL that DART used to
            track impressions. This URL can't exceed 1024
            characters and must start with http:// or
            https://.

            This field is a member of `oneof`_ ``_rich_media_impressions_url``.
        backup_image_impressions_url (str):
            Optional. The tracking URL to be triggered
            when the Rich Media backup image is served.

            This field is a member of `oneof`_ ``_backup_image_impressions_url``.
        override_css (str):
            Optional. The override CSS. You can put custom CSS code here
            to repair creative styling; e.g.
            ``tr td { background-color:#FBB; }``.

            This field is a member of `oneof`_ ``_override_css``.
        required_flash_plugin_version (str):
            Output only. The Flash plugin version required to view this
            creative; e.g. ``Flash 10.2/AS 3``.

            This field is a member of `oneof`_ ``_required_flash_plugin_version``.
        duration (google.protobuf.duration_pb2.Duration):
            Optional. The duration of the creative.

            This field is a member of `oneof`_ ``_duration``.
        billing_attribute (google.ads.admanager_v1.types.RichMediaStudioCreativeBillingAttributeEnum.RichMediaStudioCreativeBillingAttribute):
            Optional. The billing attribute associated
            with this creative.

            This field is a member of `oneof`_ ``_billing_attribute``.
        rich_media_studio_child_asset_properties (MutableSequence[google.ads.admanager_v1.types.RichMediaStudioChildAssetProperty]):
            Output only. Child assets associated with
            this creative.
        ssl_scan_result (google.ads.admanager_v1.types.CreativeSslScanResultEnum.CreativeSslScanResult):
            Output only. The SSL compatibility scan
            result of this creative.

            This field is a member of `oneof`_ ``_ssl_scan_result``.
        ssl_manual_override (google.ads.admanager_v1.types.CreativeSslOverrideEnum.CreativeSslOverride):
            Optional. The manual override for the SSL
            compatibility of this creative.

            This field is a member of `oneof`_ ``_ssl_manual_override``.
    """

    locked_orientation: creative_enums.CreativeLockedOrientationEnum.CreativeLockedOrientation = proto.Field(
        proto.ENUM,
        number=1,
        optional=True,
        enum=creative_enums.CreativeLockedOrientationEnum.CreativeLockedOrientation,
    )
    studio_creative_id: int = proto.Field(
        proto.INT64,
        number=3,
        optional=True,
    )
    creative_format: rich_media_studio_creative_format_enum.RichMediaStudioCreativeFormatEnum.RichMediaStudioCreativeFormat = proto.Field(
        proto.ENUM,
        number=4,
        optional=True,
        enum=rich_media_studio_creative_format_enum.RichMediaStudioCreativeFormatEnum.RichMediaStudioCreativeFormat,
    )
    total_file_size: int = proto.Field(
        proto.INT64,
        number=6,
        optional=True,
    )
    ad_tag_keys: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )
    custom_key_values: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=8,
    )
    survey_url: str = proto.Field(
        proto.STRING,
        number=9,
        optional=True,
    )
    all_impressions_url: str = proto.Field(
        proto.STRING,
        number=10,
        optional=True,
    )
    rich_media_impressions_url: str = proto.Field(
        proto.STRING,
        number=11,
        optional=True,
    )
    backup_image_impressions_url: str = proto.Field(
        proto.STRING,
        number=12,
        optional=True,
    )
    override_css: str = proto.Field(
        proto.STRING,
        number=13,
        optional=True,
    )
    required_flash_plugin_version: str = proto.Field(
        proto.STRING,
        number=14,
        optional=True,
    )
    duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=15,
        optional=True,
        message=duration_pb2.Duration,
    )
    billing_attribute: rich_media_studio_creative_billing_attribute_enum.RichMediaStudioCreativeBillingAttributeEnum.RichMediaStudioCreativeBillingAttribute = proto.Field(
        proto.ENUM,
        number=16,
        optional=True,
        enum=rich_media_studio_creative_billing_attribute_enum.RichMediaStudioCreativeBillingAttributeEnum.RichMediaStudioCreativeBillingAttribute,
    )
    rich_media_studio_child_asset_properties: MutableSequence[
        rich_media_studio_messages.RichMediaStudioChildAssetProperty
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=17,
        message=rich_media_studio_messages.RichMediaStudioChildAssetProperty,
    )
    ssl_scan_result: creative_enums.CreativeSslScanResultEnum.CreativeSslScanResult = (
        proto.Field(
            proto.ENUM,
            number=18,
            optional=True,
            enum=creative_enums.CreativeSslScanResultEnum.CreativeSslScanResult,
        )
    )
    ssl_manual_override: creative_enums.CreativeSslOverrideEnum.CreativeSslOverride = (
        proto.Field(
            proto.ENUM,
            number=19,
            optional=True,
            enum=creative_enums.CreativeSslOverrideEnum.CreativeSslOverride,
        )
    )


class SetTopBoxCreativeDetails(proto.Message):
    r"""A Creative that will be served into cable set-top boxes.
    There are no assets for this creative type, as they are hosted
    by external cable systems.

    Attributes:
        vast_info (google.ads.admanager_v1.types.VastInfo):
            Optional. Fields common to Video Ad Serving
            Template (VAST) creatives
    """

    vast_info: "VastInfo" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="VastInfo",
    )


class TemplateCreativeDetails(proto.Message):
    r"""A Creative that is created by the specified creative
    template.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        amp_destination_url (str):
            Optional. The AMP destination URL for this creative. This
            must be a valid URL, including the ``http://`` or
            ``https://`` scheme.

            This field is a member of `oneof`_ ``_amp_destination_url``.
        locked_orientation (google.ads.admanager_v1.types.CreativeLockedOrientationEnum.CreativeLockedOrientation):
            Optional. A locked orientation for this
            creative to be displayed in.

            This field is a member of `oneof`_ ``_locked_orientation``.
        destination_url (str):
            Optional. The URL that the user is directed to if they click
            on the creative. This attribute is required unless the
            ``destinationUrlType`` is ``NONE``, and has a maximum length
            of 1024 characters.

            This field is a member of `oneof`_ ``_destination_url``.
        destination_url_type (google.ads.admanager_v1.types.CreativeDestinationUrlTypeEnum.CreativeDestinationUrlType):
            Optional. The action that should be performed if the user
            clicks on the creative. This attribute defaults to
            ``CLICK_TO_WEB``.

            This field is a member of `oneof`_ ``_destination_url_type``.
    """

    amp_destination_url: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    locked_orientation: creative_enums.CreativeLockedOrientationEnum.CreativeLockedOrientation = proto.Field(
        proto.ENUM,
        number=2,
        optional=True,
        enum=creative_enums.CreativeLockedOrientationEnum.CreativeLockedOrientation,
    )
    destination_url: str = proto.Field(
        proto.STRING,
        number=18,
        optional=True,
    )
    destination_url_type: creative_enums.CreativeDestinationUrlTypeEnum.CreativeDestinationUrlType = proto.Field(
        proto.ENUM,
        number=19,
        optional=True,
        enum=creative_enums.CreativeDestinationUrlTypeEnum.CreativeDestinationUrlType,
    )


class ThirdPartyCreativeDetails(proto.Message):
    r"""A Creative that is served by a 3rd-party vendor.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        snippet (str):
            The HTML snippet that this creative delivers.

            This field is a member of `oneof`_ ``_snippet``.
        expanded_snippet (str):
            Output only. The HTML snippet that this
            creative delivers with macros expanded.

            This field is a member of `oneof`_ ``_expanded_snippet``.
        locked_orientation (google.ads.admanager_v1.types.CreativeLockedOrientationEnum.CreativeLockedOrientation):
            Optional. A locked orientation for this
            creative to be displayed in.

            This field is a member of `oneof`_ ``_locked_orientation``.
        ssl_scan_result (google.ads.admanager_v1.types.CreativeSslScanResultEnum.CreativeSslScanResult):
            Output only. The SSL compatibility scan
            result of this creative.

            This field is a member of `oneof`_ ``_ssl_scan_result``.
        ssl_manual_override (google.ads.admanager_v1.types.CreativeSslOverrideEnum.CreativeSslOverride):
            Optional. The manual override for the SSL
            compatibility of this creative.

            This field is a member of `oneof`_ ``_ssl_manual_override``.
        safe_frame_compatible (bool):
            Optional. Whether the Creative is compatible
            for SafeFrame rendering.

            This field is a member of `oneof`_ ``_safe_frame_compatible``.
        third_party_impression_tracking_urls (MutableSequence[str]):
            Optional. A list of impression tracking URLs
            to ping when this creative is displayed.
        amp_redirect_url (str):
            Optional. The URL of the AMP creative.

            This field is a member of `oneof`_ ``_amp_redirect_url``.
        destination_url (str):
            Optional. The URL that the user is directed to if they click
            on the creative. This attribute is required unless the
            ``destinationUrlType`` is ``NONE``, and has a maximum length
            of 1024 characters.

            This field is a member of `oneof`_ ``_destination_url``.
        destination_url_type (google.ads.admanager_v1.types.CreativeDestinationUrlTypeEnum.CreativeDestinationUrlType):
            Optional. The action that should be performed if the user
            clicks on the creative. This attribute defaults to
            ``CLICK_TO_WEB``.

            This field is a member of `oneof`_ ``_destination_url_type``.
    """

    snippet: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )
    expanded_snippet: str = proto.Field(
        proto.STRING,
        number=5,
        optional=True,
    )
    locked_orientation: creative_enums.CreativeLockedOrientationEnum.CreativeLockedOrientation = proto.Field(
        proto.ENUM,
        number=1,
        optional=True,
        enum=creative_enums.CreativeLockedOrientationEnum.CreativeLockedOrientation,
    )
    ssl_scan_result: creative_enums.CreativeSslScanResultEnum.CreativeSslScanResult = (
        proto.Field(
            proto.ENUM,
            number=2,
            optional=True,
            enum=creative_enums.CreativeSslScanResultEnum.CreativeSslScanResult,
        )
    )
    ssl_manual_override: creative_enums.CreativeSslOverrideEnum.CreativeSslOverride = (
        proto.Field(
            proto.ENUM,
            number=3,
            optional=True,
            enum=creative_enums.CreativeSslOverrideEnum.CreativeSslOverride,
        )
    )
    safe_frame_compatible: bool = proto.Field(
        proto.BOOL,
        number=6,
        optional=True,
    )
    third_party_impression_tracking_urls: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )
    amp_redirect_url: str = proto.Field(
        proto.STRING,
        number=8,
        optional=True,
    )
    destination_url: str = proto.Field(
        proto.STRING,
        number=10,
        optional=True,
    )
    destination_url_type: creative_enums.CreativeDestinationUrlTypeEnum.CreativeDestinationUrlType = proto.Field(
        proto.ENUM,
        number=11,
        optional=True,
        enum=creative_enums.CreativeDestinationUrlTypeEnum.CreativeDestinationUrlType,
    )


class VastRedirectCreativeDetails(proto.Message):
    r"""A Creative that points to an externally hosted VAST ad and is
    served via VAST XML as a VAST Wrapper.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        vast_xml_url (str):
            Required. The URL where the 3rd party VAST
            XML is hosted.

            This field is a member of `oneof`_ ``_vast_xml_url``.
        vast_redirect_type (google.ads.admanager_v1.types.VastRedirectTypeEnum.VastRedirectType):
            Required. The type of VAST ad that this
            redirects to.

            This field is a member of `oneof`_ ``_vast_redirect_type``.
        duration (google.protobuf.duration_pb2.Duration):
            Required. The duration of the VAST ad.
        vast_pricing_enabled (bool):
            Optional. Whether pricing information from
            the VAST response will be used during ad
            selection.

            This field is a member of `oneof`_ ``_vast_pricing_enabled``.
        programmatic_demand_source (bool):
            Optional. Whether this is a redirect to a
            programmatic demand source.

            This field is a member of `oneof`_ ``_programmatic_demand_source``.
        server_side_unwrapping_disabled (bool):
            Optional. Whether server-side unwrapping is
            disabled.

            This field is a member of `oneof`_ ``_server_side_unwrapping_disabled``.
        tracking_urls (MutableSequence[google.ads.admanager_v1.types.VideoTrackingUrl]):
            Optional. URLs that will be pinged when
            conversion events happen.
        vast_preview_url (str):
            Output only. An ad tag URL that will return a
            preview of the VAST XML response specific to
            this creative.

            This field is a member of `oneof`_ ``_vast_preview_url``.
        audio (bool):
            Optional. Whether the 3rd party VAST XML points to an audio
            ad. When true, ``size`` will always be 1x1.

            This field is a member of `oneof`_ ``_audio``.
        destination_url (str):
            Optional. The URL that the user is directed to if they click
            on the creative. This attribute is required unless the
            ``destinationUrlType`` is ``NONE``, and has a maximum length
            of 1024 characters.

            This field is a member of `oneof`_ ``_destination_url``.
        destination_url_type (google.ads.admanager_v1.types.CreativeDestinationUrlTypeEnum.CreativeDestinationUrlType):
            Optional. The action that should be performed if the user
            clicks on the creative. This attribute defaults to
            ``CLICK_TO_WEB``.

            This field is a member of `oneof`_ ``_destination_url_type``.
    """

    vast_xml_url: str = proto.Field(
        proto.STRING,
        number=22,
        optional=True,
    )
    vast_redirect_type: vast_redirect_type_enum.VastRedirectTypeEnum.VastRedirectType = proto.Field(
        proto.ENUM,
        number=4,
        optional=True,
        enum=vast_redirect_type_enum.VastRedirectTypeEnum.VastRedirectType,
    )
    duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=5,
        message=duration_pb2.Duration,
    )
    vast_pricing_enabled: bool = proto.Field(
        proto.BOOL,
        number=8,
        optional=True,
    )
    programmatic_demand_source: bool = proto.Field(
        proto.BOOL,
        number=9,
        optional=True,
    )
    server_side_unwrapping_disabled: bool = proto.Field(
        proto.BOOL,
        number=10,
        optional=True,
    )
    tracking_urls: MutableSequence[video_tracking_url.VideoTrackingUrl] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=12,
            message=video_tracking_url.VideoTrackingUrl,
        )
    )
    vast_preview_url: str = proto.Field(
        proto.STRING,
        number=16,
        optional=True,
    )
    audio: bool = proto.Field(
        proto.BOOL,
        number=21,
        optional=True,
    )
    destination_url: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    destination_url_type: creative_enums.CreativeDestinationUrlTypeEnum.CreativeDestinationUrlType = proto.Field(
        proto.ENUM,
        number=3,
        optional=True,
        enum=creative_enums.CreativeDestinationUrlTypeEnum.CreativeDestinationUrlType,
    )


class VideoCreativeDetails(proto.Message):
    r"""A Creative that contains Ad Manager hosted video ads and is
    served via VAST XML.

    Attributes:
        vast_info (google.ads.admanager_v1.types.VastInfo):
            Optional. Fields common to Video Ad Serving
            Template (VAST) creatives
    """

    vast_info: "VastInfo" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="VastInfo",
    )


class VideoRedirectCreativeDetails(proto.Message):
    r"""A Creative that contains externally hosted video ads and is
    served via VAST XML.

    Attributes:
        vast_info (google.ads.admanager_v1.types.VastInfo):
            Optional. Fields common to Video Ad Serving
            Template (VAST) creatives
    """

    vast_info: "VastInfo" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="VastInfo",
    )


class VastInfo(proto.Message):
    r"""Fields common to Video Ad Serving Template (VAST) creatives.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        duration (google.protobuf.duration_pb2.Duration):
            Optional. The expected duration of this
            creative.
        allow_duration_override (bool):
            Optional. Allows the creative duration to
            differ from the actual asset durations.

            This field is a member of `oneof`_ ``_allow_duration_override``.
        tracking_urls (MutableSequence[google.ads.admanager_v1.types.VideoTrackingUrl]):
            Optional. URLs that will be pinged when
            conversion events happen.
        custom_parameters (str):
            Optional. A comma separated key=value list of parameters
            that will be supplied to the creative, written into the VAST
            ``AdParameters`` node.

            This field is a member of `oneof`_ ``_custom_parameters``.
        ad_id (str):
            Optional. The ad id associated with the video as defined by
            the ``adIdType`` registry. This field is required if
            ``adIdType`` is not ``NONE``.

            This field is a member of `oneof`_ ``_ad_id``.
        ad_id_type (google.ads.admanager_v1.types.VastAdIdTypeEnum.VastAdIdType):
            Optional. The registry which the ad id of this creative
            belongs to. This field defaults to ``NONE``.

            This field is a member of `oneof`_ ``_ad_id_type``.
        skippable_ad_type (google.ads.admanager_v1.types.SkippableAdTypeEnum.SkippableAdType):
            Optional. The type of skippable ad.

            This field is a member of `oneof`_ ``_skippable_ad_type``.
        vast_preview_url (str):
            Output only. An ad tag URL that will return a
            preview of the VAST XML response specific to
            this creative.

            This field is a member of `oneof`_ ``_vast_preview_url``.
        creative_set_display_name (str):
            Output only. The display name of the creative
            set.

            This field is a member of `oneof`_ ``_creative_set_display_name``.
        creative_set (str):
            Output only. The resource name of the creative set. Format:
            "networks/{network_code}/creativeSets/{creative_set_id}".

            This field is a member of `oneof`_ ``_creative_set``.
        destination_url (str):
            Optional. The URL that the user is directed to if they click
            on the creative. This attribute is required unless the
            ``destinationUrlType`` is ``NONE``, and has a maximum length
            of 1024 characters.

            This field is a member of `oneof`_ ``_destination_url``.
        destination_url_type (google.ads.admanager_v1.types.CreativeDestinationUrlTypeEnum.CreativeDestinationUrlType):
            Optional. The action that should be performed if the user
            clicks on the creative. This attribute defaults to
            ``CLICK_TO_WEB``.

            This field is a member of `oneof`_ ``_destination_url_type``.
        companion_creatives (MutableSequence[str]):
            Optional. The companion creatives that are associated with
            this creative. Format:
            "networks/{network_code}/creatives/{creative_id}".
    """

    duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=1,
        message=duration_pb2.Duration,
    )
    allow_duration_override: bool = proto.Field(
        proto.BOOL,
        number=2,
        optional=True,
    )
    tracking_urls: MutableSequence[video_tracking_url.VideoTrackingUrl] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message=video_tracking_url.VideoTrackingUrl,
        )
    )
    custom_parameters: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )
    ad_id: str = proto.Field(
        proto.STRING,
        number=5,
        optional=True,
    )
    ad_id_type: creative_enums.VastAdIdTypeEnum.VastAdIdType = proto.Field(
        proto.ENUM,
        number=6,
        optional=True,
        enum=creative_enums.VastAdIdTypeEnum.VastAdIdType,
    )
    skippable_ad_type: skippable_ad_type_enum.SkippableAdTypeEnum.SkippableAdType = (
        proto.Field(
            proto.ENUM,
            number=7,
            optional=True,
            enum=skippable_ad_type_enum.SkippableAdTypeEnum.SkippableAdType,
        )
    )
    vast_preview_url: str = proto.Field(
        proto.STRING,
        number=8,
        optional=True,
    )
    creative_set_display_name: str = proto.Field(
        proto.STRING,
        number=14,
        optional=True,
    )
    creative_set: str = proto.Field(
        proto.STRING,
        number=15,
        optional=True,
    )
    destination_url: str = proto.Field(
        proto.STRING,
        number=16,
        optional=True,
    )
    destination_url_type: creative_enums.CreativeDestinationUrlTypeEnum.CreativeDestinationUrlType = proto.Field(
        proto.ENUM,
        number=17,
        optional=True,
        enum=creative_enums.CreativeDestinationUrlTypeEnum.CreativeDestinationUrlType,
    )
    companion_creatives: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=18,
    )


class BuyerPlacementConfig(proto.Message):
    r"""Represents the buyer placement configuration for a creative.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        placement_id (str):
            Optional. The ID of the buyer placement.

            This field is a member of `oneof`_ ``_placement_id``.
        placement_display_name (str):
            Optional. The name of the buyer placement.

            This field is a member of `oneof`_ ``_placement_display_name``.
    """

    placement_id: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    placement_display_name: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
