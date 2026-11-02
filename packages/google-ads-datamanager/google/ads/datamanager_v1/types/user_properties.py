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
    package="google.ads.datamanager.v1",
    manifest={
        "CustomerType",
        "CustomerValueBucket",
        "UserProperties",
        "UserProperty",
    },
)


class CustomerType(proto.Enum):
    r"""Type of the customer associated with the event.

    Values:
        CUSTOMER_TYPE_UNSPECIFIED (0):
            Unspecified CustomerType. Should never be
            used.
        NEW (1):
            The customer is new to the advertiser.
        RETURNING (2):
            The customer is returning to the advertiser.
        REENGAGED (3):
            The customer has re-engaged with the
            advertiser.
    """

    CUSTOMER_TYPE_UNSPECIFIED = 0
    NEW = 1
    RETURNING = 2
    REENGAGED = 3


class CustomerValueBucket(proto.Enum):
    r"""The advertiser-assessed value of the customer.

    Values:
        CUSTOMER_VALUE_BUCKET_UNSPECIFIED (0):
            Unspecified CustomerValueBucket. Should never
            be used.
        LOW (1):
            The customer is low value.
        MEDIUM (2):
            The customer is medium value.
        HIGH (3):
            The customer is high value.
    """

    CUSTOMER_VALUE_BUCKET_UNSPECIFIED = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3


class UserProperties(proto.Message):
    r"""Advertiser-assessed information about the user at the time
    that the event happened. See
    https://support.google.com/google-ads/answer/14007601 for more
    details.

    Attributes:
        customer_type (google.ads.datamanager_v1.types.CustomerType):
            Optional. Type of the customer associated
            with the event.
        customer_value_bucket (google.ads.datamanager_v1.types.CustomerValueBucket):
            Optional. The advertiser-assessed value of
            the customer.
        additional_user_properties (MutableSequence[google.ads.datamanager_v1.types.UserProperty]):
            Optional. A bucket of any additional `user
            properties <https://developers.google.com/analytics/devguides/collection/protocol/ga4/user-properties>`__
            for the user associated with this event.
    """

    customer_type: "CustomerType" = proto.Field(
        proto.ENUM,
        number=1,
        enum="CustomerType",
    )
    customer_value_bucket: "CustomerValueBucket" = proto.Field(
        proto.ENUM,
        number=2,
        enum="CustomerValueBucket",
    )
    additional_user_properties: MutableSequence["UserProperty"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="UserProperty",
    )


class UserProperty(proto.Message):
    r"""A bucket of any additional `user
    properties <https://developers.google.com/analytics/devguides/collection/protocol/ga4/user-properties>`__
    for the user associated with this event.

    Attributes:
        property_name (str):
            Required. The name of the user property to
            use.
        value (str):
            Required. The string representation of the
            value of the user property to use.
    """

    property_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    value: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
