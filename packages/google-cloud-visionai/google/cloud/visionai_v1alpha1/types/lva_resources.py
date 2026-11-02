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

from google.cloud.visionai_v1alpha1.types import lva

__protobuf__ = proto.module(
    package="google.cloud.visionai.v1alpha1",
    manifest={
        "Analysis",
    },
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
        analysis_definition (google.cloud.visionai_v1alpha1.types.AnalysisDefinition):
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


__all__ = tuple(sorted(__protobuf__.manifest))
