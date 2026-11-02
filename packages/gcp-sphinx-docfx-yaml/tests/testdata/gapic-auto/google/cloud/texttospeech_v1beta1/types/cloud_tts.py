# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
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
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.texttospeech.v1beta1",
    manifest={
        "SsmlVoiceGender",
        "AudioEncoding",
        "ListVoicesRequest",
        "ListVoicesResponse",
        "Voice",
        "SynthesizeSpeechRequest",
        "SynthesisInput",
        "VoiceSelectionParams",
        "AudioConfig",
        "CustomVoiceParams",
        "SynthesizeSpeechResponse",
        "Timepoint",
    },
)


class SsmlVoiceGender(proto.Enum):
    r"""Gender of the voice as described in `SSML voice
    element <https://www.w3.org/TR/speech-synthesis11/#edef_voice>`__.
    """

    SSML_VOICE_GENDER_UNSPECIFIED = 0
    MALE = 1
    FEMALE = 2
    NEUTRAL = 3


class AudioEncoding(proto.Enum):
    r"""Configuration to set up audio encoder. The encoding
    determines the output audio format that we'd like.
    """

    AUDIO_ENCODING_UNSPECIFIED = 0
    LINEAR16 = 1
    MP3 = 2
    MP3_64_KBPS = 4
    OGG_OPUS = 3
    MULAW = 5
    ALAW = 6


class ListVoicesRequest(proto.Message):
    r"""The top-level message sent by the client for the ``ListVoices``
    method.

    Attributes:
        language_code (str):
            Optional. Recommended.
            `BCP-47 <https://www.rfc-editor.org/rfc/bcp/bcp47.txt>`__
            language tag. If not specified, the API will return all
            supported voices. If specified, the ListVoices call will
            only return voices that can be used to synthesize this
            language_code. For example, if you specify ``"en-NZ"``, all
            ``"en-NZ"`` voices will be returned. If you specify
            ``"no"``, both ``"no-\*"`` (Norwegian) and ``"nb-\*"``
            (Norwegian Bokmal) voices will be returned.
    """

    language_code = proto.Field(
        proto.STRING,
        number=1,
    )


class ListVoicesResponse(proto.Message):
    r"""The message returned to the client by the ``ListVoices`` method.

    Attributes:
        voices (Sequence[google.cloud.texttospeech_v1beta1.types.Voice]):
            The list of voices.
    """

    voices = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Voice",
    )


class Voice(proto.Message):
    r"""Description of a voice supported by the TTS service.

    Attributes:
        language_codes (Sequence[str]):
            The languages that this voice supports, expressed as
            `BCP-47 <https://www.rfc-editor.org/rfc/bcp/bcp47.txt>`__
            language tags (e.g. "en-US", "es-419", "cmn-tw").
        name (str):
            The name of this voice.  Each distinct voice
            has a unique name.
        ssml_gender (google.cloud.texttospeech_v1beta1.types.SsmlVoiceGender):
            The gender of this voice.
        natural_sample_rate_hertz (int):
            The natural sample rate (in hertz) for this
            voice.
    """

    language_codes = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    name = proto.Field(
        proto.STRING,
        number=2,
    )
    ssml_gender = proto.Field(
        proto.ENUM,
        number=3,
        enum="SsmlVoiceGender",
    )
    natural_sample_rate_hertz = proto.Field(
        proto.INT32,
        number=4,
    )


class SynthesizeSpeechRequest(proto.Message):
    r"""The top-level message sent by the client for the
    ``SynthesizeSpeech`` method.

    Attributes:
        input (google.cloud.texttospeech_v1beta1.types.SynthesisInput):
            Required. The Synthesizer requires either
            plain text or SSML as input.
        voice (google.cloud.texttospeech_v1beta1.types.VoiceSelectionParams):
            Required. The desired voice of the
            synthesized audio.
        audio_config (google.cloud.texttospeech_v1beta1.types.AudioConfig):
            Required. The configuration of the
            synthesized audio.
        enable_time_pointing (Sequence[google.cloud.texttospeech_v1beta1.types.SynthesizeSpeechRequest.TimepointType]):
            Whether and what timepoints are returned in
            the response.
    """

    class TimepointType(proto.Enum):
        r"""The type of timepoint information that is returned in the
        response.
        """

        TIMEPOINT_TYPE_UNSPECIFIED = 0
        SSML_MARK = 1

    input = proto.Field(
        proto.MESSAGE,
        number=1,
        message="SynthesisInput",
    )
    voice = proto.Field(
        proto.MESSAGE,
        number=2,
        message="VoiceSelectionParams",
    )
    audio_config = proto.Field(
        proto.MESSAGE,
        number=3,
        message="AudioConfig",
    )
    enable_time_pointing = proto.RepeatedField(
        proto.ENUM,
        number=4,
        enum=TimepointType,
    )


