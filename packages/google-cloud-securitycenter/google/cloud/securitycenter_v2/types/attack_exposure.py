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

import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.securitycenter.v2",
    manifest={
        "AttackExposure",
    },
)


class AttackExposure(proto.Message):
    r"""An attack exposure contains the results of an attack path
    simulation run.

    Attributes:
        score (float):
            A number between 0 (inclusive) and infinity
            that represents how important this finding is to
            remediate. The higher the score, the more
            important it is to remediate.
        latest_calculation_time (google.protobuf.timestamp_pb2.Timestamp):
            The most recent time the attack exposure was
            updated on this finding.
        attack_exposure_result (str):
            The resource name of the attack path simulation result that
            contains the details regarding this attack exposure score.
            Example:
            ``organizations/123/simulations/456/attackExposureResults/789``
        state (google.cloud.securitycenter_v2.types.AttackExposure.State):
            Output only. What state this AttackExposure
            is in. This captures whether or not an attack
            exposure has been calculated or not.
        exposed_high_value_resources_count (int):
            The number of high value resources that are
            exposed as a result of this finding.
        exposed_medium_value_resources_count (int):
            The number of medium value resources that are
            exposed as a result of this finding.
        exposed_low_value_resources_count (int):
            The number of high value resources that are
            exposed as a result of this finding.
    """

    class State(proto.Enum):
        r"""This enum defines the various states an AttackExposure can be
        in.

        Values:
            STATE_UNSPECIFIED (0):
                The state is not specified.
            CALCULATED (1):
                The attack exposure has been calculated.
            NOT_CALCULATED (2):
                The attack exposure has not been calculated.
        """

        STATE_UNSPECIFIED = 0
        CALCULATED = 1
        NOT_CALCULATED = 2

    score: float = proto.Field(
        proto.DOUBLE,
        number=1,
    )
    latest_calculation_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    attack_exposure_result: str = proto.Field(
        proto.STRING,
        number=3,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=4,
        enum=State,
    )
    exposed_high_value_resources_count: int = proto.Field(
        proto.INT32,
        number=5,
    )
    exposed_medium_value_resources_count: int = proto.Field(
        proto.INT32,
        number=6,
    )
    exposed_low_value_resources_count: int = proto.Field(
        proto.INT32,
        number=7,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
