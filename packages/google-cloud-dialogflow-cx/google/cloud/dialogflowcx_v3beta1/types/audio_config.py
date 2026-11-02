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

import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.dialogflow.cx.v3beta1",
    manifest={
        "AudioEncoding",
        "SpeechModelVariant",
        "SsmlVoiceGender",
        "OutputAudioEncoding",
        "SpeechWordInfo",
        "BargeInConfig",
        "InputAudioConfig",
        "VoiceSelectionParams",
        "SynthesizeSpeechConfig",
        "OutputAudioConfig",
        "TextToSpeechSettings",
    },
)


class AudioEncoding(proto.Enum):
    r"""Audio encoding of the audio content sent in the conversational query
    request. Refer to the `Cloud Speech API
    documentation <https://cloud.google.com/speech-to-text/docs/basics>`__
    for more details.

    Values:
        AUDIO_ENCODING_UNSPECIFIED (0):
            Not specified.
        AUDIO_ENCODING_LINEAR_16 (1):
            Uncompressed 16-bit signed little-endian samples (Linear
            PCM). LINT: LEGACY_NAMES
        AUDIO_ENCODING_FLAC (2):
            ```FLAC`` <https://xiph.org/flac/documentation.html>`__
            (Free Lossless Audio Codec) is the recommended encoding
            because it is lossless (therefore recognition is not
            compromised) and requires only about half the bandwidth of
            ``LINEAR16``. ``FLAC`` stream encoding supports 16-bit and
            24-bit samples, however, not all fields in ``STREAMINFO``
            are supported.
        AUDIO_ENCODING_MULAW (3):
            8-bit samples that compand 14-bit audio
            samples using G.711 PCMU/mu-law.
        AUDIO_ENCODING_AMR (4):
            Adaptive Multi-Rate Narrowband codec. ``sample_rate_hertz``
            must be 8000.
        AUDIO_ENCODING_AMR_WB (5):
            Adaptive Multi-Rate Wideband codec. ``sample_rate_hertz``
            must be 16000.
        AUDIO_ENCODING_OGG_OPUS (6):
            Opus encoded audio frames in Ogg container
            (`OggOpus <https://wiki.xiph.org/OggOpus>`__).
            ``sample_rate_hertz`` must be 16000.
        AUDIO_ENCODING_SPEEX_WITH_HEADER_BYTE (7):
            Although the use of lossy encodings is not recommended, if a
            very low bitrate encoding is required, ``OGG_OPUS`` is
            highly preferred over Speex encoding. The
            `Speex <https://speex.org/>`__ encoding supported by
            Dialogflow API has a header byte in each block, as in MIME
            type ``audio/x-speex-with-header-byte``. It is a variant of
            the RTP Speex encoding defined in `RFC
            5574 <https://tools.ietf.org/html/rfc5574>`__. The stream is
            a sequence of blocks, one block per RTP packet. Each block
            starts with a byte containing the length of the block, in
            bytes, followed by one or more frames of Speex data, padded
            to an integral number of bytes (octets) as specified in RFC
            5574. In other words, each RTP header is replaced with a
            single byte containing the block length. Only Speex wideband
            is supported. ``sample_rate_hertz`` must be 16000.
        AUDIO_ENCODING_ALAW (8):
            8-bit samples that compand 13-bit audio
            samples using G.711 PCMU/a-law.
    """

    AUDIO_ENCODING_UNSPECIFIED = 0
    AUDIO_ENCODING_LINEAR_16 = 1
    AUDIO_ENCODING_FLAC = 2
    AUDIO_ENCODING_MULAW = 3
    AUDIO_ENCODING_AMR = 4
    AUDIO_ENCODING_AMR_WB = 5
    AUDIO_ENCODING_OGG_OPUS = 6
    AUDIO_ENCODING_SPEEX_WITH_HEADER_BYTE = 7
    AUDIO_ENCODING_ALAW = 8


