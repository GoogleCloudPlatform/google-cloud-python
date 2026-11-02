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
    package="google.cloud.datacatalog.v1beta1",
    manifest={
        "UsageStats",
        "UsageSignal",
    },
)


class UsageStats(proto.Message):
    r"""Detailed counts on the entry's usage.
    Caveats:

    - Only BigQuery tables have usage stats
    - The usage stats only include BigQuery query jobs
    - The usage stats might be underestimated, e.g. wildcard table
      references are not yet counted in usage computation
    https://cloud.google.com/bigquery/docs/querying-wildcard-tables

    Attributes:
        total_completions (float):
            The number of times that the underlying entry
            was successfully used.
        total_failures (float):
            The number of times that the underlying entry
            was attempted to be used but failed.
        total_cancellations (float):
            The number of times that the underlying entry
            was attempted to be used but was cancelled by
            the user.
        total_execution_time_for_completions_millis (float):
            Total time spent (in milliseconds) during
            uses the resulted in completions.
    """

    total_completions: float = proto.Field(
        proto.FLOAT,
        number=1,
    )
    total_failures: float = proto.Field(
        proto.FLOAT,
        number=2,
    )
    total_cancellations: float = proto.Field(
        proto.FLOAT,
        number=3,
    )
    total_execution_time_for_completions_millis: float = proto.Field(
        proto.FLOAT,
        number=4,
    )


class UsageSignal(proto.Message):
    r"""The set of all usage signals that we store in Data Catalog.

    Attributes:
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            The timestamp of the end of the usage
            statistics duration.
        usage_within_time_range (MutableMapping[str, google.cloud.datacatalog_v1beta1.types.UsageStats]):
            Usage statistics over each of the pre-defined
            time ranges, supported strings for time ranges
            are {"24H", "7D", "30D"}.
    """

    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    usage_within_time_range: MutableMapping[str, "UsageStats"] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=2,
        message="UsageStats",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
