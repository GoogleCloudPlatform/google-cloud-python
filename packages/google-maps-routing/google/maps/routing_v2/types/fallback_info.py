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
    package="google.maps.routing.v2",
    manifest={
        "FallbackReason",
        "FallbackRoutingMode",
        "FallbackInfo",
    },
)


class FallbackReason(proto.Enum):
    r"""Reasons for using fallback response.

    Values:
        FALLBACK_REASON_UNSPECIFIED (0):
            No fallback reason specified.
        SERVER_ERROR (1):
            A server error happened while calculating
            routes with your preferred routing mode, but we
            were able to return a result calculated by an
            alternative mode.
        LATENCY_EXCEEDED (2):
            We were not able to finish the calculation
            with your preferred routing mode on time, but we
            were able to return a result calculated by an
            alternative mode.
    """

    FALLBACK_REASON_UNSPECIFIED = 0
    SERVER_ERROR = 1
    LATENCY_EXCEEDED = 2


class FallbackRoutingMode(proto.Enum):
    r"""Actual routing mode used for returned fallback response.

    Values:
        FALLBACK_ROUTING_MODE_UNSPECIFIED (0):
            Not used.
        FALLBACK_TRAFFIC_UNAWARE (1):
            Indicates the ``TRAFFIC_UNAWARE``
            [``RoutingPreference``][google.maps.routing.v2.RoutingPreference]
            was used to compute the response.
        FALLBACK_TRAFFIC_AWARE (2):
            Indicates the ``TRAFFIC_AWARE``
            [``RoutingPreference``][google.maps.routing.v2.RoutingPreference]
            was used to compute the response.
    """

    FALLBACK_ROUTING_MODE_UNSPECIFIED = 0
    FALLBACK_TRAFFIC_UNAWARE = 1
    FALLBACK_TRAFFIC_AWARE = 2


class FallbackInfo(proto.Message):
    r"""Information related to how and why a fallback result was
    used. If this field is set, then it means the server used a
    different routing mode from your preferred mode as fallback.

    Attributes:
        routing_mode (google.maps.routing_v2.types.FallbackRoutingMode):
            Routing mode used for the response. If
            fallback was triggered, the mode may be
            different from routing preference set in the
            original client request.
        reason (google.maps.routing_v2.types.FallbackReason):
            The reason why fallback response was used
            instead of the original response. This field is
            only populated when the fallback mode is
            triggered and the fallback response is returned.
    """

    routing_mode: "FallbackRoutingMode" = proto.Field(
        proto.ENUM,
        number=1,
        enum="FallbackRoutingMode",
    )
    reason: "FallbackReason" = proto.Field(
        proto.ENUM,
        number=2,
        enum="FallbackReason",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
