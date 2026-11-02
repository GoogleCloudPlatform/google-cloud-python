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

from google.cloud.visionai_v1.types import lva

__protobuf__ = proto.module(
    package="google.cloud.visionai.v1",
    manifest={
        "Operator",
        "Analysis",
        "Process",
    },
)


class Operator(proto.Message):
    r"""Message describing the Operator object.

    Attributes:
        name (str):
            Name of the resource.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The create timestamp.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The update timestamp.
        labels (MutableMapping[str, str]):
            Labels as key value pairs.
        operator_definition (google.cloud.visionai_v1.types.OperatorDefinition):
            The definition of the operator.
        docker_image (str):
            The link to the docker image of the operator.
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
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    operator_definition: lva.OperatorDefinition = proto.Field(
        proto.MESSAGE,
        number=5,
        message=lva.OperatorDefinition,
    )
    docker_image: str = proto.Field(
        proto.STRING,
        number=6,
    )


class Analysis(proto.Message):
    r"""Message describing the Analysis object.

    Attributes:
        name (str):
            The name of resource.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The create timestamp.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The update timestamp.
        labels (MutableMapping[str, str]):
            Labels as key value pairs.
        analysis_definition (google.cloud.visionai_v1.types.AnalysisDefinition):
            The definition of the analysis.
        input_streams_mapping (MutableMapping[str, str]):
            Map from the input parameter in the definition to the real
            stream. E.g., suppose you had a stream source operator named
            "input-0" and you try to receive from the real stream
            "stream-0". You can add the following mapping: [input-0:
            stream-0].
        output_streams_mapping (MutableMapping[str, str]):
            Map from the output parameter in the definition to the real
            stream. E.g., suppose you had a stream sink operator named
            "output-0" and you try to send to the real stream
            "stream-0". You can add the following mapping: [output-0:
            stream-0].
        disable_event_watch (bool):
            Boolean flag to indicate whether you would
            like to disable the ability to automatically
            start a Process when new event happening in the
            input Stream. If you would like to start a
            Process manually, the field needs to be set to
            true.
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
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    analysis_definition: lva.AnalysisDefinition = proto.Field(
        proto.MESSAGE,
        number=5,
        message=lva.AnalysisDefinition,
    )
    input_streams_mapping: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=6,
    )
    output_streams_mapping: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=7,
    )
    disable_event_watch: bool = proto.Field(
        proto.BOOL,
        number=8,
    )


class Process(proto.Message):
    r"""Message describing the Process object.

    Attributes:
        name (str):
            The name of resource.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The create timestamp.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The update timestamp.
        analysis (str):
            Required. Reference to an existing Analysis
            resource.
        attribute_overrides (MutableSequence[str]):
            Optional. Attribute overrides of the Analyzers. Format for
            each single override item:
            "{analyzer_name}:{attribute_key}={value}".
        run_status (google.cloud.visionai_v1.types.RunStatus):
            Optional. Status of the Process.
        run_mode (google.cloud.visionai_v1.types.RunMode):
            Optional. Run mode of the Process.
        event_id (str):
            Optional. Event ID of the input/output
            streams. This is useful when you have a
            StreamSource/StreamSink operator in the
            Analysis, and you want to manually specify the
            Event to read from/write to.
        batch_id (str):
            Optional. Optional: Batch ID of the Process.
        retry_count (int):
            Optional. Optional: The number of retries for
            a process in submission mode the system should
            try before declaring failure. By default, no
            retry will be performed.
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
    analysis: str = proto.Field(
        proto.STRING,
        number=4,
    )
    attribute_overrides: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    run_status: lva.RunStatus = proto.Field(
        proto.MESSAGE,
        number=6,
        message=lva.RunStatus,
    )
    run_mode: lva.RunMode = proto.Field(
        proto.ENUM,
        number=7,
        enum=lva.RunMode,
    )
    event_id: str = proto.Field(
        proto.STRING,
        number=8,
    )
    batch_id: str = proto.Field(
        proto.STRING,
        number=9,
    )
    retry_count: int = proto.Field(
        proto.INT32,
        number=10,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
