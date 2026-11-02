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
        "TermsOfServiceStatus",
        "TermsOfService",
    },
)


class TermsOfServiceStatus(proto.Enum):
    r"""Represents the caller's decision to accept or reject the
    terms of service.

    Values:
        TERMS_OF_SERVICE_STATUS_UNSPECIFIED (0):
            Not specified.
        ACCEPTED (1):
            Status indicating the caller has chosen to
            accept the terms of service.
        REJECTED (2):
            Status indicating the caller has chosen to
            reject the terms of service.
    """

    TERMS_OF_SERVICE_STATUS_UNSPECIFIED = 0
    ACCEPTED = 1
    REJECTED = 2


class TermsOfService(proto.Message):
    r"""The terms of service that the user has accepted/rejected.

    Attributes:
        customer_match_terms_of_service_status (google.ads.datamanager_v1.types.TermsOfServiceStatus):
            Optional. The Customer Match terms of service:
            https://support.google.com/adspolicy/answer/6299717. This
            must be accepted when ingesting
            [UserData][google.ads.datamanager.v1.UserData] or
            [MobileData][google.ads.datamanager.v1.MobileData]. This
            field is not required for Partner Match User list.
    """

    customer_match_terms_of_service_status: "TermsOfServiceStatus" = proto.Field(
        proto.ENUM,
        number=1,
        enum="TermsOfServiceStatus",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
