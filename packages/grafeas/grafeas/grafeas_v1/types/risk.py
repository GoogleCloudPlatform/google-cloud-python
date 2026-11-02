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
    package="grafeas.v1",
    manifest={
        "Risk",
        "CISAKnownExploitedVulnerabilities",
        "ExploitPredictionScoringSystem",
    },
)


class Risk(proto.Message):
    r"""

    Attributes:
        cisa_kev (grafeas.grafeas_v1.types.CISAKnownExploitedVulnerabilities):
            CISA maintains the authoritative source of
            vulnerabilities that have been exploited in the
            wild.
        epss (grafeas.grafeas_v1.types.ExploitPredictionScoringSystem):
            The Exploit Prediction Scoring System (EPSS)
            estimates the likelihood (probability) that a
            software vulnerability will be exploited in the
            wild.
    """

    cisa_kev: "CISAKnownExploitedVulnerabilities" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="CISAKnownExploitedVulnerabilities",
    )
    epss: "ExploitPredictionScoringSystem" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ExploitPredictionScoringSystem",
    )


class CISAKnownExploitedVulnerabilities(proto.Message):
    r"""

    Attributes:
        known_ransomware_campaign_use (str):
            Whether the vulnerability is known to have
            been leveraged as part of a ransomware campaign.
    """

    known_ransomware_campaign_use: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ExploitPredictionScoringSystem(proto.Message):
    r"""

    Attributes:
        percentile (float):
            The percentile of the current score, the
            proportion of all scored vulnerabilities with
            the same or a lower EPSS score
        score (float):
            The EPSS score representing the probability [0-1] of
            exploitation in the wild in the next 30 days
    """

    percentile: float = proto.Field(
        proto.DOUBLE,
        number=1,
    )
    score: float = proto.Field(
        proto.DOUBLE,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
