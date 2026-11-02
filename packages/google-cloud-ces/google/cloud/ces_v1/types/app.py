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
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.ces_v1.types import bigquery_export, common
from google.cloud.ces_v1.types import schema as gcc_schema

__protobuf__ = proto.module(
    package="google.cloud.ces.v1",
    manifest={
        "App",
        "TimeZoneSettings",
        "LanguageSettings",
        "AudioProcessingConfig",
        "AmbientSoundConfig",
        "BargeInConfig",
        "SynthesizeSpeechConfig",
        "MetricAnalysisSettings",
        "LoggingSettings",
        "ErrorHandlingSettings",
        "EvaluationMetricsThresholds",
        "ClientCertificateSettings",
        "VpcScSettings",
        "ConversationLoggingSettings",
        "CloudLoggingSettings",
        "AudioRecordingConfig",
        "RedactionConfig",
        "DataStoreSettings",
    },
)


class App(proto.Message):
    r"""An app serves as a top-level container for a group of agents,
    including the root agent and its sub-agents, along with their
    associated configurations. These agents work together to achieve
    specific goals within the app's context.

    Attributes:
        name (str):
            Identifier. The unique identifier of the app. Format:
            ``projects/{project}/locations/{location}/apps/{app}``
        display_name (str):
            Required. Display name of the app.
        description (str):
            Optional. Human-readable description of the
            app.
        pinned (bool):
            Optional. Whether the app is pinned in the
            app list.
        root_agent (str):
            Optional. The root agent is the entry point of the app.
            Format:
            ``projects/{project}/locations/{location}/apps/{app}/agents/{agent}``
        language_settings (google.cloud.ces_v1.types.LanguageSettings):
            Optional. Language settings of the app.
        time_zone_settings (google.cloud.ces_v1.types.TimeZoneSettings):
            Optional. TimeZone settings of the app.
        audio_processing_config (google.cloud.ces_v1.types.AudioProcessingConfig):
            Optional. Audio processing configuration of
            the app.
        logging_settings (google.cloud.ces_v1.types.LoggingSettings):
            Optional. Logging settings of the app.
        error_handling_settings (google.cloud.ces_v1.types.ErrorHandlingSettings):
            Optional. Error handling settings of the app.
        model_settings (google.cloud.ces_v1.types.ModelSettings):
            Optional. The default LLM model settings for
            the app. Individual resources (e.g. agents,
            guardrails) can override these configurations as
            needed.
        tool_execution_mode (google.cloud.ces_v1.types.App.ToolExecutionMode):
            Optional. The tool execution mode for the
            app. If not provided, will default to PARALLEL.
        evaluation_metrics_thresholds (google.cloud.ces_v1.types.EvaluationMetricsThresholds):
            Optional. The evaluation thresholds for the
            app.
        variable_declarations (MutableSequence[google.cloud.ces_v1.types.App.VariableDeclaration]):
            Optional. The declarations of the variables.
        predefined_variable_declarations (MutableSequence[google.cloud.ces_v1.types.App.VariableDeclaration]):
            Output only. The declarations of predefined
            variables for the app.
        global_instruction (str):
            Optional. Instructions for all the agents in
            the app. You can use this instruction to set up
            a stable identity or personality across all the
            agents.
        guardrails (MutableSequence[str]):
            Optional. List of guardrails for the app. Format:
            ``projects/{project}/locations/{location}/apps/{app}/guardrails/{guardrail}``
        data_store_settings (google.cloud.ces_v1.types.DataStoreSettings):
            Optional. The data store settings for the
            app.
        default_channel_profile (google.cloud.ces_v1.types.ChannelProfile):
            Optional. The default channel profile used by
            the app.
        metadata (MutableMapping[str, str]):
            Optional. Metadata about the app. This field
            can be used to store additional information
            relevant to the app's details or intended
            usages.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the app was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the app was last
            updated.
        etag (str):
            Output only. Etag used to ensure the object
            hasn't changed during a read-modify-write
            operation. If the etag is empty, the update will
            overwrite any concurrent changes.
        deployment_count (int):
            Output only. Number of deployments in the
            app.
        client_certificate_settings (google.cloud.ces_v1.types.ClientCertificateSettings):
            Optional. The default client certificate
            settings for the app.
        vpc_sc_settings (google.cloud.ces_v1.types.VpcScSettings):
            Optional. VPC-SC settings for the app.
        locked (bool):
            Optional. Indicates whether the app is locked
            for changes. If the app is locked, modifications
            to the app resources will be rejected.
        validation_errors (MutableSequence[str]):
            Output only. Misconfigurations or warnings in
            the app.
    """

    class ToolExecutionMode(proto.Enum):
        r"""Defines the tool execution behavior if there are **multiple** tools
        being selected by the agent **at the same time**.

        Values:
            TOOL_EXECUTION_MODE_UNSPECIFIED (0):
                Unspecified tool execution mode. Default to
                PARALLEL.
            PARALLEL (1):
                If there are multiple tools being selected, they will be
                executed in parallel, with the same
                `ToolContext <https://google.github.io/adk-docs/context/#the-different-types-of-context>`__.
            SEQUENTIAL (2):
                If there are multiple tools being selected, they will be
                executed sequentially. The next tool will only be executed
                after the previous tool completes and it can see updated
                `ToolContext <https://google.github.io/adk-docs/context/#the-different-types-of-context>`__
                from the previous tool.
        """

        TOOL_EXECUTION_MODE_UNSPECIFIED = 0
        PARALLEL = 1
        SEQUENTIAL = 2

    class VariableDeclaration(proto.Message):
        r"""Defines the structure and metadata for a variable.

        Attributes:
            name (str):
                Required. The name of the variable. The name
                must start with a letter or underscore and
                contain only letters, numbers, or underscores.
            description (str):
                Required. The description of the variable.
            schema (google.cloud.ces_v1.types.Schema):
                Required. The schema of the variable.
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        description: str = proto.Field(
            proto.STRING,
            number=2,
        )
        schema: gcc_schema.Schema = proto.Field(
            proto.MESSAGE,
            number=3,
            message=gcc_schema.Schema,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    pinned: bool = proto.Field(
        proto.BOOL,
        number=31,
    )
    root_agent: str = proto.Field(
        proto.STRING,
        number=4,
    )
    language_settings: "LanguageSettings" = proto.Field(
        proto.MESSAGE,
        number=18,
        message="LanguageSettings",
    )
    time_zone_settings: "TimeZoneSettings" = proto.Field(
        proto.MESSAGE,
        number=27,
        message="TimeZoneSettings",
    )
    audio_processing_config: "AudioProcessingConfig" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="AudioProcessingConfig",
    )
    logging_settings: "LoggingSettings" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="LoggingSettings",
    )
    error_handling_settings: "ErrorHandlingSettings" = proto.Field(
        proto.MESSAGE,
        number=34,
        message="ErrorHandlingSettings",
    )
    model_settings: common.ModelSettings = proto.Field(
        proto.MESSAGE,
        number=13,
        message=common.ModelSettings,
    )
    tool_execution_mode: ToolExecutionMode = proto.Field(
        proto.ENUM,
        number=32,
        enum=ToolExecutionMode,
    )
    evaluation_metrics_thresholds: "EvaluationMetricsThresholds" = proto.Field(
        proto.MESSAGE,
        number=24,
        message="EvaluationMetricsThresholds",
    )
    variable_declarations: MutableSequence[VariableDeclaration] = proto.RepeatedField(
        proto.MESSAGE,
        number=14,
        message=VariableDeclaration,
    )
    predefined_variable_declarations: MutableSequence[VariableDeclaration] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=28,
            message=VariableDeclaration,
        )
    )
    global_instruction: str = proto.Field(
        proto.STRING,
        number=17,
    )
    guardrails: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=10,
    )
    data_store_settings: "DataStoreSettings" = proto.Field(
        proto.MESSAGE,
        number=15,
        message="DataStoreSettings",
    )
    default_channel_profile: common.ChannelProfile = proto.Field(
        proto.MESSAGE,
        number=22,
        message=common.ChannelProfile,
    )
    metadata: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=11,
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
    etag: str = proto.Field(
        proto.STRING,
        number=12,
    )
    deployment_count: int = proto.Field(
        proto.INT32,
        number=23,
    )
    client_certificate_settings: "ClientCertificateSettings" = proto.Field(
        proto.MESSAGE,
        number=25,
        message="ClientCertificateSettings",
    )
    vpc_sc_settings: "VpcScSettings" = proto.Field(
        proto.MESSAGE,
        number=26,
        message="VpcScSettings",
    )
    locked: bool = proto.Field(
        proto.BOOL,
        number=29,
    )
    validation_errors: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=39,
    )


class TimeZoneSettings(proto.Message):
    r"""TimeZone settings of the app.

    Attributes:
        time_zone (str):
            Optional. The time zone of the app from the `time zone
            database <https://www.iana.org/time-zones>`__, e.g.,
            America/Los_Angeles, Europe/Paris.
    """

    time_zone: str = proto.Field(
        proto.STRING,
        number=1,
    )


class LanguageSettings(proto.Message):
    r"""Language settings of the app.

    Attributes:
        default_language_code (str):
            Optional. The default language code of the
            app.
        supported_language_codes (MutableSequence[str]):
            Optional. List of languages codes supported by the app, in
            addition to the ``default_language_code``.
        enable_multilingual_support (bool):
            Optional. Enables multilingual support. If
            true, agents in the app will use pre-built
            instructions to improve handling of multilingual
            input.
        fallback_action (str):
            Optional. Deprecated: This feature is no longer supported.
            Use ``enable_multilingual_support`` instead to improve
            handling of multilingual input. The action to perform when
            an agent receives input in an unsupported language.

            This can be a predefined action or a custom tool call. Valid
            values are:

            - A tool's full resource name, which triggers a specific
              tool execution.
            - A predefined system action, such as "escalate" or "exit",
              which triggers an
              [EndSession][google.cloud.ces.v1.EndSession] signal with
              corresponding
              [metadata][google.cloud.ces.v1.EndSession.metadata] to
              terminate the conversation.
    """

    default_language_code: str = proto.Field(
        proto.STRING,
        number=1,
    )
    supported_language_codes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    enable_multilingual_support: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    fallback_action: str = proto.Field(
        proto.STRING,
        number=4,
    )


class AudioProcessingConfig(proto.Message):
    r"""Configuration for how the input and output audio should be
    processed and delivered.

    Attributes:
        synthesize_speech_configs (MutableMapping[str, google.cloud.ces_v1.types.SynthesizeSpeechConfig]):
            Optional. Configuration of how the agent response should be
            synthesized, mapping from the language code to
            [SynthesizeSpeechConfig][google.cloud.ces.v1.SynthesizeSpeechConfig].

            If the configuration for the specified language code is not
            found, the configuration for the root language code will be
            used. For example, if the map contains "en-us" and "en", and
            the specified language code is "en-gb", then "en"
            configuration will be used.

            Note: Language code is case-insensitive.
        barge_in_config (google.cloud.ces_v1.types.BargeInConfig):
            Optional. Configures the agent behavior for
            the user barge-in activities.
        inactivity_timeout (google.protobuf.duration_pb2.Duration):
            Optional. The duration of user inactivity (no
            speech or interaction) before the agent prompts
            the user for reengagement. If not set, the agent
            will not prompt the user for reengagement.
        ambient_sound_config (google.cloud.ces_v1.types.AmbientSoundConfig):
            Optional. Configuration for the ambient sound
            to be played with the synthesized agent
            response, to enhance the naturalness of the
            conversation.
    """

    synthesize_speech_configs: MutableMapping[str, "SynthesizeSpeechConfig"] = (
        proto.MapField(
            proto.STRING,
            proto.MESSAGE,
            number=1,
            message="SynthesizeSpeechConfig",
        )
    )
    barge_in_config: "BargeInConfig" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="BargeInConfig",
    )
    inactivity_timeout: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=4,
        message=duration_pb2.Duration,
    )
    ambient_sound_config: "AmbientSoundConfig" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="AmbientSoundConfig",
    )


class AmbientSoundConfig(proto.Message):
    r"""Configuration for the ambient sound to be played with the
    synthesized agent response, to enhance the naturalness of the
    conversation.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        prebuilt_ambient_noise (google.cloud.ces_v1.types.AmbientSoundConfig.PrebuiltAmbientNoise):
            Optional. Deprecated: ``prebuilt_ambient_noise`` is
            deprecated in favor of ``prebuilt_ambient_sound``.

            This field is a member of `oneof`_ ``source``.
        gcs_uri (str):
            Optional. Ambient noise as a mono-channel, 16kHz WAV file
            stored in `Cloud
            Storage <https://cloud.google.com/storage>`__.

            Note: Please make sure the CES service agent
            ``service-<PROJECT-NUMBER>@gcp-sa-ces.iam.gserviceaccount.com``
            has ``storage.objects.get`` permission to the Cloud Storage
            object.

            This field is a member of `oneof`_ ``source``.
        prebuilt_ambient_sound (str):
            Optional. Name of the prebuilt ambient sound. Valid values
            are:

            - "coffee_shop"
            - "keyboard"
            - "keypad"
            - "hum"
            - "office_1"
            - "office_2"
            - "office_3"
            - "room_1"
            - "room_2"
            - "room_3"
            - "room_4"
            - "room_5"
            - "air_conditioner".

            This field is a member of `oneof`_ ``source``.
        volume_gain_db (float):
            Optional. Volume gain (in dB) of the normal native volume
            supported by ambient noise, in the range [-96.0, 16.0]. If
            unset, or set to a value of 0.0 (dB), will play at normal
            native signal amplitude. A value of -6.0 (dB) will play at
            approximately half the amplitude of the normal native signal
            amplitude. A value of +6.0 (dB) will play at approximately
            twice the amplitude of the normal native signal amplitude.
            We strongly recommend not to exceed +10 (dB) as there's
            usually no effective increase in loudness for any value
            greater than that.
    """

    class PrebuiltAmbientNoise(proto.Enum):
        r"""Prebuilt ambient noise.

        Values:
            PREBUILT_AMBIENT_NOISE_UNSPECIFIED (0):
                Not specified.
            RETAIL_STORE (1):
                Ambient noise of a retail store.
            CONVENTION_HALL (2):
                Ambient noise of a convention hall.
            OUTDOOR (3):
                Ambient noise of a street.
        """

        PREBUILT_AMBIENT_NOISE_UNSPECIFIED = 0
        RETAIL_STORE = 1
        CONVENTION_HALL = 2
        OUTDOOR = 3

    prebuilt_ambient_noise: PrebuiltAmbientNoise = proto.Field(
        proto.ENUM,
        number=1,
        oneof="source",
        enum=PrebuiltAmbientNoise,
    )
    gcs_uri: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="source",
    )
    prebuilt_ambient_sound: str = proto.Field(
        proto.STRING,
        number=4,
        oneof="source",
    )
    volume_gain_db: float = proto.Field(
        proto.DOUBLE,
        number=3,
    )


class BargeInConfig(proto.Message):
    r"""Configuration for how the user barge-in activities should be
    handled.

    Attributes:
        disable_barge_in (bool):
            Optional. Deprecated: ``disable_barge_in`` is deprecated in
            favor of
            [``disable_barge_in_control``][google.cloud.ces.v1.ChannelProfile.disable_barge_in_control]
            in ChannelProfile.

            Disables user barge-in while the agent is speaking. If true,
            user input during agent response playback will be ignored.
        barge_in_awareness (bool):
            Optional. If enabled, the agent will adapt
            its next response based on the assumption that
            the user hasn't heard the full preceding agent
            message. This should not be used in scenarios
            where agent responses are displayed visually.
    """

    disable_barge_in: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    barge_in_awareness: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class SynthesizeSpeechConfig(proto.Message):
    r"""Configuration for how the agent response should be
    synthesized.

    Attributes:
        voice (str):
            Optional. The name of the voice. If not set, the service
            will choose a voice based on the other parameters such as
            language_code.

            For the list of available voices, please refer to `Supported
            voices and
            languages <https://cloud.google.com/text-to-speech/docs/voices>`__
            from Cloud Text-to-Speech.
        voice_sample_gcs_uri (str):
            Optional. The Cloud Storage URI to the audio sample for
            voice cloning. The audio sample should be a mono-channel,
            24kHz WAV file.

            Note: Please make sure the CES service agent
            ``service-<PROJECT-NUMBER>@gcp-sa-ces.iam.gserviceaccount.com``
            has ``storage.objects.get`` permission to the Cloud Storage
            object.
        speaking_rate (float):
            Optional. The speaking rate/speed in the range [0.25, 2.0].
            1.0 is the normal native speed supported by the specific
            voice. 2.0 is twice as fast, and 0.5 is half as fast. Values
            outside of the range [0.25, 2.0] will return an error.
        model (str):
            Optional. The model used to synthesize audio.
            Currently supported values:

            - "gemini-3.1-flash-tts-preview"
            If empty, Chirp3-HD is used.
        instruction (str):
            Optional. The instruction used to synthesize
            speech when using a generative model.
    """

    voice: str = proto.Field(
        proto.STRING,
        number=1,
    )
    voice_sample_gcs_uri: str = proto.Field(
        proto.STRING,
        number=3,
    )
    speaking_rate: float = proto.Field(
        proto.DOUBLE,
        number=2,
    )
    model: str = proto.Field(
        proto.STRING,
        number=4,
    )
    instruction: str = proto.Field(
        proto.STRING,
        number=5,
    )


class MetricAnalysisSettings(proto.Message):
    r"""Settings to describe the conversation data collection
    behaviors for LLM analysis metrics pipeline.

    Attributes:
        llm_metrics_opted_out (bool):
            Optional. Whether to collect conversation
            data for llm analysis metrics. If true,
            conversation data will not be collected for llm
            analysis metrics; otherwise, conversation data
            will be collected.
    """

    llm_metrics_opted_out: bool = proto.Field(
        proto.BOOL,
        number=1,
    )


class LoggingSettings(proto.Message):
    r"""Settings to describe the logging behaviors for the app.

    Attributes:
        redaction_config (google.cloud.ces_v1.types.RedactionConfig):
            Optional. Configuration for how sensitive
            data should be redacted.
        audio_recording_config (google.cloud.ces_v1.types.AudioRecordingConfig):
            Optional. Configuration for how audio interactions should be
            recorded. The audio is subject to redaction as configured in
            [RedactionConfig][google.cloud.ces.v1.LoggingSettings.redaction_config].
        unredacted_audio_recording_config (google.cloud.ces_v1.types.AudioRecordingConfig):
            Optional. Configures an additional recording of unredacted
            audio. This can be used to maintain a raw audio copy when
            audio redaction is
            [enabled][google.cloud.ces.v1.RedactionConfig.enable_redaction],
            typically for auditing or monitoring purposes.
        bigquery_export_settings (google.cloud.ces_v1.types.BigQueryExportSettings):
            Optional. Configures the BigQuery export behaviors for the
            app. The conversation data is subject to redaction as
            configured in
            [RedactionConfig][google.cloud.ces.v1.LoggingSettings.redaction_config].
        unredacted_bigquery_export_settings (google.cloud.ces_v1.types.BigQueryExportSettings):
            Optional. Configures the BigQuery export
            behaviors for the app. The unredacted
            conversation data will be exported to BigQuery
            tables if it is enabled.
        cloud_logging_settings (google.cloud.ces_v1.types.CloudLoggingSettings):
            Optional. Settings to describe the Cloud
            Logging behaviors for the app.
        conversation_logging_settings (google.cloud.ces_v1.types.ConversationLoggingSettings):
            Optional. Settings to describe the
            conversation logging behaviors for the app.
        evaluation_audio_recording_config (google.cloud.ces_v1.types.AudioRecordingConfig):
            Optional. Configuration for how audio
            interactions should be recorded for the
            evaluation. By default, audio recording is not
            enabled for evaluation sessions.
        metric_analysis_settings (google.cloud.ces_v1.types.MetricAnalysisSettings):
            Optional. Settings to describe the
            conversation data collection behaviors for the
            LLM analysis pipeline for the app.
    """

    redaction_config: "RedactionConfig" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="RedactionConfig",
    )
    audio_recording_config: "AudioRecordingConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="AudioRecordingConfig",
    )
    unredacted_audio_recording_config: "AudioRecordingConfig" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="AudioRecordingConfig",
    )
    bigquery_export_settings: bigquery_export.BigQueryExportSettings = proto.Field(
        proto.MESSAGE,
        number=3,
        message=bigquery_export.BigQueryExportSettings,
    )
    unredacted_bigquery_export_settings: bigquery_export.BigQueryExportSettings = (
        proto.Field(
            proto.MESSAGE,
            number=9,
            message=bigquery_export.BigQueryExportSettings,
        )
    )
    cloud_logging_settings: "CloudLoggingSettings" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="CloudLoggingSettings",
    )
    conversation_logging_settings: "ConversationLoggingSettings" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="ConversationLoggingSettings",
    )
    evaluation_audio_recording_config: "AudioRecordingConfig" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="AudioRecordingConfig",
    )
    metric_analysis_settings: "MetricAnalysisSettings" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="MetricAnalysisSettings",
    )


class ErrorHandlingSettings(proto.Message):
    r"""Settings to describe how errors should be handled in the app.

    Attributes:
        error_handling_strategy (google.cloud.ces_v1.types.ErrorHandlingSettings.ErrorHandlingStrategy):
            Optional. The strategy to use for error
            handling.
        fallback_response_config (google.cloud.ces_v1.types.ErrorHandlingSettings.FallbackResponseConfig):
            Optional. Configuration for handling fallback
            responses.
        end_session_config (google.cloud.ces_v1.types.ErrorHandlingSettings.EndSessionConfig):
            Optional. Configuration for ending the
            session in case of system errors (e.g. LLM
            errors).
    """

    class ErrorHandlingStrategy(proto.Enum):
        r"""Defines the strategy for handling errors.

        Values:
            ERROR_HANDLING_STRATEGY_UNSPECIFIED (0):
                Unspecified error handling strategy.
            NONE (1):
                No specific handling is enabled.
            FALLBACK_RESPONSE (2):
                A fallback message will be returned to the
                user in case of system errors (e.g. LLM errors).
            END_SESSION (3):
                An [EndSession][google.cloud.ces.v1.EndSession] signal will
                be emitted in case of system errors (e.g. LLM errors).
        """

        ERROR_HANDLING_STRATEGY_UNSPECIFIED = 0
        NONE = 1
        FALLBACK_RESPONSE = 2
        END_SESSION = 3

    class FallbackResponseConfig(proto.Message):
        r"""Configuration for handling fallback responses.

        Attributes:
            custom_fallback_messages (MutableMapping[str, str]):
                Optional. The fallback messages in case of system errors
                (e.g. LLM errors), mapped by `supported language
                code <https://docs.cloud.google.com/customer-engagement-ai/conversational-agents/ps/reference/language>`__.
            max_fallback_attempts (int):
                Optional. The maximum number of fallback attempts to make
                before the agent emitting
                [EndSession][google.cloud.ces.v1.EndSession] Signal.
        """

        custom_fallback_messages: MutableMapping[str, str] = proto.MapField(
            proto.STRING,
            proto.STRING,
            number=1,
        )
        max_fallback_attempts: int = proto.Field(
            proto.INT32,
            number=2,
        )

    class EndSessionConfig(proto.Message):
        r"""Configuration for ending the session in case of system errors
        (e.g. LLM errors).


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            escalate_session (bool):
                Optional. Whether to escalate the session in
                [EndSession][google.cloud.ces.v1.EndSession]. If session is
                escalated, [metadata in
                EndSession][google.cloud.ces.v1.EndSession.metadata] will
                contain ``session_escalated = true``. See
                https://docs.cloud.google.com/customer-engagement-ai/conversational-agents/ps/deploy/google-telephony-platform#transfer_a_call_to_a_human_agent
                for details.

                This field is a member of `oneof`_ ``_escalate_session``.
        """

        escalate_session: bool = proto.Field(
            proto.BOOL,
            number=1,
            optional=True,
        )

    error_handling_strategy: ErrorHandlingStrategy = proto.Field(
        proto.ENUM,
        number=1,
        enum=ErrorHandlingStrategy,
    )
    fallback_response_config: FallbackResponseConfig = proto.Field(
        proto.MESSAGE,
        number=2,
        message=FallbackResponseConfig,
    )
    end_session_config: EndSessionConfig = proto.Field(
        proto.MESSAGE,
        number=3,
        message=EndSessionConfig,
    )


class EvaluationMetricsThresholds(proto.Message):
    r"""Threshold settings for metrics in an Evaluation.

    Attributes:
        golden_evaluation_metrics_thresholds (google.cloud.ces_v1.types.EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds):
            Optional. The golden evaluation metrics
            thresholds.
        hallucination_metric_behavior (google.cloud.ces_v1.types.EvaluationMetricsThresholds.HallucinationMetricBehavior):
            Optional. Deprecated: Use
            ``golden_hallucination_metric_behavior`` instead. The
            hallucination metric behavior is currently used for golden
            evaluations.
        golden_hallucination_metric_behavior (google.cloud.ces_v1.types.EvaluationMetricsThresholds.HallucinationMetricBehavior):
            Optional. The hallucination metric behavior
            for golden evaluations.
        scenario_hallucination_metric_behavior (google.cloud.ces_v1.types.EvaluationMetricsThresholds.HallucinationMetricBehavior):
            Optional. The hallucination metric behavior
            for scenario evaluations.
    """

    class HallucinationMetricBehavior(proto.Enum):
        r"""The hallucination metric behavior. Regardless of the
        behavior, the metric will always be calculated. The difference
        is that when disabled, the metric is not used to calculate the
        overall evaluation score.

        Values:
            HALLUCINATION_METRIC_BEHAVIOR_UNSPECIFIED (0):
                Unspecified hallucination metric behavior.
            DISABLED (1):
                Disable hallucination metric.
            ENABLED (2):
                Enable hallucination metric.
        """

        HALLUCINATION_METRIC_BEHAVIOR_UNSPECIFIED = 0
        DISABLED = 1
        ENABLED = 2

    class GoldenEvaluationMetricsThresholds(proto.Message):
        r"""Settings for golden evaluations.

        Attributes:
            turn_level_metrics_thresholds (google.cloud.ces_v1.types.EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.TurnLevelMetricsThresholds):
                Optional. The turn level metrics thresholds.
            expectation_level_metrics_thresholds (google.cloud.ces_v1.types.EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.ExpectationLevelMetricsThresholds):
                Optional. The expectation level metrics
                thresholds.
            tool_matching_settings (google.cloud.ces_v1.types.EvaluationMetricsThresholds.ToolMatchingSettings):
                Optional. The tool matching settings. An
                extra tool call is a tool call that is present
                in the execution but does not match any tool
                call in the golden expectation.
        """

        class TurnLevelMetricsThresholds(proto.Message):
            r"""Turn level metrics thresholds.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                semantic_similarity_success_threshold (int):
                    Optional. The success threshold for semantic
                    similarity. Must be an integer between 0 and 4.
                    Default is >= 3.

                    This field is a member of `oneof`_ ``_semantic_similarity_success_threshold``.
                overall_tool_invocation_correctness_threshold (float):
                    Optional. The success threshold for overall
                    tool invocation correctness. Must be a float
                    between 0 and 1. Default is 1.0.

                    This field is a member of `oneof`_ ``_overall_tool_invocation_correctness_threshold``.
                semantic_similarity_channel (google.cloud.ces_v1.types.EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.TurnLevelMetricsThresholds.SemanticSimilarityChannel):
                    Optional. The semantic similarity channel to
                    use for evaluation.
            """

            class SemanticSimilarityChannel(proto.Enum):
                r"""Semantic similarity channel to use.

                Values:
                    SEMANTIC_SIMILARITY_CHANNEL_UNSPECIFIED (0):
                        Metric unspecified. Defaults to TEXT.
                    TEXT (1):
                        Use text semantic similarity.
                    AUDIO (2):
                        Use audio semantic similarity.
                """

                SEMANTIC_SIMILARITY_CHANNEL_UNSPECIFIED = 0
                TEXT = 1
                AUDIO = 2

            semantic_similarity_success_threshold: int = proto.Field(
                proto.INT32,
                number=1,
                optional=True,
            )
            overall_tool_invocation_correctness_threshold: float = proto.Field(
                proto.FLOAT,
                number=2,
                optional=True,
            )
            semantic_similarity_channel: "EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.TurnLevelMetricsThresholds.SemanticSimilarityChannel" = proto.Field(
                proto.ENUM,
                number=3,
                enum="EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.TurnLevelMetricsThresholds.SemanticSimilarityChannel",
            )

        class ExpectationLevelMetricsThresholds(proto.Message):
            r"""Expectation level metrics thresholds.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                tool_invocation_parameter_correctness_threshold (float):
                    Optional. The success threshold for
                    individual tool invocation parameter
                    correctness. Must be a float between 0 and 1.
                    Default is 1.0.

                    This field is a member of `oneof`_ ``_tool_invocation_parameter_correctness_threshold``.
            """

            tool_invocation_parameter_correctness_threshold: float = proto.Field(
                proto.FLOAT,
                number=1,
                optional=True,
            )

        turn_level_metrics_thresholds: "EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.TurnLevelMetricsThresholds" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.TurnLevelMetricsThresholds",
        )
        expectation_level_metrics_thresholds: "EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.ExpectationLevelMetricsThresholds" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.ExpectationLevelMetricsThresholds",
        )
        tool_matching_settings: "EvaluationMetricsThresholds.ToolMatchingSettings" = (
            proto.Field(
                proto.MESSAGE,
                number=3,
                message="EvaluationMetricsThresholds.ToolMatchingSettings",
            )
        )

    class ToolMatchingSettings(proto.Message):
        r"""Settings for matching tool calls.

        Attributes:
            extra_tool_call_behavior (google.cloud.ces_v1.types.EvaluationMetricsThresholds.ToolMatchingSettings.ExtraToolCallBehavior):
                Optional. Behavior for extra tool calls.
                Defaults to FAIL.
        """

        class ExtraToolCallBehavior(proto.Enum):
            r"""Defines the behavior when an extra tool call is encountered.
            An extra tool call is a tool call that is present in the
            execution but does not match any tool call in the golden
            expectation.

            Values:
                EXTRA_TOOL_CALL_BEHAVIOR_UNSPECIFIED (0):
                    Unspecified behavior. Defaults to FAIL.
                FAIL (1):
                    Fail the evaluation if an extra tool call is
                    encountered.
                ALLOW (2):
                    Allow the extra tool call.
            """

            EXTRA_TOOL_CALL_BEHAVIOR_UNSPECIFIED = 0
            FAIL = 1
            ALLOW = 2

        extra_tool_call_behavior: "EvaluationMetricsThresholds.ToolMatchingSettings.ExtraToolCallBehavior" = proto.Field(
            proto.ENUM,
            number=1,
            enum="EvaluationMetricsThresholds.ToolMatchingSettings.ExtraToolCallBehavior",
        )

    golden_evaluation_metrics_thresholds: GoldenEvaluationMetricsThresholds = (
        proto.Field(
            proto.MESSAGE,
            number=1,
            message=GoldenEvaluationMetricsThresholds,
        )
    )
    hallucination_metric_behavior: HallucinationMetricBehavior = proto.Field(
        proto.ENUM,
        number=3,
        enum=HallucinationMetricBehavior,
    )
    golden_hallucination_metric_behavior: HallucinationMetricBehavior = proto.Field(
        proto.ENUM,
        number=5,
        enum=HallucinationMetricBehavior,
    )
    scenario_hallucination_metric_behavior: HallucinationMetricBehavior = proto.Field(
        proto.ENUM,
        number=4,
        enum=HallucinationMetricBehavior,
    )


class ClientCertificateSettings(proto.Message):
    r"""Settings for custom client certificates.

    Attributes:
        tls_certificate (str):
            Required. The TLS certificate encoded in PEM
            format. This string must include the begin
            header and end footer lines.
        private_key (str):
            Required. The name of the SecretManager secret version
            resource storing the private key encoded in PEM format.
            Format:
            ``projects/{project}/secrets/{secret}/versions/{version}``
        passphrase (str):
            Optional. The name of the SecretManager secret version
            resource storing the passphrase to decrypt the private key.
            Should be left unset if the private key is not encrypted.
            Format:
            ``projects/{project}/secrets/{secret}/versions/{version}``
    """

    tls_certificate: str = proto.Field(
        proto.STRING,
        number=1,
    )
    private_key: str = proto.Field(
        proto.STRING,
        number=2,
    )
    passphrase: str = proto.Field(
        proto.STRING,
        number=3,
    )


class VpcScSettings(proto.Message):
    r"""VPC-SC settings for the app.

    Attributes:
        allowed_origins (MutableSequence[str]):
            Optional. The allowed HTTP(s) origins that
            OpenAPI tools in the App are able to directly
            call when VPC Service Controls are enabled.
            These strings must match the origin exactly,
            including the port if specified. For example,
            "https://example.com" or
            "https://example.com:443". This list does not
            yet apply to Python tools that may make direct
            HTTP calls.
    """

    allowed_origins: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class ConversationLoggingSettings(proto.Message):
    r"""Settings to describe the conversation logging behaviors for
    the app.

    Attributes:
        disable_conversation_logging (bool):
            Optional. Whether to disable conversation
            logging for the sessions.
        retention_window (google.protobuf.duration_pb2.Duration):
            Optional. Controls the retention window for
            the conversation. If not set, the conversation
            will be retained for 365 days.
    """

    disable_conversation_logging: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    retention_window: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=2,
        message=duration_pb2.Duration,
    )


class CloudLoggingSettings(proto.Message):
    r"""Settings to describe the Cloud Logging behaviors for the app.

    Attributes:
        enable_cloud_logging (bool):
            Optional. Whether to enable Cloud Logging for
            the sessions.
    """

    enable_cloud_logging: bool = proto.Field(
        proto.BOOL,
        number=1,
    )


class AudioRecordingConfig(proto.Message):
    r"""Configuration for how the audio interactions should be
    recorded.

    Attributes:
        gcs_bucket (str):
            Optional. The `Cloud
            Storage <https://cloud.google.com/storage>`__ bucket to
            store the session audio recordings. The URI must start with
            "gs://".

            Please choose a bucket location that meets your data
            residency requirements.

            Note: If the Cloud Storage bucket is in a different project
            from the app, you should grant ``storage.objects.create``
            permission to the CES service agent
            ``service-<PROJECT-NUMBER>@gcp-sa-ces.iam.gserviceaccount.com``.
        gcs_path_prefix (str):
            Optional. The Cloud Storage path prefix for audio
            recordings.

            This prefix can include the following placeholders, which
            will be dynamically substituted at serving time:

            - $project: project ID
            - $location: app location
            - $app: app ID
            - $date: session date in YYYY-MM-DD format
            - $session: session ID

            If the path prefix is not specified, the default prefix
            ``$project/$location/$app/$date/$session/`` will be used.
    """

    gcs_bucket: str = proto.Field(
        proto.STRING,
        number=1,
    )
    gcs_path_prefix: str = proto.Field(
        proto.STRING,
        number=2,
    )


class RedactionConfig(proto.Message):
    r"""Configuration to instruct how sensitive data should be
    handled.

    Attributes:
        enable_redaction (bool):
            Optional. If true, redaction will be applied
            in various logging scenarios, including
            conversation history, Cloud Logging and audio
            recording.
        inspect_template (str):
            Optional. `DLP <https://cloud.google.com/dlp/docs>`__
            inspect template name to configure detection of sensitive
            data types.

            Format:
            ``projects/{project}/locations/{location}/inspectTemplates/{inspect_template}``
        deidentify_template (str):
            Optional. `DLP <https://cloud.google.com/dlp/docs>`__
            deidentify template name to instruct on how to de-identify
            content.

            Format:
            ``projects/{project}/locations/{location}/deidentifyTemplates/{deidentify_template}``
    """

    enable_redaction: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    inspect_template: str = proto.Field(
        proto.STRING,
        number=2,
    )
    deidentify_template: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DataStoreSettings(proto.Message):
    r"""Data store related settings for the app.

    Attributes:
        engines (MutableSequence[google.cloud.ces_v1.types.DataStoreSettings.Engine]):
            Output only. The engines for the app.
    """

    class Engine(proto.Message):
        r"""An engine to which the data stores are connected.
        See Vertex AI Search:

        https://cloud.google.com/generative-ai-app-builder/docs/enterprise-search-introduction.

        Attributes:
            name (str):
                Output only. The resource name of the engine. Format:
                ``projects/{project}/locations/{location}/collections/{collection}/engines/{engine}``
            type_ (google.cloud.ces_v1.types.DataStoreSettings.Engine.Type):
                Output only. The type of the engine.
        """

        class Type(proto.Enum):
            r"""The type of the engine.
            See the documentation available at
            https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/SolutionType
            and
            https://cloud.google.com/generative-ai-app-builder/docs/create-datastore-ingest.

            Values:
                TYPE_UNSPECIFIED (0):
                    Unspecified engine type.
                ENGINE_TYPE_SEARCH (1):
                    The SOLUTION_TYPE_SEARCH engine for the app. All connector
                    data stores added to the app will be added to this engine.
                ENGINE_TYPE_CHAT (2):
                    Chat engine type. The SOLUTION_TYPE_CHAT engine for the app.
                    All connector data stores added to the app will be added to
                    this engine.
            """

            TYPE_UNSPECIFIED = 0
            ENGINE_TYPE_SEARCH = 1
            ENGINE_TYPE_CHAT = 2

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        type_: "DataStoreSettings.Engine.Type" = proto.Field(
            proto.ENUM,
            number=2,
            enum="DataStoreSettings.Engine.Type",
        )

    engines: MutableSequence[Engine] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=Engine,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
