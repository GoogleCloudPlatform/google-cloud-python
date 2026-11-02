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
    package="google.monitoring.metricsscope.v1",
    manifest={
        "MetricsScope",
        "MonitoredProject",
    },
)


class MetricsScope(proto.Message):
    r"""Represents a `Metrics
    Scope <https://cloud.google.com/monitoring/settings#concept-scope>`__
    in Cloud Monitoring, which specifies one or more Google projects and
    zero or more AWS accounts to monitor together.

    Attributes:
        name (str):
            Immutable. The resource name of the Monitoring Metrics
            Scope. On input, the resource name can be specified with the
            scoping project ID or number. On output, the resource name
            is specified with the scoping project number. Example:
            ``locations/global/metricsScopes/{SCOPING_PROJECT_ID_OR_NUMBER}``
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when this ``Metrics Scope`` was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when this ``Metrics Scope`` record was
            last updated.
        monitored_projects (MutableSequence[google.cloud.monitoring_metrics_scope_v1.types.MonitoredProject]):
            Output only. The list of projects monitored by this
            ``Metrics Scope``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    monitored_projects: MutableSequence["MonitoredProject"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="MonitoredProject",
    )


class MonitoredProject(proto.Message):
    r"""A `project being
    monitored <https://cloud.google.com/monitoring/settings/multiple-projects#create-multi>`__
    by a ``Metrics Scope``.

    Attributes:
        name (str):
            Immutable. The resource name of the ``MonitoredProject``. On
            input, the resource name includes the scoping project ID and
            monitored project ID. On output, it contains the equivalent
            project numbers. Example:
            ``locations/global/metricsScopes/{SCOPING_PROJECT_ID_OR_NUMBER}/projects/{MONITORED_PROJECT_ID_OR_NUMBER}``
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when this ``MonitoredProject`` was
            created.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
