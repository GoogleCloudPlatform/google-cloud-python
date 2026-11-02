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
    package="google.cloud.visionai.v1alpha1",
    manifest={
        "Cluster",
        "OperationMetadata",
        "GcsSource",
    },
)


class Cluster(proto.Message):
    r"""Message describing the Cluster object.

    Attributes:
        name (str):
            Output only. Name of the resource.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The create timestamp.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The update timestamp.
        labels (MutableMapping[str, str]):
            Labels as key value pairs
        annotations (MutableMapping[str, str]):
            Annotations to allow clients to store small
            amounts of arbitrary data.
        dataplane_service_endpoint (str):
            Output only. The DNS name of the data plane
            service
        state (google.cloud.visionai_v1alpha1.types.Cluster.State):
            Output only. The current state of the
            cluster.
        psc_target (str):
            Output only. The private service connection
            service target name.
    """

    class State(proto.Enum):
        r"""The current state of the cluster.

        Values:
            STATE_UNSPECIFIED (0):
                Not set.
            PROVISIONING (1):
                The PROVISIONING state indicates the cluster
                is being created.
            RUNNING (2):
                The RUNNING state indicates the cluster has
                been created and is fully usable.
            STOPPING (3):
                The STOPPING state indicates the cluster is
                being deleted.
            ERROR (4):
                The ERROR state indicates the cluster is
                unusable. It will be automatically deleted.
        """

        STATE_UNSPECIFIED = 0
        PROVISIONING = 1
        RUNNING = 2
        STOPPING = 3
        ERROR = 4

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
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    dataplane_service_endpoint: str = proto.Field(
        proto.STRING,
        number=6,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=7,
        enum=State,
    )
    psc_target: str = proto.Field(
        proto.STRING,
        number=8,
    )


class OperationMetadata(proto.Message):
    r"""Represents the metadata of the long-running operation.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation was
            created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation finished
            running.
        target (str):
            Output only. Server-defined resource path for
            the target of the operation.
        verb (str):
            Output only. Name of the verb executed by the
            operation.
        status_message (str):
            Output only. Human-readable status of the
            operation, if any.
        requested_cancellation (bool):
            Output only. Identifies whether the user has requested
            cancellation of the operation. Operations that have
            successfully been cancelled have [Operation.error][] value
            with a [google.rpc.Status.code][google.rpc.Status.code] of
            1, corresponding to ``Code.CANCELLED``.
        api_version (str):
            Output only. API version used to start the
            operation.
    """

    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    target: str = proto.Field(
        proto.STRING,
        number=3,
    )
    verb: str = proto.Field(
        proto.STRING,
        number=4,
    )
    status_message: str = proto.Field(
        proto.STRING,
        number=5,
    )
    requested_cancellation: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    api_version: str = proto.Field(
        proto.STRING,
        number=7,
    )


class GcsSource(proto.Message):
    r"""The Google Cloud Storage location for the input content.

    Attributes:
        uris (MutableSequence[str]):
            Required. References to a Google Cloud
            Storage paths.
    """

    uris: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
