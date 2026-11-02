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
    package="google.monitoring.dashboard.v1",
    manifest={
        "LogsPanel",
    },
)


class LogsPanel(proto.Message):
    r"""A widget that displays a stream of log.

    Attributes:
        filter (str):
            A filter that chooses which log entries to return. See
            `Advanced Logs
            Queries <https://cloud.google.com/logging/docs/view/advanced-queries>`__.
            Only log entries that match the filter are returned. An
            empty filter matches all log entries.
        resource_names (MutableSequence[str]):
            The names of logging resources to collect
            logs for. Currently only projects are supported.
            If empty, the widget will default to the host
            project.
    """

    filter: str = proto.Field(
        proto.STRING,
        number=1,
    )
    resource_names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
