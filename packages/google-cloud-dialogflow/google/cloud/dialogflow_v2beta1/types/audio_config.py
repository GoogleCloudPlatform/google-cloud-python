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
    package="google.cloud.dialogflow.v2beta1",
    manifest={
        "TelephonyDtmf",
        "AudioEncoding",
        "SpeechModelVariant",
        "SsmlVoiceGender",
        "OutputAudioEncoding",
        "SpeechContext",
        "SpeechWordInfo",
        "BargeInConfig",
        "InputAudioConfig",
        "VoiceSelectionParams",
        "SynthesizeSpeechConfig",
        "CustomPronunciationParams",
        "OutputAudioConfig",
        "TelephonyDtmfEvents",
        "SpeechToTextConfig",
    },
)


class TelephonyDtmf(proto.Enum):
    r"""`DTMF <https://en.wikipedia.org/wiki/Dual-tone_multi-frequency_signaling>`__
    digit in Telephony Gateway.

    Values:
        TELEPHONY_DTMF_UNSPECIFIED (0):
            Not specified. This value may be used to
            indicate an absent digit.
        DTMF_ONE (1):
            Number: '1'.
        DTMF_TWO (2):
            Number: '2'.
        DTMF_THREE (3):
            Number: '3'.
        DTMF_FOUR (4):
            Number: '4'.
        DTMF_FIVE (5):
            Number: '5'.
        DTMF_SIX (6):
            Number: '6'.
        DTMF_SEVEN (7):
            Number: '7'.
        DTMF_EIGHT (8):
            Number: '8'.
        DTMF_NINE (9):
            Number: '9'.
        DTMF_ZERO (10):
            Number: '0'.
        DTMF_A (11):
            Letter: 'A'.
        DTMF_B (12):
            Letter: 'B'.
        DTMF_C (13):
            Letter: 'C'.
        DTMF_D (14):
            Letter: 'D'.
        DTMF_STAR (15):
            Asterisk/star: '\*'.
        DTMF_POUND (16):
            Pound/diamond/hash/square/gate/octothorpe:
            '#'.
    """

    TELEPHONY_DTMF_UNSPECIFIED = 0
    DTMF_ONE = 1
    DTMF_TWO = 2
    DTMF_THREE = 3
    DTMF_FOUR = 4
    DTMF_FIVE = 5
    DTMF_SIX = 6
    DTMF_SEVEN = 7
    DTMF_EIGHT = 8
    DTMF_NINE = 9
    DTMF_ZERO = 10
    DTMF_A = 11
    DTMF_B = 12
    DTMF_C = 13
    DTMF_D = 14
    DTMF_STAR = 15
    DTMF_POUND = 16


