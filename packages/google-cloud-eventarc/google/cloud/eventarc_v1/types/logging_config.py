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
    package="google.cloud.eventarc.v1",
    manifest={
        "LoggingConfig",
    },
)


class LoggingConfig(proto.Message):
    r"""The configuration for Platform Telemetry logging for Eventarc
    Advanced resources.

    Attributes:
        log_severity (google.cloud.eventarc_v1.types.LoggingConfig.LogSeverity):
            Optional. The minimum severity of logs that
            will be sent to Stackdriver/Platform Telemetry.
            Logs at severitiy ≥ this value will be sent,
            unless it is NONE.
    """

    class LogSeverity(proto.Enum):
        r"""The different severities for logging supported by Eventarc
        Advanced resources.
        This enum is an exhaustive list of log severities and is FROZEN.
        Do not expect new values to be added.

        Values:
            LOG_SEVERITY_UNSPECIFIED (0):
                Log severity is not specified. This value is treated the
                same as NONE, but is used to distinguish between no update
                and update to NONE in update_masks.
            NONE (1):
                Default value at resource creation, presence
                of this value must be treated as no
                logging/disable logging.
            DEBUG (2):
                Debug or trace level logging.
            INFO (3):
                Routine information, such as ongoing status
                or performance.
            NOTICE (4):
                Normal but significant events, such as start
                up, shut down, or a configuration change.
            WARNING (5):
                Warning events might cause problems.
            ERROR (6):
                Error events are likely to cause problems.
            CRITICAL (7):
                Critical events cause more severe problems or
                outages.
            ALERT (8):
                A person must take action immediately.
            EMERGENCY (9):
                One or more systems are unusable.
        """

        LOG_SEVERITY_UNSPECIFIED = 0
        NONE = 1
        DEBUG = 2
        INFO = 3
        NOTICE = 4
        WARNING = 5
        ERROR = 6
        CRITICAL = 7
        ALERT = 8
        EMERGENCY = 9

    log_severity: LogSeverity = proto.Field(
        proto.ENUM,
        number=1,
        enum=LogSeverity,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
