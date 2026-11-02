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
    package="google.backstory",
    manifest={
        "Id",
    },
)


class Id(proto.Message):
    r"""Identifier to identify a UDM object like a UDM event, Entity,
    Collection. The full identifier for persistence is created by
    setting the 32 most significant bits as the Id.Namespace enum
    This is a convenience wrapper to define the id space enum values
    and provide an easy interface for RPCs, most persistence use
    cases should use a denormalized form.

    Attributes:
        namespace (google.backstory.types.Id.Namespace):
            Namespace the id belongs to.
        id (bytes):
            Full raw ID.
        string_id (str):
            Some ids are stored as strings that are not able to be
            translated to bytes, so store these separately. Ex.
            detection id of the form de_aaaaaaaa-aaaa...
    """

    class Namespace(proto.Enum):
        r"""Extracted Namespace Component

        Values:
            NORMALIZED_TELEMETRY (0):
                Ingested and Normalized telemetry events
            RAW_TELEMETRY (1):
                Ingested Raw telemetry
            RULE_DETECTIONS (2):
                Chronicle Rules engine
            UPPERCASE (3):
                Uppercase
            MACHINE_INTELLIGENCE (4):
                DSML - Machine Intelligence
            SECURITY_COMMAND_CENTER (5):
                A normalized telemetry event from Google
                Security Command Center.
            UNSPECIFIED (6):
                Unspecified Namespace
            SOAR_ALERT (7):
                An alert coming from other SIEMs via
                Chronicle SOAR.
            VIRUS_TOTAL (8):
                VirusTotal.
        """

        NORMALIZED_TELEMETRY = 0
        RAW_TELEMETRY = 1
        RULE_DETECTIONS = 2
        UPPERCASE = 3
        MACHINE_INTELLIGENCE = 4
        SECURITY_COMMAND_CENTER = 5
        UNSPECIFIED = 6
        SOAR_ALERT = 7
        VIRUS_TOTAL = 8

    namespace: Namespace = proto.Field(
        proto.ENUM,
        number=1,
        enum=Namespace,
    )
    id: bytes = proto.Field(
        proto.BYTES,
        number=2,
    )
    string_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
