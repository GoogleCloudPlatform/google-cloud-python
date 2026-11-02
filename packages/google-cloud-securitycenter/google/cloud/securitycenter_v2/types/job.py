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
        "JobState",
        "Job",
    },
)


class JobState(proto.Enum):
    r"""JobState represents the state of the job.

    Values:
        JOB_STATE_UNSPECIFIED (0):
            Unspecified represents an unknown state and
            should not be used.
        PENDING (1):
            Job is scheduled and pending for run
        RUNNING (2):
            Job in progress
        SUCCEEDED (3):
            Job has completed with success
        FAILED (4):
            Job has completed but with failure
    """

    JOB_STATE_UNSPECIFIED = 0
    PENDING = 1
    RUNNING = 2
    SUCCEEDED = 3
    FAILED = 4


class Job(proto.Message):
    r"""Describes a job

    Attributes:
        name (str):
            The fully-qualified name for a job. e.g.
            ``projects/<project_id>/jobs/<job_id>``
        state (google.cloud.securitycenter_v2.types.JobState):
            Output only. State of the job, such as ``RUNNING`` or
            ``PENDING``.
        error_code (int):
            Optional. If the job did not complete
            successfully, this field describes why.
        location (str):
            Optional. Gives the location where the job ran, such as
            ``US`` or ``europe-west1``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    state: "JobState" = proto.Field(
        proto.ENUM,
        number=2,
        enum="JobState",
    )
    error_code: int = proto.Field(
        proto.INT32,
        number=3,
    )
    location: str = proto.Field(
        proto.STRING,
        number=4,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
