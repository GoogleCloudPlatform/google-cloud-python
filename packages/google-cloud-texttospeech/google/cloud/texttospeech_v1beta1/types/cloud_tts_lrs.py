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

from google.cloud.texttospeech_v1beta1.types import cloud_tts

__protobuf__ = proto.module(
    package="google.cloud.texttospeech.v1beta1",
    manifest={
        "SynthesizeLongAudioRequest",
        "SynthesizeLongAudioResponse",
        "SynthesizeLongAudioMetadata",
    },
)


class SynthesizeLongAudioRequest(proto.Message):
    r"""The top-level message sent by the client for the
    ``SynthesizeLongAudio`` method.

    Attributes:
        parent (str):
            The resource states of the request in the form of
            ``projects/*/locations/*``.
        input (google.cloud.texttospeech_v1beta1.types.SynthesisInput):
            Required. The Synthesizer requires either
            plain text or SSML as input.
        audio_config (google.cloud.texttospeech_v1beta1.types.AudioConfig):
            Required. The configuration of the
            synthesized audio.
        output_gcs_uri (str):
            Required. Specifies a Cloud Storage URI for the synthesis
            results. Must be specified in the format:
            ``gs://bucket_name/object_name``, and the bucket must
            already exist.
        voice (google.cloud.texttospeech_v1beta1.types.VoiceSelectionParams):
            Required. The desired voice of the
            synthesized audio.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    input: cloud_tts.SynthesisInput = proto.Field(
        proto.MESSAGE,
        number=2,
        message=cloud_tts.SynthesisInput,
    )
    audio_config: cloud_tts.AudioConfig = proto.Field(
        proto.MESSAGE,
        number=3,
        message=cloud_tts.AudioConfig,
    )
    output_gcs_uri: str = proto.Field(
        proto.STRING,
        number=4,
    )
    voice: cloud_tts.VoiceSelectionParams = proto.Field(
        proto.MESSAGE,
        number=5,
        message=cloud_tts.VoiceSelectionParams,
    )


class SynthesizeLongAudioResponse(proto.Message):
    r"""The message returned to the client by the ``SynthesizeLongAudio``
    method.

    """


class SynthesizeLongAudioMetadata(proto.Message):
    r"""Metadata for response returned by the ``SynthesizeLongAudio``
    method.

    Attributes:
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Time when the request was received.
        last_update_time (google.protobuf.timestamp_pb2.Timestamp):
            Deprecated. Do not use.
        progress_percentage (float):
            The progress of the most recent processing
            update in percentage, ie. 70.0%.
    """

    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    last_update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    progress_percentage: float = proto.Field(
        proto.DOUBLE,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
