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

import google.type.date_pb2 as date_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "DateRange",
    },
)


class DateRange(proto.Message):
    r"""A date range with fixed start and end dates (e.g. 2021-06-01
    - 2021-06-30).

    Attributes:
        start_date (google.type.date_pb2.Date):
            The start of the date range.
        end_date (google.type.date_pb2.Date):
            The end of the date range.
    """

    start_date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=1,
        message=date_pb2.Date,
    )
    end_date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=2,
        message=date_pb2.Date,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
