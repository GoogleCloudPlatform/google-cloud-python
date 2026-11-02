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
    package="google.appengine.v1",
    manifest={
        "NetworkSettings",
    },
)


class NetworkSettings(proto.Message):
    r"""A NetworkSettings resource is a container for ingress
    settings for a version or service.

    Attributes:
        ingress_traffic_allowed (google.cloud.appengine_admin_v1.types.NetworkSettings.IngressTrafficAllowed):
            The ingress settings for version or service.
    """

    class IngressTrafficAllowed(proto.Enum):
        r"""If unspecified, INGRESS_TRAFFIC_ALLOWED_ALL will be used.

        Values:
            INGRESS_TRAFFIC_ALLOWED_UNSPECIFIED (0):
                Unspecified
            INGRESS_TRAFFIC_ALLOWED_ALL (1):
                Allow HTTP traffic from public and private
                sources.
            INGRESS_TRAFFIC_ALLOWED_INTERNAL_ONLY (2):
                Allow HTTP traffic from only private VPC
                sources.
            INGRESS_TRAFFIC_ALLOWED_INTERNAL_AND_LB (3):
                Allow HTTP traffic from private VPC sources
                and through load balancers.
        """

        INGRESS_TRAFFIC_ALLOWED_UNSPECIFIED = 0
        INGRESS_TRAFFIC_ALLOWED_ALL = 1
        INGRESS_TRAFFIC_ALLOWED_INTERNAL_ONLY = 2
        INGRESS_TRAFFIC_ALLOWED_INTERNAL_AND_LB = 3

    ingress_traffic_allowed: IngressTrafficAllowed = proto.Field(
        proto.ENUM,
        number=1,
        enum=IngressTrafficAllowed,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
