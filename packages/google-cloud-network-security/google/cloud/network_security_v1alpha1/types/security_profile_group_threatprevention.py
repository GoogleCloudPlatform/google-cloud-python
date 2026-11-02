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
    package="google.cloud.networksecurity.v1alpha1",
    manifest={
        "Severity",
        "ThreatType",
        "ThreatAction",
        "Protocol",
        "ThreatPreventionProfile",
        "SeverityOverride",
        "ThreatOverride",
        "AntivirusOverride",
    },
)


class Severity(proto.Enum):
    r"""Severity level.

    Values:
        SEVERITY_UNSPECIFIED (0):
            Severity level not specified.
        INFORMATIONAL (1):
            Suspicious events that do not pose an
            immediate threat, but that are reported to call
            attention to deeper problems that could possibly
            exist.
        LOW (2):
            Warning-level threats that have very little
            impact on an organization's infrastructure. They
            usually require local or physical system access
            and may often result in victim privacy issues
            and information leakage.
        MEDIUM (3):
            Minor threats in which impact is minimized,
            that do not compromise the target or exploits
            that require an attacker to reside on the same
            local network as the victim, affect only
            non-standard configurations or obscure
            applications, or provide very limited access.
        HIGH (4):
            Threats that have the ability to become
            critical but have mitigating factors; for
            example, they may be difficult to exploit, do
            not result in elevated privileges, or do not
            have a large victim pool.
        CRITICAL (5):
            Serious threats, such as those that affect
            default installations of widely deployed
            software, result in root compromise of servers,
            and the exploit code is widely available to
            attackers. The attacker usually does not need
            any special authentication credentials or
            knowledge about the individual victims and the
            target does not need to be manipulated into
            performing any special functions.
    """

    SEVERITY_UNSPECIFIED = 0
    INFORMATIONAL = 1
    LOW = 2
    MEDIUM = 3
    HIGH = 4
    CRITICAL = 5


class ThreatType(proto.Enum):
    r"""Type of threat.

    Values:
        THREAT_TYPE_UNSPECIFIED (0):
            Type of threat not specified.
        UNKNOWN (1):
            Type of threat is not derivable from threat
            ID. An override will be created for all types.
            Firewall will ignore overridden signature ID's
            that don't exist in the specific type.
        VULNERABILITY (2):
            Threats related to system flaws that an
            attacker might otherwise attempt to exploit.
        ANTIVIRUS (3):
            Threats related to viruses and malware found
            in executables and file types.
        SPYWARE (4):
            Threats related to command-and-control (C2)
            activity, where spyware on an infected client is
            collecting data without the user's consent
            and/or communicating with a remote attacker.
        DNS (5):
            Threats related to DNS.
    """

    THREAT_TYPE_UNSPECIFIED = 0
    UNKNOWN = 1
    VULNERABILITY = 2
    ANTIVIRUS = 3
    SPYWARE = 4
    DNS = 5


class ThreatAction(proto.Enum):
    r"""Threat action override.

    Values:
        THREAT_ACTION_UNSPECIFIED (0):
            Threat action not specified.
        DEFAULT_ACTION (4):
            The default action (as specified by the
            vendor) is taken.
        ALLOW (1):
            The packet matching this rule will be allowed
            to transmit.
        ALERT (2):
            The packet matching this rule will be allowed to transmit,
            but a threat_log entry will be sent to the consumer project.
        DENY (3):
            The packet matching this rule will be dropped, and a
            threat_log entry will be sent to the consumer project.
    """

    THREAT_ACTION_UNSPECIFIED = 0
    DEFAULT_ACTION = 4
    ALLOW = 1
    ALERT = 2
    DENY = 3


class Protocol(proto.Enum):
    r"""Antivirus protocol.

    Values:
        PROTOCOL_UNSPECIFIED (0):
            Protocol not specified.
        SMTP (1):
            SMTP protocol
        SMB (2):
            SMB protocol
        POP3 (3):
            POP3 protocol
        IMAP (4):
            IMAP protocol
        HTTP2 (5):
            HTTP2 protocol
        HTTP (6):
            HTTP protocol
        FTP (7):
            FTP protocol
    """

    PROTOCOL_UNSPECIFIED = 0
    SMTP = 1
    SMB = 2
    POP3 = 3
    IMAP = 4
    HTTP2 = 5
    HTTP = 6
    FTP = 7


class ThreatPreventionProfile(proto.Message):
    r"""ThreatPreventionProfile defines an action for specific threat
    signatures or severity levels.

    Attributes:
        severity_overrides (MutableSequence[google.cloud.network_security_v1alpha1.types.SeverityOverride]):
            Optional. Configuration for overriding
            threats actions by severity match.
        threat_overrides (MutableSequence[google.cloud.network_security_v1alpha1.types.ThreatOverride]):
            Optional. Configuration for overriding threats actions by
            threat_id match. If a threat is matched both by
            configuration provided in severity_overrides and
            threat_overrides, the threat_overrides action is applied.
        antivirus_overrides (MutableSequence[google.cloud.network_security_v1alpha1.types.AntivirusOverride]):
            Optional. Configuration for overriding
            antivirus actions per protocol.
    """

    severity_overrides: MutableSequence["SeverityOverride"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="SeverityOverride",
    )
    threat_overrides: MutableSequence["ThreatOverride"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="ThreatOverride",
    )
    antivirus_overrides: MutableSequence["AntivirusOverride"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="AntivirusOverride",
    )


class SeverityOverride(proto.Message):
    r"""Defines what action to take for a specific severity match.

    Attributes:
        severity (google.cloud.network_security_v1alpha1.types.Severity):
            Required. Severity level to match.
        action (google.cloud.network_security_v1alpha1.types.ThreatAction):
            Required. Threat action override.
    """

    severity: "Severity" = proto.Field(
        proto.ENUM,
        number=1,
        enum="Severity",
    )
    action: "ThreatAction" = proto.Field(
        proto.ENUM,
        number=2,
        enum="ThreatAction",
    )


class ThreatOverride(proto.Message):
    r"""Defines what action to take for a specific threat_id match.

    Attributes:
        threat_id (str):
            Required. Vendor-specific ID of a threat to
            override.
        type_ (google.cloud.network_security_v1alpha1.types.ThreatType):
            Output only. Type of the threat (read only).
        action (google.cloud.network_security_v1alpha1.types.ThreatAction):
            Required. Threat action override. For some
            threat types, only a subset of actions applies.
    """

    threat_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_: "ThreatType" = proto.Field(
        proto.ENUM,
        number=2,
        enum="ThreatType",
    )
    action: "ThreatAction" = proto.Field(
        proto.ENUM,
        number=3,
        enum="ThreatAction",
    )


class AntivirusOverride(proto.Message):
    r"""Defines what action to take for antivirus threats per
    protocol.

    Attributes:
        protocol (google.cloud.network_security_v1alpha1.types.Protocol):
            Required. Protocol to match.
        action (google.cloud.network_security_v1alpha1.types.ThreatAction):
            Required. Threat action override. For some
            threat types, only a subset of actions applies.
    """

    protocol: "Protocol" = proto.Field(
        proto.ENUM,
        number=1,
        enum="Protocol",
    )
    action: "ThreatAction" = proto.Field(
        proto.ENUM,
        number=2,
        enum="ThreatAction",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
