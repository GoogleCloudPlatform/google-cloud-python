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
    package="google.cloud.support.v2beta",
    manifest={
        "Escalation",
    },
)


class Escalation(proto.Message):
    r"""An escalation of a support case.

    Attributes:
        reason (google.cloud.support_v2beta.types.Escalation.Reason):
            Required. The reason why the Case is being
            escalated.
        justification (str):
            Required. A free text description to accompany the
            ``reason`` field above. Provides additional context on why
            the case is being escalated.
    """

    class Reason(proto.Enum):
        r"""An enum detailing the possible reasons a case may be
        escalated.

        Values:
            REASON_UNSPECIFIED (0):
                The escalation reason is in an unknown state
                or has not been specified.
            RESOLUTION_TIME (1):
                The case is taking too long to resolve.
            TECHNICAL_EXPERTISE (2):
                The support agent does not have the expertise
                required to successfully resolve the issue.
            BUSINESS_IMPACT (3):
                The issue is having a significant business
                impact.
        """

        REASON_UNSPECIFIED = 0
        RESOLUTION_TIME = 1
        TECHNICAL_EXPERTISE = 2
        BUSINESS_IMPACT = 3

    reason: Reason = proto.Field(
        proto.ENUM,
        number=4,
        enum=Reason,
    )
    justification: str = proto.Field(
        proto.STRING,
        number=5,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
