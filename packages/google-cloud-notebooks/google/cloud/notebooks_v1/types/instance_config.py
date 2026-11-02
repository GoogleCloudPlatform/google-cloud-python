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
    package="google.cloud.notebooks.v1",
    manifest={
        "InstanceConfig",
    },
)


class InstanceConfig(proto.Message):
    r"""Notebook instance configurations that can be updated.

    Attributes:
        notebook_upgrade_schedule (str):
            Cron expression in UTC timezone, used to schedule instance
            auto upgrade. Please follow the `cron
            format <https://en.wikipedia.org/wiki/Cron>`__.
        enable_health_monitoring (bool):
            Verifies core internal services are running.
    """

    notebook_upgrade_schedule: str = proto.Field(
        proto.STRING,
        number=1,
    )
    enable_health_monitoring: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