class SpeechModelVariant(proto.Enum):
    r"""Variant of the specified [Speech
    model][google.cloud.dialogflow.cx.v3beta1.InputAudioConfig.model] to
    use.

    See the `Cloud Speech
    documentation <https://cloud.google.com/speech-to-text/docs/enhanced-models>`__
    for which models have different variants. For example, the
    "phone_call" model has both a standard and an enhanced variant. When
    you use an enhanced model, you will generally receive higher quality
    results than for a standard model.

    Values:
        SPEECH_MODEL_VARIANT_UNSPECIFIED (0):
            No model variant specified. In this case Dialogflow defaults
            to USE_BEST_AVAILABLE.
        USE_BEST_AVAILABLE (1):
            Use the best available variant of the [Speech
            model][InputAudioConfig.model] that the caller is eligible
            for.
        USE_STANDARD (2):
            Use standard model variant even if an enhanced model is
            available. See the `Cloud Speech
            documentation <https://cloud.google.com/speech-to-text/docs/enhanced-models>`__
            for details about enhanced models.
        USE_ENHANCED (3):
            Use an enhanced model variant:

            - If an enhanced variant does not exist for the given
              [model][google.cloud.dialogflow.cx.v3beta1.InputAudioConfig.model]
              and request language, Dialogflow falls back to the
              standard variant.

              The `Cloud Speech
              documentation <https://cloud.google.com/speech-to-text/docs/enhanced-models>`__
              describes which models have enhanced variants.
    """

    SPEECH_MODEL_VARIANT_UNSPECIFIED = 0
    USE_BEST_AVAILABLE = 1
    USE_STANDARD = 2
    USE_ENHANCED = 3


class SsmlVoiceGender(proto.Enum):
    r"""Gender of the voice as described in `SSML voice
    element <https://www.w3.org/TR/speech-synthesis11/#edef_voice>`__.

    Values:
        SSML_VOICE_GENDER_UNSPECIFIED (0):
            An unspecified gender, which means that the
            client doesn't care which gender the selected
            voice will have.
        SSML_VOICE_GENDER_MALE (1):
            A male voice.
        SSML_VOICE_GENDER_FEMALE (2):
            A female voice.
        SSML_VOICE_GENDER_NEUTRAL (3):
            A gender-neutral voice.
    """

    SSML_VOICE_GENDER_UNSPECIFIED = 0
    SSML_VOICE_GENDER_MALE = 1
    SSML_VOICE_GENDER_FEMALE = 2
    SSML_VOICE_GENDER_NEUTRAL = 3


class OutputAudioEncoding(proto.Enum):
    r"""Audio encoding of the output audio format in Text-To-Speech.

    Values:
        OUTPUT_AUDIO_ENCODING_UNSPECIFIED (0):
            Not specified.
        OUTPUT_AUDIO_ENCODING_LINEAR_16 (1):
            Uncompressed 16-bit signed little-endian samples (Linear
            PCM). Audio content returned as LINEAR16 also contains a WAV
            header. LINT: LEGACY_NAMES
        OUTPUT_AUDIO_ENCODING_MP3 (2):
            MP3 audio at 64kbps.
        OUTPUT_AUDIO_ENCODING_MP3_64_KBPS (4):
            MP3 audio at 64kbps. LINT: LEGACY_NAMES
        OUTPUT_AUDIO_ENCODING_OGG_OPUS (3):
            Opus encoded audio wrapped in an ogg
            container. The result will be a file which can
            be played natively on Android, and in browsers
            (at least Chrome and Firefox). The quality of
            the encoding is considerably higher than MP3
            while using approximately the same bitrate.
        OUTPUT_AUDIO_ENCODING_MULAW (5):
            8-bit samples that compand 14-bit audio
            samples using G.711 PCMU/mu-law.
        OUTPUT_AUDIO_ENCODING_ALAW (6):
            8-bit samples that compand 13-bit audio
            samples using G.711 PCMU/a-law.
    """

    OUTPUT_AUDIO_ENCODING_UNSPECIFIED = 0
    OUTPUT_AUDIO_ENCODING_LINEAR_16 = 1
    OUTPUT_AUDIO_ENCODING_MP3 = 2
    OUTPUT_AUDIO_ENCODING_MP3_64_KBPS = 4
    OUTPUT_AUDIO_ENCODING_OGG_OPUS = 3
    OUTPUT_AUDIO_ENCODING_MULAW = 5
    OUTPUT_AUDIO_ENCODING_ALAW = 6


