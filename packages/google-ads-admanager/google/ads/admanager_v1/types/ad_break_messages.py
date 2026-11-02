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

from google.ads.admanager_v1.types import early_ad_break_notification_enums

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "AdBreak",
    },
)


class AdBreak(proto.Message):
    r"""The ``AdBreak`` resource.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the ``AdBreak``. This field
            uses the ``LiveStreamEvent`` resource's asset key in the
            URI, even if the ad break was created, updated, or queried
            using the custom asset key.

            Format:
            ``networks/{network_code}/liveStreamEventsByAssetKey/{asset_key}/adBreaks/{ad_break_id}``
        ad_break_id (str):
            Optional. Immutable. ``AdBreak`` ID. Must consist only of
            lowercase letters, digits, and hyphens. Ad break IDs have a
            maximum length of 63 characters. If not set, an ad break ID
            is generated as a UUID string.

            This field is a member of `oneof`_ ``_ad_break_id``.
        asset_key (str):
            Optional. Immutable. The asset key of the
            ``LiveStreamEvent`` that the ad break belongs to. Either an
            asset key or a custom asset key must be provided for
            creation.

            This field is a member of `oneof`_ ``_asset_key``.
        custom_asset_key (str):
            Optional. Immutable. The custom asset key of the
            ``LiveStreamEvent`` that the ad break belongs to. Either an
            asset key or a custom asset key must be provided for
            creation.

            This field is a member of `oneof`_ ``_custom_asset_key``.
        expected_start_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. The expected start time of the ad
            break. When set, the scheduled ad break will be
            decisioned shortly before the expected start
            time.
            If this field is not set, ad decisioning begins
            immediately. An ad break can be created up to
            six hours before the expected start time.

            This field is a member of `oneof`_ ``_expected_start_time``.
        duration (google.protobuf.duration_pb2.Duration):
            Required. The duration of the ``AdBreak``. An expected
            duration in seconds with up to nine fractional digits,
            ending with ``s``, for example, ``3.5s``. This value will be
            updated to match the actual duration from the manifest or
            pod request after the ad break's state is
            [``COMPLETE``][google.ads.admanager.v1.AdBreakStateEnum.AdBreakState.COMPLETE].

            This field is a member of `oneof`_ ``_duration``.
        break_state (google.ads.admanager_v1.types.AdBreakStateEnum.AdBreakState):
            Output only. The state of the ``AdBreak``.

            This field is a member of `oneof`_ ``_break_state``.
        break_sequence (int):
            Output only. The sequence id of the ``AdBreak``. The unique
            sequence number of the created ad break. This value is only
            set after the ``AdBreak`` starts decisioning indicated by
            the ad break state's being
            [``DECISIONED``][google.ads.admanager.v1.AdBreakStateEnum.AdBreakState.DECISIONED]
            .

            This field is a member of `oneof`_ ``_break_sequence``.
        pod_template_name (str):
            Optional. The pod template name of the ``AdBreak``. This
            field is the required unique name across all pod templates
            in the network, not the display name.

            This field is a member of `oneof`_ ``_pod_template_name``.
        custom_params (str):
            Optional. The key-value pairs to be included on the ad
            requests for this ``AdBreak``. Key-value pairs to include on
            ad requests for this break for custom criteria targeting in
            Google Ad Manager, separated by ``=`` and joined by ``&``.

            Format:"key1=value&key2=value".

            This field is a member of `oneof`_ ``_custom_params``.
        scte_35_cue_out (str):
            Optional. The Base64-encoded SCTE-35 command associated with
            the ``AdBreak``. This field can include the
            ``splice_insert()`` or ``time_signal()`` command.

            **Examples**

            - ``time_signal()``
              ::

                 /DA0AAAAAAAA///wBQb+cr0AUAAeAhxDVUVJSAAAjn/PAAGlmbAICAAAAAAsoKGKNAIAmsnRfg==

            - ``splice_insert()``
              ::

                 /DAvAAAAAAAA///wFAVIAACPf+/+c2nALv4AUsz1AAAAAAAKAAhDVUVJAAABNWLbowo=

            This field is a member of `oneof`_ ``_scte_35_cue_out``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    ad_break_id: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    asset_key: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    custom_asset_key: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )
    expected_start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        optional=True,
        message=timestamp_pb2.Timestamp,
    )
    duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=6,
        optional=True,
        message=duration_pb2.Duration,
    )
    break_state: early_ad_break_notification_enums.AdBreakStateEnum.AdBreakState = (
        proto.Field(
            proto.ENUM,
            number=7,
            optional=True,
            enum=early_ad_break_notification_enums.AdBreakStateEnum.AdBreakState,
        )
    )
    break_sequence: int = proto.Field(
        proto.INT64,
        number=8,
        optional=True,
    )
    pod_template_name: str = proto.Field(
        proto.STRING,
        number=9,
        optional=True,
    )
    custom_params: str = proto.Field(
        proto.STRING,
        number=10,
        optional=True,
    )
    scte_35_cue_out: str = proto.Field(
        proto.STRING,
        number=11,
        optional=True,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
