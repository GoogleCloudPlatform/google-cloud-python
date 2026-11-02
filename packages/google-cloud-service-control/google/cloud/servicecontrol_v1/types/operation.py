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

import google.protobuf.any_pb2 as any_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.servicecontrol_v1.types import log_entry, metric_value

__protobuf__ = proto.module(
    package="google.api.servicecontrol.v1",
    manifest={
        "Operation",
    },
)


class Operation(proto.Message):
    r"""Represents information regarding an operation.

    Attributes:
        operation_id (str):
            Identity of the operation. This must be
            unique within the scope of the service that
            generated the operation. If the service calls
            Check() and Report() on the same operation, the
            two calls should carry the same id.

            UUID version 4 is recommended, though not
            required. In scenarios where an operation is
            computed from existing information and an
            idempotent id is desirable for deduplication
            purpose, UUID version 5 is recommended. See RFC
            4122 for details.
        operation_name (str):
            Fully qualified name of the operation.
            Reserved for future use.
        consumer_id (str):
            Identity of the consumer who is using the service. This
            field should be filled in for the operations initiated by a
            consumer, but not for service-initiated operations that are
            not related to a specific consumer.

            - This can be in one of the following formats:

              - project:PROJECT_ID,
              - project\ ``_``\ number:PROJECT_NUMBER,
              - projects/PROJECT_ID or PROJECT_NUMBER,
              - folders/FOLDER_NUMBER,
              - organizations/ORGANIZATION_NUMBER,
              - api\ ``_``\ key:API_KEY.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Required. Start time of the operation.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            End time of the operation. Required when the operation is
            used in
            [ServiceController.Report][google.api.servicecontrol.v1.ServiceController.Report],
            but optional when the operation is used in
            [ServiceController.Check][google.api.servicecontrol.v1.ServiceController.Check].
        labels (MutableMapping[str, str]):
            Labels describing the operation. Only the following labels
            are allowed:

            - Labels describing monitored resources as defined in the
              service configuration.
            - Default labels of metric values. When specified, labels
              defined in the metric value override these default.
            - The following labels defined by Google Cloud Platform:

              - ``cloud.googleapis.com/location`` describing the
                location where the operation happened,
              - ``servicecontrol.googleapis.com/user_agent`` describing
                the user agent of the API request,
              - ``servicecontrol.googleapis.com/service_agent``
                describing the service used to handle the API request
                (e.g. ESP),
              - ``servicecontrol.googleapis.com/platform`` describing
                the platform where the API is served, such as App
                Engine, Compute Engine, or Kubernetes Engine.
        metric_value_sets (MutableSequence[google.cloud.servicecontrol_v1.types.MetricValueSet]):
            Represents information about this operation.
            Each MetricValueSet corresponds to a metric
            defined in the service configuration. The data
            type used in the MetricValueSet must agree with
            the data type specified in the metric
            definition.

            Within a single operation, it is not allowed to
            have more than one MetricValue instances that
            have the same metric names and identical label
            value combinations. If a request has such
            duplicated MetricValue instances, the entire
            request is rejected with an invalid argument
            error.
        log_entries (MutableSequence[google.cloud.servicecontrol_v1.types.LogEntry]):
            Represents information to be logged.
        importance (google.cloud.servicecontrol_v1.types.Operation.Importance):
            DO NOT USE. This is an experimental field.
        user_labels (MutableMapping[str, str]):
            Private Preview. This feature is only
            available for approved services.
            User defined labels for the resource that this
            operation is associated with.
        extensions (MutableSequence[google.protobuf.any_pb2.Any]):
            Unimplemented.
    """

    class Importance(proto.Enum):
        r"""Defines the importance of the data contained in the
        operation.

        Values:
            LOW (0):
                Allows data caching, batching, and
                aggregation. It provides higher performance with
                higher data loss risk.
            HIGH (1):
                Disables data aggregation to minimize data
                loss. It is for operations that contains
                significant monetary value or audit trail. This
                feature only applies to the client libraries.
        """

        LOW = 0
        HIGH = 1

    operation_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    operation_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    consumer_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=6,
    )
    metric_value_sets: MutableSequence[metric_value.MetricValueSet] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=7,
            message=metric_value.MetricValueSet,
        )
    )
    log_entries: MutableSequence[log_entry.LogEntry] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message=log_entry.LogEntry,
    )
    importance: Importance = proto.Field(
        proto.ENUM,
        number=11,
        enum=Importance,
    )
    user_labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=12,
    )
    extensions: MutableSequence[any_pb2.Any] = proto.RepeatedField(
        proto.MESSAGE,
        number=16,
        message=any_pb2.Any,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
