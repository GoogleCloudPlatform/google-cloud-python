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
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.securitycenter.v1",
    manifest={
        "CloudArmor",
        "SecurityPolicy",
        "Requests",
        "AdaptiveProtection",
        "Attack",
    },
)


class CloudArmor(proto.Message):
    r"""Fields related to Google Cloud Armor findings.

    Attributes:
        security_policy (google.cloud.securitycenter_v1.types.SecurityPolicy):
            Information about the `Google Cloud Armor security
            policy <https://cloud.google.com/armor/docs/security-policy-overview>`__
            relevant to the finding.
        requests (google.cloud.securitycenter_v1.types.Requests):
            Information about incoming requests evaluated by `Google
            Cloud Armor security
            policies <https://cloud.google.com/armor/docs/security-policy-overview>`__.
        adaptive_protection (google.cloud.securitycenter_v1.types.AdaptiveProtection):
            Information about potential Layer 7 DDoS attacks identified
            by `Google Cloud Armor Adaptive
            Protection <https://cloud.google.com/armor/docs/adaptive-protection-overview>`__.
        attack (google.cloud.securitycenter_v1.types.Attack):
            Information about DDoS attack volume and
            classification.
        threat_vector (str):
            Distinguish between volumetric & protocol DDoS attack and
            application layer attacks. For example, "L3_4" for Layer 3
            and Layer 4 DDoS attacks, or "L_7" for Layer 7 DDoS attacks.
        duration (google.protobuf.duration_pb2.Duration):
            Duration of attack from the start until the
            current moment (updated every 5 minutes).
    """

    security_policy: "SecurityPolicy" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="SecurityPolicy",
    )
    requests: "Requests" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Requests",
    )
    adaptive_protection: "AdaptiveProtection" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="AdaptiveProtection",
    )
    attack: "Attack" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="Attack",
    )
    threat_vector: str = proto.Field(
        proto.STRING,
        number=5,
    )
    duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=6,
        message=duration_pb2.Duration,
    )


class SecurityPolicy(proto.Message):
    r"""Information about the `Google Cloud Armor security
    policy <https://cloud.google.com/armor/docs/security-policy-overview>`__
    relevant to the finding.

    Attributes:
        name (str):
            The name of the Google Cloud Armor security
            policy, for example, "my-security-policy".
        type_ (str):
            The type of Google Cloud Armor security
            policy for example, 'backend security policy',
            'edge security policy', 'network edge security
            policy', or 'always-on DDoS protection'.
        preview (bool):
            Whether or not the associated rule or policy
            is in preview mode.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_: str = proto.Field(
        proto.STRING,
        number=2,
    )
    preview: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class Requests(proto.Message):
    r"""Information about the requests relevant to the finding.

    Attributes:
        ratio (float):
            For 'Increasing deny ratio', the ratio is the
            denied traffic divided by the allowed traffic.
            For 'Allowed traffic spike', the ratio is the
            allowed traffic in the short term divided by
            allowed traffic in the long term.
        short_term_allowed (int):
            Allowed RPS (requests per second) in the
            short term.
        long_term_allowed (int):
            Allowed RPS (requests per second) over the
            long term.
        long_term_denied (int):
            Denied RPS (requests per second) over the
            long term.
    """

    ratio: float = proto.Field(
        proto.DOUBLE,
        number=1,
    )
    short_term_allowed: int = proto.Field(
        proto.INT32,
        number=2,
    )
    long_term_allowed: int = proto.Field(
        proto.INT32,
        number=3,
    )
    long_term_denied: int = proto.Field(
        proto.INT32,
        number=4,
    )


class AdaptiveProtection(proto.Message):
    r"""Information about `Google Cloud Armor Adaptive
    Protection <https://cloud.google.com/armor/docs/cloud-armor-overview#google-cloud-armor-adaptive-protection>`__.

    Attributes:
        confidence (float):
            A score of 0 means that there is low confidence that the
            detected event is an actual attack. A score of 1 means that
            there is high confidence that the detected event is an
            attack. See the `Adaptive Protection
            documentation <https://cloud.google.com/armor/docs/adaptive-protection-overview#configure-alert-tuning>`__
            for further explanation.
    """

    confidence: float = proto.Field(
        proto.DOUBLE,
        number=1,
    )


class Attack(proto.Message):
    r"""Information about DDoS attack volume and classification.

    Attributes:
        volume_pps (int):
            Total PPS (packets per second) volume of
            attack.
        volume_bps (int):
            Total BPS (bytes per second) volume of
            attack.
        classification (str):
            Type of attack, for example, 'SYN-flood',
            'NTP-udp', or 'CHARGEN-udp'.
    """

    volume_pps: int = proto.Field(
        proto.INT32,
        number=1,
    )
    volume_bps: int = proto.Field(
        proto.INT32,
        number=2,
    )
    classification: str = proto.Field(
        proto.STRING,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
