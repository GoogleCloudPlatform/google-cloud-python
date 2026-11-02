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

import google.type.localized_text_pb2 as localized_text_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.maps.routing.v2",
    manifest={
        "LocalizedTime",
    },
)


class LocalizedTime(proto.Message):
    r"""Localized description of time.

    Attributes:
        time (google.type.localized_text_pb2.LocalizedText):
            The time specified as a string in a given
            time zone.
        time_zone (str):
            Contains the time zone. The value is the name of the time
            zone as defined in the `IANA Time Zone
            Database <http://www.iana.org/time-zones>`__, e.g.
            "America/New_York".
    """

    time: localized_text_pb2.LocalizedText = proto.Field(
        proto.MESSAGE,
        number=1,
        message=localized_text_pb2.LocalizedText,
    )
    time_zone: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
