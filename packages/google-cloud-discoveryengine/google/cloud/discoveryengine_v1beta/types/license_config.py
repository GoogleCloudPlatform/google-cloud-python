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

import google.type.date_pb2 as date_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.discoveryengine_v1beta.types import common

__protobuf__ = proto.module(
    package="google.cloud.discoveryengine.v1beta",
    manifest={
        "LicenseConfig",
    },
)


class LicenseConfig(proto.Message):
    r"""Information about users' licenses.

    Attributes:
        name (str):
            Immutable. Identifier. The fully qualified resource name of
            the license config. Format:
            ``projects/{project}/locations/{location}/licenseConfigs/{license_config}``
        license_count (int):
            Required. Number of licenses purchased.
        subscription_tier (google.cloud.discoveryengine_v1beta.types.SubscriptionTier):
            Required. Subscription tier information for
            the license config.
        state (google.cloud.discoveryengine_v1beta.types.LicenseConfig.State):
            Output only. The state of the license config.
        auto_renew (bool):
            Optional. Whether the license config should
            be auto renewed when it reaches the end date.
        start_date (google.type.date_pb2.Date):
            Required. The start date.
        end_date (google.type.date_pb2.Date):
            Optional. The planed end date.
        subscription_term (google.cloud.discoveryengine_v1beta.types.SubscriptionTerm):
            Required. Subscription term.
        free_trial (bool):
            Optional. Whether the license config is for
            free trial.
        gemini_bundle (bool):
            Output only. Whether the license config is
            for Gemini bundle.
        early_terminated (bool):
            Output only. Indication of whether the
            subscription is terminated earlier than the
            expiration date. This is usually terminated by
            pipeline once the subscription gets terminated
            from subsv3.
        early_termination_date (google.type.date_pb2.Date):
            Output only. The date when the subscription
            is terminated earlier than the expiration date.
    """

    class State(proto.Enum):
        r"""License config state enumeration.

        Values:
            STATE_UNSPECIFIED (0):
                Default value. The license config does not
                exist.
            ACTIVE (1):
                The license config is effective and being
                used.
            EXPIRED (2):
                The license config has expired.
            NOT_STARTED (3):
                The license config has not started yet, and
                its start date is in the future.
            WITHDRAWN (4):
                This is when a sub license config has
                returned all its seats back to
                BillingAccountLicenseConfig that it belongs to.
                Similar to EXPIRED.
            DEACTIVATING (5):
                The license config is terminated earlier than
                the expiration date and it is deactivating. The
                customer will still have access in this state.
                It will be converted to EXPIRED after the
                deactivating period ends (14 days) or when the
                end date is reached, whichever comes first.
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        EXPIRED = 2
        NOT_STARTED = 3
        WITHDRAWN = 4
        DEACTIVATING = 5

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    license_count: int = proto.Field(
        proto.INT64,
        number=2,
    )
    subscription_tier: common.SubscriptionTier = proto.Field(
        proto.ENUM,
        number=3,
        enum=common.SubscriptionTier,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=4,
        enum=State,
    )
    auto_renew: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    start_date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=6,
        message=date_pb2.Date,
    )
    end_date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=7,
        message=date_pb2.Date,
    )
    subscription_term: common.SubscriptionTerm = proto.Field(
        proto.ENUM,
        number=8,
        enum=common.SubscriptionTerm,
    )
    free_trial: bool = proto.Field(
        proto.BOOL,
        number=9,
    )
    gemini_bundle: bool = proto.Field(
        proto.BOOL,
        number=11,
    )
    early_terminated: bool = proto.Field(
        proto.BOOL,
        number=12,
    )
    early_termination_date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=13,
        message=date_pb2.Date,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
