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

from google.cloud.monitoring_metrics_scope_v1.types import metrics_scope

__protobuf__ = proto.module(
    package="google.monitoring.metricsscope.v1",
    manifest={
        "GetMetricsScopeRequest",
        "ListMetricsScopesByMonitoredProjectRequest",
        "ListMetricsScopesByMonitoredProjectResponse",
        "CreateMonitoredProjectRequest",
        "DeleteMonitoredProjectRequest",
        "OperationMetadata",
    },
)


class GetMetricsScopeRequest(proto.Message):
    r"""Request for the ``GetMetricsScope`` method.

    Attributes:
        name (str):
            Required. The resource name of the ``Metrics Scope``.
            Example:
            ``locations/global/metricsScopes/{SCOPING_PROJECT_ID_OR_NUMBER}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListMetricsScopesByMonitoredProjectRequest(proto.Message):
    r"""Request for the ``ListMetricsScopesByMonitoredProject`` method.

    Attributes:
        monitored_resource_container (str):
            Required. The resource name of the ``Monitored Project``
            being requested. Example:
            ``projects/{MONITORED_PROJECT_ID_OR_NUMBER}``
    """

    monitored_resource_container: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListMetricsScopesByMonitoredProjectResponse(proto.Message):
    r"""Response for the ``ListMetricsScopesByMonitoredProject`` method.

    Attributes:
        metrics_scopes (MutableSequence[google.cloud.monitoring_metrics_scope_v1.types.MetricsScope]):
            A set of all metrics scopes that the
            specified monitored project has been added to.
    """

    metrics_scopes: MutableSequence[metrics_scope.MetricsScope] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=metrics_scope.MetricsScope,
    )


class CreateMonitoredProjectRequest(proto.Message):
    r"""Request for the ``CreateMonitoredProject`` method.

    Attributes:
        parent (str):
            Required. The resource name of the existing
            ``Metrics Scope`` that will monitor this project. Example:
            ``locations/global/metricsScopes/{SCOPING_PROJECT_ID_OR_NUMBER}``
        monitored_project (google.cloud.monitoring_metrics_scope_v1.types.MonitoredProject):
            Required. The initial ``MonitoredProject`` configuration.
            Specify only the ``monitored_project.name`` field. All other
            fields are ignored. The ``monitored_project.name`` must be
            in the format:
            ``locations/global/metricsScopes/{SCOPING_PROJECT_ID_OR_NUMBER}/projects/{MONITORED_PROJECT_ID_OR_NUMBER}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    monitored_project: metrics_scope.MonitoredProject = proto.Field(
        proto.MESSAGE,
        number=2,
        message=metrics_scope.MonitoredProject,
    )


class DeleteMonitoredProjectRequest(proto.Message):
    r"""Request for the ``DeleteMonitoredProject`` method.

    Attributes:
        name (str):
            Required. The resource name of the ``MonitoredProject``.
            Example:
            ``locations/global/metricsScopes/{SCOPING_PROJECT_ID_OR_NUMBER}/projects/{MONITORED_PROJECT_ID_OR_NUMBER}``

            Authorization requires the following `Google
            IAM <https://cloud.google.com/iam>`__ permissions on both
            the ``Metrics Scope`` and on the ``MonitoredProject``:
            ``monitoring.metricsScopes.link``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class OperationMetadata(proto.Message):
    r"""Contains metadata for longrunning operation for the edit
    Metrics Scope endpoints.

    Attributes:
        state (google.cloud.monitoring_metrics_scope_v1.types.OperationMetadata.State):
            Current state of the batch operation.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            The time when the batch request was received.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            The time when the operation result was last
            updated.
    """

    class State(proto.Enum):
        r"""Batch operation states.

        Values:
            STATE_UNSPECIFIED (0):
                Invalid.
            CREATED (1):
                Request has been received.
            RUNNING (2):
                Request is actively being processed.
            DONE (3):
                The batch processing is done.
            CANCELLED (4):
                The batch processing was cancelled.
        """

        STATE_UNSPECIFIED = 0
        CREATED = 1
        RUNNING = 2
        DONE = 3
        CANCELLED = 4

    state: State = proto.Field(
        proto.ENUM,
        number=1,
        enum=State,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