class SpeechWordInfo(proto.Message):
    r"""Information for a word recognized by the speech recognizer.

    Attributes:
        word (str):
            The word this info is for.
        start_offset (google.protobuf.duration_pb2.Duration):
            Time offset relative to the beginning of the
            audio that corresponds to the start of the
            spoken word. This is an experimental feature and
            the accuracy of the time offset can vary.
        end_offset (google.protobuf.duration_pb2.Duration):
            Time offset relative to the beginning of the
            audio that corresponds to the end of the spoken
            word. This is an experimental feature and the
            accuracy of the time offset can vary.
        confidence (float):
            The Speech confidence between 0.0 and 1.0 for
            this word. A higher number indicates an
            estimated greater likelihood that the recognized
            word is correct. The default of 0.0 is a
            sentinel value indicating that confidence was
            not set.

            This field is not guaranteed to be fully stable
            over time for the same audio input. Users should
            also not rely on it to always be provided.
    """

    word: str = proto.Field(
        proto.STRING,
        number=3,
    )
    start_offset: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=1,
        message=duration_pb2.Duration,
    )
    end_offset: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=2,
        message=duration_pb2.Duration,
    )
    confidence: float = proto.Field(
        proto.FLOAT,
        number=4,
    )


class BargeInConfig(proto.Message):
    r"""Configuration of the barge-in behavior. Barge-in instructs the API
    to return a detected utterance at a proper time while the client is
    playing back the response audio from a previous request. When the
    client sees the utterance, it should stop the playback and
    immediately get ready for receiving the responses for the current
    request.

    The barge-in handling requires the client to start streaming audio
    input as soon as it starts playing back the audio from the previous
    response. The playback is modeled into two phases:

    - No barge-in phase: which goes first and during which speech
      detection should not be carried out.

    - Barge-in phase: which follows the no barge-in phase and during
      which the API starts speech detection and may inform the client
      that an utterance has been detected. Note that no-speech event is
      not expected in this phase.

    The client provides this configuration in terms of the durations of
    those two phases. The durations are measured in terms of the audio
    length from the start of the input audio.

    No-speech event is a response with END_OF_UTTERANCE without any
    transcript following up.

    Attributes:
        no_barge_in_duration (google.protobuf.duration_pb2.Duration):
            Duration that is not eligible for barge-in at
            the beginning of the input audio.
        total_duration (google.protobuf.duration_pb2.Duration):
            Total duration for the playback at the
            beginning of the input audio.
    """

    no_barge_in_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=1,
        message=duration_pb2.Duration,
    )
    total_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=2,
        message=duration_pb2.Duration,
    )