class AudioEncoding(proto.Enum):
    r"""Audio encoding of the audio content sent in the conversational query
    request. Refer to the `Cloud Speech API
    documentation <https://cloud.google.com/speech-to-text/docs/basics>`__
    for more details.

    Values:
        AUDIO_ENCODING_UNSPECIFIED (0):
            Not specified.
        AUDIO_ENCODING_LINEAR_16 (1):
            Uncompressed 16-bit signed little-endian
            samples (Linear PCM).
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
    model][google.cloud.dialogflow.v2beta1.InputAudioConfig.model] to
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

            Please see the `Dialogflow
            docs <https://cloud.google.com/dialogflow/docs/data-logging>`__
            for how to make your project eligible for enhanced models.
        USE_STANDARD (2):
            Use standard model variant even if an enhanced model is
            available. See the `Cloud Speech
            documentation <https://cloud.google.com/speech-to-text/docs/enhanced-models>`__
            for details about enhanced models.
        USE_ENHANCED (3):
            Use an enhanced model variant:

            - If an enhanced variant does not exist for the given
              [model][google.cloud.dialogflow.v2beta1.InputAudioConfig.model]
              and request language, Dialogflow falls back to the
              standard variant.

              The `Cloud Speech
              documentation <https://cloud.google.com/speech-to-text/docs/enhanced-models>`__
              describes which models have enhanced variants.

            - If the API caller isn't eligible for enhanced models,
              Dialogflow returns an error. Please see the `Dialogflow
              docs <https://cloud.google.com/dialogflow/docs/data-logging>`__
              for how to make your project eligible.
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
            Uncompressed 16-bit signed little-endian
            samples (Linear PCM). Audio content returned as
            LINEAR16 also contains a WAV header.
        OUTPUT_AUDIO_ENCODING_MP3 (2):
            MP3 audio at 64kbps.
        OUTPUT_AUDIO_ENCODING_MP3_64_KBPS (4):
            MP3 audio at 64kbps.
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


class SpeechContext(proto.Message):
    r"""Hints for the speech recognizer to help with recognition in a
    specific conversation state.

    Attributes:
        phrases (MutableSequence[str]):
            Optional. A list of strings containing words and phrases
            that the speech recognizer should recognize with higher
            likelihood.

            This list can be used to:

            - improve accuracy for words and phrases you expect the user
              to say, e.g. typical commands for your Dialogflow agent
            - add additional words to the speech recognizer vocabulary
            - ...

            See the `Cloud Speech
            documentation <https://cloud.google.com/speech-to-text/quotas>`__
            for usage limits.
        boost (float):
            Optional. Boost for this context compared to other contexts:

            - If the boost is positive, Dialogflow will increase the
              probability that the phrases in this context are
              recognized over similar sounding phrases.
            - If the boost is unspecified or non-positive, Dialogflow
              will not apply any boost.

            Dialogflow recommends that you use boosts in the range (0,
            20] and that you find a value that fits your use case with
            binary search.
    """

    phrases: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    boost: float = proto.Field(
        proto.FLOAT,
        number=2,
    )


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

    The flow goes like below:

    ::

       --> Time

       without speech detection  | utterance only | utterance or no-speech event
                                 |                |
                 +-------------+ | +------------+ | +---------------+
       ----------+ no barge-in +-|-+  barge-in  +-|-+ normal period +-----------
                 +-------------+ | +------------+ | +---------------+

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


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        audio_encoding (google.cloud.dialogflow_v2beta1.types.AudioEncoding):
            Required. Audio encoding of the audio content
            to process.
        sample_rate_hertz (int):
            Required. Sample rate (in Hertz) of the audio content sent
            in the query. Refer to `Cloud Speech API
            documentation <https://cloud.google.com/speech-to-text/docs/basics>`__
            for more details.
        language_code (str):
            Required. The language of the supplied audio. Dialogflow
            does not do translations. See `Language
            Support <https://cloud.google.com/dialogflow/docs/reference/language>`__
            for a list of the currently supported language codes. Note
            that queries in the same session do not necessarily need to
            specify the same language. If not set, the language is
            inferred from the
            [ConversationProfile.stt_config][google.cloud.dialogflow.v2beta1.ConversationProfile.stt_config].
        enable_word_info (bool):
            If ``true``, Dialogflow returns
            [SpeechWordInfo][google.cloud.dialogflow.v2beta1.SpeechWordInfo]
            in
            [StreamingRecognitionResult][google.cloud.dialogflow.v2beta1.StreamingRecognitionResult]
            with information about the recognized speech words, e.g.
            start and end time offsets. If false or unspecified, Speech
            doesn't return any word-level information.
        phrase_hints (MutableSequence[str]):
            A list of strings containing words and phrases that the
            speech recognizer should recognize with higher likelihood.

            See `the Cloud Speech
            documentation <https://cloud.google.com/speech-to-text/docs/basics#phrase-hints>`__
            for more details.

            This field is deprecated. Please use
            ```speech_contexts`` <>`__ instead. If you specify both
            ```phrase_hints`` <>`__ and ```speech_contexts`` <>`__,
            Dialogflow will treat the ```phrase_hints`` <>`__ as a
            single additional ```SpeechContext`` <>`__.
        speech_contexts (MutableSequence[google.cloud.dialogflow_v2beta1.types.SpeechContext]):
            Context information to assist speech recognition.

            See `the Cloud Speech
            documentation <https://cloud.google.com/speech-to-text/docs/basics#phrase-hints>`__
            for more details.
        model (str):
            Optional. Which Speech model to select for the given
            request. For more information, see `Speech
            models <https://cloud.google.com/dialogflow/es/docs/speech-models>`__.
        model_variant (google.cloud.dialogflow_v2beta1.types.SpeechModelVariant):
            Which variant of the [Speech
            model][google.cloud.dialogflow.v2beta1.InputAudioConfig.model]
            to use.
        single_utterance (bool):
            If ``false`` (default), recognition does not cease until the
            client closes the stream. If ``true``, the recognizer will
            detect a single spoken utterance in input audio. Recognition
            ceases when it detects the audio's voice has stopped or
            paused. In this case, once a detected intent is received,
            the client should close the stream and start a new request
            with a new stream as needed. Note: This setting is relevant
            only for streaming methods. Note: When specified,
            InputAudioConfig.single_utterance takes precedence over
            StreamingDetectIntentRequest.single_utterance.
        enable_voice_activity_events (bool):
            Optional. If ``true``, responses with voice activity speech
            events will be returned as they are detected. Note: This
            setting is relevant only for streaming methods.
        disable_no_speech_recognized_event (bool):
            Only used in
            [Participants.AnalyzeContent][google.cloud.dialogflow.v2beta1.Participants.AnalyzeContent]
            and
            [Participants.StreamingAnalyzeContent][google.cloud.dialogflow.v2beta1.Participants.StreamingAnalyzeContent].
            If ``false`` and recognition doesn't return any result,
            trigger ``NO_SPEECH_RECOGNIZED`` event to Dialogflow agent.
        barge_in_config (google.cloud.dialogflow_v2beta1.types.BargeInConfig):
            Configuration of barge-in behavior during the
            streaming of input audio.
        enable_automatic_punctuation (bool):
            Enable automatic punctuation option at the
            speech backend.
        default_no_speech_timeout (google.protobuf.duration_pb2.Duration):
            If set, use this no-speech timeout when the
            agent does not provide a no-speech timeout
            itself.
        phrase_sets (MutableSequence[str]):
            A collection of phrase set resources to use
            for speech adaptation.
        opt_out_conformer_model_migration (bool):
            If ``true``, the request will opt out for STT conformer
            model migration. This field will be deprecated once force
            migration takes place in June 2024. Please refer to
            `Dialogflow ES Speech model
            migration <https://cloud.google.com/dialogflow/es/docs/speech-model-migration>`__.
        gemini_asr_config (google.cloud.dialogflow_v2beta1.types.SpeechToTextConfig.GeminiAsrConfig):
            Optional. Configuration for using Gemini ASR models served
            via Vertex AI. This field is only used when
            ``use_gemini_asr`` is true.
        use_gemini_asr (bool):
            Optional. If true, Gemini ASR will be used
            for transcription instead of Cloud
            Speech-to-Text. If false, Cloud Speech-to-Text
            will be used. If unset, this setting is
            inherited from the ConversationProfile.

            This field is a member of `oneof`_ ``_use_gemini_asr``.
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
    language_code: str = proto.Field(
        proto.STRING,
        number=3,
    )
    enable_word_info: bool = proto.Field(
        proto.BOOL,
        number=13,
    )
    phrase_hints: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    speech_contexts: MutableSequence["SpeechContext"] = proto.RepeatedField(
        proto.MESSAGE,
        number=11,
        message="SpeechContext",
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
    enable_voice_activity_events: bool = proto.Field(
        proto.BOOL,
        number=27,
    )
    disable_no_speech_recognized_event: bool = proto.Field(
        proto.BOOL,
        number=14,
    )
    barge_in_config: "BargeInConfig" = proto.Field(
        proto.MESSAGE,
        number=15,
        message="BargeInConfig",
    )
    enable_automatic_punctuation: bool = proto.Field(
        proto.BOOL,
        number=17,
    )
    default_no_speech_timeout: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=18,
        message=duration_pb2.Duration,
    )
    phrase_sets: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=20,
    )
    opt_out_conformer_model_migration: bool = proto.Field(
        proto.BOOL,
        number=26,
    )
    gemini_asr_config: "SpeechToTextConfig.GeminiAsrConfig" = proto.Field(
        proto.MESSAGE,
        number=30,
        message="SpeechToTextConfig.GeminiAsrConfig",
    )
    use_gemini_asr: bool = proto.Field(
        proto.BOOL,
        number=31,
        optional=True,
    )


class VoiceSelectionParams(proto.Message):
    r"""Description of which voice to use for speech synthesis.

    Attributes:
        name (str):
            Optional. The name of the voice. If not set, the service
            will choose a voice based on the other parameters such as
            language_code and
            [ssml_gender][google.cloud.dialogflow.v2beta1.VoiceSelectionParams.ssml_gender].

            For the list of available voices, please refer to `Supported
            voices and
            languages <https://cloud.google.com/text-to-speech/docs/voices>`__.
        ssml_gender (google.cloud.dialogflow_v2beta1.types.SsmlVoiceGender):
            Optional. The preferred gender of the voice. If not set, the
            service will choose a voice based on the other parameters
            such as language_code and
            [name][google.cloud.dialogflow.v2beta1.VoiceSelectionParams.name].
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
        voice (google.cloud.dialogflow_v2beta1.types.VoiceSelectionParams):
            Optional. The desired voice of the
            synthesized audio.
        pronunciations (MutableSequence[google.cloud.dialogflow_v2beta1.types.CustomPronunciationParams]):
            Optional. The custom pronunciations for the
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
    pronunciations: MutableSequence["CustomPronunciationParams"] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message="CustomPronunciationParams",
    )