class SynthesisInput(proto.Message):
    r"""Contains text input to be synthesized. Either ``text`` or ``ssml``
    must be supplied. Supplying both or neither returns
    [google.rpc.Code.INVALID_ARGUMENT][]. The input size is limited to
    5000 characters.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        text (str):
            The raw text to be synthesized.

            This field is a member of `oneof`_ ``input_source``.
        ssml (str):
            The SSML document to be synthesized. The SSML document must
            be valid and well-formed. Otherwise the RPC will fail and
            return [google.rpc.Code.INVALID_ARGUMENT][]. For more
            information, see
            `SSML <https://cloud.google.com/text-to-speech/docs/ssml>`__.

            This field is a member of `oneof`_ ``input_source``.
    """

    text = proto.Field(
        proto.STRING,
        number=1,
        oneof="input_source",
    )
    ssml = proto.Field(
        proto.STRING,
        number=2,
        oneof="input_source",
    )


class VoiceSelectionParams(proto.Message):
    r"""Description of which voice to use for a synthesis request.

    Attributes:
        language_code (str):
            Required. The language (and potentially also the region) of
            the voice expressed as a
            `BCP-47 <https://www.rfc-editor.org/rfc/bcp/bcp47.txt>`__
            language tag, e.g. "en-US". This should not include a script
            tag (e.g. use "cmn-cn" rather than "cmn-Hant-cn"), because
            the script will be inferred from the input provided in the
            SynthesisInput. The TTS service will use this parameter to
            help choose an appropriate voice. Note that the TTS service
            may choose a voice with a slightly different language code
            than the one selected; it may substitute a different region
            (e.g. using en-US rather than en-CA if there isn't a
            Canadian voice available), or even a different language,
            e.g. using "nb" (Norwegian Bokmal) instead of "no"
            (Norwegian)".
        name (str):
            The name of the voice. If not set, the service will choose a
            voice based on the other parameters such as language_code
            and gender.
        ssml_gender (google.cloud.texttospeech_v1beta1.types.SsmlVoiceGender):
            The preferred gender of the voice. If not set, the service
            will choose a voice based on the other parameters such as
            language_code and name. Note that this is only a preference,
            not requirement; if a voice of the appropriate gender is not
            available, the synthesizer should substitute a voice with a
            different gender rather than failing the request.
        custom_voice (google.cloud.texttospeech_v1beta1.types.CustomVoiceParams):
            The configuration for a custom voice. If
            [CustomVoiceParams.model] is set, the service will choose
            the custom voice matching the specified configuration.
    """

    language_code = proto.Field(
        proto.STRING,
        number=1,
    )
    name = proto.Field(
        proto.STRING,
        number=2,
    )
    ssml_gender = proto.Field(
        proto.ENUM,
        number=3,
        enum="SsmlVoiceGender",
    )
    custom_voice = proto.Field(
        proto.MESSAGE,
        number=4,
        message="CustomVoiceParams",
    )