class InputAudioConfig(proto.Message):
    r"""Instructs the speech recognizer on how to process the audio
    content.

    Attributes:
        audio_encoding (google.cloud.dialogflowcx_v3beta1.types.AudioEncoding):
            Required. Audio encoding of the audio content
            to process.
        sample_rate_hertz (int):
            Sample rate (in Hertz) of the audio content sent in the
            query. Refer to `Cloud Speech API
            documentation <https://cloud.google.com/speech-to-text/docs/basics>`__
            for more details.
        enable_word_info (bool):
            Optional. If ``true``, Dialogflow returns
            [SpeechWordInfo][google.cloud.dialogflow.cx.v3beta1.SpeechWordInfo]
            in
            [StreamingRecognitionResult][google.cloud.dialogflow.cx.v3beta1.StreamingRecognitionResult]
            with information about the recognized speech words, e.g.
            start and end time offsets. If false or unspecified, Speech
            doesn't return any word-level information.
        phrase_hints (MutableSequence[str]):
            Optional. A list of strings containing words and phrases
            that the speech recognizer should recognize with higher
            likelihood.

            See `the Cloud Speech
            documentation <https://cloud.google.com/speech-to-text/docs/basics#phrase-hints>`__
            for more details.
        model (str):
            Optional. Which Speech model to select for the given
            request. For more information, see `Speech
            models <https://cloud.google.com/dialogflow/cx/docs/concept/speech-models>`__.
        model_variant (google.cloud.dialogflowcx_v3beta1.types.SpeechModelVariant):
            Optional. Which variant of the [Speech
            model][google.cloud.dialogflow.cx.v3beta1.InputAudioConfig.model]
            to use.
        single_utterance (bool):
            Optional. If ``false`` (default), recognition does not cease
            until the client closes the stream. If ``true``, the
            recognizer will detect a single spoken utterance in input
            audio. Recognition ceases when it detects the audio's voice
            has stopped or paused. In this case, once a detected intent
            is received, the client should close the stream and start a
            new request with a new stream as needed. Note: This setting
            is relevant only for streaming methods.
        barge_in_config (google.cloud.dialogflowcx_v3beta1.types.BargeInConfig):
            Configuration of barge-in behavior during the
            streaming of input audio.
        opt_out_conformer_model_migration (bool):
            If ``true``, the request will opt out for STT conformer
            model migration. This field will be deprecated once force
            migration takes place in June 2024. Please refer to
            `Dialogflow CX Speech model
            migration <https://cloud.google.com/dialogflow/cx/docs/concept/speech-model-migration>`__.
    """

    audio_encoding: "AudioEncoding" = proto.Field(
        proto.ENUM,
        number=1,
        enum="AudioEncoding",
    )
    sample_rate_hertz: int = proto.Field(
        proto.INT32,
        number=2,
    )
    enable_word_info: bool = proto.Field(
        proto.BOOL,
        number=13,
    )
    phrase_hints: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    model: str = proto.Field(
        proto.STRING,
        number=7,
    )
    model_variant: "SpeechModelVariant" = proto.Field(
        proto.ENUM,
        number=10,
        enum="SpeechModelVariant",
    )
    single_utterance: bool = proto.Field(
        proto.BOOL,
        number=8,
    )
    barge_in_config: "BargeInConfig" = proto.Field(
        proto.MESSAGE,
        number=15,
        message="BargeInConfig",
    )
    opt_out_conformer_model_migration: bool = proto.Field(
        proto.BOOL,
        number=26,
    )