class CustomPronunciationParams(proto.Message):
    r"""Pronunciation customization for a phrase.

    Attributes:
        phrase (str):
            The phrase to which the customization is
            applied. The phrase can be multiple words, such
            as proper nouns, but shouldn't span the length
            of the sentence.
        phonetic_encoding (google.cloud.dialogflow_v2beta1.types.CustomPronunciationParams.PhoneticEncoding):
            The phonetic encoding of the phrase.
        pronunciation (str):
            The pronunciation of the phrase. This must be
            in the phonetic encoding specified above.
    """

    class PhoneticEncoding(proto.Enum):
        r"""The phonetic encoding of the phrase.

        Values:
            PHONETIC_ENCODING_UNSPECIFIED (0):
                Not specified.
            PHONETIC_ENCODING_IPA (1):
                IPA, such as apple -> ˈæpəl.
                https://en.wikipedia.org/wiki/International_Phonetic_Alphabet
            PHONETIC_ENCODING_X_SAMPA (2):
                X-SAMPA, such as apple -> "{p@l".
                https://en.wikipedia.org/wiki/X-SAMPA
        """

        PHONETIC_ENCODING_UNSPECIFIED = 0
        PHONETIC_ENCODING_IPA = 1
        PHONETIC_ENCODING_X_SAMPA = 2

    phrase: str = proto.Field(
        proto.STRING,
        number=1,
    )
    phonetic_encoding: PhoneticEncoding = proto.Field(
        proto.ENUM,
        number=2,
        enum=PhoneticEncoding,
    )
    pronunciation: str = proto.Field(
        proto.STRING,
        number=3,
    )


