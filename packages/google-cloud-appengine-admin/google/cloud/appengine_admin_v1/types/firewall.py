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
        "FirewallRule",
    },
)


class FirewallRule(proto.Message):
    r"""A single firewall rule that is evaluated against incoming
    traffic and provides an action to take on matched requests.

    Attributes:
        priority (int):
            A positive integer between [1, Int32.MaxValue-1] that
            defines the order of rule evaluation. Rules with the lowest
            priority are evaluated first.

            A default rule at priority Int32.MaxValue matches all IPv4
            and IPv6 traffic when no previous rule matches. Only the
            action of this rule can be modified by the user.
        action (google.cloud.appengine_admin_v1.types.FirewallRule.Action):
            The action to take on matched requests.
        source_range (str):
            IP address or range, defined using CIDR notation, of
            requests that this rule applies to. You can use the wildcard
            character "\*" to match all IPs equivalent to "0/0" and
            "::/0" together. Examples: ``192.168.1.1`` or
            ``192.168.0.0/16`` or ``2001:db8::/32`` or
            ``2001:0db8:0000:0042:0000:8a2e:0370:7334``.

            .. raw:: html

                <p>Truncation will be silently performed on addresses which are not
                properly truncated. For example, `1.2.3.4/24` is accepted as the same
                address as `1.2.3.0/24`. Similarly, for IPv6, `2001:db8::1/32` is accepted
                as the same address as `2001:db8::/32`.
        description (str):
            An optional string description of this rule.
            This field has a maximum length of 100
            characters.
    """

    class Action(proto.Enum):
        r"""Available actions to take on matching requests.

        Values:
            UNSPECIFIED_ACTION (0):
                No description available.
            ALLOW (1):
                Matching requests are allowed.
            DENY (2):
                Matching requests are denied.
        """

        UNSPECIFIED_ACTION = 0
        ALLOW = 1
        DENY = 2

    priority: int = proto.Field(
        proto.INT32,
        number=1,
    )
    action: Action = proto.Field(
        proto.ENUM,
        number=2,
        enum=Action,
    )
    source_range: str = proto.Field(
        proto.STRING,
        number=3,
    )
    description: str = proto.Field(
        proto.STRING,
        number=4,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
