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
        "CloudDlpInspection",
    },
)


class CloudDlpInspection(proto.Message):
    r"""Details about the Cloud Data Loss Prevention (Cloud DLP) `inspection
    job <https://cloud.google.com/dlp/docs/concepts-job-triggers>`__
    that produced the finding.

    Attributes:
        inspect_job (str):
            Name of the inspection job, for example,
            ``projects/123/locations/europe/dlpJobs/i-8383929``.
        info_type (str):
            The type of information (or
            `infoType <https://cloud.google.com/dlp/docs/infotypes-reference>`__)
            found, for example, ``EMAIL_ADDRESS`` or ``STREET_ADDRESS``.
        info_type_count (int):
            The number of times Cloud DLP found this
            infoType within this job and resource.
        full_scan (bool):
            Whether Cloud DLP scanned the complete
            resource or a sampled subset.
    """

    inspect_job: str = proto.Field(
        proto.STRING,
        number=1,
    )
    info_type: str = proto.Field(
        proto.STRING,
        number=2,
    )
    info_type_count: int = proto.Field(
        proto.INT64,
        number=3,
    )
    full_scan: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
