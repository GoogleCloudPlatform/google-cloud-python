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

from google.ads.admanager_v1.types import dai_session_enums

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "DaiSession",
    },
)


class DaiSession(proto.Message):
    r"""Representation of an individual Dynamic Ad Insertion (DAI) session
    watching a [LiveStream][google.ads.admanager.v1.LiveStream] resource
    or VOD [Content][google.ads.admanager.v1.Content] resource. Use the
    Stream Activity Monitor (SAM) on the Google Ad Manager UI to look up
    this session. For details, see `Locate a DAI session ID or debug
    key <https://support.google.com/admanager/answer/7257678>`__.

    Attributes:
        name (str):
            Identifier. The resource name of the ``DaiSession``.
        creation_context (google.ads.admanager_v1.types.DaiSession.CreationContext):
            Output only. Context data to create the DAI
            session.
        slate (google.ads.admanager_v1.types.DaiSession.Creative):
            Output only. Slate creative to use in the DAI
            session for unfilled ad durations.
        ad_selections (MutableMapping[int, google.ads.admanager_v1.types.DaiSession.AdSelection]):
            Output only. The ad requests, ad responses
            and nested ads in the DAI session.
        ad_pods (MutableMapping[int, google.ads.admanager_v1.types.DaiSession.AdPod]):
            Output only. All decisioned ad pods for this
            session, disregarding serving status. Keyed by a
            unique ID to reference an ad pod from a
            different submessage.
        ad_breaks (MutableMapping[int, google.ads.admanager_v1.types.DaiSession.AdBreak]):
            Output only. All DAI ad breaks for this
            session. Contains information such as ad
            duration, slate duration, and various ad
            statuses. Keyed by a unique ID to reference an
            ad break from a different submessage.
        findings (MutableSequence[google.ads.admanager_v1.types.DaiSession.Finding]):
            Output only. Information about errors or
            notable discoveries that occurred during a
            session.
        session_duration (google.protobuf.duration_pb2.Duration):
            Output only. The duration of the DAI session,
            calculated as the difference between the
            timestamp of DAI's latest recorded event and the
            timestamp of the session create request.
    """

    class CreationContext(proto.Message):
        r"""Context data to create the DAI session.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            linear_info (google.ads.admanager_v1.types.DaiSession.CreationContext.LinearInfo):
                Output only. The
                [LiveStream][google.ads.admanager.v1.LiveStream] resource in
                the stream request that creates the DAI session.

                This field is a member of `oneof`_ ``content_info``.
            vod_info (google.ads.admanager_v1.types.DaiSession.CreationContext.VodInfo):
                Output only. The [Content][google.ads.admanager.v1.Content]
                resource in the stream request that creates the DAI session.

                This field is a member of `oneof`_ ``content_info``.
            debug_key (str):
                Output only. The string the ``dai-sam-id`` parameter sets in
                the DAI stream request. For details, see `Locate a DAI
                session ID or debug
                key <https://support.google.com/admanager/answer/7257678>`__.

                This field is a member of `oneof`_ ``_debug_key``.
            content_title (str):
                Output only. The
                [LiveStream.display_name][google.ads.admanager.v1.LiveStream.display_name]
                field or
                [Content.display_name][google.ads.admanager.v1.Content.display_name]
                field associated with the DAI session.

                This field is a member of `oneof`_ ``_content_title``.
            session_title (str):
                Output only. The string the ``session_title`` parameter sets
                in the DAI stream request. For details, see
                `CreateStreamOptions </ad-manager/dynamic-ad-insertion/api/pod-serving/reference/vod#createstreamoptions>`__.

                This field is a member of `oneof`_ ``_session_title``.
            stream_create_request (google.ads.admanager_v1.types.DaiSession.HttpRequest):
                Output only. The HTTP request creating the DAI session. For
                details, see `Linear
                API </ad-manager/dynamic-ad-insertion/api/full-service/reference/live#method_stream>`__,
                `VOD
                API </ad-manager/dynamic-ad-insertion/api/full-service/reference/vod#method_stream>`__,
                `pod serving live
                API </ad-manager/dynamic-ad-insertion/api/pod-serving/reference/live#method_stream>`__
                and `pod serving VOD
                API </ad-manager/dynamic-ad-insertion/api/pod-serving/reference/vod#method_create_stream>`__.
            stitching_type (google.ads.admanager_v1.types.StitchingTypeEnum.StitchingType):
                Output only. Whether the stream request is for `Full-service
                DAI </ad-manager/dynamic-ad-insertion/full-service>`__ or
                `Pod
                serving </ad-manager/dynamic-ad-insertion/pod-serving>`__.

                This field is a member of `oneof`_ ``_stitching_type``.
            reporting_type (google.ads.admanager_v1.types.ReportingTypeEnum.ReportingType):
                Output only. Whether ad tracking URLs are pinged on the
                client side or server side. If IMA SDK is used to make the
                stream requests, IMA SDK pings the ad tracking URLs on the
                client side. For server-side beaconing, see `Integrate with
                DAI using server-side beaconing
                (SSB) <https://support.google.com/admanager/answer/7299051>`__.

                This field is a member of `oneof`_ ``_reporting_type``.
            interstitial_enabled (bool):
                Output only. Whether the parameter ``dai-istl`` on the
                stream request is set to true. This parameter is only
                accepted for
                [LiveStream][google.ads.admanager.v1.LiveStream] resources
                with the
                [dynamic_ad_insertion_type][google.ads.admanager.v1.LiveStream.dynamic_ad_insertion_type]
                field set to
                [DynamicAdInsertionType.LINEAR][google.ads.admanager.v1.DynamicAdInsertionTypeEnum.DynamicAdInsertionType.LINEAR]
                value.

                This field is a member of `oneof`_ ``_interstitial_enabled``.
        """

        class VodInfo(proto.Message):
            r"""The VOD [Content][google.ads.admanager.v1.Content] resource in the
            stream request that creates the DAI session.


            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                content (str):
                    Output only. The
                    [name][google.ads.admanager.v1.Content.name] field of the
                    VOD [Content][google.ads.admanager.v1.Content] resource.

                    This field is a member of `oneof`_ ``_content``.
                cms_id (int):
                    Output only. The identifier of the content source from which
                    Google Ad Manager ingested the
                    [Content][google.ads.admanager.v1.Content] resource
                    associated with this session. For more information, see
                    `Create a content source for video on
                    demand <https://support.google.com/admanager/answer/7064112>`__.

                    This field is a member of `oneof`_ ``_cms_id``.
                vid (str):
                    Output only. The video ID of the
                    [Content][google.ads.admanager.v1.Content] resource that
                    this session is associated with. This value is the same as
                    the
                    [CmsContent.cms_content_id][google.ads.admanager.v1.CmsContent.cms_content_id]
                    field. For details, see `Content ingestion and best
                    practices <https://support.google.com/admanager/answer/6057894>`__.

                    This field is a member of `oneof`_ ``_vid``.
                cue_points (MutableSequence[int]):
                    Output only. The cue points detected in the
                    ingested VOD content manifest. Stored in
                    milliseconds starting from the beginning of the
                    content.
                content_duration (google.protobuf.duration_pb2.Duration):
                    Output only. The VOD
                    [Content.duration][google.ads.admanager.v1.Content.duration]
                    field. Represents the duration of the content without ads.
            """

            content: str = proto.Field(
                proto.STRING,
                number=3,
                optional=True,
            )
            cms_id: int = proto.Field(
                proto.INT64,
                number=1,
                optional=True,
            )
            vid: str = proto.Field(
                proto.STRING,
                number=2,
                optional=True,
            )
            cue_points: MutableSequence[int] = proto.RepeatedField(
                proto.INT64,
                number=4,
            )
            content_duration: duration_pb2.Duration = proto.Field(
                proto.MESSAGE,
                number=5,
                message=duration_pb2.Duration,
            )

        class LinearInfo(proto.Message):
            r"""The [LiveStream][google.ads.admanager.v1.LiveStream] resource in the
            stream request that creates the DAI session.


            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                live_stream (str):
                    Output only. The
                    [name][google.ads.admanager.v1.LiveStream.name] field of the
                    [LiveStream][google.ads.admanager.v1.LiveStream] resource.

                    This field is a member of `oneof`_ ``_live_stream``.
                asset_key (str):
                    Output only. The
                    [LiveStream.asset_key][google.ads.admanager.v1.LiveStream.asset_key]
                    field. Google Ad Manager only generates this field for
                    livestreams with the
                    [dynamic_ad_insertion_type][google.ads.admanager.v1.LiveStream.dynamic_ad_insertion_type]
                    field set to
                    [DynamicAdInsertionType.LINEAR][google.ads.admanager.v1.DynamicAdInsertionTypeEnum.DynamicAdInsertionType.LINEAR]
                    value.

                    This field is a member of `oneof`_ ``_asset_key``.
                custom_asset_key (str):
                    Output only. The
                    [LiveStream.custom_asset_key][google.ads.admanager.v1.LiveStream.custom_asset_key]
                    field. This field is only populated for livestreams with the
                    [dynamic_ad_insertion_type][google.ads.admanager.v1.LiveStream.dynamic_ad_insertion_type]
                    field set to
                    [DynamicAdInsertionType.POD_SERVING_MANIFEST][google.ads.admanager.v1.DynamicAdInsertionTypeEnum.DynamicAdInsertionType.POD_SERVING_MANIFEST]
                    value or
                    [DynamicAdInsertionType.POD_SERVING_REDIRECT][google.ads.admanager.v1.DynamicAdInsertionTypeEnum.DynamicAdInsertionType.POD_SERVING_REDIRECT]
                    value.

                    This field is a member of `oneof`_ ``_custom_asset_key``.
                prefetch_enabled (bool):
                    Output only. Whether the
                    [LiveStream.prefetch_enabled][google.ads.admanager.v1.LiveStream.prefetch_enabled]
                    field is set to true.

                    This field is a member of `oneof`_ ``_prefetch_enabled``.
                pod_trimming_enabled (bool):
                    Output only. Whether ad pod trimming is
                    enabled for the DAI session.

                    This field is a member of `oneof`_ ``_pod_trimming_enabled``.
                pod_trim_tolerance (google.protobuf.duration_pb2.Duration):
                    Optional. The maximum duration allowed to be
                    trimmed from an ad pod before whole ads are
                    dropped. This field is only populated when pod
                    trimming is enabled.

                    This field is a member of `oneof`_ ``_pod_trim_tolerance``.
                event_start_time (google.protobuf.timestamp_pb2.Timestamp):
                    The
                    [LiveStream.start_time][google.ads.admanager.v1.LiveStream.start_time]
                    field.
                event_end_time (google.protobuf.timestamp_pb2.Timestamp):
                    Output only. The
                    [LiveStream.end_time][google.ads.admanager.v1.LiveStream.end_time]
                    field.
            """

            live_stream: str = proto.Field(
                proto.STRING,
                number=5,
                optional=True,
            )
            asset_key: str = proto.Field(
                proto.STRING,
                number=1,
                optional=True,
            )
            custom_asset_key: str = proto.Field(
                proto.STRING,
                number=2,
                optional=True,
            )
            prefetch_enabled: bool = proto.Field(
                proto.BOOL,
                number=3,
                optional=True,
            )
            pod_trimming_enabled: bool = proto.Field(
                proto.BOOL,
                number=4,
                optional=True,
            )
            pod_trim_tolerance: duration_pb2.Duration = proto.Field(
                proto.MESSAGE,
                number=8,
                optional=True,
                message=duration_pb2.Duration,
            )
            event_start_time: timestamp_pb2.Timestamp = proto.Field(
                proto.MESSAGE,
                number=6,
                message=timestamp_pb2.Timestamp,
            )
            event_end_time: timestamp_pb2.Timestamp = proto.Field(
                proto.MESSAGE,
                number=7,
                message=timestamp_pb2.Timestamp,
            )

        linear_info: "DaiSession.CreationContext.LinearInfo" = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="content_info",
            message="DaiSession.CreationContext.LinearInfo",
        )
        vod_info: "DaiSession.CreationContext.VodInfo" = proto.Field(
            proto.MESSAGE,
            number=3,
            oneof="content_info",
            message="DaiSession.CreationContext.VodInfo",
        )
        debug_key: str = proto.Field(
            proto.STRING,
            number=8,
            optional=True,
        )
        content_title: str = proto.Field(
            proto.STRING,
            number=10,
            optional=True,
        )
        session_title: str = proto.Field(
            proto.STRING,
            number=9,
            optional=True,
        )
        stream_create_request: "DaiSession.HttpRequest" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="DaiSession.HttpRequest",
        )
        stitching_type: dai_session_enums.StitchingTypeEnum.StitchingType = proto.Field(
            proto.ENUM,
            number=4,
            optional=True,
            enum=dai_session_enums.StitchingTypeEnum.StitchingType,
        )
        reporting_type: dai_session_enums.ReportingTypeEnum.ReportingType = proto.Field(
            proto.ENUM,
            number=5,
            optional=True,
            enum=dai_session_enums.ReportingTypeEnum.ReportingType,
        )
        interstitial_enabled: bool = proto.Field(
            proto.BOOL,
            number=6,
            optional=True,
        )

    class AdSelection(proto.Message):
        r"""The ad requests, ad response, and nested ads in the DAI
        session.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            type_ (google.ads.admanager_v1.types.AdResponseTypeEnum.AdResponseType):
                Output only. Response type of the parent ad
                request.

                This field is a member of `oneof`_ ``_type``.
            ad_request (google.ads.admanager_v1.types.DaiSession.AdSelection.AdRequest):
                Output only. Top-level ad request.
        """

        class AdRequest(proto.Message):
            r"""Top-level ad request.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                ad_request_key (int):
                    Output only. Ad request ID.

                    This field is a member of `oneof`_ ``_ad_request_key``.
                http_request (google.ads.admanager_v1.types.DaiSession.HttpRequest):
                    Output only. The HTTP request of the ad
                    request.
                child_requests (MutableSequence[google.ads.admanager_v1.types.DaiSession.AdSelection.AdRequest]):
                    Output only. Ad requests made to follow
                    redirects or unwrap a previous VMAP or VAST
                    wrapper ad response.
                ad_tag (str):
                    Output only. The ad request URL.

                    This field is a member of `oneof`_ ``_ad_tag``.
                effective_ad_request_url (str):
                    Output only. The effective ad request URL header value on
                    the ad response. This value is only populated for VMAP ad
                    requests when video playlist internal redirects are enabled.
                    For details, see `Internal redirect to Google Campaign
                    Manager
                    360 <https://support.google.com/admanager/answer/9580500>`__.

                    This field is a member of `oneof`_ ``_effective_ad_request_url``.
            """

            ad_request_key: int = proto.Field(
                proto.INT64,
                number=1,
                optional=True,
            )
            http_request: "DaiSession.HttpRequest" = proto.Field(
                proto.MESSAGE,
                number=2,
                message="DaiSession.HttpRequest",
            )
            child_requests: MutableSequence["DaiSession.AdSelection.AdRequest"] = (
                proto.RepeatedField(
                    proto.MESSAGE,
                    number=3,
                    message="DaiSession.AdSelection.AdRequest",
                )
            )
            ad_tag: str = proto.Field(
                proto.STRING,
                number=4,
                optional=True,
            )
            effective_ad_request_url: str = proto.Field(
                proto.STRING,
                number=5,
                optional=True,
            )

        type_: dai_session_enums.AdResponseTypeEnum.AdResponseType = proto.Field(
            proto.ENUM,
            number=1,
            optional=True,
            enum=dai_session_enums.AdResponseTypeEnum.AdResponseType,
        )
        ad_request: "DaiSession.AdSelection.AdRequest" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="DaiSession.AdSelection.AdRequest",
        )

    class AdPod(proto.Message):
        r"""Information about a single decisioned ad pod in this session.
        This message pertains to the smallest unit of ads to insert in a
        session, and might be a pod fragment.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            requested_break_type (google.ads.admanager_v1.types.BreakTypeEnum.BreakType):
                Output only. Type of ad break this ad pod was
                decisioned for.

                This field is a member of `oneof`_ ``_requested_break_type``.
            ad_request_key (int):
                Output only. Ad request ID that links to the
                ad request that resulted in this ad pod.

                This field is a member of `oneof`_ ``_ad_request_key``.
            creatives (MutableMapping[int, google.ads.admanager_v1.types.DaiSession.Creative]):
                Output only. The creatives in this ad pod.
                Keyed by a unique ID used to reference this
                creative from a different submessage.
            prefetch_stage (google.ads.admanager_v1.types.PrefetchStageTypeEnum.PrefetchStageType):
                Output only. Indicates the prefetch stage for this ad pod.
                If prefetch is not enabled this stage is set to the
                [PrefetchStageType.DISABLED][google.ads.admanager.v1.PrefetchStageTypeEnum.PrefetchStageType.DISABLED]
                value.

                This field is a member of `oneof`_ ``_prefetch_stage``.
            ad_break_id (str):
                Output only. Publisher-provided or DAI-generated break ID
                for the `Ad break
                API </ad-manager/dynamic-ad-insertion/api/ad-break>`__ or
                `pod serving
                API </ad-manager/dynamic-ad-insertion/pod-serving>`__.

                This field is a member of `oneof`_ ``_ad_break_id``.
            label (str):
                Output only. Descriptive label for this ad
                pod, used to distinguish ad pods from one
                another in this session. e.g. "midroll-1", "2".

                This field is a member of `oneof`_ ``_label``.
        """

        requested_break_type: dai_session_enums.BreakTypeEnum.BreakType = proto.Field(
            proto.ENUM,
            number=1,
            optional=True,
            enum=dai_session_enums.BreakTypeEnum.BreakType,
        )
        ad_request_key: int = proto.Field(
            proto.INT64,
            number=2,
            optional=True,
        )
        creatives: MutableMapping[int, "DaiSession.Creative"] = proto.MapField(
            proto.INT64,
            proto.MESSAGE,
            number=3,
            message="DaiSession.Creative",
        )
        prefetch_stage: dai_session_enums.PrefetchStageTypeEnum.PrefetchStageType = (
            proto.Field(
                proto.ENUM,
                number=4,
                optional=True,
                enum=dai_session_enums.PrefetchStageTypeEnum.PrefetchStageType,
            )
        )
        ad_break_id: str = proto.Field(
            proto.STRING,
            number=5,
            optional=True,
        )
        label: str = proto.Field(
            proto.STRING,
            number=6,
            optional=True,
        )

    class AdBreak(proto.Message):
        r"""Information about an ad break in this session. Includes
        statuses such as ad and slate durations.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            linear (google.ads.admanager_v1.types.DaiSession.AdBreak.LinearBreak):
                Output only. Information on the break for a
                linear session.

                This field is a member of `oneof`_ ``stream_type_info``.
            vod (google.ads.admanager_v1.types.DaiSession.AdBreak.VodBreak):
                Output only. Information on the break for a
                VOD session.

                This field is a member of `oneof`_ ``stream_type_info``.
            pod_keys (MutableSequence[int]):
                Output only. Ad pod ID that links to one or
                more decisioned ad pods for this break. Most
                types of sessions will have a single pod key,
                but in the case of prefetched pods there will be
                two pod keys.
            ad_break_id (str):
                Output only. Publisher-provided or DAI-generated break ID
                for the `Ad break
                API </ad-manager/dynamic-ad-insertion/api/ad-break>`__ or
                `pod serving
                API </ad-manager/dynamic-ad-insertion/pod-serving>`__.

                This field is a member of `oneof`_ ``_ad_break_id``.
            break_type (google.ads.admanager_v1.types.BreakTypeEnum.BreakType):
                Output only. Type of break this represents.

                This field is a member of `oneof`_ ``_break_type``.
            break_sequence (int):
                Output only. The index of this ad break in
                the session.

                This field is a member of `oneof`_ ``_break_sequence``.
            served_ads_duration (google.protobuf.duration_pb2.Duration):
                Output only. The duration of ads that were
                inserted for this break.
            executed_break_duration (google.protobuf.duration_pb2.Duration):
                Output only. The total duration of the break
                as it was served by DAI. In VOD, this value is
                the duration of ads inserted in between content.
                In linear, this value is the duration between
                cue out and cue in.
            tracking_pings (MutableMapping[int, google.ads.admanager_v1.types.DaiSession.AdBreak.TrackingPing]):
                Output only. Tracking pings that were issued
                for this break. Keyed by a unique ID to
                reference this tracking ping from a different
                submessage.
        """

        class VodBreak(proto.Message):
            r"""Represents Video on Demand related break information.

            Attributes:
                time_offset (google.protobuf.duration_pb2.Duration):
                    Output only. The time difference between the
                    start of this break and the start of the
                    session. Includes the time for any preceding ad
                    breaks.
            """

            time_offset: duration_pb2.Duration = proto.Field(
                proto.MESSAGE,
                number=1,
                message=duration_pb2.Duration,
            )

        class LinearBreak(proto.Message):
            r"""Represents linear session related break information.

            Attributes:
                break_start_time (google.protobuf.timestamp_pb2.Timestamp):
                    Output only. The timestamp of when the break
                    started.
                expected_break_duration (google.protobuf.duration_pb2.Duration):
                    Output only. The duration of the placement
                    opportunity associated with the break.
                slate_duration (google.protobuf.duration_pb2.Duration):
                    Output only. The duration of slate that was
                    inserted for this break.
                underlying_duration (google.protobuf.duration_pb2.Duration):
                    Output only. The duration of underlying
                    content that was inserted for this break.
            """

            break_start_time: timestamp_pb2.Timestamp = proto.Field(
                proto.MESSAGE,
                number=3,
                message=timestamp_pb2.Timestamp,
            )
            expected_break_duration: duration_pb2.Duration = proto.Field(
                proto.MESSAGE,
                number=4,
                message=duration_pb2.Duration,
            )
            slate_duration: duration_pb2.Duration = proto.Field(
                proto.MESSAGE,
                number=5,
                message=duration_pb2.Duration,
            )
            underlying_duration: duration_pb2.Duration = proto.Field(
                proto.MESSAGE,
                number=6,
                message=duration_pb2.Duration,
            )

        class TrackingPing(proto.Message):
            r"""Information about a tracking ping issued for a break.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                original_tracking_event_id (str):
                    Output only. A unique ID for this tracking
                    event, which is the ID3 tag in client-side
                    reporting.

                    This field is a member of `oneof`_ ``_original_tracking_event_id``.
                request (google.ads.admanager_v1.types.DaiSession.HttpRequest):
                    Output only. The HTTP request made to the ad
                    server for this tracking ping.
            """

            original_tracking_event_id: str = proto.Field(
                proto.STRING,
                number=4,
                optional=True,
            )
            request: "DaiSession.HttpRequest" = proto.Field(
                proto.MESSAGE,
                number=2,
                message="DaiSession.HttpRequest",
            )

        linear: "DaiSession.AdBreak.LinearBreak" = proto.Field(
            proto.MESSAGE,
            number=7,
            oneof="stream_type_info",
            message="DaiSession.AdBreak.LinearBreak",
        )
        vod: "DaiSession.AdBreak.VodBreak" = proto.Field(
            proto.MESSAGE,
            number=8,
            oneof="stream_type_info",
            message="DaiSession.AdBreak.VodBreak",
        )
        pod_keys: MutableSequence[int] = proto.RepeatedField(
            proto.INT64,
            number=1,
        )
        ad_break_id: str = proto.Field(
            proto.STRING,
            number=2,
            optional=True,
        )
        break_type: dai_session_enums.BreakTypeEnum.BreakType = proto.Field(
            proto.ENUM,
            number=3,
            optional=True,
            enum=dai_session_enums.BreakTypeEnum.BreakType,
        )
        break_sequence: int = proto.Field(
            proto.INT64,
            number=4,
            optional=True,
        )
        served_ads_duration: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=5,
            message=duration_pb2.Duration,
        )
        executed_break_duration: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=6,
            message=duration_pb2.Duration,
        )
        tracking_pings: MutableMapping[int, "DaiSession.AdBreak.TrackingPing"] = (
            proto.MapField(
                proto.INT64,
                proto.MESSAGE,
                number=9,
                message="DaiSession.AdBreak.TrackingPing",
            )
        )

    class HttpRequest(proto.Message):
        r"""An HTTP request made by DAI.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            request_time (google.protobuf.timestamp_pb2.Timestamp):
                Output only. The time when the request was
                made.
            latency (google.protobuf.duration_pb2.Duration):
                Output only. How long the request took to
                complete.
            url (str):
                Output only. The URL sent in the request.

                This field is a member of `oneof`_ ``_url``.
            user_agent (str):
                Output only. The user agent sent with the
                request.

                This field is a member of `oneof`_ ``_user_agent``.
            response_code (int):
                Output only. The HTTP response code.

                This field is a member of `oneof`_ ``_response_code``.
            response_body (str):
                Output only. The full response body.

                This field is a member of `oneof`_ ``_response_body``.
        """

        request_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=1,
            message=timestamp_pb2.Timestamp,
        )
        latency: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=2,
            message=duration_pb2.Duration,
        )
        url: str = proto.Field(
            proto.STRING,
            number=3,
            optional=True,
        )
        user_agent: str = proto.Field(
            proto.STRING,
            number=4,
            optional=True,
        )
        response_code: int = proto.Field(
            proto.INT32,
            number=5,
            optional=True,
        )
        response_body: str = proto.Field(
            proto.STRING,
            number=6,
            optional=True,
        )

    class Creative(proto.Message):
        r"""Information about a single creative.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            id_type (google.ads.admanager_v1.types.CreativeIdTypeEnum.CreativeIdType):
                Output only. The type of ID that is used to
                identify this creative.

                This field is a member of `oneof`_ ``_id_type``.
            id_value (str):
                Output only. The value for the given ID type.

                This field is a member of `oneof`_ ``_id_value``.
            ad_system (str):
                Output only. The ad system that provided this
                creative.

                This field is a member of `oneof`_ ``_ad_system``.
            duration (google.protobuf.duration_pb2.Duration):
                Output only. Duration of the creative.
            pod_sequence (int):
                Output only. The index at which this creative
                appeared in the ad pod.

                This field is a member of `oneof`_ ``_pod_sequence``.
            vast_infos (MutableSequence[google.ads.admanager_v1.types.DaiSession.Creative.VastInfo]):
                Output only. The VAST infos that resulted in
                this creative.
            ad_buffet (bool):
                Output only. Whether this creative was from
                ad buffet.

                This field is a member of `oneof`_ ``_ad_buffet``.
        """

        class VastInfo(proto.Message):
            r"""Details about a single VAST info.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                ad_system (str):
                    Output only. Value of
                    VAST/Ad/InLine/AdSystem.

                    This field is a member of `oneof`_ ``_ad_system``.
                ad_system_version (str):
                    Output only. Version attribute from
                    VAST/Ad/InLine/AdSystem.

                    This field is a member of `oneof`_ ``_ad_system_version``.
                ad_title (str):
                    Output only. Value of VAST/Ad/InLine/AdTitle.

                    This field is a member of `oneof`_ ``_ad_title``.
                description (str):
                    Output only. Value of
                    VAST/Ad/InLine/Description.

                    This field is a member of `oneof`_ ``_description``.
                creative_id (str):
                    Output only. The ``id`` attribute from
                    VAST/Ad/InLine/Creatives/Creative.

                    This field is a member of `oneof`_ ``_creative_id``.
            """

            ad_system: str = proto.Field(
                proto.STRING,
                number=1,
                optional=True,
            )
            ad_system_version: str = proto.Field(
                proto.STRING,
                number=2,
                optional=True,
            )
            ad_title: str = proto.Field(
                proto.STRING,
                number=3,
                optional=True,
            )
            description: str = proto.Field(
                proto.STRING,
                number=4,
                optional=True,
            )
            creative_id: str = proto.Field(
                proto.STRING,
                number=5,
                optional=True,
            )

        id_type: dai_session_enums.CreativeIdTypeEnum.CreativeIdType = proto.Field(
            proto.ENUM,
            number=1,
            optional=True,
            enum=dai_session_enums.CreativeIdTypeEnum.CreativeIdType,
        )
        id_value: str = proto.Field(
            proto.STRING,
            number=2,
            optional=True,
        )
        ad_system: str = proto.Field(
            proto.STRING,
            number=3,
            optional=True,
        )
        duration: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=4,
            message=duration_pb2.Duration,
        )
        pod_sequence: int = proto.Field(
            proto.INT32,
            number=5,
            optional=True,
        )
        vast_infos: MutableSequence["DaiSession.Creative.VastInfo"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=6,
                message="DaiSession.Creative.VastInfo",
            )
        )
        ad_buffet: bool = proto.Field(
            proto.BOOL,
            number=7,
            optional=True,
        )

    class Finding(proto.Message):
        r"""Information about errors or notable discoveries that occurred
        during a session.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            pod_finding (google.ads.admanager_v1.types.DaiSession.Finding.PodFinding):
                Output only. A finding related to building an
                ad pod.

                This field is a member of `oneof`_ ``type``.
            slate_finding (google.ads.admanager_v1.types.DaiSession.Finding.SlateFinding):
                Output only. A finding related to the slate
                creative.

                This field is a member of `oneof`_ ``type``.
            ad_break_finding (google.ads.admanager_v1.types.DaiSession.Finding.AdBreakFinding):
                Output only. A finding related to an ad
                break.

                This field is a member of `oneof`_ ``type``.
            tracking_finding (google.ads.admanager_v1.types.DaiSession.Finding.TrackingPingFinding):
                Output only. A finding related to a tracking
                ping.

                This field is a member of `oneof`_ ``type``.
            creative_finding (google.ads.admanager_v1.types.DaiSession.Finding.CreativeFinding):
                Output only. A finding related to a creative.

                This field is a member of `oneof`_ ``type``.
            ad_request_finding (google.ads.admanager_v1.types.DaiSession.Finding.AdRequestFinding):
                Output only. A finding related to an ad
                request within ad selection.

                This field is a member of `oneof`_ ``type``.
            severity (google.ads.admanager_v1.types.SessionFindingSeverityEnum.SessionFindingSeverity):
                Output only. The severity of the finding to
                the session.

                This field is a member of `oneof`_ ``_severity``.
            description (str):
                Output only. A description of the finding.

                This field is a member of `oneof`_ ``_description``.
        """

        class PodFinding(proto.Message):
            r"""A finding that occurred while decisioning an ad pod.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                type_ (google.ads.admanager_v1.types.PodFindingTypeEnum.PodFindingType):
                    Output only. The finding's type.

                    This field is a member of `oneof`_ ``_type``.
                pod_key (int):
                    Output only. ID that links to the relevant ad
                    pod.

                    This field is a member of `oneof`_ ``_pod_key``.
            """

            type_: dai_session_enums.PodFindingTypeEnum.PodFindingType = proto.Field(
                proto.ENUM,
                number=1,
                optional=True,
                enum=dai_session_enums.PodFindingTypeEnum.PodFindingType,
            )
            pod_key: int = proto.Field(
                proto.INT64,
                number=2,
                optional=True,
            )

        class SlateFinding(proto.Message):
            r"""A finding that occurred regarding the slate creative, which can be
            found at the
            [DaiSession.slate][google.ads.admanager.v1.DaiSession.slate] field.


            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                type_ (google.ads.admanager_v1.types.SlateFindingTypeEnum.SlateFindingType):
                    Output only. The finding's type.

                    This field is a member of `oneof`_ ``_type``.
            """

            type_: dai_session_enums.SlateFindingTypeEnum.SlateFindingType = (
                proto.Field(
                    proto.ENUM,
                    number=1,
                    optional=True,
                    enum=dai_session_enums.SlateFindingTypeEnum.SlateFindingType,
                )
            )

        class AdBreakFinding(proto.Message):
            r"""A finding that occurred while serving ads for a session.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                type_ (google.ads.admanager_v1.types.AdBreakFindingTypeEnum.AdBreakFindingType):
                    Output only. The finding's type.

                    This field is a member of `oneof`_ ``_type``.
                break_key (int):
                    Output only. The ID that links to the
                    relevant ad break.

                    This field is a member of `oneof`_ ``_break_key``.
            """

            type_: dai_session_enums.AdBreakFindingTypeEnum.AdBreakFindingType = (
                proto.Field(
                    proto.ENUM,
                    number=1,
                    optional=True,
                    enum=dai_session_enums.AdBreakFindingTypeEnum.AdBreakFindingType,
                )
            )
            break_key: int = proto.Field(
                proto.INT64,
                number=2,
                optional=True,
            )

        class TrackingPingFinding(proto.Message):
            r"""A finding that occurred while pinging tracking URLs for a
            session.


            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                type_ (google.ads.admanager_v1.types.TrackingPingFindingTypeEnum.TrackingPingFindingType):
                    Output only. The finding's type.

                    This field is a member of `oneof`_ ``_type``.
                tracking_ping_key (int):
                    Output only. The ID that links to the
                    relevant tracking ping.

                    This field is a member of `oneof`_ ``_tracking_ping_key``.
            """

            type_: dai_session_enums.TrackingPingFindingTypeEnum.TrackingPingFindingType = proto.Field(
                proto.ENUM,
                number=1,
                optional=True,
                enum=dai_session_enums.TrackingPingFindingTypeEnum.TrackingPingFindingType,
            )
            tracking_ping_key: int = proto.Field(
                proto.INT64,
                number=2,
                optional=True,
            )

        class CreativeFinding(proto.Message):
            r"""A finding that occurred while looking up creative
            information.


            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                type_ (google.ads.admanager_v1.types.CreativeFindingTypeEnum.CreativeFindingType):
                    Output only. The finding's type.

                    This field is a member of `oneof`_ ``_type``.
                creative_key (int):
                    Output only. The ID that links to the
                    relevant creative.

                    This field is a member of `oneof`_ ``_creative_key``.
            """

            type_: dai_session_enums.CreativeFindingTypeEnum.CreativeFindingType = (
                proto.Field(
                    proto.ENUM,
                    number=1,
                    optional=True,
                    enum=dai_session_enums.CreativeFindingTypeEnum.CreativeFindingType,
                )
            )
            creative_key: int = proto.Field(
                proto.INT64,
                number=2,
                optional=True,
            )

        class AdRequestFinding(proto.Message):
            r"""A finding that occurred while making an ad request.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                type_ (google.ads.admanager_v1.types.AdRequestFindingTypeEnum.AdRequestFindingType):
                    Output only. The finding's type.

                    This field is a member of `oneof`_ ``_type``.
                ad_selection_key (int):
                    Output only. The ID that links to the
                    relevant ad selection.

                    This field is a member of `oneof`_ ``_ad_selection_key``.
                ad_request_key (int):
                    Output only. The ID that links to the
                    relevant ad request.

                    This field is a member of `oneof`_ ``_ad_request_key``.
            """

            type_: dai_session_enums.AdRequestFindingTypeEnum.AdRequestFindingType = proto.Field(
                proto.ENUM,
                number=1,
                optional=True,
                enum=dai_session_enums.AdRequestFindingTypeEnum.AdRequestFindingType,
            )
            ad_selection_key: int = proto.Field(
                proto.INT64,
                number=2,
                optional=True,
            )
            ad_request_key: int = proto.Field(
                proto.INT64,
                number=3,
                optional=True,
            )

        pod_finding: "DaiSession.Finding.PodFinding" = proto.Field(
            proto.MESSAGE,
            number=4,
            oneof="type",
            message="DaiSession.Finding.PodFinding",
        )
        slate_finding: "DaiSession.Finding.SlateFinding" = proto.Field(
            proto.MESSAGE,
            number=5,
            oneof="type",
            message="DaiSession.Finding.SlateFinding",
        )
        ad_break_finding: "DaiSession.Finding.AdBreakFinding" = proto.Field(
            proto.MESSAGE,
            number=6,
            oneof="type",
            message="DaiSession.Finding.AdBreakFinding",
        )
        tracking_finding: "DaiSession.Finding.TrackingPingFinding" = proto.Field(
            proto.MESSAGE,
            number=7,
            oneof="type",
            message="DaiSession.Finding.TrackingPingFinding",
        )
        creative_finding: "DaiSession.Finding.CreativeFinding" = proto.Field(
            proto.MESSAGE,
            number=8,
            oneof="type",
            message="DaiSession.Finding.CreativeFinding",
        )
        ad_request_finding: "DaiSession.Finding.AdRequestFinding" = proto.Field(
            proto.MESSAGE,
            number=9,
            oneof="type",
            message="DaiSession.Finding.AdRequestFinding",
        )
        severity: dai_session_enums.SessionFindingSeverityEnum.SessionFindingSeverity = proto.Field(
            proto.ENUM,
            number=1,
            optional=True,
            enum=dai_session_enums.SessionFindingSeverityEnum.SessionFindingSeverity,
        )
        description: str = proto.Field(
            proto.STRING,
            number=2,
            optional=True,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    creation_context: CreationContext = proto.Field(
        proto.MESSAGE,
        number=3,
        message=CreationContext,
    )
    slate: Creative = proto.Field(
        proto.MESSAGE,
        number=4,
        message=Creative,
    )
    ad_selections: MutableMapping[int, AdSelection] = proto.MapField(
        proto.INT64,
        proto.MESSAGE,
        number=5,
        message=AdSelection,
    )
    ad_pods: MutableMapping[int, AdPod] = proto.MapField(
        proto.INT64,
        proto.MESSAGE,
        number=6,
        message=AdPod,
    )
    ad_breaks: MutableMapping[int, AdBreak] = proto.MapField(
        proto.INT64,
        proto.MESSAGE,
        number=7,
        message=AdBreak,
    )
    findings: MutableSequence[Finding] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message=Finding,
    )
    session_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=9,
        message=duration_pb2.Duration,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
