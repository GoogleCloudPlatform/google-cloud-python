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
    package="google.cloud.dataplex.v1",
    manifest={
        "DataScanCatalogPublishingStatus",
    },
)


class DataScanCatalogPublishingStatus(proto.Message):
    r"""The status of publishing the data scan result as Dataplex
    Universal Catalog metadata. Multiple DataScan log events may
    exist, each with different publishing information depending on
    the type of publishing triggered.

    Attributes:
        state (google.cloud.dataplex_v1.types.DataScanCatalogPublishingStatus.State):
            Output only. Execution state for publishing.
    """

    class State(proto.Enum):
        r"""Execution state for the publishing.

        Values:
            STATE_UNSPECIFIED (0):
                The publishing state is unspecified.
            SUCCEEDED (1):
                Publishing to catalog completed successfully.
            FAILED (2):
                Publish to catalog failed.
            SKIPPED (3):
                Publishing to catalog was skipped.
        """

        STATE_UNSPECIFIED = 0
        SUCCEEDED = 1
        FAILED = 2
        SKIPPED = 3

    state: State = proto.Field(
        proto.ENUM,
        number=1,
        enum=State,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
