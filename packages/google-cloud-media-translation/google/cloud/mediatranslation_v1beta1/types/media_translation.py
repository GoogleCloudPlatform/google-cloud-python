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

import google.rpc.status_pb2 as status_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.mediatranslation.v1beta1",
    manifest={
        "TranslateSpeechConfig",
        "StreamingTranslateSpeechConfig",
        "StreamingTranslateSpeechRequest",
        "StreamingTranslateSpeechResult",
        "StreamingTranslateSpeechResponse",
    },
)


class TranslateSpeechConfig(proto.Message):
    r"""Provides information to the speech translation that specifies
    how to process the request.

    Attributes:
        audio_encoding (str):
            Required. Encoding of audio data. Supported formats:

            - ``linear16``

              Uncompressed 16-bit signed little-endian samples (Linear
              PCM).

            - ``flac``

              ``flac`` (Free Lossless Audio Codec) is the recommended
              encoding because it is lossless--therefore recognition is
              not compromised--and requires only about half the
              bandwidth of ``linear16``.

            - ``mulaw``

              8-bit samples that compand 14-bit audio samples using
              G.711 PCMU/mu-law.

            - ``amr``

              Adaptive Multi-Rate Narrowband codec.
              ``sample_rate_hertz`` must be 8000.

            - ``amr-wb``

              Adaptive Multi-Rate Wideband codec. ``sample_rate_hertz``
              must be 16000.

            - ``ogg-opus``

              Opus encoded audio frames in
              `Ogg <https://wikipedia.org/wiki/Ogg>`__ container.
              ``sample_rate_hertz`` must be one of 8000, 12000, 16000,
              24000, or 48000.

            - ``mp3``

              MP3 audio. Support all standard MP3 bitrates (which range
              from 32-320 kbps). When using this encoding,
              ``sample_rate_hertz`` has to match the sample rate of the
              file being used.
        source_language_code (str):
            Required. Source language code (BCP-47) of
            the input audio.
        target_language_code (str):
            Required. Target language code (BCP-47) of
            the output.
        sample_rate_hertz (int):
            Optional. Sample rate in Hertz of the audio
            data. Valid values are: 8000-48000. 16000 is
            optimal. For best results, set the sampling rate
            of the audio source to 16000 Hz. If that's not
            possible, use the native sample rate of the
            audio source (instead of re-sampling).
        model (str):
            Optional. ``google-provided-model/video`` and
            ``google-provided-model/enhanced-phone-call`` are premium
            models. ``google-provided-model/phone-call`` is not premium
            model.
    """

    audio_encoding: str = proto.Field(
        proto.STRING,
        number=1,
    )
    source_language_code: str = proto.Field(
        proto.STRING,
        number=2,
    )
    target_language_code: str = proto.Field(
        proto.STRING,
        number=3,
    )
    sample_rate_hertz: int = proto.Field(
        proto.INT32,
        number=4,
    )
    model: str = proto.Field(
        proto.STRING,
        number=5,
    )


class StreamingTranslateSpeechConfig(proto.Message):
    r"""Config used for streaming translation.

    Attributes:
        audio_config (google.cloud.mediatranslation_v1beta1.types.TranslateSpeechConfig):
            Required. The common config for all the
            following audio contents.
        single_utterance (bool):
            Optional. If ``false`` or omitted, the system performs
            continuous translation (continuing to wait for and process
            audio even if the user pauses speaking) until the client
            closes the input stream (gRPC API) or until the maximum time
            limit has been reached. May return multiple
            ``StreamingTranslateSpeechResult``\ s with the ``is_final``
            flag set to ``true``.

            If ``true``, the speech translator will detect a single
            spoken utterance. When it detects that the user has paused
            or stopped speaking, it will return an
            ``END_OF_SINGLE_UTTERANCE`` event and cease translation.
            When the client receives 'END_OF_SINGLE_UTTERANCE' event,
            the client should stop sending the requests. However,
            clients should keep receiving remaining responses until the
            stream is terminated. To construct the complete sentence in
            a streaming way, one should override (if 'is_final' of
            previous response is false), or append (if 'is_final' of
            previous response is true).
    """

    audio_config: "TranslateSpeechConfig" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="TranslateSpeechConfig",
    )
    single_utterance: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class StreamingTranslateSpeechRequest(proto.Message):
    r"""The top-level message sent by the client for the
    ``StreamingTranslateSpeech`` method. Multiple
    ``StreamingTranslateSpeechRequest`` messages are sent. The first
    message must contain a ``streaming_config`` message and must not
    contain ``audio_content`` data. All subsequent messages must contain
    ``audio_content`` data and must not contain a ``streaming_config``
    message.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        streaming_config (google.cloud.mediatranslation_v1beta1.types.StreamingTranslateSpeechConfig):
            Provides information to the recognizer that specifies how to
            process the request. The first
            ``StreamingTranslateSpeechRequest`` message must contain a
            ``streaming_config`` message.

            This field is a member of `oneof`_ ``streaming_request``.
        audio_content (bytes):
            The audio data to be translated. Sequential chunks of audio
            data are sent in sequential
            ``StreamingTranslateSpeechRequest`` messages. The first
            ``StreamingTranslateSpeechRequest`` message must not contain
            ``audio_content`` data and all subsequent
            ``StreamingTranslateSpeechRequest`` messages must contain
            ``audio_content`` data. The audio bytes must be encoded as
            specified in ``StreamingTranslateSpeechConfig``. Note: as
            with all bytes fields, protobuffers use a pure binary
            representation (not base64).

            This field is a member of `oneof`_ ``streaming_request``.
    """

    streaming_config: "StreamingTranslateSpeechConfig" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="streaming_request",
        message="StreamingTranslateSpeechConfig",
    )
    audio_content: bytes = proto.Field(
        proto.BYTES,
        number=2,
        oneof="streaming_request",
    )


