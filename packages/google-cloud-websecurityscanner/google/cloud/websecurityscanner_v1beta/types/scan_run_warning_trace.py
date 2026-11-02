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
    package="google.cloud.websecurityscanner.v1beta",
    manifest={
        "ScanRunWarningTrace",
    },
)


class ScanRunWarningTrace(proto.Message):
    r"""Output only.
    Defines a warning trace message for ScanRun. Warning traces
    provide customers with useful information that helps make the
    scanning process more effective.

    Attributes:
        code (google.cloud.websecurityscanner_v1beta.types.ScanRunWarningTrace.Code):
            Indicates the warning code.
    """

    class Code(proto.Enum):
        r"""Output only.
        Defines a warning message code.
        Next id: 6

        Values:
            CODE_UNSPECIFIED (0):
                Default value is never used.
            INSUFFICIENT_CRAWL_RESULTS (1):
                Indicates that a scan discovered an
                unexpectedly low number of URLs. This is
                sometimes caused by complex navigation features
                or by using a single URL for numerous pages.
            TOO_MANY_CRAWL_RESULTS (2):
                Indicates that a scan discovered too many
                URLs to test, or excessive redundant URLs.
            TOO_MANY_FUZZ_TASKS (3):
                Indicates that too many tests have been
                generated for the scan. Customer should try
                reducing the number of starting URLs, increasing
                the QPS rate, or narrowing down the scope of the
                scan using the excluded patterns.
            BLOCKED_BY_IAP (4):
                Indicates that a scan is blocked by IAP.
        """

        CODE_UNSPECIFIED = 0
        INSUFFICIENT_CRAWL_RESULTS = 1
        TOO_MANY_CRAWL_RESULTS = 2
        TOO_MANY_FUZZ_TASKS = 3
        BLOCKED_BY_IAP = 4

    code: Code = proto.Field(
        proto.ENUM,
        number=1,
        enum=Code,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
