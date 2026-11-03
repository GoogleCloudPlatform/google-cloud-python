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
    ad_rule_enums,
    ad_rule_slot_behavior_enum,
    ad_rule_slot_bumper_enum,
    ad_rule_slot_midroll_frequency_type_enum,
)
from google.ads.admanager_v1.types import targeting as gaa_targeting

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "AdRule",
        "AdRuleSlot",
    },
)


class AdRule(proto.Message):
    r"""An AdRule contains data that the ad server will use to
    generate a playlist of video ads.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the ``AdRule``. Format:
            ``networks/{network_code}/adRules/{ad_rule_id}``
        display_name (str):
            Required. The unique name of the AdRule. This
            attribute is required to create an ad rule and
            has a maximum length of 255 characters.

            This field is a member of `oneof`_ ``_display_name``.
        priority (int):
            Optional. The priority of the AdRule. This
            attribute is required and can range from 1 to
            1000, with 1 being the highest possible
            priority.

            Changing an ad rule's priority can affect the
            priorities of other ad rules. For example,
            increasing an ad rule's priority from 5 to 1
            will shift the ad rules that were previously in
            priority positions 1 through 4 down one.

            This field is a member of `oneof`_ ``_priority``.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Required. The start time of the AdRule. This
            attribute is required and must be a date in the
            future for new ad rules.

            This field is a member of `oneof`_ ``_start_time``.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. This end time of the AdRule. This attribute is
            required unless
            [endTimeUnlimited][google.ads.admanager.v1.AdRule.end_time_unlimited]
            is set to true. If specified, it must be after the
            [startTime][google.ads.admanager.v1.AdRule.start_time].

            This field is a member of `oneof`_ ``_end_time``.
        end_time_unlimited (bool):
            Optional. Specifies whether or not the AdRule
            has an end time. This attribute is optional and
            defaults to false.

            This field is a member of `oneof`_ ``_end_time_unlimited``.
        status (google.ads.admanager_v1.types.AdRuleStatusEnum.AdRuleStatus):
            Output only. The AdRuleStatus of the AdRule. This attribute
            is read-only and defaults to
            [AdRuleStatusEnum.AdRuleStatus.INACTIVE][google.ads.admanager.v1.AdRuleStatusEnum.AdRuleStatus.INACTIVE].

            This field is a member of `oneof`_ ``_status``.
        frequency_cap_behavior (google.ads.admanager_v1.types.AdRuleFrequencyCapBehaviorEnum.AdRuleFrequencyCapBehavior):
            Optional. The FrequencyCapBehavior of the AdRule. This
            attribute is optional and defaults to
            [AdRuleFrequencyCapBehaviorEnum.AdRuleFrequencyCapBehavior.DEFER][google.ads.admanager.v1.AdRuleFrequencyCapBehaviorEnum.AdRuleFrequencyCapBehavior.DEFER].

            This field is a member of `oneof`_ ``_frequency_cap_behavior``.
        max_impressions_per_line_item_per_stream (int):
            Optional. This AdRule object's frequency cap
            for the maximum impressions per stream. This
            attribute is optional and defaults to 0.

            This field is a member of `oneof`_ ``_max_impressions_per_line_item_per_stream``.
        max_impressions_per_line_item_per_pod (int):
            Optional. This AdRule object's frequency cap
            for the maximum impressions per pod. This
            attribute is optional and defaults to 0.

            This field is a member of `oneof`_ ``_max_impressions_per_line_item_per_pod``.
        preroll (google.ads.admanager_v1.types.AdRuleSlot):
            Required. This AdRule object's pre-roll slot.
            This attribute is required.

            This field is a member of `oneof`_ ``_preroll``.
        midrolls (MutableSequence[google.ads.admanager_v1.types.AdRuleSlot]):
            Required. This AdRule object's video mid-roll
            slots. This attribute is required, and there
            must be at least one mid-roll.
        postroll (google.ads.admanager_v1.types.AdRuleSlot):
            Required. This AdRule object's post-roll
            slot. This attribute is required.

            This field is a member of `oneof`_ ``_postroll``.
        targeting (google.ads.admanager_v1.types.Targeting):
            Required. The targeting of the ``AdRule``.

            This field is a member of `oneof`_ ``_targeting``.
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
    priority: int = proto.Field(
        proto.INT32,
        number=3,
        optional=True,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=13,
        optional=True,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=14,
        optional=True,
        message=timestamp_pb2.Timestamp,
    )
    end_time_unlimited: bool = proto.Field(
        proto.BOOL,
        number=15,
        optional=True,
    )
    status: ad_rule_enums.AdRuleStatusEnum.AdRuleStatus = proto.Field(
        proto.ENUM,
        number=4,
        optional=True,
        enum=ad_rule_enums.AdRuleStatusEnum.AdRuleStatus,
    )
    frequency_cap_behavior: ad_rule_enums.AdRuleFrequencyCapBehaviorEnum.AdRuleFrequencyCapBehavior = proto.Field(
        proto.ENUM,
        number=5,
        optional=True,
        enum=ad_rule_enums.AdRuleFrequencyCapBehaviorEnum.AdRuleFrequencyCapBehavior,
    )
    max_impressions_per_line_item_per_stream: int = proto.Field(
        proto.INT32,
        number=6,
        optional=True,
    )
    max_impressions_per_line_item_per_pod: int = proto.Field(
        proto.INT32,
        number=7,
        optional=True,
    )
    preroll: "AdRuleSlot" = proto.Field(
        proto.MESSAGE,
        number=8,
        optional=True,
        message="AdRuleSlot",
    )
    midrolls: MutableSequence["AdRuleSlot"] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message="AdRuleSlot",
    )
    postroll: "AdRuleSlot" = proto.Field(
        proto.MESSAGE,
        number=10,
        optional=True,
        message="AdRuleSlot",
    )
    targeting: gaa_targeting.Targeting = proto.Field(
        proto.MESSAGE,
        number=11,
        optional=True,
        message=gaa_targeting.Targeting,
    )


class AdRuleSlot(proto.Message):
    r"""Simple object representing an ad slot within an AdRule. Ad
    rule slots contain information about the types/number of ads to
    display, as well as additional information on how the ad server
    will generate playlists.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        slot_behavior (google.ads.admanager_v1.types.AdRuleSlotBehaviorEnum.AdRuleSlotBehavior):
            Optional. The AdRuleSlotBehavior for video ads for this
            slot. This attribute is optional and defaults to
            [AdRuleSlotBehaviorEnum.AdRuleSlotBehavior.DEFER][google.ads.admanager.v1.AdRuleSlotBehaviorEnum.AdRuleSlotBehavior.DEFER].
            Indicates whether video ads are allowed for this slot, or if
            the decision is deferred to alower-priority ad rule.

            This field is a member of `oneof`_ ``_slot_behavior``.
        max_video_ad_duration (google.protobuf.duration_pb2.Duration):
            Optional. The maximum duration in
            milliseconds of video ads within this slot. This
            attribute is optional and defaults to 0.

            This field is a member of `oneof`_ ``_max_video_ad_duration``.
        video_midroll_frequency_type (google.ads.admanager_v1.types.AdRuleSlotMidrollFrequencyTypeEnum.AdRuleSlotMidrollFrequencyType):
            Optional. The frequency type for video ads in this ad rule
            slot. This attribute is required for mid-rolls, but if this
            is not a mid-roll, the value is set to
            [AdRuleSlotMidrollFrequencyTypeEnum.AdRuleSlotMidrollFrequencyType.NONE][google.ads.admanager.v1.AdRuleSlotMidrollFrequencyTypeEnum.AdRuleSlotMidrollFrequencyType.NONE].

            This field is a member of `oneof`_ ``_video_midroll_frequency_type``.
        video_midroll_frequency (str):
            Optional. The mid-roll frequency of this ad rule slot for
            video ads. This attribute is required for mid-rolls, but if
            MidrollFrequencyType is set to
            [AdRuleSlotMidrollFrequencyTypeEnum.AdRuleSlotMidrollFrequencyType.NONE][google.ads.admanager.v1.AdRuleSlotMidrollFrequencyTypeEnum.AdRuleSlotMidrollFrequencyType.NONE],
            this value should be ignored. For example, if this slot has
            a frequency type of
            [AdRuleSlotMidrollFrequencyTypeEnum.AdRuleSlotMidrollFrequencyType.EVERY_N_SECONDS][google.ads.admanager.v1.AdRuleSlotMidrollFrequencyTypeEnum.AdRuleSlotMidrollFrequencyType.EVERY_N_SECONDS]
            and #videoMidrollFrequency = "60", this would mean "play a
            mid-roll every 60 seconds.".

            This field is a member of `oneof`_ ``_video_midroll_frequency``.
        bumper (google.ads.admanager_v1.types.AdRuleSlotBumperEnum.AdRuleSlotBumper):
            Optional. The AdRuleSlotBumper for this slot. This attribute
            is optional and defaults to
            [AdRuleSlotBumperEnum.AdRuleSlotBumper.NONE][google.ads.admanager.v1.AdRuleSlotBumperEnum.AdRuleSlotBumper.NONE].

            This field is a member of `oneof`_ ``_bumper``.
        max_bumper_duration (google.protobuf.duration_pb2.Duration):
            Optional. The maximum duration of bumper ads
            within this slot. This attribute is optional and
            defaults to 0.

            This field is a member of `oneof`_ ``_max_bumper_duration``.
        max_pod_duration (google.protobuf.duration_pb2.Duration):
            Optional. The maximum pod duration for this
            slot. This attribute is optional and defaults to
            0.

            This field is a member of `oneof`_ ``_max_pod_duration``.
        pod_max_ad_count (int):
            Optional. The maximum number of ads allowed
            in a pod in this slot. This attribute is
            optional and defaults to 0.

            This field is a member of `oneof`_ ``_pod_max_ad_count``.
    """

    slot_behavior: ad_rule_slot_behavior_enum.AdRuleSlotBehaviorEnum.AdRuleSlotBehavior = proto.Field(
        proto.ENUM,
        number=1,
        optional=True,
        enum=ad_rule_slot_behavior_enum.AdRuleSlotBehaviorEnum.AdRuleSlotBehavior,
    )
    max_video_ad_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=4,
        optional=True,
        message=duration_pb2.Duration,
    )
    video_midroll_frequency_type: ad_rule_slot_midroll_frequency_type_enum.AdRuleSlotMidrollFrequencyTypeEnum.AdRuleSlotMidrollFrequencyType = proto.Field(
        proto.ENUM,
        number=5,
        optional=True,
        enum=ad_rule_slot_midroll_frequency_type_enum.AdRuleSlotMidrollFrequencyTypeEnum.AdRuleSlotMidrollFrequencyType,
    )
    video_midroll_frequency: str = proto.Field(
        proto.STRING,
        number=6,
        optional=True,
    )
    bumper: ad_rule_slot_bumper_enum.AdRuleSlotBumperEnum.AdRuleSlotBumper = (
        proto.Field(
            proto.ENUM,
            number=7,
            optional=True,
            enum=ad_rule_slot_bumper_enum.AdRuleSlotBumperEnum.AdRuleSlotBumper,
        )
    )
    max_bumper_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=8,
        optional=True,
        message=duration_pb2.Duration,
    )
    max_pod_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=9,
        optional=True,
        message=duration_pb2.Duration,
    )
    pod_max_ad_count: int = proto.Field(
        proto.INT32,
        number=10,
        optional=True,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