class StreamingTranslateSpeechResult(proto.Message):
    r"""A streaming speech translation result corresponding to a
    portion of the audio that is currently being processed.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        text_translation_result (google.cloud.mediatranslation_v1beta1.types.StreamingTranslateSpeechResult.TextTranslationResult):
            Text translation result.

            This field is a member of `oneof`_ ``result``.
    """

    class TextTranslationResult(proto.Message):
        r"""Text translation result.

        Attributes:
            translation (str):
                Output only. The translated sentence.
            is_final (bool):
                Output only. If ``false``, this
                ``StreamingTranslateSpeechResult`` represents an interim
                result that may change. If ``true``, this is the final time
                the translation service will return this particular
                ``StreamingTranslateSpeechResult``, the streaming translator
                will not return any further hypotheses for this portion of
                the transcript and corresponding audio.
        """

        translation: str = proto.Field(
            proto.STRING,
            number=1,
        )
        is_final: bool = proto.Field(
            proto.BOOL,
            number=2,
        )

    text_translation_result: TextTranslationResult = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="result",
        message=TextTranslationResult,
    )


class StreamingTranslateSpeechResponse(proto.Message):
    r"""A streaming speech translation response corresponding to a
    portion of the audio currently processed.

    Attributes:
        error (google.rpc.status_pb2.Status):
            Output only. If set, returns a
            [google.rpc.Status][google.rpc.Status] message that
            specifies the error for the operation.
        result (google.cloud.mediatranslation_v1beta1.types.StreamingTranslateSpeechResult):
            Output only. The translation result that is currently being
            processed (is_final could be true or false).
        speech_event_type (google.cloud.mediatranslation_v1beta1.types.StreamingTranslateSpeechResponse.SpeechEventType):
            Output only. Indicates the type of speech
            event.
    """

    class SpeechEventType(proto.Enum):
        r"""Indicates the type of speech event.

        Values:
            SPEECH_EVENT_TYPE_UNSPECIFIED (0):
                No speech event specified.
            END_OF_SINGLE_UTTERANCE (1):
                This event indicates that the server has detected the end of
                the user's speech utterance and expects no additional
                speech. Therefore, the server will not process additional
                audio (although it may subsequently return additional
                results). When the client receives 'END_OF_SINGLE_UTTERANCE'
                event, the client should stop sending the requests. However,
                clients should keep receiving remaining responses until the
                stream is terminated. To construct the complete sentence in
                a streaming way, one should override (if 'is_final' of
                previous response is false), or append (if 'is_final' of
                previous response is true). This event is only sent if
                ``single_utterance`` was set to ``true``, and is not used
                otherwise.
        """

        SPEECH_EVENT_TYPE_UNSPECIFIED = 0
        END_OF_SINGLE_UTTERANCE = 1

    error: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=1,
        message=status_pb2.Status,
    )
    result: "StreamingTranslateSpeechResult" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="StreamingTranslateSpeechResult",
    )
    speech_event_type: SpeechEventType = proto.Field(
        proto.ENUM,
        number=3,
        enum=SpeechEventType,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
