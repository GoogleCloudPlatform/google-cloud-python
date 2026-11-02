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
        "Chokepoint",
    },
)


class Chokepoint(proto.Message):
    r"""Contains details about a chokepoint, which is a resource or resource
    group where high-risk attack paths converge, based on [attack path
    simulations]
    (https://cloud.google.com/security-command-center/docs/attack-exposure-learn#attack_path_simulations).

    Attributes:
        related_findings (MutableSequence[str]):
            List of resource names of findings associated
            with this chokepoint. For example,
            organizations/123/sources/456/findings/789. This
            list will have at most 100 findings.
    """

    related_findings: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