class AudioConfig(proto.Message):
    r"""Description of audio data to be synthesized.

    Attributes:
        audio_encoding (google.cloud.texttospeech_v1beta1.types.AudioEncoding):
            Required. The format of the audio byte
            stream.
        speaking_rate (float):
            Optional. Input only. Speaking rate/speed, in the range
            [0.25, 4.0]. 1.0 is the normal native speed supported by the
            specific voice. 2.0 is twice as fast, and 0.5 is half as
            fast. If unset(0.0), defaults to the native 1.0 speed. Any
            other values < 0.25 or > 4.0 will return an error.
        pitch (float):
            Optional. Input only. Speaking pitch, in the range [-20.0,
            20.0]. 20 means increase 20 semitones from the original
            pitch. -20 means decrease 20 semitones from the original
            pitch.
        volume_gain_db (float):
            Optional. Input only. Volume gain (in dB) of the normal
            native volume supported by the specific voice, in the range
            [-96.0, 16.0]. If unset, or set to a value of 0.0 (dB), will
            play at normal native signal amplitude. A value of -6.0 (dB)
            will play at approximately half the amplitude of the normal
            native signal amplitude. A value of +6.0 (dB) will play at
            approximately twice the amplitude of the normal native
            signal amplitude. Strongly recommend not to exceed +10 (dB)
            as there's usually no effective increase in loudness for any
            value greater than that.
        sample_rate_hertz (int):
            Optional. The synthesis sample rate (in hertz) for this
            audio. When this is specified in SynthesizeSpeechRequest, if
            this is different from the voice's natural sample rate, then
            the synthesizer will honor this request by converting to the
            desired sample rate (which might result in worse audio
            quality), unless the specified sample rate is not supported
            for the encoding chosen, in which case it will fail the
            request and return [google.rpc.Code.INVALID_ARGUMENT][].
        effects_profile_id (Sequence[str]):
            Optional. Input only. An identifier which selects 'audio
            effects' profiles that are applied on (post synthesized)
            text to speech. Effects are applied on top of each other in
            the order they are given. See `audio
            profiles <https://cloud.google.com/text-to-speech/docs/audio-profiles>`__
            for current supported profile ids.
    """

    audio_encoding = proto.Field(
        proto.ENUM,
        number=1,
        enum="AudioEncoding",
    )
    speaking_rate = proto.Field(
        proto.DOUBLE,
        number=2,
    )
    pitch = proto.Field(
        proto.DOUBLE,
        number=3,
    )
    volume_gain_db = proto.Field(
        proto.DOUBLE,
        number=4,
    )
    sample_rate_hertz = proto.Field(
        proto.INT32,
        number=5,
    )
    effects_profile_id = proto.RepeatedField(
        proto.STRING,
        number=6,
    )


class CustomVoiceParams(proto.Message):
    r"""Description of the custom voice to be synthesized.

    Attributes:
        model (str):
            Required. The name of the AutoML model that
            synthesizes the custom voice.
        reported_usage (google.cloud.texttospeech_v1beta1.types.CustomVoiceParams.ReportedUsage):
            Optional. The usage of the synthesized audio
            to be reported.
    """

    class ReportedUsage(proto.Enum):
        r"""The usage of the synthesized audio. You must report your
        honest and correct usage of the service as it's regulated by
        contract and will cause significant difference in billing.
        """

        REPORTED_USAGE_UNSPECIFIED = 0
        REALTIME = 1
        OFFLINE = 2

    model = proto.Field(
        proto.STRING,
        number=1,
    )
    reported_usage = proto.Field(
        proto.ENUM,
        number=3,
        enum=ReportedUsage,
    )


class SynthesizeSpeechResponse(proto.Message):
    r"""The message returned to the client by the ``SynthesizeSpeech``
    method.

    Attributes:
        audio_content (bytes):
            The audio data bytes encoded as specified in the request,
            including the header for encodings that are wrapped in
            containers (e.g. MP3, OGG_OPUS). For LINEAR16 audio, we
            include the WAV header. Note: as with all bytes fields,
            protobuffers use a pure binary representation, whereas JSON
            representations use base64.
        timepoints (Sequence[google.cloud.texttospeech_v1beta1.types.Timepoint]):
            A link between a position in the original request input and
            a corresponding time in the output audio. It's only
            supported via ``<mark>`` of SSML input.
        audio_config (google.cloud.texttospeech_v1beta1.types.AudioConfig):
            The audio metadata of ``audio_content``.
    """

    audio_content = proto.Field(
        proto.BYTES,
        number=1,
    )
    timepoints = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="Timepoint",
    )
    audio_config = proto.Field(
        proto.MESSAGE,
        number=4,
        message="AudioConfig",
    )


class Timepoint(proto.Message):
    r"""This contains a mapping between a certain point in the input
    text and a corresponding time in the output audio.

    Attributes:
        mark_name (str):
            Timepoint name as received from the client within ``<mark>``
            tag.
        time_seconds (float):
            Time offset in seconds from the start of the
            synthesized audio.
    """

    mark_name = proto.Field(
        proto.STRING,
        number=4,
    )
    time_seconds = proto.Field(
        proto.DOUBLE,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
