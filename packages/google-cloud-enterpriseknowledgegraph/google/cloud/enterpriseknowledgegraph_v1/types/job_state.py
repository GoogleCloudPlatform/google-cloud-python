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
    package="google.cloud.enterpriseknowledgegraph.v1",
    manifest={
        "JobState",
    },
)


class JobState(proto.Enum):
    r"""Describes the state of a job.

    Values:
        JOB_STATE_UNSPECIFIED (0):
            The job state is unspecified.
        JOB_STATE_PENDING (9):
            The service is preparing to run the job.
        JOB_STATE_RUNNING (1):
            The job is in progress.
        JOB_STATE_SUCCEEDED (2):
            The job completed successfully.
        JOB_STATE_FAILED (3):
            The job failed.
        JOB_STATE_CANCELLED (4):
            The job has been cancelled.
        JOB_STATE_KNOWLEDGE_EXTRACTION (5):
            Entity Recon API: The knowledge extraction
            job is running.
        JOB_STATE_RECON_PREPROCESSING (6):
            Entity Recon API: The preprocessing job is
            running.
        JOB_STATE_CLUSTERING (7):
            Entity Recon API: The clustering job is
            running.
        JOB_STATE_EXPORTING_CLUSTERS (8):
            Entity Recon API: The exporting clusters job
            is running.
    """

    JOB_STATE_UNSPECIFIED = 0
    JOB_STATE_PENDING = 9
    JOB_STATE_RUNNING = 1
    JOB_STATE_SUCCEEDED = 2
    JOB_STATE_FAILED = 3
    JOB_STATE_CANCELLED = 4
    JOB_STATE_KNOWLEDGE_EXTRACTION = 5
    JOB_STATE_RECON_PREPROCESSING = 6
    JOB_STATE_CLUSTERING = 7
    JOB_STATE_EXPORTING_CLUSTERS = 8


__all__ = tuple(sorted(__protobuf__.manifest))
