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
    package="google.cloud.securitycenter.v1",
    manifest={
        "ToxicCombination",
    },
)


class ToxicCombination(proto.Message):
    r"""Contains details about a group of security issues that, when
    the issues occur together, represent a greater risk than when
    the issues occur independently. A group of such issues is
    referred to as a toxic combination.

    Attributes:
        attack_exposure_score (float):
            The `Attack exposure
            score <https://cloud.google.com/security-command-center/docs/attack-exposure-learn#attack_exposure_scores>`__
            of this toxic combination. The score is a measure of how
            much this toxic combination exposes one or more high-value
            resources to potential attack.
        related_findings (MutableSequence[str]):
            List of resource names of findings associated with this
            toxic combination. For example,
            ``organizations/123/sources/456/findings/789``.
    """

    attack_exposure_score: float = proto.Field(
        proto.DOUBLE,
        number=1,
    )
    related_findings: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