class VoiceSelectionParams(proto.Message):
    r"""Description of which voice to use for speech synthesis.

    Attributes:
        name (str):
            Optional. The name of the voice. If not set, the service
            will choose a voice based on the other parameters such as
            language_code and
            [ssml_gender][google.cloud.dialogflow.cx.v3beta1.VoiceSelectionParams.ssml_gender].

            For the list of available voices, please refer to `Supported
            voices and
            languages <https://cloud.google.com/text-to-speech/docs/voices>`__.
        ssml_gender (google.cloud.dialogflowcx_v3beta1.types.SsmlVoiceGender):
            Optional. The preferred gender of the voice. If not set, the
            service will choose a voice based on the other parameters
            such as language_code and
            [name][google.cloud.dialogflow.cx.v3beta1.VoiceSelectionParams.name].
            Note that this is only a preference, not requirement. If a
            voice of the appropriate gender is not available, the
            synthesizer should substitute a voice with a different
            gender rather than failing the request.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    ssml_gender: "SsmlVoiceGender" = proto.Field(
        proto.ENUM,
        number=2,
        enum="SsmlVoiceGender",
    )


class SynthesizeSpeechConfig(proto.Message):
    r"""Configuration of how speech should be synthesized.

    Attributes:
        speaking_rate (float):
            Optional. Speaking rate/speed, in the range [0.25, 4.0]. 1.0
            is the normal native speed supported by the specific voice.
            2.0 is twice as fast, and 0.5 is half as fast. If
            unset(0.0), defaults to the native 1.0 speed. Any other
            values < 0.25 or > 4.0 will return an error.
        pitch (float):
            Optional. Speaking pitch, in the range [-20.0, 20.0]. 20
            means increase 20 semitones from the original pitch. -20
            means decrease 20 semitones from the original pitch.
        volume_gain_db (float):
            Optional. Volume gain (in dB) of the normal native volume
            supported by the specific voice, in the range [-96.0, 16.0].
            If unset, or set to a value of 0.0 (dB), will play at normal
            native signal amplitude. A value of -6.0 (dB) will play at
            approximately half the amplitude of the normal native signal
            amplitude. A value of +6.0 (dB) will play at approximately
            twice the amplitude of the normal native signal amplitude.
            We strongly recommend not to exceed +10 (dB) as there's
            usually no effective increase in loudness for any value
            greater than that.
        effects_profile_id (MutableSequence[str]):
            Optional. An identifier which selects 'audio
            effects' profiles that are applied on (post
            synthesized) text to speech. Effects are applied
            on top of each other in the order they are
            given.
        voice (google.cloud.dialogflowcx_v3beta1.types.VoiceSelectionParams):
            Optional. The desired voice of the
            synthesized audio.
    """

    speaking_rate: float = proto.Field(
        proto.DOUBLE,
        number=1,
    )
    pitch: float = proto.Field(
        proto.DOUBLE,
        number=2,
    )
    volume_gain_db: float = proto.Field(
        proto.DOUBLE,
        number=3,
    )
    effects_profile_id: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    voice: "VoiceSelectionParams" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="VoiceSelectionParams",
    )


class OutputAudioConfig(proto.Message):
    r"""Instructs the speech synthesizer how to generate the output
    audio content.

    Attributes:
        audio_encoding (google.cloud.dialogflowcx_v3beta1.types.OutputAudioEncoding):
            Required. Audio encoding of the synthesized
            audio content.
        sample_rate_hertz (int):
            Optional. The synthesis sample rate (in
            hertz) for this audio. If not provided, then the
            synthesizer will use the default sample rate
            based on the audio encoding. If this is
            different from the voice's natural sample rate,
            then the synthesizer will honor this request by
            converting to the desired sample rate (which
            might result in worse audio quality).
        synthesize_speech_config (google.cloud.dialogflowcx_v3beta1.types.SynthesizeSpeechConfig):
            Optional. Configuration of how speech should be synthesized.
            If not specified,
            [Agent.text_to_speech_settings][google.cloud.dialogflow.cx.v3beta1.Agent.text_to_speech_settings]
            is applied.
    """

    audio_encoding: "OutputAudioEncoding" = proto.Field(
        proto.ENUM,
        number=1,
        enum="OutputAudioEncoding",
    )
    sample_rate_hertz: int = proto.Field(
        proto.INT32,
        number=2,
    )
    synthesize_speech_config: "SynthesizeSpeechConfig" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="SynthesizeSpeechConfig",
    )


class TextToSpeechSettings(proto.Message):
    r"""Settings related to speech synthesizing.

    Attributes:
        synthesize_speech_configs (MutableMapping[str, google.cloud.dialogflowcx_v3beta1.types.SynthesizeSpeechConfig]):
            Configuration of how speech should be synthesized, mapping
            from language
            (https://cloud.google.com/dialogflow/cx/docs/reference/language)
            to SynthesizeSpeechConfig.

            These settings affect:

            - The `phone
              gateway <https://cloud.google.com/dialogflow/cx/docs/concept/integration/phone-gateway>`__
              synthesize configuration set via
              [Agent.text_to_speech_settings][google.cloud.dialogflow.cx.v3beta1.Agent.text_to_speech_settings].

            - How speech is synthesized when invoking
              [session][google.cloud.dialogflow.cx.v3beta1.Sessions]
              APIs.
              [Agent.text_to_speech_settings][google.cloud.dialogflow.cx.v3beta1.Agent.text_to_speech_settings]
              only applies if
              [OutputAudioConfig.synthesize_speech_config][google.cloud.dialogflow.cx.v3beta1.OutputAudioConfig.synthesize_speech_config]
              is not specified.
    """

    synthesize_speech_configs: MutableMapping[str, "SynthesizeSpeechConfig"] = (
        proto.MapField(
            proto.STRING,
            proto.MESSAGE,
            number=1,
            message="SynthesizeSpeechConfig",
        )
    )


__all__ = tuple(sorted(__protobuf__.manifest))