class OutputAudioConfig(proto.Message):
    r"""Instructs the speech synthesizer how to generate the output
    audio content. If this audio config is supplied in a request, it
    overrides all existing text-to-speech settings applied to the
    agent.

    Attributes:
        audio_encoding (google.cloud.dialogflow_v2beta1.types.OutputAudioEncoding):
            Required. Audio encoding of the synthesized
            audio content.
        sample_rate_hertz (int):
            The synthesis sample rate (in hertz) for this
            audio. If not provided, then the synthesizer
            will use the default sample rate based on the
            audio encoding. If this is different from the
            voice's natural sample rate, then the
            synthesizer will honor this request by
            converting to the desired sample rate (which
            might result in worse audio quality).
        synthesize_speech_config (google.cloud.dialogflow_v2beta1.types.SynthesizeSpeechConfig):
            Configuration of how speech should be
            synthesized.
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


class TelephonyDtmfEvents(proto.Message):
    r"""A wrapper of repeated TelephonyDtmf digits.

    Attributes:
        dtmf_events (MutableSequence[google.cloud.dialogflow_v2beta1.types.TelephonyDtmf]):
            A sequence of TelephonyDtmf digits.
    """

    dtmf_events: MutableSequence["TelephonyDtmf"] = proto.RepeatedField(
        proto.ENUM,
        number=1,
        enum="TelephonyDtmf",
    )


class SpeechToTextConfig(proto.Message):
    r"""Configures speech transcription for
    [ConversationProfile][google.cloud.dialogflow.v2beta1.ConversationProfile].

    Attributes:
        speech_model_variant (google.cloud.dialogflow_v2beta1.types.SpeechModelVariant):
            The speech model used in speech to text.
            ``SPEECH_MODEL_VARIANT_UNSPECIFIED``, ``USE_BEST_AVAILABLE``
            will be treated as ``USE_ENHANCED``. It can be overridden in
            [AnalyzeContentRequest][google.cloud.dialogflow.v2beta1.AnalyzeContentRequest]
            and
            [StreamingAnalyzeContentRequest][google.cloud.dialogflow.v2beta1.StreamingAnalyzeContentRequest]
            request. If enhanced model variant is specified and an
            enhanced version of the specified model for the language
            does not exist, then it would emit an error.
        model (str):
            Which Speech model to select. Select the model best suited
            to your domain to get best results. If a model is not
            explicitly specified, then Dialogflow auto-selects a model
            based on other parameters in the SpeechToTextConfig and
            Agent settings. If enhanced speech model is enabled for the
            agent and an enhanced version of the specified model for the
            language does not exist, then the speech is recognized using
            the standard version of the specified model. Refer to `Cloud
            Speech API
            documentation <https://cloud.google.com/speech-to-text/docs/basics#select-model>`__
            for more details. If you specify a model, the following
            models typically have the best performance:

            - phone_call (best for Agent Assist and telephony)
            - latest_short (best for Dialogflow non-telephony)
            - command_and_search

            Leave this field unspecified to use `Agent Speech
            settings <https://cloud.google.com/dialogflow/cx/docs/concept/agent#settings-speech>`__
            for model selection.
        phrase_sets (MutableSequence[str]):
            List of names of Cloud Speech phrase sets that are used for
            transcription. For phrase set limitations, please refer to
            `Cloud Speech API quotas and
            limits <https://cloud.google.com/speech-to-text/quotas#content>`__.
        audio_encoding (google.cloud.dialogflow_v2beta1.types.AudioEncoding):
            Audio encoding of the audio content to
            process.
        sample_rate_hertz (int):
            Sample rate (in Hertz) of the audio content sent in the
            query. Refer to `Cloud Speech API
            documentation <https://cloud.google.com/speech-to-text/docs/basics>`__
            for more details.
        language_code (str):
            The language of the supplied audio. Dialogflow does not do
            translations. See `Language
            Support <https://cloud.google.com/dialogflow/docs/reference/language>`__
            for a list of the currently supported language codes. Note
            that queries in the same session do not necessarily need to
            specify the same language. If not specified, the default
            language configured at
            [ConversationProfile][google.cloud.dialogflow.v2beta1.ConversationProfile]
            is used.
        enable_word_info (bool):
            If ``true``, Dialogflow returns
            [SpeechWordInfo][google.cloud.dialogflow.v2beta1.SpeechWordInfo]
            in
            [StreamingRecognitionResult][google.cloud.dialogflow.v2beta1.StreamingRecognitionResult]
            with information about the recognized speech words, e.g.
            start and end time offsets. If false or unspecified, Speech
            doesn't return any word-level information.
        use_timeout_based_endpointing (bool):
            Use timeout based endpointing, interpreting
            endpointer sensitivity as seconds of timeout
            value.
        gemini_asr_config (google.cloud.dialogflow_v2beta1.types.SpeechToTextConfig.GeminiAsrConfig):
            Optional. Configuration for using Gemini ASR models served
            via Vertex AI, overriding the default Gemini ASR model or
            providing additional advanced parameters. This field is only
            used when ``use_gemini_asr`` is true.
        use_gemini_asr (bool):
            Optional. If true, Gemini ASR will be used
            for transcription instead of Cloud
            Speech-to-Text.
    """

    class GeminiAsrConfig(proto.Message):
        r"""Configuration for using Gemini ASR models served via Vertex
        AI. This message is used to override the default Gemini ASR
        model or provide additional advanced parameters.

        Attributes:
            model_id (str):
                Optional. The Gemini ASR model ID used for
                transcription. This value overrides the default
                model ID configured on the server. Example:
                "gemini-3-flash-lite-asr-preview".
            silence_duration_ms (int):
                Optional. The required duration of detected
                silence (or non-speech) before end-of-speech is
                committed.
            prefix_padding_ms (int):
                Optional. The required duration of detected
                speech before start-of-speech is committed.
            start_of_speech_sensitivity (google.cloud.dialogflow_v2beta1.types.SpeechToTextConfig.GeminiAsrConfig.StartSensitivity):
                Optional. Start of speech sensitivity.
            end_of_speech_sensitivity (google.cloud.dialogflow_v2beta1.types.SpeechToTextConfig.GeminiAsrConfig.EndSensitivity):
                Optional. End of speech sensitivity.
        """

        class StartSensitivity(proto.Enum):
            r"""Start of speech sensitivity.

            Values:
                START_SENSITIVITY_UNSPECIFIED (0):
                    The default is START_SENSITIVITY_LOW.
                START_SENSITIVITY_HIGH (1):
                    Automatic detection will detect the start of
                    speech more often.
                START_SENSITIVITY_LOW (2):
                    Automatic detection will detect the start of
                    speech less often.
            """

            START_SENSITIVITY_UNSPECIFIED = 0
            START_SENSITIVITY_HIGH = 1
            START_SENSITIVITY_LOW = 2

        class EndSensitivity(proto.Enum):
            r"""End of speech sensitivity.

            Values:
                END_SENSITIVITY_UNSPECIFIED (0):
                    The default is END_SENSITIVITY_LOW.
                END_SENSITIVITY_HIGH (1):
                    Automatic detection ends speech more often.
                END_SENSITIVITY_LOW (2):
                    Automatic detection ends speech less often.
            """

            END_SENSITIVITY_UNSPECIFIED = 0
            END_SENSITIVITY_HIGH = 1
            END_SENSITIVITY_LOW = 2

        model_id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        silence_duration_ms: int = proto.Field(
            proto.INT32,
            number=2,
        )
        prefix_padding_ms: int = proto.Field(
            proto.INT32,
            number=3,
        )
        start_of_speech_sensitivity: "SpeechToTextConfig.GeminiAsrConfig.StartSensitivity" = proto.Field(
            proto.ENUM,
            number=4,
            enum="SpeechToTextConfig.GeminiAsrConfig.StartSensitivity",
        )
        end_of_speech_sensitivity: "SpeechToTextConfig.GeminiAsrConfig.EndSensitivity" = proto.Field(
            proto.ENUM,
            number=5,
            enum="SpeechToTextConfig.GeminiAsrConfig.EndSensitivity",
        )

    speech_model_variant: "SpeechModelVariant" = proto.Field(
        proto.ENUM,
        number=1,
        enum="SpeechModelVariant",
    )
    model: str = proto.Field(
        proto.STRING,
        number=2,
    )
    phrase_sets: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    audio_encoding: "AudioEncoding" = proto.Field(
        proto.ENUM,
        number=6,
        enum="AudioEncoding",
    )
    sample_rate_hertz: int = proto.Field(
        proto.INT32,
        number=7,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=8,
    )
    enable_word_info: bool = proto.Field(
        proto.BOOL,
        number=9,
    )
    use_timeout_based_endpointing: bool = proto.Field(
        proto.BOOL,
        number=11,
    )
    gemini_asr_config: GeminiAsrConfig = proto.Field(
        proto.MESSAGE,
        number=15,
        message=GeminiAsrConfig,
    )
    use_gemini_asr: bool = proto.Field(
        proto.BOOL,
        number=16,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
