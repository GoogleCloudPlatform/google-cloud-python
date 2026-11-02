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
    package="google.cloud.securitycenter.v2",
    manifest={
        "IpRules",
        "IpRule",
        "Allowed",
        "Denied",
    },
)


class IpRules(proto.Message):
    r"""IP rules associated with the finding.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        direction (google.cloud.securitycenter_v2.types.IpRules.Direction):
            The direction that the rule is applicable to,
            one of ingress or egress.
        allowed (google.cloud.securitycenter_v2.types.Allowed):
            Tuple with allowed rules.

            This field is a member of `oneof`_ ``rules``.
        denied (google.cloud.securitycenter_v2.types.Denied):
            Tuple with denied rules.

            This field is a member of `oneof`_ ``rules``.
        source_ip_ranges (MutableSequence[str]):
            If source IP ranges are specified, the
            firewall rule applies only to traffic that has a
            source IP address in these ranges. These ranges
            must be expressed in CIDR format. Only supports
            IPv4.
        destination_ip_ranges (MutableSequence[str]):
            If destination IP ranges are specified, the
            firewall rule applies only to traffic that has a
            destination IP address in these ranges. These
            ranges must be expressed in CIDR format. Only
            supports IPv4.
        exposed_services (MutableSequence[str]):
            Name of the network protocol service, such as
            FTP, that is exposed by the open port. Follows
            the naming convention available at:

            https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml.
    """

    class Direction(proto.Enum):
        r"""The type of direction that the rule is applicable to, one of ingress
        or egress. Not applicable to OPEN_X_PORT findings.

        Values:
            DIRECTION_UNSPECIFIED (0):
                Unspecified direction value.
            INGRESS (1):
                Ingress direction value.
            EGRESS (2):
                Egress direction value.
        """

        DIRECTION_UNSPECIFIED = 0
        INGRESS = 1
        EGRESS = 2

    direction: Direction = proto.Field(
        proto.ENUM,
        number=1,
        enum=Direction,
    )
    allowed: "Allowed" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="rules",
        message="Allowed",
    )
    denied: "Denied" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="rules",
        message="Denied",
    )
    source_ip_ranges: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    destination_ip_ranges: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    exposed_services: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )


class IpRule(proto.Message):
    r"""IP rule information.

    Attributes:
        protocol (str):
            The IP protocol this rule applies to. This
            value can either be one of the following well
            known protocol strings (TCP, UDP, ICMP, ESP, AH,
            IPIP, SCTP) or a string representation of the
            integer value.
        port_ranges (MutableSequence[google.cloud.securitycenter_v2.types.IpRule.PortRange]):
            Optional. An optional list of ports to which
            this rule applies. This field is only applicable
            for the UDP or (S)TCP protocols. Each entry must
            be either an integer or a range including a min
            and max port number.
    """

    class PortRange(proto.Message):
        r"""A port range which is inclusive of the min and max values.
        Values are between 0 and 2^16-1. The max can be equal / must be
        not smaller than the min value. If min and max are equal this
        indicates that it is a single port.

        Attributes:
            min_ (int):
                Minimum port value.
            max_ (int):
                Maximum port value.
        """

        min_: int = proto.Field(
            proto.INT64,
            number=1,
        )
        max_: int = proto.Field(
            proto.INT64,
            number=2,
        )

    protocol: str = proto.Field(
        proto.STRING,
        number=1,
    )
    port_ranges: MutableSequence[PortRange] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=PortRange,
    )


class Allowed(proto.Message):
    r"""Allowed IP rule.

    Attributes:
        ip_rules (MutableSequence[google.cloud.securitycenter_v2.types.IpRule]):
            Optional. Optional list of allowed IP rules.
    """

    ip_rules: MutableSequence["IpRule"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="IpRule",
    )


class Denied(proto.Message):
    r"""Denied IP rule.

    Attributes:
        ip_rules (MutableSequence[google.cloud.securitycenter_v2.types.IpRule]):
            Optional. Optional list of denied IP rules.
    """

    ip_rules: MutableSequence["IpRule"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="IpRule",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
